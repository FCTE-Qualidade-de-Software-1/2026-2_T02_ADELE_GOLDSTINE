# Fase 1 - Estabelecimento dos Requisitos da Avaliação

Esta fase corresponde à primeira etapa do processo de avaliação de produto de software definido pela norma **ISO/IEC 25040**, na qual são estabelecidos os requisitos postos no nosso projeto.

## 1.1 Objetivo da Avaliação

O objetivo desta avaliação é analisar a qualidade do **SIGAA** (Sistema Integrado de Gestão de Atividades Acadêmicas) utilizado pela **Universidade de Brasília (UnB)**. O SIGAA é a base funcional de organização pra alunos, professores e alguns funcionários da instituição, abrangendo funcionalidades como matrícula em disciplinas, consulta de notas e menções, visualização de turmas e horários, visualização de grade e etc...

A avaliação tem como finalidade identificar pontos fortes e fracos no que diz respeito a consulta de grade e criação de fluxo no SIGAA, tendo como referêncial a experiência dos alunos E a existência de concorrentes de terceiros que vingaram por A) Serem mais acessíveis E/OU B) suprirem a necessidade de forma que o SIGAA não faz.

## 1.2 Produto de Software Avaliado

O **SIGAA** é um sistema web integrado de gestão acadêmica desenvolvido originalmente pela **Universidade Federal do Rio Grande do Norte (UFRN)**. O sistema foi adotado por diversas universidades federais brasileiras, incluindo a UnB, como solução institucional para a administração de atividades acadêmicas.

Entre as principais funcionalidades do SIGAA, destacam-se:

- **Matrícula em disciplinas** e gerenciamento de turmas;
- **Consulta de notas**, menções e histórico acadêmico;
- **Visualização de horários** e calendário acadêmico;
- **Gestão de processos institucionais**, como trancamento de disciplinas, aproveitamento de créditos e emissão de documentos;
- **Comunicação** entre discentes e docentes por meio de fóruns e notícias das turmas.

O SIGAA opera como uma aplicação web , sendo utilizado por uma ampla camada de dispositivos.

## 1.3 Modelo de Qualidade

O modelo de qualidade adotado nesta avaliação é o definido pela norma **ISO/IEC 25010:2011**, que integra a família de normas **SQuaRE** (*Systems and software Quality Requirements and Evaluation* — ISO/IEC 25000). Essa norma estabelece um modelo de qualidade de produto de software composto por **8 características de qualidade**:

1. Adequação Funcional
2. Eficiência de Desempenho
3. Compatibilidade
4. Usabilidade
5. Confiabilidade
6. Segurança
7. Manutenibilidade
8. Portabilidade

Cada característica é subdividida em subcaracterísticas que permitem uma avaliação mais detalhada e precisa dos diferentes aspectos de qualidade do software.

## 1.4 Características de Qualidade Selecionadas

Para esta avaliação, foram selecionadas **três características de qualidade** da ISO/IEC 25010, consideradas as mais relevantes para o contexto de uso do SIGAA na UnB. A justificativa para cada seleção é apresentada a seguir.

### 1.4.1 Adequação Funcional

A Adequação Funcional avalia o grau em que o software fornece funções que atendem às necessidades declaradas e implícitas dos usuários. Suas subcaracterísticas são: **completude funcional**, **correção funcional** e **adequação funcional** (pertinência).

**Justificativa:** O SIGAA é o sistema central de gestão acadêmica da UnB, sendo utilizado para atividades essenciais como matrícula, consulta de notas e acompanhamento de turmas. É fundamental que o sistema ofereça todas as funções necessárias, que essas funções produzam resultados corretos e que sejam adequadas às tarefas dos usuários. Falhas nessa característica impactam diretamente a vida acadêmica de milhares de estudantes, docentes e servidores.

### 1.4.2 Usabilidade

A Usabilidade avalia o grau em que o software pode ser utilizado por usuários específicos para atingir objetivos com eficácia, eficiência e satisfação. Suas subcaracterísticas incluem: **reconhecimento de adequação**, **apreensibilidade**, **operabilidade**, **proteção contra erros do usuário**, **estética da interface** e **acessibilidade**.

**Justificativa:** O SIGAA possui uma base de usuários diversificada, composta por estudantes de graduação e pós-graduação, docentes e técnicos administrativos, com diferentes níveis de proficiência tecnológica.

### 1.4.3 Portabilidade

A Portabilidade avalia o grau de eficácia e eficiência com que o software pode ser transferido de um ambiente para outro. Suas subcaracterísticas são: **adaptabilidade**, **capacidade de instalação** e **capacidade de substituição**.

**Justificativa:** Os usuários acessam o SIGAA a partir de diferentes dispositivos (computadores de mesa, notebooks, tablets e smartphones) e navegadores web (Chrome, Firefox, Safari, Edge, entre outros). Avaliar a adaptabilidade do sistema a diferentes ambientes de execução e a consistência da experiência de acesso em múltiplas plataformas é relevante para garantir que todos os usuários possam utilizar o sistema de forma adequada, independentemente do dispositivo ou navegador empregado, principalmente numa faculdade pública onde existe um leque de usuários extensos com limitações orçamentárias. É ideal saber se o SIGAA é portanto, inclusivo e democrático. 

## 1.5 Escopo da Avaliação

O escopo desta avaliação está delimitado aos **módulos voltados ao discente** do SIGAA na UnB, com foco na **interface web** do sistema. Serão consideradas as funcionalidades mais utilizadas pelos estudantes, tais como:

- Visualização do fluxo de disciplinas;
- Consulta de notas e menções;
- Visualização de turmas e horários;
- Acesso ao histórico acadêmico;
- Navegação geral pelo sistema.

A avaliação considerará a **versão do sistema disponível durante o 2º semestre letivo de 2026**, refletindo o estado atual do produto em uso pela comunidade universitária.

## 1.6 Rigor da Avaliação

A avaliação seguirá uma abordagem sistemática fundamentada no processo de avaliação de produto de software definido pela **ISO/IEC 25040**, contemplando:

- **Definição de métricas** de qualidade alinhadas às características e subcaracterísticas selecionadas da ISO/IEC 25010;
- **Procedimentos de coleta de dados** estruturados, incluindo inspeção da interface, testes exploratórios e análise heurística;
- **Critérios de interpretação e julgamento** dos resultados obtidos, com níveis de pontuação claramente definidos.

O rigor adotado busca garantir a reprodutibilidade e a objetividade da avaliação, de forma compatível com o contexto acadêmico da disciplina de Qualidade de Software 1 (FGA0315).

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 16/10/2026 | Criação do documento da Fase 1 | [Davi Nobre](https://github.com/Jagaima) |
| 1.1 | 16/10/2026 | Parte da documentação da Fase 1 adcionada. (métricas, rigor, caracteriticas escolhidas)| [Davi Nobre](https://github.com/Jagaima) |
