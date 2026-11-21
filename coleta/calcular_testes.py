"""Cálculo das métricas do teste com usuários e do questionário.

Lê as planilhas de ``dados/brutos/testes-usuarios/`` e ``dados/brutos/questionario/``
(formato em docs/fase-3/planilhas.md) e grava em ``dados/consolidados/metricas.csv``
as linhas de M3, M4, M5, M6, M7, M8, M11, M12 e MA1, substituídas a cada execução.

Uma métrica só é calculada quando os dados de todas as tentativas estão preenchidos.
Enquanto faltarem participantes, o nível fica vazio e a observação diz que o valor é parcial.

Uso: ``python coleta/calcular_testes.py``.
"""

from __future__ import annotations

import csv
import statistics as st
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TESTES = RAIZ / "dados/brutos/testes-usuarios"
QUEST = RAIZ / "dados/brutos/questionario"
REF = RAIZ / "dados/referencia"
METRICAS = RAIZ / "dados/consolidados/metricas.csv"
# O protocolo previa 6 participantes; a coleta foi encerrada com 5 (P1, P2, P3, P4 e P6), decisão da equipe em 21/11/2026.
PARTICIPANTES_PREVISTOS = 5
TAREFAS = ["T1", "T2", "T3", "T4", "T5", "T6"]
PROPRIAS = {"M3", "M4", "M5", "M6", "M7", "M8", "M11", "M12", "MA1", "IQ1", "IQ2", "IQ3", "IQ4", "HP1"}

# Tabelas 2 e 3 de Níveis de Pontuação (Fase 2). (limite, rótulo, maior_melhor)
FAIXAS = {
    "M3": ([(0.10, "Excelente"), (0.25, "Bom"), (0.50, "Regular")], False),
    "M4": ([(0.90, "Excelente"), (0.75, "Bom"), (0.50, "Regular")], True),
    "M5": ([(0.90, "Excelente"), (0.78, "Bom"), (0.60, "Regular")], True),
    "M6": ([(1.5, "Excelente"), (2.5, "Bom"), (4.0, "Regular")], False),
    "M7": ([(1.11, "Excelente"), (1.33, "Bom"), (2.00, "Regular")], False),
    "M8": ([(0.90, "Excelente"), (0.70, "Bom"), (0.50, "Regular")], True),
    "M11": ([(0.90, "Excelente"), (0.75, "Bom"), (0.50, "Regular")], True),
    "M12": ([(80.3, "Excelente"), (68.0, "Bom"), (51.0, "Regular")], True),
}


def nivel(metrica: str, valor: float) -> str:
    faixas, maior_melhor = FAIXAS[metrica]
    for limite, rotulo in faixas:
        if (valor >= limite - 1e-9) if maior_melhor else (valor <= limite + 1e-9):
            return rotulo
    return "Insatisfatório"


def ler(caminho: Path) -> list[dict]:
    if not caminho.exists():
        return []
    with caminho.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def situacao(participantes: set[str]) -> tuple[bool, str]:
    n = len(participantes)
    completo = n >= PARTICIPANTES_PREVISTOS
    obs = "" if completo else (
        f"parcial: {n} de {PARTICIPANTES_PREVISTOS} participantes "
        f"({', '.join(sorted(participantes))}); sem nível até a conclusão")
    return completo, obs


def geral(m: str, n: int, valor: float, completo: bool, obs: str) -> tuple:
    niv = nivel(m, valor) if completo and m in FAIXAS else ""
    if not completo and m in FAIXAS:
        obs += f"; nível provisório: {nivel(m, valor)}"
    return (m, "geral", "", n, valor, niv, obs)


def proporcao(linhas: list[dict], cond) -> tuple[int, int]:
    return sum(1 for r in linhas if cond(r)), len(linhas)


def m3(resp: list[dict]) -> list[tuple]:
    validas = [r for r in resp if r["f1"] in {"sim", "nao"}]
    if not validas:
        return []
    a, b = proporcao(validas, lambda r: r["f1"] == "sim")
    completo, obs = situacao({r["participante"] for r in validas})
    return [geral("M3", b, a / b, completo, f"{a} de {b} usam ferramenta externa (F1); {obs}".rstrip("; "))]


def m5(sess: list[dict]) -> list[tuple]:
    a, b = proporcao(sess, lambda r: r["concluida"] == "sim")
    completo, obs = situacao({r["participante"] for r in sess})
    out = [geral("M5", b, a / b, completo, f"{a} de {b} tentativas concluídas sem ajuda; {obs}".rstrip("; "))]
    for t in TAREFAS:
        lt = [r for r in sess if r["tarefa"] == t]
        if lt:
            x, y = proporcao(lt, lambda r: r["concluida"] == "sim")
            out.append(("M5", "tarefa", t, y, x / y, "", "recorte por tarefa (regra 3)"))
    for g in ("comeco", "meio_fim"):
        lg = [r for r in sess if r["grupo"] == g]
        if lg:
            x, y = proporcao(lg, lambda r: r["concluida"] == "sim")
            np_ = len({r["participante"] for r in lg})
            out.append(("M5", "grupo", g, y, x / y, "", f"recorte descritivo ({np_} participantes)"))
    cal = [r for r in sess if r["grupo"] == "comeco" and r["ja_executou"] == "nao"]
    if cal:
        x, y = proporcao(cal, lambda r: r["concluida"] == "sim")
        out.append(("M5", "grupo", "calouros_primeiro_contato", y, x / y, "",
                    "grupo do começo do curso, só tarefas nunca executadas antes (ficha de M5)"))
    return out


def caminhos() -> tuple[dict[str, int], dict[str, list[str]]]:
    """C_min de cada tarefa (maior ordem do caminho ótimo) e itens válidos de primeira escolha."""
    cmin: dict[str, int] = {}
    validos: dict[str, list[str]] = defaultdict(list)
    for r in ler(REF / "caminhos.csv"):
        if r["tipo"] == "otimo":
            cmin[r["tarefa"]] = max(cmin.get(r["tarefa"], 0), int(r["ordem"]))
        if r["ordem"] in {"0", "1"}:
            validos[r["tarefa"]].append(r["passo"])
    return cmin, validos


def m4(sess: list[dict]) -> list[tuple]:
    """Primeira escolha válida. Sem clique só é válida se a tarefa foi concluída sem cliques (caminho de 0 passos)."""
    if any(not r["primeira_escolha_valida"] for r in sess):
        return []
    a, b = proporcao(sess, lambda r: r["primeira_escolha_valida"] == "sim")
    completo, obs = situacao({r["participante"] for r in sess})
    out = [geral("M4", b, a / b, completo, f"{a} de {b} tentativas com a primeira escolha no caminho; {obs}".rstrip("; "))]
    for t in TAREFAS:
        lt = [r for r in sess if r["tarefa"] == t]
        x, y = proporcao(lt, lambda r: r["primeira_escolha_valida"] == "sim")
        out.append(("M4", "tarefa", t, y, x / y, "", "recorte por tarefa (regra 3)"))
    return out


def m6(sess: list[dict]) -> list[tuple]:
    esp = defaultdict(list)
    for r in ler(REF / "tempos-especialista.csv"):
        esp[r["tarefa"]].append(float(r["tempo_s"]))
    if not esp:
        return []
    razoes, out, fora = [], [], []
    for t in TAREFAS:
        tp = [float(r["tempo_s"]) for r in sess if r["tarefa"] == t and r["concluida"] == "sim"]
        if not tp:
            fora.append(t)
            continue
        if not esp.get(t):
            return []  # falta o tempo do especialista de uma tarefa concluída
        te = st.mean(esp[t])
        razoes.append(st.mean(tp) / te)
        out.append(("M6", "tarefa", t, len(tp), razoes[-1], "",
                    f"Tp = {st.mean(tp):.1f} s ({len(tp)} concluídas); Te = {te:.1f} s ({len(esp[t])} execuções)"))
    completo, obs = situacao({r["participante"] for r in sess})
    extra = f"; fora da média (nenhuma conclusão): {', '.join(fora)}" if fora else ""
    return [geral("M6", len(razoes), st.mean(razoes), completo,
                  f"média de {len(razoes)} tarefas{extra}; {obs}".rstrip("; "))] + out


def m7(sess: list[dict]) -> list[tuple]:
    """Cliques dos que concluíram / C_min. Tarefa com C_min = 0 (informação já na página inicial) fica fora da média."""
    cmin, _ = caminhos()
    if not cmin or any(r["concluida"] == "sim" and not r["cliques"] for r in sess):
        return []
    razoes, out, sem_cmin, sem_conc = [], [], [], []
    for t in TAREFAS:
        cp = [int(r["cliques"]) for r in sess if r["tarefa"] == t and r["concluida"] == "sim"]
        if not cp:
            sem_conc.append(t)
            continue
        if cmin.get(t, 0) == 0:
            sem_cmin.append(t)
            out.append(("M7", "tarefa", t, len(cp), st.mean(cp), "",
                        f"C_min = 0 (a informação está na página inicial): fora da média; valor = média de cliques"))
            continue
        razoes.append(st.mean(cp) / cmin[t])
        out.append(("M7", "tarefa", t, len(cp), razoes[-1], "",
                    f"Cp = {st.mean(cp):.2f} cliques ({len(cp)} concluídas); C_min = {cmin[t]}"))
    completo, obs = situacao({r["participante"] for r in sess})
    extra = ""
    if sem_cmin:
        extra += f"; fora da média por C_min = 0: {', '.join(sem_cmin)}"
    if sem_conc:
        extra += f"; fora da média (nenhuma conclusão): {', '.join(sem_conc)}"
    return [geral("M7", len(razoes), st.mean(razoes), completo,
                  f"média de {len(razoes)} tarefas{extra}; {obs}".rstrip("; "))] + out


def m8(sess: list[dict]) -> list[tuple]:
    if any(not r["avaliador_gravacao"] for r in sess):
        return []
    erros = ler(TESTES / "erros.csv")
    for r in sess:  # as contagens de sessoes.csv devem bater com as linhas de erros.csv
        le = [e for e in erros if e["participante"] == r["participante"] and e["tarefa"] == r["tarefa"]]
        rec = sum(1 for e in le if e["recuperado"] == "sim")
        if (len(le), rec) != (int(r["erros"] or 0), int(r["erros_recuperados"] or 0)):
            raise SystemExit(f"{r['participante']} {r['tarefa']}: erros em sessoes.csv não batem com erros.csv")
    a, b = proporcao(erros, lambda e: e["recuperado"] == "sim")
    valor = a / b if b else 1.0
    completo, obs = situacao({r["participante"] for r in sess})
    out = [geral("M8", b, valor, completo, f"{a} de {b} erros recuperados sem ajuda e sem refazer passos; {obs}".rstrip("; "))]
    for t in TAREFAS:
        lt = [e for e in erros if e["tarefa"] == t]
        if lt:
            x, y = proporcao(lt, lambda e: e["recuperado"] == "sim")
            out.append(("M8", "tarefa", t, y, x / y, "", "recorte por tarefa (regra 3)"))
    return out


def nao_perguntada(r: dict) -> bool:
    """Tarefa concluída sem a pergunta de compreensão: conta como correta (ficha de M11)."""
    return r["tarefa_concluida"] == "sim" and not r["resposta_dada"]


def correta_m11(r: dict) -> bool:
    return r["correta"] == "sim" or nao_perguntada(r)


def m11(comp: list[dict]) -> list[tuple]:
    a, b = proporcao(comp, correta_m11)
    completo, obs = situacao({r["participante"] for r in comp})
    nao_perg = sum(1 for r in comp if nao_perguntada(r))
    extra = f"; inclui {nao_perg} pergunta(s) não feita(s) em tarefa concluída, contadas como corretas" if nao_perg else ""
    out = [geral("M11", b, a / b, completo, f"{a} de {b} respostas corretas sem legenda{extra}; {obs}".rstrip("; "))]
    for t in ("T2", "T4", "T6"):
        lt = [r for r in comp if r["tarefa"] == t]
        if lt:
            x, y = proporcao(lt, correta_m11)
            out.append(("M11", "tarefa", t, y, x / y, "", "recorte por pergunta"))
    return out


def m12(sus: list[dict]) -> list[tuple]:
    if not sus:
        return []
    for r in sus:  # confere a pontuação gravada com a regra da ficha
        itens = [int(r[f"i{i}"]) for i in range(1, 11)]
        calc = 2.5 * sum((v - 1) if i % 2 == 0 else (5 - v) for i, v in enumerate(itens))
        if abs(calc - float(r["pontuacao"])) > 1e-9:
            raise SystemExit(f"SUS de {r['participante']}: pontuação {r['pontuacao']} difere do cálculo {calc}")
    valores = [float(r["pontuacao"]) for r in sus]
    completo, obs = situacao({r["participante"] for r in sus})
    media = st.mean(valores)
    out = [geral("M12", len(valores), media, completo,
                 f"média de {len(valores)} questionários (mín. {min(valores):g}, máx. {max(valores):g}); {obs}".rstrip("; "))]
    por = defaultdict(list)
    for r in sus:
        por[r["grupo"]].append(float(r["pontuacao"]))
    for g, v in sorted(por.items()):
        out.append(("M12", "grupo", g, len(v), st.mean(v), "", f"recorte descritivo ({len(v)} participantes)"))
    return out


def ma1(sess: list[dict]) -> list[tuple]:
    a, b = proporcao(sess, lambda r: r["declarou_inexistente"] == "sim")
    _, obs = situacao({r["participante"] for r in sess})
    return [("MA1", "geral", "", b, a / b, "", f"{a} de {b} tentativas com declaração de função inexistente; sem nível (métrica auxiliar); {obs}".rstrip("; "))]


GRUPOS = ("comeco", "meio_fim")
PROBLEMAS_B5 = ["zoom_rolagem", "menu_nao_abriu", "botoes_pequenos", "conteudo_cortado", "nao_concluiu", "nenhum", "nao_usa"]


def indicadores(resp: list[dict], sess: list[dict]) -> list[tuple]:
    """IQ1 a IQ4 e HP1 (página Questionário, seções 5 e 6): descritivos, sem nível de pontuação."""
    if not resp:
        return []
    grupo = {r["participante"]: r["grupo"] for r in sess}
    por_grupo = {g: [r for r in resp if grupo.get(r["participante"]) == g] for g in GRUPOS}
    n = {g: len(v) for g, v in por_grupo.items()}
    out = []

    def mediana_c1(linhas, t):
        v = [int(r[f"c1_{t[1]}"]) for r in linhas if r[f"c1_{t[1]}"] not in {"", "nunca_fiz"}]
        return (st.median(v), len(v)) if v else (None, 0)

    # IQ1 - facilidade percebida (1 a 5), mediana por tarefa ignorando "Nunca fiz"; também por grupo
    med_grupo = {g: {} for g in GRUPOS}
    for t in TAREFAS:
        m, k = mediana_c1(resp, t)
        out.append(("IQ1", "tarefa", t, k, m, "", "mediana da facilidade percebida (C1, 1 a 5); sem nível"))
        for g in GRUPOS:
            mg, kg = mediana_c1(por_grupo[g], t)
            med_grupo[g][t] = mg
            out.append(("IQ1", f"tarefa_{g}", t, kg, mg, "", f"recorte descritivo ({kg} participantes)"))

    # IQ2 - proporção de tarefas em que já precisou de ajuda (C2)
    def prop_c2(r):
        marc = [x for x in r["c2"].split(";") if x in TAREFAS]
        return len(marc) / len(TAREFAS)
    out.append(("IQ2", "geral", "", len(resp), st.mean(prop_c2(r) for r in resp), "",
                "média, por participante, de tarefas marcadas em C2 / 6; sem nível"))
    for g in GRUPOS:
        if por_grupo[g]:
            out.append(("IQ2", "grupo", g, n[g], st.mean(prop_c2(r) for r in por_grupo[g]), "",
                        f"recorte descritivo ({n[g]} participantes)"))
    for t in TAREFAS:
        k = sum(1 for r in resp if t in r["c2"].split(";"))
        out.append(("IQ2", "tarefa", t, len(resp), k / len(resp), "",
                    f"{k} de {len(resp)} já precisaram de ajuda nesta tarefa"))

    # IQ3 - acerto da sigla IRA (D2)
    a = sum(1 for r in resp if r["d2"] == "rendimento")
    out.append(("IQ3", "geral", "", len(resp), a / len(resp), "", f"{a} de {len(resp)} acertaram a sigla IRA (D2); sem nível"))
    for g in GRUPOS:
        if por_grupo[g]:
            ag = sum(1 for r in por_grupo[g] if r["d2"] == "rendimento")
            out.append(("IQ3", "grupo", g, n[g], ag / n[g], "", f"{ag} de {n[g]} acertos"))

    # IQ4 - dependência do celular (B1 = celular e B2 = não ou só às vezes) e problemas no celular (B5)
    dep = sum(1 for r in resp if r["b1"] == "celular" and r["b2"] in {"nao", "as_vezes"})
    usa = sum(1 for r in resp if r["b1"] in {"celular", "ambos"})
    out.append(("IQ4", "dependentes_celular", "", len(resp), dep / len(resp), "",
                f"{dep} de {len(resp)} dependem do celular (B1 = celular e B2 = não ou só às vezes); "
                f"{usa} usam o celular como principal ou tanto quanto o computador; sem nível"))
    for prob in PROBLEMAS_B5:
        k = sum(1 for r in resp if prob in r["b5"].split(";"))
        out.append(("IQ4", "problema_celular", prob, len(resp), k / len(resp), "", f"{k} de {len(resp)} marcaram em B5"))

    # HP1 - o começo do curso relata menor facilidade (IQ1) que o meio ou fim, em ao menos 4 das 6 tarefas
    menor = [t for t in TAREFAS if None not in (med_grupo["comeco"][t], med_grupo["meio_fim"][t])
             and med_grupo["comeco"][t] < med_grupo["meio_fim"][t]]
    if min(n.values()) < 3:
        clas = "inconclusiva"
        motivo = f"grupo com menos de três questionários válidos (começo: {n['comeco']}, meio ou fim: {n['meio_fim']})"
    else:
        clas = "tendência observada" if len(menor) >= 4 else "sem tendência"
        motivo = f"mediana do começo menor em {len(menor)} de 6 tarefas"
    out.append(("HP1", "geral", "", len(resp), len(menor), "",
                f"{clas}: {motivo}; tarefas com mediana menor no começo do curso: {', '.join(menor) or 'nenhuma'} "
                f"(valor = número dessas tarefas; indício descritivo, não confirmação)"))
    return out


def pendentes(sess: list[dict]) -> list[str]:
    """Métricas que ainda dependem de dados não preenchidos."""
    msg = []
    if any(not r["primeira_escolha_valida"] for r in sess):
        msg.append("M4: falta primeira_escolha_valida (gravações) e a lista de itens válidos em caminhos.csv")
    if not ler(REF / "tempos-especialista.csv"):
        msg.append("M6: tempos-especialista.csv está vazio")
    if not ler(REF / "caminhos.csv") or any(r["concluida"] == "sim" and not r["cliques"] for r in sess):
        msg.append("M7: falta C_min (caminhos.csv) ou cliques nas tentativas concluídas")
    if any(not r["avaliador_gravacao"] for r in sess):
        msg.append("M8: gravações ainda sem avaliador (colunas erros e erros_recuperados)")
    return msg


def atualizar(novas: list[tuple]):
    campos = ["metrica", "recorte", "valor_recorte", "n", "valor", "nivel", "observacao"]
    linhas = [r for r in ler(METRICAS) if r["metrica"] not in PROPRIAS]
    for m, rec, vr, n, v, niv, obs in novas:
        linhas.append({"metrica": m, "recorte": rec, "valor_recorte": vr, "n": n,
                       "valor": "" if v is None else f"{v:.4f}", "nivel": niv, "observacao": obs})
    METRICAS.parent.mkdir(parents=True, exist_ok=True)
    with METRICAS.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)


def main():
    sess = ler(TESTES / "sessoes.csv")
    novas = (m3(ler(QUEST / "respostas.csv")) + m4(sess) + m5(sess) + m6(sess) + m7(sess) + m8(sess) + m11(ler(TESTES / "compreensao.csv"))
             + m12(ler(TESTES / "sus.csv")) + ma1(sess) + indicadores(ler(QUEST / "respostas.csv"), sess))
    atualizar(novas)
    for m in novas:
        if m[1] == "geral" and m[0].startswith("M"):
            fmt = f"{m[4]:.2f}" if m[0] in {"M6", "M7", "M12"} else f"{m[4]:.1%}"
            print(f"{m[0]}: {fmt} {m[5] or '(sem nível)'} - {m[6]}")
    for p in pendentes(sess):
        print("pendente -", p)


if __name__ == "__main__":
    main()
