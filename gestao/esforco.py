"""Cálculo do esforço da equipe (indicador I3 da Gestão do Projeto).

Uso:
    python gestao/esforco.py calcular [--entrega E2] [--detalhado]   # horas e percentual por membro
    python gestao/esforco.py pr [--base origin/main] [--head HEAD] [--numero N]
                                                     # prévia do I3 de um PR (usada pelo GitHub Actions)
    python gestao/esforco.py estimar --ref <commit>  # método da Entrega 1, mantido para reprodução

A partir da Entrega 2 as horas do trabalho no repositório são estimadas automaticamente a partir
do histórico do Git: palavras realmente adicionadas nos textos e linhas adicionadas no código,
convertidas em horas pelas taxas de TAXAS, por integração na main (PR ou commit direto).
A planilha gestao/esforco.csv guarda só o que o Git não vê (reuniões, pesquisa) e a Entrega 1.
O mesmo arquivo é carregado como hook do MkDocs para montar o dashboard no build do site.

A metodologia está descrita em docs/contribuicao.md.
"""

import argparse
import csv
import html
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLANILHA = RAIZ / "gestao" / "esforco.csv"
URL_METODOLOGIA = "https://fcte-qualidade-de-software-1.github.io/2026-2_T02_ADELE_GOLDSTINE/contribuicao/"

MEMBROS = [
    "Arthur Carvalho Leite",
    "Caio Melo Borges",
    "Daniel Nunes Duarte",
    "Davi dos Santos Brito Nobre",
    "Felipe de Aquino Campêlo",
    "Leonardo Fachinello Bonetti",
]

# Login do GitHub de cada membro: identifica os e-mails noreply (<id>+<login>@users.noreply.github.com)
LOGINS = {
    "arthurlleite": "Arthur Carvalho Leite",
    "CaioMelo25": "Caio Melo Borges",
    "DanNunes777": "Daniel Nunes Duarte",
    "Jagaima": "Davi dos Santos Brito Nobre",
    "felipeacampelo": "Felipe de Aquino Campêlo",
    "LeoFacB": "Leonardo Fachinello Bonetti",
}

# E-mails pessoais usados nos commits (conferidos com a API do GitHub em 10/11/2026)
EMAILS = {
    "arthur.c.lleite@gmail.com": "Arthur Carvalho Leite",
    "caioborges250802@gmail.com": "Caio Melo Borges",
    "danielnunes.dnd2@gmail.com": "Daniel Nunes Duarte",
    "davinobre.ik@gmail.com": "Davi dos Santos Brito Nobre",
    "felipeaquinocamp@gmail.com": "Felipe de Aquino Campêlo",
    "leonardofbonetti@gmail.com": "Leonardo Fachinello Bonetti",
}


def membro_do_email(email):
    if email in EMAILS:
        return EMAILS[email]
    noreply = re.fullmatch(r"(?:\d+\+)?([^@]+)@users\.noreply\.github\.com", email)
    if noreply and noreply.group(1) in LOGINS:
        return LOGINS[noreply.group(1)]
    raise ValueError(f"E-mail de commit sem membro associado: {email!r}. Adicione-o em EMAILS ou LOGINS (gestao/esforco.py).")


# Taxas de produção de cada categoria de artefato: (unidades por hora, unidade)
TAXAS = {
    "redacao": (1100, "palavras"),  # páginas da GitPage: conteúdo original, com pesquisa e apoio de IA
    "consolidacao": (2200, "palavras"),  # artigo em LaTeX: reescrita de conteúdo já produzido nas páginas
    "infraestrutura": (100, "linhas"),  # scripts, workflows, estilos e configuração do site, com apoio de IA
}

# Revisão de PR: tempo fixo por revisor em cada PR (o mesmo da Entrega 1, Tabela 5 da metodologia)
# mais as palavras dos comentários de revisão, pela taxa de redação
HORAS_POR_REVISAO = 0.25
TAXA_COMENTARIOS = TAXAS["redacao"][0]

TEXTO = (".md", ".tex", ".bib")
CODIGO = (".py", ".yml", ".yaml", ".css", ".js", ".sh", ".html")
# Material copiado de terceiros, dados e arquivos gerados não medem esforço da equipe
IGNORADOS = ("artigo/modelo-ieee/", "site/", "gestao/esforco.csv")


def categoria(arquivo):
    """Categoria de esforço de um arquivo, ou None se ele não entra na medição."""
    if arquivo.startswith(IGNORADOS):
        return None
    if arquivo.endswith(TEXTO):
        return "consolidacao" if arquivo.startswith("artigo/") else "redacao"
    if arquivo.endswith(CODIGO):
        return "infraestrutura"
    return None


def git(*args):
    return subprocess.run(
        ["git", "-c", "core.quotePath=false", *args],
        cwd=RAIZ, capture_output=True, text=True, check=True,
    ).stdout


# ---------------------------------------------------------------------------
# Entrega 1: estimativa única, reconstruída do histórico (seção 3.3 da metodologia)
# ---------------------------------------------------------------------------

CAMINHOS_E1 = ["docs", "artigo/secoes", "artigo/artigo.tex", "artigo/bibliografia.bib"]


def palavras_adicionadas(ref):
    """Soma as palavras das linhas adicionadas por cada membro em cada arquivo, até `ref`.

    Método usado na Entrega 1 (linha inteira adicionada). Mantido sem alteração para que
    as linhas `estimada` de gestao/esforco.csv possam ser reproduzidas.
    """
    saida = git("log", ref, "--no-merges", "-w", "-p", "--format=COMMIT %ae", "--", *CAMINHOS_E1)
    contagem = defaultdict(int)
    autor = arquivo = None
    for linha in saida.splitlines():
        if linha.startswith("COMMIT "):
            try:
                autor = membro_do_email(linha.split(" ", 1)[1])
            except ValueError:
                autor = None
        elif linha.startswith("+++ "):
            arquivo = linha[6:] if linha.startswith("+++ b/") else None
        elif linha.startswith("+") and autor and arquivo and arquivo.endswith(TEXTO):
            contagem[(autor, arquivo)] += len(linha[1:].split())
    return contagem


def estimar(args):
    escritor = csv.writer(sys.stdout, lineterminator="\n")
    for (membro, arquivo), palavras in sorted(palavras_adicionadas(args.ref).items()):
        cat = categoria(arquivo)
        taxa = TAXAS[cat][0]
        escritor.writerow([
            args.entrega, args.data, membro, f"{palavras / taxa:.2f}", cat,
            f"{arquivo}: {palavras} palavras / {taxa} por hora",
            f"git log {args.ref[:7]}", "estimada",
        ])


# ---------------------------------------------------------------------------
# A partir da Entrega 2: estimativa automática por integração na main
# ---------------------------------------------------------------------------

# Cada entrega termina na tag Entrega<n> (a release). A Entrega 1 fica congelada na planilha.
ENTREGAS = ["E1", "E2"]
ENTREGAS_AUTOMATICAS = ["E2"]


def tag(entrega):
    return "Entrega" + entrega[1:]


def existe(ref):
    return subprocess.run(["git", "rev-parse", "-q", "--verify", f"{ref}^{{commit}}"],
                          cwd=RAIZ, capture_output=True).returncode == 0


def entrega_aberta():
    for e in ENTREGAS:
        if not existe(tag(e)):
            return e
    raise ValueError("Todas as entregas de ENTREGAS já têm tag; cadastre a próxima.")


def contar_palavras(texto):
    """Palavras com ao menos uma letra ou número (ignora |, ---, * e outros sinais de markdown)."""
    return sum(1 for p in texto.split() if any(c.isalnum() for c in p))


def arquivo_renomeado(caminho):
    """Destino de um caminho do --numstat com renomeação: 'a/{x => y}.py' ou 'x => y'."""
    if "=>" not in caminho:
        return caminho
    if "{" in caminho:
        return re.sub(r"\{[^{}]* => ([^{}]*)\}", r"\1", caminho).replace("//", "/")
    return caminho.split(" => ", 1)[1]


def medir(faixa, evidencia, data, entrega):
    """Registros automáticos dos commits de `faixa` (argumentos de revisão do git log)."""
    contagem = defaultdict(int)

    # Textos: só as palavras realmente adicionadas (--word-diff), não a linha inteira alterada
    saida = git("log", *faixa, "--no-merges", "-M", "-p", "--word-diff=porcelain", "--format=COMMIT %ae")
    email = arquivo = None
    cabecalho = False
    for linha in saida.splitlines():
        if linha.startswith("COMMIT "):
            email, arquivo, cabecalho = linha[7:], None, False
        elif linha.startswith("diff --git "):
            arquivo, cabecalho = None, True
        elif cabecalho:
            if linha.startswith("+++ "):
                arquivo = linha[6:] if linha.startswith("+++ b/") else None
            elif linha.startswith("@@"):
                cabecalho = False
        elif linha.startswith("+") and arquivo and categoria(arquivo) in ("redacao", "consolidacao"):
            palavras = contar_palavras(linha[1:])
            if palavras:
                contagem[(membro_do_email(email), arquivo)] += palavras

    # Código: linhas adicionadas
    saida = git("log", *faixa, "--no-merges", "-M", "--numstat", "--format=COMMIT %ae")
    for linha in saida.splitlines():
        if linha.startswith("COMMIT "):
            email = linha[7:]
            continue
        partes = linha.split("\t")
        if len(partes) != 3 or not partes[0].isdigit():
            continue  # linha vazia ou arquivo binário
        arquivo = arquivo_renomeado(partes[2])
        if categoria(arquivo) == "infraestrutura" and int(partes[0]):
            contagem[(membro_do_email(email), arquivo)] += int(partes[0])

    registros = []
    for (membro, arquivo), volume in sorted(contagem.items()):
        cat = categoria(arquivo)
        taxa, unidade = TAXAS[cat]
        horas = round(volume / taxa, 2)
        registros.append({
            "entrega": entrega, "data": data, "membro": membro, "horas": f"{horas:.2f}",
            "horas_num": horas, "categoria": cat,
            "descricao": f"{arquivo}: {volume} {unidade} / {taxa} por hora",
            "evidencia": evidencia, "origem": "automatica",
        })
    return registros


def integracoes(inicio, fim):
    """Cada entrada na main entre `inicio` e `fim`: (faixa de commits, evidência, data, PRs).

    PRs lista o PR integrado e os PRs integrados antes no mesmo ramo (por exemplo, o #8,
    integrado no ramo do #6), para buscar as revisões de todos.
    """
    saida = git("log", "--first-parent", "--date=format:%d/%m/%Y",
                "--format=%H %P%x09%cd%x09%s", f"{inicio}..{fim}")
    for linha in saida.splitlines():
        hashes, data, assunto = linha.split("\t", 2)
        commit, *pais = hashes.split()
        if len(pais) > 1:  # merge de PR: os commits do ramo integrado
            faixa = [f"{pais[0]}..{pais[1]}"]
            pr = re.search(r"Merge pull request #(\d+)", assunto)
            internos = re.findall(r"Merge pull request #(\d+)", git("log", "--merges", "--format=%s", *faixa))
            prs = ([pr.group(1)] if pr else []) + internos
            yield faixa, f"PR #{pr.group(1)}" if pr else f"merge {commit[:7]}", data, prs
        else:  # squash de PR ou commit direto na main
            pr = re.search(r"\(#(\d+)\)$", assunto)
            yield ["-1", commit], f"PR #{pr.group(1)}" if pr else f"commit {commit[:7]}", data, [pr.group(1)] if pr else []


# ---------------------------------------------------------------------------
# Revisões de PR (API do GitHub, via gh)
# ---------------------------------------------------------------------------

FUSO = timezone(timedelta(hours=-3))
AVISOS = set()


class RevisoesIndisponiveis(Exception):
    pass


def repositorio():
    if os.environ.get("GITHUB_REPOSITORY"):
        return os.environ["GITHUB_REPOSITORY"]
    url = git("remote", "get-url", "origin").strip()
    return re.search(r"github\.com[:/](.+?)(?:\.git)?$", url).group(1)


def api(caminho, jq=".[] | tojson"):
    """Resultado de um endpoint da API do GitHub (por padrão, os itens de uma lista, um JSON por linha)."""
    try:
        saida = subprocess.run(
            ["gh", "api", "--paginate", f"repos/{repositorio()}/{caminho}", "--jq", jq],
            cwd=RAIZ, capture_output=True, text=True, check=True,
        ).stdout
    except FileNotFoundError:
        raise RevisoesIndisponiveis("GitHub CLI (gh) não instalado") from None
    except subprocess.CalledProcessError as erro:
        raise RevisoesIndisponiveis(f"falha na API do GitHub ({caminho}): {erro.stderr.strip()}") from None
    if jq != ".[] | tojson":
        return saida.strip()
    return [json.loads(linha) for linha in saida.splitlines() if linha]


@lru_cache(maxsize=None)
def dados_do_pr(numero):
    """Autor do PR e manifestações de revisão: (login, palavras, data/hora) de cada uma."""
    autor = api(f"pulls/{numero}", jq=".user.login")
    manifestacoes = []
    for r in api(f"pulls/{numero}/reviews?per_page=100"):
        if r.get("submitted_at"):  # revisões pendentes ainda não foram enviadas
            manifestacoes.append((r["user"]["login"], contar_palavras(r.get("body") or ""), r["submitted_at"]))
    for c in api(f"pulls/{numero}/comments?per_page=100"):
        manifestacoes.append((c["user"]["login"], contar_palavras(c.get("body") or ""), c["created_at"]))
    return autor, tuple(manifestacoes)


def revisoes(numero, entrega):
    """Registros de revisão do PR: 0,25 h por revisor + palavras dos comentários."""
    autor, manifestacoes = dados_do_pr(numero)
    por_revisor = {}
    for login, palavras, quando in manifestacoes:
        if login == autor or login not in LOGINS:  # o autor responde à revisão; bots e a professora não são membros
            continue
        data = datetime.fromisoformat(quando.replace("Z", "+00:00")).astimezone(FUSO)
        anterior = por_revisor.get(login, (0, data))
        por_revisor[login] = (anterior[0] + palavras, min(anterior[1], data))
    registros = []
    fixas = f"{HORAS_POR_REVISAO:.2f}".replace(".", ",")
    for login, (palavras, data) in sorted(por_revisor.items()):
        horas = round(HORAS_POR_REVISAO + palavras / TAXA_COMENTARIOS, 2)
        registros.append({
            "entrega": entrega, "data": data.strftime("%d/%m/%Y"), "membro": LOGINS[login],
            "horas": f"{horas:.2f}", "horas_num": horas, "categoria": "revisao",
            "descricao": f"Revisão do PR #{numero}: {fixas} h fixas + "
                         f"{palavras} palavras de comentários / {TAXA_COMENTARIOS} por hora",
            "evidencia": f"PR #{numero}", "origem": "automatica",
        })
    return registros


def revisoes_dos_prs(numeros, entrega):
    """Revisões de vários PRs. No GitHub Actions a falha da API interrompe o cálculo;
    fora dele, o cálculo segue sem as revisões e avisa."""
    try:
        return [r for n in numeros for r in revisoes(n, entrega)]
    except RevisoesIndisponiveis as erro:
        if os.environ.get("GITHUB_ACTIONS") == "true":
            raise
        AVISOS.add(f"Revisões de PR não incluídas: {erro}. Rode 'gh auth login' para incluí-las.")
        return []


def automaticas(entrega, ate="HEAD"):
    if git("rev-parse", "--is-shallow-repository").strip() == "true":
        raise RuntimeError("Histórico do Git incompleto (clone raso): use fetch-depth: 0 no actions/checkout.")
    anterior = ENTREGAS[ENTREGAS.index(entrega) - 1]
    if not existe(tag(anterior)):
        raise RuntimeError(f"Tag {tag(anterior)} não encontrada: rode git fetch --tags. Ela marca o início da {entrega}.")
    fim = tag(entrega) if existe(tag(entrega)) else ate
    registros = []
    for faixa, evidencia, data, prs in integracoes(tag(anterior), fim):
        registros += medir(faixa, evidencia, data, entrega)
        registros += revisoes_dos_prs(prs, entrega)
    return registros


# ---------------------------------------------------------------------------
# Planilha (trabalho fora do Git e Entrega 1) e cálculo do indicador
# ---------------------------------------------------------------------------

def ler_planilha():
    """Linhas validadas da planilha: uma linha inválida interrompe o cálculo e o build do site."""
    registros = []
    with PLANILHA.open(encoding="utf-8", newline="") as f:
        for numero, linha in enumerate(csv.DictReader(f), start=2):
            local = f"esforco.csv, linha {numero}"
            membro = (linha.get("membro") or "").strip()
            if membro not in MEMBROS:
                raise ValueError(f"{local}: membro não cadastrado em MEMBROS: {membro!r}")
            if linha.get("entrega") not in ENTREGAS:
                raise ValueError(f"{local}: entrega desconhecida: {linha.get('entrega')!r}")
            try:
                horas = float((linha.get("horas") or "").strip().replace(",", "."))
            except ValueError:
                raise ValueError(f"{local}: horas inválidas: {linha.get('horas')!r}") from None
            try:
                datetime.strptime(linha.get("data") or "", "%d/%m/%Y")
            except ValueError:
                raise ValueError(f"{local}: data fora do formato dd/mm/aaaa: {linha.get('data')!r}") from None
            registros.append({**linha, "membro": membro, "horas_num": horas})
    return registros


def todos_registros(entrega=None, ate="HEAD"):
    """Planilha + estimativa automática do Git, opcionalmente filtrados por entrega."""
    registros = [r for r in ler_planilha() if not entrega or r["entrega"] == entrega]
    for e in ENTREGAS_AUTOMATICAS:
        if not entrega or e == entrega:
            registros += automaticas(e, ate)
    return registros


def somar(registros):
    horas = {m: 0.0 for m in MEMBROS}
    por_categoria = defaultdict(lambda: defaultdict(float))
    for r in registros:
        horas[r["membro"]] += r["horas_num"]
        por_categoria[r["membro"]][r["categoria"]] += r["horas_num"]
    return horas, por_categoria


def percentuais(horas):
    """Percentuais com uma casa decimal que somam exatamente 100,0 (maiores restos)."""
    total = sum(horas.values())
    exatos = {m: h / total * 1000 for m, h in horas.items()}
    base = {m: int(v) for m, v in exatos.items()}
    sobra = 1000 - sum(base.values())
    for m in sorted(exatos, key=lambda m: exatos[m] - base[m], reverse=True)[:sobra]:
        base[m] += 1
    return {m: v / 10 for m, v in base.items()}


def fora_da_faixa(pct):
    return pct < 10 or pct > 40


def br(valor):
    return f"{valor:.1f}".replace(".", ",")


def _data(registro):
    return datetime.strptime(registro["data"], "%d/%m/%Y")


def calcular(args):
    registros = todos_registros(args.entrega)
    horas, por_categoria = somar(registros)
    total = sum(horas.values())
    if not total:
        print(f"Nenhuma hora registrada para a entrega {args.entrega}." if args.entrega else "Nenhuma hora registrada.")
        return
    cats = sorted({c for m in por_categoria.values() for c in m})
    pct = percentuais(horas)
    print("| Membro | " + " | ".join(cats) + " | Horas | Esforço (%) |")
    print("| ------ | " + " | ".join(":-:" for _ in cats) + " | :-: | :-: |")
    for m in MEMBROS:
        colunas = [br(por_categoria[m][c]) for c in cats]
        alerta = " ⚠" if fora_da_faixa(pct[m]) else ""
        print(f"| {m} | " + " | ".join(colunas) + f" | {br(horas[m])} | {br(pct[m])}{alerta} |")
    print("| **Total** | " + " | ".join("" for _ in cats) + f" | **{br(total)}** | **100,0** |")
    for aviso in sorted(AVISOS):
        print(f"⚠ {aviso}", file=sys.stderr)

    if args.detalhado:
        def texto(valor):
            return str(valor or "").replace("|", "\\|").replace("\n", " ").strip()
        print("\n### Registros atribuídos por integrante")
        print("\n| Integrante | Data | Categoria | Atividade | Evidência | Horas | Origem |")
        print("|---|---|---|---|---|---:|---|")
        for r in sorted(registros, key=lambda r: (MEMBROS.index(r["membro"]), _data(r))):
            print(f"| {texto(r['membro'])} | {texto(r['data'])} | {texto(r['categoria'])} | "
                  f"{texto(r['descricao'])} | {texto(r['evidencia'])} | {br(r['horas_num'])} | "
                  f"{texto(r['origem'])} |")


# ---------------------------------------------------------------------------
# Comentário do GitHub Actions no PR
# ---------------------------------------------------------------------------

MARCADOR_COMENTARIO = "<!-- esforco-pr -->"


def comentario_pr(args):
    entrega = entrega_aberta()
    evidencia = f"PR #{args.numero}" if args.numero else "este PR"
    do_pr = medir([f"{args.base}..{args.head}"], evidencia, date.today().strftime("%d/%m/%Y"), entrega)
    if args.numero:
        do_pr += revisoes_dos_prs([args.numero], entrega)
    antes = todos_registros(entrega, ate=args.base)
    horas_pr, _ = somar(do_pr)
    horas_antes, _ = somar(antes)
    horas_depois, _ = somar(antes + do_pr)

    linhas = [MARCADOR_COMENTARIO, f"### Esforço estimado deste PR (I3, {entrega})", ""]
    if not do_pr:
        linhas.append("Este PR não altera textos nem código medidos e ainda não tem revisões, então não soma horas automáticas.")
        print("\n".join(linhas))
        return

    linhas += [
        f"Estimativa automática a partir das palavras e linhas adicionadas em cada commit e das revisões do PR, pela "
        f"[metodologia de contribuição]({URL_METODOLOGIA}). Quem revisa o PR valida esta estimativa.",
        "", "| Membro | Horas neste PR |", "| ------ | :-: |",
    ]
    for m in MEMBROS:
        if horas_pr[m]:
            alerta = " ⚠ acima de 4 h: justificar na revisão" if horas_pr[m] > 4 else ""
            linhas.append(f"| {m} | {br(horas_pr[m])}{alerta} |")
    linhas.append(f"| **Total** | **{br(sum(horas_pr.values()))}** |")

    linhas += ["", f"**Participação na {entrega} se o PR for integrado**", "",
               "| Membro | Horas antes | Horas depois | Esforço (%) |", "| ------ | :-: | :-: | :-: |"]
    pct = percentuais(horas_depois)
    for m in MEMBROS:
        alerta = " ⚠" if fora_da_faixa(pct[m]) else ""
        linhas.append(f"| {m} | {br(horas_antes[m])} | {br(horas_depois[m])} | {br(pct[m])}{alerta} |")
    linhas += ["", "⚠ fora da faixa de 10% a 40% do critério de decisão do I3.", "",
               "<details><summary>Detalhamento por arquivo</summary>", "",
               "| Membro | Categoria | Arquivo e volume | Horas |", "| ------ | --------- | ---------------- | :-: |"]
    for r in do_pr:
        linhas.append(f"| {r['membro']} | {r['categoria']} | {r['descricao']} | {br(r['horas_num'])} |")
    linhas += ["", "</details>"]
    print("\n".join(linhas))


# ---------------------------------------------------------------------------
# Dashboard do site (hook do MkDocs)
# ---------------------------------------------------------------------------

MARCADOR_DASHBOARD = "[[DASHBOARD_ESFORCO]]"


def _html(texto):
    return html.escape(str(texto or ""), quote=True)


def dashboard_markdown(repo_url=""):
    """Monta o painel HTML com a planilha e a estimativa automática do Git."""
    entregas = defaultdict(list)
    for r in todos_registros():
        entregas[r["entrega"]].append(r)

    if not entregas:
        return '<p class="esforco-vazio">Ainda não há contribuições registradas.</p>'

    blocos = ['<div class="esforco-dashboard">']
    for aviso in sorted(AVISOS):
        print(f"esforco.py: {aviso}", file=sys.stderr)
        blocos.append(f'<p class="esforco-vazio">⚠ {_html(aviso)}</p>')
    for entrega in sorted(entregas):
        registros = entregas[entrega]
        totais, categorias = somar(registros)
        origens = defaultdict(float)
        for r in registros:
            origens[(r.get("origem") or "não informada").strip()] += r["horas_num"]

        total = sum(totais.values())
        pct = percentuais(totais) if total else {m: 0.0 for m in MEMBROS}
        maior = max((max(0, h) for h in totais.values()), default=0) or 1
        atualizado = max(map(_data, registros)).strftime("%d/%m/%Y")

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
            situacao = "fora da faixa" if fora_da_faixa(pct[membro]) else "dentro da faixa"
            classe = " fora-limite" if fora_da_faixa(pct[membro]) else ""
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

        planilha = "<code>gestao/esforco.csv</code>"
        if repo_url:
            planilha = f'<a href="{_html(repo_url.rstrip("/") + "/blob/main/gestao/esforco.csv")}">gestao/esforco.csv</a>'
        blocos.append(f'<p class="esforco-fonte">Fonte: histórico do Git e revisões dos PRs (origem automatica) e {planilha}. '
                      'Atualização calculada durante a publicação do site.</p>')
        blocos.append('</section>')
    blocos.append('</div>')
    return "\n".join(blocos)


def on_page_markdown(markdown, page, config, files):
    """Hook MkDocs: substitui o marcador do dashboard pelos dados de esforço."""
    if MARCADOR_DASHBOARD in markdown:
        markdown = markdown.replace(MARCADOR_DASHBOARD, dashboard_markdown(config.get("repo_url", "")))
    return markdown


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="comando", required=True)
    p = sub.add_parser("calcular", help="soma as horas (planilha + Git) e calcula o percentual")
    p.add_argument("--entrega", choices=ENTREGAS)
    p.add_argument("--detalhado", action="store_true",
                   help="inclui cada registro, atribuído ao integrante correspondente")
    p.set_defaults(func=calcular)
    p = sub.add_parser("pr", help="comentário com a prévia do I3 para um PR")
    p.add_argument("--base", default="origin/main")
    p.add_argument("--head", default="HEAD")
    p.add_argument("--numero")
    p.set_defaults(func=comentario_pr)
    p = sub.add_parser("estimar", help="método da Entrega 1: gera as linhas estimadas até um commit")
    p.add_argument("--ref", required=True)
    p.add_argument("--entrega", default="E1")
    p.add_argument("--data", default="19/10/2026")
    p.set_defaults(func=estimar)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
