# Referencial Teórico

Esta página reproduz o Referencial Teórico do [artigo da Entrega 1](index.md).

## 1. Qualidade de produto e a família SQuaRE

A série ISO/IEC 25000 (SQuaRE) organiza os requisitos, modelos, medidas e o processo de avaliação da qualidade de sistemas e software [1]. A ISO/IEC 25010:2023 substitui a versão de 2011 e organiza a qualidade do produto em nove características [2] (Tabela 1). Nesta documentação, as características renomeadas aparecem com o nome de 2023 seguido do de 2011. A satisfação integrava o modelo de qualidade em uso da versão de 2011 [3] e, quando usada, é tratada como medida complementar de qualidade em uso [4].

*Tabela 1 - Características de qualidade de produto da ISO/IEC 25010:2023.*

| Característica (2023) | Nome em 2011 |
| --------------------- | ------------ |
| Adequação Funcional | Adequação Funcional |
| Eficiência de Desempenho | Eficiência de Desempenho |
| Compatibilidade | Compatibilidade |
| Capacidade de Interação | Usabilidade |
| Confiabilidade | Confiabilidade |
| Segurança | Segurança |
| Manutenibilidade | Manutenibilidade |
| Flexibilidade | Portabilidade |
| Segurança Operacional | (nova) |

*Fonte: elaborado pela equipe, com base em [2] e [3].*

## 2. Processo de avaliação de produto

A ISO/IEC 25040 descreve a avaliação como um processo em atividades sucessivas [5]. No material da disciplina, ele é apresentado em quatro fases [6] (Tabela 2). A especificação deve ser detalhada o bastante para que a avaliação seja repetível e reprodutível.

*Tabela 2 - Fases do processo de avaliação e entregas do projeto.*

| Fase | Atividade | Produto | Entrega |
| ---- | --------- | ------- | ------- |
| 1 | Estabelecer os requisitos | Propósito, tipo de produto e modelo de qualidade | Entrega 1 |
| 2 | Especificar a avaliação | Métricas, níveis de pontuação e critérios de julgamento | Entrega 1 |
| 3 | Projetar a avaliação | Plano com método, instruções, recursos e cronograma | Entrega 2 |
| 4 | Executar a avaliação | Medidas obtidas, comparadas com os critérios e julgadas | Entrega 2 |

*Fonte: elaborado pela equipe, com base em [5], [6] e [7].*

## 3. Método Goal-Question-Metric

O GQM parte do princípio de que a medição deve ser orientada a objetivos [8]. A definição ocorre em três níveis, e a interpretação segue o caminho inverso [9]:

- **conceitual:** o objetivo de medição;
- **operacional:** as questões que caracterizam o objeto quanto ao foco de qualidade;
- **quantitativo:** as métricas que respondem às questões.

Cada objetivo é escrito em um *template* com objeto, propósito, foco de qualidade, ponto de vista e contexto [8], e cada questão recebe uma hipótese, a resposta esperada antes da medição. Boas métricas são simples, objetivas, fáceis de coletar, robustas e válidas [9]. A aplicação no projeto está na [Fase 2](../fase-2/index.md).

## 4. Medição prática de software e sistemas

O PSM é uma abordagem de medição dirigida por necessidades de informação e ligada à gestão de projetos [10]. Seu modelo de informação, adotado pela ISO/IEC/IEEE 15939 [11], liga atributos a medidas básicas, medidas derivadas e indicadores, estes associados a critérios de decisão [12]. As necessidades de informação são agrupadas em categorias, entre elas calendário e progresso, recursos e custos e desempenho dos processos. O *framework* CID adapta essas categorias a equipes que trabalham em ciclos curtos, com medidas como *burndown*, comprometido *versus* concluído e tempo de ciclo [13] [14]. A aplicação no projeto está em [Gestão do Projeto](../gestao-psm.md).

## 5. Medidas de referência

A ISO/IEC 25023 define medidas de produto como cobertura e correção funcional na forma X = 1 − A/B [15], e a ISO/IEC 25022, medidas de eficácia, eficiência e satisfação em uso [4]. As referências externas usadas nos níveis de pontuação estão na Tabela 3.

*Tabela 3 - Medidas de referência usadas na especificação.*

| Medida | Referência | Uso na Fase 2 |
| ------ | ---------- | ------------- |
| Taxa de conclusão de tarefas | Média de referência de 78% [16] | Faixas de M5 |
| *System Usability Scale* (SUS) | Pontuação de 0 a 100 [17], com média de referência 68 [18] | Faixas de M12 e indicador IQ4 |
| *Single Ease Question* (SEQ) | Facilidade percebida de uma tarefa em um item [18] | Bloco C do [questionário](../fase-2/questionario.md) |
| Acessibilidade | Critérios A e AA das WCAG 2.2 [19] | M9 e M10 |

*Fonte: elaborado pela equipe.*

## 6. Personas

Personas são arquétipos de usuários, descritos com objetivos, contexto e frustrações, que orientam o projeto e a avaliação de um produto para quem de fato o usa [20]. A antipersona descreve quem não é público-alvo e ajuda a delimitar o escopo. Em uma avaliação de qualidade, as personas tornam concreto o ponto de vista declarado nos objetivos de medição e ajudam a escolher tarefas e recortes de análise. As personas do projeto estão em [Personas](../fase-1/personas.md).

## Referências

[1] ISO/IEC 25000:2014. *Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - Guide to SQuaRE*. Genebra: ISO, 2014.

[2] ISO/IEC 25010:2023. *Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - Product quality model*. Genebra: ISO, 2023.

[3] ISO/IEC 25010:2011. *Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - System and software quality models*. Genebra: ISO, 2011.

[4] ISO/IEC 25022:2016. *Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - Measurement of quality in use*. Genebra: ISO, 2016.

[5] ISO/IEC 25040:2024. *Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - Quality evaluation framework*. Genebra: ISO, 2024.

[6] RAMOS, C. S. *Processo de Avaliação de Produto de Software*. Notas de aula (Aula 07), FGA0315 Qualidade de Software 1, Universidade de Brasília, 2026.

[7] RAMOS, C. S. *Projeto Final da Disciplina - Avaliação da Qualidade de Produto de Software*. FGA0315 Qualidade de Software 1, Universidade de Brasília, 2026.

[8] BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Wiley, 1994.

[9] RAMOS, C. S. *Medição baseada em objetivos: Goal-Question-Metric*. Notas de aula (Aula 08), FGA0315 Qualidade de Software 1, Universidade de Brasília, 2026.

[10] McGARRY, J. et al. *Practical Software Measurement: Objective Information for Decision Makers*. Boston: Addison-Wesley, 2002.

[11] ISO/IEC/IEEE 15939:2017. *Systems and software engineering - Measurement process*. Genebra: ISO, 2017.

[12] RAMOS, C. S. *Medição Prática de Software e Sistemas (PSM)*. Notas de aula (Aula 09), FGA0315 Qualidade de Software 1, Universidade de Brasília, 2026.

[13] JONES, C. L. et al. *Practical Software and Systems Measurement Continuous Iterative Development Measurement Framework: Part 1 - Concepts, Definitions, Principles, and Measures*. Versão 2.1. PSM, NDIA e INCOSE, 2021.

[14] JONES, C. L. et al. *Practical Software and Systems Measurement Continuous Iterative Development Measurement Framework: Part 2 - Measurement Specifications and Enterprise Measures*. Versão 2.1. PSM, NDIA e INCOSE, 2021.

[15] ISO/IEC 25023:2016. *Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE) - Measurement of system and software product quality*. Genebra: ISO, 2016.

[16] SAURO, J. What is a good task-completion rate? *MeasuringU*, 2011. Disponível em: <https://measuringu.com/task-completion/>. Acesso em: 18 out. 2026.

[17] BROOKE, J. SUS: a "quick and dirty" usability scale. In: JORDAN, P. W. et al. (ed.). *Usability Evaluation in Industry*. Londres: Taylor & Francis, 1996. p. 189-194.

[18] SAURO, J.; LEWIS, J. R. *Quantifying the User Experience: Practical Statistics for User Research*. 2. ed. Cambridge: Morgan Kaufmann, 2016.

[19] W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation, 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>.

[20] COOPER, A. *The Inmates Are Running the Asylum: Why High-Tech Products Drive Us Crazy and How to Restore the Sanity*. Indianapolis: Sams, 1999.

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento | Davi Nobre |
| 1.1 | 26/10/2026 | Conteúdo do Referencial Teórico, a partir do artigo da Entrega 1 | [arthurlleite](https://github.com/arthurlleite) |
