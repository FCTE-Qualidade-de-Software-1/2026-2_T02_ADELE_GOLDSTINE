"""Cálculo do esforço da equipe (indicador I3 da Gestão do Projeto).

Uso:
    python gestao/esforco.py estimar --ref <commit>   # reconstrói as horas a partir do git blame
    python gestao/esforco.py calcular [--entrega E1] [--detalhado]
                                                   # horas e registros atribuídos por membro

A metodologia está descrita em docs/contribuicao.md.
"""

import argparse
import csv
import html
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
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


MARCADOR_DASHBOARD = "[[DASHBOARD_ESFORCO]]"


def _html(texto):
    return html.escape(str(texto or ""), quote=True)


def dashboard_markdown(repo_url=""):
    """Monta o painel HTML a partir do esquema existente de gestao/esforco.csv."""
    entregas = defaultdict(list)
    with PLANILHA.open(encoding="utf-8", newline="") as f:
        # Mesmas validações do comando calcular: uma linha inválida interrompe o build do
        # site em vez de ser descartada, para o painel nunca divergir da tabela de contribuição.
        for numero, linha in enumerate(csv.DictReader(f), start=2):
            membro = (linha.get("membro") or "").strip()
            if membro not in MEMBROS:
                raise ValueError(f"esforco.csv, linha {numero}: membro não cadastrado em MEMBROS: {membro!r}")
            try:
                horas = float((linha.get("horas") or "").strip().replace(",", "."))
            except ValueError:
                raise ValueError(f"esforco.csv, linha {numero}: horas inválidas: {linha.get('horas')!r}") from None
            entregas[(linha.get("entrega") or "Sem entrega").strip()].append(
                {**linha, "membro": membro, "horas_num": horas}
            )

    if not entregas:
        return '<p class="esforco-vazio">Ainda não há contribuições registradas em <code>gestao/esforco.csv</code>.</p>'

    blocos = ['<div class="esforco-dashboard">']
    for entrega in sorted(entregas):
        registros = entregas[entrega]
        totais = {m: 0.0 for m in MEMBROS}
        categorias = defaultdict(lambda: defaultdict(float))
        origens = defaultdict(float)
        for r in registros:
            totais[r["membro"]] += r["horas_num"]
            categorias[r["membro"]][r.get("categoria", "") or "sem categoria"] += r["horas_num"]
            origens[(r.get("origem") or "não informada").strip()] += r["horas_num"]

        total = sum(totais.values())
        pct = percentuais(totais) if total else {m: 0.0 for m in MEMBROS}
        maior = max((max(0, h) for h in totais.values()), default=0) or 1
        datas = []
        for r in registros:
            try:
                datas.append(datetime.strptime(r.get("data", ""), "%d/%m/%Y"))
            except ValueError:
                pass
        atualizado = max(datas).strftime("%d/%m/%Y") if datas else "data não informada"

        blocos += [f'<section class="esforco-entrega"><h2>{_html(entrega)}</h2>',
                   '<div class="esforco-kpis">',
                   f'<div class="esforco-kpi"><span>Horas líquidas</span><strong>{br(total)} h</strong></div>',
                   f'<div class="esforco-kpi"><span>Integrantes</span><strong>{sum(h != 0 for h in totais.values())} / {len(MEMBROS)}</strong></div>',
                   f'<div class="esforco-kpi"><span>Registros</span><strong>{len(registros)}</strong></div>',
                   f'<div class="esforco-kpi"><span>Última data registrada</span><strong>{atualizado}</strong></div>',
                   '</div>',
                   '<h3>Participação por integrante</h3>',
                   '<div class="esforco-grafico" role="img" aria-label="Horas atribuídas por integrante">']

        for membro in MEMBROS:
            valor = totais[membro]
            largura = min(100, max(0, valor / maior * 100))
            situacao = "dentro da faixa" if 10 <= pct[membro] <= 40 else "fora da faixa"
            classe = "" if situacao == "dentro da faixa" else " fora-limite"
            blocos.append(
                '<div class="esforco-linha-grafico">'
                f'<span class="esforco-nome">{_html(membro)}</span>'
                f'<div class="esforco-trilho"><span class="esforco-barra{classe}" '
                f'style="width:{largura:.2f}%"></span></div>'
                f'<span class="esforco-valor">{br(valor)} h · {br(pct[membro])}% · {situacao}</span></div>'
            )
        blocos.append('</div>')

        blocos += ['<h3>Resumo por integrante e categoria</h3>',
                   '<div class="esforco-tabela-wrap"><table class="esforco-tabela">',
                   '<thead><tr><th>Integrante</th><th>Horas</th><th>Participação</th><th>Atividades por categoria</th></tr></thead><tbody>']
        for membro in MEMBROS:
            grupos = sorted(categorias[membro].items(), key=lambda par: (-abs(par[1]), par[0]))
            atividade = "<ul>" + "".join(
                f"<li>{_html(cat.replace('-', ' ').capitalize())}: {br(h)} h</li>" for cat, h in grupos
            ) + "</ul>" if grupos else "—"
            blocos.append(
                f'<tr><th scope="row">{_html(membro)}</th><td>{br(totais[membro])} h</td>'
                f'<td>{br(pct[membro])}%</td><td>{atividade}</td></tr>'
            )
        blocos.append(f'<tr class="esforco-total"><th scope="row">Total</th><td>{br(total)} h</td><td>100,0%</td><td>{len(registros)} registros</td></tr>')
        blocos.append('</tbody></table></div>')

        blocos += ['<h3>Origem dos registros</h3><ul class="esforco-origens">']
        for origem, h in sorted(origens.items()):
            blocos.append(f'<li><strong>{_html(origem.capitalize())}</strong>: {br(h)} h</li>')
        blocos.append('</ul>')

        if repo_url:
            blocos.append(f'<p class="esforco-fonte">Fonte: <a href="{_html(repo_url.rstrip("/") + "/blob/main/gestao/esforco.csv")}">gestao/esforco.csv</a>. Atualização calculada durante a publicação do site.</p>')
        else:
            blocos.append('<p class="esforco-fonte">Fonte: <code>gestao/esforco.csv</code>. Atualização calculada durante a publicação do site.</p>')
        blocos.append('</section>')
    blocos.append('</div>')
    return "\n".join(blocos)


def on_page_markdown(markdown, page, config, files):
    """Hook MkDocs: substitui o marcador do dashboard com dados do CSV do projeto."""
    if MARCADOR_DASHBOARD in markdown:
        markdown = markdown.replace(MARCADOR_DASHBOARD, dashboard_markdown(config.get("repo_url", "")))
    return markdown


def calcular(args):
    horas = {m: 0.0 for m in MEMBROS}
    por_categoria = defaultdict(lambda: defaultdict(float))
    registros = []
    with open(PLANILHA, encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            if args.entrega and linha["entrega"] != args.entrega:
                continue
            membro = linha["membro"].strip()
            if membro not in horas:
                raise ValueError(f"Membro não cadastrado em MEMBROS: {membro!r}")
            h = float(linha["horas"].strip().replace(",", "."))
            horas[membro] += h
            por_categoria[membro][linha["categoria"]] += h
            registros.append({**linha, "membro": membro, "horas_num": h})
    total = sum(horas.values())
    if not total:
        print(f"Nenhuma hora registrada para a entrega {args.entrega}." if args.entrega else "Nenhuma hora registrada na planilha.")
        return
    cats = sorted({c for m in por_categoria.values() for c in m})
    pct = percentuais(horas)
    print("| Membro | " + " | ".join(cats) + " | Horas | Esforço (%) |")
    print("| ------ | " + " | ".join(":-:" for _ in cats) + " | :-: | :-: |")
    for m in MEMBROS:
        colunas = [br(por_categoria[m][c]) for c in cats]
        alerta = " ⚠" if pct[m] < 10 or pct[m] > 40 else ""
        print(f"| {m} | " + " | ".join(colunas) + f" | {br(horas[m])} | {br(pct[m])}{alerta} |")
    print("| **Total** | " + " | ".join("" for _ in cats) + f" | **{br(total)}** | **100,0** |")

    if args.detalhado:
        print("\n### Registros atribuídos por integrante")
        print("\n| Integrante | Data | Categoria | Atividade | Evidência | Horas | Origem |")
        print("|---|---|---|---|---|---:|---|")
        for linha in sorted(registros, key=lambda l: (MEMBROS.index(l["membro"]), datetime.strptime(l["data"], "%d/%m/%Y"))):
            texto = lambda valor: str(valor or "").replace("|", "\\|").replace("\n", " ").strip()
            print(f"| {texto(linha['membro'])} | {texto(linha['data'])} | {texto(linha['categoria'])} | "
                  f"{texto(linha['descricao'])} | {texto(linha['evidencia'])} | {br(linha['horas_num'])} | "
                  f"{texto(linha['origem'])} |")


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
    p.add_argument("--detalhado", action="store_true",
                   help="inclui cada registro, atribuído ao integrante correspondente")
    p.set_defaults(func=calcular)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
