# Planilhas de Coleta

Esta página define o formato de cada arquivo de dados da avaliação. Os arquivos foram previstos na [Tabela 19 de Métricas](../fase-2/metricas.md#artefatos-de-dados-previstos), que deixou o detalhamento para a Fase 3. Os modelos, só com o cabeçalho, já estão na pasta [`dados/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/tree/main/dados) do repositório.

## 1. Convenções

As convenções da Tabela 1 valem para todos os arquivos. Elas garantem que os dados de membros diferentes possam ser somados sem conversão.

*Tabela 1 - Convenções de preenchimento.*

| Item | Convenção |
| ---- | --------- |
| Formato | CSV em UTF-8, separado por vírgula, com o cabeçalho na primeira linha. Texto com vírgula vai entre aspas |
| Números | Ponto como separador decimal (ex.: `2.5`) |
| Datas | `AAAA-MM-DD` (ex.: `2026-11-16`) |
| Tempos | Em segundos inteiros (`tempo_s`). Marcações em vídeo em `mm:ss` |
| Sim e não | `sim` ou `nao`, sem acento e em minúsculas |
| Tarefas | `T1` a `T6`, conforme o [escopo da Fase 1](../fase-1/escopo.md#21-tarefas-representativas) |
| Participantes | `P1` a `P6`. A correspondência entre nome e código fica fora do repositório |
| Avaliadores | Primeiro nome do membro da equipe |
| Evidência | Caminho do arquivo de captura de tela no repositório, com dados pessoais cobertos, ou o minuto da gravação (`P3 04:12`) |

*Fonte: elaboração da equipe.*

## 2. Arquivos de referência

Os arquivos de referência são preenchidos **antes** do teste com usuários, porque M4, M6 e M7 dependem deles.

*Tabela 2 - Arquivos de referência.*

| Arquivo | Uma linha por | Colunas | Métricas |
| ------- | ------------- | ------- | -------- |
| `dados/referencia/caminhos.csv` | Passo de cada caminho válido de cada tarefa | `tarefa`; `caminho` (C1, C2...); `tipo` (`otimo` ou `alternativo`); `ordem` (1, 2...); `passo` (texto do link ou item clicado); `pagina_destino`; `classificacao_av1` e `classificacao_av2` (`necessario` ou `desnecessario`); `classificacao_final`; `evidencia` | M4, M7 |
| `dados/referencia/tempos-especialista.csv` | Execução do especialista | `tarefa`; `especialista`; `execucao` (1 a 3); `tempo_s`; `navegador`; `data`; `evidencia` | M6 |

*Fonte: elaboração da equipe.*

A partir de `caminhos.csv`: C<sub>min</sub> de uma tarefa é o maior valor de `ordem` no caminho `otimo`, e os itens válidos para a primeira escolha (M4) são os passos de `ordem` 1 de todos os caminhos da tarefa. Os tempos do especialista ficam num arquivo próprio, separado do `caminhos.csv` previsto na Tabela 19, porque têm uma linha por execução e não por passo.

## 3. Teste com usuários

*Tabela 3 - Arquivos do teste com usuários.*

| Arquivo | Uma linha por | Colunas | Métricas |
| ------- | ------------- | ------- | -------- |
| `dados/brutos/testes-usuarios/sessoes.csv` | Participante e tarefa (6 linhas por participante) | `participante`; `grupo` (`comeco` ou `meio_fim`); `semestre`; `prev_conclusao` (`sim`, `nao` ou `nao_sei`); `ordem` (posição da tarefa na sessão); `tarefa`; `ja_executou`; `inicio_video` e `fim_video` (`mm:ss`); `tempo_s`; `concluida`; `motivo_nao_conclusao` (`desistiu`, `pediu_ajuda`, `tempo_esgotado` ou `resultado_errado`); `cliques`; `primeira_escolha` (texto do item); `primeira_escolha_valida`; `erros`; `erros_recuperados`; `declarou_inexistente`; `declaracao` (fala literal); `moderador`; `avaliador_gravacao`; `data`; `observacoes` | M4, M5, M6, M7, M8, MA1 |
| `dados/brutos/testes-usuarios/erros.csv` | Erro observado na gravação | `participante`; `tarefa`; `erro` (1, 2...); `tempo_video`; `tipo` (`item_errado`, `dado_invalido`, `mensagem_sistema` ou `sessao_expirada`); `recuperado_sem_ajuda`; `refez_passos`; `recuperado` (`sim` só se recuperou sem ajuda e sem refazer passos); `descricao` | M8 |
| `dados/brutos/testes-usuarios/compreensao.csv` | Participante e pergunta (3 linhas por participante) | `participante`; `tarefa` (T2, T4 ou T6); `pergunta`; `resposta_dada`; `resposta_esperada`; `abriu_legenda_ajuda`; `tarefa_concluida`; `correta`; `avaliador` | M11 |
| `dados/brutos/testes-usuarios/sus.csv` | Participante | `participante`; `grupo`; `i1` a `i10` (1 a 5); `pontuacao` (0 a 100) | M12 |

*Fonte: elaboração da equipe.*

As colunas `erros` e `erros_recuperados` de `sessoes.csv` são as contagens das linhas de `erros.csv` da mesma tentativa. O detalhamento em `erros.csv` não estava na Tabela 19: ele foi acrescentado para que cada erro contado em M8 aponte para o minuto da gravação em que ocorreu.

Em `sessoes.csv`, `tempo_s` e `cliques` só são usados em M6 e M7 quando `concluida` = `sim`, conforme as fichas das métricas. `ja_executou` alimenta o recorte de calouros de M5.

## 4. Questionário

*Tabela 4 - Arquivo do questionário.*

| Arquivo | Uma linha por | Colunas | Métricas |
| ------- | ------------- | ------- | -------- |
| `dados/brutos/questionario/respostas.csv` | Resposta válida | `resposta` (R1, R2...); `data_hora`; `consentimento`; uma coluna por item da página [Questionário](../fase-2/questionario.md#3-itens-do-questionario), de `a1` a `f5` (o item C1.1 vira `c1_1`) | M3, M1 |

*Fonte: elaboração da equipe.*

A exportação do formulário é convertida para esses nomes de coluna. Respostas abertas (F2 a F5) são revisadas antes da publicação para retirar qualquer dado que identifique o respondente.

## 5. Inspeções

*Tabela 5 - Arquivos das inspeções.*

| Arquivo | Uma linha por | Colunas | Métricas |
| ------- | ------------- | ------- | -------- |
| `dados/brutos/inspecao/funcoes.csv` | Função da lista de referência | `funcao`; `origem` (`questionario`, `ferramenta` ou `tarefa`); `tarefa`; `existe_av1`, `evidencia_av1`, `existe_av2`, `evidencia_av2`; `existe_final`; `desempate` (nome do terceiro avaliador, se houve divergência) | M1 |
| `dados/brutos/inspecao/correcao.csv` | Atributo comparado | `verificacao` (V1, V2...); `tarefa`; `atributo`; `item_critico`; `fonte_oficial`; `valor_sigaa`; `valor_fonte`; `resultado_av1`, `resultado_av2` e `resultado_final` (`coincide` ou `diverge`); `evidencia` | M2 |
| `dados/brutos/inspecao/cenarios-erro.csv` | Cenário C1 a C6 | `cenario`; `tarefa`; `passos`; `tratado_av1`, `evidencia_av1`, `tratado_av2`, `evidencia_av2`; `tratado_final`; `desempate` | M20 |
| `dados/brutos/inspecao/acessibilidade-manual.csv` | Página e critério (4 linhas por página) | `tarefa`; `pagina`; `criterio` (a, b, c ou d da ficha de M10); `atende_av1`, `atende_av2`, `atende_final`; `navegador`; `leitor_tela`; `evidencia` | M10 |
| `dados/brutos/acessibilidade/wave/resumo.csv` | Página | `tarefa`; `pagina`; `data`; `navegador`; `erros`; `alertas`; `relatorio` (arquivo do relatório na mesma pasta) | M9 |

*Fonte: elaboração da equipe.*

O `resumo.csv` do WAVE não estava na Tabela 19, que previa só a pasta com os relatórios. Ele reúne as contagens usadas no cálculo de M9, e cada linha aponta para o relatório de origem. Os alertas são registrados, mas não entram na métrica.

## 6. Flexibilidade

*Tabela 6 - Arquivos de flexibilidade.*

| Arquivo | Uma linha por | Colunas | Métricas |
| ------- | ------------- | ------- | -------- |
| `dados/brutos/flexibilidade/navegadores.csv` | Combinação tarefa × navegador (24 linhas) | `tarefa`; `navegador`; `versao`; `sistema`; `resultado` (`sem_falha` ou `com_falha`); `tipo_falha`; `avaliador`; `data`; `evidencia` | M13 |
| `dados/brutos/flexibilidade/paginas-adaptadas.csv` | Página × largura (12 linhas) | `tarefa`; `pagina`; `largura_px` (360 ou 768); `dispositivo`; `crit_a` a `crit_e` (critérios da ficha de M14); `adaptada` (`sim` só se os cinco critérios forem atendidos); `avaliador`; `data`; `evidencia` | M14 |
| `dados/brutos/flexibilidade/tempos-celular.csv` | Avaliador e tarefa | `avaliador`; `tarefa`; `tempo_computador_s`; `tempo_celular_s`; `celular`; `navegador_celular`; `rede`; `data`; `evidencia` | M15 |

*Fonte: elaboração da equipe.*

## 7. Consolidação

*Tabela 7 - Arquivo consolidado.*

| Arquivo | Uma linha por | Colunas |
| ------- | ------------- | ------- |
| `dados/consolidados/metricas.csv` | Métrica e recorte | `metrica`; `recorte` (`geral`, `tarefa`, `grupo` ou `pagina`); `valor_recorte` (ex.: `T2`, `comeco`); `n` (quantidade de observações); `valor`; `nivel` (conforme [Níveis de Pontuação](../fase-2/niveis-pontuacao.md)); `observacao` |

*Fonte: elaboração da equipe.*

Só a linha `geral` de cada métrica entra no julgamento. Os demais recortes localizam os problemas, conforme a regra 3 de [Níveis de Pontuação](../fase-2/niveis-pontuacao.md#regra-3-resultados-por-perfil-por-pagina-e-por-tarefa).

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 10/11/2026 | Formato dos arquivos de dados da Tabela 19 de Métricas e convenções de preenchimento | Leonardo Bonetti |
