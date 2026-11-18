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
PARTICIPANTES_PREVISTOS = 6
TAREFAS = ["T1", "T2", "T3", "T4", "T5", "T6"]
PROPRIAS = {"M3", "M4", "M5", "M6", "M7", "M8", "M11", "M12", "MA1"}

# Tabelas 2 e 3 de Níveis de Pontuação (Fase 2). (limite, rótulo, maior_melhor)
FAIXAS = {
    "M3": ([(0.10, "Excelente"), (0.25, "Bom"), (0.50, "Regular")], False),
    "M5": ([(0.90, "Excelente"), (0.78, "Bom"), (0.60, "Regular")], True),
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


def m11(comp: list[dict]) -> list[tuple]:
    a, b = proporcao(comp, lambda r: r["correta"] == "sim")
    completo, obs = situacao({r["participante"] for r in comp})
    nao_perg = sum(1 for r in comp if r["tarefa_concluida"] == "sim" and not r["resposta_dada"])
    extra = f"; {nao_perg} pergunta(s) não feita(s) em tarefa concluída, contadas como incorretas" if nao_perg else ""
    out = [geral("M11", b, a / b, completo, f"{a} de {b} respostas corretas sem legenda{extra}; {obs}".rstrip("; "))]
    for t in ("T2", "T4", "T6"):
        lt = [r for r in comp if r["tarefa"] == t]
        if lt:
            x, y = proporcao(lt, lambda r: r["correta"] == "sim")
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
                       "valor": f"{v:.4f}", "nivel": niv, "observacao": obs})
    METRICAS.parent.mkdir(parents=True, exist_ok=True)
    with METRICAS.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)


def main():
    sess = ler(TESTES / "sessoes.csv")
    novas = (m3(ler(QUEST / "respostas.csv")) + m5(sess) + m11(ler(TESTES / "compreensao.csv"))
             + m12(ler(TESTES / "sus.csv")) + ma1(sess))
    atualizar(novas)
    for m in novas:
        if m[1] == "geral":
            fmt = f"{m[4]:.1f}" if m[0] == "M12" else f"{m[4]:.1%}"
            print(f"{m[0]}: {fmt} {m[5] or '(sem nível)'} - {m[6]}")
    for p in pendentes(sess):
        print("pendente -", p)


if __name__ == "__main__":
    main()
