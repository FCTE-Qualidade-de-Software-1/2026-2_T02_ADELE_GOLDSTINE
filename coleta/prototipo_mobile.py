"""Geração das telas SVG/PNG e do simulador HTML interativo do Protótipo Mobile (Fase 4).

Produz as quatro telas em alta fidelidade (SVG e PNG em 2x via Google Chrome headless)
e o simulador HTML interativo navegável do redesenho Mobile-First (360 x 800 px) do
Portal do Discente do SIGAA/UnB, preservando visualmente as funções do sistema original
(incluindo módulos e atalhos fora do escopo da avaliação como controles desabilitados)
e incorporando a identidade visual da UnB.

Dois usos:
- hook do MkDocs: o marcador ``[[PROTOTIPO_MOBILE_INTERATIVO]]`` em uma página vira o
  simulador mobile interativo (telas Início, Turmas/Notas, Integralização e Calendário);
- linha de comando: ``python coleta/prototipo_mobile.py`` grava os 4 SVGs e o arquivo
  ``prototipo-interativo.html`` em ``docs/assets/prototipo-mobile/``; com ``--png``,
  renderiza também os 4 PNGs em escala 2x pelo Google Chrome em modo headless.
"""

from __future__ import annotations

import base64
import os
import re
import shutil
import subprocess
import sys
import tempfile
from html import escape
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "docs/assets/prototipo-mobile"
LOGO_UNB = SAIDA / "logo-unb.png"

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

PALETA = {
    "navy": "#003366",
    "navy_dark": "#002244",
    "blue": "#1D4ED8",
    "blue_soft": "#EFF6FF",
    "blue_border": "#BFDBFE",
    "green": "#065F46",
    "green_mid": "#059669",
    "green_soft": "#ECFDF5",
    "green_border": "#A7F3D0",
    "red": "#991B1B",
    "amber": "#92400E",
    "amber_soft": "#FFFBEB",
    "amber_border": "#FDE68A",
    "bg": "#F1F5F9",
    "surface": "#FFFFFF",
    "surface_alt": "#F8FAFC",
    "disabled_bg": "#F1F5F9",
    "disabled_border": "#CBD5E1",
    "disabled_ink": "#64748B",
    "border": "#CBD5E1",
    "border_soft": "#E2E8F0",
    "ink": "#0F172A",
    "ink_mid": "#334155",
    "ink_light": "#475569",
}

MARCADOR = "[[PROTOTIPO_MOBILE_INTERATIVO]]"


def _e(texto: object) -> str:
    return escape(str(texto), quote=True)


def logo_unb_data_uri() -> str:
    """Retorna a logo da UnB em data URI PNG para embutir em SVGs e HTML."""
    if not LOGO_UNB.exists():
        return ""
    b64 = base64.b64encode(LOGO_UNB.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{b64}"


def encontrar_chrome() -> str | None:
    """Localiza o executável do Google Chrome ou Chromium no Windows, macOS ou Linux."""
    candidatos = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        shutil.which("google-chrome") or "",
        shutil.which("chromium") or "",
        shutil.which("chrome") or "",
    ]
    for c in candidatos:
        if c and Path(c).exists():
            return c
    return None


def _estilo_svg() -> str:
    return (
        "<style>"
        f".pm text{{font-family:{FONT}}}"
        f".pm .ink{{fill:{PALETA['ink']}}}"
        f".pm .muted{{fill:{PALETA['ink_light']}}}"
        f".pm .mid{{fill:{PALETA['ink_mid']}}}"
        f".pm .dis{{fill:{PALETA['disabled_ink']}}}"
        f".pm .white{{fill:#FFFFFF}}"
        ".pm .subwhite{fill:#E2E8F0}"
        ".pm .subblue{fill:#DBEAFE}"
        ".pm .subsky{fill:#BFDBFE}"
        ".pm .b{font-weight:700}"
        ".pm .sb{font-weight:600}"
        ".pm .num{font-variant-numeric:tabular-nums}"
        "</style>"
    )


def _wrap_svg(largura: int, altura: int, titulo: str, corpo: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'class="pm" fill="{PALETA["ink"]}" viewBox="0 0 {largura} {altura}" '
        f'width="{largura}" height="{altura}" role="img" aria-label="{_e(titulo)}">'
        f"{_estilo_svg()}"
        f'<rect x="0" y="0" width="{largura}" height="{altura}" fill="#F8FAFC" rx="14"/>'
        f"{corpo}</svg>"
    )


def _icone_vec(nome: str, x: float, y: float, cor: str, tam: float = 14) -> str:
    """Ícones vetoriais geométricos simples para a barra de navegação e ações."""
    s = tam / 16.0
    t = f'transform="translate({x:.1f},{y:.1f}) scale({s:.3f})"'
    if nome == "home":
        return f'<g {t} fill="none" stroke="{cor}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 7.5 L8 2 L14 7.5 V14 H10 V9.5 H6 V14 H2 Z"/></g>'
    if nome == "book":
        return f'<g {t} fill="none" stroke="{cor}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="2" width="11" height="12" rx="1.5"/><line x1="6" y1="2" x2="6" y2="14"/><line x1="8.5" y1="6" x2="11.5" y2="6"/></g>'
    if nome == "chart":
        return f'<g {t} fill="{cor}"><rect x="2" y="9" width="3" height="5" rx="0.8"/><rect x="6.5" y="5" width="3" height="9" rx="0.8"/><rect x="11" y="2" width="3" height="12" rx="0.8"/></g>'
    if nome == "cal":
        return f'<g {t} fill="none" stroke="{cor}" stroke-width="1.8" stroke-linecap="round"><rect x="2" y="3" width="12" height="11" rx="1.8"/><line x1="2" y1="6.8" x2="14" y2="6.8"/><line x1="5.5" y1="1.5" x2="5.5" y2="4"/><line x1="10.5" y1="1.5" x2="10.5" y2="4"/></g>'
    if nome == "dl":
        return f'<g {t} fill="none" stroke="{cor}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 2.5 V10.5 M5 7.8 L8 10.8 L11 7.8"/><path d="M2.5 12 V13.5 H13.5 V12"/></g>'
    if nome == "ext":
        return f'<g {t} fill="none" stroke="{cor}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 2.5 H13.5 V7 M13.5 2.5 L7.5 8.5"/><path d="M12.5 9.5 V13.5 H2.5 V3.5 H6.5"/></g>'
    if nome == "back":
        return f'<g {t} fill="none" stroke="{cor}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3 L5 8 L10 13"/></g>'
    return ""


def _chip_visual(x: float, y: float, w: float, h: float, texto: str, ativo: bool = False) -> str:
    """Botão visual (apenas exibição quando desabilitado por estar fora do escopo)."""
    if ativo:
        bg, brd, cls, cor = PALETA["blue"], PALETA["blue"], "white b", "#FFFFFF"
        dash = ""
    else:
        bg, brd, cls, cor = PALETA["disabled_bg"], PALETA["disabled_border"], "dis sb", PALETA["disabled_ink"]
        dash = ' stroke-dasharray="3 2"'
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6" '
        f'fill="{bg}" stroke="{brd}" stroke-width="1"{dash}/>'
        f'<text x="{x + w / 2:.1f}" y="{y + h / 2 + 3.2:.1f}" text-anchor="middle" '
        f'font-size="9" class="{cls}" fill="{cor}">{_e(texto)}</text>'
    )


def _moldura_sigaa(w_svg: int, h_svg: int, titulo: str, subtitulo: str, aba_ativa: int, logo_uri: str) -> tuple[list[str], int, int, int]:
    """Desenha apenas o smartphone (388 px) com logo UnB, barra do sistema e navegação inferior."""
    x, y, w, h = 16, 14, w_svg - 32, h_svg - 28
    sx, sy, sw, sh = x + 10, y + 10, w - 20, h - 20
    cx = sx + 10
    cw = sw - 20

    p: list[str] = [
        f'<rect x="{x + 3}" y="{y + 5}" width="{w}" height="{h}" rx="30" fill="#CBD5E1" opacity="0.5"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="28" fill="#1E293B"/>',
        f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="20" fill="{PALETA["bg"]}"/>',
        # Barra de status do aparelho + tempo de sessão do SIGAA
        f'<rect x="{sx}" y="{sy}" width="{sw}" height="22" rx="20" fill="{PALETA["navy_dark"]}"/>',
        f'<rect x="{sx}" y="{sy + 11}" width="{sw}" height="11" fill="{PALETA["navy_dark"]}"/>',
        f'<text class="white b num" x="{sx + 14}" y="{sy + 15}" font-size="10">09:41</text>',
        f'<text class="subwhite num" x="{sx + sw - 14}" y="{sy + 15}" text-anchor="end" font-size="9.5">Sessão: 00:40 · 360 px</text>',
    ]

    # Cabeçalho institucional com Logo UnB + UnB SIGAA + A- / A+
    hy, hh = sy + 22, 46
    p.append(f'<rect x="{sx}" y="{hy}" width="{sw}" height="{hh}" fill="{PALETA["navy"]}"/>')
    p.append(f'<rect x="{cx}" y="{hy + 10}" width="44" height="24" rx="4" fill="#FFFFFF"/>')
    if logo_uri:
        p.append(f'<image href="{logo_uri}" x="{cx + 2}" y="{hy + 12}" width="40" height="20" preserveAspectRatio="xMidYMid meet"/>')
    else:
        p.append(f'<text class="b" x="{cx + 22}" y="{hy + 25}" text-anchor="middle" font-size="10" fill="{PALETA["navy"]}">UnB</text>')

    p.append(f'<text class="white b" x="{cx + 52}" y="{hy + 20}" font-size="13">{_e(titulo)}</text>')
    p.append(f'<text class="subwhite" x="{cx + 52}" y="{hy + 35}" font-size="9.5">{_e(subtitulo)}</text>')

    # Controles A- / A+ (OP-08 preservado)
    p.append(f'<rect x="{sx + sw - 68}" y="{hy + 9}" width="26" height="26" rx="6" fill="#0F4C81" stroke="#60A5FA"/>')
    p.append(f'<text class="white b" x="{sx + sw - 55}" y="{hy + 26}" text-anchor="middle" font-size="10">A-</text>')
    p.append(f'<rect x="{sx + sw - 38}" y="{hy + 9}" width="26" height="26" rx="6" fill="#0F4C81" stroke="#60A5FA"/>')
    p.append(f'<text class="white b" x="{sx + sw - 25}" y="{hy + 26}" text-anchor="middle" font-size="10">A+</text>')

    # Barra superior de utilitários do sistema (visuais não clicáveis)
    uy = hy + hh
    p.append(f'<rect x="{sx}" y="{uy}" width="{sw}" height="24" fill="#E2E8F0"/>')
    p.append(f'<line x1="{sx}" y1="{uy + 24}" x2="{sx + sw}" y2="{uy + 24}" stroke="{PALETA["border"]}" stroke-width="1"/>')
    utils = ["Portal Público", "Ajuda?", "Caixa Postal", "Módulos", "Sair"]
    ux = cx
    for idx, rot in enumerate(utils):
        uw = 68 if idx == 0 else (44 if idx == 1 else (68 if idx == 2 else (50 if idx == 3 else 36)))
        p.append(f'<rect x="{ux}" y="{uy + 3}" width="{uw}" height="18" rx="4" fill="#F8FAFC" stroke="#CBD5E1" stroke-dasharray="2 1.5"/>')
        p.append(f'<text class="dis sb" x="{ux + uw / 2:.1f}" y="{uy + 15}" text-anchor="middle" font-size="8">{rot}</text>')
        ux += uw + 5

    # Barra inferior fixa de navegação (4 abas primárias, altura 52 px)
    nh = 52
    ny = sy + sh - nh
    p.append(f'<rect x="{sx}" y="{ny}" width="{sw}" height="{nh}" rx="20" fill="#FFFFFF"/>')
    p.append(f'<rect x="{sx}" y="{ny}" width="{sw}" height="22" fill="#FFFFFF"/>')
    p.append(f'<line x1="{sx}" y1="{ny}" x2="{sx + sw}" y2="{ny}" stroke="{PALETA["border"]}" stroke-width="1"/>')
    abas = [("Início", "home"), ("Turmas", "book"), ("Progresso", "chart"), ("Calendário", "cal")]
    la = sw / 4
    for i, (nome, icone) in enumerate(abas):
        ax = sx + i * la
        ativo = i == aba_ativa
        cor = PALETA["blue"] if ativo else PALETA["ink_light"]
        if ativo:
            p.append(f'<rect x="{ax + 14:.1f}" y="{ny + 5}" width="{la - 28:.1f}" height="24" rx="12" fill="{PALETA["blue_soft"]}"/>')
        p.append(_icone_vec(icone, ax + la / 2 - 7, ny + 10, cor, 14))
        p.append(f'<text x="{ax + la / 2:.1f}" y="{ny + 42}" text-anchor="middle" font-size="10" '
                 f'class="{"b" if ativo else "sb"}" fill="{cor}">{nome}</text>')

    return p, cx, cw, uy + 30


def gerar_tela_1(logo_uri: str) -> str:
    """Tela 1: Início do Portal Mobile com funções do escopo e atalhos visuais do SIGAA."""
    W, H = 420, 960
    p, x, w, y = _moldura_sigaa(W, H, "UnB - SIGAA", "Portal do Discente · 2026.2", 0, logo_uri)

    # Faixa de identificação institucional + atalhos de conta visuais (não clicáveis)
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="58" rx="8" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b" x="{x + 9}" y="{y + 15}" font-size="9.8" fill="{PALETA["navy"]}">CAMPUS UNB GAMA: FCTE · ENGENHARIA DE SOFTWARE (ATIVO)</text>')
    atalhos_topo = [("Abrir Chamado", 70), ("Alterar Senha", 66), ("Dados/Foto", 58), ("Mensagens", 58), ("Menu Disc.", 62)]
    tx = x + 9
    for rot, tw in atalhos_topo:
        p.append(_chip_visual(tx, y + 24, tw, 24, rot, ativo=False))
        tx += tw + 4

    # Faixa dos 7 módulos horizontais (Ensino ativo; Pesquisa a Outros visuais/não clicáveis)
    y += 66
    modulos = [("Ensino", 48, True), ("Pesquisa", 52, False), ("Extensão", 52, False), ("Bolsas", 42, False), ("Estágio", 46, False), ("Mobilid.", 48, False), ("Outros", 42, False)]
    mx = x
    for rot, mw, atv in modulos:
        p.append(_chip_visual(mx, y, mw, 24, rot, ativo=atv))
        mx += mw + 3

    # Cartão de Integralizações e Índices (dados reais da interface do SIGAA)
    y += 32
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="82" rx="9" fill="#FFFFFF" stroke="{PALETA["blue_border"]}" stroke-width="1.2"/>')
    p.append(f'<text class="b" x="{x + 10}" y="{y + 17}" font-size="11" fill="{PALETA["navy"]}">Integralizações e Índices Acadêmicos</text>')
    p.append(f'<text class="b num" x="{x + w - 10}" y="{y + 17}" text-anchor="end" font-size="11" fill="{PALETA["green"]}">62% Integralizado</text>')
    p.append(f'<text class="b num" x="{x + 10}" y="{y + 34}" font-size="12.5" fill="{PALETA["blue"]}">1.320 h pendentes</text>')
    p.append(f'<text class="muted num" x="{x + 124}" y="{y + 34}" font-size="9.8">(Obrig: 930 h · Opt: 390 h · Comp: 0 h)</text>')
    p.append(f'<rect x="{x + 10}" y="{y + 42}" width="{w - 20}" height="6" rx="3" fill="#E2E8F0"/>')
    p.append(f'<rect x="{x + 10}" y="{y + 42}" width="{(w - 20) * 0.62:.0f}" height="6" rx="3" fill="{PALETA["green_mid"]}"/>')
    p.append(f'<text class="mid num" x="{x + 10}" y="{y + 62}" font-size="9.8">Currículo: 3.480 h · IRA: 3,7508 · MP: 3,8088</text>')
    p.append(f'<text class="b" x="{x + w - 10}" y="{y + 75}" text-anchor="end" font-size="9.5" fill="{PALETA["blue"]}">Detalhar integralização &gt;</text>')

    # Botões de acesso rápido (Atestado de Matrícula e Histórico)
    y += 89
    bw = (w - 8) / 2
    p.append(f'<rect x="{x}" y="{y}" width="{bw:.1f}" height="38" rx="8" fill="{PALETA["blue"]}"/>')
    p.append(f'<text class="white b" x="{x + bw / 2:.1f}" y="{y + 23}" text-anchor="middle" font-size="11">Emitir Atestado</text>')
    p.append(f'<rect x="{x + bw + 8:.1f}" y="{y}" width="{bw:.1f}" height="38" rx="8" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b" x="{x + bw + 8 + bw / 2:.1f}" y="{y + 23}" text-anchor="middle" font-size="11" fill="{PALETA["navy"]}">Emitir Histórico</text>')

    # Bloco Últimas Atualizações (presente na captura real)
    y += 45
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="38" rx="8" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b" x="{x + 10}" y="{y + 15}" font-size="9.5" fill="{PALETA["navy"]}">Últimas Atualizações</text>')
    p.append(_chip_visual(x + w - 68, y + 5, 58, 16, "<< Parar >>", ativo=False))
    p.append(f'<text class="mid" x="{x + 10}" y="{y + 30}" font-size="9">11/11/2026 - ECONOMIA DE ENERGIA: Tarefa alterada.</text>')

    # Seção Turmas do Semestre (horários decodificados inline + locais do print)
    y += 47
    p.append(f'<text class="b" x="{x}" y="{y + 12}" font-size="12">Turmas do Semestre (2026.2)</text>')
    p.append(f'<rect x="{x + w - 122}" y="{y - 2}" width="122" height="20" rx="10" fill="#E2E8F0"/>')
    p.append(f'<rect x="{x + w - 120}" y="{y}" width="54" height="16" rx="8" fill="#FFFFFF"/>')
    p.append(f'<text class="b" x="{x + w - 93}" y="{y + 11}" text-anchor="middle" font-size="8.8">Lista</text>')
    p.append(f'<text class="mid" x="{x + w - 35}" y="{y + 11}" text-anchor="middle" font-size="8.8">Grade</text>')

    turmas = [
        ("QUALIDADE DE SOFTWARE 1", "Seg e Qua · 10h00-11h50 (24M34)", "Local: FCTE - S6"),
        ("ECONOMIA DE ENERGIA", "Ter e Qui · 08h00-09h50 (35M12)", "Local: FCTE - S5"),
        ("PARADIGMAS DE PROGRAMAÇÃO", "Qua e Sex · 14h00-15h50 (46T23)", "Local: FCTE - S10"),
        ("PROJETO INTEGRADOR DE ENGENHARIA 1", "Seg e Qua · 16h00-17h50 (24T45)", "Local: FCTE - S2"),
    ]
    cy = y + 23
    for tit, hor, loc in turmas:
        p.append(f'<rect x="{x}" y="{cy}" width="{w}" height="58" rx="8" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
        p.append(f'<text class="b" x="{x + 10}" y="{cy + 16}" font-size="10.2" fill="{PALETA["navy"]}">{tit}</text>')
        p.append(f'<text class="mid" x="{x + 10}" y="{cy + 31}" font-size="9.5">{hor}</text>')
        p.append(f'<text class="muted" x="{x + 10}" y="{cy + 46}" font-size="9">{loc}</text>')
        p.append(f'<rect x="{x + w - 118}" y="{cy + 32}" width="54" height="20" rx="4" fill="{PALETA["blue_soft"]}"/>')
        p.append(f'<text class="b" x="{x + w - 91}" y="{cy + 45}" text-anchor="middle" font-size="8.5" fill="{PALETA["blue"]}">Materiais</text>')
        p.append(f'<rect x="{x + w - 60}" y="{cy + 32}" width="50" height="20" rx="4" fill="{PALETA["green_soft"]}"/>')
        p.append(f'<text class="b" x="{x + w - 35}" y="{cy + 45}" text-anchor="middle" font-size="8.5" fill="{PALETA["green"]}">Notas</text>')
        cy += 63

    # Link visual Ver turmas anteriores
    p.append(_chip_visual(x + w - 120, cy + 1, 120, 18, "Ver turmas anteriores", ativo=False))

    # Seções Minhas Atividades + Comunidades Virtuais (do print real)
    ay = cy + 25
    p.append(f'<rect x="{x}" y="{ay}" width="{w}" height="42" rx="8" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b" x="{x + 10}" y="{ay + 15}" font-size="9.5" fill="{PALETA["navy"]}">Minhas Atividades</text>')
    p.append(f'<text class="mid" x="{x + 10}" y="{ay + 30}" font-size="8.8">30/11/2026 23:59 (9 dias) · ECONOMIA DE ENERGIA: Relatório</text>')

    ay += 48
    p.append(f'<rect x="{x}" y="{ay}" width="{w}" height="28" rx="8" fill="#F8FAFC" stroke="{PALETA["border"]}" stroke-dasharray="3 2"/>')
    p.append(f'<text class="dis sb" x="{x + 10}" y="{ay + 18}" font-size="8.8">Comunidades Virtuais: Não participa de nenhuma comunidade virtual.</text>')

    # Atalhos institucionais visuais (não clicáveis)
    ay += 34
    atalhos_rod = [("Avaliação Institucional", 112), ("Regulamento Graduação", 114), ("Extrato Restaurante (RU)", 114)]
    ax = x
    for rot, aw in atalhos_rod:
        p.append(_chip_visual(ax, ay, aw, 24, rot, ativo=False))
        ax += aw + 4

    return _wrap_svg(W, H, "Tela 1 — Início do Portal Mobile (SIGAA/UnB)", "".join(p))


def gerar_tela_2(logo_uri: str) -> str:
    """Tela 2: Turma Virtual Unificada, Materiais, Notas e atalhos visuais fora do escopo."""
    W, H = 420, 960
    p, x, w, y = _moldura_sigaa(W, H, "UnB - SIGAA", "Turma Virtual · Qualidade de Software 1", 1, logo_uri)

    # Faixa de módulos preservada
    modulos = [("Ensino", 48, True), ("Pesquisa", 52, False), ("Extensão", 52, False), ("Bolsas", 42, False), ("Estágio", 46, False), ("Mobilid.", 48, False), ("Outros", 42, False)]
    mx = x
    for rot, mw, atv in modulos:
        p.append(_chip_visual(mx, y, mw, 22, rot, ativo=atv))
        mx += mw + 3

    # Cabeçalho da disciplina sem sobreposição sobre o título
    y += 30
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="74" rx="9" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(_icone_vec("back", x + 10, y + 12, PALETA["blue"], 14))
    p.append(f'<text class="b" x="{x + 28}" y="{y + 23}" font-size="11.5" fill="{PALETA["navy"]}">QUALIDADE DE SOFTWARE 1</text>')
    p.append(f'<text class="muted" x="{x + 28}" y="{y + 38}" font-size="9.8">FGA0315 · 2026.2 · FCTE - S6 · Seg/Qua 10h00-11h50</text>')
    p.append(f'<rect x="{x + 10}" y="{y + 46}" width="88" height="20" rx="5" fill="{PALETA["surface_alt"]}" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="mid sb" x="{x + 54}" y="{y + 59}" text-anchor="middle" font-size="9">Trocar turma</text>')
    p.append(f'<rect x="{x + 104}" y="{y + 46}" width="92" height="20" rx="5" fill="{PALETA["surface_alt"]}" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="mid sb" x="{x + 150}" y="{y + 59}" text-anchor="middle" font-size="9">Plano de Ensino</text>')
    p.append(_chip_visual(x + 202, y + 46, 136, 20, "Config. da Turma (Visual)", ativo=False))

    # Menu de opções da Turma Virtual (escopo + funções apagadas fora do escopo)
    y += 82
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="38" rx="8" fill="#E2E8F0"/>')
    p.append(f'<rect x="{x + 4}" y="{y + 4}" width="110" height="30" rx="6" fill="{PALETA["blue"]}"/>')
    p.append(f'<text class="white b" x="{x + 59}" y="{y + 23}" text-anchor="middle" font-size="10.5">Materiais</text>')
    p.append(f'<text class="mid b" x="{x + 174}" y="{y + 23}" text-anchor="middle" font-size="10.5">Minhas Notas</text>')
    p.append(f'<text class="mid sb" x="{x + 290}" y="{y + 23}" text-anchor="middle" font-size="10.5">Notícias</text>')

    y += 44
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="52" rx="8" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="dis sb" x="{x + 10}" y="{y + 15}" font-size="8.8">Demais módulos da Turma Virtual (fora do escopo):</text>')
    extras_tv = [("Participantes", 68), ("Frequência", 58), ("Tarefas", 46), ("Fóruns", 44), ("Enquetes", 50), ("Estat.", 42)]
    ex = x + 10
    for rot, ew in extras_tv:
        p.append(_chip_visual(ex, y + 22, ew, 22, rot, ativo=False))
        ex += ew + 4

    # Central Única de Materiais (4 locais do SIGAA reunidos)
    y += 62
    p.append(f'<text class="b" x="{x}" y="{y + 12}" font-size="11.5">Central Única de Materiais</text>')
    for i, chip in enumerate(["Todos (4)", "Arquivos", "Referências", "Conteúdos"]):
        cw_c = 78 if i != 2 else 86
        cx_c = x + sum([82, 82, 90][k] for k in range(i)) if i > 0 else x
        atv = i == 0
        p.append(f'<rect x="{cx_c}" y="{y + 20}" width="{cw_c}" height="24" rx="12" fill="{PALETA["navy"] if atv else "#FFFFFF"}" '
                 f'stroke="{PALETA["navy"] if atv else PALETA["border"]}"/>')
        p.append(f'<text x="{cx_c + cw_c / 2}" y="{y + 35}" text-anchor="middle" font-size="9.5" class="{"white b" if atv else "mid"}">{chip}</text>')

    mats = [
        ("Plano de Ensino e Cronograma 2026.2", "PDF · 240 KB · Anexo na página inicial", "dl"),
        ("Roteiro do Trabalho Final da Disciplina", "PDF · 410 KB · Pasta Arquivos", "dl"),
        ("Norma ISO/IEC 25010:2023 (Referência)", "Link externo · Seção Referências", "ext"),
        ("Guia de Revisão de Qualidade", "Conteúdo / Página web da turma", "ext"),
    ]
    my = y + 52
    for tit, sub, ic in mats:
        p.append(f'<rect x="{x}" y="{my}" width="{w}" height="56" rx="8" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
        p.append(f'<text class="b" x="{x + 12}" y="{my + 22}" font-size="10.5">{tit}</text>')
        p.append(f'<text class="muted" x="{x + 12}" y="{my + 39}" font-size="9.2">{sub}</text>')
        p.append(f'<rect x="{x + w - 52}" y="{my + 6}" width="44" height="44" rx="8" fill="{PALETA["blue_soft"]}" stroke="{PALETA["blue_border"]}"/>')
        p.append(_icone_vec(ic, x + w - 37, my + 20, PALETA["blue"], 15))
        my += 62

    # Prévia da aba Minhas Notas (acesso em 1 toque)
    p.append(f'<rect x="{x}" y="{my + 4}" width="{w}" height="82" rx="9" fill="{PALETA["green_soft"]}" stroke="{PALETA["green_border"]}"/>')
    p.append(f'<text class="b" x="{x + 12}" y="{my + 23}" font-size="11" fill="{PALETA["green"]}">Relatório de Notas desta Disciplina</text>')
    p.append(f'<text class="mid num" x="{x + 12}" y="{my + 42}" font-size="10.5">Entrega 1: 9,2   |   Ponto de Controle 2: 9,0   |   Faltas: 0</text>')
    p.append(f'<text class="b num" x="{x + 12}" y="{my + 60}" font-size="11" fill="{PALETA["navy"]}">Média parcial: 9,10 (Menção estimada: SS)</text>')
    p.append(f'<text class="muted" x="{x + 12}" y="{my + 75}" font-size="9.2">Acesso direto pela aba Minhas Notas sem menu suspenso.</text>')

    return _wrap_svg(W, H, "Tela 2 — Turma Virtual Unificada e Notas (SIGAA/UnB)", "".join(p))


def gerar_tela_3(logo_uri: str) -> str:
    """Tela 3: Integralização Curricular, Índices, Dados Institucionais e Serviços do Menu Ensino."""
    W, H = 420, 960
    p, x, w, y = _moldura_sigaa(W, H, "UnB - SIGAA", "Integralização e Ensino · 2026.2", 2, logo_uri)

    # Card destaque de Carga Horária Pendente
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="92" rx="10" fill="{PALETA["navy"]}"/>')
    p.append(f'<text class="white sb" x="{x + 14}" y="{y + 20}" font-size="10.5">Carga Horária Total Pendente para Conclusão</text>')
    p.append(f'<text class="white b num" x="{x + 14}" y="{y + 46}" font-size="21">1.320 horas pendentes</text>')
    p.append(f'<text class="subwhite num" x="{x + 14}" y="{y + 65}" font-size="10">2.160 h cumpridas de 3.480 h do currículo (62% integralizado)</text>')
    p.append(f'<text class="subsky" x="{x + 14}" y="{y + 81}" font-size="9.5">Consulta direta na tela sem precisar emitir o Histórico PDF.</text>')

    # Barras por modalidade curricular (valores reais do print)
    y += 102
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="142" rx="9" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b" x="{x + 12}" y="{y + 20}" font-size="11.5">Detalhamento por Modalidade Curricular</text>')
    cats = [
        ("CH. Obrigatória", "1.470 / 2.400 h", "Pendente: 930 h", 0.61, PALETA["blue"]),
        ("CH. Optativa", "540 / 930 h", "Pendente: 390 h", 0.58, PALETA["green_mid"]),
        ("CH. Complementar", "150 / 150 h", "Pendente: 0 h", 1.00, "#6366F1"),
    ]
    for i, (nome, cumprida, pend, frac, cor) in enumerate(cats):
        cy = y + 34 + i * 35
        p.append(f'<text class="sb" x="{x + 12}" y="{cy + 10}" font-size="10">{nome}</text>')
        p.append(f'<text class="muted num" x="{x + w - 12}" y="{cy + 10}" text-anchor="end" font-size="9.8">{cumprida} · {pend}</text>')
        p.append(f'<rect x="{x + 12}" y="{cy + 16}" width="{w - 24}" height="7" rx="3.5" fill="#E2E8F0"/>')
        p.append(f'<rect x="{x + 12}" y="{cy + 16}" width="{(w - 24) * frac:.0f}" height="7" rx="3.5" fill="{cor}"/>')

    # Índices Acadêmicos com siglas explicadas + Dados Institucionais
    y += 150
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="92" rx="9" fill="{PALETA["surface_alt"]}" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b" x="{x + 12}" y="{y + 18}" font-size="11" fill="{PALETA["navy"]}">Índices Acadêmicos e Dados Institucionais</text>')
    p.append(f'<text class="ink num" x="{x + 12}" y="{y + 36}" font-size="10">IRA (Índice de Rendimento Acadêmico): 3,7508</text>')
    p.append(f'<text class="ink num" x="{x + 12}" y="{y + 52}" font-size="10">MP (Média Ponderada): 3,8088</text>')
    p.append(f'<text class="mid" x="{x + 12}" y="{y + 68}" font-size="9.5">Curso: Engenharia de Software / FCTE (Bacharelado - MT)</text>')
    p.append(f'<text class="mid num" x="{x + 12}" y="{y + 82}" font-size="9.5">Nível: Graduação · Status: ATIVO · Entrada: 2021.2</text>')

    # Obrigatórias Pendentes e Documentos
    y += 100
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="128" rx="9" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b" x="{x + 12}" y="{y + 19}" font-size="11">Componentes Pendentes e Documentos</text>')
    p.append(f'<rect x="{x + 12}" y="{y + 27}" width="{w - 24}" height="28" rx="6" fill="{PALETA["green_soft"]}"/>')
    p.append(f'<text class="b" x="{x + 20}" y="{y + 40}" font-size="9.5" fill="{PALETA["green"]}">Trabalho de Conclusão de Curso 1 (60 h)</text>')
    p.append(f'<text class="mid" x="{x + 20}" y="{y + 50}" font-size="8.5">Pré-requisito cumprido · Obrigatória pendente</text>')
    p.append(f'<rect x="{x + 12}" y="{y + 60}" width="{w - 24}" height="28" rx="6" fill="{PALETA["blue_soft"]}"/>')
    p.append(f'<text class="b" x="{x + 20}" y="{y + 73}" font-size="9.5" fill="{PALETA["blue"]}">Qualidade de Software 2 (60 h)</text>')
    p.append(f'<text class="mid" x="{x + 20}" y="{y + 83}" font-size="8.5">Fluxo sugerido do 9º semestre · Sem pendência</text>')
    bw = (w - 30) / 2
    p.append(f'<rect x="{x + 12}" y="{y + 94}" width="{bw:.1f}" height="26" rx="6" fill="{PALETA["blue"]}"/>')
    p.append(f'<text class="white b" x="{x + 12 + bw / 2:.1f}" y="{y + 111}" text-anchor="middle" font-size="9.5">Emitir Atestado Matrícula</text>')
    p.append(f'<rect x="{x + 18 + bw:.1f}" y="{y + 94}" width="{bw:.1f}" height="26" rx="6" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b" x="{x + 18 + bw + bw / 2:.1f}" y="{y + 111}" text-anchor="middle" font-size="9.5" fill="{PALETA["navy"]}">Emitir Histórico PDF</text>')

    # Demais serviços do Menu Ensino (visuais não clicáveis - fora do escopo)
    y += 136
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="114" rx="9" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="dis b" x="{x + 12}" y="{y + 18}" font-size="10">Demais Serviços do Menu Ensino (fora do escopo)</text>')
    servs = [
        ("Declaração de Vínculo", 160), ("Declaração Passe Livre", 160),
        ("Carteirinha Estudantil", 160), ("Matrícula On-Line", 160),
        ("Trancamento de Matrícula", 160), ("Consultas Gerais", 160),
    ]
    for i, (rot, sw_b) in enumerate(servs):
        col = i % 2
        row = i // 2
        bx = x + 12 + col * (sw_b + 6)
        by = y + 26 + row * 28
        p.append(_chip_visual(bx, by, sw_b, 22, rot, ativo=False))

    return _wrap_svg(W, H, "Tela 3 — Integralização Curricular e Serviços de Ensino (SIGAA/UnB)", "".join(p))


def gerar_tela_4(logo_uri: str) -> str:
    """Tela 4: Calendário Acadêmico 2026.2 Nativo e atalhos visuais correlatos."""
    W, H = 420, 960
    p, x, w, y = _moldura_sigaa(W, H, "UnB - SIGAA", "Calendário Acadêmico · Graduação 2026.2", 3, logo_uri)

    # Faixa de contexto + seletor de semestre (sem sair do SIGAA e sem lista desde 2000)
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="8" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<rect x="{x + 10}" y="{y + 11}" width="142" height="24" rx="6" fill="{PALETA["green_soft"]}" stroke="{PALETA["green_border"]}"/>')
    p.append(f'<text class="b" x="{x + 81}" y="{y + 26}" text-anchor="middle" font-size="9.5" fill="{PALETA["green"]}">Calendário Interno SIGAA</text>')
    p.append(f'<rect x="{x + 162}" y="{y + 11}" width="{w - 172}" height="24" rx="6" fill="{PALETA["surface_alt"]}" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b num" x="{x + 162 + (w - 172) / 2}" y="{y + 26}" text-anchor="middle" font-size="9.5" fill="{PALETA["navy"]}">Período: 2026.2 (Vigente) v</text>')

    # Banner crítico de Trancamento de Turmas
    y += 56
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="88" rx="10" fill="{PALETA["amber_soft"]}" stroke="{PALETA["amber_border"]}" stroke-width="1.5"/>')
    p.append(f'<rect x="{x + 12}" y="{y + 10}" width="150" height="18" rx="4" fill="{PALETA["amber"]}"/>')
    p.append(f'<text class="white b" x="{x + 87}" y="{y + 23}" text-anchor="middle" font-size="9">PRAZO CRÍTICO DO SEMESTRE</text>')
    p.append(f'<text class="b" x="{x + 12}" y="{y + 45}" font-size="13" fill="{PALETA["ink"]}">Trancamento Geral e de Turmas</text>')
    p.append(f'<text class="b num" x="{x + 12}" y="{y + 64}" font-size="12" fill="{PALETA["amber"]}">10/08/2026 até 09/10/2026</text>')
    p.append(f'<text class="mid" x="{x + 12}" y="{y + 79}" font-size="9.5">Data-limite vigente no período 2026.2: 09/10/2026.</text>')

    # Filtros rápidos
    y += 98
    filtros = [("Todos", 62), ("Matrícula", 78), ("Trancamento", 92), ("Provas e Notas", 94)]
    fx = x
    for i, (rot, fw) in enumerate(filtros):
        atv = i == 0
        p.append(f'<rect x="{fx}" y="{y}" width="{fw}" height="24" rx="12" fill="{PALETA["blue"] if atv else "#FFFFFF"}" '
                 f'stroke="{PALETA["blue"] if atv else PALETA["border"]}"/>')
        p.append(f'<text x="{fx + fw / 2}" y="{y + 15.5}" text-anchor="middle" font-size="9" class="{"white b" if atv else "mid"}">{rot}</text>')
        fx += fw + 6

    # Lista cronológica do semestre corrente (datas reais do print: 10/08/2026 - 14/12/2026)
    marcos = [
        ("10/08/2026", "Início do Período Letivo 2026.2", "Abertura regular das aulas na graduação.", PALETA["green"]),
        ("10/08 a 09/10", "Período de Trancamento de Turmas", "Prazo oficial para trancamento pelo SIGAA.", PALETA["amber"]),
        ("30/11/2026", "Entrega de Atividades Extensionistas", "Marco visualizado no painel Minhas Atividades.", PALETA["blue"]),
        ("14/12/2026", "Término do Período Letivo 2026.2", "Encerramento das aulas regulares do semestre.", PALETA["navy"]),
        ("21/12/2026", "Prazo Final de Menções", "Consolidação das médias finais pelos docentes.", PALETA["ink_mid"]),
    ]
    my = y + 34
    for dt, tit, desc, cor in marcos:
        p.append(f'<rect x="{x}" y="{my}" width="{w}" height="54" rx="8" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
        p.append(f'<rect x="{x}" y="{my}" width="5" height="54" rx="2" fill="{cor}"/>')
        p.append(f'<text class="b num" x="{x + 14}" y="{my + 21}" font-size="10.2" fill="{cor}">{dt}</text>')
        p.append(f'<text class="b" x="{x + 108}" y="{my + 21}" font-size="10.5">{tit}</text>')
        p.append(f'<text class="mid" x="{x + 14}" y="{my + 40}" font-size="9.5">{desc}</text>')
        my += 61

    # Nota de integração + botões visuais fora do escopo (Regulamento e Calendários anteriores)
    p.append(f'<rect x="{x}" y="{my + 4}" width="{w}" height="110" rx="9" fill="#FFFFFF" stroke="{PALETA["border"]}"/>')
    p.append(f'<text class="b" x="{x + 12}" y="{my + 22}" font-size="10" fill="{PALETA["navy"]}">Documentos Normativos e Outros Períodos</text>')
    p.append(f'<text class="mid" x="{x + 12}" y="{my + 38}" font-size="9">Consulte diretamente as normas e os calendários arquivados:</text>')
    p.append(_chip_visual(x + 12, my + 48, w - 24, 24, "Regulamento dos Cursos de Graduação (Visual)", ativo=False))
    p.append(_chip_visual(x + 12, my + 78, (w - 30) / 2, 24, "Calendário Pós-Graduação", ativo=False))
    p.append(_chip_visual(x + 18 + (w - 30) / 2, my + 78, (w - 30) / 2, 24, "Calendários Anteriores", ativo=False))

    return _wrap_svg(W, H, "Tela 4 — Calendário Acadêmico 2026.2 Integrado (SIGAA/UnB)", "".join(p))


TELAS = [
    ("tela-1-inicio-t2-t3-t4", gerar_tela_1),
    ("tela-2-turma-notas-t1-t5", gerar_tela_2),
    ("tela-3-integralizacao-t4", gerar_tela_3),
    ("tela-4-calendario-t6", gerar_tela_4),
]


# ---------------------------------------------------------------------------
# Protótipo HTML/CSS/JS Interativo (360 x 800 px navegável)
# ---------------------------------------------------------------------------

CSS_INTERATIVO = """
<style>
.pm-wrap{margin:1.5rem 0;display:flex;flex-wrap:wrap;gap:1.5rem;align-items:flex-start;justify-content:center}
.pm-guide{flex:1 1 280px;max-width:380px;background:var(--md-code-bg-color,#f8fafc);border:1px solid var(--md-default-fg-color--lightest,#cbd5e1);border-radius:12px;padding:1rem 1.15rem;font-size:.82rem;line-height:1.5}
.pm-guide h4{margin:0 0 .6rem;font-size:.92rem}
.pm-guide-btn{display:block;width:100%;text-align:left;padding:.55rem .7rem;margin:.4rem 0;border-radius:8px;border:1px solid var(--md-default-fg-color--lightest,#cbd5e1);background:var(--md-default-bg-color,#fff);color:var(--md-default-fg-color,#0f172a);cursor:pointer;font-size:.78rem;transition:border-color .15s,background .15s}
.pm-guide-btn:hover,.pm-guide-btn.ativo{border-color:#1d4ed8;background:#eff6ff;color:#0f172a}
.pm-phone{width:360px;max-width:100%;height:730px;background:#1e293b;border-radius:30px;padding:10px;box-shadow:0 16px 36px rgba(15,23,42,.22);display:flex;flex-direction:column;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0f172a;box-sizing:border-box}
.pm-screen{background:#f1f5f9;border-radius:22px;overflow:hidden;display:flex;flex-direction:column;height:100%;position:relative}
.pm-status{background:#002244;color:#fff;font-size:12px;padding:4px 14px;display:flex;justify-content:space-between;font-weight:600;flex:none}
.pm-header{background:#003366;color:#fff;padding:8px 12px;display:flex;justify-content:space-between;align-items:center;gap:8px;flex:none}
.pm-brand{display:flex;align-items:center;gap:8px}
.pm-logo-box{background:#fff;border-radius:4px;padding:2px 3px;display:flex;align-items:center;justify-content:center;flex:none}
.pm-logo-box img{width:38px;height:19px;display:block;object-fit:contain}
.pm-header-title{font-size:13.5px;font-weight:700;line-height:1.15}
.pm-header-sub{font-size:12px;color:#e2e8f0;margin-top:1px}
.pm-font-btns{display:flex;gap:5px;flex:none}
.pm-font-btn{min-width:30px;min-height:30px;border-radius:7px;border:1px solid #60a5fa;background:#0f4c81;color:#fff;font-weight:700;font-size:12px;cursor:pointer}
.pm-utils,.pm-mods{display:flex;flex-wrap:wrap;gap:4px;padding:5px 10px;background:#e2e8f0;border-bottom:1px solid #cbd5e1;flex:none}
.pm-mods{background:#fff}
.pm-dis{min-height:24px;padding:3px 7px;border-radius:5px;border:1px dashed #cbd5e1;background:#f1f5f9;color:#64748b;font-size:12px;font-weight:600;cursor:not-allowed}
.pm-mod-ativo{padding:3px 9px;border-radius:5px;border:1px solid #1d4ed8;background:#1d4ed8;color:#fff;font-size:12px;font-weight:700}
.pm-body{flex:1;overflow-y:auto;padding:10px;display:flex;flex-direction:column;gap:8px;font-size:13.5px}
.pm-body.fs-lg{font-size:15.5px}
.pm-body.fs-sm{font-size:12px}
.pm-card{background:#fff;border:1px solid #cbd5e1;border-radius:10px;padding:10px;box-sizing:border-box}
.pm-card-navy{background:#003366;color:#fff;border:none}
.pm-card-amber{background:#fffbeb;border:1.5px solid #fde68a}
.pm-row{display:flex;justify-content:space-between;align-items:center;gap:8px}
.pm-btn-row{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.pm-btn{min-height:46px;padding:7px 9px;border-radius:8px;border:1px solid #cbd5e1;background:#fff;color:#003366;font-weight:700;font-size:12px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;line-height:1.2}
.pm-btn-primary{background:#1d4ed8;border-color:#1d4ed8;color:#fff}
.pm-btn-soft{background:#eff6ff;border-color:#bfdbfe;color:#1d4ed8;min-height:38px}
.pm-bar-bg{height:7px;border-radius:4px;background:#e2e8f0;overflow:hidden;margin:5px 0}
.pm-bar-fill{height:100%;background:#059669;border-radius:4px}
.pm-seg{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;background:#e2e8f0;padding:4px;border-radius:9px}
.pm-seg-2{grid-template-columns:repeat(2,1fr)}
.pm-seg button{min-height:38px;border:none;border-radius:6px;background:transparent;color:#334155;font-weight:600;font-size:12px;cursor:pointer}
.pm-seg button.ativo{background:#1d4ed8;color:#fff}
.pm-box-hor{background:#f8fafc;border:1px solid #e2e8f0;border-radius:6px;padding:7px;margin:6px 0;font-size:12px;line-height:1.35}
.pm-chip-row{display:flex;flex-wrap:wrap;gap:5px}
.pm-chip{min-height:32px;padding:4px 9px;border-radius:16px;border:1px solid #cbd5e1;background:#fff;color:#334155;font-size:12px;font-weight:600;cursor:pointer}
.pm-chip.ativo{background:#003366;border-color:#003366;color:#fff}
.pm-mat-item{display:flex;justify-content:space-between;align-items:center;gap:8px;background:#fff;border:1px solid #cbd5e1;border-radius:8px;padding:9px}
.pm-icon-btn{min-width:48px;min-height:44px;border-radius:8px;border:1px solid #bfdbfe;background:#eff6ff;color:#1d4ed8;font-weight:700;font-size:12px;cursor:pointer;display:flex;align-items:center;justify-content:center}
.pm-nav{background:#fff;border-top:1px solid #cbd5e1;display:grid;grid-template-columns:repeat(4,1fr);flex:none}
.pm-nav button{min-height:52px;border:none;background:#fff;color:#475569;font-size:12px;font-weight:600;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;padding:4px}
.pm-nav button.ativo{color:#1d4ed8;font-weight:700;box-shadow:inset 0 3px 0 #1d4ed8}
.pm-toast{background:#065f46;color:#fff;font-size:12px;padding:8px 12px;border-radius:8px;margin-top:4px;display:none}
.pm-toast.vis{display:block}
.pm-grade-tbl{width:100%;border-collapse:collapse;font-size:12px;background:#fff}
.pm-grade-tbl th,.pm-grade-tbl td{border:1px solid #cbd5e1;padding:5px 4px;text-align:center}
.pm-grade-tbl th{background:#eff6ff;color:#003366}
</style>
"""


def _html_interativo(logo_uri: str) -> str:
    logo_tag = f'<div class="pm-logo-box"><img src="{logo_uri}" alt="Logo da Universidade de Brasília"></div>' if logo_uri else ""
    return f"""
<div class="pm-wrap" id="pm-simulador">
  <div class="pm-guide">
    <h4>Simulador Interativo Mobile (360 × 800 px)</h4>
    <p style="margin:0 0 .5rem">Navegue pelas quatro telas principais do Portal do Discente reformulado. Os botões tracejados representam funções existentes no SIGAA original que ficam fora do escopo avaliado e permanecem exibidos apenas visualmente:</p>
    <button type="button" class="pm-guide-btn ativo" data-goto="inicio"><strong>1. Início</strong> — Integralização, emissão de atestado/histórico, últimas atualizações e turmas com horários decodificados.</button>
    <button type="button" class="pm-guide-btn" data-goto="turmas"><strong>2. Turmas e Notas</strong> — Central única de materiais e acesso direto às notas sem menus suspensos.</button>
    <button type="button" class="pm-guide-btn" data-goto="progresso"><strong>3. Progresso</strong> — Detalhamento de horas pendentes, siglas explicadas (IRA/MP) e serviços do menu Ensino.</button>
    <button type="button" class="pm-guide-btn" data-goto="calendario"><strong>4. Calendário 2026.2</strong> — Aberto diretamente no semestre vigente dentro do SIGAA, sem redirecionar ao site da SAA.</button>
    <p style="margin:.6rem 0 0;font-size:.74rem;opacity:.8">Use os botões <strong>A- / A+</strong> no topo para testar a escala tipográfica acessível.</p>
  </div>

  <div class="pm-phone" role="region" aria-label="Protótipo interativo do SIGAA Mobile da UnB em 360 pixels">
    <div class="pm-screen">
      <div class="pm-status">
        <span>09:41 · UnB SIGAA</span>
        <span>Sessão: 00:40 · 360 px</span>
      </div>
      <div class="pm-header">
        <div class="pm-brand">
          {logo_tag}
          <div>
            <div class="pm-header-title" id="pm-title">UnB - SIGAA</div>
            <div class="pm-header-sub" id="pm-sub">Portal do Discente · 2026.2</div>
          </div>
        </div>
        <div class="pm-font-btns">
          <button type="button" class="pm-font-btn" id="pm-f-down" aria-label="Diminuir fonte">A-</button>
          <button type="button" class="pm-font-btn" id="pm-f-up" aria-label="Aumentar fonte">A+</button>
        </div>
      </div>

      <div class="pm-utils" aria-label="Atalhos institucionais do SIGAA fora do escopo">
        <button type="button" class="pm-dis" disabled title="Função fora do escopo (exibição visual)">Portal Público</button>
        <button type="button" class="pm-dis" disabled title="Função fora do escopo (exibição visual)">Ajuda?</button>
        <button type="button" class="pm-dis" disabled title="Função fora do escopo (exibição visual)">Caixa Postal</button>
        <button type="button" class="pm-dis" disabled title="Função fora do escopo (exibição visual)">Módulos</button>
        <button type="button" class="pm-dis" disabled title="Função fora do escopo (exibição visual)">Sair</button>
      </div>

      <div class="pm-mods" aria-label="Módulos do Portal do Discente">
        <span class="pm-mod-ativo">Ensino</span>
        <button type="button" class="pm-dis" disabled title="Módulo fora do escopo (apenas visual)">Pesquisa</button>
        <button type="button" class="pm-dis" disabled title="Módulo fora do escopo (apenas visual)">Extensão</button>
        <button type="button" class="pm-dis" disabled title="Módulo fora do escopo (apenas visual)">Bolsas</button>
        <button type="button" class="pm-dis" disabled title="Módulo fora do escopo (apenas visual)">Estágio</button>
        <button type="button" class="pm-dis" disabled title="Módulo fora do escopo (apenas visual)">Mobilidade</button>
        <button type="button" class="pm-dis" disabled title="Módulo fora do escopo (apenas visual)">Outros</button>
      </div>

      <div class="pm-body" id="pm-body">
        <div id="pm-toast" class="pm-toast" role="status"></div>

        <!-- ABA 1: INÍCIO -->
        <div id="pm-tab-inicio" class="pm-panel">
          <div class="pm-card">
            <div style="font-size:12px;font-weight:700;color:#003366;margin-bottom:5px">CAMPUS UNB GAMA: FCTE · ENGENHARIA DE SOFTWARE (ATIVO)</div>
            <div class="pm-chip-row">
              <button type="button" class="pm-dis" disabled>Abrir Chamado</button>
              <button type="button" class="pm-dis" disabled>Alterar Senha</button>
              <button type="button" class="pm-dis" disabled>Dados e Foto</button>
              <button type="button" class="pm-dis" disabled>Mensagens</button>
            </div>
          </div>

          <div class="pm-card" style="border-color:#bfdbfe">
            <div class="pm-row">
              <strong style="color:#003366;font-size:12px">Integralizações e Índices</strong>
              <strong style="color:#065f46;font-size:12px">62% Integralizado</strong>
            </div>
            <div style="margin-top:3px;font-size:15px;font-weight:700;color:#1d4ed8">1.320 h pendentes <span style="font-size:12px;font-weight:400;color:#475569">(Obrig: 930 h · Opt: 390 h · Comp: 0 h)</span></div>
            <div class="pm-bar-bg"><div class="pm-bar-fill" style="width:62%"></div></div>
            <div class="pm-row" style="font-size:12px;color:#334155">
              <span>Currículo: 3.480 h · IRA: 3,7508 · MP: 3,8088</span>
              <button type="button" class="pm-chip" data-goto="progresso" style="min-height:26px;border-color:#bfdbfe;color:#1d4ed8">Detalhar</button>
            </div>
          </div>

          <div class="pm-btn-row">
            <button type="button" class="pm-btn pm-btn-primary" data-toast="Atestado de Matrícula 2026.2 gerado em PDF em 1 toque.">Emitir Atestado</button>
            <button type="button" class="pm-btn" data-goto="progresso">Emitir Histórico</button>
          </div>

          <div class="pm-card">
            <div class="pm-row">
              <strong style="font-size:12px;color:#003366">Últimas Atualizações</strong>
              <button type="button" class="pm-dis" disabled>&lt;&lt; Parar &gt;&gt;</button>
            </div>
            <div style="font-size:12px;color:#334155;margin-top:3px">11/11/2026 - ECONOMIA DE ENERGIA (2026.2): Tarefa alterada.</div>
          </div>

          <div class="pm-row" style="margin:4px 0 2px">
            <strong style="font-size:13px">Turmas do Semestre (2026.2)</strong>
            <div class="pm-seg pm-seg-2" style="width:120px">
              <button type="button" class="ativo" data-view="lista">Lista</button>
              <button type="button" data-view="grade">Grade</button>
            </div>
          </div>

          <div id="pm-view-lista" style="display:flex;flex-direction:column;gap:8px">
            <div class="pm-card">
              <strong style="font-size:12.5px;color:#003366">QUALIDADE DE SOFTWARE 1</strong>
              <div class="pm-box-hor">
                <div><strong>Seg e Qua · 10h00–11h50</strong> (24M34)</div>
                <div>Local: <strong>FCTE - S6</strong></div>
              </div>
              <div class="pm-btn-row">
                <button type="button" class="pm-btn pm-btn-soft" data-goto="turmas" data-subtab="materiais">Materiais</button>
                <button type="button" class="pm-btn pm-btn-soft" data-goto="turmas" data-subtab="notas" style="background:#ecfdf5;border-color:#a7f3d0;color:#065f46">Minhas Notas</button>
              </div>
            </div>
            <div class="pm-card">
              <strong style="font-size:12.5px;color:#003366">ECONOMIA DE ENERGIA</strong>
              <div class="pm-box-hor">
                <div><strong>Ter e Qui · 08h00–09h50</strong> (35M12)</div>
                <div>Local: <strong>FCTE - S5</strong></div>
              </div>
              <div class="pm-btn-row">
                <button type="button" class="pm-btn pm-btn-soft" data-goto="turmas" data-subtab="materiais">Materiais</button>
                <button type="button" class="pm-btn pm-btn-soft" data-goto="turmas" data-subtab="notas" style="background:#ecfdf5;border-color:#a7f3d0;color:#065f46">Minhas Notas</button>
              </div>
            </div>
            <div class="pm-card">
              <strong style="font-size:12.5px;color:#003366">PARADIGMAS DE PROGRAMAÇÃO</strong>
              <div class="pm-box-hor">
                <div><strong>Qua e Sex · 14h00–15h50</strong> (46T23)</div>
                <div>Local: <strong>FCTE - S10</strong></div>
              </div>
              <div class="pm-btn-row">
                <button type="button" class="pm-btn pm-btn-soft" data-goto="turmas" data-subtab="materiais">Materiais</button>
                <button type="button" class="pm-btn pm-btn-soft" data-goto="turmas" data-subtab="notas" style="background:#ecfdf5;border-color:#a7f3d0;color:#065f46">Minhas Notas</button>
              </div>
            </div>
          </div>

          <div id="pm-view-grade" style="display:none">
            <div class="pm-card">
              <strong style="font-size:12px;color:#003366">Grade Semanal Integrada (2026.2)</strong>
              <table class="pm-grade-tbl" style="margin-top:6px">
                <thead><tr><th>Hora</th><th>Seg/Qua</th><th>Ter/Qui</th><th>Sex</th></tr></thead>
                <tbody>
                  <tr><td>08h-10h</td><td>—</td><td>Economia (S5)</td><td>—</td></tr>
                  <tr><td>10h-12h</td><td>Qualidade (S6)</td><td>—</td><td>—</td></tr>
                  <tr><td>14h-16h</td><td>Paradigmas (S10)</td><td>—</td><td>Paradigmas (S10)</td></tr>
                </tbody>
              </table>
            </div>
          </div>

          <div class="pm-card">
            <strong style="font-size:12px;color:#003366">Minhas Atividades e Comunidades</strong>
            <div style="font-size:12px;color:#334155;margin-top:4px">30/11/2026 23:59 (9 dias) · ECONOMIA DE ENERGIA: Relatório</div>
            <div style="font-size:12px;color:#64748b;margin-top:4px">Comunidades Virtuais: Não participa de nenhuma comunidade virtual.</div>
            <div class="pm-chip-row" style="margin-top:6px">
              <button type="button" class="pm-dis" disabled>Ver turmas anteriores</button>
              <button type="button" class="pm-dis" disabled>Avaliação Institucional</button>
              <button type="button" class="pm-dis" disabled>Regulamento Graduação</button>
              <button type="button" class="pm-dis" disabled>Extrato Restaurante (RU)</button>
            </div>
          </div>
        </div>

        <!-- ABA 2: TURMAS E NOTAS -->
        <div id="pm-tab-turmas" class="pm-panel" style="display:none">
          <div class="pm-card">
            <strong style="font-size:13px;color:#003366;display:block">QUALIDADE DE SOFTWARE 1 (FGA0315)</strong>
            <div style="font-size:12px;color:#475569;margin:2px 0 8px">2026.2 · FCTE - S6 · Seg e Qua 10h00–11h50</div>
            <div class="pm-chip-row">
              <button type="button" class="pm-chip" style="min-height:30px" data-toast="Seletor de turmas matriculadas aberto.">Trocar turma</button>
              <button type="button" class="pm-chip" style="min-height:30px" data-toast="Plano de Ensino aberto em PDF.">Plano de Ensino</button>
              <button type="button" class="pm-dis" disabled>Config. da Turma</button>
            </div>
          </div>

          <div class="pm-seg">
            <button type="button" class="ativo" data-subtab="materiais">Materiais</button>
            <button type="button" class="subtab-btn" data-subtab="notas">Minhas Notas</button>
            <button type="button" class="subtab-btn" data-subtab="avisos">Notícias</button>
          </div>

          <div class="pm-card">
            <div style="font-size:12px;color:#64748b;margin-bottom:4px">Demais seções da Turma Virtual (fora do escopo):</div>
            <div class="pm-chip-row">
              <button type="button" class="pm-dis" disabled>Participantes</button>
              <button type="button" class="pm-dis" disabled>Frequência</button>
              <button type="button" class="pm-dis" disabled>Tarefas</button>
              <button type="button" class="pm-dis" disabled>Fóruns</button>
              <button type="button" class="pm-dis" disabled>Enquetes</button>
              <button type="button" class="pm-dis" disabled>Estatísticas</button>
            </div>
          </div>

          <div id="pm-sub-materiais" style="display:flex;flex-direction:column;gap:7px">
            <div class="pm-chip-row">
              <button type="button" class="pm-chip ativo" data-filter="todos">Todos (3)</button>
              <button type="button" class="pm-chip" data-filter="arquivo">Arquivos</button>
              <button type="button" class="pm-chip" data-filter="link">Referências</button>
            </div>
            <div class="pm-mat-item" data-tipo="arquivo">
              <div><strong style="font-size:12px">Plano de Ensino 2026.2</strong><div style="font-size:12px;color:#475569">PDF · 240 KB · Anexo principal</div></div>
              <button type="button" class="pm-icon-btn" data-toast="Download iniciado: Plano_Ensino_2026_2.pdf.">Baixar</button>
            </div>
            <div class="pm-mat-item" data-tipo="arquivo">
              <div><strong style="font-size:12px">Roteiro do Trabalho Final</strong><div style="font-size:12px;color:#475569">PDF · 410 KB · Pasta Arquivos</div></div>
              <button type="button" class="pm-icon-btn" data-toast="Download iniciado: Roteiro_Trabalho_Final.pdf.">Baixar</button>
            </div>
            <div class="pm-mat-item" data-tipo="link">
              <div><strong style="font-size:12px">Norma ISO/IEC 25010:2023</strong><div style="font-size:12px;color:#475569">Link externo · Seção Referências</div></div>
              <button type="button" class="pm-icon-btn" data-toast="Referência externa aberta em nova aba.">Abrir</button>
            </div>
          </div>

          <div id="pm-sub-notas" style="display:none;flex-direction:column;gap:8px">
            <div class="pm-card" style="background:#ecfdf5;border-color:#a7f3d0">
              <div style="font-size:12px;color:#065f46;font-weight:700">Relatório de Notas da Disciplina</div>
              <div style="font-size:17px;font-weight:700;color:#003366;margin:4px 0">Média parcial: 9,10 (SS)</div>
              <div style="font-size:12px;color:#334155">Frequência registrada: 100% (0 faltas)</div>
            </div>
            <div class="pm-card">
              <div class="pm-row"><strong>Entrega 1</strong><strong>9,2</strong></div>
              <div class="pm-row" style="margin-top:6px"><strong>Ponto de Controle 2</strong><strong>9,0</strong></div>
              <div class="pm-row" style="margin-top:6px"><strong>Entrega Final</strong><span style="color:#475569">Aguardando lançamento</span></div>
            </div>
          </div>

          <div id="pm-sub-avisos" style="display:none;flex-direction:column;gap:8px">
            <div class="pm-card">
              <strong style="font-size:12px">Apresentação da Entrega 2</strong>
              <div style="font-size:12px;color:#475569;margin-top:2px">Confirmada conforme cronograma oficial da disciplina.</div>
            </div>
          </div>
        </div>

        <!-- ABA 3: PROGRESSO / INTEGRALIZAÇÃO -->
        <div id="pm-tab-progresso" class="pm-panel" style="display:none">
          <div class="pm-card pm-card-navy">
            <div style="font-size:12px;color:#cbd5e1">Carga Horária Total Pendente para Conclusão</div>
            <div style="font-size:20px;font-weight:700;margin:4px 0">1.320 horas pendentes</div>
            <div style="font-size:12px;color:#cbd5e1">2.160 h cumpridas de 3.480 h totais (62% integralizado)</div>
          </div>

          <div class="pm-card">
            <strong style="font-size:12px">Por modalidade curricular</strong>
            <div style="margin-top:6px;font-size:12px">
              <div class="pm-row"><span>CH. Obrigatória</span><strong>1.470 / 2.400 h (Pendente: 930 h)</strong></div>
              <div class="pm-bar-bg"><div class="pm-bar-fill" style="width:61%;background:#1d4ed8"></div></div>
              <div class="pm-row"><span>CH. Optativa</span><strong>540 / 930 h (Pendente: 390 h)</strong></div>
              <div class="pm-bar-bg"><div class="pm-bar-fill" style="width:58%"></div></div>
              <div class="pm-row"><span>CH. Complementar</span><strong>150 / 150 h (Pendente: 0 h)</strong></div>
              <div class="pm-bar-bg"><div class="pm-bar-fill" style="width:100%;background:#6366f1"></div></div>
            </div>
          </div>

          <div class="pm-card" style="background:#f8fafc">
            <strong style="font-size:12px;color:#003366">Índices Acadêmicos e Dados Institucionais</strong>
            <div style="font-size:12px;margin-top:4px"><strong>IRA (Índice de Rendimento Acadêmico):</strong> 3,7508</div>
            <div style="font-size:12px;margin-top:2px"><strong>MP (Média Ponderada):</strong> 3,8088 · Entrada: 2021.2</div>
            <div class="pm-btn-row" style="margin-top:8px">
              <button type="button" class="pm-btn pm-btn-primary" style="min-height:38px" data-toast="Atestado de Matrícula emitido em PDF.">Emitir Atestado</button>
              <button type="button" class="pm-btn" style="min-height:38px" data-toast="Histórico Escolar emitido em PDF.">Emitir Histórico</button>
            </div>
          </div>

          <div class="pm-card">
            <div style="font-size:12px;font-weight:700;color:#64748b;margin-bottom:5px">Demais serviços do menu Ensino (fora do escopo):</div>
            <div class="pm-chip-row">
              <button type="button" class="pm-dis" disabled>Declaração de Vínculo</button>
              <button type="button" class="pm-dis" disabled>Passe Livre</button>
              <button type="button" class="pm-dis" disabled>Carteirinha Estudantil</button>
              <button type="button" class="pm-dis" disabled>Matrícula On-Line</button>
              <button type="button" class="pm-dis" disabled>Trancamento</button>
              <button type="button" class="pm-dis" disabled>Consultas Gerais</button>
            </div>
          </div>
        </div>

        <!-- ABA 4: CALENDÁRIO -->
        <div id="pm-tab-calendario" class="pm-panel" style="display:none">
          <div class="pm-card">
            <div class="pm-row">
              <span style="background:#ecfdf5;color:#065f46;border:1px solid #a7f3d0;padding:3px 8px;border-radius:6px;font-size:12px;font-weight:700">Calendário Interno SIGAA</span>
              <select id="pm-cal-sem" aria-label="Selecionar período do calendário" style="min-height:34px;border-radius:6px;border:1px solid #cbd5e1;padding:4px 8px;font-size:12px;font-weight:700;color:#003366">
                <option value="2026.2" selected>2026.2 (Vigente)</option>
                <option value="2027.1">2027.1 (Previsto)</option>
              </select>
            </div>
          </div>

          <div class="pm-card pm-card-amber">
            <span style="background:#92400e;color:#fff;padding:2px 7px;border-radius:4px;font-size:12px;font-weight:700">PRAZO CRÍTICO DO SEMESTRE</span>
            <div style="font-size:13.5px;font-weight:700;margin-top:5px" id="pm-cal-destaque-tit">Trancamento Geral e de Turmas</div>
            <div style="font-size:12.5px;font-weight:700;color:#92400e;margin-top:2px" id="pm-cal-destaque-dt">10/08/2026 até 09/10/2026</div>
            <div style="font-size:12px;color:#334155;margin-top:3px" id="pm-cal-destaque-desc">Data-limite para trancamento no SIGAA: 09/10/2026.</div>
          </div>

          <div style="display:flex;flex-direction:column;gap:7px">
            <div class="pm-card" style="border-left:5px solid #065f46">
              <strong style="color:#065f46;font-size:12px">10/08/2026 — Início do Período Letivo</strong>
              <div style="font-size:12px;color:#334155">Abertura regular das aulas da graduação 2026.2.</div>
            </div>
            <div class="pm-card" style="border-left:5px solid #92400e">
              <strong style="color:#92400e;font-size:12px">09/10/2026 — Limite de Trancamento</strong>
              <div style="font-size:12px;color:#334155">Último dia para trancar disciplinas regulares no SIGAA.</div>
            </div>
            <div class="pm-card" style="border-left:5px solid #003366">
              <strong style="color:#003366;font-size:12px">14/12/2026 — Término do Período Letivo</strong>
              <div style="font-size:12px;color:#334155">Encerramento das aulas e consolidação de menções até 21/12.</div>
            </div>
          </div>

          <div class="pm-card">
            <div style="font-size:12px;font-weight:700;color:#64748b;margin-bottom:5px">Documentos normativos (fora do escopo):</div>
            <div class="pm-chip-row">
              <button type="button" class="pm-dis" disabled>Regulamento dos Cursos de Graduação</button>
              <button type="button" class="pm-dis" disabled>Calendário Pós-Graduação</button>
              <button type="button" class="pm-dis" disabled>Calendários Anteriores</button>
            </div>
          </div>
        </div>
      </div>

      <nav class="pm-nav" aria-label="Navegação principal do protótipo">
        <button type="button" class="ativo" data-goto="inicio"><span>Início</span></button>
        <button type="button" data-goto="turmas"><span>Turmas</span></button>
        <button type="button" data-goto="progresso"><span>Progresso</span></button>
        <button type="button" data-goto="calendario"><span>Calendário</span></button>
      </nav>
    </div>
  </div>
</div>

<script>
(function(){{
  var root = document.getElementById('pm-simulador');
  if(!root) return;
  var titulos = {{
    inicio: ['UnB - SIGAA', 'Portal do Discente · 2026.2'],
    turmas: ['UnB - SIGAA', 'Turma Virtual · Qualidade de Software 1'],
    progresso: ['UnB - SIGAA', 'Integralização e Ensino · 2026.2'],
    calendario: ['UnB - SIGAA', 'Calendário Acadêmico · Graduação 2026.2']
  }};
  var body = document.getElementById('pm-body');
  var toast = document.getElementById('pm-toast');
  function irPara(aba, subtab){{
    root.querySelectorAll('.pm-panel').forEach(function(p){{ p.style.display='none'; }});
    var alvo = document.getElementById('pm-tab-' + aba);
    if(alvo) alvo.style.display='flex', alvo.style.flexDirection='column', alvo.style.gap='8px';
    document.getElementById('pm-title').textContent = titulos[aba][0];
    document.getElementById('pm-sub').textContent = titulos[aba][1];
    root.querySelectorAll('.pm-nav button, .pm-guide-btn').forEach(function(b){{
      b.classList.toggle('ativo', b.getAttribute('data-goto') === aba);
    }});
    if(aba === 'turmas' && subtab) abrirSubtab(subtab);
    body.scrollTop = 0;
  }}
  function abrirSubtab(sub){{
    ['materiais','notas','avisos'].forEach(function(s){{
      var el = document.getElementById('pm-sub-' + s);
      if(el) el.style.display = (s === sub) ? 'flex' : 'none';
    }});
    root.querySelectorAll('[data-subtab]').forEach(function(b){{
      if(b.closest('.pm-seg')) b.classList.toggle('ativo', b.getAttribute('data-subtab') === sub);
    }});
  }}
  root.addEventListener('click', function(ev){{
    var g = ev.target.closest('[data-goto]');
    if(g){{ irPara(g.getAttribute('data-goto'), g.getAttribute('data-subtab')); return; }}
    var s = ev.target.closest('[data-subtab]');
    if(s){{ abrirSubtab(s.getAttribute('data-subtab')); return; }}
    var v = ev.target.closest('[data-view]');
    if(v){{
      var modo = v.getAttribute('data-view');
      document.getElementById('pm-view-lista').style.display = modo==='lista' ? 'flex' : 'none';
      document.getElementById('pm-view-grade').style.display = modo==='grade' ? 'block' : 'none';
      v.parentElement.querySelectorAll('button').forEach(function(b){{ b.classList.toggle('ativo', b===v); }});
      return;
    }}
    var f = ev.target.closest('[data-filter]');
    if(f){{
      var tipo = f.getAttribute('data-filter');
      f.parentElement.querySelectorAll('button').forEach(function(b){{ b.classList.toggle('ativo', b===f); }});
      root.querySelectorAll('.pm-mat-item').forEach(function(it){{
        it.style.display = (tipo==='todos' || it.getAttribute('data-tipo')===tipo) ? 'flex' : 'none';
      }});
      return;
    }}
    var t = ev.target.closest('[data-toast]');
    if(t){{
      toast.textContent = t.getAttribute('data-toast');
      toast.classList.add('vis');
      setTimeout(function(){{ toast.classList.remove('vis'); }}, 4000);
    }}
  }});
  document.getElementById('pm-f-up').addEventListener('click', function(){{
    body.classList.remove('fs-sm'); body.classList.add('fs-lg');
  }});
  document.getElementById('pm-f-down').addEventListener('click', function(){{
    body.classList.remove('fs-lg'); body.classList.add('fs-sm');
  }});
  var sel = document.getElementById('pm-cal-sem');
  if(sel){{
    sel.addEventListener('change', function(){{
      var p27 = sel.value === '2027.1';
      document.getElementById('pm-cal-destaque-tit').textContent = p27 ? 'Calendário Previsto 2027.1' : 'Trancamento Geral e de Turmas';
      document.getElementById('pm-cal-destaque-dt').textContent = p27 ? 'Previsão de início: 08/03/2027' : '10/08/2026 até 09/10/2026';
      document.getElementById('pm-cal-destaque-desc').textContent = p27 ? 'Período futuro selecionado manualmente.' : 'Data-limite para trancamento no SIGAA: 09/10/2026.';
    }});
  }}
  irPara('inicio');
}})();
</script>
"""


def widget_interativo_html() -> str:
    """Bloco HTML completo do simulador para embutir no MkDocs e na página avulsa."""
    return CSS_INTERATIVO + _html_interativo(logo_unb_data_uri())


def on_page_markdown(markdown, page, config, files):  # noqa: ARG001 (assinatura do MkDocs)
    """Hook do MkDocs: substitui o marcador do protótipo pelo simulador interativo."""
    if MARCADOR not in markdown:
        return markdown
    return markdown.replace(MARCADOR, widget_interativo_html())


def main() -> None:
    SAIDA.mkdir(parents=True, exist_ok=True)
    png = "--png" in sys.argv
    chrome = encontrar_chrome() if png else None
    if png and not chrome:
        raise SystemExit("Google Chrome não encontrado para gerar os arquivos PNG.")

    logo_uri = logo_unb_data_uri()
    for nome, gerador in TELAS:
        svg = gerador(logo_uri)
        (SAIDA / f"{nome}.svg").write_text(svg, encoding="utf-8")
        if png and chrome:
            m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
            larg, alt = (int(m.group(1)), int(m.group(2))) if m else (420, 960)
            with tempfile.TemporaryDirectory() as tmp:
                pag = Path(tmp) / "tela.html"
                pag.write_text(
                    f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:#f8fafc}}'
                    f"svg{{display:block}}</style>{svg}",
                    encoding="utf-8",
                )
                subprocess.run(
                    [
                        chrome,
                        "--headless=new",
                        "--disable-gpu",
                        "--hide-scrollbars",
                        "--force-device-scale-factor=2",
                        f"--window-size={larg},{alt}",
                        f"--screenshot={SAIDA / (nome + '.png')}",
                        pag.as_uri(),
                    ],
                    check=True,
                    capture_output=True,
                )
        print(f"{nome}: {(SAIDA / (nome + '.svg')).relative_to(RAIZ)}{' e .png' if png else ''}")

    pag_interativa = SAIDA / "prototipo-interativo.html"
    pag_interativa.write_text(
        "<!doctype html><html lang=\"pt-BR\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
        "<title>Protótipo Mobile SIGAA/UnB (Fase 4 — Adele Goldstine)</title>"
        "<style>body{margin:0;padding:20px;background:#f1f5f9;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;color:#0f172a}"
        "h1{text-align:center;font-size:1.15rem;margin:0 0 .4rem;color:#003366}"
        "p.topo{text-align:center;font-size:.85rem;margin:0 0 1rem;color:#475569}</style></head><body>"
        "<h1>Protótipo Mobile-First de Alta Fidelidade — SIGAA/UnB (360 × 800 px)</h1>"
        "<p class=\"topo\">Ação de Melhoria Técnica Obrigatória (Fase 4) — Equipe T02 Adele Goldstine (FGA0315/UnB)</p>"
        f"{widget_interativo_html()}</body></html>",
        encoding="utf-8",
    )
    print(f"interativo: {pag_interativa.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
