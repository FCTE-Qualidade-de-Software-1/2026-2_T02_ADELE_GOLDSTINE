# Artigo - Entrega 1

Artigo do Projeto Final de FGA0315 Qualidade de Software 1, no **modelo IEEE para conferências** (IEEEtran), conforme a premissa 7 do roteiro.

- **PDF:** [`artigo.pdf`](artigo.pdf) (9 páginas, dentro do limite de 15 da premissa 9)
- **Overleaf:** <https://www.overleaf.com/project/6adebc46cbee7aeb66190d80/share#d055fe4415c09eb12ae4905f6f1a72e9c10e86b94b7eb508>
- **Modelo original do IEEE:** [`modelo-ieee/`](modelo-ieee/) — pacote oficial IEEEtran v1.8b, sem alterações, obtido no CTAN em 19/10/2026 (<https://ctan.org/pkg/ieeetran>, arquivo <https://mirrors.ctan.org/macros/latex/contrib/IEEEtran.zip>). Contém a classe `IEEEtran.cls`, o modelo de conferência `bare_conf.tex`, o estilo de referências `bibtex/IEEEtran.bst` e os manuais `IEEEtran_HOWTO.pdf` e `bibtex/IEEEtran_bst_HOWTO.pdf`.

## Estrutura

| Arquivo/pasta | Conteúdo |
| ------------- | -------- |
| `artigo.tex` | Documento principal: artigo no formato `\documentclass[conference]{IEEEtran}` |
| `secoes/` | Resumo e seções (Introdução, Referencial teórico, Metodologia, Fase 1, Fase 2, Considerações) e apêndice de contribuição |
| `bibliografia.bib` | Referências, formatadas pelo `IEEEtran.bst` (manter alinhado com `docs/referencias.md`) |
| `IEEEtran.cls`, `IEEEtran.bst` | Cópias do modelo oficial, necessárias para compilar |
| `figuras/` | Imagens usadas no texto |

Conforme orientação da professora, o artigo não tem capa nem sumário: começa direto no título, autores, resumo e Introdução, e segue o formato IEEE sem alterações de margens, fontes ou espaçamento.

## Como compilar

**Overleaf:** envie a pasta `artigo/` compactada, defina `artigo.tex` como documento principal e use pdfLaTeX.

**Localmente:** `latexmk -pdf artigo.tex`, ou `pdflatex artigo`, `bibtex artigo`, `pdflatex artigo`, `pdflatex artigo`. Também compila com [Tectonic](https://tectonic-typesetting.github.io/) (`tectonic -X compile artigo.tex`), que usa XeLaTeX; nesse caso o preâmbulo troca as fontes do IEEEtran pelos equivalentes TeX Gyre (Termes, Heros e Cursor).

## Antes da entrega

Os percentuais de esforço de `secoes/07_apendice.tex` vêm de `python gestao/esforco.py calcular --entrega E1` (metodologia em `docs/contribuicao.md`). Se alguém corrigir as próprias horas em `gestao/esforco.csv`, rode o cálculo de novo e atualize o apêndice e a página Contribuição.
