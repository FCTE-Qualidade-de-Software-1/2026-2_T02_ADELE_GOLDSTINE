"""Cálculo de M15 (tempo relativo no celular) a partir de ``dados/brutos/flexibilidade/tempos-celular.csv``.

X = Tm / Td, com Tm = soma dos tempos de T1 a T6 no celular e Td = soma no computador, por avaliador,
e média entre os avaliadores (ficha de M15 em docs/fase-2/metricas.md). Grava as linhas de M15 em
``dados/consolidados/metricas.csv``, substituídas a cada execução: o resultado geral, com nível, e a
razão de cada tarefa, como recorte por página (regra 3 de Níveis de Pontuação).

Uso: ``python coleta/calcular_m15.py``.
"""

from __future__ import annotations

import csv
import statistics as st
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TEMPOS = RAIZ / "dados/brutos/flexibilidade/tempos-celular.csv"
METRICAS = RAIZ / "dados/consolidados/metricas.csv"
TAREFAS = ["T1", "T2", "T3", "T4", "T5", "T6"]
CAMPOS = ["metrica", "recorte", "valor_recorte", "n", "valor", "nivel", "observacao"]


def nivel(x: float) -> str:
    """Faixas de M15 na Tabela 3 de Níveis de Pontuação (Fase 2)."""
    for limite, rotulo in [(1.2, "Excelente"), (1.5, "Bom"), (2.0, "Regular")]:
        if x <= limite:
            return rotulo
    return "Insatisfatório"


def main():
    with TEMPOS.open(encoding="utf-8") as f:
        linhas = [r for r in csv.DictReader(f) if r["tempo_celular_s"] and r["tempo_computador_s"]]
    por_avaliador = defaultdict(dict)
    for r in linhas:
        por_avaliador[r["avaliador"]][r["tarefa"]] = (float(r["tempo_celular_s"]), float(r["tempo_computador_s"]))

    completos = {a: t for a, t in por_avaliador.items() if set(t) == set(TAREFAS)}
    novas = []
    if completos:
        razoes = []
        for t in completos.values():
            tm = sum(v[0] for v in t.values())
            td = sum(v[1] for v in t.values())
            razoes.append((tm, td, tm / td))
        x = st.mean(r[2] for r in razoes)
        detalhe = "; ".join(f"{a}: Tm = {tm:.1f} s, Td = {td:.1f} s"
                            for a, (tm, td, _) in zip(completos, razoes))
        novas.append(("M15", "geral", "", len(completos), x, nivel(x),
                      f"{len(completos)} avaliador(es); {detalhe}"))
        for tarefa in TAREFAS:
            rz = [t[tarefa][0] / t[tarefa][1] for t in completos.values()]
            novas.append(("M15", "tarefa", tarefa, len(rz), st.mean(rz), "", "recorte por tarefa (regra 3)"))

    with METRICAS.open(encoding="utf-8") as f:
        atuais = [r for r in csv.DictReader(f) if r["metrica"] != "M15"]
    for m, rec, vr, n, v, niv, obs in novas:
        atuais.append({"metrica": m, "recorte": rec, "valor_recorte": vr, "n": n,
                       "valor": f"{v:.4f}", "nivel": niv, "observacao": obs})
    with METRICAS.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(atuais)
    for linha in novas:
        print(linha)


if __name__ == "__main__":
    main()
