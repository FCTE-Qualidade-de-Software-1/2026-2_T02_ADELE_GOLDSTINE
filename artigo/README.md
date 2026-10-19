# Artigo - Entrega 1

Código-fonte LaTeX do artigo do Projeto Final de FGA0315 Qualidade de Software 1, no modelo abnTeX2 da FCTE/UnB.

## Como compilar

**Overleaf (recomendado):** envie a pasta `artigo/` compactada como novo projeto, defina `artigo.tex` como documento principal e use o compilador **pdfLaTeX**.

**Localmente (TeX Live ou MiKTeX com abnTeX2):**

```bash
cd artigo
latexmk -pdf artigo.tex
```

ou, sem `latexmk`: `pdflatex artigo`, `bibtex artigo`, `pdflatex artigo`, `pdflatex artigo`.

## Estrutura

| Pasta/arquivo | Conteúdo |
| ------------- | -------- |
| `artigo.tex` | Documento principal: ordem dos elementos pré-textuais, textuais e pós-textuais |
| `bibliografia.bib` | Referências (manter alinhado com `docs/referencias.md`) |
| `fixos/` | Classe, pacotes, comandos, capa, ficha catalográfica, listas e sumário |
| `editaveis/00_informacoes.tex` | Título, autores, disciplina, professora e palavras-chave |
| `editaveis/01_*` a `08_*` | Resumo, abstract, siglas, símbolos e capítulos |
| `editaveis/09_apendices.tex` | Apêndice A: tabela de contribuição (não conta no limite de páginas) |
| `figuras/` | Capa do modelo e figuras do texto |

## Antes da entrega

- Procure por `\pendente{` no código: os itens em vermelho (percentuais de esforço e atividades da tabela de contribuição) precisam ser preenchidos pela equipe.
- O roteiro limita o artigo a 15 páginas, incluindo referências, e pede um modelo SBC, ACM ou IEEE (premissas 7 e 9). Confirme com a professora se o modelo abnTeX2 com capa, folha de rosto e listas é aceito.
