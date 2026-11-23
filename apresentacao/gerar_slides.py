"""Gera os slides complementares da apresentação final, no estilo do deck da equipe.

Cada slide sai como imagem PNG (1456 × 816, densidade 2), pronta para importar no
Canva, e todos juntos num PDF. Os números vêm dos mesmos arquivos da GitPage:

- ``dados/consolidados/metricas.csv`` (16 métricas, via ``coleta/graficos_finais.py``);
- ``dados/consolidados/matriz-resumo.csv`` e ``matriz-dispositivos.csv`` (matriz multiplataforma);
- ``dados/consolidados/desempenho.csv`` (dados complementares de desempenho).

Saída: ``docs/assets/apresentacao/slide-NN.png``, ``slides-complementares.pdf`` e, em
``docs/assets/apresentacao/pecas/``, cada gráfico ou bloco em PNG com fundo transparente,
para montar slides no Canva.
Uso: ``python apresentacao/gerar_slides.py`` (Playwright com Chromium; fontes Antonio
e Open Sans do Google Fonts).
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "coleta"))
import graficos_finais as gf  # noqa: E402

SAIDA = RAIZ / "docs/assets/apresentacao"
ARTIGO_IMG = SAIDA / "artigo-paginas.png"
W, H = 1456, 816

NIV_CLASSE = {"Insatisfatório": "n0", "Regular": "n1", "Bom": "n2", "Excelente": "n3"}
DESCR = {  # o que cada métrica mede, em linguagem de apresentação
    "M1": "funções da lista de referência que existem", "M2": "informações iguais ao histórico oficial",
    "M3": "participantes que planejam fora do SIGAA", "M4": "1º clique no caminho certo",
    "M5": "tentativas concluídas sem ajuda", "M6": "vezes o tempo de quem conhece o sistema",
    "M7": "vezes os cliques do caminho mínimo", "M8": "erros que o próprio estudante desfez",
    "M20": "cenários de erro com resposta adequada", "M9": "erros WCAG A/AA do WAVE, por página",
    "M10": "verificações de teclado, foco, zoom e leitor", "M11": "informações lidas certo sem legenda",
    "M12": "System Usability Scale (média de referência 68)", "M13": "combinações navegador × tarefa sem falha",
    "M14": "verificações em 360 e 768 px adaptadas", "M15": "tempo no celular ÷ tempo no computador",
}


def ler(nome):
    p = RAIZ / "dados/consolidados" / nome
    return list(csv.DictReader(p.open(encoding="utf-8"))) if p.exists() else []


def br(v, casas=1):
    return gf.num(v, casas)


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Antonio:wght@200;300;400&family=Open+Sans:wght@400;600;700;800&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Open Sans',sans-serif;color:#24243a;background:#777}
.s{width:1456px;height:816px;background:#f7f8fb;position:relative;overflow:hidden;page-break-after:always}
.lat{position:absolute;left:0;top:0;bottom:0;width:68px;background:#7179e6;z-index:3}
.lat span{position:absolute;left:23px;bottom:58px;writing-mode:vertical-rl;transform:rotate(180deg);color:#e6e8ff;letter-spacing:6px;font-size:15px}
h1{font-family:Antonio;font-weight:200;color:#7179e6;font-size:76px;text-align:center;line-height:1;padding-top:64px;text-transform:uppercase;letter-spacing:.5px}
.topo{position:absolute;left:0;right:0;top:0;height:196px;background:#7179e6}
.topo h1{color:#fff}
.faixa{position:absolute;left:148px;right:80px;top:195px;height:75px;background:#e1e3f7;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:28px;text-align:center;padding:0 20px}
.topo ~ .faixa{background:none;top:212px;height:60px}
.corpo{position:absolute;left:148px;right:80px;top:292px;bottom:40px}
.nota{position:absolute;left:148px;right:80px;bottom:28px;text-align:center;font-size:18px;color:#3a3a4e;line-height:1.35}
.cards{display:flex;gap:44px;height:330px}
.card{flex:1;background:#e1e3f7;border-radius:22px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:20px}
.card b{font-family:Arial,sans-serif;font-size:88px;color:#7179e6;line-height:1.05;font-weight:800}
.card span{font-size:24px;margin-top:20px;line-height:1.3}
/* chips de nível */
.chip{display:inline-block;border-radius:30px;padding:4px 14px;font-weight:700;font-size:17px;white-space:nowrap}
.n0{background:#f9d3d5;color:#a3202a}.n1{background:#fbe4d0;color:#94500f}.n2{background:#d9e7f8;color:#1d58a5}.n3{background:#2a6fc9;color:#fff}
.hc{background:#2a6fc9;color:#fff}.hr{background:#d8434a;color:#fff}.hi{background:#8a8a9c;color:#fff}
/* régua de faixas */
.cab{display:grid;grid-template-columns:345px 520px 1fr;align-items:end;margin-bottom:8px}
.cab .rot{display:grid;grid-template-columns:repeat(4,1fr);text-align:center;font-weight:800;font-size:16px}
.cab .rot span{padding-bottom:2px}
.lin{display:grid;grid-template-columns:345px 520px 1fr;align-items:center;border-top:1px solid #e3e3ec}
.lin .nm b{font-size:22px;color:#5a62d4;margin-right:8px}
.lin .nm span{font-size:20px;font-weight:700}
.lin .nm small{display:block;font-size:15.5px;color:#55546a;margin-top:2px}
.regua{position:relative;height:100%;display:grid;grid-template-columns:repeat(4,1fr);gap:3px}
.regua i{display:block;height:100%}
.f0{background:#f4c4c6}.f1{background:#f8e1e3}.f2{background:#dde9f7}.f3{background:#bcd5f1}
.ponto{position:absolute;top:50%;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:50%;background:#1d1d2b;border:3px solid #fff;box-shadow:0 1px 4px #0005}
.res{padding-left:24px;display:flex;flex-direction:column;gap:6px}
.res .v{font-size:30px;font-weight:800;line-height:1}
.res .v .chip{vertical-align:middle;margin-left:10px}
.res .h{font-size:15.5px;color:#3a3a4e}
.res .h .chip{font-size:14px;padding:2px 10px;margin-left:4px}
/* barras genéricas */
.bar-lin{display:grid;align-items:center;column-gap:16px}
.trilho{position:relative;height:100%}
.barra{position:absolute;left:0;top:50%;transform:translateY(-50%);border-radius:0 6px 6px 0}
.ref{position:absolute;top:-6px;bottom:-6px;border-left:2.5px dashed #24243a}
.ref span{position:absolute;top:-26px;left:6px;font-size:15px;font-weight:700;white-space:nowrap}
.val{position:absolute;top:50%;transform:translateY(-50%);font-weight:800;font-size:19px;white-space:nowrap;padding-left:10px}
.legenda{display:flex;gap:28px;justify-content:center;font-size:17px;margin-bottom:14px}
.legenda i{display:inline-block;width:18px;height:18px;border-radius:4px;vertical-align:-3px;margin-right:8px}
/* blocos (estilo PROBLEMAS / DECISÕES) */
.esq{position:absolute;left:68px;top:0;bottom:0;width:452px;background:#666fc9;display:flex;flex-direction:column;justify-content:center;padding:0 60px}
.esq h1{color:#fff;text-align:left;padding:0;font-size:68px}
.esq hr{border:0;border-top:2px solid #e1e3f7;margin:28px 0;width:336px}
.esq p{color:#fff;font-size:22px}
.blocos{position:absolute;left:590px;right:112px;top:56px;bottom:56px;display:flex;flex-direction:column;justify-content:space-between}
.bloco{background:#666fc9;border-radius:40px;display:flex;min-height:196px}
.bloco .ic{width:124px;flex:none;background:#7179e6;border-radius:40px 0 0 40px;display:flex;align-items:center;justify-content:center;color:#fff;font-family:Antonio;font-size:70px;font-weight:300}
.bloco .tx{padding:24px 30px;color:#fff;display:flex;flex-direction:column;justify-content:center}
.bloco h3{font-size:25px;margin-bottom:10px}
.bloco p{font-size:20.5px;line-height:1.38}
/* grade de hipóteses */
.hgrid{display:grid;grid-template-columns:repeat(var(--n,8),1fr);gap:10px;margin-top:22px}
.hq{border-radius:14px;padding:9px 6px;text-align:center;color:#fff}
.hq b{display:block;font-size:24px}.hq span{font-size:14.5px;display:block;margin-top:3px;line-height:1.2}
/* melhorias */
.recs{display:grid;grid-template-columns:1fr 1fr;gap:10px 28px}
.rec{display:flex;gap:16px;align-items:flex-start;background:#fff;border-radius:16px;padding:9px 18px;box-shadow:0 1px 3px #0001;border-left:6px solid #7179e6}
.rec .nr{font-family:Antonio;font-size:40px;color:#7179e6;line-height:1;min-width:30px}
.rec h4{font-size:19px;margin-bottom:3px}
.rec p{font-size:15px;color:#46465a;line-height:1.3}
.dupla{display:flex;gap:44px}
.dupla .col{flex:1;border:2px solid #7179e6;border-radius:20px;padding:24px 30px;background:#fff}
.dupla h3{font-family:Antonio;font-weight:300;color:#7179e6;font-size:44px;margin-bottom:14px;text-transform:uppercase}
.dupla li{font-size:20px;line-height:1.38;margin:0 0 12px 24px}
"""

LAT = '<div class="lat"><span>ADELE GOLDSTINE | 2026</span></div>'


def sec(conteudo):
    lat = "" if conteudo.startswith('<div class="topo">') else LAT
    return f'<section class="s">{lat}{conteudo}</section>'


def titulo(t, faixa, topo=False):
    h = f'<div class="topo"><h1>{t}</h1></div>' if topo else f"<h1>{t}</h1>"
    return h + f'<div class="faixa">{faixa}</div>'


# ---------------------------------------------------------------------------
def mini_barras(titulo_, itens, sufixo="%", vmax=100, alt=27, fonte=15.5):
    """Painel de barras horizontais: itens = [(rótulo, valor, cor)]."""
    lin = "".join(
        f'<div style="display:grid;grid-template-columns:190px 1fr;align-items:center;height:{alt}px;gap:10px">'
        f'<div style="font-size:{fonte}px;font-weight:600">{r}</div><div class="trilho" style="height:{alt - 8}px;background:#ebebf3;border-radius:4px">'
        f'<div class="barra" style="height:{alt - 8}px;width:{max(v / vmax * 82, 0.6):.1f}%;background:{c};border-radius:4px"></div>'
        f'<div class="val" style="left:{v / vmax * 82:.1f}%;font-size:{fonte}px">{br(v, 0)}{sufixo}</div></div></div>' for r, v, c in itens)
    return (f'<div style="flex:1;background:#fff;border-radius:16px;padding:12px 18px;box-shadow:0 1px 3px #0001">'
            f'<div style="font-size:17px;font-weight:800;color:#5a62d4;margin-bottom:6px">{titulo_}</div>{lin}</div>')


def cor_pct(v):
    return "#d8434a" if v < 50 else ("#e39a3b" if v < 75 else ("#7fb0e6" if v < 100 else "#2a6fc9"))


def slide_metricas(t, faixa, codigos, nota, topo=False, extra="", compacto=False):
    m = gf.metricas()
    hip = {mt: (h, prev, cl) for h, (mt, prev, cl) in gf.HIPOTESES.items()}
    alt = 60 if compacto else min(112 if not extra else 80, 410 // len(codigos))
    linhas = []
    curtos = {"M10": "Acessibilidade manual", "M13": "Compatibilidade de navegadores", "M14": "Páginas adaptadas ao celular",
              "M20": "Cenários de erro tratados", "M9": "Erros WAVE por página"}
    for k in codigos:
        _, nome, lim, f = gf.METRICAS[k]
        if compacto:
            nome = curtos.get(k, nome)
        v, nv = m[k]
        pos = gf.posicao(v, lim) / 4 * 100
        h, prev, cl = hip[k]
        obt = gf.NIVEIS.index(nv)
        if cl == "Refutada":
            cl_txt, cl_cls = ("Refutada ↑ melhor" if gf.SENTIDO.get(h, "melhor" if obt > prev else "pior") == "melhor" else "Refutada ↓ pior"), "hr"
        else:
            cl_txt, cl_cls = cl, {"Confirmada": "hc", "Inconclusiva": "hi"}[cl]
        linhas.append(
            f'<div class="lin" style="height:{alt}px"><div class="nm"><b>{k}</b><span>{gf.e(nome)}</span><small>{DESCR[k]}</small></div>'
            f'<div class="regua" style="padding:{max((alt - 52) // 2, 8)}px 0"><i class="f0"></i><i class="f1"></i><i class="f2"></i><i class="f3"></i>'
            f'<div class="ponto" style="left:{pos:.1f}%"></div></div>'
            f'<div class="res"><div class="v">{gf.fmt(v, f)}<span class="chip {NIV_CLASSE[nv]}">{nv}</span></div>'
            f'<div class="h">{h} previa {gf.NIVEIS[prev]} <span class="chip {cl_cls}">{cl_txt}</span></div></div></div>')
    cab = ('<div class="cab"><div style="font-size:15px;color:#55546a">pior ← → melhor</div><div class="rot">'
           + "".join(f"<span>{n}</span>" for n in gf.NIVEIS) + '</div><div style="padding-left:24px;font-size:15px;color:#55546a">resultado · hipótese</div></div>')
    extra_html = f'<div style="display:flex;gap:24px;margin-top:16px">{extra}</div>' if extra else ""
    if compacto:
        extra_html += ("<style>.cmp .lin .nm span{font-size:18px}.cmp .lin .nm b{font-size:19px}.cmp .lin .nm small{font-size:13.5px}"
                       ".cmp .res{gap:2px}.cmp .res .v{font-size:23px}.cmp .res .v .chip{font-size:14px;padding:2px 10px}"
                       ".cmp .lin .nm small{white-space:nowrap}.cmp .res .h{font-size:13.5px}.cmp .res .h .chip{font-size:12.5px;padding:1px 8px}.cmp .ponto{width:22px;height:22px;margin:-11px 0 0 -11px}</style>")
    return sec(titulo(t, faixa, topo) + f'<div class="corpo{" cmp" if compacto else ""}" style="top:{276 if compacto else 300}px">{cab}{"".join(linhas)}{extra_html}</div><div class="nota">{nota}</div>')


SISTEMA = ["M1", "M2", "M20", "M9", "M10", "M13", "M14"]  # métricas medidas por script (inspeção automatizada, WAVE e Playwright)


def slide_metodo():
    cards = [
        ("Playwright", "Navegadores reais", "M13, M14 e matriz",
         "Chrome, Edge, Firefox e Safari/WebKit executam T1 a T6 sozinhos; os critérios de M14 viram medidas em px de cada texto e botão."),
        ("WAVE", "Motor oficial 3.3.4", "M9",
         "O mesmo motor da extensão é injetado na página final de cada tarefa; erros WCAG A e AA por página."),
        ("Inspeção", "Script + 2º avaliador", "M1, M2, M10 e M20",
         "Teclado (Tab/Enter), foco, zoom 200%, árvore de acessibilidade, 6 cenários de erro e funções dos menus."),
    ]
    cs = "".join(f'<div style="flex:1;border:2px solid #7179e6;border-radius:18px;padding:26px 26px;background:#fff;height:430px">'
                 f'<div style="font-family:Arial;font-weight:800;font-size:46px;color:#7179e6">{a}</div>'
                 f'<div style="font-size:19px;font-weight:800;color:#5a62d4;margin-top:20px">{b}</div>'
                 f'<div style="font-size:19px;font-weight:700;margin-top:4px">{c}</div>'
                 f'<p style="font-size:18.5px;line-height:1.42;margin-top:16px;color:#3a3a4e">{d}</p></div>' for a, b, c, d in cards)
    return sec(titulo("Teste com os Scripts", "Como medimos o sistema", True)
               + f'<div class="corpo" style="top:296px"><div style="display:flex;gap:36px">{cs}</div></div>'
               + '<div class="nota">Scripts versionados em coleta/, o mesmo procedimento em qualquer máquina · só consultas (nunca matrícula ou trancamento) · uma sessão por vez · senha só em variável de ambiente · capturas borradas.</div>')


def slide_hipoteses(codigos=None):
    m = gf.metricas()
    hips = {h: v for h, v in gf.HIPOTESES.items() if codigos is None or v[0] in codigos}
    tot = len(hips)
    conf = [h for h, v in hips.items() if v[2] == "Confirmada"]
    ref = [h for h, v in hips.items() if v[2] == "Refutada"]
    sent = {h: gf.SENTIDO.get(h, "melhor" if gf.NIVEIS.index(m[v[0]][1]) > v[1] else "pior") for h, v in hips.items() if v[2] == "Refutada"}
    piores = sum(1 for x in sent.values() if x == "pior")
    cards = "".join(
        f'<div class="card" style="height:190px;background:{bg}"><b style="color:{cor}">{len(lst)}</b>'
        f'<span><b style="font-size:30px;color:{cor};font-family:Open Sans">{br(len(lst) / tot * 100, 1).replace(",0", "")}%</b> {rot}</span></div>'
        for lst, rot, cor, bg in ((conf, "confirmadas", "#2a6fc9", "#dde9f7"), (ref, "refutadas", "#d8434a", "#f9d6d8")))
    cards += ('<div class="card" style="height:190px;background:#e6e6ee;flex-direction:row;gap:28px">'
              f'<div><div style="font-family:Arial;font-weight:800;font-size:76px;color:#d8434a;line-height:1">{piores} ↓</div>'
              '<div style="font-size:21px;margin-top:10px">para pior</div></div>'
              f'<div><div style="font-family:Arial;font-weight:800;font-size:76px;color:#2a6fc9;line-height:1">{len(ref) - piores} ↑</div>'
              '<div style="font-size:21px;margin-top:10px">para melhor</div></div></div>')
    qs = []
    for h, (mt, prev, cl) in hips.items():
        obt = gf.NIVEIS.index(m[mt][1])
        cor = {"Confirmada": "#2a6fc9", "Refutada": "#d8434a", "Inconclusiva": "#8a8a9c"}[cl]
        seta = "" if cl != "Refutada" else (" ↑" if gf.SENTIDO.get(h, "melhor" if obt > prev else "pior") == "melhor" else " ↓")
        qs.append(f'<div class="hq" style="background:{cor}"><b>{h}{seta}</b><span>{mt}<br>{gf.NIVEIS[prev][:5]}. → {gf.NIVEIS[obt][:5]}.</span></div>')
    return sec(titulo("Hipóteses do sistema", f"{tot} hipóteses das métricas medidas por script: o que previmos × o que medimos")
               + f'<div class="corpo" style="top:292px"><div class="cards" style="height:190px">{cards}</div><div class="hgrid" style="--n:{min(len(qs), 8)}">{"".join(qs)}</div></div>'
               + '<div class="nota">↓ pior: H2 (2 datas do calendário divergem da SAA) e H11 (menu Ensino sem teclado nem nome no leitor de tela) · '
                 '↑ melhor: H9 (só a sessão expirada não é tratada) e H14 (funciona nos 4 navegadores).</div>')


def slide_julgamento():
    m = gf.metricas()
    lin = []
    for g in ("G2", "G1", "G3"):
        qs = [(k, gf.NIVEIS.index(m[k][1])) for k, v in gf.METRICAS.items() if v[0] == g]
        med = sum(n for _, n in qs) / len(qs)
        julg = "Não atende" if med < 1 else ("Atende" if med >= 2 and all(n for _, n in qs) else "Atende parcialmente")
        cor = "#d8434a" if julg == "Não atende" else ("#e39a3b" if julg != "Atende" else "#2a6fc9")
        chips = "".join(f'<span class="chip {NIV_CLASSE[gf.NIVEIS[n]]}" style="font-size:14px;padding:2px 9px;margin:0 5px 5px 0">{k}</span>' for k, n in qs)
        lin.append(
            f'<div class="bar-lin" style="grid-template-columns:300px 640px 1fr;height:142px">'
            f'<div><div style="font-size:24px;font-weight:800">{gf.OBJETIVOS[g]}</div><div style="font-size:16px;color:#55546a">{g} · {len(qs)} questões</div></div>'
            f'<div><div class="trilho" style="height:46px;background:#ebebf3;border-radius:6px">'
            f'<div class="barra" style="height:46px;width:{med / 3 * 100:.1f}%;background:{cor}"></div>'
            + "".join(f'<div class="ref" style="left:{x / 3 * 100:.2f}%">{"<span>" + r + "</span>" if g == "G2" else ""}</div>' for x, r in ((1, "1 · não atende abaixo"), (2, "2 · atende a partir")))
            + f'</div><div style="margin-top:12px">{chips}</div></div>'
            f'<div style="padding-left:26px"><div style="font-size:52px;font-weight:800;line-height:1;color:{cor}">{br(med, 2)}</div>'
            f'<div style="font-size:22px;font-weight:800;margin-top:4px">{julg}</div></div></div>')
    return sec(titulo("Julgamento", "Média dos níveis das questões (0 a 3) e regra da Fase 2", True)
               + f'<div class="corpo" style="top:312px">{"".join(lin)}</div>'
               + '<div class="nota">Atende: média ≥ 2 e nenhuma questão Insatisfatória · Não atende: média &lt; 1 · sem nota única. '
                 'Chips = nível de cada questão (cor da faixa). Flexibilidade soma um ponto forte (M13) e um crítico (M14).</div>')


def slide_ranking():
    dados = [("T6 Calendário acadêmico", 1.25, "60% concluíram · 4,67× o tempo"), ("T4 Índices e carga pendente", 1.33, "60% concluíram · 8,48× o tempo"),
             ("T1 Notas", 1.75, "100% concluíram · 4,50× o tempo"), ("T5 Material da turma", 2.00, "80% concluíram · 2,32× o tempo"),
             ("T2 Horário e local", 2.33, "100% concluíram · 2,58× o tempo"), ("T3 Atestado", 2.50, "100% concluíram · 3,78× o tempo")]
    lin = []
    for nome, v, det in dados:
        cor = "#d8434a" if v < 1.5 else ("#e39a3b" if v < 2 else "#7179e6")
        lin.append(f'<div class="bar-lin" style="grid-template-columns:330px 1fr;height:72px"><div><div style="font-size:21px;font-weight:800">{nome}</div>'
                   f'<div style="font-size:15.5px;color:#55546a">{det}</div></div><div class="trilho" style="height:40px">'
                   f'<div class="barra" style="height:40px;width:{v / 3 * 85:.1f}%;background:{cor}"></div>'
                   f'<div class="val" style="left:{v / 3 * 85:.1f}%">{br(v, 2)}</div></div></div>')
    return sec(titulo("Onde corrigir primeiro", "Ranking das tarefas: média dos níveis de M5, M6, M7 e M1 (0 a 3)")
               + f'<div class="corpo" style="top:300px">{"".join(lin)}</div>'
               + '<div class="nota">T6: 3 de 5 clicaram no link do portal que abre a Pós-Graduação. T4: a carga horária pendente está na página inicial, mas ninguém a vê.</div>')


# ---------------------------------------------------------------------------
def dados_matriz():
    res = ler("matriz-resumo.csv")
    movel = [r for r in res if r["categoria"] != "Computador"]
    return res, movel


def slide_matriz_cards():
    res, movel = dados_matriz()
    concl = sum(int(r["tarefas_concluidas"]) for r in res)
    total = sum(int(r["tarefas"]) for r in res)
    navs = len({r["navegador"] for r in res})
    adapt = sum(int(r["paginas_adaptadas"] or 0) for r in movel)
    aval = sum(int(r["paginas_avaliadas"] or 0) for r in movel)
    cards = "".join(f'<div class="card"><b>{n}</b><span>{t}</span></div>' for n, t in (
        (len(res), "perfis de sistema,<br>aparelho e navegador"), (navs, "navegadores<br>(Blink, Gecko, WebKit)"),
        (f"{round(concl / total * 100)}%", f"tarefas concluídas<br>({concl} de {total})"), (f"{round(adapt / aval * 100) if aval else 0}%", f"páginas adaptadas<br>no celular ({adapt} de {aval})")))
    return sec(titulo("Matriz multiplataforma", "Os scripts de M13 e M14 levados a Windows, macOS, Linux, Android, iOS e iPadOS")
               + f'<div class="corpo" style="top:300px"><div class="cards" style="gap:30px">{cards}</div></div>'
               + '<div class="nota">Motor real de cada navegador + tela, densidade, toque, modo móvel e user agent de cada aparelho (Playwright). '
                 'Login da UnB + T1 a T6 em cada perfil. Dado complementar: não altera M13 nem M14.</div>')


def slide_matriz_grade():
    res, movel = dados_matriz()
    det = {(r["perfil"], r["pagina"]): r for r in ler("matriz-dispositivos.csv")}
    cols = ["login", "T1", "T2", "T3", "T4", "T5", "T6"]
    paineis = {}
    for cat in ("Computador", "Celular", "Tablet"):
        rs = [r for r in res if r["categoria"] == cat]
        if not rs:
            continue
        lin = []
        for r in rs:
            cel = []
            for c in cols:
                d = det.get((r["perfil"], c))
                if not d:
                    cel.append('<i style="background:#ddd"></i>')
                    continue
                if d["concluiu"] != "sim":
                    cor, s = "#d8434a", "✕"
                elif cat != "Computador" and (d["adaptada"] == "não" if c != "login" else "não" in (d["crit_a"], d["crit_b"], d["crit_e"])):
                    cor, s = "#f3a9ac", "✓"
                else:
                    cor, s = "#2a6fc9", "✓"
                cel.append(f'<i style="background:{cor};color:{"#24243a" if cor == "#f3a9ac" else "#fff"}">{s}</i>')
            nome = r["aparelho"].split(" (")[0].replace("Notebook ", "").replace("MacBook Air ", "Mac ").replace("Monitor ", "")
            lin.append(f'<div style="display:grid;grid-template-columns:1fr 196px;align-items:center;height:{34 if cat == "Computador" else 33}px;gap:8px">'
                       f'<div style="font-size:14.5px;line-height:1.05"><b>{gf.e(r["navegador"].replace(" (WebKit)", ""))}</b><br><span style="color:#55546a;font-size:12.5px">{gf.e(r["sistema"])} · {gf.e(nome)}</span></div>'
                       f'<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:3px;height:80%">' + "".join(cel).replace("<i ", '<i class="cel" ') + "</div></div>")
        head = ('<div style="display:grid;grid-template-columns:1fr 196px;gap:8px;font-size:12.5px;font-weight:800;margin-bottom:4px"><span></span>'
                '<div style="display:grid;grid-template-columns:repeat(7,1fr);text-align:center"><span>Login</span>' + "".join(f"<span>{c}</span>" for c in cols[1:]) + "</div></div>")
        paineis[cat] = (f'<div style="background:#fff;border-radius:18px;padding:10px 16px 12px;box-shadow:0 1px 3px #0001">'
                       f'<div style="font-family:Antonio;font-weight:300;font-size:26px;color:#7179e6;margin-bottom:2px">{cat.upper()} · {len(rs)}</div>{head}{"".join(lin)}</div>')
    adapt = sum(int(r["paginas_adaptadas"] or 0) for r in movel)
    aval = sum(int(r["paginas_avaliadas"] or 0) for r in movel)
    login = sum(1 for r in movel if r.get("login_cabe_na_tela") == "sim")
    leg = ('<div class="legenda"><span><i style="background:#2a6fc9"></i>concluiu e cabe na tela</span>'
           '<span><i style="background:#f3a9ac"></i>concluiu, mas exige zoom e rolagem lateral</span><span><i style="background:#d8434a"></i>não concluiu</span></div>')
    return sec(titulo("Funciona em tudo, adapta em nada", f"{adapt} de {aval} páginas adaptadas no celular e tablet · login da UnB: {login} de {len(movel)}")
               + f'<div class="corpo" style="top:280px;bottom:10px">{leg}<div style="display:flex;gap:18px;align-items:flex-start"><div style="flex:1">{paineis.get("Computador", "")}</div><div style="flex:1;display:flex;flex-direction:column;gap:12px">{paineis.get("Celular", "")}{paineis.get("Tablet", "")}</div></div></div>'
               + '<style>.cel{display:flex;align-items:center;justify-content:center;border-radius:4px;font-style:normal;font-weight:800;font-size:13px}</style>')


def slide_fontes():
    res, movel = dados_matriz()
    lin = []
    esc = lambda v: v / 16 * 100
    for r in movel:
        fs, fl = float(r["fonte_minima_px"]), float(r["fonte_minima_login_px"] or 0)
        lin.append(f'<div class="bar-lin" style="grid-template-columns:300px 1fr;height:{min(46, 430 // len(movel))}px"><div style="font-size:17px"><b>{gf.e(r["aparelho"].split(" (")[0])}</b> '
                   f'<span style="color:#55546a">· {gf.e(r["navegador"].replace(" (WebKit)", ""))}</span></div><div class="trilho" style="height:28px">'
                   f'<div class="barra" style="height:26px;width:{esc(fs):.1f}%;background:#d8434a"></div>'
                   f'<div class="val" style="left:{esc(fs):.1f}%">{br(fs, 1)} px <span style="font-weight:600;color:#55546a;font-size:15px">(página a {br(float(r["escala_mediana"]) * 100, 0)}%)</span></div>'
                   f'<div style="position:absolute;top:50%;left:{esc(fl):.1f}%;width:18px;height:18px;margin:-9px 0 0 -9px;border-radius:50%;background:#2a6fc9;border:3px solid #fff;box-shadow:0 1px 3px #0005"></div>'
                   f'<div class="ref" style="left:75%;border-color:#24243a"></div></div></div>')
    leg = ('<div class="legenda"><span><i style="background:#d8434a"></i>menor fonte do SIGAA na tela do aparelho</span>'
           '<span><i style="background:#2a6fc9;border-radius:50%"></i>menor fonte da página de login da UnB</span>'
           '<span><i style="background:none;border-left:3px dashed #24243a;border-radius:0"></i>12 px: mínimo legível (critério b)</span></div>')
    fmin = min(float(r["fonte_minima_px"]) for r in movel)
    fmax = max(float(r["fonte_minima_px"]) for r in movel)
    return sec(titulo("No celular, o texto encolhe", f"Sem &lt;meta viewport&gt;: a página de 980 px é reduzida e o texto fica com {br(fmin, 1)} a {br(fmax, 1)} px")
               + f'<div class="corpo" style="top:286px">{leg}{"".join(lin)}</div>'
               + '<div class="nota" style="bottom:18px">A página de login da UnB, no mesmo percurso, já é responsiva: a correção é viável no próprio ambiente da universidade.</div>')


def slide_desempenho():
    dados = {}
    for r in ler("desempenho.csv"):
        if r.get("situacao") == "medida":
            dados.setdefault(r["tarefa"], {})["comp" if r["cenario"].startswith("computador") else "cel"] = float(r["carga_total_mediana_s"])
    nomes = {"T1": "T1 Notas", "T2": "T2 Portal", "T3": "T3 Atestado", "T4": "T4 Índices", "T5": "T5 Turma Virtual", "T6": "T6 Calendário"}
    esc = lambda v: v / 21 * 100
    lin = []
    for t in sorted(dados):
        d = dados[t]
        barras = "".join(
            f'<div class="trilho" style="height:24px;margin:3px 0"><div class="barra" style="height:22px;width:{esc(d[k]):.1f}%;background:{c}"></div>'
            f'<div class="val" style="left:{esc(d[k]):.1f}%;font-size:17px">{br(d[k], 2)} s</div>'
            + ("".join(f'<div class="ref" style="left:{esc(x):.2f}%;top:-5px;bottom:-5px"></div>' for x in (1, 10))) + "</div>"
            for k, c in (("comp", "#7179e6"), ("cel", "#e39a3b")))
        lin.append(f'<div class="bar-lin" style="grid-template-columns:220px 1fr;height:68px"><div style="font-size:20px;font-weight:800">{nomes[t]}</div><div>{barras}</div></div>')
    leg = ('<div class="legenda"><span><i style="background:#7179e6"></i>computador</span><span><i style="background:#e39a3b"></i>celular 360 px em 4G (perfil do Lighthouse)</span>'
           '<span><i style="background:none;border-left:3px dashed #24243a;border-radius:0"></i>1 s e 10 s: limites de atenção de Nielsen</span></div>')
    return sec(titulo("Desempenho (complementar)", "No celular em 4G, a espera multiplica por 2,5 a 8,9 — e T5 passa de 19 s")
               + f'<div class="corpo" style="top:286px">{leg}{"".join(lin)}</div>'
               + '<div class="nota" style="bottom:16px">Sem nível: Eficiência de Desempenho saiu da especificação. Turma Virtual: 1,9 MB e CLS de 1,05 (a página pula depois de carregar).</div>')


# ---------------------------------------------------------------------------
def slide_blocos(t, sub, blocos):
    bs = "".join(f'<div class="bloco"><div class="ic">{i}</div><div class="tx"><h3>{h}</h3><p>{p}</p></div></div>' for i, h, p in blocos)
    return sec(f'<div class="esq"><h1>{t}</h1><hr><p>{sub}</p></div><div class="blocos">{bs}</div>')


def slide_melhorias():
    itens = [
        ("Layout responsivo", "&lt;meta viewport&gt; e layout fluido no portal do discente · M14 = 0 de 12; matriz: 0 de 60 páginas"),
        ("Menu acessível", "foco do teclado, nome no leitor de tela e abertura por toque · M10 = 54,2%"),
        ("Corrigir os erros do WAVE", "idioma da página, texto alternativo em 47 imagens, rótulos e contraste · M9 = 13,17 por página"),
        ("Aviso de sessão expirada", "mensagem clara em vez de voltar ao portal em silêncio · único cenário não tratado (M20)"),
        ("Turma Virtual mais leve", "carregar sob demanda e reservar espaço para os painéis · 19 s no 4G; CLS de 1,05"),
        ("Planejamento do curso", "fluxo, semestres, grade antes da matrícula e simulação do IRA · as 4 funções ausentes em M1"),
    ]
    recs = "".join(f'<div class="rec" style="padding:16px 22px"><div class="nr" style="font-size:52px">{i}</div><div><h4 style="font-size:22px">{h}</h4><p style="font-size:17.5px">{p}</p></div></div>' for i, (h, p) in enumerate(itens, 1))
    return sec(titulo("Melhorias recomendadas", "Para a STI/UnB, em ordem de prioridade, cada uma ligada à medida que a justifica", True)
               + f'<div class="corpo" style="top:290px;bottom:30px"><div class="recs" style="gap:18px 30px">{recs}</div></div>')


def slide_limitacoes():
    return sec(titulo("Limitações e próximos passos", "O que os scripts não medem e como continuar")
               + '<div class="corpo" style="top:300px"><div class="dupla"><div class="col"><h3>Limitações</h3><ul>'
                 "<li>Emulação: reproduz navegador, tela e toque, mas não o sistema operacional nem o desempenho do aparelho.</li>"
                 "<li>Uma conta de estudante e uma rede; desempenho fora do pico de matrícula.</li>"
                 "<li>WAVE detecta só parte das barreiras; o resto exige inspeção manual (M10).</li>"
                 "<li>Matrícula e trancamento fora do escopo: alterariam dados reais.</li>"
                 '</ul></div><div class="col"><h3>Trabalhos futuros</h3><ul>'
                 "<li>Rodar a matriz em aparelhos reais (iPhone, Android de entrada e tablet).</li>"
                 "<li>Medir o desempenho nos períodos de matrícula, com o servidor sob carga.</li>"
                 "<li>Rodar os mesmos scripts a cada nova versão do SIGAA, como teste de regressão.</li>"
                 "<li>Aplicar os scripts às páginas de outras tarefas do portal.</li></ul></div></div></div>")


def slide_artigo():
    img = (f'<img src="{ARTIGO_IMG.as_uri()}" style="height:560px">' if ARTIGO_IMG.exists()
           else '<div style="width:760px;height:536px;border:3px dashed #7179e6;border-radius:8px;display:flex;align-items:center;justify-content:center;color:#7179e6;font-size:26px">imagem do artigo compilado</div>')
    selos = "".join(f'<span class="chip n2" style="margin:0 8px 10px 0;font-size:18px">{s}</span>' for s in ("Modelo IEEEtran", "12 páginas (limite 15)", "Pronto para o Overleaf"))
    return sec("<h1>O artigo está pronto</h1>" + f'<div style="position:absolute;left:110px;right:80px;top:190px;display:flex;gap:30px;align-items:flex-start">{img}'
               f'<div style="flex:1;font-size:21px;line-height:1.5;padding-top:20px">{selos}<p style="margin-top:16px">Fases 1 a 4 completas: <b style="color:#5a62d4">16 métricas</b>, '
               f'<b style="color:#5a62d4">16 hipóteses</b>, julgamento das três características, <b style="color:#5a62d4">matriz multiplataforma</b>, '
               f'ação de melhoria e <b style="color:#5a62d4">conclusão</b>.</p><p style="margin-top:16px">Gráficos interativos e dados na GitPage: '
               f'<b>Fase 4 › Síntese e Conclusão</b>.</p></div></div>')


def resumo(cod, oque):
    m = gf.metricas()
    h, (mt, prev, cl) = next((h, v) for h, v in gf.HIPOTESES.items() if v[0] == cod)
    v, nv = m[cod]
    obt = gf.NIVEIS.index(nv)
    if cl == "Refutada":
        sent = gf.SENTIDO.get(h, "melhor" if obt > prev else "pior")
        chip = f'<span class="chip hr" style="font-size:13px;padding:2px 9px">Refutada {"↑" if sent == "melhor" else "↓"} {sent}</span>'
    else:
        chip = '<span class="chip hc" style="font-size:13px;padding:2px 9px">Confirmada</span>'
    return (f'<div style="flex:1;background:#e1e3f7;border-radius:14px;padding:12px 18px;font-size:16.5px;line-height:1.4">'
            f'<b style="color:#5a62d4;font-size:18px">{cod}</b> <b>{gf.e(gf.METRICAS[cod][1])}</b> · {oque}<br>'
            f'<b>{h}</b> previa <b>{gf.NIVEIS[prev]}</b>; deu <b>{gf.fmt(v, gf.METRICAS[cod][3])} ({nv})</b> {chip}</div>')


def slide_detalhe(t, faixa, resumos, paineis, nota, topo=False):
    return sec(titulo(t, faixa, topo)
               + f'<div class="corpo" style="top:290px"><div style="display:flex;gap:24px">{resumos}</div>'
               + f'<div style="display:flex;gap:24px;margin-top:18px">{paineis}</div></div><div class="nota">{nota}</div>')


def extra_matriz():
    res, movel = dados_matriz()
    itens = []
    for cat in ("Computador", "Celular", "Tablet"):
        rs = [r for r in res if r["categoria"] == cat]
        conc = sum(int(r["tarefas_concluidas"]) for r in rs)
        tot = sum(int(r["tarefas"]) for r in rs)
        itens.append((f"{cat}: tarefas", conc / tot * 100, "#2a6fc9"))
        if cat != "Computador":
            ad = sum(int(r["paginas_adaptadas"] or 0) for r in rs)
            av = sum(int(r["paginas_avaliadas"] or 0) for r in rs)
            itens.append((f"{cat}: adaptadas", ad / av * 100, "#d8434a"))
    login = sum(1 for r in movel if r.get("login_cabe_na_tela") == "sim")
    itens.append(("Login UnB no celular", login / len(movel) * 100, "#2a6fc9"))
    return mini_barras(f"Matriz · {len(res)} perfis em 7 navegadores", itens, alt=43, fonte=16.5)


def extra_acess():
    m9 = {r["valor_recorte"]: float(r["valor"]) for r in ler("metricas.csv") if r["metrica"] == "M9" and r["recorte"] == "pagina"}
    nomes = {"T1": "T1 Notas", "T2": "T2 Portal", "T3": "T3 Atestado", "T4": "T4 Índices", "T5": "T5 Turma Virtual", "T6": "T6 Calendário"}
    p1 = mini_barras("M9 · erros WAVE por página (Excelente = 0)",
                     [(nomes[t], m9[t], "#d8434a" if m9[t] > 5 else ("#e39a3b" if m9[t] > 2 else "#7fb0e6")) for t in sorted(m9)], sufixo="", vmax=40, alt=46, fonte=18)
    m10 = {r["valor_recorte"]: float(r["valor"]) * 100 for r in ler("metricas.csv") if r["metrica"] == "M10" and r["recorte"] == "criterio"}
    rot = {"a": "(a) teclado", "b": "(b) foco visível", "c": "(c) zoom 200%", "d": "(d) nome no leitor"}
    p2 = mini_barras("M10 · páginas que atendem cada critério (de 6)", [(rot[k], m10[k], cor_pct(m10[k])) for k in "abcd"], alt=69, fonte=18)
    return p1 + p2


def painel_m14():
    return extra_flex(so_m14=True)


def extra_flex(so_m14=False):
    linhas = list(csv.DictReader((RAIZ / "dados/brutos/flexibilidade/paginas-adaptadas.csv").open(encoding="utf-8")))
    rot = {"a": "(a) cabe sem zoom", "b": "(b) texto ≥ 12 px", "c": "(c) sem sobreposição", "d": "(d) menu ao toque", "e": "(e) alvo ≥ 24 px"}
    vals = {k: sum(x["crit_" + k] == "sim" for x in linhas) / len(linhas) * 100 for k in "abcde"}
    p1 = mini_barras("M14 · verificações que atendem cada critério (de 12)", [(rot[k], vals[k], cor_pct(vals[k])) for k in "abcde"], alt=52, fonte=18)
    if so_m14:
        return p1
    m13 = [(r["valor_recorte"].split(" (")[0].replace("WebKit", "Safari (WebKit)"), float(r["valor"]) * 100, "#2a6fc9")
           for r in ler("metricas.csv") if r["metrica"] == "M13" and r["recorte"] == "navegador"]
    p2 = mini_barras("M13 · tarefas concluídas por navegador (de 6)", m13)
    return p1 + p2


def slide_final():
    conc = [("Funciona e está correto", "Funções das 6 tarefas existem, dados 97% iguais ao histórico, 120 de 120 tarefas em 20 perfis."),
            ("A acessibilidade exclui", "13,17 erros por página; sem mouse, o menu Ensino não abre e 4 das 6 tarefas não começam."),
            ("Não foi feito para o celular", "0 de 60 páginas adaptadas; texto de 2,9 a 6,8 px. O login da UnB já é responsivo.")]
    mel = [("Layout responsivo", "&lt;meta viewport&gt; e layout fluido · M14"), ("Menu acessível", "teclado, leitor de tela e toque · M10"),
           ("Erros do WAVE", "alt em 47 imagens, idioma, rótulos · M9"), ("Aviso de sessão expirada", "único cenário não tratado · M20"),
           ("Turma Virtual mais leve", "19 s no 4G; página pula (CLS 1,05)"), ("Planejamento do curso", "as 4 funções ausentes · M1")]
    c = "".join(f'<div class="bloco" style="min-height:118px;border-radius:26px"><div class="ic" style="width:84px;font-size:52px;border-radius:26px 0 0 26px">{i}</div>'
                f'<div class="tx" style="padding:12px 20px"><h3 style="font-size:20px;margin-bottom:4px">{h}</h3><p style="font-size:16px;line-height:1.3">{t}</p></div></div>'
                for i, (h, t) in enumerate(conc, 1))
    m = "".join(f'<div class="rec" style="padding:8px 14px"><div class="nr" style="font-size:32px">{i}</div><div><h4 style="font-size:17px">{h}</h4><p style="font-size:14.5px">{t}</p></div></div>'
                for i, (h, t) in enumerate(mel, 1))
    return sec(titulo("Conclusão e melhorias", "O que os scripts mostram e o que a STI/UnB deve corrigir primeiro", True)
               + f'<div class="corpo" style="top:290px;display:flex;gap:30px"><div style="flex:1.05;display:flex;flex-direction:column;gap:14px">{c}</div>'
               + f'<div style="flex:1;display:flex;flex-direction:column;gap:9px">{m}</div></div>'
               + '<div class="nota">Limite: emulação reproduz navegador, tela e toque, mas não o sistema operacional nem o desempenho do aparelho.</div>')


def montar() -> list[str]:
    return [
        slide_metodo(),
        slide_metricas("Resultados das métricas", "7 métricas medidas por script · 3 hipóteses confirmadas, 4 refutadas", SISTEMA,
                       "Cada faixa foi fixada na Fase 2, antes da coleta; o ponto é o valor medido. O sistema vai bem em funções, dados, erros e navegadores, e mal em acessibilidade e celular.",
                       compacto=True),
        slide_detalhe("Acessibilidade", "Barreiras em todas as páginas: o menu principal não funciona sem mouse",
                      resumo("M9", "erros WCAG A/AA que o WAVE encontra na página") + resumo("M10", "teclado, foco, zoom 200% e leitor de tela"),
                      extra_acess(), "47 imagens sem texto alternativo, botões vazios e páginas sem idioma · o menu Ensino não recebe foco nem tem nome no leitor de tela.", True),
        slide_detalhe("Flexibilidade", "Funciona em todo navegador, não se adapta a nenhuma tela pequena",
                      resumo("M13", "6 tarefas × 4 navegadores sem falha") + resumo("M14", "página cabe na tela de 360 e 768 px"),
                      painel_m14() + extra_matriz(),
                      "Sem &lt;meta viewport&gt;, o navegador monta a página com 980 px e a reduz para caber na tela: 37% em 360 px, 78% em 768 px."),
        slide_fontes(),
        slide_final(),
        slide_artigo(),
    ]


NOMES_PECAS = ["01-teste-com-os-scripts", "02-resultados-metricas-e-hipoteses", "03-acessibilidade", "04-flexibilidade-e-matriz",
               "05-fontes-no-celular", "06-conclusao-e-melhorias", "07-artigo"]


def exportar_pecas(p):
    """Cada gráfico ou bloco de cada slide, com fundo transparente, para usar no Canva."""
    pecas = SAIDA / "pecas"
    pecas.mkdir(exist_ok=True)
    for velho in pecas.glob("*.png"):
        velho.unlink()
    p.add_style_tag(content="html,body,.s{background:transparent!important}.lat,.topo,h1,.faixa,.nota,.esq{visibility:hidden}"
                    ".corpo{padding:34px 12px 12px!important;height:auto!important;bottom:auto!important}")
    for i, sec_ in enumerate(p.locator("section.s").all()):
        nome = NOMES_PECAS[i] if i < len(NOMES_PECAS) else f"{i + 1:02d}"
        blocos = sec_.locator(".bloco")
        if blocos.count() and not sec_.locator(".rec").count():
            for j, b in enumerate(blocos.all(), 1):
                b.screenshot(path=str(pecas / f"{nome}-{j}.png"), omit_background=True, timeout=60000)
            continue
        alvo = sec_.locator(".corpo")
        if not alvo.count():
            alvo = sec_.locator("img")
        alvo.first.screenshot(path=str(pecas / f"{nome}.png"), omit_background=True, timeout=60000)
    print(len(list(pecas.glob("*.png"))), "peças em", pecas.relative_to(RAIZ))


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    for velho in SAIDA.glob("slide-*.png"):
        velho.unlink()
    slides = montar()
    fonte = SAIDA / "slides-complementares.html"
    fonte.write_text(f"<!doctype html><html lang='pt-BR'><meta charset='utf-8'><style>{CSS}</style><body>{''.join(slides)}</body></html>", encoding="utf-8")
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        p = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        p.goto(fonte.as_uri())
        p.wait_for_load_state("networkidle")
        p.evaluate("document.fonts.ready")
        for i, el in enumerate(p.locator("section.s").all(), 1):
            el.screenshot(path=str(SAIDA / f"slide-{i:02d}.png"), timeout=60000)
            print(SAIDA.relative_to(RAIZ) / f"slide-{i:02d}.png")
        p.pdf(path=str(SAIDA / "slides-complementares.pdf"), width=f"{W}px", height=f"{H}px",
              print_background=True, margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        exportar_pecas(p)
        b.close()
    fonte.unlink()


if __name__ == "__main__":
    main()
