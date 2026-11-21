"""Gráficos dos resultados do teste com usuários e do questionário.

Lê os mesmos dados de ``dados/`` usados por ``coleta/calcular_testes.py`` e desenha gráficos SVG,
sem bibliotecas externas, com a paleta do site (variáveis --viz-* de docs/stylesheets/extra.css;
fora do site valem as cores de reserva do tema claro).

Dois usos:
- hook do MkDocs: o marcador ``[[GRAFICO_TU:<nome>]]`` numa página vira o gráfico, com legenda e
  tabela com os dados (tema claro e escuro);
- linha de comando: ``python coleta/graficos_testes.py`` grava cada gráfico em
  ``docs/assets/graficos/teste-usuarios/<nome>.svg`` (com título, para os slides) e, com ``--png``,
  também em PNG, renderizado pelo Google Chrome em modo headless.
"""

from __future__ import annotations

import csv
import re
import statistics as st
import subprocess
import sys
import tempfile
from html import escape
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
TESTES = RAIZ / "dados/brutos/testes-usuarios"
QUEST = RAIZ / "dados/brutos/questionario"
REF = RAIZ / "dados/referencia"
METRICAS = RAIZ / "dados/consolidados/metricas.csv"
SAIDA = RAIZ / "docs/assets/graficos/teste-usuarios"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

LARGURA = 720
TAREFAS = ["T1", "T2", "T3", "T4", "T5", "T6"]
NOME_TAREFA = {
    "T1": "T1 Notas", "T2": "T2 Horário e local", "T3": "T3 Atestado",
    "T4": "T4 O que falta para formar", "T5": "T5 Material da turma", "T6": "T6 Calendário",
}
# Cores de reserva (tema claro) das variáveis --viz-* do site
RESERVA = {1: "#2a78d6", 2: "#eb6834", 3: "#1baf7a", 4: "#eda100", 5: "#e87ba4", 6: "#008300", 7: "#6250d6", 8: "#e34948"}
TEXTO = "var(--md-default-fg-color--light, #52514e)"
TINTA = "var(--md-default-fg-color, #0b0b0b)"
FUNDO = "var(--md-default-bg-color, #fcfcfb)"

ESTILO = (
    "<style>"
    ".tu text{font-family:var(--md-text-font-family,-apple-system,'Helvetica Neue',Arial,sans-serif);"
    f"font-size:12px;fill:{TEXTO}}}"
    f".tu .tinta{{fill:{TINTA}}}"
    f".tu .forte{{fill:{TINTA};font-weight:700}}"
    ".tu .num{font-variant-numeric:tabular-nums}"
    f".tu .valor{{fill:{TINTA};font-variant-numeric:tabular-nums;paint-order:stroke;stroke:{FUNDO};"
    "stroke-width:3px;stroke-linejoin:round}"
    ".tu .grade{stroke:var(--viz-grade,#e1e0d9);stroke-width:1}"
    ".tu .base{stroke:var(--viz-base,#c3c2b7);stroke-width:1}"
    ".tu .limite{stroke:var(--viz-limite,#52514e);stroke-width:1.5;stroke-dasharray:5 4}"
    f".tu .fundo{{fill:{FUNDO}}}"
    f".tu .anel{{stroke:{FUNDO};stroke-width:2}}"
    ".tu .alvo{fill:transparent;pointer-events:all}"
    ".tu .alvo:hover{fill:var(--md-default-fg-color--lightest,#0000001a);fill-opacity:.35}"
    + "".join(f".tu .s{k}{{fill:var(--viz-{k},{c})}}.tu .l{k}{{stroke:var(--viz-{k},{c})}}" for k, c in RESERVA.items())
    + ".tu .ruim{fill:#e34948}.tu .bom{fill:#2a78d6}"
    "</style>"
)


# ---------------------------------------------------------------------------
# Utilitários
# ---------------------------------------------------------------------------

def _e(t) -> str:
    return escape(str(t), quote=True)


def num(v, casas=1) -> str:
    return f"{v:.{casas}f}".replace(".", ",")


def pct(v) -> str:
    return f"{v * 100:.0f}%" if abs(v * 100 - round(v * 100)) < 0.05 else f"{num(v * 100)}%"


def ler(caminho: Path) -> list[dict]:
    if not caminho.exists():
        return []
    with caminho.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def barra_h(x0, y, largura, altura, classe, r=4, titulo=""):
    """Barra horizontal ancorada à esquerda, com a ponta direita arredondada."""
    if largura <= 0:
        return ""
    r = min(r, largura, altura / 2)
    x1 = x0 + largura
    t = f"<title>{_e(titulo)}</title>" if titulo else ""
    return (f'<path class="{classe}" d="M{x0:.1f},{y:.1f} H{x1 - r:.1f} Q{x1:.1f},{y:.1f} {x1:.1f},{y + r:.1f} '
            f'V{y + altura - r:.1f} Q{x1:.1f},{y + altura:.1f} {x1 - r:.1f},{y + altura:.1f} H{x0:.1f} Z">{t}</path>')


def segmento(x0, y, largura, altura, classe, ultimo, titulo=""):
    """Segmento de barra empilhada: só o último tem a ponta arredondada."""
    if largura <= 0:
        return ""
    if ultimo:
        return barra_h(x0, y, largura, altura, classe, titulo=titulo)
    return (f'<rect class="{classe}" x="{x0:.1f}" y="{y:.1f}" width="{largura:.1f}" height="{altura:.1f}">'
            f"<title>{_e(titulo)}</title></rect>")


def legenda_svg(itens, x, y, forma="quadrado") -> str:
    """Legenda desenhada no SVG (versão para slides): [(rótulo, slot)]."""
    partes, cx = [], x
    for rotulo, slot in itens:
        if forma == "ponto":
            partes.append(f'<circle class="s{slot}" cx="{cx + 6}" cy="{y - 4}" r="5"/>')
        else:
            partes.append(f'<rect class="s{slot}" x="{cx}" y="{y - 10}" width="12" height="12" rx="3"/>')
        partes.append(f'<text x="{cx + 18}" y="{y}">{_e(rotulo)}</text>')
        cx += 30 + len(rotulo) * 6.6
    return "".join(partes)


def legenda_html(itens, forma="quadrado") -> str:
    lis = "".join(
        f'<li><span class="viz-amostra viz-{"quadrado" if forma != "traco" else "traco"}" '
        f'style="--c:var(--viz-{slot})"></span>{_e(rotulo)}</li>' for rotulo, slot in itens)
    return f'<ul class="viz-legenda">{lis}</ul>'


def tabela_html(cabecalho, linhas) -> str:
    th = "".join(f"<th>{_e(c)}</th>" for c in cabecalho)
    tr = "".join("<tr>" + "".join(f"<td>{_e(c)}</td>" for c in l) + "</tr>" for l in linhas)
    return (f'<details class="viz-dados"><summary>Ver os dados do gráfico</summary><div class="viz-tabela-wrap">'
            f"<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div></details>")


class Grafico:
    """Um gráfico: corpo SVG desenhado a partir de y0, com legenda, nota e tabela."""

    def __init__(self, nome, titulo, pergunta, desenhar, legenda=None, forma_legenda="quadrado",
                 nota="", tabela=None):
        self.nome, self.titulo, self.pergunta = nome, titulo, pergunta
        self.desenhar = desenhar  # função (y0) -> (corpo_svg, altura_total)
        self.legenda = legenda or []
        self.forma_legenda = forma_legenda
        self.nota, self.tabela = nota, tabela

    def svg(self, para_slide=False) -> str:
        y0 = 0
        cab = ""
        if para_slide:
            y0 = 62 + (26 if self.legenda else 0)
            cab = (f'<text class="forte" x="16" y="26" style="font-size:17px">{_e(self.titulo)}</text>'
                   f'<text x="16" y="48" style="font-size:13px">{_e(self.pergunta)}</text>')
            if self.legenda:
                cab += legenda_svg(self.legenda, 16, 76, self.forma_legenda)
        corpo, altura = self.desenhar(y0)
        rodape = ""
        if para_slide and self.nota:
            altura += 10
            for i, linha in enumerate(_quebrar(_sem_tags(self.nota), 118)):
                rodape += f'<text x="16" y="{altura + 14 * i}" style="font-size:11px">{_e(linha)}</text>'
            altura += 14 * len(_quebrar(_sem_tags(self.nota), 118)) + 6
        fundo = f'<rect class="fundo" x="0" y="0" width="{LARGURA}" height="{altura}"/>' if para_slide else ""
        return (f'<svg xmlns="http://www.w3.org/2000/svg" class="tu" viewBox="0 0 {LARGURA} {altura}" '
                f'width="{LARGURA}" height="{altura}" role="img" aria-label="{_e(self.titulo)}" '
                f'preserveAspectRatio="xMinYMin meet">{ESTILO}{fundo}{cab}{corpo}{rodape}</svg>')

    def html(self) -> str:
        svg = self.svg().replace(f'width="{LARGURA}" height=', 'data-h=', 1)
        legenda = legenda_html(self.legenda, self.forma_legenda) if self.legenda else ""
        nota = f'<p class="viz-nota">{self.nota}</p>' if self.nota else ""
        tabela = tabela_html(*self.tabela) if self.tabela else ""
        return (f'<figure class="viz"><figcaption class="viz-titulo">{_e(self.titulo)}</figcaption>'
                f'<p class="viz-nota" style="margin:0 0 .3rem">{_e(self.pergunta)}</p>{legenda}'
                f'<div class="viz-scroll">{svg}</div>{nota}{tabela}</figure>')


def _sem_tags(t):
    return re.sub(r"<[^>]+>", "", t)


def _quebrar(texto, n):
    linhas, atual = [], ""
    for p in texto.split():
        if len(atual) + len(p) + 1 > n:
            linhas.append(atual)
            atual = p
        else:
            atual = f"{atual} {p}".strip()
    return linhas + ([atual] if atual else [])


# ---------------------------------------------------------------------------
# Dados
# ---------------------------------------------------------------------------

def dados():
    sess = ler(TESTES / "sessoes.csv")
    return {
        "sess": sess,
        "comp": ler(TESTES / "compreensao.csv"),
        "sus": ler(TESTES / "sus.csv"),
        "resp": ler(QUEST / "respostas.csv"),
        "erros": ler(TESTES / "erros.csv"),
        "esp": ler(REF / "tempos-especialista.csv"),
        "metricas": ler(METRICAS),
        "grupo": {r["participante"]: r["grupo"] for r in sess},
        "participantes": sorted({r["participante"] for r in sess}),
    }


def geral(d, m):
    for r in d["metricas"]:
        if r["metrica"] == m and r["recorte"] == "geral":
            return float(r["valor"]), r["nivel"]
    return None, ""


# ---------------------------------------------------------------------------
# 1. Painel das métricas frente aos níveis de pontuação
# ---------------------------------------------------------------------------

NIVEIS = ["Insatisfatório", "Regular", "Bom", "Excelente"]
# Limites de cada faixa, do pior para o melhor extremo (Níveis de Pontuação, Fase 2).
# Nas faixas abertas, o extremo é só o limite do desenho.
FAIXAS = {
    "M3": ("Uso de ferramenta externa", [1.0, 0.50, 0.25, 0.10, 0.0], "pct"),
    "M4": ("Acerto na primeira escolha de menu", [0.0, 0.50, 0.75, 0.90, 1.0], "pct"),
    "M5": ("Tarefas concluídas sem ajuda", [0.0, 0.60, 0.78, 0.90, 1.0], "pct"),
    "M6": ("Tempo em relação ao especialista", [8.0, 4.0, 2.5, 1.5, 1.0], "x"),
    "M7": ("Cliques em relação ao caminho mínimo", [3.0, 2.0, 1.33, 1.11, 1.0], "x"),
    "M8": ("Erros recuperados sem ajuda", [0.0, 0.50, 0.70, 0.90, 1.0], "pct"),
    "M11": ("Leitura correta sem legenda", [0.0, 0.50, 0.75, 0.90, 1.0], "pct"),
    "M12": ("Satisfação (SUS, 0 a 100)", [0.0, 51.0, 68.0, 80.3, 100.0], "sus"),
}


def _posicao(valor, limites):
    """Posição de 0 a 4 na régua de faixas iguais (0 = pior extremo, 4 = melhor)."""
    for i in range(4):
        a, b = limites[i], limites[i + 1]
        lo, hi = min(a, b), max(a, b)
        if lo - 1e-9 <= valor <= hi + 1e-9:
            return i + (valor - a) / (b - a)
    return 0.0 if (valor > limites[0]) == (limites[0] > limites[4]) else 4.0


def _fmt(valor, tipo):
    if tipo == "pct":
        return pct(valor)
    if tipo == "x":
        return f"{num(valor, 2)}×"
    return num(valor)


def painel(d) -> Grafico:
    linhas = [(m, *FAIXAS[m], *geral(d, m)) for m in FAIXAS]
    linhas = [l for l in linhas if l[4] is not None]

    def desenhar(y0):
        esq, dir_, sup, alt_l = 250, 160, 30, 34
        x_de = lambda p: esq + p / 4 * (LARGURA - esq - dir_)
        h = sup + alt_l * len(linhas) + 8
        c = []
        for i, nivel in enumerate(NIVEIS):
            classe = "ruim" if i < 2 else "bom"
            opac = [0.30, 0.13, 0.13, 0.30][i]
            c.append(f'<rect class="{classe}" x="{x_de(i):.1f}" y="{y0 + sup - 6}" width="{x_de(1) - x_de(0) - 2:.1f}" '
                     f'height="{alt_l * len(linhas) + 6}" rx="4" fill-opacity="{opac}"/>')
            c.append(f'<text class="forte" x="{(x_de(i) + x_de(i + 1)) / 2:.1f}" y="{y0 + 16}" text-anchor="middle">{nivel}</text>')
        c.append(f'<text x="{x_de(0):.1f}" y="{y0 + 16}" text-anchor="end" dx="-8">pior ←</text>')
        c.append(f'<text x="{x_de(4):.1f}" y="{y0 + 16}" dx="6">→ melhor</text>')
        for k, (m, nome, lim, tipo, valor, nivel) in enumerate(linhas):
            yc = y0 + sup + alt_l * k + alt_l / 2
            c.append(f'<text class="tinta" x="12" y="{yc + 4:.1f}"><tspan class="forte">{m}</tspan>  {_e(nome)}</text>')
            c.append(f'<line class="grade" x1="{x_de(0):.1f}" x2="{x_de(4):.1f}" y1="{yc:.1f}" y2="{yc:.1f}"/>')
            x = x_de(_posicao(valor, lim))
            c.append(f'<circle class="anel" cx="{x:.1f}" cy="{yc:.1f}" r="7" style="fill:{TINTA}"/>')
            c.append(f'<text class="valor" x="{LARGURA - dir_ + 12}" y="{yc + 4:.1f}" style="font-weight:700">'
                     f'{_fmt(valor, tipo)}</text>')
            c.append(f'<text x="{LARGURA - dir_ + 64}" y="{yc + 4:.1f}">{nivel}</text>')
            faixas = "; ".join(f"{NIVEIS[i]}: {_fmt(lim[i], tipo)} a {_fmt(lim[i + 1], tipo)}" for i in range(4))
            c.append(f'<rect class="alvo" x="0" y="{yc - alt_l / 2:.1f}" width="{LARGURA}" height="{alt_l}">'
                     f"<title>{m} {nome}: {_fmt(valor, tipo)} ({nivel}). {faixas}</title></rect>")
        return "".join(c), y0 + h

    nota = ("Cada faixa tem a mesma largura; o ponto fica na posição do valor dentro da faixa. Níveis da página "
            "Níveis de Pontuação (Fase 2). M6 e M7 em vezes o especialista e o caminho mínimo; nas faixas abertas, "
            "o extremo do desenho é só um limite visual. Teste com 5 participantes (P1, P2, P3, P4 e P6).")
    tabela = (["Métrica", "Descrição", "Valor", "Nível"], [(m, n, _fmt(v, t), nv) for m, n, _, t, v, nv in linhas])
    return Grafico("painel-metricas", "Como o SIGAA se saiu em cada métrica do teste com usuários",
                   "Onde cada resultado caiu nas faixas definidas antes da coleta?", desenhar, nota=nota, tabela=tabela)


# ---------------------------------------------------------------------------
# Barras empilhadas por tarefa (conclusão e primeira escolha)
# ---------------------------------------------------------------------------

def _empilhadas_por_tarefa(contagens, categorias, total, y0, destaque=None):
    """contagens: {tarefa: [n por categoria]}; categorias: [(rótulo, slot)]."""
    esq, dir_, sup, alt_l, barra = 190, 70, 6, 40, 24
    x_de = lambda v: esq + v / total * (LARGURA - esq - dir_)
    c = []
    for i in range(total + 1):
        x = x_de(i)
        c.append(f'<line class="{"base" if i == 0 else "grade"}" x1="{x:.1f}" x2="{x:.1f}" y1="{y0 + sup}" '
                 f'y2="{y0 + sup + alt_l * len(TAREFAS)}"/>')
        c.append(f'<text class="num" x="{x:.1f}" y="{y0 + sup + alt_l * len(TAREFAS) + 16}" text-anchor="middle">{i}</text>')
    c.append(f'<text x="{x_de(total):.1f}" y="{y0 + sup + alt_l * len(TAREFAS) + 32}" text-anchor="end">participantes</text>')
    for k, t in enumerate(TAREFAS):
        y = y0 + sup + alt_l * k + (alt_l - barra) / 2
        c.append(f'<text class="tinta" x="12" y="{y + barra / 2 + 4:.1f}">{_e(NOME_TAREFA[t])}</text>')
        x = x_de(0)
        valores = contagens[t]
        ultimo = max((j for j, v in enumerate(valores) if v), default=-1)
        for j, ((rot, slot), v) in enumerate(zip(categorias, valores)):
            if not v:
                continue
            w = x_de(v) - x_de(0)
            gap = 2 if j != ultimo else 0
            c.append(segmento(x, y, w - gap, barra, f"s{slot}", j == ultimo, f"{NOME_TAREFA[t]}: {rot}, {v} de {total}"))
            if w > 22:
                c.append(f'<text class="num" x="{x + (w - gap) / 2:.1f}" y="{y + barra / 2 + 4:.1f}" text-anchor="middle" '
                         f'style="fill:#fff;font-weight:700">{v}</text>')
            x += w
        prim = valores[0]
        c.append(f'<text class="valor" x="{x_de(total) + 10:.1f}" y="{y + barra / 2 + 4:.1f}" style="font-weight:700">'
                 f'{pct(prim / total)}</text>')
        if destaque and t in destaque:
            c.append(f'<text x="{x_de(total) + 10:.1f}" y="{y + barra / 2 + 18:.1f}" style="font-size:10px">{_e(destaque[t])}</text>')
    return "".join(c), y0 + sup + alt_l * len(TAREFAS) + 40


def conclusao(d) -> Grafico:
    cats = [("Concluiu sem ajuda", 1), ("Desistiu", 2), ("Resultado fora do SIGAA ou errado", 3)]
    mapa = {"": 0, "desistiu": 1, "resultado_errado": 2, "pediu_ajuda": 1, "tempo_esgotado": 1}
    cont = {t: [0, 0, 0] for t in TAREFAS}
    for r in d["sess"]:
        idx = 0 if r["concluida"] == "sim" else mapa.get(r["motivo_nao_conclusao"], 1)
        cont[r["tarefa"]][idx] += 1
    n = len(d["participantes"])
    m5, _ = geral(d, "M5")
    nota = (f"M5 geral = {pct(m5)} ({sum(c[0] for c in cont.values())} de {n * 6} tentativas). "
            "Nenhum participante pediu ajuda nem esgotou os 5 minutos. O número à direita é a proporção de conclusões.")
    tabela = (["Tarefa"] + [c for c, _ in cats], [(NOME_TAREFA[t], *cont[t]) for t in TAREFAS])
    return Grafico("conclusao-por-tarefa", "Em quais tarefas os estudantes travaram",
                   "Quantos participantes concluíram cada tarefa sem ajuda (M5)?",
                   lambda y0: _empilhadas_por_tarefa(cont, cats, n, y0), cats, nota=nota, tabela=tabela)


def primeira_escolha(d) -> Grafico:
    cats = [("Primeira escolha no caminho certo", 1), ("Primeira escolha fora do caminho", 2), ("Não clicou em nada e desistiu", 3)]
    cont = {t: [0, 0, 0] for t in TAREFAS}
    for r in d["sess"]:
        if r["primeira_escolha_valida"] == "sim":
            cont[r["tarefa"]][0] += 1
        elif not r["primeira_escolha"]:
            cont[r["tarefa"]][2] += 1
        else:
            cont[r["tarefa"]][1] += 1
    t6_link = sum(1 for r in d["sess"] if r["tarefa"] == "T6" and "Calendário Acadêmico de Graduação" in r["primeira_escolha"])
    n = len(d["participantes"])
    m4, _ = geral(d, "M4")
    destaque = {"T6": f"{t6_link} no link do portal que abre o site da SAA"}
    nota = (f"M4 geral = {pct(m4)}. Em T2 e T4 a informação já está na página inicial: ler a tabela sem clicar conta "
            f"como acerto. Em T6, {t6_link} dos 5 clicaram primeiro no link \"Calendário Acadêmico de Graduação\" do "
            "portal, que abre a página de Pós-Graduação do site da SAA.")
    tabela = (["Tarefa"] + [c for c, _ in cats], [(NOME_TAREFA[t], *cont[t]) for t in TAREFAS])
    return Grafico("primeira-escolha", "Onde os estudantes clicam primeiro",
                   "O primeiro clique de cada tarefa leva ao lugar certo (M4)?",
                   lambda y0: _empilhadas_por_tarefa(cont, cats, n, y0), cats, nota=nota, tabela=tabela)


# ---------------------------------------------------------------------------
# 3. Tempo dos participantes frente ao especialista
# ---------------------------------------------------------------------------

def tempos(d) -> Grafico:
    esp = {t: st.mean(float(r["tempo_s"]) for r in d["esp"] if r["tarefa"] == t) for t in TAREFAS}
    pontos = {t: [(r["participante"], int(r["tempo_s"]), r["concluida"] == "sim") for r in d["sess"] if r["tarefa"] == t]
              for t in TAREFAS}
    maximo = max(v for p in pontos.values() for _, v, _ in p)
    topo = 140 if maximo <= 140 else (maximo // 20 + 1) * 20

    def desenhar(y0):
        esq, dir_, sup, alt_l = 190, 70, 8, 42
        x_de = lambda v: esq + v / topo * (LARGURA - esq - dir_)
        c = []
        for v in range(0, topo + 1, 20):
            x = x_de(v)
            c.append(f'<line class="{"base" if v == 0 else "grade"}" x1="{x:.1f}" x2="{x:.1f}" y1="{y0 + sup}" '
                     f'y2="{y0 + sup + alt_l * 6}"/>')
            c.append(f'<text class="num" x="{x:.1f}" y="{y0 + sup + alt_l * 6 + 16}" text-anchor="middle">{v}</text>')
        c.append(f'<text x="{x_de(topo):.1f}" y="{y0 + sup + alt_l * 6 + 32}" text-anchor="end">segundos</text>')
        for k, t in enumerate(TAREFAS):
            yc = y0 + sup + alt_l * k + alt_l / 2
            c.append(f'<text class="tinta" x="12" y="{yc + 4:.1f}">{_e(NOME_TAREFA[t])}</text>')
            xe = x_de(esp[t])
            c.append(f'<rect class="s2" x="{xe - 2:.1f}" y="{yc - 13:.1f}" width="4" height="26" rx="2">'
                     f"<title>{NOME_TAREFA[t]}: especialista {num(esp[t])} s (média de 3)</title></rect>")
            usados = []
            for p, v, ok in sorted(pontos[t], key=lambda x: x[1]):
                dy = 0
                while any(abs(x_de(v) - ux) < 9 and dy == udy for ux, udy in usados):
                    dy = -dy + (8 if dy <= 0 else 0)
                usados.append((x_de(v), dy))
                estilo = "" if ok else f' style="fill:{FUNDO};stroke:var(--viz-1,#2a78d6);stroke-width:2"'
                c.append(f'<circle class="s1 anel" cx="{x_de(v):.1f}" cy="{yc + dy:.1f}" r="5.5"{estilo}>'
                         f"<title>{p}, {NOME_TAREFA[t]}: {v} s{'' if ok else ' (não concluiu)'}</title></circle>")
            tp = [v for _, v, ok in pontos[t] if ok]
            if tp:
                c.append(f'<text class="valor" x="{x_de(topo) + 10:.1f}" y="{yc + 4:.1f}" style="font-weight:700">'
                         f'{num(st.mean(tp) / esp[t])}×</text>')
        return "".join(c), y0 + sup + alt_l * 6 + 40

    leg = [("Participante que concluiu", 1), ("Especialista (média de 3 execuções)", 2)]
    m6, nivel = geral(d, "M6")
    nota = (f"Círculo vazado: tentativa não concluída (fora do cálculo). À direita, o tempo médio de quem concluiu "
            f"dividido pelo do especialista. M6 = {num(m6, 2)}× ({nivel}): em média, os participantes levaram mais de "
            "quatro vezes o tempo de quem conhece o caminho.")
    linhas = [(NOME_TAREFA[t], num(esp[t]), ", ".join(f"{p}: {v} s{'' if ok else ' (não concluiu)'}" for p, v, ok in pontos[t]))
              for t in TAREFAS]
    return Grafico("tempo-vs-especialista", "Quanto tempo os estudantes levaram em relação a um especialista",
                   "Quão longe do caminho de quem já conhece o SIGAA cada tentativa ficou (M6)?", desenhar, leg, "ponto",
                   nota, (["Tarefa", "Especialista (s)", "Participantes"], linhas))


# ---------------------------------------------------------------------------
# 4. Percepção x desempenho
# ---------------------------------------------------------------------------

def percepcao(d) -> Grafico:
    pts = []
    for t in TAREFAS:
        v = [int(r[f"c1_{t[1]}"]) for r in d["resp"] if r[f"c1_{t[1]}"] not in {"", "nunca_fiz"}]
        tent = [r for r in d["sess"] if r["tarefa"] == t]
        pts.append((t, st.median(v), sum(r["concluida"] == "sim" for r in tent) / len(tent)))

    def desenhar(y0):
        esq, dir_, sup, inf = 70, 30, 14, 46
        alt = 330
        x_de = lambda v: esq + (v - 1) / 4 * (LARGURA - esq - dir_)
        y_de = lambda v: y0 + sup + (1 - v) * (alt - sup - inf)
        c = []
        for v in range(1, 6):
            c.append(f'<line class="{"base" if v == 1 else "grade"}" x1="{x_de(v):.1f}" x2="{x_de(v):.1f}" '
                     f'y1="{y_de(1):.1f}" y2="{y_de(0):.1f}"/>')
            c.append(f'<text class="num" x="{x_de(v):.1f}" y="{y_de(0) + 16:.1f}" text-anchor="middle">{v}</text>')
        c.append(f'<text x="{x_de(1):.1f}" y="{y_de(0) + 34:.1f}">muito difícil</text>')
        c.append(f'<text x="{x_de(5):.1f}" y="{y_de(0) + 34:.1f}" text-anchor="end">muito fácil</text>')
        c.append(f'<text x="{(x_de(1) + x_de(5)) / 2:.1f}" y="{y_de(0) + 34:.1f}" text-anchor="middle">'
                 "facilidade percebida no questionário (mediana, C1)</text>")
        for v in (0, 0.2, 0.4, 0.6, 0.8, 1.0):
            c.append(f'<line class="{"base" if v == 0 else "grade"}" x1="{x_de(1):.1f}" x2="{x_de(5):.1f}" '
                     f'y1="{y_de(v):.1f}" y2="{y_de(v):.1f}"/>')
            c.append(f'<text class="num" x="{esq - 8}" y="{y_de(v) + 4:.1f}" text-anchor="end">{pct(v)}</text>')
        c.append(f'<text x="{esq - 8}" y="{y0 + 6}" text-anchor="end">concluíram</text>')
        grupos = {}
        for t, x, y in pts:
            grupos.setdefault((x, y), []).append(t)
        for (x, y), ts in grupos.items():
            px, py = x_de(x), y_de(y)
            c.append(f'<circle class="s1 anel" cx="{px:.1f}" cy="{py:.1f}" r="8">'
                     f"<title>{', '.join(NOME_TAREFA[t] for t in ts)}: facilidade {num(x)}, {pct(y)} concluíram</title></circle>")
            rot = " e ".join(NOME_TAREFA[t] for t in ts)
            ancora, dx = ("end", -14) if px > LARGURA - 200 else ("start", 14)
            c.append(f'<text class="valor" x="{px + dx:.1f}" y="{py + 4:.1f}" text-anchor="{ancora}">{_e(rot)}</text>')
        return "".join(c), y0 + alt

    nota = ("Em T4 os estudantes dizem que a tarefa é fácil (mediana 4), mas 2 de 5 não a concluíram: a dificuldade "
            "não é percebida. Em T6 a percepção (mediana 2) e o desempenho concordam. Facilidade de 1 a 5, ignorando "
            "\"nunca fiz\"; conclusão sem ajuda na sessão (M5 por tarefa).")
    return Grafico("percepcao-vs-desempenho", "O que os estudantes acham fácil nem sempre é o que conseguem fazer",
                   "A facilidade relatada no questionário bate com o desempenho na sessão?", desenhar, nota=nota,
                   tabela=(["Tarefa", "Facilidade (mediana)", "Concluíram"],
                           [(NOME_TAREFA[t], num(x), pct(y)) for t, x, y in pts]))


# ---------------------------------------------------------------------------
# 5. SUS por participante
# ---------------------------------------------------------------------------

def sus(d) -> Grafico:
    sem = {r["participante"]: r["a2"] for r in d["resp"]}
    lin = sorted(((r["participante"], float(r["pontuacao"]), d["grupo"].get(r["participante"], "")) for r in d["sus"]),
                 key=lambda x: -x[1])
    media = st.mean(v for _, v, _ in lin)

    def desenhar(y0):
        esq, dir_, sup, alt_l, barra = 190, 40, 22, 38, 22
        x_de = lambda v: esq + v / 100 * (LARGURA - esq - dir_)
        h = sup + alt_l * len(lin)
        c = []
        for v in range(0, 101, 20):
            c.append(f'<line class="{"base" if v == 0 else "grade"}" x1="{x_de(v):.1f}" x2="{x_de(v):.1f}" '
                     f'y1="{y0 + sup}" y2="{y0 + h}"/>')
            c.append(f'<text class="num" x="{x_de(v):.1f}" y="{y0 + h + 16}" text-anchor="middle">{v}</text>')
        for k, (p, v, g) in enumerate(lin):
            y = y0 + sup + alt_l * k + (alt_l - barra) / 2
            perfil = f"{sem.get(p, '?')}º semestre"
            c.append(f'<text class="tinta" x="12" y="{y + barra / 2 + 4:.1f}"><tspan class="forte">{p}</tspan>  {perfil}</text>')
            c.append(barra_h(x_de(0), y, x_de(v) - x_de(0), barra, "s1", titulo=f"{p} ({perfil}): SUS {num(v)}"))
            c.append(f'<text class="valor" x="{x_de(v) + 6:.1f}" y="{y + barra / 2 + 4:.1f}">{num(v)}</text>')
        for v, rot in ((51, "51: limite do nível Regular"), (68, "68: média de referência do SUS"), (media, f"{num(media)}: média do SIGAA")):
            x = x_de(v)
            c.append(f'<line class="limite" x1="{x:.1f}" x2="{x:.1f}" y1="{y0 + sup - 6}" y2="{y0 + h}"/>')
        c.append(f'<text class="tinta" x="{x_de(media):.1f}" y="{y0 + 12}" text-anchor="middle" style="font-weight:700">média {num(media)}</text>')
        c.append(f'<text x="{x_de(51):.1f}" y="{y0 + 12}" text-anchor="middle">51 Regular</text>')
        c.append(f'<text x="{x_de(68):.1f}" y="{y0 + 12}" text-anchor="middle">68 Bom</text>')
        return "".join(c), y0 + h + 30

    nota = ("Nenhum participante deu ao SIGAA nota acima de 51, o limite inferior do nível Regular. A média 32,5 fica "
            "no nível Insatisfatório (M12); 68 é a média de referência da escala SUS e o limite do nível Bom.")
    return Grafico("sus-por-participante", "Satisfação com o SIGAA (escala SUS)",
                   "Como cada participante avaliou o sistema ao fim da sessão (M12)?", desenhar, nota=nota,
                   tabela=(["Participante", "Semestre", "SUS"], [(p, sem.get(p, ""), num(v)) for p, v, _ in lin]))


# ---------------------------------------------------------------------------
# 6. Problemas no celular
# ---------------------------------------------------------------------------

PROBLEMAS = {
    "zoom_rolagem": "Precisou dar zoom ou rolar para o lado",
    "botoes_pequenos": "Botões ou links pequenos demais",
    "menu_nao_abriu": "Um menu não abriu ao tocar",
    "nao_concluiu": "Não conseguiu concluir o que queria",
    "conteudo_cortado": "Conteúdo cortado ou sobreposto",
}


def celular(d) -> Grafico:
    n = len(d["resp"])
    lin = sorted(((rot, sum(1 for r in d["resp"] if k in r["b5"].split(";"))) for k, rot in PROBLEMAS.items()),
                 key=lambda x: -x[1])

    def desenhar(y0):
        esq, dir_, sup, alt_l, barra = 270, 70, 6, 38, 22
        x_de = lambda v: esq + v / n * (LARGURA - esq - dir_)
        h = sup + alt_l * len(lin)
        c = []
        for i in range(n + 1):
            c.append(f'<line class="{"base" if i == 0 else "grade"}" x1="{x_de(i):.1f}" x2="{x_de(i):.1f}" '
                     f'y1="{y0 + sup}" y2="{y0 + h}"/>')
            c.append(f'<text class="num" x="{x_de(i):.1f}" y="{y0 + h + 16}" text-anchor="middle">{i}</text>')
        c.append(f'<text x="{x_de(n):.1f}" y="{y0 + h + 32}" text-anchor="end">participantes</text>')
        for k, (rot, v) in enumerate(lin):
            y = y0 + sup + alt_l * k + (alt_l - barra) / 2
            c.append(f'<text class="tinta" x="12" y="{y + barra / 2 + 4:.1f}">{_e(rot)}</text>')
            c.append(barra_h(x_de(0), y, x_de(v) - x_de(0), barra, "s1", titulo=f"{rot}: {v} de {n}"))
            c.append(f'<text class="valor" x="{x_de(v) + 8:.1f}" y="{y + barra / 2 + 4:.1f}" style="font-weight:700">{v} de {n}</text>')
        return "".join(c), y0 + h + 40

    nota = ("Respostas ao item B5 do questionário (vários podiam ser marcados). Todos os 5 participantes usam o SIGAA "
            "no celular. Na inspeção, nenhuma das 6 páginas do escopo se adapta a 360 px ou 768 px (M14 = 0 de 12): "
            "o layout fixo de 980 px é reduzido e o texto chega a cerca de 3 px.")
    return Grafico("problemas-celular", "O que acontece quando o estudante usa o SIGAA no celular",
                   "Quais problemas os participantes já tiveram no celular (IQ4)?", desenhar, nota=nota,
                   tabela=(["Problema", "Participantes"], [(r, f"{v} de {n}") for r, v in lin]))


# ---------------------------------------------------------------------------
# 7. Trajetória em T6 (calendário)
# ---------------------------------------------------------------------------

def trajetoria_t6(d) -> Grafico:
    t6 = [r for r in d["sess"] if r["tarefa"] == "T6"]
    rota = lambda r: "ensino" if r["primeira_escolha_valida"] == "sim" else "saa"
    voltou = {e["participante"] for e in d["erros"] if e["tarefa"] == "T6" and e["recuperado"] == "sim"}

    def fim(r):
        if r["concluida"] == "sim":
            return "ok"
        return "fora" if r["motivo_nao_conclusao"] == "resultado_errado" else "desistiu"

    meio = {"ensino": "Menu Ensino > Calendário Acadêmico", "saa": "Link \"Calendário Acadêmico de Graduação\" do portal"}
    sub = {"ensino": "caminho do SIGAA", "saa": "abre o site da SAA, na página de Pós-Graduação"}
    fins = {"ok": "Abriu o calendário 2026.2 no SIGAA", "fora": "Usou o calendário fora do SIGAA", "desistiu": "Desistiu"}
    fluxos = {}
    for r in t6:
        fluxos.setdefault((rota(r), fim(r)), []).append(r["participante"])
    n = len(t6)

    def desenhar(y0):
        unid, gap_meio, gap_fim, larg_no = 34, 74, 18, 14
        xs = [16, 250, 520]
        topo = y0 + 84
        c = [f'<text class="forte" x="{xs[0]}" y="{y0 + 14}">Início</text>',
             f'<text class="forte" x="{xs[1]}" y="{y0 + 14}">Primeiro clique</text>',
             f'<text class="forte" x="{xs[2]}" y="{y0 + 14}">Resultado</text>']
        cont_meio = {k: sum(len(v) for (a, _), v in fluxos.items() if a == k) for k in meio}
        cont_fim = {k: sum(len(v) for (_, b), v in fluxos.items() if b == k) for k in fins}

        def nos(contagem, gap):
            pos, y = {}, topo
            for k, v in contagem.items():
                if v:
                    pos[k] = [y, y]  # topo do nó, cursor das faixas
                    y += v * unid + gap
            return pos

        p_meio, p_fim = nos(cont_meio, gap_meio), nos(cont_fim, gap_fim)
        altura_meio = sum(cont_meio.values()) * unid + gap_meio * (len(p_meio) - 1)
        y_ini = topo + (altura_meio - n * unid) / 2
        cursor_ini = y_ini
        cor_rota = {"ensino": 1, "saa": 2}

        def faixa(x0, ya, x1, yb, h, slot, titulo):
            cx = (x0 + x1) / 2
            return (f'<path class="s{slot}" fill-opacity=".35" d="M{x0:.1f},{ya:.1f} C{cx:.1f},{ya:.1f} {cx:.1f},{yb:.1f} '
                    f'{x1:.1f},{yb:.1f} V{yb + h:.1f} C{cx:.1f},{yb + h:.1f} {cx:.1f},{ya + h:.1f} {x0:.1f},{ya + h:.1f} Z">'
                    f"<title>{_e(titulo)}</title></path>")

        for rot in p_meio:
            h = cont_meio[rot] * unid
            c.append(faixa(xs[0] + larg_no, cursor_ini, xs[1], p_meio[rot][0], h, cor_rota[rot],
                           f"{meio[rot]}: {cont_meio[rot]} de {n}"))
            cursor_ini += h
        for (a, b), ps in sorted(fluxos.items(), key=lambda kv: (list(meio).index(kv[0][0]), list(fins).index(kv[0][1]))):
            h = len(ps) * unid
            ya, yb = p_meio[a][1], p_fim[b][1]
            extra = " (voltou ao SIGAA)" if a == "saa" and b == "ok" else ""
            c.append(faixa(xs[1] + larg_no, ya, xs[2], yb, h, cor_rota[a], f"{', '.join(ps)}: {meio[a]} → {fins[b]}{extra}"))
            c.append(f'<text class="tinta" x="{xs[1] + larg_no + 8}" y="{ya + h / 2 + 4:.1f}" style="font-size:11px">'
                     f'{", ".join(ps)}{extra}</text>')
            p_meio[a][1] += h
            p_fim[b][1] += h
        c.append(f'<rect x="{xs[0]}" y="{y_ini:.1f}" width="{larg_no}" height="{n * unid}" rx="3" style="fill:{TINTA}"/>')
        c.append(f'<text class="tinta" x="{xs[0]}" y="{y_ini + n * unid + 18:.1f}" style="font-weight:700">'
                 f'{n} participantes</text>')
        for k, (y, _) in p_meio.items():
            h = cont_meio[k] * unid
            c.append(f'<rect class="s{cor_rota[k]}" x="{xs[1]}" y="{y:.1f}" width="{larg_no}" height="{h}" rx="3"/>')
            linhas = [(l, True) for l in _quebrar(f"{meio[k]} ({cont_meio[k]})", 40)] + [(l, False) for l in _quebrar(sub[k], 44)]
            for i, (l, forte) in enumerate(linhas):
                yy = y - 8 - 15 * (len(linhas) - 1 - i)
                estilo = ' style="font-weight:700"' if forte else ' style="font-size:11px"'
                c.append(f'<text class="tinta" x="{xs[1]}" y="{yy:.1f}"{estilo}>{_e(l)}</text>')
        for k, (y, _) in p_fim.items():
            h = cont_fim[k] * unid
            c.append(f'<rect x="{xs[2]}" y="{y:.1f}" width="{larg_no}" height="{h}" rx="3" style="fill:{TINTA}"/>')
            linhas = _quebrar(f"{cont_fim[k]} · {fins[k]}", 24)
            for i, l in enumerate(linhas):
                yy = y + h / 2 + 4 + 15 * (i - (len(linhas) - 1) / 2)
                c.append(f'<text class="tinta" x="{xs[2] + larg_no + 10}" y="{yy:.1f}"'
                         f'{' style="font-weight:700"' if i == 0 else ""}>{_e(l)}</text>')
        fundo = max(max(y + cont_fim[k] * unid for k, (y, _) in p_fim.items()),
                    max(y + cont_meio[k] * unid for k, (y, _) in p_meio.items()), y_ini + n * unid + 18)
        return "".join(c), fundo + 16

    leg = [("Caminho pelo menu Ensino", 1), ("Link do portal para o site da SAA", 2)]
    nota = ("Trajetória de cada participante em T6, pela análise das gravações. O link do painel do portal leva à "
            "página de Pós-Graduação do site da SAA: dos 3 que caíram nele, um voltou ao SIGAA e concluiu, um usou o "
            "calendário fora do SIGAA (não conta como conclusão) e um desistiu. A largura de cada faixa é o número de "
            "participantes.")
    linhas = [(meio[a], fins[b], ", ".join(ps)) for (a, b), ps in fluxos.items()]
    return Grafico("trajetoria-t6", "A armadilha do calendário acadêmico (T6)",
                   "Por onde os participantes tentaram chegar ao calendário, e onde chegaram?", desenhar, leg,
                   nota=nota, tabela=(["Primeiro clique", "Resultado", "Participantes"], linhas))


# ---------------------------------------------------------------------------

def graficos() -> list[Grafico]:
    d = dados()
    return [painel(d), conclusao(d), primeira_escolha(d), trajetoria_t6(d), tempos(d), percepcao(d), sus(d), celular(d)]


# Hook do MkDocs -------------------------------------------------------------

MARCADOR = re.compile(r"\[\[GRAFICO_TU:([a-z0-9-]+)\]\]")


def on_page_markdown(markdown, page, config, files):  # noqa: ARG001 (assinatura do MkDocs)
    if "[[GRAFICO_TU:" not in markdown:
        return markdown
    por_nome = {g.nome: g for g in graficos()}
    return MARCADOR.sub(lambda m: por_nome[m.group(1)].html() if m.group(1) in por_nome else m.group(0), markdown)


# Linha de comando -----------------------------------------------------------

def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    png = "--png" in sys.argv
    for g in graficos():
        svg = g.svg(para_slide=True)
        (SAIDA / f"{g.nome}.svg").write_text(svg, encoding="utf-8")
        if png:
            altura = int(re.search(r'viewBox="0 0 \d+ (\d+(?:\.\d+)?)"', svg).group(1).split(".")[0]) + 1
            with tempfile.TemporaryDirectory() as tmp:
                pagina = Path(tmp) / "g.html"
                pagina.write_text(f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:#fcfcfb}}'
                                  f"svg{{display:block}}</style>{svg}", encoding="utf-8")
                subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                                "--force-device-scale-factor=2", f"--window-size={LARGURA},{altura}",
                                f"--screenshot={SAIDA / (g.nome + '.png')}", pagina.as_uri()],
                               check=True, capture_output=True)
        print(f"{g.nome}: {SAIDA.relative_to(RAIZ) / g.nome}.svg{' e .png' if png else ''}")


if __name__ == "__main__":
    main()
