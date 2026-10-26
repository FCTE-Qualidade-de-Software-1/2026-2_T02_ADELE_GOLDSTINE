# Questões

As questões representam o **nível operacional** do GQM. Cada questão caracteriza um atributo do foco de qualidade do objetivo correspondente, de modo que o conjunto de questões de um objetivo cubra todos os atributos declarados nele (Tabelas 1 a 3). Com exceção da satisfação (Q13), cada atributo é uma subcaracterística da ISO/IEC 25010:2023 [1].

Cada questão é respondida por exatamente uma métrica, e cada métrica responde a exatamente uma questão. Quando um atributo é observado por duas métricas, ele recebe duas questões, cada uma sobre um aspecto diferente do atributo (por exemplo, Q6 e Q7, ambas de operabilidade).

## G1 - Adequação Funcional

*Tabela 1 - Questões do objetivo G1 - Adequação Funcional.*

| ID | Questão | Atributo do foco de qualidade |
| -- | ------- | ----------------------------- |
| Q1 | O SIGAA oferece as funções de que o estudante precisa para consultar sua situação acadêmica, planejar o fluxo e emitir documentos? | Completude funcional |
| Q2 | As informações exibidas pelo SIGAA nas tarefas do escopo estão corretas? | Correção funcional |
| Q3 | As funções do SIGAA são suficientes para que o estudante planeje seu fluxo sem depender de ferramentas externas? | Pertinência funcional |

A Fase 1 descreve a pertinência funcional (*functional appropriateness*, chamada de adequação na [adaptação do modelo de qualidade](../fase-1/modelo-qualidade.md#2-adaptacoes-ao-contexto-do-sigaa)) como a conclusão das tarefas sem passos desnecessários. Q3 a observa pelo indício registrado em OP-07: quando as funções não bastam, o estudante recorre a ferramentas externas. Os passos desnecessários dentro do próprio SIGAA são tratados em Q7, pelo desvio de caminho (M7).

## G2 - Capacidade de Interação (Usabilidade)

*Tabela 2 - Questões do objetivo G2 - Capacidade de Interação.*

| ID | Questão | Atributo do foco de qualidade |
| -- | ------- | ----------------------------- |
| Q4 | O estudante identifica onde está a função de que precisa? | Reconhecimento de adequação |
| Q5 | O estudante consegue concluir as tarefas sem ajuda, inclusive no primeiro contato com o sistema? | Apreensibilidade |
| Q6 | A navegação permite concluir as tarefas sem demora excessiva em relação a um usuário experiente? | Operabilidade |
| Q7 | A navegação leva o estudante até a função sem passos desnecessários? | Operabilidade |
| Q8 | O estudante consegue se recuperar quando comete um erro, sem perder o que já fez? | Proteção contra erros do usuário |
| Q9 | O sistema trata situações de erro previsíveis, como a expiração da sessão ou o uso do botão Voltar, sem obrigar o estudante a recomeçar a tarefa? | Proteção contra erros do usuário |
| Q10 | As páginas do escopo atendem aos critérios de acessibilidade verificáveis por ferramenta automática? | Inclusividade |
| Q11 | As páginas do escopo podem ser usadas com teclado, leitor de tela e ampliação, aspectos que exigem inspeção manual? | Inclusividade |
| Q12 | O estudante compreende as informações exibidas sem consultar legenda ou ajuda externa? | Autodescritividade |
| Q13 | O estudante fica satisfeito ao usar o SIGAA nas tarefas de rotina? | Satisfação (qualidade em uso) |

A satisfação não é subcaracterística do modelo de qualidade de produto da ISO/IEC 25010:2023 [1]. Ela pertence ao modelo de qualidade em uso, que na versão de 2011 fazia parte da própria ISO/IEC 25010 [2]. Q13 foi mantida como medida complementar da percepção do estudante, que a Fase 1 aponta como origem das queixas mais frequentes, e por isso a satisfação está declarada no foco de qualidade de G2.

## G3 - Flexibilidade (Portabilidade)

*Tabela 3 - Questões do objetivo G3 - Flexibilidade.*

| ID | Questão | Atributo do foco de qualidade |
| -- | ------- | ----------------------------- |
| Q14 | As tarefas do escopo funcionam corretamente nos navegadores mais usados? | Adaptabilidade (ambiente de software) |
| Q15 | As páginas do escopo se adaptam a telas de celular e tablet e à interação por toque? | Adaptabilidade (ambiente de hardware) |
| Q16 | O estudante conclui as tarefas no celular com esforço semelhante ao do computador? | Adaptabilidade (ambiente de hardware) |

## Relação com as métricas

A métrica que responde a cada questão (Tabela 4) estão detalhadas na página [Métricas](metricas.md), e a hipótese de cada questão, na página [Hipóteses](hipoteses.md).

*Tabela 4 - Relação entre questões e métricas.*

| Questão | Métrica |
| ------- | ------- |
| Q1 | M1 |
| Q2 | M2 |
| Q3 | M3 |
| Q4 | M4 |
| Q5 | M5 |
| Q6 | M6 |
| Q7 | M7 |
| Q8 | M8 |
| Q9 | M20 |
| Q10 | M9 |
| Q11 | M10 |
| Q12 | M11 |
| Q13 | M12 |
| Q14 | M13 |
| Q15 | M14 |
| Q16 | M15 |

## Referências

[1] ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

[2] ISO/IEC 25010:2011. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 17/10/2026 | Definição das questões Q1 a Q9 | Felipe Campêlo |
| 1.2 | 18/10/2026 | Numeração e legendas de tabelas; classificação de Q6; referência à ISO/IEC 25010 | Felipe Campêlo |
| 2.0 | 18/10/2026 | Alinhamento à Fase 1 reestruturada: questões Q1 a Q14, uma por subcaracterística mantida, e questões de G4 | Felipe Campêlo |
| 2.1 | 18/10/2026 | Redação de Q6, Q10 e Q14 no nível do atributo, e não da métrica; coluna "Atributo do foco de qualidade" | Felipe Campêlo |
| 2.2 | 18/10/2026 | Integração da versão complementar: métrica M20 (cenários de erro) associada a Q7 e referência às hipóteses | Leonardo Bonetti |
| 2.3 | 25/10/2026 | Remoção das questões Q13 e Q14 do objetivo G4 (Eficiência de Desempenho) | Leonardo Bonetti |
| 2.4 | 25/10/2026 | Subcaracterística de Q3 nomeada pertinência funcional | Leonardo Bonetti |
| 2.5 | 25/10/2026 | Uma métrica por questão: Q6, Q7, Q8 e Q12 divididas por aspecto do atributo; questões renumeradas de Q1 a Q16; Tabela 4 em relação 1:1 | Leonardo Bonetti |
