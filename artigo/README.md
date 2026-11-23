# Artigo - Entrega Final

Artigo do Projeto Final de FGA0315 Qualidade de Software 1, no **modelo IEEE para conferências** (IEEEtran), conforme a premissa 7 do roteiro.

- **PDF:** [`artigo.pdf`](artigo.pdf) (12 páginas com as referências, dentro do limite de 15 da premissa 9; sem apêndice)
- **Overleaf:** <https://www.overleaf.com/project/6b04809b6bd87c703701ebf4/share#ec4b766bf0e081e6b89f4427f7486bd96f1c4c0347d4e6d0>
- **Modelo original do IEEE:** [`modelo-ieee/`](modelo-ieee/) — pacote oficial IEEEtran v1.8b, sem alterações, obtido no CTAN em 19/10/2026 (<https://ctan.org/pkg/ieeetran>, arquivo <https://mirrors.ctan.org/macros/latex/contrib/IEEEtran.zip>). Contém a classe `IEEEtran.cls`, o modelo de conferência `bare_conf.tex`, o estilo de referências `bibtex/IEEEtran.bst` e os manuais `IEEEtran_HOWTO.pdf` e `bibtex/IEEEtran_bst_HOWTO.pdf`.

## Estrutura

| Arquivo/pasta | Conteúdo |
| ------------- | -------- |
| `artigo.tex` | Documento principal: artigo no formato `\documentclass[conference]{IEEEtran}` |
| `secoes/` | Resumo e seções (Introdução, Referencial teórico, Metodologia, Fases 1 a 4, Ação de melhoria e Conclusão) |
| `bibliografia.bib` | Referências, formatadas pelo `IEEEtran.bst` (manter alinhado com `docs/referencias.md`) |
| `IEEEtran.cls`, `IEEEtran.bst` | Cópias do modelo oficial, necessárias para compilar |
| `figuras/` | Imagens usadas no texto |

Conforme orientação da professora, o artigo não tem capa nem sumário: começa direto no título, autores, resumo e Introdução, e segue o formato IEEE sem alterações de margens, fontes ou espaçamento.

## Como compilar

**Overleaf:** envie a pasta `artigo/` compactada, defina `artigo.tex` como documento principal e use pdfLaTeX.

**Localmente:** `latexmk -pdf artigo.tex`, ou `pdflatex artigo`, `bibtex artigo`, `pdflatex artigo`, `pdflatex artigo`. Também compila com [Tectonic](https://tectonic-typesetting.github.io/) (`tectonic -X compile artigo.tex`), que usa XeLaTeX; nesse caso o preâmbulo troca as fontes do IEEEtran pelos equivalentes TeX Gyre (Termes, Heros e Cursor).

## Pacote para o Overleaf

Para gerar o `.zip` com tudo o que o Overleaf precisa (sem o PDF e sem o modelo original): `cd artigo && zip -r ../artigo-overleaf.zip artigo.tex secoes bibliografia.bib IEEEtran.cls IEEEtran.bst figuras`. Os números do artigo vêm de `dados/consolidados/` e da [Síntese e Conclusão](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_ADELE_GOLDSTINE/fase-4/sintese-final/) da GitPage.
