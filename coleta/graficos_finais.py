"""Gráficos da síntese final: todas as métricas, hipóteses, objetivos, matriz
multiplataforma e desempenho complementar.

Lê ``dados/consolidados/metricas.csv``, ``matriz-resumo.csv``,
``matriz-dispositivos.csv`` e ``desempenho.csv`` e grava SVGs em
``docs/assets/graficos/final/``. Também é um hook do MkDocs: o marcador
``[[GRAFICO_FINAL:nome]]`` numa página é trocado pelo SVG (com dicas ao passar o
mouse) e por uma tabela com os mesmos dados.

Uso: ``python coleta/graficos_finais.py`` (o ``mkdocs build`` também chama o hook).
"""

from __future__ import annotations

import csv
import html
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CONS = RAIZ / "dados/consolidados"
SAIDA = RAIZ / "docs/assets/graficos/final"

NIVEIS = ["Insatisfatório", "Regular", "Bom", "Excelente"]
FAIXA_COR = ["#f4c4c6", "#f8e1e3", "#dde9f7", "#bcd5f1"]  # mesmas faixas do painel do teste com usuários
RUIM, BOM, TINTA, TEXTO, GRADE = "#d8434a", "#2a6fc9", "#1d1d2b", "#55546a", "#e3e3ea"
INDIGO = "#6c74e0"
FONTE = "'Open Sans','Segoe UI',system-ui,sans-serif"

# Métrica: (objetivo, nome, limites do pior ao melhor extremo, formato). Fase 2, Níveis de Pontuação.
METRICAS = {
    "M1": ("G1", "Cobertura funcional", [0.0, 0.75, 0.90, 0.9999, 1.0], "pct"),
    "M2": ("G1", "Correção funcional", [0.0, 0.90, 0.97, 0.9999, 1.0], "pct"),
    "M3": ("G1", "Uso de ferramenta externa", [1.0, 0.50, 0.25, 0.10, 0.0], "pct"),
    "M4": ("G2", "Acerto na primeira escolha", [0.0, 0.50, 0.75, 0.90, 1.0], "pct"),
    "M5": ("G2", "Conclusão sem ajuda", [0.0, 0.60, 0.78, 0.90, 1.0], "pct"),
    "M6": ("G2", "Tempo × especialista", [8.0, 4.0, 2.5, 1.5, 1.0], "x"),
    "M7": ("G2", "Cliques × caminho mínimo", [3.0, 2.0, 1.33, 1.11, 1.0], "x"),
    "M8": ("G2", "Erros recuperados sem ajuda", [0.0, 0.50, 0.70, 0.90, 1.0], "pct"),
    "M20": ("G2", "Cenários de erro tratados", [0.0, 0.50, 0.75, 0.9999, 1.0], "pct"),
    "M9": ("G2", "Erros WAVE por página", [20.0, 5.0, 2.0, 0.0001, 0.0], "n"),
    "M10": ("G2", "Critérios manuais de acessibilidade", [0.0, 0.75, 0.90, 0.9999, 1.0], "pct"),
    "M11": ("G2", "Leitura correta sem legenda", [0.0, 0.50, 0.75, 0.90, 1.0], "pct"),
    "M12": ("G2", "Satisfação (SUS)", [0.0, 51.0, 68.0, 80.3, 100.0], "sus"),
    "M13": ("G3", "Compatibilidade entre navegadores", [0.0, 0.75, 0.90, 0.9999, 1.0], "pct"),
    "M14": ("G3", "Páginas adaptadas a telas pequenas", [0.0, 0.50, 0.80, 0.9999, 1.0], "pct"),
    "M15": ("G3", "Tempo no celular × computador", [3.0, 2.0, 1.5, 1.2, 1.0], "x"),
}
OBJETIVOS = {"G1": "Adequação Funcional", "G2": "Capacidade de Interação", "G3": "Flexibilidade"}

# Hipótese: (métrica, nível previsto, classificação). Julgamento, Tabelas 2 a 4.
# H5 é refutada para melhor pelo recorte dos calouros (10 de 12 concluídas, acima dos < 65% previstos),
# embora M5 geral tenha ficado no nível previsto; por isso o sentido não sai da comparação de níveis.
SENTIDO = {"H5": "melhor"}
HIPOTESES = {
    "H1": ("M1", 1, "Confirmada"), "H2": ("M2", 3, "Refutada"), "H3": ("M3", 1, "Refutada"),
    "H4": ("M4", 1, "Confirmada"), "H5": ("M5", 2, "Refutada"), "H6": ("M6", 1, "Refutada"),
    "H7": ("M7", 1, "Confirmada"), "H8": ("M8", 1, "Refutada"), "H9": ("M20", 0, "Refutada"),
    "H10": ("M9", 0, "Confirmada"), "H11": ("M10", 1, "Refutada"), "H12": ("M11", 1, "Confirmada"),
    "H13": ("M12", 1, "Refutada"), "H14": ("M13", 2, "Refutada"), "H15": ("M14", 0, "Confirmada"),
    "H16": ("M15", 1, "Confirmada"),
}


def e(t) -> str:
    return html.escape(str(t), quote=True)


def num(v: float, casas: int = 1) -> str:
    return f"{v:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def fmt(v: float, tipo: str) -> str:
    if tipo == "pct":
        return num(v * 100, 1).replace(",0", "") + "%"
    if tipo == "x":
        return num(v, 2) + "×"
    return num(v, 2 if tipo == "n" else 1)


def ler(nome: str) -> list[dict]:
    caminho = CONS / nome
    if not caminho.exists():
        return []
    with caminho.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def metricas() -> dict[str, tuple[float, str]]:
    return {r["metrica"]: (float(r["valor"]), r["nivel"]) for r in ler("metricas.csv")
            if r["recorte"] == "geral" and r["metrica"] in METRICAS}


def posicao(v: float, lim: list[float]) -> float:
    for i in range(4):
        a, b = lim[i], lim[i + 1]
        if min(a, b) - 1e-9 <= v <= max(a, b) + 1e-9:
            return i + (v - a) / (b - a) if b != a else i + 0.5
    return 0.0 if (v > lim[0]) == (lim[0] > lim[4]) else 4.0


def svg(w: int, h: int, corpo: str, titulo: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="{e(titulo)}" style="font-family:{FONTE};font-size:13px;max-width:100%;height:auto">'
            f'<title>{e(titulo)}</title><rect width="{w}" height="{h}" fill="#fbfbfe" rx="10"/>{corpo}</svg>')


def texto(x, y, t, cor=TEXTO, peso=400, ancora="start", tam=13, extra=""):
    halo = 'paint-order="stroke" stroke="#fbfbfe" stroke-width="3" stroke-linejoin="round"' if cor in (TINTA, TEXTO) else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" fill="{cor}" font-weight="{peso}" text-anchor="{ancora}" '
            f'font-size="{tam}" {halo} {extra}>{e(t)}</text>')


def faixas(x_de, y0, altura, rotulos=True):
    c = []
    for i, n in enumerate(NIVEIS):
        c.append(f'<rect x="{x_de(i) + 1:.1f}" y="{y0}" width="{x_de(1) - x_de(0) - 2:.1f}" height="{altura}" rx="5" fill="{FAIXA_COR[i]}"/>')
        if rotulos:
            c.append(texto((x_de(i) + x_de(i + 1)) / 2, y0 - 10, n, TINTA, 700, "middle"))
    return "".join(c)


# ---------------------------------------------------------------------------
def g_metricas():
    m = metricas()
    W, esq, dir_, sup, lh = 1000, 330, 190, 56, 30
    x_de = lambda p: esq + p / 4 * (W - esq - dir_)
    linhas, y, corpo, tabela = [], sup, [], []
    for g in OBJETIVOS:
        linhas.append(("grupo", g))
        linhas += [("m", k) for k, v in METRICAS.items() if v[0] == g and k in m]
    H = sup + lh * len(linhas) + 16
    corpo.append(faixas(x_de, sup - 4, lh * len(linhas) + 4))
    corpo.append(texto(x_de(0) - 8, sup - 14, "pior ←", ancora="end"))
    corpo.append(texto(x_de(4) + 8, sup - 14, "→ melhor"))
    for tipo, k in linhas:
        yc = y + lh / 2
        if tipo == "grupo":
            corpo.append(texto(16, yc + 5, f"{k} · {OBJETIVOS[k]}", INDIGO, 700, tam=14))
        else:
            _, nome, lim, f = METRICAS[k]
            v, nv = m[k]
            x = x_de(posicao(v, lim))
            corpo.append(texto(28, yc + 5, k, TINTA, 700))
            corpo.append(texto(70, yc + 5, nome, TINTA))
            corpo.append(f'<line x1="{x_de(0)}" x2="{x_de(4)}" y1="{yc}" y2="{yc}" stroke="#fff" stroke-width="1.5"/>')
            corpo.append(f'<circle cx="{x:.1f}" cy="{yc}" r="8" fill="{TINTA}" stroke="#fff" stroke-width="2"><title>{e(k)} {e(nome)}: {e(fmt(v, f))} ({e(nv)})</title></circle>')
            corpo.append(texto(W - dir_ + 14, yc + 5, fmt(v, f), TINTA, 700))
            corpo.append(texto(W - dir_ + 84, yc + 5, nv))
            tabela.append((k, OBJETIVOS[METRICAS[k][0]], nome, fmt(v, f), nv))
        y += lh
    titulo = "As 16 métricas nas faixas de nível definidas na Fase 2"
    return svg(W, H, "".join(corpo), titulo), (["Métrica", "Característica", "Descrição", "Valor", "Nível"], tabela)


def g_hipoteses():
    m = metricas()
    W, esq, dir_, sup, lh = 1000, 330, 200, 70, 27
    x_de = lambda p: esq + p / 4 * (W - esq - dir_)
    xc = lambda n: x_de(n + 0.5)
    corpo, tabela = [faixas(x_de, sup - 4, lh * 16 + 4)], []
    # legenda
    corpo.append(f'<circle cx="24" cy="22" r="7" fill="#fff" stroke="{TINTA}" stroke-width="2"/>')
    corpo.append(texto(36, 27, "nível previsto (hipótese)"))
    corpo.append(f'<circle cx="214" cy="22" r="7" fill="{TINTA}"/>')
    corpo.append(texto(226, 27, "nível obtido (métrica)"))
    cores = {"Confirmada": BOM, "Refutada": RUIM, "Inconclusiva": "#8a8a99"}
    for i, (h, (mt, prev, cl)) in enumerate(HIPOTESES.items()):
        yc = sup + lh * i + lh / 2
        obt = NIVEIS.index(m[mt][1])
        rotulo = cl if cl != "Refutada" else ("Refutada · " + SENTIDO.get(h, "melhor" if obt > prev else "pior"))
        corpo.append(texto(20, yc + 5, h, TINTA, 700))
        corpo.append(texto(66, yc + 5, f"{mt} · {METRICAS[mt][1]}"))
        if obt != prev:
            corpo.append(f'<line x1="{xc(prev):.1f}" x2="{xc(obt):.1f}" y1="{yc}" y2="{yc}" stroke="{TINTA}" stroke-width="2"/>')
        corpo.append(f'<circle cx="{xc(prev):.1f}" cy="{yc}" r="7" fill="#fff" stroke="{TINTA}" stroke-width="2"/>')
        corpo.append(f'<circle cx="{xc(obt):.1f}" cy="{yc}" r="{4.5 if obt == prev else 7}" fill="{TINTA}"><title>{h}: previsto {NIVEIS[prev]}, obtido {NIVEIS[obt]} ({rotulo})</title></circle>')
        corpo.append(f'<rect x="{W - dir_ + 14}" y="{yc - 9}" width="12" height="12" rx="3" fill="{cores[cl]}"/>')
        corpo.append(texto(W - dir_ + 32, yc + 2, rotulo, TINTA, 600))
        tabela.append((h, mt, NIVEIS[prev], NIVEIS[obt], rotulo))
    H = sup + lh * 16 + 14
    conf = sum(1 for v in HIPOTESES.values() if v[2] == "Confirmada")
    ref = sum(1 for v in HIPOTESES.values() if v[2] == "Refutada")
    titulo = f"Hipóteses H1 a H16: {conf} confirmadas e {ref} refutadas"
    return svg(W, H, "".join(corpo), titulo), (["Hipótese", "Métrica", "Previsto", "Obtido", "Classificação"], tabela)


def g_objetivos():
    m = metricas()
    W, esq, dir_, sup, lh = 1000, 250, 200, 50, 80
    x_de = lambda v: esq + v / 3 * (W - esq - dir_)
    corpo, tabela = [], []
    for v, r in ((0, "0"), (1, "1 · limite do “não atende”"), (2, "2 · limite do “atende”"), (3, "3")):
        corpo.append(f'<line x1="{x_de(v):.1f}" x2="{x_de(v):.1f}" y1="{sup - 8}" y2="{sup + lh * 3}" stroke="{GRADE if v in (0, 3) else TEXTO}" stroke-width="1.5" {"" if v in (0, 3) else "stroke-dasharray=\"5 4\""}/>')
        corpo.append(texto(x_de(v), sup - 16, r, TEXTO, 400, "middle", 12))
    for i, g in enumerate(("G2", "G1", "G3")):
        qs = [NIVEIS.index(m[k][1]) for k, v in METRICAS.items() if v[0] == g]
        media = sum(qs) / len(qs)
        julg = "Não atende" if media < 1 else ("Atende" if media >= 2 and 0 not in qs else "Atende parcialmente")
        y = sup + lh * i
        corpo.append(texto(20, y + 30, OBJETIVOS[g], TINTA, 700, tam=15))
        corpo.append(texto(20, y + 50, f"{g} · {len(qs)} questões"))
        cor = RUIM if julg == "Não atende" else ("#e39a3b" if julg == "Atende parcialmente" else BOM)
        corpo.append(f'<rect x="{x_de(0)}" y="{y + 18}" width="{x_de(media) - x_de(0):.1f}" height="26" rx="4" fill="{cor}"><title>{g}: média {num(media, 2)} · {julg}</title></rect>')
        dist = ", ".join(f"{qs.count(n)} {NIVEIS[n]}" for n in (3, 2, 1, 0) if qs.count(n))
        corpo.append(texto(x_de(0), y + 62, "questões: " + dist, TEXTO, 400, tam=12))
        corpo.append(texto(W - dir_ + 16, y + 30, num(media, 2), TINTA, 700, tam=20))
        corpo.append(texto(W - dir_ + 16, y + 50, julg, TINTA, 600))
        tabela.append((g, OBJETIVOS[g], ", ".join(map(str, qs)), num(media, 2), julg))
    H = sup + lh * 3 + 12
    titulo = "Média dos níveis das questões por característica (0 a 3)"
    return svg(W, H, "".join(corpo), titulo), (["Objetivo", "Característica", "Níveis das questões", "Média", "Julgamento"], tabela)


# ---------------------------------------------------------------------------
def g_matriz():
    det = ler("matriz-dispositivos.csv")
    res = ler("matriz-resumo.csv")
    if not res:
        return None
    cel = {(r["perfil"], r["pagina"]): r for r in det}
    cols = ["login", "T1", "T2", "T3", "T4", "T5", "T6"]
    W, esq, sup, lh, cw = 1000, 360, 92, 25, 62
    corpo, tabela = [], []
    cores = {"ok": BOM, "nao_adapta": "#f2a7aa", "falha": RUIM}
    leg = [("ok", "concluiu e a página cabe na tela"), ("nao_adapta", "concluiu, mas a página não se adapta (zoom e rolagem)"), ("falha", "não concluiu")]
    x = 20
    for k, t in leg:
        corpo.append(f'<rect x="{x}" y="14" width="14" height="14" rx="3" fill="{cores[k]}"/>')
        corpo.append(texto(x + 20, 26, t))
        x += 30 + len(t) * 6.6
    for j, c in enumerate(cols):
        corpo.append(texto(esq + cw * j + cw / 2, sup - 12, "Login UnB" if c == "login" else c, TINTA, 700, "middle"))
    corpo.append(texto(esq + cw * 7 + 14, sup - 12, "páginas adaptadas", TINTA, 700))
    y, cat_ant = sup, None
    for r in res:
        if r["categoria"] != cat_ant:
            if cat_ant:
                y += 10
            corpo.append(texto(20, y + 17, r["categoria"].upper(), INDIGO, 700, tam=12, extra='letter-spacing="1.5"'))
            y += 22
            cat_ant = r["categoria"]
        movel = r["categoria"] != "Computador"
        corpo.append(texto(20, y + 17, f'{r["sistema"]} · {r["navegador"]}', TINTA, 600))
        corpo.append(texto(esq - 10, y + 17, r["aparelho"].replace(" (", " · ").rstrip(")"), TEXTO, 400, "end", 12))
        for j, c in enumerate(cols):
            d = cel.get((r["perfil"], c))
            if not d:
                continue
            if d["concluiu"] != "sim":
                k, s = "falha", "✕"
            elif movel and (d["adaptada"] == "não" if c != "login" else "não" in (d["crit_a"], d["crit_b"], d["crit_e"])):
                k, s = "nao_adapta", "✓"
            else:
                k, s = "ok", "✓"
            dica = (f'{r["sistema"]} · {r["navegador"]} · {r["aparelho"]} · {c}: '
                    + ("concluiu" if d["concluiu"] == "sim" else "não concluiu")
                    + (f'; escala {d["escala_visual"]}, menor fonte {d["fonte_minima_efetiva_px"]} px' if d["escala_visual"] else ""))
            corpo.append(f'<rect x="{esq + cw * j + 2}" y="{y + 2}" width="{cw - 4}" height="{lh - 4}" rx="4" fill="{cores[k]}"><title>{e(dica)}</title></rect>')
            corpo.append(texto(esq + cw * j + cw / 2, y + 17, s, "#fff" if k != "nao_adapta" else TINTA, 700, "middle"))
        adapt = f'{r["paginas_adaptadas"]} de {r["paginas_avaliadas"]}' if movel else "não se aplica"
        corpo.append(texto(esq + cw * 7 + 14, y + 17, adapt, TINTA if movel else TEXTO, 700 if movel else 400))
        tabela.append((r["categoria"], r["sistema"], r["navegador"], r["aparelho"], f'{r["tarefas_concluidas"]} de {r["tarefas"]}', adapt, r.get("login_cabe_na_tela") or "—"))
        y += lh
    titulo = "Matriz multiplataforma: login e tarefas T1 a T6 em cada sistema, aparelho e navegador"
    return svg(W, y + 16, "".join(corpo), titulo), (["Categoria", "Sistema", "Navegador", "Aparelho", "Tarefas concluídas", "Páginas do SIGAA adaptadas", "Login da UnB cabe na tela"], tabela)


def g_fontes():
    res = [r for r in ler("matriz-resumo.csv") if r["categoria"] != "Computador" and r["fonte_minima_px"]]
    if not res:
        return None
    W, esq, dir_, sup, lh = 1000, 330, 60, 64, 30
    vmax = 18
    x_de = lambda v: esq + v / vmax * (W - esq - dir_)
    corpo, tabela = [], []
    corpo.append(f'<circle cx="24" cy="22" r="7" fill="{BOM}"/>')
    corpo.append(texto(36, 27, "página de login da UnB (responsiva)"))
    corpo.append(f'<circle cx="300" cy="22" r="7" fill="{RUIM}"/>')
    corpo.append(texto(312, 27, "menor fonte nas páginas do SIGAA (T1 a T6)"))
    for v in range(0, vmax + 1, 3):
        corpo.append(f'<line x1="{x_de(v):.1f}" x2="{x_de(v):.1f}" y1="{sup - 6}" y2="{sup + lh * len(res)}" stroke="{GRADE}"/>')
        corpo.append(texto(x_de(v), sup + lh * len(res) + 18, f"{v} px", TEXTO, 400, "middle", 12))
    corpo.append(f'<line x1="{x_de(12):.1f}" x2="{x_de(12):.1f}" y1="{sup - 16}" y2="{sup + lh * len(res)}" stroke="{TINTA}" stroke-width="1.5" stroke-dasharray="5 4"/>')
    corpo.append(texto(x_de(12) + 6, sup - 8, "mínimo legível: 12 px (critério b de M14)", TINTA, 600, tam=12))
    for i, r in enumerate(res):
        yc = sup + lh * i + lh / 2
        fs, fl = float(r["fonte_minima_px"]), float(r["fonte_minima_login_px"] or 0)
        corpo.append(texto(20, yc + 5, f'{r["aparelho"]} · {r["navegador"].replace(" (WebKit)", "")}', TINTA, 600))
        corpo.append(f'<line x1="{x_de(fs):.1f}" x2="{x_de(fl):.1f}" y1="{yc}" y2="{yc}" stroke="{TEXTO}" stroke-width="2"/>')
        corpo.append(f'<circle cx="{x_de(fl):.1f}" cy="{yc}" r="7" fill="{BOM}" stroke="#fff" stroke-width="2"><title>Login: {num(fl, 1)} px</title></circle>')
        corpo.append(f'<circle cx="{x_de(fs):.1f}" cy="{yc}" r="7" fill="{RUIM}" stroke="#fff" stroke-width="2"><title>SIGAA: {num(fs, 1)} px, escala {r["escala_mediana"]}</title></circle>')
        corpo.append(texto(x_de(fs) - 12, yc + 4, f"{num(fs, 1)} px", TINTA, 700, "end", 12))
        tabela.append((r["aparelho"], r["navegador"], f"{num(fl, 1)} px", f"{num(fs, 1)} px", num(float(r["escala_mediana"]) * 100, 0) + "%"))
    titulo = "Menor fonte efetiva na tela do aparelho: login da UnB × páginas do SIGAA"
    return svg(W, sup + lh * len(res) + 30, "".join(corpo), titulo), (["Aparelho", "Navegador", "Login UnB", "SIGAA (menor)", "Escala da página"], tabela)


def g_desempenho():
    linhas = [r for r in ler("desempenho.csv") if r.get("situacao") == "medida"]
    if not linhas:
        return None
    dados = {}
    for r in linhas:
        dados.setdefault(r["tarefa"], {})["comp" if r["cenario"].startswith("computador") else "cel"] = float(r["carga_total_mediana_s"])
    W, esq, dir_, sup, lh = 1000, 170, 70, 70, 52
    vmax = 20
    x_de = lambda v: esq + v / vmax * (W - esq - dir_)
    corpo, tabela = [], []
    corpo.append(f'<rect x="20" y="14" width="14" height="14" rx="3" fill="{INDIGO}"/>')
    corpo.append(texto(40, 26, "computador, rede local"))
    corpo.append(f'<rect x="220" y="14" width="14" height="14" rx="3" fill="#e39a3b"/>')
    corpo.append(texto(240, 26, "celular 360 px, 4G e CPU limitadas (perfil do Lighthouse)"))
    tarefas = sorted(dados)
    for v in range(0, vmax + 1, 5):
        corpo.append(f'<line x1="{x_de(v):.1f}" x2="{x_de(v):.1f}" y1="{sup - 6}" y2="{sup + lh * len(tarefas)}" stroke="{GRADE}"/>')
        corpo.append(texto(x_de(v), sup + lh * len(tarefas) + 18, f"{v} s", TEXTO, 400, "middle", 12))
    for v, r in ((1, "1 s: fluxo do pensamento"), (10, "10 s: limite da atenção")):
        corpo.append(f'<line x1="{x_de(v):.1f}" x2="{x_de(v):.1f}" y1="{sup - 16}" y2="{sup + lh * len(tarefas)}" stroke="{TINTA}" stroke-width="1.5" stroke-dasharray="5 4"/>')
        corpo.append(texto(x_de(v) + 6, sup - 8, r + " (Nielsen)", TINTA, 600, tam=12))
    nomes = {"T1": "T1 Notas", "T2": "T2 Portal", "T3": "T3 Atestado", "T4": "T4 Índices", "T5": "T5 Turma Virtual", "T6": "T6 Calendário"}
    for i, t in enumerate(tarefas):
        y = sup + lh * i
        corpo.append(texto(20, y + 30, nomes.get(t, t), TINTA, 600))
        for k, (chave, cor) in enumerate((("comp", INDIGO), ("cel", "#e39a3b"))):
            v = dados[t].get(chave)
            if v is None:
                continue
            yy = y + 8 + k * 20
            corpo.append(f'<rect x="{x_de(0)}" y="{yy}" width="{max(x_de(min(v, vmax)) - x_de(0), 2):.1f}" height="17" rx="4" fill="{cor}"><title>{t} · {"computador" if chave == "comp" else "celular 4G"}: {num(v, 2)} s</title></rect>')
            corpo.append(texto(x_de(min(v, vmax)) + 6, yy + 13, f"{num(v, 2)} s", TINTA, 700, tam=12))
        tabela.append((nomes.get(t, t), f'{num(dados[t].get("comp", 0), 2)} s', f'{num(dados[t].get("cel", 0), 2)} s'))
    titulo = "Espera pelo sistema em cada tarefa (mediana, cache desativado)"
    return svg(W, sup + lh * len(tarefas) + 30, "".join(corpo), titulo), (["Tarefa", "Computador", "Celular em 4G"], tabela)


GRAFICOS = {
    "metricas": g_metricas, "hipoteses": g_hipoteses, "objetivos": g_objetivos,
    "matriz": g_matriz, "fontes": g_fontes, "desempenho": g_desempenho,
}


def tabela_html(cab, linhas) -> str:
    th = "".join(f"<th>{e(c)}</th>" for c in cab)
    tr = "".join("<tr>" + "".join(f"<td>{e(v)}</td>" for v in l) + "</tr>" for l in linhas)
    return f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


def gerar() -> dict[str, tuple[str, tuple]]:
    SAIDA.mkdir(parents=True, exist_ok=True)
    feitos = {}
    for nome, f in GRAFICOS.items():
        r = f()
        if r:
            (SAIDA / f"{nome}.svg").write_text(r[0], encoding="utf-8")
            feitos[nome] = r
    return feitos


MARCADOR = re.compile(r"\[\[GRAFICO_FINAL:([a-z]+)\]\]")
_CACHE: dict = {}


def on_page_markdown(markdown, page, config, files):  # noqa: ARG001 (assinatura do MkDocs)
    if "[[GRAFICO_FINAL:" not in markdown:
        return markdown
    if not _CACHE:
        _CACHE.update(gerar())

    def troca(mo):
        g = _CACHE.get(mo.group(1))
        if not g:
            return f"*Gráfico `{mo.group(1)}` indisponível: rode a coleta e o cálculo.*"
        return (f'<div class="grafico-final" markdown="0">{g[0]}</div>\n\n'
                f'<details markdown="0"><summary>Ver os dados em tabela</summary>{tabela_html(*g[1])}</details>\n')
    return MARCADOR.sub(troca, markdown)


if __name__ == "__main__":
    for n in gerar():
        print(SAIDA.relative_to(RAIZ) / f"{n}.svg")
