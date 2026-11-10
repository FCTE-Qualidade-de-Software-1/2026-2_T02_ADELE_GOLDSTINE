"""Rascunho não ativado: hook MkDocs para o novo formato de horas.csv.

Planilha esperada em dados/gestao/horas.csv, com cabeçalho:
    data,membro,atividade,issue,horas

Para ativar no futuro, copiar para o local de hooks escolhido, configurar o hook
no mkdocs.yml e incluir [[TABELA_HORAS]] na página desejada. Este arquivo não é
carregado pelo site enquanto permanecer nesta pasta.
"""

import csv
from collections import defaultdict
from pathlib import Path


MARCADOR_HORAS = "[[TABELA_HORAS]]"
CAMPOS_OBRIGATORIOS = {"data", "membro", "atividade", "issue", "horas"}


def _numero(valor):
    return float(str(valor or "0").strip().replace(",", "."))


def _horas(valor):
    return f"{valor:.2f}".rstrip("0").rstrip(".").replace(".", ",") + " h"


def _data(valor):
    partes = str(valor or "").strip().split("-")
    if len(partes) == 3 and len(partes[0]) == 4:
        return f"{partes[2]}/{partes[1]}/{partes[0]}"
    return str(valor or "")


def _link_issue(valor, repo_url):
    numero = str(valor or "").strip().lstrip("#")
    if numero.isdigit() and repo_url:
        return f"[#{numero}]({repo_url.rstrip('/')}/issues/{numero})"
    return f"#{numero}" if numero.isdigit() else str(valor or "—").strip()


def gerar_tabela(markdown, config):
    """Substitui [[TABELA_HORAS]] por resumo e registros individuais."""
    if MARCADOR_HORAS not in markdown:
        return markdown

    raiz = Path(config["config_file_path"]).parent
    planilha = raiz / "dados" / "gestao" / "horas.csv"
    repo_url = config.get("repo_url") or ""
    extra = config.get("extra", {}) or {}
    custo_hora = float(extra.get("custo_hora", 0))

    if not planilha.exists():
        return markdown.replace(
            MARCADOR_HORAS,
            "_Planilha `dados/gestao/horas.csv` ainda não encontrada._",
        )

    with planilha.open(encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        campos = set(leitor.fieldnames or [])
        ausentes = CAMPOS_OBRIGATORIOS - campos
        if ausentes:
            detalhe = ", ".join(sorted(ausentes))
            return markdown.replace(
                MARCADOR_HORAS,
                f"_Formato de `dados/gestao/horas.csv` inválido; faltam as colunas: {detalhe}._",
            )
        linhas = []
        for numero_linha, linha in enumerate(leitor, start=2):
            membro = (linha.get("membro") or "").strip()
            if not membro:
                continue
            try:
                horas = _numero(linha.get("horas"))
            except ValueError:
                continue
            linhas.append({**linha, "membro": membro, "_horas": horas,
                           "_linha": numero_linha})

    linhas.sort(key=lambda linha: (linha.get("data") or "", linha["_linha"]))
    por_membro = defaultdict(float)
    for linha in linhas:
        por_membro[linha["membro"]] += linha["_horas"]
    total = sum(por_membro.values())

    saida = [
        "## Horas e custo por integrante", "",
        "| Integrante | Horas | % do total | Custo |",
        "|---|---:|---:|---:|",
    ]
    for membro, horas in sorted(por_membro.items(), key=lambda item: (-item[1], item[0].casefold())):
        percentual = horas / total * 100 if total else 0
        custo = horas * custo_hora
        saida.append(
            f"| {membro} | {_horas(horas)} | {percentual:.1f}% | R$ {custo:.2f} |"
        )
    custo_total = total * custo_hora
    percentual_total = "100%" if total else "0%"
    saida.append(
        f"| **Total** | **{_horas(total)}** | **{percentual_total}** | **R$ {custo_total:.2f}** |"
    )
    saida += [
        "", "## Registro de horas", "",
        "| Data | Integrante | Atividade | Issue | Horas |",
        "|---|---|---|---|---:|",
    ]
    for linha in linhas:
        atividade = (linha.get("atividade") or "").replace("|", "\\|").replace("\n", " ")
        saida.append(
            f"| {_data(linha.get('data'))} | {linha['membro']} | {atividade} | "
            f"{_link_issue(linha.get('issue'), repo_url)} | {_horas(linha['_horas'])} |"
        )

    return markdown.replace(MARCADOR_HORAS, "\n".join(saida))


def on_page_markdown(markdown, page, config, files):
    """Ponto de entrada do hook MkDocs, caso o rascunho seja ativado."""
    return gerar_tabela(markdown, config)
