# Gestão das contribuições

`esforco.csv` é a fonte única dos registros de esforço da equipe. Cada linha atribui horas a um integrante, entrega e atividade; a coluna `membro` determina a quem as horas são contabilizadas. Não mantenha uma segunda planilha de horas para evitar totais divergentes.

## Registrar ou corrigir uma contribuição

Edite `esforco.csv` em UTF-8 e mantenha o cabeçalho. Ao final de cada sessão de trabalho, adicione uma linha com os campos nesta ordem:

| Campo | Como preencher |
|---|---|
| `entrega` | Identificador, por exemplo `E2` |
| `data` | Data no formato `dd/mm/aaaa` |
| `membro` | Nome completo, igual ao cadastrado em `esforco.py` |
| `horas` | Horas-pessoa em decimal, por exemplo `1.50` |
| `categoria` | `redacao`, `pesquisa`, `revisao`, `integracao`, `reuniao`, `infraestrutura` ou `consolidacao` |
| `descricao` | Trabalho realizado e artefato relacionado |
| `evidencia` | Commit, PR, issue, ata ou outra evidência verificável |
| `origem` | `registrada`, `estimada` ou `declarada` |

Exemplo (substitua pelos dados reais da sessão):

```csv
E2,09/11/2026,Felipe de Aquino Campêlo,1.50,revisao,"Revisão das métricas da Fase 2",PR #12,registrada
```

Use aspas em campos de texto que contenham vírgula. Registre reuniões para cada participante presente, usando a ata como evidência. Corrija ou remova a linha original quando um registro estiver errado; não lance a mesma sessão duas vezes.

## Calcular a participação

Na raiz do repositório, rode:

```bash
python gestao/esforco.py calcular --entrega E2
```

O resultado soma as horas por integrante e categoria e calcula o percentual de cada pessoa sobre o total da entrega. Para a tabela geral, omita `--entrega E2`; para conferir a Entrega 1, use `--entrega E1`. Após revisar os números, atualize `docs/contribuicao.md` e o apêndice do artigo.

## Situação atual

Os registros existentes em `esforco.csv` são da Entrega 1 e incluem horas estimadas ou declaradas, identificadas pela coluna `origem`. Ainda não há registros da Entrega 2; lance apenas horas efetivamente trabalhadas e acompanhadas de evidência.

O código fornecido para a GitPage espera outra planilha (`dados/gestao/horas.csv`) e outros nomes de coluna. Este projeto mantém `esforco.csv` como fonte única no formato já usado pelo cálculo de contribuição.
