# Gestão das contribuições

O esforço de cada integrante (indicador I3) vem de duas fontes, somadas pelo `esforco.py`:

| Fonte | O que cobre | Como entra |
|---|---|---|
| Histórico do Git e API do GitHub (automática) | Trabalho no repositório a partir da Entrega 2: textos, artigo, scripts, workflows, estilos e revisões de PR | Calculada a cada PR e a cada publicação do site, sem ação dos integrantes |
| `esforco.csv` (manual) | Trabalho que o Git não vê (reuniões, pesquisa, estudo) e as horas da Entrega 1 | Uma linha por sessão, com evidência |

A metodologia completa está em [`docs/contribuicao.md`](../docs/contribuicao.md).

## Estimativa automática

Para cada entrada na `main` (PR ou *commit* direto) depois da tag da entrega anterior, o script conta, por autor de cada *commit*:

- nos textos (`.md`, `.tex`, `.bib`), as **palavras realmente adicionadas** (`git log --word-diff`), sem contar a linha inteira quando só uma palavra mudou;
- no código (`.py`, `.yml`, `.css`, `.js`...), as **linhas adicionadas**.

O volume é convertido em horas pelas taxas de `TAXAS` em `esforco.py`. Cada revisor de um PR recebe ainda 0,25 h fixas mais as palavras dos seus comentários de revisão (`HORAS_POR_REVISAO`), lidas da API do GitHub pelo `gh`. O modelo IEEE copiado, PDFs, imagens e o próprio `esforco.csv` ficam de fora.

Em cada PR, a cada push e a cada revisão, o *workflow* `.github/workflows/esforco-pr.yml` comenta as horas estimadas e a participação de cada membro se o PR for integrado. O revisor valida a estimativa na revisão. O dashboard do site é recalculado a cada publicação (`deploy-pages.yml`).

Se um *commit* for feito com um e-mail que o script não conhece, o cálculo para com um erro: adicione o e-mail em `EMAILS` ou o login do GitHub em `LOGINS`.

## Registrar trabalho fora do repositório

**Não registre na planilha o trabalho que já está no Git** (páginas, artigo, código): ele já é contado automaticamente e seria somado duas vezes. Use `esforco.csv` só para reuniões, pesquisa, estudo e outras atividades sem *commit*. Edite em UTF-8, mantenha o cabeçalho e adicione uma linha por sessão:

| Campo | Como preencher |
|---|---|
| `entrega` | `E1` ou `E2` |
| `data` | Data no formato `dd/mm/aaaa` |
| `membro` | Nome completo, igual ao cadastrado em `MEMBROS` no `esforco.py` |
| `horas` | Horas-pessoa em decimal, por exemplo `1.50` |
| `categoria` | `pesquisa`, `reuniao` ou outra atividade sem artefato no Git (revisões feitas no GitHub já são contadas) |
| `descricao` | Trabalho realizado |
| `evidencia` | Ata, mensagem, rascunho, issue ou PR que comprove a atividade |
| `origem` | `registrada` (ou `estimada`/`declarada`, usadas na Entrega 1) |

Exemplo:

```csv
E2,09/11/2026,Felipe de Aquino Campêlo,1.00,reuniao,"Reunião de planejamento da Fase 3",ata de 09/11/2026,registrada
```

Use aspas em campos de texto que contenham vírgula. Registre reuniões para cada participante presente, usando a ata como evidência. Uma linha com membro, entrega, horas ou data inválidos interrompe o cálculo e a publicação do site, para que o dashboard nunca mostre um total errado.

## Calcular a participação

Na raiz do repositório, com o histórico completo do Git. Para incluir as revisões, o `gh` precisa estar autenticado (`gh auth login`); sem ele, o cálculo local segue sem as revisões e avisa. No GitHub Actions, uma falha da API interrompe o cálculo.

```bash
python gestao/esforco.py calcular --entrega E2              # tabela por membro e categoria
python gestao/esforco.py calcular --entrega E2 --detalhado  # cada registro, com a evidência
python gestao/esforco.py pr --base origin/main              # prévia do comentário do PR atual
```

A Entrega 1 continua reproduzível pelo método original: `python gestao/esforco.py estimar --ref cf12104` gera exatamente as linhas `estimada` da planilha.

Ao fim de cada entrega, crie a tag da *release* (`Entrega2`, ...): ela fecha o intervalo de *commits* da entrega e a próxima começa a partir dela.
