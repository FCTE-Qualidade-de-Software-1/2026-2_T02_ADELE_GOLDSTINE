# Síntese dos Resultados e Conclusão

<!-- Critérios F4-C3 a F4-C5 e seção de conclusão do artigo: resultado de cada métrica, hipóteses, julgamento, melhorias e conclusão da avaliação. -->

Esta página reúne, em gráficos, o resultado das quatro fases: o valor e o nível de cada uma das 16 métricas, o que cada hipótese previa e o que foi medido, o julgamento das três características, os dados complementares de desempenho e a [matriz multiplataforma](matriz-multiplataforma.md). Termina com a conclusão da avaliação, as melhorias recomendadas e o que fica para trabalhos futuros. O detalhamento de cada resultado está em [Julgamento da Avaliação](julgamento.md); os valores vêm de [`dados/consolidados/metricas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/dados/consolidados/metricas.csv), e os gráficos são gerados por [`coleta/graficos_finais.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/blob/main/coleta/graficos_finais.py) a cada publicação da GitPage. Passe o mouse sobre os pontos e as barras para ver os valores.

## 1. As 16 métricas

Cada métrica foi comparada às faixas fixadas na Fase 2, antes da coleta ([Níveis de Pontuação](../fase-2/niveis-pontuacao.md#faixas-por-metrica)). As faixas têm a mesma largura no gráfico, e o ponto fica na posição do valor dentro da sua faixa.

[[GRAFICO_FINAL:metricas]]

*Figura 1 - Valor e nível das 16 métricas, por característica. Fonte: elaboração da equipe.*

*Tabela 1 - Distribuição dos níveis das 16 questões.*

| Nível | Questões | Total | Percentual |
| ----- | -------- | :---: | :--------: |
| Excelente (3) | Q14 (M13) | 1 | 6,25% |
| Bom (2) | Q2 (M2), Q5 (M5), Q8 (M8), Q9 (M20) | 4 | 25,0% |
| Regular (1) | Q1 (M1), Q4 (M4), Q7 (M7), Q12 (M11), Q16 (M15) | 5 | 31,25% |
| Insatisfatório (0) | Q3 (M3), Q6 (M6), Q10 (M9), Q11 (M10), Q13 (M12), Q15 (M14) | 6 | 37,5% |

*Fonte: elaboração da equipe.*

Duas em cada três questões ficaram em Regular ou Insatisfatório. Os resultados Bons e Excelentes estão no que o SIGAA **faz** (as funções existem, os dados estão corretos, as tarefas terminam e funcionam em qualquer navegador de computador); os Insatisfatórios, em **como** ele faz: o tempo, a satisfação, a acessibilidade e a tela do celular.

## 2. Hipóteses: o previsto e o obtido

Cada questão tinha uma hipótese, escrita na Fase 2 a partir das observações preliminares da Fase 1. O círculo vazio é o nível previsto e o cheio, o obtido; quando coincidem, a hipótese foi confirmada.

[[GRAFICO_FINAL:hipoteses]]

*Figura 2 - Nível previsto e nível obtido em cada hipótese. Fonte: elaboração da equipe.*

Foram **7 hipóteses confirmadas (43,75%)** e **9 refutadas (56,25%)**; nenhuma ficou inconclusiva. Das nove refutadas, cinco erraram para pior (H2, H3, H6, H11 e H13) e quatro para melhor (H5, H8, H9 e H14). H5 foi refutada pelo recorte dos calouros: eles concluíram 10 de 12 tentativas (83,3%), e não menos de 65%, como previsto; a diferença entre os grupos está na satisfação (SUS de 22,5 no começo do curso contra 39,2 no meio ou fim). As refutações para pior estão no tempo, na satisfação, na acessibilidade manual e no uso de ferramentas externas: a equipe esperava um SIGAA "usável, porém trabalhoso", e os dados mostram que ele é mais demorado, menos satisfatório e mais dependente do mouse do que isso.

## 3. Julgamento das características

O julgamento segue as três etapas da Fase 2: a questão recebe o nível da sua métrica; o objetivo, a média das questões; e a característica **atende** com média de pelo menos 2 e nenhuma questão Insatisfatória, **não atende** com média abaixo de 1 e **atende parcialmente** nos demais casos. Não há nota única para o SIGAA.

[[GRAFICO_FINAL:objetivos]]

*Figura 3 - Média dos níveis das questões e julgamento de cada característica. Fonte: elaboração da equipe.*

| Característica | Média | Julgamento | O que pesou |
| -------------- | :---: | ---------- | ----------- |
| Capacidade de Interação (G2) | 0,90 | **Não atende** | Tempo 4,39 vezes o do especialista, SUS de 32,5, 13,17 erros de acessibilidade por página e menu principal inacessível pelo teclado |
| Adequação Funcional (G1) | 1,00 | **Atende parcialmente** | Dados corretos (97%), mas 3 de 5 estudantes planejam o curso fora do SIGAA |
| Flexibilidade (G3) | 1,33 | **Atende parcialmente** | 100% nos navegadores de computador, 0% de páginas adaptadas ao celular |

As hipóteses de relação ficaram assim: **HR1 (Flexibilidade → Capacidade de Interação) estabelecida, com ressalva** (no celular, as tarefas levam 1,59 vez o tempo do computador, com as maiores razões nas páginas de tabela e menu: T2, T5 e T6) e **HR2 (Capacidade de Interação → Adequação Funcional) não estabelecida** (MA1 = 0: ninguém concluiu que uma função existente não existia; quem não achou desistiu ou saiu do SIGAA).

## 4. Dados complementares de desempenho

Eficiência de Desempenho saiu da especificação na Fase 2 e não tem nível, mas os mesmos *scripts* mediram a espera pelo sistema em cada tarefa ([Desempenho](desempenho.md)).

[[GRAFICO_FINAL:desempenho]]

*Figura 4 - Espera pelo sistema em cada tarefa, no computador e no celular em 4G. Fonte: elaboração da equipe, a partir de `dados/consolidados/desempenho.csv`.*

No computador, todas as tarefas ficaram entre 0,6 e 2,1 s. No celular em 4G, a espera multiplica por 2,5 a 8,9 vezes, e duas tarefas passam do limite de 10 s em que o usuário perde a atenção: a Turma Virtual (19,0 s, com cerca de 1,9 MB) e o calendário (10,1 s). O mesmo estudante que encontra páginas não adaptadas no celular (M14) espera mais por elas.

## 5. Conclusão

A avaliação respondeu à pergunta da Fase 1 com evidências: **o SIGAA entrega o que o estudante precisa, mas a um custo alto de tempo, esforço e satisfação, e não foi feito para o celular, que é o aparelho que todos os participantes usam.**

1. **O núcleo funcional é sólido.** As funções das seis tarefas existem (M1 = 100% por tarefa), os dados acadêmicos estão corretos (M2 = 97%, sem erro em item crítico), 83,3% das tentativas terminam sem ajuda (M5) e as tarefas funcionam em todos os navegadores de computador (M13 = 100%). Na [matriz multiplataforma](matriz-multiplataforma.md), todas as tarefas também foram concluídas nos sete navegadores e nos 20 perfis de sistema e aparelho.
2. **O custo está na interação.** O estudante leva 4,39 vezes o tempo de um usuário experiente (M6), dá 46% mais cliques que o caminho mínimo (M7), lê corretamente sem legenda só metade das informações (M11) e dá ao sistema 32,5 pontos no SUS (M12), metade da média de referência de 68.
3. **A acessibilidade exclui.** São 13,17 erros automáticos por página (M9) e só 54,2% dos critérios manuais atendidos (M10): sem mouse, o menu Ensino não recebe foco, e as tarefas T1, T3, T4 e T6 não começam.
4. **O celular é o ponto mais crítico.** Nenhuma página se adapta (M14 = 0 de 12): sem `<meta viewport>`, o layout de 980 px é reduzido a 37% a 49% da escala no celular, e o texto chega a 2,9 px. A matriz multiplataforma mostra que isso vale para Android, iOS e iPadOS, em todos os navegadores e tamanhos de tela (0 de 60 páginas adaptadas), enquanto a página de login da UnB, do mesmo percurso, já é responsiva (10 de 10).
5. **T6 e T4 são as tarefas a corrigir primeiro.** O link do calendário no portal leva à Pós-Graduação (3 de 5 caíram nele), e a carga horária pendente, embora esteja na página inicial, não é percebida (2 de 5 desistiram).

## 6. Melhorias

### 6.1 Melhoria executada

A equipe construiu o [Protótipo Mobile-First](prototipo-mobile.md) (360 px), navegável de T1 a T6, que trata a característica e as tarefas de pior resultado. Medido com os mesmos critérios e *scripts* aplicados ao SIGAA, o protótipo levou **M14 de 0 para 12 de 12** páginas adaptadas e **M9 de 13,17 para 0** erros por página, e T6 passa a ser feita em **um toque**, sem sair do SIGAA. O efeito no tempo e na satisfação não foi medido, porque não houve novo teste com usuários.

### 6.2 Melhorias recomendadas

*Tabela 2 - Melhorias recomendadas, por evidência e responsável.*

| Prioridade | Melhoria | Evidência | Para quem | Esforço estimado |
| :--------: | -------- | --------- | --------- | ---------------- |
| 1 | Declarar `<meta name="viewport" content="width=device-width, initial-scale=1">` e trocar a largura fixa de 980 px por um layout fluido nas páginas do portal do discente | M14 = 0/12; matriz: 0 de 60 páginas adaptadas em 10 perfis de celular e tablet; 5 de 5 usam o celular | STI/UnB | Médio: CSS das páginas do portal, sem mudança de regras de negócio |
| 2 | Tornar o menu principal acessível: foco do teclado, nome acessível e abertura por clique ou toque, e não só pela passagem do mouse | M10 = 54,2%; T1, T3, T4 e T6 não começam sem mouse; 2 de 5 relataram menu que não abre ao toque | STI/UnB | Baixo a médio: troca do JSCookMenu por um menu com ARIA |
| 3 | Corrigir o link "Calendário Acadêmico de Graduação" do painel e abrir o calendário vigente direto | T6: pior tarefa (índice 1,25); 3 de 5 caíram na página da Pós-Graduação | STI/UnB e SAA | Baixo: um link |
| 4 | Destacar a carga horária pendente e o percentual integralizado no topo do portal | T4: 60% de conclusão e 8,48 vezes o tempo do especialista | STI/UnB | Baixo |
| 5 | Mostrar o horário por extenso ao lado do código (24M34 → "Seg e Qua, 10h-11h50") | M11: 40% leram o código de T2 sem legenda | STI/UnB | Baixo |
| 6 | Corrigir os erros do WAVE: idioma da página, texto alternativo em 47 imagens, botões e campos sem rótulo e contraste | M9 = 13,17 erros/página; 37 na Turma Virtual | STI/UnB | Baixo a médio |
| 7 | Avisar quando a sessão expira, em vez de voltar ao portal sem mensagem | M20: único cenário não tratado (C1) | STI/UnB | Baixo |
| 8 | Reduzir o peso da Turma Virtual (carregar sob demanda) e reservar espaço para os painéis que deslocam a página | 19 s no celular em 4G; CLS de 1,05 | STI/UnB | Médio |
| 9 | Orientar calouros sobre o calendário, a integralização e o código de horário enquanto as correções não chegam | T4 e T6: 2 de 5 já precisaram de ajuda (IQ2) | DEG e coordenações | Baixo |
| 10 | Oferecer o planejamento do fluxo do curso (simulação de semestres e grade antes da matrícula) | M3 = 60% usam ferramenta externa; M1: faltam 4 funções de planejamento | STI/UnB | Alto |

*Fonte: elaboração da equipe.*

### 6.3 Trabalhos futuros

- **Novo teste com usuários no protótipo**, com os mesmos protocolo e tarefas, para medir o efeito da melhoria em M5, M6 e M12, que hoje é só projetado.
- **Teste em aparelhos reais de cada plataforma** (iPhone com Safari, Android de entrada e tablet), para confirmar a matriz feita por emulação, que não reproduz o sistema operacional nem o desempenho do aparelho.
- **Amostra maior e estratificada**, com estudantes de outros *campi* e estudantes com deficiência usando leitor de tela, para que os recortes por grupo tenham mais participantes.
- **Medição de desempenho nos picos de matrícula**, quando o servidor está sob carga.

## 7. Limitações

As limitações de cada método estão em [Julgamento da Avaliação](julgamento.md#7-limitacoes): amostra de cinco participantes recrutados por conveniência na FCTE; M14 e a matriz multiplataforma por emulação; inspeção com um avaliador automatizado e um humano; M15 com um avaliador; desempenho medido de um único ponto de rede, fora do horário de pico; e a impossibilidade de avaliar matrícula e trancamento sem alterar dados reais.

## Referências

[1] ISO/IEC 25040:2024. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality evaluation framework*.

[2] BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Wiley, 1994.

[3] NIELSEN, J. *Usability Engineering*. Morgan Kaufmann, 1993.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 23/11/2026 | Criação da página: gráficos das 16 métricas, das hipóteses, do julgamento e do desempenho; conclusão, melhorias recomendadas, trabalhos futuros e limitações | [arthurlleite](https://github.com/arthurlleite) |
