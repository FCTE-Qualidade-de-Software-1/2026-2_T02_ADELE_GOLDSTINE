"""Coleta automatizada de Flexibilidade (M13, M14) e de desempenho no SIGAA/UnB.

Executa as tarefas T1 a T6 do escopo da Fase 1 com o Playwright, na conta do
avaliador, só com consultas (nenhum dado acadêmico é alterado), e grava:

- um registro JSON por execução de tarefa (``dados/brutos/<grupo>/automatizado/``);
- capturas de tela com o texto e as imagens borrados (evidências publicáveis);
- opcionalmente, capturas sem borrão numa pasta local fora do repositório.

As credenciais vêm só das variáveis de ambiente SIGAA_USUARIO e SIGAA_SENHA e
nunca são gravadas. Uso (ver coleta/README.md):

    python coleta/sigaa_coleta.py navegadores
    python coleta/sigaa_coleta.py telas
    python coleta/sigaa_coleta.py desempenho --repeticoes 5
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import platform
import re
import sys
import time
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
LOGIN = ("https://autenticacao.unb.br/sso-server/login"
         "?service=https%3A%2F%2Fsig.unb.br%2Fsigaa%2Flogin%2Fcas")
PAUSA_S = 3  # intervalo entre ações, para não sobrecarregar o ambiente de produção

# Itens de menu permitidos. O script só aciona consultas desta lista; ações como
# trancamento ou matrícula nunca são clicadas.
MENU_PERMITIDO = {"Consultar Minhas Notas", "Emitir Atestado de Matrícula",
                  "Consultar Índices Acadêmicos", "Calendário Acadêmico"}

TURMA_T5 = "FUNDAMENTOS DE REDES DE COMPUTADORES"
MATERIAL_T5 = "Plano de Ensino"
MODO_T5 = "arquivo"
SEMESTRE = "2026.2"

# Marcadores que indicam que a página final da tarefa foi exibida corretamente
MARCADORES = {
    "T1": ["Notas do(a) Aluno(a)", "Situação"],
    "T2": ["Turmas do Semestre", "Horário"],
    "T3": ["Atestado de Matrícula", "Turmas Matriculadas"],
    "T4": ["Índices Acadêmicos", "IRA"],
    "T5": ["Turma Virtual", MATERIAL_T5],
    "T6": ["Dados do Calendário Acadêmico", "Trancamento de Turmas"],
}
PAGINAS = {
    "T1": "Relatório de notas do aluno",
    "T2": "Portal do Discente (Turmas do Semestre)",
    "T3": "Atestado de matrícula",
    "T4": "Índices acadêmicos",
    "T5": "Turma Virtual (materiais da turma)",
    "T6": "Visualização do calendário acadêmico 2026.2",
}

# Perfis de rede e CPU. "4g_lenta" reproduz o perfil de limitação aplicado pelo
# Lighthouse com limitação no navegador (DevTools throttling) para dispositivos
# móveis: latência de requisição de 562,5 ms (150 ms de RTT x 3,75), download de
# 1.474,56 kbit/s, upload de 675 kbit/s e CPU 4 vezes mais lenta.
REDES = {
    "local": None,
    "4g_lenta": {"latency": 562.5, "down_kbps": 1474.56, "up_kbps": 675, "cpu": 4},
}

DISPOSITIVOS = {
    "computador": {"viewport": {"width": 1366, "height": 768}, "toque": False},
    "tablet_768": {"viewport": {"width": 768, "height": 1024}, "toque": True,
                   "device_scale_factor": 2, "is_mobile": True,
                   "user_agent": ("Mozilla/5.0 (Linux; Android 14; SM-X200) AppleWebKit/537.36 "
                                  "(KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36")},
    "celular_360": {"viewport": {"width": 360, "height": 800}, "toque": True,
                    "device_scale_factor": 3, "is_mobile": True,
                    "user_agent": ("Mozilla/5.0 (Linux; Android 14; SM-A155M) AppleWebKit/537.36 "
                                   "(KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36")},
}

# CSS aplicado só no momento da captura publicável: o texto vira um borrão e as
# imagens (como a foto do estudante) ficam desfocadas, sem alterar o layout.
CSS_BORRAO = """
body *:not(script):not(style) { color: transparent !important;
  text-shadow: 0 0 12px rgba(0,0,0,.7) !important; }
img { filter: blur(40px) grayscale(1) !important; }
input, textarea, select { color: transparent !important; }
"""

# --------------------------------------------------------------------------
# Scripts executados na página
# --------------------------------------------------------------------------

# Observadores de responsividade e estabilidade, instalados antes dos scripts de cada página:
# Long Tasks (tarefas > 50 ms na thread principal), Layout Instability (CLS) e Event Timing
# (duração de cada evento de interação, base do INP).
JS_OBSERVADORES = """
window.__q = {lt: [], cls: 0, ev: []};
try { new PerformanceObserver(l => { for (const e of l.getEntries()) __q.lt.push([e.startTime, e.duration]); })
  .observe({type: 'longtask', buffered: true}); } catch (e) {}
try { new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) __q.cls += e.value; })
  .observe({type: 'layout-shift', buffered: true}); } catch (e) {}
try { new PerformanceObserver(l => { for (const e of l.getEntries()) __q.ev.push([e.name, e.duration, e.processingEnd - e.processingStart]); })
  .observe({type: 'event', buffered: true, durationThreshold: 16}); } catch (e) {}
"""

# Fluidez da rolagem: rola a página do topo ao fim em passos por quadro e mede o intervalo entre quadros.
JS_ROLAGEM = """async () => {
  const alt = Math.max(document.documentElement.scrollHeight - innerHeight, 0);
  window.scrollTo(0, 0);
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  const passos = Math.max(60, Math.min(240, Math.ceil(alt / 20)));
  const dt = []; let ant = performance.now();
  for (let i = 1; i <= passos; i++) {
    window.scrollTo(0, alt * i / passos);
    await new Promise(r => requestAnimationFrame(r));
    const t = performance.now(); dt.push(t - ant); ant = t;
  }
  window.scrollTo(0, 0);
  dt.sort((a, b) => a - b);
  let total = 0; for (let i = 0; i < dt.length; i++) total += dt[i];
  return {quadros: dt.length, altura_rolada_px: Math.round(alt),
          fps_medio: +(1000 * dt.length / total).toFixed(1),
          quadro_p95_ms: +dt[Math.floor(0.95 * (dt.length - 1))].toFixed(1),
          quadros_acima_50ms: dt.filter(x => x > 50).length};
}"""

JS_RESPONSIVIDADE = """() => {
  const q = window.__q || {lt: [], cls: 0, ev: []};
  let tbt = 0, maior = 0; for (const [ini, d] of q.lt) { tbt += Math.max(0, d - 50); maior = Math.max(maior, d); }
  let ev = 0; for (const e of q.ev) ev = Math.max(ev, e[1]);
  return {tarefas_longas: q.lt.length, tbt_ms: Math.round(tbt), maior_tarefa_ms: Math.round(maior),
          cls: +q.cls.toFixed(4), maior_evento_ms: Math.round(ev)};
}"""

JS_DESEMPENHO = """async () => {
  const n = performance.getEntriesByType('navigation')[0] || {};
  const r = performance.getEntriesByType('resource');
  const fcp = performance.getEntriesByName('first-contentful-paint')[0];
  const lcp = await new Promise(res => {
    let v = null;
    try {
      new PerformanceObserver(l => { const e = l.getEntries(); if (e.length) v = e[e.length-1].startTime; })
        .observe({type: 'largest-contentful-paint', buffered: true});
    } catch (e) {}
    setTimeout(() => res(v), 400);
  });
  const soma = (k) => { let a = 0; for (let i = 0; i < r.length; i++) a += (r[i][k] || 0); return a; };  // sem reduce: o Prototype.js do SIGAA o sobrescreve
  return {
    ttfb_ms: n.responseStart ?? null,
    dcl_ms: n.domContentLoadedEventEnd ?? null,
    load_ms: n.loadEventEnd ?? null,
    fcp_ms: fcp ? fcp.startTime : null,
    lcp_ms: lcp,
    tipo_navegacao: n.type ?? null,
    requisicoes: 1 + r.length,
    bytes_transferidos: (n.transferSize || 0) + soma('transferSize'),
    bytes_codificados: (n.encodedBodySize || 0) + soma('encodedBodySize'),
    html_bytes: n.decodedBodySize ?? null,
    elementos_dom: document.getElementsByTagName('*').length,
  };
}"""

# Verificações automáticas dos critérios (a), (b), (c) e (e) de M14.
JS_ADAPTACAO = r"""() => {
  const vv = window.visualViewport;
  const escala = vv ? vv.scale : 1;
  const larguraLayout = document.documentElement.clientWidth;
  const larguraConteudo = Math.max(document.documentElement.scrollWidth, document.body.scrollWidth);
  const meta = document.querySelector('meta[name=viewport]');
  const banner = [...document.querySelectorAll('div')].find(d => /Nós usamos cookies/.test(d.textContent) && getComputedStyle(d).position === 'fixed');
  const fora = (el) => banner && banner.contains(el);
  const visivel = (el) => {
    const s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none' || +s.opacity === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };
  // (b) tamanho de fonte efetivo de cada texto visível
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let tot = 0, peq = 0, minimo = 999; const folhas = new Set();
  while (w.nextNode()) {
    const t = w.currentNode; if (!t.textContent.trim()) continue;
    const el = t.parentElement; if (!el || fora(el) || !visivel(el)) continue;
    if (['SCRIPT','STYLE','NOSCRIPT','OPTION'].includes(el.tagName)) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize) * escala;
    tot++; if (fs < 12) peq++; if (fs < minimo) minimo = fs; folhas.add(el);
  }
  // Camadas fixas (como o aviso de cookies) cobrem a página por projeto e são dispensáveis;
  // elementos posicionados fora do documento (diálogos ocultos) não são vistos pelo usuário.
  const emCamadaFixa = (el) => { for (let e = el; e && e !== document.body; e = e.parentElement) { const p = getComputedStyle(e).position; if (p === 'fixed' || p === 'sticky') return true; } return false; };
  const naTela = (r) => r.right + scrollX > 0 && r.bottom + scrollY > 0 && r.left + scrollX < larguraConteudo + 1;
  // (c) sobreposição entre textos: caixas reais de cada trecho de texto (Range.getClientRects),
  //     para que um link quebrado em duas linhas não seja tratado como um retângulo único
  const caixas = [];
  const w2 = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let idx = 0;
  while (w2.nextNode()) {
    const t = w2.currentNode; if (!t.textContent.trim()) continue;
    const el = t.parentElement; if (!el || !folhas.has(el) || emCamadaFixa(el)) continue;
    const rg = document.createRange(); rg.selectNodeContents(t);
    for (const r of rg.getClientRects()) if (r.width > 1 && r.height > 1 && naTela(r)) caixas.push({n: idx, el, r});
    idx++;
  }
  const lista = [...folhas].map(el => ({el}));
  let sobrepostos = 0; const exemplos = [];
  const desc = (el) => el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).join('.') : '');
  const fmt = (r) => [r.left, r.top, r.width, r.height].map(Math.round).join(',');
  for (let i = 0; i < caixas.length; i++) for (let j = i + 1; j < caixas.length; j++) {
    const a = caixas[i], b = caixas[j];
    if (a.n === b.n) continue;
    const x = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left);
    const y = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
    if (x <= 0 || y <= 0) continue;
    const menor = Math.min(a.r.width * a.r.height, b.r.width * b.r.height);
    if (x * y > 0.25 * menor) { sobrepostos++; if (exemplos.length < 5) exemplos.push(desc(a.el) + '@' + fmt(a.r) + ' x ' + desc(b.el) + '@' + fmt(b.r)); }
  }
  // (c) texto coberto por controles ou imagens (ex.: título sob os botões da barra)
  const cobertores = [...document.querySelectorAll('button, input[type=button], input[type=submit], input[type=image], img, select')]
    .filter(el => visivel(el) && !emCamadaFixa(el)).map(el => ({el, r: el.getBoundingClientRect()})).filter(o => naTela(o.r));
  let cobertos = 0;
  for (const c of caixas) for (const o of cobertores) {
    if (o.el.contains(c.el) || c.el.contains(o.el)) continue;
    const x = Math.min(c.r.right, o.r.right) - Math.max(c.r.left, o.r.left);
    const y = Math.min(c.r.bottom, o.r.bottom) - Math.max(c.r.top, o.r.top);
    if (x > 0 && y > 0 && x * y > 0.25 * c.r.width * c.r.height) { cobertos++; if (exemplos.length < 8) exemplos.push('coberto: ' + desc(c.el) + '@' + fmt(c.r) + ' por ' + desc(o.el) + '@' + fmt(o.r)); break; }
  }
  let cortados = 0;
  for (const {el} of lista) {
    const s = getComputedStyle(el);
    if (!emCamadaFixa(el) && /(hidden|clip)/.test(s.overflowX + s.overflow) && el.scrollWidth > el.clientWidth + 1) { cortados++; if (exemplos.length < 8) exemplos.push('cortado: ' + desc(el)); }
  }
  // (e) área de toque dos controles (WCAG 2.2, critério 2.5.8)
  const sel = 'a[href], a[onclick], button, input:not([type=hidden]), select, textarea, [role=button], td[class^=ThemeOfficeMainItem]';
  const alvos = [...document.querySelectorAll(sel)].filter(el => !fora(el) && visivel(el));
  const rects = alvos.map(el => el.getBoundingClientRect());
  const inline = (el) => {
    if (el.tagName !== 'A' || getComputedStyle(el).display !== 'inline') return false;
    const p = el.parentElement; if (!p) return false;
    return p.textContent.trim().length > el.textContent.trim().length + 15;
  };
  let pequenos = 0, excecaoInline = 0, espacados = 0;
  const minEf = 24 / escala;  // 24 px CSS efetivos na tela do aparelho
  alvos.forEach((el, i) => {
    const r = rects[i];
    if (r.width >= minEf && r.height >= minEf) return;
    if (inline(el)) { excecaoInline++; return; }
    // exceção de espaçamento: um círculo de 24 px centrado no alvo não pode tocar outro alvo
    const cx = r.left + r.width / 2, cy = r.top + r.height / 2, raio = minEf / 2;
    const toca = rects.some((o, k) => {
      if (k === i || alvos[k].contains(el) || el.contains(alvos[k])) return false;
      const px = Math.max(o.left, Math.min(cx, o.right)), py = Math.max(o.top, Math.min(cy, o.bottom));
      return (px - cx) ** 2 + (py - cy) ** 2 < raio ** 2;
    });
    if (toca) pequenos++; else espacados++;
  });
  return {
    escala_visual: escala, largura_layout_px: larguraLayout, largura_conteudo_px: larguraConteudo,
    meta_viewport: meta ? meta.getAttribute('content') : null,
    textos: tot, textos_menores_12px: peq, fonte_minima_efetiva_px: tot ? +minimo.toFixed(2) : null,
    textos_sobrepostos: sobrepostos, textos_cobertos: cobertos, textos_cortados: cortados, exemplos_c: exemplos,
    alvos: alvos.length, alvos_abaixo_24px: pequenos, alvos_excecao_inline: excecaoInline,
    alvos_excecao_espacamento: espacados, banner_cookies: !!banner,
  };
}"""

JS_ASSINATURA = """() => ({
  tabelas: document.querySelectorAll('table').length,
  linhas: document.querySelectorAll('table tr').length,
  links: document.querySelectorAll('a').length,
  menu_portal: document.querySelectorAll('td[class^=ThemeOfficeMainItem]').length,
  css_ok: [...document.querySelectorAll('link[rel=stylesheet]')].every(l => !!l.sheet),
  folhas_estilo: document.styleSheets.length,
  rodape: (document.body.innerText.match(/app\\d+\\.sigaa\\d+/) || [null])[0],
  versao: (document.body.innerText.match(/v(\\d+\\.\\d+\\.\\d+\\.\\d+)/) || [null, null])[1],
})"""


# --------------------------------------------------------------------------
# Sessão e navegação
# --------------------------------------------------------------------------

class Sessao:
    def __init__(self, pw, motor: str, dispositivo: str, rede: str = "local",
                 canal: str | None = None, sem_cache: bool = False,
                 cfg: dict | None = None, executavel: str | None = None,
                 argumentos: list[str] | None = None):
        """`cfg`, `executavel` e `argumentos` são usados pela matriz multiplataforma
        (matriz_dispositivos.py): perfil de dispositivo próprio e navegadores baseados
        no Chromium instalados fora do sistema (Edge, Brave, Opera, Vivaldi)."""
        self.motor, self.dispositivo, self.rede = motor, dispositivo, rede
        cfg = cfg or DISPOSITIVOS[dispositivo]
        tipo = getattr(pw, motor)
        lanc = {"timeout": 90000}
        if canal:
            lanc["channel"] = canal
        if executavel:
            lanc["executable_path"] = executavel
        if argumentos:
            lanc["args"] = argumentos
        self.browser = tipo.launch(**lanc)
        opts = {"viewport": cfg["viewport"], "locale": "pt-BR", "accept_downloads": True,
                "has_touch": cfg["toque"]}
        for k in ("device_scale_factor", "user_agent"):
            if k in cfg:
                opts[k] = cfg[k]
        if "user_agent" in opts:  # {v}: versão principal do navegador em execução
            opts["user_agent"] = opts["user_agent"].replace("{v}", self.browser.version.split(".")[0])
        if cfg.get("is_mobile") and motor in ("chromium", "webkit"):  # o Firefox não emula is_mobile
            opts["is_mobile"] = True
        self.ctx = self.browser.new_context(**opts)
        self.ctx.add_init_script(JS_OBSERVADORES)
        self.pg: Page = self.ctx.new_page()
        self.toque = cfg["toque"]
        self.falhas_rede: list[str] = []
        self.pg.on("requestfailed", lambda r: self.falhas_rede.append(f"falhou [{r.failure}] {r.url[:120]}"))
        self.pg.on("response", lambda r: r.status >= 400 and self.falhas_rede.append(f"{r.status} {r.url[:120]}"))
        self.erros_console: list[str] = []
        self.pg.on("pageerror", lambda e: self.erros_console.append(str(e)[:200]))
        if motor == "chromium":
            self.cdp = self.ctx.new_cdp_session(self.pg)
            self.cdp.send("Network.enable")
            if sem_cache:
                self.cdp.send("Network.setCacheDisabled", {"cacheDisabled": True})
            perfil = REDES[rede]
            if perfil:
                self.cdp.send("Network.emulateNetworkConditions", {
                    "offline": False, "latency": perfil["latency"],
                    "downloadThroughput": perfil["down_kbps"] * 1000 / 8,
                    "uploadThroughput": perfil["up_kbps"] * 1000 / 8})
                self.cdp.send("Emulation.setCPUThrottlingRate", {"rate": perfil["cpu"]})
        elif rede != "local":
            raise SystemExit("A limitação de rede só está disponível no Chromium.")
        self.versao = self.browser.version
        self.home = None
        self.tentativas_estaticos = 0
        self.toques_corrigidos = 0

    def login(self):
        pg = self.pg
        pg.goto(LOGIN, wait_until="networkidle", timeout=120000)
        pg.fill("input[name=username]", os.environ["SIGAA_USUARIO"])
        pg.fill("input[name=password]", os.environ["SIGAA_SENHA"])
        try:
            pg.click("button[name=submit]", timeout=15000)
        except Exception:  # noqa: BLE001  (botão instável na animação da página: envia com Enter)
            pg.press("input[name=password]", "Enter")
        # No WebKit, o "networkidle" pode chegar antes do redirecionamento do CAS para o SIGAA
        try:
            pg.wait_for_url(re.compile(r"https://sigaa?\.unb\.br/"), timeout=60000)
        except Exception:  # noqa: BLE001
            pass
        pg.wait_for_load_state("networkidle", timeout=120000)
        if "telaAvisoLogon" in pg.url:
            with pg.expect_navigation(wait_until="load", timeout=120000):
                pg.locator("input[type=submit][value*='Continuar']").first.click()
            pg.wait_for_load_state("networkidle", timeout=120000)
        if "discente" not in pg.url:
            raise SystemExit(f"Login não chegou ao Portal do Discente: {pg.url}")
        self.home = pg.url
        self.garantir_estaticos()

    def garantir_estaticos(self, maximo: int = 5) -> int:
        """Recarrega o portal se CSS e JavaScript não carregaram (falha do servidor).

        O portal só é considerado carregado quando o menu horizontal foi montado
        pelo JavaScript. Cada recarga é contada e registrada.
        """
        falhas = 0
        for _ in range(maximo):
            if self.pg.locator("td.ThemeOfficeMainItem").count() > 0:
                break
            falhas += 1
            time.sleep(PAUSA_S)
            self.pg.goto(self.home, wait_until="networkidle", timeout=120000)
        self.tentativas_estaticos += falhas
        return falhas

    def ir_home(self):
        time.sleep(PAUSA_S)
        self.pg.goto(self.home, wait_until="networkidle", timeout=180000)
        return self.garantir_estaticos()

    def tocar(self, locator):
        """Toque na tela.

        No WebKit em modo móvel, o tap() do Playwright usa a posição do elemento em
        pixels de layout, mas o toque é aplicado em pixels da área visível: quando o
        navegador reduz a página (sem <meta viewport>), o toque cai em outro ponto. Aqui
        a posição é convertida pela escala e pelo deslocamento da área visível
        (visualViewport), e o toque real é enviado nesse ponto; a correção é contada.
        """
        if self.motor == "webkit" and self.toque:
            locator.scroll_into_view_if_needed(timeout=15000)
            bb = locator.bounding_box(timeout=15000)
            esc, dx, dy = self.pg.evaluate("[visualViewport.scale, visualViewport.offsetLeft, visualViewport.offsetTop]")
            x = (bb["x"] + bb["width"] / 2 - dx) * esc
            y = (bb["y"] + bb["height"] / 2 - dy) * esc
            self.pg.touchscreen.tap(x, y)
            self.toques_corrigidos += 1
        else:
            locator.tap()

    def acionar(self, locator):
        if self.toque:
            self.tocar(locator)
        else:
            locator.click()

    def menu_ensino(self, item: str) -> bool:
        """Abre Ensino > item. Retorna se o submenu abriu pela interação do dispositivo.

        O JSCookMenu troca a classe do item sob o ponteiro (ThemeOfficeMainItem ->
        ThemeOfficeMainItemHover), por isso os seletores usam o prefixo da classe.
        """
        assert item in MENU_PERMITIDO, item
        principal = self.pg.locator("td[class^='ThemeOfficeMainItem']:has-text('Ensino')").first
        alvo = self.pg.locator(f"td.ThemeOfficeMenuItemText:text-is('{item}')").first
        alvo_linha = self.pg.locator(f"tr[class^='ThemeOfficeMenuItem']:has(td.ThemeOfficeMenuItemText:text-is('{item}'))").first
        self.alvos_usados.append(self.medir_alvo(principal))
        t0 = time.perf_counter()
        if self.toque:
            self.tocar(principal)
        else:
            principal.hover()
        try:
            alvo.wait_for(state="visible", timeout=3000)
            self.abertura_menu_ms = round((time.perf_counter() - t0) * 1000)
        except Exception:  # noqa: BLE001
            self.abertura_menu_ms = None
        abriu = alvo.is_visible()
        if not abriu:  # registra a falha ao toque e segue com o ponteiro para medir o resto
            principal.hover()
            self.pg.wait_for_timeout(700)
        self.alvos_usados.append(self.medir_alvo(alvo_linha))
        if abriu and self.toque:
            self.tocar(alvo)
        else:
            alvo.click()
        return abriu

    def medir_alvo(self, loc) -> dict:
        try:
            r = loc.bounding_box(timeout=5000) or {"width": 0, "height": 0}
        except Exception:  # noqa: BLE001
            return {"largura_px": None, "altura_px": None}
        escala = self.pg.evaluate("window.visualViewport ? visualViewport.scale : 1")
        return {"largura_px": round(r["width"] * escala, 1), "altura_px": round(r["height"] * escala, 1)}

    def fechar(self):
        self.browser.close()


def esperar(pg: Page):
    pg.wait_for_load_state("load", timeout=180000)
    try:
        pg.wait_for_load_state("networkidle", timeout=90000)
    except Exception:
        pass


def executar_tarefa(s: Sessao, tarefa: str) -> dict:
    """Executa a tarefa a partir do portal e devolve as medidas da página final."""
    pg = s.pg
    s.alvos_usados = []
    s.abertura_menu_ms = None
    s.falhas_rede.clear()
    s.erros_console.clear()
    reg = {"tarefa": tarefa, "passos": [], "toque_menu": None, "download": None}
    falhas_estaticos = s.ir_home()

    def passo(nome, acao):
        t0 = time.perf_counter()
        with pg.expect_navigation(wait_until="load", timeout=180000):
            acao()
        esperar(pg)
        reg["passos"].append({"passo": nome, "tempo_ms": round((time.perf_counter() - t0) * 1000),
                              **pg.evaluate(JS_DESEMPENHO), **pg.evaluate(JS_RESPONSIVIDADE)})

    if tarefa == "T2":
        passo("portal", lambda: pg.reload(wait_until="load"))
    elif tarefa in ("T1", "T3", "T4"):
        item = {"T1": "Consultar Minhas Notas", "T3": "Emitir Atestado de Matrícula",
                "T4": "Consultar Índices Acadêmicos"}[tarefa]
        passo(item, lambda: reg.__setitem__("toque_menu", s.menu_ensino(item)))
    elif tarefa == "T6":
        passo("lista de calendários", lambda: reg.__setitem__("toque_menu", s.menu_ensino("Calendário Acadêmico")))
        lupa = pg.locator(f"thead:has-text('Calendário {SEMESTRE}') + tbody a[title='Visualizar Calendário Acadêmico']").first
        s.alvos_usados.append(s.medir_alvo(lupa))
        passo(f"calendário {SEMESTRE}", lambda: s.acionar(lupa))
    elif tarefa == "T5":
        turma = pg.locator(f"a:text-is('{TURMA_T5}')").first
        s.alvos_usados.append(s.medir_alvo(turma))
        passo("turma virtual", lambda: s.acionar(turma))
        if MODO_T5 == "noticia":
            not_loc = pg.locator("#formMenu .itemMenu:has-text('Notícias')").first
            s.alvos_usados.append(s.medir_alvo(not_loc))
            passo("notícias", lambda: s.acionar(not_loc))
            vis = pg.locator("a[title*='Visualizar'], img[title*='Visualizar']").first
            s.alvos_usados.append(s.medir_alvo(vis))
            passo("visualizar notícia", lambda: s.acionar(vis))
        else:
            menu_mat = pg.locator("#formMenu div:text-is('Materiais'), #formMenu td:text-is('Materiais'), #formMenu :text-is('Materiais')").first
            try:
                s.alvos_usados.append(s.medir_alvo(menu_mat))
                s.acionar(menu_mat)
                try:
                    pg.locator("#formMenu :text-is('Conteúdo'), #formMenu :text-is('Arquivos')").first.wait_for(state="visible", timeout=3000)
                    reg["toque_menu"] = True
                except Exception:  # noqa: BLE001
                    reg["toque_menu"] = False
            except Exception as e:  # noqa: BLE001
                reg["toque_menu"] = False
                reg["erro_menu_materiais"] = type(e).__name__
            mat = pg.locator(f"#formAva a:text-is('{MATERIAL_T5}')").first
            s.alvos_usados.append(s.medir_alvo(mat))
            t0 = time.perf_counter()
            try:
                with pg.expect_download(timeout=120000) as d:
                    s.acionar(mat)
                dl = d.value
                caminho = dl.path()
                reg["download"] = {"tempo_ms": round((time.perf_counter() - t0) * 1000),
                                   "bytes": os.path.getsize(caminho) if caminho else None,
                                   "extensao": Path(dl.suggested_filename).suffix.lower(),
                                   "falha": dl.failure()}
                dl.delete()
            except Exception as e:  # noqa: BLE001
                reg["download"] = {"falha": type(e).__name__}
    else:
        raise ValueError(tarefa)

    reg["abertura_menu_ms"] = s.abertura_menu_ms
    if getattr(s, "medir_rolagem", False):
        try:
            reg["rolagem"] = pg.evaluate(JS_ROLAGEM)
        except Exception as e:  # noqa: BLE001
            reg["rolagem"] = {"erro": type(e).__name__}
    texto = pg.locator("body").inner_text()
    reg["marcadores_ok"] = all(m.lower() in texto.lower() for m in MARCADORES[tarefa])
    if tarefa == "T5" and MODO_T5 == "arquivo":
        reg["marcadores_ok"] = reg["marcadores_ok"] and bool(reg["download"]) and not reg["download"].get("falha")
    reg["assinatura"] = pg.evaluate(JS_ASSINATURA)
    reg["falhas_estaticos_antes"] = falhas_estaticos
    reg["falhas_rede"] = list(s.falhas_rede)
    reg["erros_js"] = list(s.erros_console)
    reg["alvos_usados"] = list(s.alvos_usados)
    reg["url_final"] = pg.url.split("?")[0]
    if s.toques_corrigidos:
        reg["toques_corrigidos"] = s.toques_corrigidos
        s.toques_corrigidos = 0
    return reg


def falha_recurso_sigaa(reg: dict) -> list[str]:
    """Falhas de CSS/JS/imagem do próprio SIGAA: problema do servidor, não do navegador."""
    return [f for f in reg.get("falhas_rede", [])
            if ("sigaa.unb.br" in f or "autenticacao.unb.br" in f) and "ERR_ABORTED" not in f and "NS_BINDING_ABORTED" not in f]


def executar_com_repeticao(s: "Sessao", tarefa: str, maximo: int = 3) -> dict:
    """Executa a tarefa; se um recurso do SIGAA falhou, repete (até `maximo` vezes) e registra."""
    historico = []
    for tentativa in range(1, maximo + 1):
        try:
            reg = executar_tarefa(s, tarefa)
        except Exception as e:  # noqa: BLE001
            reg = {"tarefa": tarefa, "erro": f"{type(e).__name__}: {str(e)[:300]}"}
        falhas = falha_recurso_sigaa(reg)
        if (reg.get("assinatura") or {}).get("css_ok") is False:
            falhas.append("folha de estilo não carregada")
        reg["tentativa"] = tentativa
        reg["tentativas_anteriores"] = historico[:]
        if not falhas and not reg.get("erro"):
            return reg
        historico.append({"tentativa": tentativa, "erro": reg.get("erro"), "falhas_recurso_sigaa": falhas[:5]})
    return reg


def capturar(pg: Page, destino: Path, local: Path | None, nome: str):
    """Grava a captura borrada no repositório e, se pedido, a original fora dele."""
    destino.mkdir(parents=True, exist_ok=True)
    if local:
        local.mkdir(parents=True, exist_ok=True)
        pg.screenshot(path=str(local / f"{nome}.png"), full_page=True)
    h = pg.add_style_tag(content=CSS_BORRAO)
    pg.wait_for_timeout(300)
    pg.screenshot(path=str(destino / f"{nome}.jpg"), full_page=True, type="jpeg", quality=55)
    h.evaluate("e => e.remove()")
    return str((destino / f"{nome}.jpg").relative_to(RAIZ))


def base_registro(s: Sessao, extra: dict) -> dict:
    return {"data_hora": dt.datetime.now().isoformat(timespec="seconds"),
            "motor": s.motor, "navegador_versao": s.versao, "dispositivo": s.dispositivo,
            "rede": s.rede, "sistema": f"{platform.system()} {platform.release()}",
            "playwright": __import__("importlib.metadata").metadata.version("playwright"), **extra}


def gravar(arquivo: Path, reg: dict):
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    with arquivo.open("a", encoding="utf-8") as f:
        f.write(json.dumps(reg, ensure_ascii=False) + "\n")


# --------------------------------------------------------------------------
# Rotinas de coleta
# --------------------------------------------------------------------------

NAVEGADORES = {  # chave: (rótulo, motor do Playwright, canal, slug da evidência)
    "chrome": ("Google Chrome", "chromium", "chrome", "chromium"),
    "firefox": ("Firefox (Gecko, build do Playwright)", "firefox", None, "firefox"),
    "webkit": ("WebKit (motor do Safari, build do Playwright)", "webkit", None, "webkit"),
    "edge": ("Microsoft Edge", "chromium", "msedge", "msedge"),
}


def coletar_navegadores(args):
    saida = RAIZ / "dados/brutos/flexibilidade/automatizado/navegadores.jsonl"
    evid = RAIZ / "dados/brutos/flexibilidade/evidencias/navegadores"
    with sync_playwright() as pw:
        for chave in args.navegadores:
            rotulo, motor, canal, slug = NAVEGADORES[chave]
            s = Sessao(pw, motor, "computador", canal=canal)
            try:
                s.login()
                for t in args.tarefas:
                    for tentativa in (1, 2):
                        try:
                            reg = executar_tarefa(s, t)
                        except Exception as e:  # noqa: BLE001
                            reg = {"tarefa": t, "erro": f"{type(e).__name__}: {str(e)[:300]}"}
                        reg["tentativa"] = tentativa
                        if args.apenas_referencia:
                            reg["evidencia"] = None
                        else:
                            nome = f"{t}-{slug}-t{tentativa}"
                            try:
                                reg["evidencia"] = capturar(s.pg, evid, args.local and Path(args.local) / "navegadores", nome)
                            except Exception:  # noqa: BLE001
                                reg["evidencia"] = None
                        extra = {"navegador": rotulo, **reg}
                        if args.avaliador:
                            extra["avaliador"] = args.avaliador
                        if args.apenas_referencia:
                            extra["apenas_referencia"] = True
                        gravar(saida, base_registro(s, extra))
                        print(rotulo, t, "ok" if reg.get("marcadores_ok") else "FALHA", flush=True)
                        if reg.get("marcadores_ok"):
                            break
            finally:
                s.fechar()


def coletar_telas(args):
    saida = RAIZ / "dados/brutos/flexibilidade/automatizado/telas.jsonl"
    evid = RAIZ / "dados/brutos/flexibilidade/evidencias/telas"
    with sync_playwright() as pw:
        for disp in ("celular_360", "tablet_768"):
            s = Sessao(pw, "chromium", disp, canal="chrome")
            try:
                s.login()
                for t in args.tarefas:
                    reg = executar_com_repeticao(s, t)
                    if not reg.get("erro"):
                        try:
                            reg["adaptacao"] = s.pg.evaluate(JS_ADAPTACAO)
                        except Exception as e:  # noqa: BLE001
                            reg["erro"] = f"{type(e).__name__}: {str(e)[:300]}"
                    try:
                        reg["evidencia"] = capturar(s.pg, evid, args.local and Path(args.local) / "telas", f"{t}-{disp}")
                    except Exception:  # noqa: BLE001
                        reg["evidencia"] = None
                    gravar(saida, base_registro(s, {"navegador": "Google Chrome (modo de dispositivo)", **reg}))
                    print(disp, t, reg.get("adaptacao", {}).get("largura_conteudo_px"), flush=True)
            finally:
                s.fechar()


def coletar_desempenho(args):
    saida = RAIZ / "dados/brutos/desempenho/automatizado/execucoes.jsonl"
    todos = {"computador": ("computador", "local"), "celular_4g": ("celular_360", "4g_lenta")}
    cenarios = [todos[c] for c in args.cenarios]
    with sync_playwright() as pw:
        for disp, rede in cenarios:
            s = Sessao(pw, "chromium", disp, rede=rede, canal="chrome", sem_cache=True)
            s.medir_rolagem = True
            try:
                s.login()
                for rep in range(1, args.repeticoes + 1):
                    for t in args.tarefas:
                        reg = executar_com_repeticao(s, t)
                        reg["repeticao"] = rep
                        gravar(saida, base_registro(s, {"navegador": "Google Chrome", "cache": "desativado", **reg}))
                        tot = sum(p["load_ms"] or 0 for p in reg.get("passos", []))
                        print(disp, rede, rep, t, round(tot), flush=True)
            finally:
                s.fechar()


def main():
    global TURMA_T5, MATERIAL_T5, MODO_T5
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rotina", choices=["navegadores", "telas", "desempenho"])
    ap.add_argument("--tarefas", nargs="+", default=["T1", "T2", "T3", "T4", "T5", "T6"])
    ap.add_argument("--navegadores", nargs="+", choices=list(NAVEGADORES), default=["chrome", "firefox", "webkit", "edge"])
    ap.add_argument("--avaliador", help="primeiro nome do avaliador registrado no JSONL")
    ap.add_argument("--turma-t5", default=TURMA_T5, help="nome exato do link da turma no Portal do Discente para T5")
    ap.add_argument("--material-t5", default=MATERIAL_T5, help="nome exato do arquivo/material na Turma Virtual para T5")
    ap.add_argument("--modo-t5", choices=["arquivo", "noticia"], default="arquivo", help="arquivo (baixa material) ou noticia (abre notícia na Turma Virtual)")
    ap.add_argument("--apenas-referencia", action="store_true", help="registra Chrome só como referência de tabelas da mesma conta (não substitui M13)")
    ap.add_argument("--repeticoes", type=int, default=5)
    ap.add_argument("--cenarios", nargs="+", choices=["computador", "celular_4g"], default=["computador", "celular_4g"])
    ap.add_argument("--local", help="pasta FORA do repositório para as capturas sem borrão")
    args = ap.parse_args()
    TURMA_T5 = args.turma_t5
    MATERIAL_T5 = args.material_t5
    MODO_T5 = args.modo_t5
    MARCADORES["T5"] = ["Turma Virtual", "Notícia"] if MODO_T5 == "noticia" else ["Turma Virtual", MATERIAL_T5]
    for v in ("SIGAA_USUARIO", "SIGAA_SENHA"):
        if not os.environ.get(v):
            sys.exit(f"Defina a variável de ambiente {v}.")
    if args.local and Path(args.local).resolve().is_relative_to(RAIZ):
        sys.exit("--local precisa ficar fora do repositório (as capturas não estão borradas).")
    {"navegadores": coletar_navegadores, "telas": coletar_telas,
     "desempenho": coletar_desempenho}[args.rotina](args)


if __name__ == "__main__":
    main()
