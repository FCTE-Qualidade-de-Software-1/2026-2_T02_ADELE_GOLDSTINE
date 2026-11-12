# Fase 3 - Projeto da Avaliação

Esta fase corresponde à terceira atividade do processo de avaliação de produto da **ISO/IEC 25040** [1], na qual a avaliação é projetada: para cada métrica especificada na [Fase 2](../fase-2/index.md), definem-se o método de coleta, os instrumentos, os recursos, o ambiente e o cronograma. O resultado é o plano seguido na Fase 4.

A Fase 2 deixou três itens para esta fase: o formato dos arquivos de dados, os instrumentos e o roteiro de execução, e o acesso às gravações ([Métricas, artefatos de dados previstos](../fase-2/metricas.md#artefatos-de-dados-previstos)). Os dois primeiros estão nas páginas da Tabela 1, e o acesso às gravações está em [Recursos e Ambiente](recursos-ambiente.md#5-gravacoes).

*Tabela 1 - Páginas da Fase 3.*

| Página | Conteúdo |
| ------ | -------- |
| [Protocolo do Teste com Usuários](teste-usuarios.md) | Participantes, roteiro da sessão, enunciados das tarefas, ordem, registro e SUS |
| [Planilhas de Coleta](planilhas.md) | Formato de cada arquivo de dados e convenções de preenchimento |
| [Recursos e Ambiente](recursos-ambiente.md) | Produto avaliado, hardware e software por método, pessoas e conhecimento exigido, massa de dados e gravações |

*Fonte: elaboração da equipe.*

## 3.1 Métodos de coleta

As métricas são obtidas por três métodos, já previstos nos [instrumentos de coleta da Fase 2](../fase-2/index.md#23-instrumentos-de-coleta).

*Tabela 2 - Métodos de coleta.*

| Método | Métricas | Quem executa | Fonte do procedimento |
| ------ | -------- | ------------ | --------------------- |
| Teste com usuários | M4, M5, M6, M7, M8, M11, M12 e MA1 | Moderador e avaliador da gravação, com 6 estudantes | [Protocolo do Teste com Usuários](teste-usuarios.md) |
| Questionário online | M3 e lista de referência de M1 | Estudantes de graduação, de forma anônima | [Questionário](../fase-2/questionario.md) |
| Inspeção pela equipe | M1, M2, M9, M10, M13, M14, M15 e M20 | Dois avaliadores independentes e um terceiro para divergências, nas métricas em que a ficha o exige | Fichas das métricas em [Métricas](../fase-2/metricas.md) |

*Fonte: elaboração da equipe.*

## 3.2 Rastreabilidade com a Fase 2

A Tabela 3 liga cada métrica ao instrumento que a coleta e ao arquivo em que o dado bruto fica registrado. Assim, cada valor calculado na Fase 4 pode ser conferido até a sua origem.

*Tabela 3 - Métrica, instrumento e arquivo de dados.*

| Métrica | Instrumento | Arquivo de dados |
| ------- | ----------- | ---------------- |
| M1 | Lista de referência verificada por dois avaliadores | `inspecao/funcoes.csv` |
| M2 | Conferência com o PPC, o calendário e os documentos do próprio SIGAA | `inspecao/correcao.csv` |
| M3 | Questionário online, item F1 | `questionario/respostas.csv` |
| M4 | Gravações, comparadas com os itens válidos de primeira escolha | `testes-usuarios/sessoes.csv` e `referencia/caminhos.csv` |
| M5 | Formulário de observação do moderador | `testes-usuarios/sessoes.csv` |
| M6 | Gravações e tempos do especialista | `testes-usuarios/sessoes.csv` e `referencia/tempos-especialista.csv` |
| M7 | Gravações e caminho mais curto | `testes-usuarios/sessoes.csv` e `referencia/caminhos.csv` |
| M8 | Gravações, um registro por erro | `testes-usuarios/erros.csv` |
| M9 | Extensão WAVE | `acessibilidade/wave/resumo.csv` e relatórios |
| M10 | Inspeção manual com teclado, zoom e leitor de tela | `inspecao/acessibilidade-manual.csv` |
| M11 | Perguntas de compreensão de T2, T4 e T6 | `testes-usuarios/compreensao.csv` |
| M12 | Questionário SUS | `testes-usuarios/sus.csv` |
| M13 | Matriz de 6 tarefas × 4 navegadores | `flexibilidade/navegadores.csv` |
| M14 | Verificação das páginas em 360 px e 768 px | `flexibilidade/paginas-adaptadas.csv` |
| M15 | Execução das tarefas no computador e no celular | `flexibilidade/tempos-celular.csv` |
| M20 | Roteiro dos cenários de erro C1 a C6 | `inspecao/cenarios-erro.csv` |
| MA1 | Formulário de observação do moderador | `testes-usuarios/sessoes.csv` |

*Fonte: elaboração da equipe. Os arquivos ficam em `dados/brutos/`, exceto os de `referencia/`, que ficam em `dados/referencia/`.*

## Referências

[1] ISO/IEC 25040:2024. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality evaluation framework*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 10/11/2026 | Criação da fase: métodos de coleta, rastreabilidade entre métricas, instrumentos e arquivos de dados | Leonardo Bonetti |
| 1.1 | 12/11/2026 | Página de Recursos e Ambiente na Tabela 1; acesso às gravações remetido a ela | [Felipe Campêlo](https://github.com/felipeacampelo) |
