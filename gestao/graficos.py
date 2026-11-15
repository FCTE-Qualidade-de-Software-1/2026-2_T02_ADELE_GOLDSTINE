"""Gráficos SVG do site, gerados no build pelo hook do MkDocs (gestao/esforco.py).

Sem dependências externas: cada função devolve HTML com um <svg> inline e uma tabela com os
mesmos dados. As cores vêm das variáveis --viz-* de docs/stylesheets/extra.css, definidas para o
tema claro e para o escuro (slate). As séries recebem as cores na ordem fixa das variáveis, nunca
pela posição no gráfico, para que um integrante ou uma categoria tenha sempre a mesma cor.
"""

import math
from html import escape

LARGURA = 720


def _e(texto):
    return escape(str(texto), quote=True)


def num(valor, casas=1):
    return f"{valor:.{casas}f}".replace(".", ",")


def _escala(maximo, divisoes=4):
    """Topo e passo 'redondos' do eixo, com cerca de `divisoes` intervalos."""
    if maximo <= 0:
        return 1.0, 0.25
    bruto = maximo / divisoes
    magnitude = 10 ** math.floor(math.log10(bruto))
    for m in (1, 2, 2.5, 5, 10):
        passo = m * magnitude
        if passo >= bruto:
            break
    return math.ceil(maximo / passo - 1e-9) * passo, passo


def _legenda(itens, forma="quadrado"):
    """Legenda em HTML: [(rótulo, slot)]. `forma` é "quadrado" (barras) ou "traco" (linhas)."""
    lis = "".join(
        f'<li><span class="viz-amostra viz-{forma}" style="--c:var(--viz-{slot})"></span>{_e(rotulo)}</li>'
        for rotulo, slot in itens
    )
    return f'<ul class="viz-legenda">{lis}</ul>'


def _tabela(resumo, cabecalho, linhas):
    """Visão em tabela dos dados do gráfico (alternativa acessível ao SVG)."""
    th = "".join(f"<th>{_e(c)}</th>" for c in cabecalho)
    tr = "".join("<tr>" + "".join(f"<td>{_e(c)}</td>" for c in linha) + "</tr>" for linha in linhas)
    return (f'<details class="viz-dados"><summary>{_e(resumo)}</summary>'
            f'<div class="viz-tabela-wrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div></details>')


def _figura(titulo, svg, legenda="", nota="", tabela=""):
    nota = f'<p class="viz-nota">{nota}</p>' if nota else ""
    return (f'<figure class="viz"><figcaption class="viz-titulo">{_e(titulo)}</figcaption>{legenda}'
            f'<div class="viz-scroll">{svg}</div>{nota}{tabela}</figure>')


def _svg(altura, rotulo, corpo):
    return (f'<svg viewBox="0 0 {LARGURA} {altura}" role="img" aria-label="{_e(rotulo)}" '
            f'preserveAspectRatio="xMinYMin meet">{corpo}</svg>')


def _eixo_y(topo, passo, y_de, x0, x1, unidade):
    """Linhas de grade horizontais e rótulos do eixo y."""
    partes = []
    v = 0.0
    while v <= topo + 1e-9:
        y = y_de(v)
        classe = "viz-base" if v == 0 else "viz-grade"
        partes.append(f'<line class="{classe}" x1="{x0}" x2="{x1}" y1="{y:.1f}" y2="{y:.1f}"/>')
        casas = 0 if passo >= 1 else 1
        partes.append(f'<text class="viz-eixo" x="{x0 - 8}" y="{y + 4:.1f}" text-anchor="end">{num(v, casas)}</text>')
        v += passo
    partes.append(f'<text class="viz-eixo" x="{x0 - 8}" y="10" text-anchor="end">{_e(unidade)}</text>')
    return "".join(partes)


def linhas_acumuladas(titulo, series, marcas_x, unidade="h", nota=""):
    """Linhas em degrau do valor acumulado no tempo.

    series: [(nome, slot, [(data, incremento)])], datas como datetime.date.
    marcas_x: datas que recebem rótulo no eixo x (por exemplo, as segundas-feiras).
    """
    datas = sorted({d for _, _, pontos in series for d, _ in pontos} | set(marcas_x))
    if not datas:
        return ""
    inicio, fim = datas[0], datas[-1]
    dias = max((fim - inicio).days, 1)
    acumulados = []
    for nome, slot, pontos in series:
        por_data = {}
        for d, h in pontos:
            por_data[d] = por_data.get(d, 0.0) + h
        total, serie = 0.0, []
        for d in sorted(por_data):
            total += por_data[d]
            serie.append((d, total, por_data[d]))
        acumulados.append((nome, slot, serie))
    maximo = max((v for _, _, s in acumulados for _, v, _ in s), default=0)
    topo, passo = _escala(maximo)

    altura, esq, dir_, sup, inf = 300, 52, 20, 22, 36
    x_de = lambda d: esq + (d - inicio).days / dias * (LARGURA - esq - dir_)
    y_de = lambda v: sup + (1 - v / topo) * (altura - sup - inf)
    corpo = [_eixo_y(topo, passo, y_de, esq, LARGURA - dir_, unidade)]
    for d in marcas_x:
        corpo.append(f'<text class="viz-eixo" x="{x_de(d):.1f}" y="{altura - 14}" text-anchor="middle">{d:%d/%m}</text>')

    alvos = []
    for nome, slot, serie in acumulados:
        if not serie:
            continue
        # Degrau: as horas entram na data da integração e ficam constantes até a próxima
        caminho = f"M{x_de(inicio):.1f},{y_de(0):.1f}"
        for d, v, _ in serie:
            caminho += f" H{x_de(d):.1f} V{y_de(v):.1f}"
        caminho += f" H{x_de(fim):.1f}"
        corpo.append(f'<path class="viz-linha" style="--c:var(--viz-{slot})" d="{caminho}"/>')
        for d, v, inc in serie:
            x, y = x_de(d), y_de(v)
            corpo.append(f'<circle class="viz-ponto" style="--c:var(--viz-{slot})" cx="{x:.1f}" cy="{y:.1f}" r="4"/>')
            dica = f"{nome}, {d:%d/%m}: {num(v)} {unidade} acumuladas (+{num(inc)} {unidade})"
            alvos.append(f'<circle class="viz-alvo" cx="{x:.1f}" cy="{y:.1f}" r="11"><title>{_e(dica)}</title></circle>')
    corpo += alvos  # alvos por último: ficam acima de todas as linhas

    tabela = _tabela(
        "Ver os dados do gráfico", ["Integrante", "Data", f"Horas no dia ({unidade})", f"Acumulado ({unidade})"],
        [(nome, f"{d:%d/%m/%Y}", num(inc), num(v)) for nome, _, serie in acumulados for d, v, inc in serie],
    )
    legenda = _legenda([(nome, slot) for nome, slot, _ in series], forma="traco")
    return _figura(titulo, _svg(altura, titulo, "".join(corpo)), legenda, nota, tabela)


def colunas(titulo, rotulos, valores, slot=1, unidade="h", nota="", cabecalho=("Período", "Horas")):
    """Colunas verticais de uma série só, com o valor sobre cada coluna."""
    if not valores:
        return ""
    topo, passo = _escala(max(valores))
    altura, esq, dir_, sup, inf = 260, 52, 20, 22, 36
    largura_util = LARGURA - esq - dir_
    faixa = largura_util / len(valores)
    barra = min(64, faixa * 0.6)
    y_de = lambda v: sup + (1 - v / topo) * (altura - sup - inf)
    corpo = [_eixo_y(topo, passo, y_de, esq, LARGURA - dir_, unidade)]
    for i, (rotulo, v) in enumerate(zip(rotulos, valores)):
        cx = esq + faixa * (i + 0.5)
        y, base = y_de(v), y_de(0)
        h = max(base - y, 0)
        if h:
            # Topo arredondado e base reta, ancorada no eixo
            r = min(4, h, barra / 2)
            x0, x1 = cx - barra / 2, cx + barra / 2
            corpo.append(
                f'<path class="viz-barra" style="--c:var(--viz-{slot})" d="M{x0:.1f},{base:.1f} V{y + r:.1f} '
                f'Q{x0:.1f},{y:.1f} {x0 + r:.1f},{y:.1f} H{x1 - r:.1f} Q{x1:.1f},{y:.1f} {x1:.1f},{y + r:.1f} '
                f'V{base:.1f} Z"/>')
            corpo.append(f'<text class="viz-valor" x="{cx:.1f}" y="{y - 6:.1f}" text-anchor="middle">{num(v)}</text>')
        corpo.append(f'<text class="viz-eixo" x="{cx:.1f}" y="{altura - 14}" text-anchor="middle">{_e(rotulo)}</text>')
        corpo.append(f'<rect class="viz-alvo" x="{cx - faixa / 2:.1f}" y="{sup}" width="{faixa:.1f}" '
                     f'height="{altura - sup - inf}"><title>{_e(rotulo)}: {num(v)} {unidade}</title></rect>')
    tabela = _tabela("Ver os dados do gráfico", list(cabecalho), [(r, num(v)) for r, v in zip(rotulos, valores)])
    return _figura(titulo, _svg(altura, titulo, "".join(corpo)), "", nota, tabela)


def barras_empilhadas(titulo, linhas, categorias, unidade="h", nota=""):
    """Barras horizontais empilhadas: uma por linha, um segmento por categoria.

    linhas: [(rótulo, {categoria: valor})]; categorias: [(chave, rótulo, slot)] na ordem fixa.
    Valores negativos (ajustes) não entram nas barras; o total à direita é o líquido.
    """
    totais_pos = [sum(max(0, v) for v in valores.values()) for _, valores in linhas]
    topo, passo = _escala(max(totais_pos, default=0))
    esq, dir_, sup = 190, 64, 8
    alt_barra, espaco = 18, 14
    altura = sup + len(linhas) * (alt_barra + espaco) + 26
    x_de = lambda v: esq + v / topo * (LARGURA - esq - dir_)
    corpo = []
    v = 0.0
    while v <= topo + 1e-9:
        classe = "viz-base" if v == 0 else "viz-grade"
        corpo.append(f'<line class="{classe}" x1="{x_de(v):.1f}" x2="{x_de(v):.1f}" y1="{sup}" y2="{altura - 26}"/>')
        corpo.append(f'<text class="viz-eixo" x="{x_de(v):.1f}" y="{altura - 8}" text-anchor="middle">'
                     f'{num(v, 0 if passo >= 1 else 1)}</text>')
        v += passo
    for i, (rotulo, valores) in enumerate(linhas):
        y = sup + i * (alt_barra + espaco) + espaco / 2
        corpo.append(f'<text class="viz-rotulo" x="{esq - 10}" y="{y + alt_barra / 2 + 4:.1f}" text-anchor="end">{_e(rotulo)}</text>')
        acumulado = 0.0
        segmentos = [(c, r, s, valores.get(c, 0)) for c, r, s in categorias if valores.get(c, 0) > 0]
        for j, (_, rot_cat, slot, val) in enumerate(segmentos):
            x0 = x_de(acumulado)
            x1 = x_de(acumulado + val)
            ultimo = j == len(segmentos) - 1
            # 2 px de superfície entre segmentos; ponta arredondada só no fim da barra
            largura = max(x1 - x0 - (0 if ultimo else 2), 0.5)
            if ultimo:
                r = min(4, largura)
                caminho = (f"M{x0:.1f},{y:.1f} H{x0 + largura - r:.1f} Q{x0 + largura:.1f},{y:.1f} "
                           f"{x0 + largura:.1f},{y + r:.1f} V{y + alt_barra - r:.1f} Q{x0 + largura:.1f},{y + alt_barra:.1f} "
                           f"{x0 + largura - r:.1f},{y + alt_barra:.1f} H{x0:.1f} Z")
            else:
                caminho = f"M{x0:.1f},{y:.1f} h{largura:.1f} v{alt_barra} h{-largura:.1f} Z"
            corpo.append(f'<path class="viz-barra" style="--c:var(--viz-{slot})" d="{caminho}">'
                         f'<title>{_e(rotulo)}, {_e(rot_cat)}: {num(val)} {unidade}</title></path>')
            acumulado += val
        liquido = sum(valores.values())
        corpo.append(f'<text class="viz-valor" x="{x_de(acumulado) + 8:.1f}" y="{y + alt_barra / 2 + 4:.1f}">'
                     f'{num(liquido)} {unidade}</text>')
    usadas = [(c, r, s) for c, r, s in categorias if any(v.get(c, 0) > 0 for _, v in linhas)]
    tabela = _tabela(
        "Ver os dados do gráfico", ["Integrante"] + [r for _, r, _ in usadas] + [f"Total ({unidade})"],
        [[rotulo] + [num(valores.get(c, 0)) for c, _, _ in usadas] + [num(sum(valores.values()))] for rotulo, valores in linhas],
    )
    legenda = _legenda([(r, s) for _, r, s in usadas])
    return _figura(titulo, _svg(altura, titulo, "".join(corpo)), legenda, nota, tabela)


def barras_com_limite(titulo, linhas, limite, rotulo_limite, unidade, slot=1, nota="", cabecalho=None):
    """Barras horizontais de uma série com uma linha de referência (critério de decisão).

    linhas: [(rótulo, valor, dica)]; barras acima do limite recebem o aviso no rótulo do valor.
    """
    maximo = max([v for _, v, _ in linhas] + [limite])
    topo, passo = _escala(maximo)
    esq, dir_, sup = 190, 130, 22
    alt_barra, espaco = 16, 10
    altura = sup + len(linhas) * (alt_barra + espaco) + 26
    x_de = lambda v: esq + v / topo * (LARGURA - esq - dir_)
    corpo = []
    v = 0.0
    while v <= topo + 1e-9:
        classe = "viz-base" if v == 0 else "viz-grade"
        corpo.append(f'<line class="{classe}" x1="{x_de(v):.1f}" x2="{x_de(v):.1f}" y1="{sup}" y2="{altura - 26}"/>')
        corpo.append(f'<text class="viz-eixo" x="{x_de(v):.1f}" y="{altura - 8}" text-anchor="middle">'
                     f'{num(v, 0 if passo >= 1 else 1)}</text>')
        v += passo
    for i, (rotulo, valor, dica) in enumerate(linhas):
        y = sup + i * (alt_barra + espaco) + espaco / 2
        corpo.append(f'<text class="viz-rotulo" x="{esq - 10}" y="{y + alt_barra / 2 + 4:.1f}" text-anchor="end">{_e(rotulo)}</text>')
        x0, x1 = x_de(0), x_de(valor)
        largura = x1 - x0
        if largura > 0.5:
            r = min(4, largura)
            corpo.append(
                f'<path class="viz-barra" style="--c:var(--viz-{slot})" d="M{x0:.1f},{y:.1f} H{x1 - r:.1f} '
                f'Q{x1:.1f},{y:.1f} {x1:.1f},{y + r:.1f} V{y + alt_barra - r:.1f} Q{x1:.1f},{y + alt_barra:.1f} '
                f'{x1 - r:.1f},{y + alt_barra:.1f} H{x0:.1f} Z"/>')
        aviso = " ⚠ acima" if valor > limite else ""
        corpo.append(f'<text class="viz-valor" x="{max(x1, x0) + 8:.1f}" y="{y + alt_barra / 2 + 4:.1f}">'
                     f'{num(valor)} {unidade}{aviso}</text>')
        corpo.append(f'<rect class="viz-alvo" x="0" y="{y - espaco / 2:.1f}" width="{LARGURA}" '
                     f'height="{alt_barra + espaco}"><title>{_e(dica)}</title></rect>')
    xl = x_de(limite)
    corpo.append(f'<line class="viz-limite" x1="{xl:.1f}" x2="{xl:.1f}" y1="{sup - 6}" y2="{altura - 26}"/>')
    corpo.append(f'<text class="viz-eixo" x="{xl:.1f}" y="{sup - 10}" text-anchor="middle">{_e(rotulo_limite)}</text>')
    cabecalho = cabecalho or ["Item", f"Valor ({unidade})"]
    tabela = _tabela("Ver os dados do gráfico", cabecalho, [(r, num(v), d) for r, v, d in linhas])
    return _figura(titulo, _svg(altura, titulo, "".join(corpo)), "", nota, tabela)
