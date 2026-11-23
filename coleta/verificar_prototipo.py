"""Verificação da ação de melhoria: M14 (e, com o motor do WAVE, M9) medidas no protótipo mobile.

Aplica ao protótipo (``docs/assets/prototipo-mobile/prototipo-interativo.html``) os mesmos
critérios usados no SIGAA, sem reescrevê-los:

- M14: o mesmo script de página ``JS_ADAPTACAO`` e os mesmos perfis de aparelho
  (``DISPOSITIVOS``) de ``sigaa_coleta.py``, e a mesma função ``criterios()`` de ``calcular.py``;
- M9 (opcional, ``--wave-js``): a mesma injeção do motor da extensão WAVE de ``coleta_wave.py``.

O protótipo é aberto em "modo tela cheia": o guia lateral, o título da página de demonstração,
a moldura do celular e a barra de status simulada (hora do aparelho) são escondidos, para que a
página medida seja só a interface proposta ocupando a tela do aparelho, como o SIGAA no celular.
Cada tarefa termina no estado em que o estudante veria a informação, alcançado por toques
(``tap``) nos mesmos controles que um usuário usaria. O registro de ``toque_menu`` e dos
``alvos_usados`` segue o formato de ``telas.jsonl``.

Saídas (o julgamento do SIGAA em ``metricas.csv`` não é alterado):
- ``dados/brutos/flexibilidade/automatizado/telas-prototipo.jsonl``;
- ``dados/brutos/flexibilidade/evidencias/prototipo/<tarefa>-<aparelho>.png``;
- ``dados/brutos/acessibilidade/wave/prototipo/`` (com ``--wave-js``);
- ``dados/consolidados/verificacao-prototipo.csv`` (antes e depois por métrica).

Uso: ``python coleta/verificar_prototipo.py [--wave-js caminho/wave.min.js] [--avaliador Nome]``
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import platform
import sys
from importlib import metadata
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
import calcular  # noqa: E402
import coleta_wave  # noqa: E402
import sigaa_coleta as sc  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
PROTOTIPO = RAIZ / "docs/assets/prototipo-mobile/prototipo-interativo.html"
SAIDA_TELAS = RAIZ / "dados/brutos/flexibilidade/automatizado/telas-prototipo.jsonl"
EVIDENCIAS = RAIZ / "dados/brutos/flexibilidade/evidencias/prototipo"
SAIDA_WAVE = RAIZ / "dados/brutos/acessibilidade/wave/prototipo"
CONSOLIDADO = RAIZ / "dados/consolidados/verificacao-prototipo.csv"
METRICAS_SIGAA = RAIZ / "dados/consolidados/metricas.csv"

# Modo tela cheia: só a interface proposta, sem os elementos da página de demonstração.
CSS_TELA_CHEIA = """
html, body { margin: 0 !important; padding: 0 !important; background: #f1f5f9 !important; }
body > h1, body > p.topo, .pm-guide, .pm-status { display: none !important; }
.pm-wrap { display: block !important; margin: 0 !important; }
.pm-phone { width: 100% !important; max-width: none !important; height: 100vh !important;
            border-radius: 0 !important; padding: 0 !important; box-shadow: none !important; }
.pm-screen { border-radius: 0 !important; }
/* Como numa página web de celular: a página inteira rola e a barra de abas fica fixa no rodapé
   (no simulador da GitPage, a rolagem é interna à moldura do celular). O detector de M14 trata
   camadas fixas como no SIGAA (aviso de cookies): o conteúdo que passa por trás delas não conta
   como sobreposição. */
.pm-phone, .pm-screen { height: auto !important; overflow: visible !important; }
.pm-body { overflow: visible !important; padding-bottom: 72px !important; }
.pm-nav { position: fixed !important; left: 0; right: 0; bottom: 0; z-index: 10; }
"""

# Estado final de cada tarefa: sequência de toques a partir da tela inicial.
# Cada passo é (seletor do controle, seletor que precisa ficar visível depois do toque).
TAREFAS = {
    "T1": [(".pm-nav [data-goto=turmas]", "#pm-tab-turmas"),
           (".pm-seg [data-subtab=notas]", "#pm-sub-notas")],
    "T2": [],  # horário e local por extenso na própria tela inicial (lista de turmas)
    "T3": [("#pm-tab-inicio [data-toast*='Atestado']", "#pm-toast.vis")],
    "T4": [(".pm-nav [data-goto=progresso]", "#pm-tab-progresso")],
    "T5": [(".pm-nav [data-goto=turmas]", "#pm-tab-turmas"),
           (".pm-seg [data-subtab=materiais]", "#pm-sub-materiais")],
    "T6": [(".pm-nav [data-goto=calendario]", "#pm-tab-calendario")],
}
PAGINAS = {
    "T1": "Turmas > Minhas Notas", "T2": "Início (turmas com horário por extenso)",
    "T3": "Início > Emitir Atestado", "T4": "Progresso (integralização)",
    "T5": "Turmas > Materiais", "T6": "Calendário 2026.2",
}


def abrir(pw, dispositivo: str):
    cfg = sc.DISPOSITIVOS[dispositivo]
    browser = pw.chromium.launch(channel="chrome")
    opts = {"viewport": cfg["viewport"], "locale": "pt-BR", "has_touch": cfg["toque"]}
    for k in ("device_scale_factor", "user_agent"):
        if k in cfg:
            opts[k] = cfg[k]
    if cfg.get("is_mobile"):
        opts["is_mobile"] = True
    ctx = browser.new_context(**opts)
    pg = ctx.new_page()
    pg.goto(PROTOTIPO.as_uri(), wait_until="load")
    pg.add_style_tag(content=CSS_TELA_CHEIA)
    pg.wait_for_timeout(300)
    return browser, pg


def executar(pg, tarefa: str) -> dict:
    """Leva o protótipo ao estado final da tarefa por toques e mede os alvos usados."""
    toque_ok, alvos = None, []
    for seletor, esperado in TAREFAS[tarefa]:
        alvo = pg.locator(seletor).first
        alvo.scroll_into_view_if_needed()
        escala = pg.evaluate("window.visualViewport ? visualViewport.scale : 1")
        caixa = alvo.bounding_box() or {"width": 0, "height": 0}
        alvos.append({"seletor": seletor, "largura_px": round(caixa["width"] * escala, 1),
                      "altura_px": round(caixa["height"] * escala, 1)})
        alvo.tap()
        try:
            pg.wait_for_selector(esperado, state="visible", timeout=3000)
            ok = True
        except Exception:  # noqa: BLE001
            ok = False
        toque_ok = ok if toque_ok is None else (toque_ok and ok)
    pg.wait_for_timeout(300)
    return {"toque_menu": toque_ok, "alvos_usados": alvos}


def base(pg, dispositivo: str, avaliador: str) -> dict:
    return {"data_hora": dt.datetime.now().isoformat(timespec="seconds"), "objeto": "prototipo",
            "arquivo": str(PROTOTIPO.relative_to(RAIZ)), "motor": "chromium",
            "navegador_versao": pg.context.browser.version, "dispositivo": dispositivo,
            "sistema": f"{platform.system()} {platform.release()}",
            "playwright": metadata.version("playwright"), "avaliador": avaliador,
            "modo": "tela cheia (sem guia, moldura e barra de status simuladas)"}


def medir_m14(pw, avaliador: str) -> list[dict]:
    regs = []
    EVIDENCIAS.mkdir(parents=True, exist_ok=True)
    for disp in ("celular_360", "tablet_768"):
        for t in TAREFAS:
            browser, pg = abrir(pw, disp)
            try:
                reg = {"tarefa": t, "pagina": PAGINAS[t], **executar(pg, t)}
                reg["adaptacao"] = pg.evaluate(sc.JS_ADAPTACAO)
                nome = EVIDENCIAS / f"{t}-{disp}.png"
                pg.screenshot(path=str(nome), full_page=True)
                reg["evidencia"] = str(nome.relative_to(RAIZ))
                reg = {**base(pg, disp, avaliador), **reg}
            finally:
                browser.close()
            regs.append(reg)
            c = calcular.criterios(reg, disp)
            print(disp, t, "".join(k if v else "-" for k, v in c.items()), flush=True)
    SAIDA_TELAS.parent.mkdir(parents=True, exist_ok=True)
    with SAIDA_TELAS.open("w", encoding="utf-8") as f:
        for r in regs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return regs


def medir_m9(pw, wave_js: Path, versao: str) -> list[dict]:
    SAIDA_WAVE.mkdir(parents=True, exist_ok=True)
    linhas = []
    for t in TAREFAS:
        browser, pg = abrir(pw, "celular_360")
        try:
            executar(pg, t)
            rel = coleta_wave.executar_wave_na_pagina(pg, wave_js)
        finally:
            browser.close()
        st = rel["statistics"]
        erros = int(st.get("error", 0)) + int(st.get("contrast", 0))
        (SAIDA_WAVE / f"{t}-wave.json").write_text(
            json.dumps({"tarefa": t, "pagina": PAGINAS[t], "ferramenta": f"WAVE Evaluation Tool {versao}",
                        "erros": erros, "wave": rel}, ensure_ascii=False, indent=2), encoding="utf-8")
        linhas.append({"tarefa": t, "pagina": PAGINAS[t], "erros": erros, "alertas": int(st.get("alert", 0))})
        print("WAVE", t, erros, flush=True)
    calcular.escrever(SAIDA_WAVE / "resumo.csv", linhas, ["tarefa", "pagina", "erros", "alertas"])
    return linhas


def valor_sigaa(metrica: str) -> str:
    for l in csv.DictReader(METRICAS_SIGAA.open(encoding="utf-8")):
        if l["metrica"] == metrica and l["recorte"] == "geral":
            return l["valor"]
    return ""


def consolidar(regs: list[dict], wave: list[dict] | None):
    linhas = []
    ok = [all(calcular.criterios(r, r["dispositivo"]).values()) for r in regs]
    a, b = sum(ok), len(ok)
    falhas = {}
    for r in regs:
        for k, v in calcular.criterios(r, r["dispositivo"]).items():
            if not v:
                falhas.setdefault(k, set()).add(f"{r['tarefa']}@{calcular.LARGURA[r['dispositivo']]}")
    obs = "; ".join(f"critério ({k}) falha em {len(v)} verificação(ões): {', '.join(sorted(v))}"
                    for k, v in sorted(falhas.items())) or "todos os critérios atendidos"
    linhas.append({"metrica": "M14", "recorte": "geral", "n": b, "valor_sigaa": valor_sigaa("M14"),
                   "valor_prototipo": f"{a / b:.4f}", "nivel_prototipo": calcular.nivel("M14", a / b),
                   "observacao": f"{a} de {b} verificações adaptadas; {obs}"})
    for crit in "abcde":
        n_ok = sum(1 for r in regs if calcular.criterios(r, r["dispositivo"])[crit])
        linhas.append({"metrica": "M14", "recorte": f"criterio_{crit}", "n": b, "valor_sigaa": "",
                       "valor_prototipo": f"{n_ok / b:.4f}", "nivel_prototipo": "",
                       "observacao": f"{n_ok} de {b} verificações atendem o critério ({crit})"})
    if wave:
        media = sum(l["erros"] for l in wave) / len(wave)
        linhas.append({"metrica": "M9", "recorte": "geral", "n": len(wave), "valor_sigaa": valor_sigaa("M9"),
                       "valor_prototipo": f"{media:.4f}", "nivel_prototipo": calcular.nivel("M9", media),
                       "observacao": f"{sum(l['erros'] for l in wave)} erros (Errors + Contrast Errors) em {len(wave)} estados"})
    calcular.escrever(CONSOLIDADO, linhas, ["metrica", "recorte", "n", "valor_sigaa", "valor_prototipo",
                                           "nivel_prototipo", "observacao"])
    for l in linhas:
        print(l)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wave-js", help="caminho local do wave.min.js (sem ele, só M14 é medida)")
    ap.add_argument("--wave-versao", default="3.3.4.0")
    ap.add_argument("--avaliador", default="Caio")
    args = ap.parse_args()
    with sync_playwright() as pw:
        regs = medir_m14(pw, args.avaliador)
        wave = medir_m9(pw, Path(args.wave_js).expanduser().resolve(), args.wave_versao) if args.wave_js else None
    consolidar(regs, wave)


if __name__ == "__main__":
    main()
