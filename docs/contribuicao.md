# Contribuição

Esta página registra as atividades e o percentual de esforço de cada membro em cada entrega. O esforço é medido em **horas-pessoa**, conforme o indicador I3 da [Gestão do Projeto](gestao-psm.md), e a seção 3 descreve como as horas foram obtidas. A mesma tabela está no Apêndice A do artigo.

## 1. Entrega 1 (Fases 1 e 2)

*Tabela 1 - Contribuição de cada membro na Entrega 1.*

| Membro | Matrícula | Atividades | Horas | Esforço (%) |
| ------ | :-------: | ---------- | :---: | :---------: |
| Arthur Carvalho Leite | 222037595 | Artigo no modelo IEEE (estrutura, redação das seções, diagrama GQM e compilação); [questionário com estudantes](fase-2/questionario.md) (itens, grupos por semestre, indicadores IQ1 a IQ6 e hipótese HP1); página de [gestão PSM/CID](gestao-psm.md) com a primeira medição; revisão de português da Fase 1 | 8,7 | 16,7 |
| Caio Melo Borges | 211030952 | Fase 1 completa: propósito e partes interessadas, software avaliado, modelo de qualidade, matriz Impacto x Risco, escopo e rigor, ODS; síntese da Fase 1; referências da Fase 1; capturas do SIGAA; integração do PR do artigo | 9,0 | 17,3 |
| Daniel Nunes Duarte | 211062910 | Apoio à equipe fora do repositório, principalmente na preparação e no dia da apresentação | 7,2 | 13,9 |
| Davi dos Santos Brito Nobre | 211062929 | Repositório, estrutura MkDocs e publicação da GitPage; primeira versão da Fase 1; integração do PR da Fase 1; organização da equipe, pesquisa e apoio às Fases 1 e 2 fora do repositório | 9,8 | 18,8 |
| Felipe de Aquino Campêlo | 231011328 | Fase 2: visão geral e rastreabilidade, objetivos G1 a G4, questões Q1 a Q14, métricas M1 a M19, primeira versão dos níveis de pontuação e gráficos GQM | 9,4 | 18,0 |
| Leonardo Fachinello Bonetti | 221022060 | Fase 2: métricas M20 e MA1, hipóteses H1 a H14 e HR1 a HR4, níveis de pontuação e critérios de julgamento, matriz de rastreabilidade, referências; integração do PR da Fase 2 | 8,0 | 15,3 |
| **Total** | | | **52,0** | **100,0** |

*Fonte: [`gestao/esforco.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/gestao/esforco.csv), calculado por `python gestao/esforco.py calcular --entrega E1`.*

!!! warning "Horas da Entrega 1 são estimadas"
    A planilha de esforço só foi adotada depois da Entrega 1 (decisão da medição 1 do indicador I3). As horas acima foram **reconstruídas a partir do histórico do repositório** pelo procedimento da seção 3.3. Cada membro deve conferir as próprias linhas na planilha e corrigi-las com evidência até a entrega; o percentual é recalculado pelo *script*.

Pelo critério de decisão do I3 (participação abaixo de 10% ou acima de 40% exige rebalanceamento), **todos os membros estão dentro da faixa**, entre 13,9% e 18,8%, e não há rebalanceamento a fazer.

## 2. Por que horas trabalhadas

A equipe avaliou três unidades para medir a contribuição:

*Tabela 2 - Alternativas de medida de esforço.*

| Medida | Vantagem | Problema neste projeto | Decisão |
| ------ | -------- | ---------------------- | ------- |
| *Issues* concluídas | Fácil de contar no GitHub | A equipe não usou *issues* na Entrega 1, e *issues* têm tamanhos muito diferentes (uma página de métricas não equivale a ajustar um link) | Descartada para a E1; adotada na E2 para o I1 e o I2, não para o esforço |
| *Commits* | Automático | Mede o hábito de *commit*, não o trabalho: Leonardo fez 9 *commits* em 4 minutos e Arthur enviou o artigo inteiro em 1. Reuniões, pesquisa e revisão não geram *commit* | Descartada |
| **Horas trabalhadas** | Mede o esforço de todas as atividades, inclusive as que não aparecem no Git; é a medida *Personnel Effort* do PSM/CID | Depende do registro de cada membro, que pode ser impreciso | **Adotada**, com validação por evidência (seção 3.2) |

## 3. Metodologia

### 3.1 Unidade e fórmula

A unidade é a **hora-pessoa**: uma hora de trabalho de um membro em uma atividade do projeto. O percentual de cada membro em uma entrega é:

> **Esforço do membro (%) = horas validadas do membro na entrega ÷ horas validadas de toda a equipe na entrega × 100**

Só entram no cálculo as horas validadas (seção 3.2). Os percentuais são arredondados para uma casa decimal pelo método dos maiores restos, para que a soma dê exatamente 100,0%.

### 3.2 Coleta automática (a partir da Entrega 2)

O registro manual de horas por sessão, previsto inicialmente para a Entrega 2, foi substituído por uma **estimativa paramétrica automática**, calculada pelo GitHub Actions a partir do histórico do repositório. É o mesmo método da Entrega 1 (seção 3.3), com duas melhorias. A coleta deixa de depender de cada membro lembrar de preencher a planilha, e a evidência de cada hora passa a ser o próprio PR ou *commit*.

**Não é contagem de *commits*.** A Tabela 2 descarta *commits* como medida porque o número de *commits* reflete o hábito de cada membro. Aqui o *commit* é só a fonte: o que se mede é o **volume adicionado** em cada um, e dividir o mesmo trabalho em 1 ou 9 *commits* produz as mesmas horas.

**Passo 1. Volume por integração.** Para cada entrada na `main` (PR ou *commit* direto) depois da tag da entrega anterior (`Entrega1` para a E2), o script soma, por autor de cada *commit* sem *merge*:

- nos textos (`.md`, `.tex`, `.bib`), as **palavras realmente adicionadas**, obtidas com `git log --word-diff`. Corrigir uma palavra num parágrafo de 200 conta 1 palavra, não 200 como no método da Entrega 1. Sinais de *markdown* sem letras nem números (`|`, `---`, `*`) não contam;
- no código e na configuração do site (`.py`, `.yml`, `.css`, `.js`), as **linhas adicionadas**, porque palavras não medem código.

Ficam de fora o modelo IEEE copiado, PDFs, imagens, documentos binários e a própria planilha de esforço.

**Passo 2. Conversão em horas.** O volume é dividido pela taxa da categoria:

*Tabela 3 - Taxas de produção a partir da Entrega 2.*

| Categoria | Arquivos | Taxa | Justificativa |
| --------- | -------- | :--: | ------------- |
| `redacao` | Textos fora de `artigo/` (páginas da GitPage, READMEs) | 1.100 palavras/h | Mesma taxa da Entrega 1 (Tabela 4) |
| `consolidacao` | Textos em `artigo/` | 2.200 palavras/h | Mesma taxa da Entrega 1 (Tabela 4) |
| `infraestrutura` | Código e configuração (`.py`, `.yml`, `.css`, `.js`) | 100 linhas/h | Scripts e estilos escritos com apoio de IA e revisados pelo autor. Taxa inicial, a ser calibrada pela equipe como as da Tabela 4 |
| `revisao` | Revisões e comentários de revisão dos PRs (API do GitHub) | 0,25 h por revisor em cada PR + 1.100 palavras/h dos comentários | Tempo fixo das revisões da Entrega 1 (Tabela 5), mais o texto escrito na revisão |

**Passo 3. Revisões de PR.** Revisar não adiciona texto ao repositório, então as revisões são lidas da API do GitHub. Cada membro que revisa um PR recebe **0,25 h fixas**, o mesmo valor atribuído às revisões da Entrega 1 (Tabela 5), mais as **palavras dos seus comentários de revisão** pela taxa de redação. Uma aprovação sem comentário vale 0,25 h, e uma revisão detalhada vale mais. O autor do PR não recebe horas de revisão pelas respostas no próprio PR, porque o trabalho dele já está nos *commits*.

**Passo 4. Trabalho fora do repositório.** Reuniões, pesquisa e estudo não geram *commit*. Eles continuam registrados em `gestao/esforco.csv`, uma linha por sessão, com a ata, a mensagem ou o rascunho como evidência. O trabalho que já está no Git não entra na planilha, para não ser contado duas vezes. As instruções de preenchimento estão em [`gestao/README.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/gestao/README.md).

**Passo 5. Validação no PR.** A cada PR e a cada revisão enviada, o *workflow* `esforco-pr.yml` comenta as horas estimadas de cada autor e revisor e a participação de cada membro na entrega se o PR for integrado, com alerta fora da faixa de 10% a 40% do I3. O revisor confere a estimativa junto com o conteúdo. Mais de 4 h de um membro num único PR exige justificativa na revisão, como o teto de plausibilidade da versão manual.

**Passo 6. Publicação.** A cada publicação do site, o [dashboard de contribuição](gestao-esforco.md) é recalculado com a planilha, o histórico do Git e as revisões dos PRs. Uma linha inválida na planilha, um *commit* de autor desconhecido ou uma falha na API do GitHub interrompem a publicação, para que o painel nunca mostre um total errado. No fechamento da entrega, o responsável pela gestão cria a tag da *release*, roda `python gestao/esforco.py calcular --entrega E2`, copia a tabela para esta página e para o apêndice do artigo, e registra o I3 na [Gestão do Projeto](gestao-psm.md).

### 3.3 Reconstrução das horas da Entrega 1

Como não havia registro de horas na Entrega 1, as horas foram estimadas por **estimativa paramétrica**: mede-se o volume de trabalho produzido por cada membro e converte-se em horas com uma taxa de produção fixa por tipo de artefato. O comando é `python gestao/esforco.py estimar --ref cf12104`.

**Passo 1. Volume de texto.** Para cada membro, somam-se as palavras de todas as linhas que ele adicionou nos arquivos de texto da equipe (`docs/`, `artigo/secoes/`, `artigo/artigo.tex` e `artigo/bibliografia.bib`), em todos os *commits* sem *merge* até `cf12104` (19/10/2026). Versões depois substituídas também contam, porque o esforço de escrevê-las existiu (é o caso da primeira versão da Fase 1, de Davi). Ficam de fora o modelo IEEE copiado do CTAN, PDFs, imagens e alterações só de espaçamento.

**Passo 2. Conversão em horas.** As taxas foram calibradas para refletir o tempo real disponível: os membros estudam e trabalham, e a Entrega 1 foi produzida em cerca de uma semana, com apoio de IA na redação. Com essas taxas, nenhum membro passa de 10 h na entrega.

*Tabela 4 - Taxas de produção usadas na estimativa.*

| Categoria | Arquivos | Taxa | Justificativa |
| --------- | -------- | :--: | ------------- |
| `redacao` | Páginas da GitPage (`docs/`) | 1.100 palavras/h | Texto original com pesquisa em normas e no SIGAA, redigido com apoio de IA e revisado pelo autor |
| `consolidacao` | Artigo em LaTeX (`artigo/`) | 2.200 palavras/h | Reescrita de conteúdo já produzido nas páginas, no formato do artigo (o dobro da taxa de redação) |

**Passo 3. Atividades sem texto.** Atividades que não geram palavras receberam horas fixas, ligadas a uma evidência no repositório ou declaradas pela equipe:

*Tabela 5 - Horas atribuídas a atividades sem texto.*

| Membro | Atividade | Horas | Evidência |
| ------ | --------- | :---: | --------- |
| Davi | Repositório, estrutura MkDocs e *workflow* da GitPage | 1,0 | *commit* `ef63af2` |
| Caio | 8 capturas de tela do SIGAA, com anonimização | 0,5 | *commit* `a311cc4` |
| Arthur | Configuração do IEEEtran, migração do abnTeX2, figuras e compilação | 1,0 | *commits* `1e073c7` e `ae19094` |
| Davi, Leonardo, Caio | Revisão e *merge* dos PRs #1, #2 e #3 | 0,25 cada | PRs #1, #2 e #3 |
| Davi | Trabalho sem registro no Git: organização da equipe, pesquisa e apoio às Fases 1 e 2. A equipe fixou o total de Davi em 9,8 h; esta linha é a diferença sobre as 2,83 h medidas no Git | 6,97 | Declaração da equipe |
| Daniel | Apoio à equipe sem registro no Git, principalmente na preparação e no dia da apresentação | 7,2 | Declaração da equipe |
| Caio | Ajuste definido pela equipe na revisão da tabela: o total de Caio foi fixado em 9,0 h, contra 9,78 h estimadas | −0,78 | Declaração da equipe |

**Passo 4. Sensibilidade.** As taxas são uma escolha da equipe, por isso o cálculo foi repetido com outras taxas:

*Tabela 6 - Esforço (%) da Entrega 1 com taxas diferentes (redação / consolidação, em palavras/h).*

| Taxas | Arthur | Caio | Daniel | Davi | Felipe | Leonardo |
| ----- | :----: | :--: | :----: | :--: | :----: | :------: |
| **1.100 / 2.200 (adotada)** | **16,7** | **17,3** | **13,9** | **18,8** | **18,0** | **15,3** |
| 800 / 1.600 | 17,8 | 19,0 | 11,0 | 15,9 | 19,7 | 16,6 |
| 1.500 / 3.000 | 15,6 | 15,5 | 16,9 | 22,1 | 16,1 | 13,8 |
| 1.100 / 1.100 (artigo igual às páginas) | 22,1 | 16,2 | 12,9 | 17,7 | 16,8 | 14,3 |

Entre os membros com trabalho medido no Git, mudar as taxas mantendo a proporção entre elas altera os percentuais em até 1,9 ponto percentual. Os percentuais de Daniel e Davi variam mais (11,0% a 16,9% e 15,9% a 22,1%) porque a maior parte das horas deles é declarada e não depende das taxas. Em todos os cenários, todos os membros ficam entre 10% e 40%. Tratar o artigo como texto original favorece Arthur; a equipe considera que o artigo consolida o conteúdo das páginas, o que justifica a taxa maior.

### 3.4 Limitações

- **Uso de IA.** Vários membros usaram IA na redação (ver [Uso de IA](uso-de-ia.md)), o que aumenta as palavras por hora. As taxas já consideram esse apoio, e como são as mesmas para todos, a proporção entre os membros se mantém.
- **Trabalho fora do Git.** Reuniões, conversas no grupo e pesquisa sem *commit* não aparecem na contagem de palavras. Na Entrega 1, esse trabalho foi incluído por declaração da equipe (casos de Davi e Daniel); a partir da Entrega 2, ele entra pela planilha, com evidência (mensagens, ata, rascunho).
- **Volume não é qualidade.** Palavras e linhas medem esforço de produção, não o valor do conteúdo. Por isso a estimativa de cada PR é validada pelo revisor (seção 3.2, passo 5).
- **Autoria do *commit*.** A estimativa automática credita o autor de cada *commit*. Trabalho feito em par, ou enviado por outro membro, precisa ser ajustado na planilha com evidência.
- **Revisão de PRs.** O tempo fixo de 0,25 h não distingue uma revisão rápida de uma revisão longa sem comentários. Revisões feitas fora do GitHub (por exemplo, numa chamada) entram na planilha, com o PR como evidência.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 19/10/2026 | Tabela de contribuição da Entrega 1, com as atividades de cada membro | [arthurlleite](https://github.com/arthurlleite) |
| 1.2 | 24/10/2026 | Metodologia de esforço por horas trabalhadas, estimativa das horas da Entrega 1 e percentuais | Caio Borges |
| 1.3 | 24/10/2026 | Taxas calibradas para no máximo 10 h por membro e inclusão do trabalho de Davi fora do repositório | Caio Borges |
| 1.4 | 24/10/2026 | Horas declaradas pela equipe para Daniel e Davi e ajuste das horas de Caio | Caio Borges |
| 1.5 | 03/11/2026 | Matrícula de Caio, descrição das horas declaradas de Davi e Caio e correção da análise de sensibilidade | Caio Borges |
| 1.6 | 10/11/2026 | Coleta automática do esforço a partir da Entrega 2 (palavras e linhas adicionadas por PR e revisões dos PRs, calculadas pelo GitHub Actions) | Caio Borges |
