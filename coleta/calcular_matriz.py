"""Consolida a matriz multiplataforma gravada por ``matriz_dispositivos.py``.

Produz:

- ``dados/consolidados/matriz-dispositivos.csv``: uma linha por perfil e página
  (login da UnB e T1 a T6), com conclusão da tarefa, escala, fonte mínima
  efetiva e os critérios (a) a (e) de M14 aplicados à largura do aparelho;
- ``dados/consolidados/matriz-resumo.csv``: uma linha por perfil.

Os critérios são os mesmos de M14 (``calcular.criterios``), com a largura do
perfil no lugar de 360/768 px. Em computador, a "adaptação" não se aplica
(o SIGAA foi feito para essa tela): registra-se só se a tarefa foi concluída e a
menor fonte. O resultado é dado complementar e não altera ``metricas.csv``.

Uso: ``python coleta/calcular_matriz.py``.
"""

from __future__ import annotations

import csv
import json
import statistics as st
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "dados/brutos/flexibilidade/automatizado/matriz.jsonl"
SAIDA = RAIZ / "dados/consolidados/matriz-dispositivos.csv"
RESUMO = RAIZ / "dados/consolidados/matriz-resumo.csv"
PAGINAS = ["login", "T1", "T2", "T3", "T4", "T5", "T6"]


def criterios(r: dict, w: int) -> dict[str, bool]:
    ad = r.get("adaptacao") or {}
    a = ad.get("largura_layout_px", 9e9) <= w + 1 and ad.get("largura_conteudo_px", 9e9) <= ad.get("largura_layout_px", 0) + 1
    b = ad.get("textos_menores_12px", 1) == 0
    c = ad.get("textos_sobrepostos", 1) == 0 and ad.get("textos_cobertos", 1) == 0 and ad.get("textos_cortados", 1) == 0
    d = r.get("toque_menu") in (True, None)
    usados = all((x.get("largura_px") or 0) >= 24 and (x.get("altura_px") or 0) >= 24 for x in r.get("alvos_usados", []))
    e = ad.get("alvos_abaixo_24px", 1) == 0 and usados
    return {"a": a, "b": b, "c": c, "d": d, "e": e}


def sim(v) -> str:
    return "" if v is None else ("sim" if v else "não")


def main():
    regs = [json.loads(l) for l in ENTRADA.read_text(encoding="utf-8").splitlines() if l.strip()]
    ultimo: dict[tuple[str, str], dict] = {}
    for r in regs:  # o último registro de cada perfil e página vale (coleta refeita substitui)
        if r.get("perfil") and r.get("tarefa"):
            ultimo[(r["perfil"], r["tarefa"])] = r
    perfis = list(dict.fromkeys(r["perfil"] for r in regs if r.get("perfil") and r.get("tarefa")))
    ordem_cat = {"Computador": 0, "Celular": 1, "Tablet": 2}
    cat = {r["perfil"]: r.get("categoria") for r in regs if r.get("categoria")}
    ordem = {p: i for i, p in enumerate(perfis)}
    perfis.sort(key=lambda p: (ordem_cat.get(cat.get(p), 9), ordem[p]))
    linhas, resumo = [], []
    for p in perfis:
        regs_p = [ultimo[(p, t)] for t in PAGINAS if (p, t) in ultimo]
        if not regs_p:
            continue
        base = regs_p[0]
        movel = base["categoria"] != "Computador"
        w = base["largura_css_px"]
        concl, adapt, esperas, fontes, escalas, toque = [], [], [], [], [], []
        for r in regs_p:
            ad = r.get("adaptacao") or {}
            ok = r.get("login_ok") if r["tarefa"] == "login" else bool(r.get("marcadores_ok"))
            c = criterios(r, w) if ad else None
            adaptada = all(c.values()) if (c and movel) else None
            espera = round(sum((x.get("load_ms") or 0) for x in r.get("passos", [])) / 1000, 2) if r.get("passos") else None
            linhas.append({
                "perfil": p, "categoria": base["categoria"], "sistema": base["sistema_emulado"],
                "aparelho": base["aparelho"], "navegador": base["navegador"], "versao": base.get("navegador_versao", ""),
                "largura_css_px": w, "pagina": r["tarefa"], "concluiu": sim(ok),
                "url_final": r.get("url_final", ""), "escala_visual": round(ad.get("escala_visual", 0), 3) if ad else "",
                "largura_layout_px": ad.get("largura_layout_px", ""), "meta_viewport": "sim" if ad.get("meta_viewport") else "não",
                "fonte_minima_efetiva_px": ad.get("fonte_minima_efetiva_px", ""),
                "textos_menores_12px": ad.get("textos_menores_12px", ""), "textos": ad.get("textos", ""),
                "alvos_abaixo_24px": ad.get("alvos_abaixo_24px", ""),
                "menu_abriu_ao_toque": sim(r.get("toque_menu")) if movel else "",
                **{f"crit_{k}": (sim(v) if movel else "") for k, v in (c or {k: None for k in "abcde"}).items()},
                "adaptada": sim(adaptada), "espera_s": espera if espera is not None else "",
                "data": r.get("data_hora", "")[:10], "evidencia": r.get("evidencia") or "",
            })
            if r["tarefa"] != "login":
                concl.append(ok)
                if adaptada is not None:
                    adapt.append(adaptada)
                if espera is not None:
                    esperas.append(espera)
                if ad:
                    fontes.append(ad.get("fonte_minima_efetiva_px") or 0)
                    escalas.append(ad.get("escala_visual") or 0)
                if movel and r.get("toque_menu") is not None:
                    toque.append(r["toque_menu"])
        login = ultimo.get((p, "login"), {})
        ad_l = login.get("adaptacao") or {}
        resumo.append({
            "perfil": p, "categoria": base["categoria"], "sistema": base["sistema_emulado"], "aparelho": base["aparelho"],
            "navegador": base["navegador"], "versao": base.get("navegador_versao", ""), "largura_css_px": w,
            "login_ok": sim(login.get("login_ok")), "tarefas_concluidas": sum(concl), "tarefas": len(concl),
            "paginas_adaptadas": sum(adapt) if movel else "", "paginas_avaliadas": len(adapt) if movel else "",
            "login_adaptado": sim(all(criterios(login, w).values())) if (movel and ad_l) else "",
            "login_cabe_na_tela": sim(all(criterios(login, w)[k] for k in "abe")) if (movel and ad_l) else "",
            "escala_mediana": round(st.median(escalas), 3) if escalas else "",
            "fonte_minima_px": round(min(fontes), 2) if fontes else "",
            "fonte_minima_login_px": ad_l.get("fonte_minima_efetiva_px", ""),
            "menus_ao_toque": f"{sum(toque)} de {len(toque)}" if toque else "",
            "espera_mediana_s": round(st.median(esperas), 2) if esperas else "",
        })
    for caminho, dados in ((SAIDA, linhas), (RESUMO, resumo)):
        with caminho.open("w", newline="", encoding="utf-8") as f:
            w_ = csv.DictWriter(f, fieldnames=list(dados[0]))
            w_.writeheader()
            w_.writerows(dados)
        print(caminho.relative_to(RAIZ), len(dados), "linhas")


if __name__ == "__main__":
    main()
