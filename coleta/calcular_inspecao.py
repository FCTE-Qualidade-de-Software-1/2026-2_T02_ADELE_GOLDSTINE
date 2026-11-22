"""Calcula M1, M2, M10 e M20 a partir das planilhas da inspeção (dados/brutos/inspecao/).

Usa só as colunas *_final (resultado depois dos dois avaliadores e do desempate) e grava
em dados/consolidados/metricas.csv, substituindo as linhas dessas métricas.

    python coleta/calcular_inspecao.py
"""

from __future__ import annotations

import csv
from pathlib import Path

import calcular

INSP = Path(__file__).resolve().parent.parent / "dados/brutos/inspecao"

FAIXAS = {  # Tabela 2 de Níveis de Pontuação (Fase 2), fixadas antes da coleta
    "M1": [(1.0, "Excelente"), (0.90, "Bom"), (0.75, "Regular")],
    "M2": [(1.0, "Excelente"), (0.97, "Bom"), (0.90, "Regular")],
    "M10": [(1.0, "Excelente"), (0.90, "Bom"), (0.75, "Regular")],
    "M20": [(1.0, "Excelente"), (0.75, "Bom"), (0.50, "Regular")],
}


def nivel(m: str, v: float) -> str:
    for limite, rotulo in FAIXAS[m]:
        if v >= limite - 1e-9:
            return rotulo
    return "Insatisfatório"


def ler(nome):
    return list(csv.DictReader((INSP / nome).open(encoding="utf-8")))


def main():
    novas = []
    f = ler("funcoes.csv")
    a = sum(r["existe_final"] == "nao" for r in f)
    v = 1 - a / len(f)
    novas.append(("M1", "geral", "", len(f), v, nivel("M1", v),
                  f"{len(f) - a} de {len(f)} funções da lista de referência existem; ausentes: {a}"))
    for t in sorted({r["tarefa"] for r in f if r["tarefa"]}):
        ft = [r for r in f if r["tarefa"] == t]
        vt = 1 - sum(r["existe_final"] == "nao" for r in ft) / len(ft)
        novas.append(("M1", "tarefa", t, len(ft), vt, "", "recorte por tarefa (regra 3 e ranking da regra 4)"))

    c = ler("correcao.csv")
    div = [r for r in c if r["resultado_final"] == "diverge"]
    crit = [r for r in div if r["item_critico"] == "sim"]
    v = 1 - len(div) / len(c)
    niv = "Insatisfatório" if crit else nivel("M2", v)
    novas.append(("M2", "geral", "", len(c), v, niv,
                  f"{len(c) - len(div)} de {len(c)} verificações coincidem; {len(div)} divergências, {len(crit)} em item crítico"
                  + (": " + "; ".join(r["atributo"] for r in div) if div else "")))
    for t in sorted({r["tarefa"] for r in c}):
        ct = [r for r in c if r["tarefa"] == t]
        vt = 1 - sum(r["resultado_final"] == "diverge" for r in ct) / len(ct)
        novas.append(("M2", "tarefa", t, len(ct), vt, "", "recorte por tarefa (regra 3)"))

    m = ler("acessibilidade-manual.csv")
    ok = sum(r["atende_final"] == "sim" for r in m)
    v = ok / len(m)
    novas.append(("M10", "geral", "", len(m), v, nivel("M10", v), f"{ok} de {len(m)} verificações atendidas (4 critérios x 6 páginas)"))
    for t in sorted({r["tarefa"] for r in m}):
        mt = [r for r in m if r["tarefa"] == t]
        novas.append(("M10", "pagina", t, len(mt), sum(r["atende_final"] == "sim" for r in mt) / len(mt), "", "recorte por página (regra 3)"))
    for cr in "abcd":
        mc = [r for r in m if r["criterio"] == cr]
        novas.append(("M10", "criterio", cr, len(mc), sum(r["atende_final"] == "sim" for r in mc) / len(mc), "", "recorte descritivo"))

    e = ler("cenarios-erro.csv")
    ok = [r["cenario"] for r in e if r["tratado_final"] == "sim"]
    v = len(ok) / len(e)
    nao = [r["cenario"] for r in e if r["tratado_final"] != "sim"]
    novas.append(("M20", "geral", "", len(e), v, nivel("M20", v), f"{len(ok)} de {len(e)} cenários tratados; não tratados: {', '.join(nao) or 'nenhum'}"))

    calcular.atualizar_metricas(novas)
    for n in novas:
        if n[1] == "geral":
            print(n[0], f"{n[4]:.4f}", n[5], "-", n[6])


if __name__ == "__main__":
    main()
