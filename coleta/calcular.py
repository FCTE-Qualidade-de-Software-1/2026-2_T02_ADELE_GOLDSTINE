"""Cálculo de M13, M14 e do resumo de desempenho a partir dos registros brutos.

Lê os arquivos JSONL gravados por ``sigaa_coleta.py`` e produz:

- ``dados/brutos/flexibilidade/navegadores.csv`` (formato das Planilhas de Coleta);
- ``dados/brutos/flexibilidade/paginas-adaptadas.csv`` (idem);
- ``dados/consolidados/desempenho.csv`` (estatísticas por cenário e tarefa);
- as linhas de M13 e M14 em ``dados/consolidados/metricas.csv`` (substituídas a cada execução).

Uso: ``python coleta/calcular.py``. O cálculo é determinístico: rodar de novo sobre os
mesmos registros produz os mesmos arquivos.
"""

from __future__ import annotations

import csv
import json
import statistics as st
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "dados/brutos"
CONSOLIDADOS = RAIZ / "dados/consolidados"
AVALIADOR = "Arthur"
TAREFAS = ["T1", "T2", "T3", "T4", "T5", "T6"]
LARGURA = {"celular_360": 360, "tablet_768": 768}
COMBINACOES_M13 = 24  # 6 tarefas x 4 navegadores (ficha de M13)
PAGINAS = {  # página final de cada tarefa (caminho principal da Fase 1)
    "T1": "Relatório de notas do aluno",
    "T2": "Portal do Discente (Turmas do Semestre)",
    "T3": "Atestado de matrícula",
    "T4": "Índices acadêmicos",
    "T5": "Turma Virtual (página inicial da turma, com os materiais)",
    "T6": "Calendário acadêmico 2026.2",
}

# Revisão visual do critério (c): pares apontados pelo detector automático que, na
# conferência das capturas, não são sobreposição de texto (ver docs/fase-4/flexibilidade.md).
# Formato: (tarefa, dispositivo) -> justificativa. Preenchido após a conferência.
FALSOS_POSITIVOS_C: dict[tuple[str, str], str] = {}


def ler_jsonl(caminho: Path) -> list[dict]:
    if not caminho.exists():
        return []
    return [json.loads(l) for l in caminho.read_text(encoding="utf-8").splitlines() if l.strip()]


def sim(v: bool) -> str:
    return "sim" if v else "nao"


def nivel(metrica: str, valor: float) -> str:
    """Faixas das Tabelas 2 e 3 de Níveis de Pontuação (Fase 2), fixadas antes da coleta."""
    if metrica == "M9":
        for limite, rotulo in [(0.0, "Excelente"), (2.0, "Bom"), (5.0, "Regular")]:
            if valor <= limite + 1e-9:
                return rotulo
        return "Insatisfatório"
    faixas = {"M13": [(1.0, "Excelente"), (0.90, "Bom"), (0.75, "Regular")],
              "M14": [(1.0, "Excelente"), (0.80, "Bom"), (0.50, "Regular")]}[metrica]
    for limite, rotulo in faixas:
        if valor >= limite - 1e-9:
            return rotulo
    return "Insatisfatório"


# --------------------------------------------------------------------------
# M13 - compatibilidade entre navegadores
# --------------------------------------------------------------------------

def m13():
    regs = ler_jsonl(BRUTOS / "flexibilidade/automatizado/navegadores.jsonl")
    ultimo: dict[tuple[str, str], dict] = {}
    tentativas: dict[tuple[str, str], int] = defaultdict(int)
    ref_por_av: dict[tuple[str, str], dict] = {}
    for r in regs:
        av = r.get("avaliador") or AVALIADOR
        if r["navegador"].startswith("Google Chrome"):
            ref_por_av[(av, r["tarefa"])] = r
        if r.get("apenas_referencia"):
            continue
        k = (r["navegador"], r["tarefa"])
        tentativas[k] += 1
        ultimo[k] = r  # vale a última tentativa (a segunda só ocorre se a primeira falhou)
    ref_geral = {t: r for (n, t), r in ultimo.items() if n.startswith("Google Chrome")}
    linhas, por_nav = [], defaultdict(list)
    for (nav, t), r in sorted(ultimo.items(), key=lambda x: (x[0][0], x[0][1])):
        av = r.get("avaliador") or AVALIADOR
        ref_t = ref_por_av.get((av, t)) or ref_geral.get(t)
        falhas = []
        if r.get("erro"):
            falhas.append("erro de execução: " + r["erro"].split(":")[0])
        elif not r.get("marcadores_ok"):
            falhas.append("página final sem o conteúdo esperado")
        if r.get("erros_js"):
            falhas.append(f"{len(r['erros_js'])} erro(s) de JavaScript")
        a, b = r.get("assinatura") or {}, (ref_t or {}).get("assinatura") or {}
        if a and b and not nav.startswith("Google Chrome") and a.get("tabelas") != b.get("tabelas"):
            falhas.append(f"estrutura diferente do Chrome ({a.get('tabelas')} x {b.get('tabelas')} tabelas)")
        # Erros de JavaScript que não impedem a tarefa são registrados, mas não contam como falha,
        # pois a ficha de M13 define falha pelo efeito visível (elemento, botão, layout ou resultado).
        sem_falha = not [f for f in falhas if not f.endswith("erro(s) de JavaScript")]
        obs = "; ".join(falhas)
        if tentativas[(nav, t)] > 1:
            obs = (obs + "; " if obs else "") + f"{tentativas[(nav, t)]} tentativas"
        linhas.append({"tarefa": t, "navegador": nav, "versao": r.get("navegador_versao", ""),
                       "sistema": r.get("sistema", ""), "resultado": "sem_falha" if sem_falha else "com_falha",
                       "tipo_falha": obs, "avaliador": av, "data": r["data_hora"][:10],
                       "evidencia": r.get("evidencia") or ""})
        por_nav[nav].append(sem_falha)
    escrever(BRUTOS / "flexibilidade/navegadores.csv", linhas,
             ["tarefa", "navegador", "versao", "sistema", "resultado", "tipo_falha", "avaliador", "data", "evidencia"])
    A = sum(l["resultado"] == "sem_falha" for l in linhas)
    B = len(linhas)
    met = []
    if B:
        # Regra 1 de Níveis de Pontuação: sem as 24 combinações, M13 não recebe nível.
        completo = B == COMBINACOES_M13
        met.append(("M13", "geral", "", B, A / B, nivel("M13", A / B) if completo else "",
                    f"{A} de {B} combinações executadas sem falha" + ("" if completo else
                    f"; parcial: faltam {COMBINACOES_M13 - B} combinações, "
                    f"intervalo possível de {A}/{COMBINACOES_M13} a {A + COMBINACOES_M13 - B}/{COMBINACOES_M13}; sem nível até a conclusão")))
        for nav, v in por_nav.items():
            met.append(("M13", "navegador", nav, len(v), sum(v) / len(v), "", "recorte descritivo"))
    return met


# --------------------------------------------------------------------------
# M14 - páginas adaptadas a telas pequenas e ao toque
# --------------------------------------------------------------------------

def criterios(r: dict, disp: str) -> dict[str, bool | None]:
    ad = r.get("adaptacao") or {}
    w = LARGURA[disp]
    # (a) Reflow: a página é montada na largura do aparelho e o conteúdo cabe nela, sem
    #     a redução automática de escala que o navegador aplica quando falta <meta viewport>.
    a = ad.get("largura_layout_px", 9e9) <= w + 1 and ad.get("largura_conteudo_px", 9e9) <= ad.get("largura_layout_px", 0) + 1
    # (b) nenhum texto com fonte efetiva menor que 12 px
    b = ad.get("textos_menores_12px", 1) == 0
    # (c) nenhum texto sobreposto ou cortado (com revisão visual dos casos apontados)
    c = ad.get("textos_sobrepostos", 1) == 0 and ad.get("textos_cobertos", 1) == 0 and ad.get("textos_cortados", 1) == 0
    if not c and (r["tarefa"], disp) in FALSOS_POSITIVOS_C:
        c = True
    # (d) os menus usados na tarefa abrem e são acionados por toque (None = tarefa sem menu)
    d = r.get("toque_menu") in (True, None)
    # (e) alvos de toque de pelo menos 24 x 24 px efetivos, ou espaçamento equivalente
    usados_ok = all((x.get("largura_px") or 0) >= 24 and (x.get("altura_px") or 0) >= 24
                    for x in r.get("alvos_usados", []))
    e = ad.get("alvos_abaixo_24px", 1) == 0 and usados_ok
    return {"a": a, "b": b, "c": c, "d": d, "e": e}


def m14():
    regs = ler_jsonl(BRUTOS / "flexibilidade/automatizado/telas.jsonl")
    ultimo = {(r["dispositivo"], r["tarefa"]): r for r in regs}
    linhas, por_pag, por_larg = [], defaultdict(list), defaultdict(list)
    for disp in ("celular_360", "tablet_768"):
        for t in TAREFAS:
            r = ultimo.get((disp, t))
            if not r or r.get("erro"):
                continue
            c = criterios(r, disp)
            ok = all(c.values())
            linhas.append({"tarefa": t, "pagina": PAGINAS[t], "largura_px": LARGURA[disp],
                           "dispositivo": "emulação do Google Chrome (modo de dispositivo, toque ativado)",
                           **{f"crit_{k}": sim(v) for k, v in c.items()}, "adaptada": sim(ok),
                           "avaliador": AVALIADOR, "data": r["data_hora"][:10], "evidencia": r.get("evidencia") or ""})
            por_pag[t].append(ok)
            por_larg[LARGURA[disp]].append(ok)
    escrever(BRUTOS / "flexibilidade/paginas-adaptadas.csv", linhas,
             ["tarefa", "pagina", "largura_px", "dispositivo", "crit_a", "crit_b", "crit_c", "crit_d", "crit_e",
              "adaptada", "avaliador", "data", "evidencia"])
    A, B = sum(l["adaptada"] == "sim" for l in linhas), len(linhas)
    met = []
    if B:
        met.append(("M14", "geral", "", B, A / B, nivel("M14", A / B),
                    f"{A} de {B} verificações adaptadas; 360 px e 768 px por emulação"))
        for t, v in sorted(por_pag.items()):
            met.append(("M14", "pagina", t, len(v), sum(v) / len(v), "", "recorte por página (regra 3)"))
        for w, v in sorted(por_larg.items()):
            met.append(("M14", "largura", f"{w}px", len(v), sum(v) / len(v), "", "recorte descritivo"))
    return met


# --------------------------------------------------------------------------
# Desempenho (dados complementares, sem nível de pontuação)
# --------------------------------------------------------------------------

def p75(v: list[float]) -> float:
    """Percentil 75 pelo método nearest-rank, o mesmo usado nos Core Web Vitals."""
    s = sorted(v)
    return s[max(0, -(-75 * len(s) // 100) - 1)]


def desempenho():
    todos = ler_jsonl(BRUTOS / "desempenho/automatizado/execucoes.jsonl")
    # Execução VÁLIDA: sem erro, com os marcadores de conclusão e sem nenhuma falha de requisição
    # do próprio SIGAA (CSS/JS). Não é possível saber se uma requisição cancelada pertencia à página
    # medida ou à anterior, então a regra é conservadora. Quando nenhuma execução de uma célula é
    # válida, as estatísticas usam as execuções concluídas (com marcadores) e a linha é marcada
    # como "indicativo": esses valores não devem ser lidos como medida.
    def concluida(r):
        return not r.get("erro") and r.get("marcadores_ok")
    def valida(r):
        # Cancelamentos feitos pelo próprio navegador ao sair da página (ERR_ABORTED) não são falha.
        falhas = [f for f in r.get("falhas_rede", []) if "sigaa.unb.br" in f
                  and "ERR_ABORTED" not in f and "NS_BINDING_ABORTED" not in f]
        return concluida(r) and not falhas
    total = defaultdict(int)
    for r in todos:
        total[(r["dispositivo"], r["rede"], r["tarefa"])] += 1
    validas = defaultdict(list); concl = defaultdict(list)
    for r in todos:
        k = (r["dispositivo"], r["rede"], r["tarefa"])
        if valida(r):
            validas[k].append(r)
        if concluida(r):
            concl[k].append(r)
    regs = [r for r in todos if valida(r)]
    print(f"desempenho: {len(regs)} execuções válidas de {len(todos)}")
    linhas = []
    for (disp, rede, t) in sorted(total):
        k = (disp, rede, t)
        rs, situacao = (validas[k], "medida") if validas[k] else (concl[k], "indicativo")
        if not rs:
            continue
        tot = [sum(p["load_ms"] for p in r["passos"]) / 1000 for r in rs]
        ult = [r["passos"][-1] for r in rs]
        dl = [r["download"]["tempo_ms"] / 1000 for r in rs if r.get("download") and r["download"].get("tempo_ms")]

        def med(k, fator=1.0, origem=ult):
            v = [p[k] for p in origem if p.get(k) is not None]
            return round(st.median(v) * fator, 3) if v else ""
        linhas.append({
            "cenario": f"{disp}/{rede}", "tarefa": t, "situacao": situacao, "n": len(rs),
            "execucoes": total[k], "validas": len(validas[k]), "passos": len(rs[0]["passos"]),
            "carga_total_mediana_s": round(st.median(tot), 2), "carga_total_p75_s": round(p75(tot), 2),
            "carga_total_min_s": round(min(tot), 2), "carga_total_max_s": round(max(tot), 2),
            "ttfb_mediana_s": med("ttfb_ms", 1 / 1000), "fcp_mediana_s": med("fcp_ms", 1 / 1000),
            "lcp_mediana_s": med("lcp_ms", 1 / 1000),
            "lcp_p75_s": round(p75([p["lcp_ms"] for p in ult if p.get("lcp_ms") is not None]) / 1000, 3)
            if any(p.get("lcp_ms") is not None for p in ult) else "",
            "requisicoes_mediana": med("requisicoes"), "transferido_mediana_kb": med("bytes_transferidos", 1 / 1024),
            "html_mediana_kb": med("html_bytes", 1 / 1024), "elementos_dom_mediana": med("elementos_dom"),
            "download_mediana_s": round(st.median(dl), 2) if dl else "",
            "resposta_pagina_final_mediana_s": med("load_ms", 1 / 1000),
            "tbt_mediana_ms": med("tbt_ms"), "tarefas_longas_mediana": med("tarefas_longas"),
            "maior_tarefa_longa_ms": max((p.get("maior_tarefa_ms") or 0) for r in rs for p in r["passos"]) if any("maior_tarefa_ms" in p for r in rs for p in r["passos"]) else "",
            "cls_mediana": round(st.median([max((p.get("cls") or 0) for p in r["passos"]) for r in rs]), 4) if any("cls" in p for r in rs for p in r["passos"]) else "",
            "cls_max": max((p.get("cls") or 0) for r in rs for p in r["passos"]) if any("cls" in p for r in rs for p in r["passos"]) else "",
            "abertura_menu_mediana_ms": round(st.median([r["abertura_menu_ms"] for r in rs if r.get("abertura_menu_ms") is not None])) if any(r.get("abertura_menu_ms") is not None for r in rs) else "",
            "rolagem_fps_mediana": round(st.median([r["rolagem"]["fps_medio"] for r in rs if (r.get("rolagem") or {}).get("fps_medio")]), 1) if any((r.get("rolagem") or {}).get("fps_medio") for r in rs) else "",
            "rolagem_quadro_p95_ms": max(r["rolagem"]["quadro_p95_ms"] for r in rs if (r.get("rolagem") or {}).get("quadro_p95_ms")) if any((r.get("rolagem") or {}).get("quadro_p95_ms") for r in rs) else "",
            "rolagem_quadros_travados": sum((r.get("rolagem") or {}).get("quadros_acima_50ms", 0) for r in rs) if any(r.get("rolagem") for r in rs) else "",
            "datas": ";".join(sorted({r["data_hora"][:16] for r in rs})[:1] + sorted({r["data_hora"][:16] for r in rs})[-1:]),
            "no_servidor": ";".join(sorted({(r.get("assinatura") or {}).get("rodape") or "?" for r in rs})),
        })
    if linhas:
        escrever(CONSOLIDADOS / "desempenho.csv", linhas, list(linhas[0].keys()))
    return len(regs)


# --------------------------------------------------------------------------
# M9 - erros automáticos de acessibilidade por página (WAVE)
# --------------------------------------------------------------------------

def m9():
    arq = BRUTOS / "acessibilidade/wave/resumo.csv"
    if not arq.exists():
        return []
    linhas = list(csv.DictReader(arq.open(encoding="utf-8")))
    if not linhas:
        return []
    total_erros = sum(int(l["erros"]) for l in linhas)
    total_alertas = sum(int(l["alertas"]) for l in linhas)
    n_pags = len(linhas)
    media = total_erros / n_pags
    completo = n_pags == len(TAREFAS)
    met = [
        ("M9", "geral", "", n_pags, media, nivel("M9", media) if completo else "",
         f"{total_erros} erros (WCAG A/AA: Errors + Contrast Errors) em {n_pags} páginas; {total_alertas} alertas fora da métrica"),
    ]
    for l in sorted(linhas, key=lambda x: x["tarefa"]):
        met.append(("M9", "pagina", l["tarefa"], 1, float(l["erros"]), "",
                    f"recorte por página (regra 3); {l['alertas']} alertas"))
    return met


# --------------------------------------------------------------------------

def escrever(caminho: Path, linhas: list[dict], campos: list[str]):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)


def atualizar_metricas(novas: list[tuple]):
    arq = CONSOLIDADOS / "metricas.csv"
    campos = ["metrica", "recorte", "valor_recorte", "n", "valor", "nivel", "observacao"]
    calculadas = {m[0] for m in novas}
    existentes = []
    if arq.exists():
        existentes = [r for r in csv.DictReader(arq.open(encoding="utf-8")) if r["metrica"] not in calculadas]
    for m, rec, vr, n, v, niv, obs in novas:
        existentes.append({"metrica": m, "recorte": rec, "valor_recorte": vr, "n": n,
                           "valor": f"{v:.4f}", "nivel": niv, "observacao": obs})
    escrever(arq, existentes, campos)


def main():
    novas = m9() + m13() + m14()
    atualizar_metricas(novas)
    n = desempenho()
    for m in novas:
        if m[1] == "geral":
            fmt = f"{m[4]:.2f}" if m[0] == "M9" else f"{m[4]:.1%}"
            print(f"{m[0]}: {fmt} ({m[5]}) - {m[6]}")
    print(f"desempenho: {n} execuções válidas")


if __name__ == "__main__":
    main()
