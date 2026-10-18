# Questões

As questões representam o **nível operacional** do GQM. Cada questão caracteriza um atributo do foco de qualidade do objetivo correspondente, de modo que o conjunto de questões de um objetivo cubra todos os atributos declarados nele (Tabelas 1 a 4). Com exceção da satisfação (Q10), cada atributo é uma subcaracterística da ISO/IEC 25010:2023 [1].

## G1 - Adequação Funcional

*Tabela 1 - Questões do objetivo G1 - Adequação Funcional.*

| ID | Questão | Atributo do foco de qualidade |
| -- | ------- | ----------------------------- |
| Q1 | O SIGAA oferece as funções de que o estudante precisa para consultar sua situação acadêmica, planejar o fluxo e emitir documentos? | Completude funcional |
| Q2 | As informações exibidas pelo SIGAA nas tarefas do escopo estão corretas? | Correção funcional |
| Q3 | As funções do SIGAA são suficientes para que o estudante planeje seu fluxo sem depender de ferramentas externas? | Adequação funcional (pertinência) |

A Fase 1 descreve a adequação funcional como a conclusão das tarefas sem passos desnecessários. Q3 a observa pelo indício registrado em OP-07: quando as funções não bastam, o estudante recorre a ferramentas externas. Os passos desnecessários dentro do próprio SIGAA são medidos em Q6, pelo desvio de caminho (M7).

## G2 - Capacidade de Interação (Usabilidade)

*Tabela 2 - Questões do objetivo G2 - Capacidade de Interação.*

| ID | Questão | Atributo do foco de qualidade |
| -- | ------- | ----------------------------- |
| Q4 | O estudante identifica onde está a função de que precisa? | Reconhecimento de adequação |
| Q5 | O estudante consegue concluir as tarefas sem ajuda, inclusive no primeiro contato com o sistema? | Apreensibilidade |
| Q6 | A navegação permite concluir as tarefas sem esforço desnecessário em relação a um usuário experiente? | Operabilidade |
| Q7 | O sistema evita que o estudante perca o que já fez quando comete um erro ou quando a sessão expira? | Proteção contra erros do usuário |
| Q8 | As páginas do escopo podem ser usadas por pessoas com deficiência? | Inclusividade |
| Q9 | O estudante compreende as informações exibidas sem consultar legenda ou ajuda externa? | Autodescritividade |
| Q10 | O estudante fica satisfeito ao usar o SIGAA nas tarefas de rotina? | Satisfação (qualidade em uso) |

A satisfação não é subcaracterística do modelo de qualidade de produto da ISO/IEC 25010:2023 [1]. Ela pertence ao modelo de qualidade em uso, que na versão de 2011 fazia parte da própria ISO/IEC 25010 [2]. Q10 foi mantida como medida complementar da percepção do estudante, que a Fase 1 aponta como origem das queixas mais frequentes, e por isso a satisfação está declarada no foco de qualidade de G2.

## G3 - Flexibilidade (Portabilidade)

*Tabela 3 - Questões do objetivo G3 - Flexibilidade.*

| ID | Questão | Atributo do foco de qualidade |
| -- | ------- | ----------------------------- |
| Q11 | As tarefas do escopo funcionam corretamente nos navegadores mais usados? | Adaptabilidade (ambiente de software) |
| Q12 | O SIGAA se adapta a telas de celular e tablet e à interação por toque? | Adaptabilidade (ambiente de hardware) |

## G4 - Eficiência de Desempenho

*Tabela 4 - Questões do objetivo G4 - Eficiência de Desempenho.*

| ID | Questão | Atributo do foco de qualidade |
| -- | ------- | ----------------------------- |
| Q13 | As páginas das tarefas carregam em tempo aceitável, em rede comum e em rede móvel? | Comportamento temporal |
| Q14 | As páginas das tarefas usam os recursos do cliente de forma compatível com o acesso por rede móvel e plano de dados limitado? | Utilização de recursos |

## Relação com as métricas

As métricas que respondem a cada questão (Tabela 5) estão detalhadas na página [Métricas](metricas.md), e a hipótese de cada questão, na página [Hipóteses](hipoteses.md).

*Tabela 5 - Relação entre questões e métricas.*

| Questão | Métricas |
| ------- | -------- |
| Q1 | M1 |
| Q2 | M2 |
| Q3 | M3 |
| Q4 | M4 |
| Q5 | M5 |
| Q6 | M6, M7 |
| Q7 | M8, M20 |
| Q8 | M9, M10 |
| Q9 | M11 |
| Q10 | M12 |
| Q11 | M13 |
| Q12 | M14, M15 |
| Q13 | M16, M17 |
| Q14 | M18, M19 |

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
