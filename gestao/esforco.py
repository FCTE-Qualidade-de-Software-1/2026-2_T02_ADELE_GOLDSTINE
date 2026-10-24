"""Cálculo do esforço da equipe (indicador I3 da Gestão do Projeto).

Uso:
    python gestao/esforco.py estimar --ref <commit>   # reconstrói as horas a partir do git blame
    python gestao/esforco.py calcular [--entrega E1]  # horas e percentual por membro

A metodologia está descrita em docs/contribuicao.md.
"""

import argparse
import csv
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLANILHA = RAIZ / "gestao" / "esforco.csv"

MEMBROS = [
    "Arthur Carvalho Leite",
    "Caio Melo Borges",
    "Daniel Nunes Duarte",
    "Davi dos Santos Brito Nobre",
    "Felipe de Aquino Campêlo",
    "Leonardo Fachinello Bonetti",
]

# E-mails de autoria no Git de cada membro (inclui os endereços noreply do GitHub)
EMAILS = {
    "arthur.c.lleite@gmail.com": "Arthur Carvalho Leite",
    "caioborges250802@gmail.com": "Caio Melo Borges",
    "108186816+CaioMelo25@users.noreply.github.com": "Caio Melo Borges",
    "davinobre.ik@gmail.com": "Davi dos Santos Brito Nobre",
    "101183717+Jagaima@users.noreply.github.com": "Davi dos Santos Brito Nobre",
    "felipeaquinocamp@gmail.com": "Felipe de Aquino Campêlo",
    "leonardofbonetti@gmail.com": "Leonardo Fachinello Bonetti",
    "124631520+LeoFacB@users.noreply.github.com": "Leonardo Fachinello Bonetti",
}

# Taxas de produção (palavras por hora) de cada categoria de artefato
TAXAS = {
    "redacao": 1100,  # páginas da GitPage: conteúdo original, com pesquisa e apoio de IA
    "consolidacao": 2200,  # artigo em LaTeX: reescrita de conteúdo já produzido nas páginas
}


def categoria(arquivo):
    if arquivo.startswith("artigo/"):
        return "consolidacao"
    return "redacao"


# Textos produzidos pela equipe (exclui o modelo IEEE copiado do CTAN, PDFs e imagens)
CAMINHOS = ["docs", "artigo/secoes", "artigo/artigo.tex", "artigo/bibliografia.bib"]
EXTENSOES = (".md", ".tex", ".bib")


def palavras_adicionadas(ref):
    """Soma as palavras das linhas adicionadas por cada membro em cada arquivo, até `ref`.

    Conta todos os commits sem merge, inclusive versões depois substituídas, porque
    o esforço de escrevê-las existiu. Alterações só de espaço em branco são ignoradas (-w).
    """
    saida = subprocess.run(
        ["git", "log", ref, "--no-merges", "-w", "-p", "--format=COMMIT %ae", "--", *CAMINHOS],
        cwd=RAIZ, capture_output=True, text=True, check=True,
    ).stdout
    contagem = defaultdict(int)
    autor = arquivo = None
    for linha in saida.splitlines():
        if linha.startswith("COMMIT "):
            autor = EMAILS.get(linha.split(" ", 1)[1])
        elif linha.startswith("+++ "):
            arquivo = linha[6:] if linha.startswith("+++ b/") else None
        elif linha.startswith("+") and autor and arquivo and arquivo.endswith(EXTENSOES):
            contagem[(autor, arquivo)] += len(linha[1:].split())
    return contagem


def estimar(args):
    escritor = csv.writer(sys.stdout, lineterminator="\n")
    for (membro, arquivo), palavras in sorted(palavras_adicionadas(args.ref).items()):
        cat = categoria(arquivo)
        escritor.writerow([
            args.entrega, args.data, membro, f"{palavras / TAXAS[cat]:.2f}", cat,
            f"{arquivo}: {palavras} palavras / {TAXAS[cat]} por hora",
            f"git log {args.ref[:7]}", "estimada",
        ])


def percentuais(horas):
    """Percentuais com uma casa decimal que somam exatamente 100,0 (maiores restos)."""
    total = sum(horas.values())
    exatos = {m: h / total * 1000 for m, h in horas.items()}
    base = {m: int(v) for m, v in exatos.items()}
    sobra = 1000 - sum(base.values())
    for m in sorted(exatos, key=lambda m: exatos[m] - base[m], reverse=True)[:sobra]:
        base[m] += 1
    return {m: v / 10 for m, v in base.items()}


def br(valor):
    return f"{valor:.1f}".replace(".", ",")


def calcular(args):
    horas = {m: 0.0 for m in MEMBROS}
    por_categoria = defaultdict(lambda: defaultdict(float))
    with open(PLANILHA, encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            if args.entrega and linha["entrega"] != args.entrega:
                continue
            h = float(linha["horas"])
            horas[linha["membro"]] += h
            por_categoria[linha["membro"]][linha["categoria"]] += h
    cats = sorted({c for m in por_categoria.values() for c in m})
    pct = percentuais(horas)
    total = sum(horas.values())
    print("| Membro | " + " | ".join(cats) + " | Horas | Esforço (%) |")
    print("| ------ | " + " | ".join(":-:" for _ in cats) + " | :-: | :-: |")
    for m in MEMBROS:
        colunas = [br(por_categoria[m][c]) for c in cats]
        alerta = " ⚠" if pct[m] < 10 or pct[m] > 40 else ""
        print(f"| {m} | " + " | ".join(colunas) + f" | {br(horas[m])} | {br(pct[m])}{alerta} |")
    print("| **Total** | " + " | ".join("" for _ in cats) + f" | **{br(total)}** | **100,0** |")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="comando", required=True)
    p = sub.add_parser("estimar", help="gera as linhas estimadas a partir do git blame")
    p.add_argument("--ref", required=True)
    p.add_argument("--entrega", default="E1")
    p.add_argument("--data", default="19/10/2026")
    p.set_defaults(func=estimar)
    p = sub.add_parser("calcular", help="soma as horas da planilha e calcula o percentual")
    p.add_argument("--entrega")
    p.set_defaults(func=calcular)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
