"""Matriz multiplataforma: T1 a T6 em 20 perfis de sistema, aparelho e navegador.

Amplia M13 (4 navegadores de computador) e M14 (emulação de 360 e 768 px no
Chrome) para uma matriz de computador (Windows, macOS e Linux), celular
(Android e iOS) e tablet (iPadOS e Android), com sete navegadores: Google
Chrome, Chromium, Microsoft Edge, Brave, Opera, Mozilla Firefox e Safari
(motor WebKit). O Vivaldi foi testado, mas trava sob automação. Reaproveita a sessão, as tarefas e as medidas de
``sigaa_coleta.py``; os resultados são dado complementar de Flexibilidade
(não substituem M13 e M14 do julgamento, definidos antes da coleta).

O que a emulação reproduz e o que não reproduz (detalhes na GitPage, em
Fase 4 > Matriz multiplataforma):

- reproduz o motor de renderização real de cada navegador, a largura da tela,
  a densidade de pixels, o toque, o modo móvel (``is_mobile``, que ativa a
  viewport de 980 px das páginas sem ``<meta viewport>``) e o user agent;
- não reproduz o sistema operacional em si (fontes, barra de rolagem, teclado
  virtual), nem o desempenho do aparelho. O "Windows" e o "macOS" dos perfis
  são o navegador real rodando no Linux com o user agent e a tela típicos
  daquele sistema.

Navegadores fora do Playwright (Edge, Brave, Opera, Vivaldi) são extraídos dos
pacotes oficiais, sem instalação no sistema; os caminhos vêm das variáveis
SIGAA_EDGE, SIGAA_BRAVE, SIGAA_OPERA e SIGAA_VIVALDI ou, por padrão, de
``~/.cache/sigaa-navegadores/`` (ver coleta/README.md). Um perfil cujo
navegador não existe é registrado como indisponível e pulado.

Uso (credenciais em SIGAA_USUARIO e SIGAA_SENHA, como em sigaa_coleta.py):

    python coleta/matriz_dispositivos.py                 # todos os perfis
    python coleta/matriz_dispositivos.py --perfis ios-iphone15 win-edge
    python coleta/matriz_dispositivos.py --listar
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sigaa_coleta as sc  # noqa: E402

SAIDA = sc.RAIZ / "dados/brutos/flexibilidade/automatizado/matriz.jsonl"
EVID = sc.RAIZ / "dados/brutos/flexibilidade/evidencias/matriz"
BASE = Path(os.path.expanduser("~/.cache/sigaa-navegadores"))

EXECUTAVEIS = {  # navegadores baseados no Chromium fora do Playwright
    "edge": os.environ.get("SIGAA_EDGE", str(BASE / "edge/opt/microsoft/msedge/msedge")),
    "brave": os.environ.get("SIGAA_BRAVE", str(BASE / "brave/brave")),
    "opera": os.environ.get("SIGAA_OPERA", str(BASE / "opera/usr/lib/x86_64-linux-gnu/opera-stable/opera")),
    "vivaldi": os.environ.get("SIGAA_VIVALDI", str(BASE / "vivaldi/opt/vivaldi/vivaldi-bin")),
}
ARGS_SEM_ASSISTENTE = ["--no-first-run", "--no-default-browser-check"]

# navegador: (rótulo, motor do Playwright, canal, executável)
NAVEGADORES = {
    "chrome": ("Google Chrome", "chromium", "chrome", None),
    "chromium": ("Chromium", "chromium", None, None),
    "edge": ("Microsoft Edge", "chromium", None, "edge"),
    "brave": ("Brave", "chromium", None, "brave"),
    "opera": ("Opera", "chromium", None, "opera"),
    "vivaldi": ("Vivaldi", "chromium", None, "vivaldi"),
    "firefox": ("Mozilla Firefox", "firefox", None, None),
    "safari": ("Safari (WebKit)", "webkit", None, None),
}

# User agents de computador. {v} recebe a versão principal do navegador em execução.
_CHR = "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{v}.0.0.0 Safari/537.36"
UA = {
    "win": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " + _CHR,
    "mac": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " + _CHR,
    "linux": "Mozilla/5.0 (X11; Linux x86_64) " + _CHR,
    "win-ff": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{v}.0) Gecko/20100101 Firefox/{v}.0",
    "linux-ff": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{v}.0) Gecko/20100101 Firefox/{v}.0",
    "mac-safari": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
                   "(KHTML, like Gecko) Version/18.5 Safari/605.1.15"),
}
SUFIXO = {"edge": " Edg/{v}.0.0.0", "opera": " OPR/{v}.0.0.0"}


def computador(largura, altura, ua, dsf=1):
    return {"viewport": {"width": largura, "height": altura}, "toque": False,
            "device_scale_factor": dsf, "user_agent": ua}


def aparelho(nome, sufixo=""):
    """Perfil a partir do catálogo de dispositivos do Playwright (tela, densidade, UA)."""
    return {"_descritor": nome, "_sufixo": sufixo}


# id: (categoria, sistema, aparelho, navegador, perfil)
PERFIS = {
    # Computador
    "win-chrome": ("Computador", "Windows 11", "Notebook 1366×768", "chrome", computador(1366, 768, UA["win"])),
    "win-edge": ("Computador", "Windows 11", "Notebook 1366×768", "edge", computador(1366, 768, UA["win"] + SUFIXO["edge"])),
    "win-firefox": ("Computador", "Windows 11", "Notebook 1366×768", "firefox", computador(1366, 768, UA["win-ff"])),
    "win-opera": ("Computador", "Windows 11", "Notebook 1366×768", "opera", computador(1366, 768, UA["win"] + SUFIXO["opera"])),
    "win-brave": ("Computador", "Windows 11", "Notebook 1366×768", "brave", computador(1366, 768, UA["win"])),
    "mac-safari": ("Computador", "macOS", "MacBook Air 1440×900", "safari", computador(1440, 900, UA["mac-safari"], 2)),
    "mac-chrome": ("Computador", "macOS", "MacBook Air 1440×900", "chrome", computador(1440, 900, UA["mac"], 2)),
    "linux-chromium": ("Computador", "Linux (Ubuntu)", "Monitor 1920×1080", "chromium", computador(1920, 1080, UA["linux"])),
    "linux-firefox": ("Computador", "Linux (Ubuntu)", "Monitor 1920×1080", "firefox", computador(1920, 1080, UA["linux-ff"])),
    "linux-chrome": ("Computador", "Linux (Ubuntu)", "Monitor 1920×1080", "chrome", computador(1920, 1080, UA["linux"])),
    # O Vivaldi 8.3 abre manualmente, mas trava sob automação (antes de carregar qualquer página);
    # por isso fica fora da matriz; o executável segue configurável em SIGAA_VIVALDI para testes.
    # Celular
    "android-s24": ("Celular", "Android 14", "Galaxy S24 (360 px)", "chrome", aparelho("Galaxy S24")),
    "android-pixel7": ("Celular", "Android 14", "Pixel 7 (412 px)", "chrome", aparelho("Pixel 7")),
    "android-a55-edge": ("Celular", "Android 14", "Galaxy A55 (480 px)", "edge", aparelho("Galaxy A55", " EdgA/{v}.0.0.0")),
    "android-motog4-opera": ("Celular", "Android 7", "Moto G4 (360 px)", "opera", aparelho("Moto G4", " OPR/{v}.0.0.0")),
    "ios-iphonese": ("Celular", "iOS 18", "iPhone SE 3ª geração (375 px)", "safari", aparelho("iPhone SE (3rd gen)")),
    "ios-iphone15": ("Celular", "iOS 17", "iPhone 15 (393 px)", "safari", aparelho("iPhone 15")),
    "ios-iphone15promax": ("Celular", "iOS 17", "iPhone 15 Pro Max (430 px)", "safari", aparelho("iPhone 15 Pro Max")),
    # Tablet
    "android-tabs9": ("Tablet", "Android 14", "Galaxy Tab S9 (640 px)", "chrome", aparelho("Galaxy Tab S9")),
    "ipados-ipadmini": ("Tablet", "iPadOS", "iPad Mini (768 px)", "safari", aparelho("iPad Mini")),
    "ipados-ipadpro11": ("Tablet", "iPadOS", "iPad Pro 11 (834 px)", "safari", aparelho("iPad Pro 11")),
}


def montar_cfg(pw, perfil: dict) -> dict:
    if "_descritor" not in perfil:
        return dict(perfil)
    d = pw.devices[perfil["_descritor"]]
    return {"viewport": d["viewport"], "toque": d["has_touch"], "is_mobile": d["is_mobile"],
            "device_scale_factor": d["device_scale_factor"],
            "user_agent": d["user_agent"] + perfil["_sufixo"]}


def medir_login(s: sc.Sessao) -> dict:
    """Mede a adaptação da página de login (servidor de autenticação da UnB) antes de entrar."""
    s.pg.goto(sc.LOGIN, wait_until="networkidle", timeout=120000)
    try:
        return s.pg.evaluate(sc.JS_ADAPTACAO)
    except Exception as e:  # noqa: BLE001
        return {"erro": type(e).__name__}


def capturar_tela(pg, nome: str) -> str:
    """Captura borrada só da área visível (o que o estudante vê ao abrir a página)."""
    EVID.mkdir(parents=True, exist_ok=True)
    h = pg.add_style_tag(content=sc.CSS_BORRAO)
    pg.wait_for_timeout(300)
    destino = EVID / f"{nome}.jpg"
    pg.screenshot(path=str(destino), type="jpeg", quality=60, scale="css")
    h.evaluate("e => e.remove()")
    return str(destino.relative_to(sc.RAIZ))


def executar_perfil(pw, pid: str, tarefas: list[str], capturas: list[str]):
    categoria, sistema, nome_aparelho, nav, perfil = PERFIS[pid]
    rotulo, motor, canal, exe_chave = NAVEGADORES[nav]
    comum = {"perfil": pid, "categoria": categoria, "sistema_emulado": sistema,
             "aparelho": nome_aparelho, "navegador": rotulo}
    exe = EXECUTAVEIS.get(exe_chave) if exe_chave else None
    if exe and not Path(exe).exists():
        sc.gravar(SAIDA, {"data_hora": time.strftime("%Y-%m-%dT%H:%M:%S"), **comum,
                          "erro": f"navegador indisponível: {exe}"})
        print(pid, "INDISPONÍVEL", flush=True)
        return
    cfg = montar_cfg(pw, perfil)
    s = sc.Sessao(pw, motor, categoria.lower(), canal=canal, cfg=cfg, executavel=exe,
                  argumentos=ARGS_SEM_ASSISTENTE if exe else None)
    try:
        comum.update({"largura_css_px": cfg["viewport"]["width"], "altura_css_px": cfg["viewport"]["height"],
                      "densidade": cfg.get("device_scale_factor", 1), "toque": cfg["toque"],
                      "modo_movel": bool(cfg.get("is_mobile")) and motor != "firefox",
                      "user_agent": s.pg.evaluate("navigator.userAgent")})
        reg_login = {"tarefa": "login", "adaptacao": medir_login(s)}
        try:
            reg_login["evidencia"] = capturar_tela(s.pg, f"{pid}-login") if "login" in capturas else None
        except Exception:  # noqa: BLE001
            reg_login["evidencia"] = None
        reg_login["login_ok"] = False
        for tentativa in (1, 2):  # a página do CAS às vezes não responde ao primeiro envio
            try:
                s.login()
                reg_login.update({"login_ok": True, "tentativa": tentativa})
                break
            except BaseException as e:  # noqa: BLE001  (SystemExit do login também é registrado)
                reg_login["erro"] = f"{type(e).__name__}: {str(e)[:600]}"
                time.sleep(sc.PAUSA_S)
        if reg_login["login_ok"]:
            reg_login.pop("erro", None)
        sc.gravar(SAIDA, sc.base_registro(s, {**comum, **reg_login}))
        print(pid, "login", "ok" if reg_login["login_ok"] else "FALHA", flush=True)
        if not reg_login["login_ok"]:
            return
        for t in tarefas:
            reg = sc.executar_com_repeticao(s, t)
            if not reg.get("erro"):
                try:
                    reg["adaptacao"] = s.pg.evaluate(sc.JS_ADAPTACAO)
                except Exception as e:  # noqa: BLE001
                    reg["erro_adaptacao"] = type(e).__name__
            reg["evidencia"] = None
            if t in capturas:
                try:
                    reg["evidencia"] = capturar_tela(s.pg, f"{pid}-{t}")
                except Exception:  # noqa: BLE001
                    pass
            sc.gravar(SAIDA, sc.base_registro(s, {**comum, **reg}))
            print(pid, t, "ok" if reg.get("marcadores_ok") else "FALHA", flush=True)
    finally:
        try:
            s.fechar()
        except Exception:  # noqa: BLE001
            pass


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--perfis", nargs="+", choices=list(PERFIS), default=list(PERFIS))
    ap.add_argument("--tarefas", nargs="+", default=["T1", "T2", "T3", "T4", "T5", "T6"])
    ap.add_argument("--capturas", nargs="*", default=["login", "T2", "T6"],
                    help="tarefas com captura borrada da área visível (login, T1 a T6)")
    ap.add_argument("--listar", action="store_true", help="lista os perfis e sai")
    args = ap.parse_args()
    if args.listar:
        for pid, (cat, so, ap_, nav, _) in PERFIS.items():
            print(f"{pid:22} {cat:10} {so:16} {ap_:30} {NAVEGADORES[nav][0]}")
        return
    for v in ("SIGAA_USUARIO", "SIGAA_SENHA"):
        if not os.environ.get(v):
            sys.exit(f"Defina a variável de ambiente {v}.")
    with sync_playwright() as pw:
        for pid in args.perfis:
            try:
                executar_perfil(pw, pid, args.tarefas, args.capturas)
            except Exception as e:  # noqa: BLE001
                sc.gravar(SAIDA, {"data_hora": time.strftime("%Y-%m-%dT%H:%M:%S"), "perfil": pid,
                                  "erro": f"{type(e).__name__}: {str(e)[:300]}"})
                print(pid, "ERRO", type(e).__name__, str(e)[:200], flush=True)
            time.sleep(sc.PAUSA_S)


if __name__ == "__main__":
    main()
