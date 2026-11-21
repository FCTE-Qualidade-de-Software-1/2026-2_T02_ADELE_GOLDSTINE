"""Coleta automatizada de acessibilidade (M9) com o motor oficial da extensão WAVE.

Navega pelas páginas finais das tarefas T1 a T6 no SIGAA/UnB (Google Chrome,
1366 x 768 px), injeta o script oficial da extensão WAVE Evaluation Tool
(``wave.min.js``) em cada página, extrai o relatório estruturado sem textos
pessoais da página e grava:

- um relatório JSON sanitizado por tarefa em ``dados/brutos/acessibilidade/wave/T*-wave.json``;
- o resumo tabular em ``dados/brutos/acessibilidade/wave/resumo.csv`` (formato de Planilhas de Coleta).

As credenciais vêm apenas de ``SIGAA_USUARIO`` e ``SIGAA_SENHA`` e nunca são gravadas.
O arquivo ``wave.min.js`` da extensão oficial não é versionado no repositório; informe o
caminho local com ``--wave-js`` (por exemplo, extraído da extensão instalada no Chrome).
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import platform
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

import sigaa_coleta as sc

RAIZ = Path(__file__).resolve().parent.parent
SAIDA_WAVE = RAIZ / "dados/brutos/acessibilidade/wave"

PAGINAS_M9 = {
    "T1": "Relatório de notas do aluno",
    "T2": "Portal do Discente (Turmas do Semestre)",
    "T3": "Atestado de matrícula",
    "T4": "Índices acadêmicos",
    "T5": "Turma Virtual (notícia da turma)",
    "T6": "Calendário acadêmico 2026.2",
}


def sanitizar_wave(bruto: dict) -> dict:
    """Remove textos da página do relatório WAVE, preservando apenas códigos e contagens."""
    stats = bruto.get("statistics") or {}
    cats_out = {}
    for nome_cat, cat in (bruto.get("categories") or {}).items():
        itens_out = {}
        for item_id, item in (cat.get("items") or {}).items():
            hidden = item.get("hidden") or []
            itens_out[item_id] = {
                "id": item.get("id", item_id),
                "description": item.get("description", ""),
                "count": int(item.get("count", 0)),
                "hidden_count": sum(1 for h in hidden if h),
            }
        cats_out[nome_cat] = {
            "description": cat.get("description", nome_cat),
            "count": int(cat.get("count", 0)),
            "items": itens_out,
        }
    return {
        "statistics": {
            "totalelements": stats.get("totalelements"),
            "allitemcount": stats.get("allitemcount"),
            "aim": stats.get("aim"),
            "error": int(stats.get("error", 0)),
            "contrast": int(stats.get("contrast", 0)),
            "alert": int(stats.get("alert", 0)),
            "feature": int(stats.get("feature", 0)),
            "structure": int(stats.get("structure", 0)),
            "aria": int(stats.get("aria", 0)),
        },
        "categories": cats_out,
    }


def executar_wave_na_pagina(pg, wave_js: Path) -> dict:
    """Injeta wave.min.js na página atual e retorna o relatório WAVE sanitizado."""
    pg.evaluate(
        """() => {
          window.__waveResults = null;
          document.addEventListener('getExtensionUrl', () => {
            document.dispatchEvent(new CustomEvent('setExtensionUrl', { detail: '' }));
          });
          document.addEventListener('waveResults', (e) => {
            window.__waveResults = e.detail && e.detail.data ? e.detail.data : e.detail;
          });
        }"""
    )
    pg.add_script_tag(path=str(wave_js))
    pg.wait_for_function("() => window.__waveResults !== null", timeout=30000)
    bruto = pg.evaluate("() => window.__waveResults")
    return sanitizar_wave(bruto)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--wave-js", required=True, help="caminho local para o arquivo wave.min.js da extensão WAVE")
    ap.add_argument("--wave-versao", default="3.3.4.0", help="versão da extensão WAVE usada na coleta")
    ap.add_argument("--tarefas", nargs="+", default=["T1", "T2", "T3", "T4", "T5", "T6"])
    ap.add_argument("--avaliador", default="Felipe", help="primeiro nome do avaliador")
    ap.add_argument("--turma-t5", default="TÉCNICAS DE PROGRAMAÇÃO EM PLATAFORMAS EMERGENTES")
    ap.add_argument("--material-t5", default=sc.MATERIAL_T5)
    ap.add_argument("--modo-t5", choices=["arquivo", "noticia"], default="noticia")
    args = ap.parse_args()

    wave_js = Path(args.wave_js).expanduser().resolve()
    if not wave_js.is_file():
        sys.exit(f"Arquivo wave.min.js não encontrado: {wave_js}")
    for v in ("SIGAA_USUARIO", "SIGAA_SENHA"):
        if not os.environ.get(v):
            sys.exit(f"Defina a variável de ambiente {v}.")

    sc.TURMA_T5 = args.turma_t5
    sc.MATERIAL_T5 = args.material_t5
    sc.MODO_T5 = args.modo_t5
    sc.MARCADORES["T5"] = ["Turma Virtual", "Notícia"] if args.modo_t5 == "noticia" else ["Turma Virtual", args.material_t5]

    SAIDA_WAVE.mkdir(parents=True, exist_ok=True)
    linhas_resumo = []

    with sync_playwright() as pw:
        s = sc.Sessao(pw, "chromium", "computador", canal="chrome")
        try:
            s.login()
            for t in args.tarefas:
                reg = sc.executar_com_repeticao(s, t)
                if reg.get("erro") or not reg.get("marcadores_ok"):
                    raise RuntimeError(f"Falha ao chegar à página final de {t}: {reg.get('erro')}")
                rel = executar_wave_na_pagina(s.pg, wave_js)
                st = rel["statistics"]
                erros_gerais = st["error"]
                erros_contraste = st["contrast"]
                erros_total = erros_gerais + erros_contraste
                alertas = st["alert"]
                agora = dt.datetime.now().isoformat(timespec="seconds")
                nome_arq = f"{t}-wave.json"
                documento = {
                    "tarefa": t,
                    "pagina": PAGINAS_M9[t],
                    "data_hora": agora,
                    "avaliador": args.avaliador,
                    "navegador": f"Google Chrome {s.versao}",
                    "sistema": f"{platform.system()} {platform.release()}",
                    "ferramenta": f"WAVE Evaluation Tool {args.wave_versao}",
                    "versao_sigaa": (reg.get("assinatura") or {}).get("versao"),
                    "url_final": reg.get("url_final"),
                    "erros_gerais": erros_gerais,
                    "erros_contraste": erros_contraste,
                    "erros_total_wcag_a_aa": erros_total,
                    "alertas": alertas,
                    "wave": rel,
                }
                (SAIDA_WAVE / nome_arq).write_text(
                    json.dumps(documento, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
                linhas_resumo.append({
                    "tarefa": t,
                    "pagina": PAGINAS_M9[t],
                    "data": agora[:10],
                    "navegador": f"Google Chrome {s.versao}",
                    "erros": erros_total,
                    "alertas": alertas,
                    "relatorio": nome_arq,
                })
                print(
                    f"{t}: erros={erros_total} (gerais={erros_gerais}, contraste={erros_contraste}), alertas={alertas}",
                    flush=True,
                )
        finally:
            s.fechar()

    with (SAIDA_WAVE / "resumo.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["tarefa", "pagina", "data", "navegador", "erros", "alertas", "relatorio"])
        w.writeheader()
        w.writerows(linhas_resumo)

    media = sum(int(l["erros"]) for l in linhas_resumo) / len(linhas_resumo)
    print(f"M9 = {sum(int(l['erros']) for l in linhas_resumo)}/{len(linhas_resumo)} = {media:.2f} erros/página")


if __name__ == "__main__":
    main()
