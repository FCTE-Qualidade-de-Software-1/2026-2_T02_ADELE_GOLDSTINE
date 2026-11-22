"""Inspeção automatizada no SIGAA/UnB: primeiro avaliador de M10 e M20 e evidências de M1.

Reaproveita o login e a navegação de ``sigaa_coleta.py`` (mesma conta, só consultas,
nenhum formulário é enviado) e grava um registro JSON por verificação em
``dados/brutos/inspecao/automatizado/``, com capturas borradas em
``dados/brutos/inspecao/evidencias/``. O segundo avaliador confere manualmente.

    python coleta/inspecao_coleta.py menus   # itens dos menus do portal (M1 e C5 de M20)
    python coleta/inspecao_coleta.py m10     # critérios (a) a (d) de M10 nas páginas de T1 a T6
    python coleta/inspecao_coleta.py m20     # cenários C1 a C6 de M20

Regras de decisão do script (fichas em docs/fase-2/metricas.md):

- M10 (a): cada controle do caminho da tarefa é alcançado com Tab e acionado com Enter
  (ou Espaço); T2 não aciona controles (a informação está na página inicial).
- M10 (b): todo elemento que recebe o foco por Tab na página final muda de aparência
  (contorno, sombra, borda, fundo, cor ou sublinhado) e tem área visível.
- M10 (c): zoom de 200% reproduzido com a janela de 1366 x 768 reduzida à metade em px CSS
  (683 x 384, densidade 2); atende se a página final mostra o conteúdo da tarefa sem
  texto sobreposto, coberto ou cortado (mesma verificação do critério (c) de M14).
  Rolagem horizontal é permitida pelo critério 1.4.4 da WCAG.
- M10 (d): cada controle do caminho é exposto na árvore de acessibilidade com papel de
  controle (link, botão, item de menu...) e nome não vazio.
- M20: tratado se o sistema previne o erro ou mostra mensagem com a causa e como
  continuar, sem obrigar a recomeçar a tarefa desde o login.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

import sigaa_coleta as sc

SAIDA = sc.RAIZ / "dados/brutos/inspecao/automatizado"
EVID = sc.RAIZ / "dados/brutos/inspecao/evidencias"

sc.DISPOSITIVOS["zoom_200"] = {"viewport": {"width": 683, "height": 384}, "toque": False,
                               "device_scale_factor": 2}

PAPEIS_CONTROLE = {"link", "button", "menuitem", "menuitemcheckbox", "menuitemradio", "tab",
                   "checkbox", "radio", "combobox", "textbox", "option", "treeitem", "switch"}

# Mensagens do próprio sistema (sem dados do estudante) que podem ser registradas
SELETOR_MENSAGENS = "#painel-erros ul.erros li, #painel-erros ul.warning li, #painel-erros ul.info li"

JS_ATIVO = """() => { const e = document.activeElement;
  if (!e || e === document.body || e === document.documentElement) return null;
  const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
  return {tag: e.tagName.toLowerCase(), id: e.id || null,
          tem_href: e.hasAttribute('href'),
          area: (r.right < 0 || r.bottom < 0 || r.left > document.documentElement.scrollWidth) ? 0 : Math.round(r.width * r.height),
          fora_da_tela: r.right < 0 || r.bottom < 0 || r.left > document.documentElement.scrollWidth,
          estilo: [s.outlineStyle, s.outlineWidth, s.outlineColor, s.boxShadow, s.borderColor,
                   s.backgroundColor, s.color, s.textDecorationLine].join('|')}; }"""

JS_ESTILO_SEM_FOCO = """() => { const e = document.activeElement; if (!e) return null;
  if (e.tagName === 'IFRAME') return 'iframe';
  e.blur(); const s = getComputedStyle(e);
  const v = [s.outlineStyle, s.outlineWidth, s.outlineColor, s.boxShadow, s.borderColor,
             s.backgroundColor, s.color, s.textDecorationLine].join('|');
  e.focus(); return v; }"""


def gravar(nome: str, reg: dict):
    sc.gravar(SAIDA / f"{nome}.jsonl", {"data_hora": time.strftime("%Y-%m-%dT%H:%M:%S"), **reg})


def mensagens(pg) -> list[str]:
    try:
        return [t.strip()[:200] for t in pg.locator(SELETOR_MENSAGENS).all_inner_texts() if t.strip()][:5]
    except Exception:  # noqa: BLE001
        return []


def esperar_nav(pg, acao, timeout=60000) -> bool:
    try:
        with pg.expect_navigation(wait_until="load", timeout=timeout):
            acao()
        sc.esperar(pg)
        return True
    except Exception:  # noqa: BLE001
        return False


# --------------------------------------------------------------------------
# Caminhos das tarefas: (rótulo, locator, efeito esperado do acionamento)
# --------------------------------------------------------------------------

def loc_ensino(pg):
    return pg.locator("td[class^='ThemeOfficeMainItem']:has-text('Ensino')").first


def loc_item(pg, item):
    return pg.locator(f"tr[class^='ThemeOfficeMenuItem']:has(td.ThemeOfficeMenuItemText:text-is('{item}'))").first


def caminho(pg, tarefa):
    lupa = pg.locator(f"thead:has-text('Calendário {sc.SEMESTRE}') + tbody a[title='Visualizar Calendário Acadêmico']").first
    menu = {"T1": "Consultar Minhas Notas", "T3": "Emitir Atestado de Matrícula",
            "T4": "Consultar Índices Acadêmicos", "T6": "Calendário Acadêmico"}
    if tarefa in menu:
        passos = [("menu Ensino", lambda: loc_ensino(pg), "submenu", menu[tarefa]),
                  (f"item {menu[tarefa]}", lambda: loc_item(pg, menu[tarefa]), "navegacao", None)]
        if tarefa == "T6":
            passos.append((f"lupa do calendário {sc.SEMESTRE}", lambda: lupa, "navegacao", None))
        return passos
    if tarefa == "T5":
        return [("link da turma", lambda: pg.locator(f"a:text-is('{sc.TURMA_T5}')").first, "navegacao", None),
                (f"material {sc.MATERIAL_T5}", lambda: pg.locator(f"#formAva a:text-is('{sc.MATERIAL_T5}')").first, "download", None)]
    return []  # T2: leitura da página inicial, sem controle acionado


def focado(loc) -> bool:
    try:
        return loc.evaluate("e => { const a = document.activeElement; return !!a && a !== document.body && (a === e || e.contains(a) || a.contains(e)); }", timeout=2000)
    except Exception:  # noqa: BLE001
        return False


def tab_ate(pg, loc, maximo=350, prazo_s=90) -> int | None:
    pg.evaluate("() => { document.activeElement && document.activeElement.blur(); window.scrollTo(0, 0); }")
    fim = time.time() + prazo_s
    for i in range(1, maximo + 1):
        pg.keyboard.press("Tab")
        if focado(loc):
            return i
        if time.time() > fim:
            return None
    return None


def efeito_ok(pg, efeito, proximo) -> bool:
    if efeito == "submenu":
        try:
            pg.locator(f"td.ThemeOfficeMenuItemText:text-is('{proximo}')").first.wait_for(state="visible", timeout=2500)
            return True
        except Exception:  # noqa: BLE001
            return False
    if efeito == "submenu_t5":
        try:
            pg.locator(f"#formAva a:text-is('{sc.MATERIAL_T5}')").first.wait_for(state="visible", timeout=2500)
            return True
        except Exception:  # noqa: BLE001
            return False
    return False


def acionar_teclado(pg, efeito, proximo) -> bool:
    url = pg.url
    for tecla in ("Enter", " "):
        if efeito == "download":
            try:
                with pg.expect_download(timeout=20000) as d:
                    pg.keyboard.press(tecla)
                d.value.delete()
                return True
            except Exception:  # noqa: BLE001
                continue
        if efeito == "navegacao":
            ok = esperar_nav(pg, lambda: pg.keyboard.press(tecla), timeout=20000)
            if ok or pg.url != url:
                return True
            continue
        pg.keyboard.press(tecla)
        if efeito_ok(pg, efeito, proximo):
            return True
    return False


def acionar_mouse(s, pg, rotulo, loc, efeito):
    if rotulo == "menu Ensino":
        loc.hover()
        pg.wait_for_timeout(700)
    elif efeito == "download":
        with pg.expect_download(timeout=60000) as d:
            loc.click()
        d.value.delete()
    elif efeito == "navegacao":
        esperar_nav(pg, lambda: loc.click())
    else:
        loc.click()
        pg.wait_for_timeout(1500)


def nome_acessivel(loc) -> dict:
    try:
        snap = loc.aria_snapshot(timeout=5000).strip().splitlines()[0]
    except Exception as e:  # noqa: BLE001
        return {"aria": None, "papel": None, "nome": None, "erro": type(e).__name__}
    m = re.match(r'-\s*([a-z]+)(?:\s+"([^"]*)")?', snap)
    papel, nome = (m.group(1), (m.group(2) or "").strip()) if m else (None, None)
    return {"aria": snap[:160], "papel": papel, "nome": nome}


def foco_visivel(pg, maximo=300) -> dict:
    pg.evaluate("() => { document.activeElement && document.activeElement.blur(); window.scrollTo(0, 0); }")
    vistos, invisiveis, exemplos, primeiro = 0, 0, [], None
    for _ in range(maximo):
        pg.keyboard.press("Tab")
        a = pg.evaluate(JS_ATIVO)
        if a is None:
            if vistos:
                break
            continue
        chave = (a["tag"], a["id"], a["estilo"])
        if primeiro is None:
            primeiro = chave
        elif chave == primeiro and vistos > 3:
            break
        sem = pg.evaluate(JS_ESTILO_SEM_FOCO)
        vistos += 1
        if a["area"] == 0 or sem == a["estilo"] or sem == "iframe":
            invisiveis += 1
            if len(exemplos) < 5:
                exemplos.append({"tag": a["tag"], "id": a["id"], "area": a["area"], "fora_da_tela": a.get("fora_da_tela")})
    return {"focados": vistos, "sem_indicador": invisiveis, "exemplos": exemplos}


# --------------------------------------------------------------------------
# Rotinas
# --------------------------------------------------------------------------

def rotina_menus(args):
    with sync_playwright() as pw:
        s = sc.Sessao(pw, "chromium", "computador")
        try:
            s.login()
            pg = s.pg
            itens = pg.evaluate("""() => {
              const out = [];
              for (const t of document.querySelectorAll('td.ThemeOfficeMainItem, td[class^=ThemeOfficeMainItem] , td.ThemeOfficeMenuItemText'))
                out.push({nivel: t.className.includes('Main') ? 'principal' : 'item', texto: t.textContent.trim()});
              return out; }""")
            sessao = re.findall(r"[Ss]ess[ãa]o[^\n]{0,40}", pg.locator("body").inner_text())[:5]
            pg.wait_for_timeout(65000)
            sessao += re.findall(r"[Ss]ess[ãa]o[^\n]{0,40}", pg.locator("body").inner_text())[:5]
            gravar("menus", {"itens_menu": itens, "texto_sessao": sessao,
                             "versao": pg.evaluate(sc.JS_ASSINATURA).get("versao")})
            print(json.dumps({"itens_menu": [i["texto"] for i in itens], "texto_sessao": sessao}, ensure_ascii=False))
        finally:
            s.fechar()


def rotina_m10(args):
    with sync_playwright() as pw:
        # (a), (b) e (d): janela de computador, sem zoom
        s = sc.Sessao(pw, "chromium", "computador")
        try:
            s.login()
            pg = s.pg
            for t in args.tarefas:
                s.ir_home()
                passos, nomes = [], []
                lista = caminho(pg, t)
                for i, (rotulo, fn, efeito, proximo) in enumerate(lista):
                    loc = fn()
                    if loc.count() == 0:
                        passos.append({"controle": rotulo, "tabs_ate_foco": None, "acionado_teclado": False,
                                       "erro": "controle não encontrado na página"})
                        print("  ", t, rotulo, "NÃO ENCONTRADO", pg.url[:80], flush=True)
                        break
                    nomes.append({"controle": rotulo, **nome_acessivel(loc)})
                    tabs = tab_ate(pg, loc)
                    print("  ", t, rotulo, "tabs:", tabs, flush=True)
                    ok = tabs is not None and acionar_teclado(pg, efeito, proximo)
                    print("  ", t, rotulo, "teclado:", ok, flush=True)
                    passos.append({"controle": rotulo, "tabs_ate_foco": tabs, "acionado_teclado": ok})
                    if not ok:  # segue pelo mouse para verificar os passos seguintes
                        try:
                            acionar_mouse(s, pg, rotulo, loc, efeito)
                        except Exception as e:  # noqa: BLE001
                            passos[-1]["erro_mouse"] = type(e).__name__
                if t == "T5":  # página final para (b): Turma Virtual com o menu Materiais aberto
                    pass
                texto = pg.locator("body").inner_text().lower()
                final_ok = all(m.lower() in texto for m in sc.MARCADORES[t] if m != sc.MATERIAL_T5)
                fv = foco_visivel(pg)
                a_ok = all(p["acionado_teclado"] for p in passos)
                d_ok = all(n["papel"] in PAPEIS_CONTROLE and n["nome"] for n in nomes)
                evid = sc.capturar(pg, EVID / "m10", None, f"{t}-m10-teclado")
                reg = {"tarefa": t, "pagina": sc.PAGINAS[t], "pagina_final_ok": final_ok,
                       "a": {"atende": a_ok, "passos": passos,
                             "obs": None if lista else "tarefa sem controle acionado (leitura da página inicial)"},
                       "b": {"atende": fv["sem_indicador"] == 0 and fv["focados"] > 0, **fv},
                       "d": {"atende": d_ok, "controles": nomes,
                             "obs": None if lista else "tarefa sem controle acionado"},
                       "navegador": f"Chromium {s.versao}", "evidencia": evid}
                gravar("m10", reg)
                print(t, "a", a_ok, "b", reg["b"]["atende"], fv["sem_indicador"], "/", fv["focados"], "d", d_ok, flush=True)
        finally:
            s.fechar()
        # (c): zoom de 200%
        s = sc.Sessao(pw, "chromium", "zoom_200")
        try:
            s.login()
            for t in args.tarefas:
                reg = sc.executar_com_repeticao(s, t)
                ad = s.pg.evaluate(sc.JS_ADAPTACAO) if not reg.get("erro") else {}
                perda = (ad.get("textos_sobrepostos", 1) + ad.get("textos_cobertos", 1) + ad.get("textos_cortados", 1))
                ok = bool(reg.get("marcadores_ok")) and perda == 0
                evid = sc.capturar(s.pg, EVID / "m10", None, f"{t}-m10-zoom200")
                gravar("m10", {"tarefa": t, "pagina": sc.PAGINAS[t],
                               "c": {"atende": ok, "conteudo_da_tarefa": reg.get("marcadores_ok"),
                                     "rolagem_horizontal": ad.get("largura_conteudo_px", 0) > ad.get("largura_layout_px", 0),
                                     **{k: ad.get(k) for k in ("largura_layout_px", "largura_conteudo_px", "textos_sobrepostos",
                                                               "textos_cobertos", "textos_cortados", "exemplos_c")},
                                     "erro": reg.get("erro")},
                               "navegador": f"Chromium {s.versao}", "evidencia": evid})
                print(t, "c", ok, perda, flush=True)
        finally:
            s.fechar()


def estado(pg, tarefa=None) -> dict:
    texto = ""
    try:
        texto = pg.locator("body").inner_text(timeout=10000).lower()
    except Exception:  # noqa: BLE001
        pass
    r = {"url": pg.url.split("?")[0][:120], "titulo": (pg.title() or "")[:80], "mensagens": mensagens(pg),
         "portal_ok": pg.locator("td.ThemeOfficeMainItem").count() > 0,
         "pagina_login": "autenticacao.unb.br" in pg.url or "login" in pg.url.lower(),
         "erro_navegador": pg.url.startswith("chrome-error") or "err_cache_miss" in texto or "document expired" in texto}
    if tarefa:
        r["marcadores_tarefa"] = all(m.lower() in texto for m in sc.MARCADORES[tarefa])
    for padrao in ("expirad", "sessão", "voltar", "comportamento inesperado", "não é possível", "período", "prazo", "operação"):
        if padrao in texto and padrao not in ("sessão",):
            r.setdefault("termos", []).append(padrao)
    return r


def rotina_m20(args):
    def item(s, nome):
        s.alvos_usados = []
        return esperar_nav(s.pg, lambda: s.menu_ensino(nome))
    with sync_playwright() as pw:
        s = sc.Sessao(pw, "chromium", "computador")
        pg = s.pg
        try:
            s.login()
            s.alvos_usados = []
            res = {}

            # C2 - botão Voltar do navegador (T1): notas -> Voltar -> continuar a tarefa
            s.ir_home(); item(s, "Consultar Minhas Notas")
            antes = estado(pg, "T1")
            try:
                pg.go_back(wait_until="load", timeout=30000)
            except Exception as e:  # noqa: BLE001
                antes["erro_voltar"] = str(e)[:120]
            depois = estado(pg)
            ev = sc.capturar(pg, EVID / "m20", None, "C2-voltar")
            sc.MENU_PERMITIDO.add("Consultar Minhas Notas")
            continuar = False
            try:
                if pg.locator("td.ThemeOfficeMainItem").count():
                    continuar = item(s, "Consultar Índices Acadêmicos") and estado(pg, "T4")["marcadores_tarefa"]
            except Exception:  # noqa: BLE001
                pass
            res["C2"] = {"tarefa": "T1", "antes": antes, "apos_voltar": depois, "continuou_sem_login": continuar, "evidencia": ev}

            # C3 - recarregar a página depois de uma ação (T3)
            s.ir_home(); item(s, "Emitir Atestado de Matrícula")
            a = estado(pg, "T3")
            dialogo = []
            pg.once("dialog", lambda d: (dialogo.append(d.message[:120]), d.accept()))
            try:
                pg.reload(wait_until="load", timeout=60000); sc.esperar(pg)
            except Exception as e:  # noqa: BLE001
                a["erro_recarregar"] = str(e)[:120]
            res["C3"] = {"tarefa": "T3", "antes": a, "apos_recarregar": estado(pg, "T3"), "dialogo": dialogo,
                         "evidencia": sc.capturar(pg, EVID / "m20", None, "C3-recarregar")}

            # C4 - função aberta em nova aba (T4 numa aba, T1 na outra, depois volta à primeira)
            s.ir_home()
            href = loc_item(pg, "Consultar Índices Acadêmicos").evaluate("e => (e.querySelector('a') || e).getAttribute('href')")
            b = s.ctx.new_page()
            b.goto(s.home, wait_until="load", timeout=120000); sc.esperar(b)
            s2 = s.__class__.__new__(s.__class__); s2.__dict__.update(s.__dict__); s2.pg = b; s2.alvos_usados = []
            ok_b = esperar_nav(b, lambda: s2.menu_ensino("Consultar Índices Acadêmicos")) and estado(b, "T4")["marcadores_tarefa"]
            ev_b = sc.capturar(b, EVID / "m20", None, "C4-aba-nova")
            s.alvos_usados = []
            ok_a = esperar_nav(pg, lambda: s.menu_ensino("Consultar Minhas Notas")) and estado(pg, "T1")["marcadores_tarefa"]
            res["C4"] = {"tarefa": "T4", "item_menu_tem_href": bool(href and href not in ("#", "javascript:void(0)")),
                         "aba_nova_ok": ok_b, "aba_original_ok": ok_a, "estado_aba_original": estado(pg),
                         "evidencia": [ev_b, sc.capturar(pg, EVID / "m20", None, "C4-aba-original")]}
            b.close()

            # C6 - documento em PDF: como o SIGAA abre o atestado e o histórico (janela nova ou não)
            s.ir_home()
            janelas = []
            s.ctx.on("page", lambda p: janelas.append(p))
            downloads = []
            pg.on("download", lambda d: downloads.append(d.suggested_filename[-4:]))
            item(s, "Emitir Atestado de Matrícula")
            res["C6"] = {"tarefa": "T3", "janela_nova": len(janelas), "download": downloads[:],
                         "mesma_pagina": estado(pg, "T3"), "evidencia": sc.capturar(pg, EVID / "m20", None, "C6-atestado")}

            # C5 - função fora do período do calendário (Trancar; prazo de trancamento já encerrado).
            # Só abre a página; nenhum formulário é enviado.
            s.ir_home()
            sc.MENU_PERMITIDO.add("Trancar")
            dialogos = []
            pg.on("dialog", lambda d: (dialogos.append(d.message[:160]), d.dismiss()))
            esperar_nav(pg, lambda: s.menu_ensino("Trancar"))
            res["C5"] = {"tarefa": "T6", "funcao": "Ensino > Trancar", "estado": estado(pg), "dialogos": dialogos,
                         "evidencia": sc.capturar(pg, EVID / "m20", None, "C5-fora-do-periodo")}

            # C1 - sessão expirada (simulada removendo o cookie de sessão do SIGAA) em T1
            s.ir_home()
            cookies = s.ctx.cookies()
            sessao = [c for c in cookies if c["name"].upper().startswith("JSESSIONID") and "sig" in c["domain"]]
            s.ctx.clear_cookies(name=re.compile(r"JSESSIONID", re.I))
            s.alvos_usados = []
            try:
                esperar_nav(pg, lambda: s.menu_ensino("Consultar Minhas Notas"))
            except Exception as e:  # noqa: BLE001
                res.setdefault("C1", {})["erro"] = str(e)[:120]
            c1 = estado(pg, "T1")
            res["C1"] = {**res.get("C1", {}), "tarefa": "T1", "simulacao": "cookie JSESSIONID removido",
                         "cookies_removidos": len(sessao), "apos_acao": c1,
                         "evidencia": sc.capturar(pg, EVID / "m20", None, "C1-sessao")}
            if c1["pagina_login"] and pg.locator("input[name=username]").count():
                pg.fill("input[name=username]", os.environ["SIGAA_USUARIO"])
                pg.fill("input[name=password]", os.environ["SIGAA_SENHA"])
                esperar_nav(pg, lambda: pg.click("button[name=submit]"))
                res["C1"]["apos_novo_login"] = estado(pg, "T1")

            for c, r in res.items():
                gravar("m20", {"cenario": c, **r, "navegador": f"Chromium {s.versao}"})
                print(c, json.dumps(r, ensure_ascii=False)[:600], flush=True)
        finally:
            s.fechar()


def rotina_c1_real(args):
    """C1 com expiração real: abre o portal, fica parado o tempo da sessão e tenta seguir a tarefa."""
    with sync_playwright() as pw:
        s = sc.Sessao(pw, "chromium", "computador")
        pg = s.pg
        try:
            s.login()
            contador = re.findall(r"Sess[ãa]o:\s*([0-9:]+)", pg.locator("body").inner_text())
            pg.wait_for_timeout(args.espera_min * 60000)
            antes = estado(pg)
            s.alvos_usados = []
            esperar_nav(pg, lambda: s.menu_ensino("Consultar Minhas Notas"))
            reg = {"cenario": "C1", "tarefa": "T1", "simulacao": f"expiração real: {args.espera_min} min parado",
                   "contador_inicial": contador[:1], "antes_da_acao": antes, "apos_acao": estado(pg, "T1"),
                   "evidencia": sc.capturar(pg, EVID / "m20", None, "C1-sessao-real")}
            if reg["apos_acao"]["pagina_login"] and pg.locator("input[name=username]").count():
                pg.fill("input[name=username]", os.environ["SIGAA_USUARIO"])
                pg.fill("input[name=password]", os.environ["SIGAA_SENHA"])
                esperar_nav(pg, lambda: pg.click("button[name=submit]"))
                reg["apos_novo_login"] = estado(pg, "T1")
            gravar("m20", {**reg, "navegador": f"Chromium {s.versao}"})
            print(json.dumps(reg, ensure_ascii=False), flush=True)
        finally:
            s.fechar()


def rotina_documentos(args):
    """Guarda, FORA do repositório, o texto das páginas e o histórico em PDF usados em M1 e M2.

    Só consultas. Os valores (notas, índices) ficam na pasta local do avaliador; no repositório
    entram apenas os resultados das verificações (coincide ou diverge).
    """
    local = Path(os.path.expanduser(args.local or "~/sigaa-originais/inspecao"))
    if sc.RAIZ in local.resolve().parents:
        raise SystemExit("A pasta local precisa ficar fora do repositório.")
    local.mkdir(parents=True, exist_ok=True)
    for i in ("Emitir Histórico", "Consultar Estrutura Curricular", "Meu Plano de Matrículas"):
        sc.MENU_PERMITIDO.add(i)
    salvar = lambda nome, pg: (local / f"{nome}.txt").write_text(pg.locator("body").inner_text(), encoding="utf-8")  # noqa: E731
    with sync_playwright() as pw:
        s = sc.Sessao(pw, "chromium", "computador")
        pg = s.pg
        try:
            s.login()
            s.alvos_usados = []
            salvar("portal", pg)
            turmas = pg.evaluate("""() => { const t = [...document.querySelectorAll('table')].find(x => /Hor[áa]rio/.test(x.innerText) && x.querySelector('a'));
              return t ? [...new Set([...t.querySelectorAll('a')].map(a => a.innerText.trim()).filter(x => x.length > 6))] : []; }""")
            for nome, item in (("notas", "Consultar Minhas Notas"), ("indices", "Consultar Índices Acadêmicos"),
                               ("estrutura", "Consultar Estrutura Curricular"), ("plano", "Meu Plano de Matrículas")):
                s.ir_home(); s.alvos_usados = []
                esperar_nav(pg, lambda: s.menu_ensino(item)); salvar(nome, pg); print(nome, pg.url[:80], flush=True)
            s.ir_home(); s.alvos_usados = []
            try:
                with pg.expect_download(timeout=120000) as d:
                    s.menu_ensino("Emitir Histórico")
                d.value.save_as(str(local / "historico.pdf")); print("historico.pdf", flush=True)
            except Exception as e:  # noqa: BLE001
                sc.esperar(pg); salvar("historico_pagina", pg); print("histórico sem download:", type(e).__name__, pg.url[:80], flush=True)
            s.ir_home(); s.alvos_usados = []
            esperar_nav(pg, lambda: s.menu_ensino("Calendário Acadêmico"))
            lupa = pg.locator(f"thead:has-text('Calendário {sc.SEMESTRE}') + tbody a[title='Visualizar Calendário Acadêmico']").first
            esperar_nav(pg, lambda: lupa.click()); salvar("calendario", pg)
            for i, t in enumerate(turmas):
                s.ir_home()
                esperar_nav(pg, lambda: pg.locator(f"a:text-is('{t}')").first.click())
                salvar(f"turma_virtual_{i + 1}", pg)
            (local / "turmas.json").write_text(json.dumps(turmas, ensure_ascii=False), encoding="utf-8")
            print("turmas:", len(turmas), flush=True)
        finally:
            s.fechar()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("rotina", choices=["menus", "m10", "m20", "c1-real", "documentos"])
    ap.add_argument("--tarefas", nargs="+", default=["T1", "T2", "T3", "T4", "T5", "T6"])
    ap.add_argument("--local", help="pasta fora do repositório (rotina documentos)")
    ap.add_argument("--espera-min", type=int, default=42)
    ap.add_argument("--turma-t5", default=sc.TURMA_T5)
    ap.add_argument("--material-t5", default=sc.MATERIAL_T5)
    args = ap.parse_args()
    sc.TURMA_T5, sc.MATERIAL_T5 = args.turma_t5, args.material_t5
    sc.MARCADORES["T5"] = ["Turma Virtual", sc.MATERIAL_T5]
    for v in ("SIGAA_USUARIO", "SIGAA_SENHA"):
        if not os.environ.get(v):
            raise SystemExit(f"Defina {v}.")
    {"menus": rotina_menus, "m10": rotina_m10, "m20": rotina_m20, "c1-real": rotina_c1_real, "documentos": rotina_documentos}[args.rotina](args)


if __name__ == "__main__":
    main()
