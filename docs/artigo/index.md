# Artigo - Entrega 2 (Ponto de Controle 2)

Artigo no estágio do Ponto de Controle 2 da Entrega 2 (Fases 1 a 3 e resultados parciais da Fase 4), no modelo IEEE para conferências (IEEEtran), conforme a premissa 7 do roteiro. A versão da Entrega 1 está na [release 1.0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/releases).

- **PDF:** [baixar o artigo](artigo.pdf){ download="artigo-adele-goldstine-e2-pc2.pdf" } ou [abrir em nova aba](artigo.pdf){ target="_blank" }
- **Fonte LaTeX:** pasta [`artigo/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/tree/main/artigo) do repositório
- **Overleaf:** <https://www.overleaf.com/project/6adebc46cbee7aeb66190d80/share#d055fe4415c09eb12ae4905f6f1a72e9c10e86b94b7eb508>

## Resumo

O Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA) é o ponto único de acesso do estudante da Universidade de Brasília (UnB) a notas, horários, documentos e turmas virtuais. Este artigo apresenta a avaliação da sua qualidade segundo o processo da ISO/IEC 25040 e o modelo da ISO/IEC 25010:2023. Na Fase 1, uma matriz Impacto x Risco priorizou as características, e a avaliação concentrou-se em Capacidade de Interação (Usabilidade), Adequação Funcional e Flexibilidade (Portabilidade). Na Fase 2, o método *Goal-Question-Metric* as desdobrou em três objetivos, 16 questões com hipóteses e 16 métricas, com níveis de pontuação fixados antes da coleta. A Fase 3 projetou a coleta: protocolo do teste com seis estudantes, inspeções por pares e uma execução instrumentada, com *scripts* que operam navegadores reais, para as métricas de Flexibilidade. Os primeiros resultados da Fase 4 mostram que nenhuma das 12 verificações de páginas em 360 e 768 px atende aos critérios de adaptação: sem a declaração de *viewport*, o navegador do celular reduz a página de 980 px a 37% da escala, e nenhum texto atinge 12 px efetivos. No computador, as páginas carregaram em até 2,1 s, mas, no celular com rede 4G simulada, o portal levou 8,5 s e a Turma Virtual, 19 s, e esta se desloca depois de pintada (CLS de 1,05). As tarefas funcionaram sem falha no Chrome e no Firefox, e as duas primeiras sessões do teste com usuários indicam satisfação muito baixa (SUS de 17,5 e 27,5). A gestão do projeto é acompanhada por indicadores do PSM/CID.

**Palavras-chave:** qualidade de produto de software, SQuaRE, ISO/IEC 25010, GQM, PSM, flexibilidade, SIGAA.

## Estrutura do artigo

*Tabela 1 - Seções do artigo e páginas correspondentes na GitPage.*

| Seção do artigo | Página na GitPage |
| --------------- | ----------------- |
| I. Introdução | [Introdução](introducao.md) |
| II. Referencial teórico | [Referencial Teórico](referencial-teorico.md) |
| III. Metodologia de desenvolvimento do projeto | [Metodologia](metodologia.md) |
| IV. Fase 1: requisitos da avaliação | [Fase 1](../fase-1/index.md) |
| V. Fase 2: especificação da avaliação | [Fase 2](../fase-2/index.md) |
| VI. Fase 3: projeto da avaliação | [Fase 3](../fase-3/index.md) |
| VII. Fase 4: execução da avaliação (resultados parciais) | [Fase 4](../fase-4/index.md), [Flexibilidade](../fase-4/flexibilidade.md) e [Desempenho](../fase-4/desempenho.md) |
| VIII. Considerações parciais e próximos passos | [Considerações Finais](consideracoes.md) (versão da Entrega 1) |
| Referências | [Referências do Artigo](referencias.md) |
| Apêndice A. Tabela de contribuição da equipe | [Contribuição](../contribuicao.md) |

*Fonte: elaborado pela equipe.*

## Artigo completo

<object data="artigo.pdf" type="application/pdf" width="100%" style="height: 85vh; min-height: 600px;">
  <p>O navegador não exibiu o PDF embutido. Use o link <a href="artigo.pdf">baixar o artigo</a>.</p>
</object>

## Histórico de Versão

| Versão | Data | Descrição | Autor |
| :----: | :--: | :-------: | :---: |
| 1.0 | 26/10/2026 | Página do artigo em PDF, com o link do Overleaf | [arthurlleite](https://github.com/arthurlleite) |
| 1.1 | 26/10/2026 | Resumo, palavras-chave e mapa das seções do artigo | [arthurlleite](https://github.com/arthurlleite) |
| 2.0 | 15/11/2026 | Versão do Ponto de Controle 2: resumo, palavras-chave e mapa das seções com as Fases 3 e 4 | [arthurlleite](https://github.com/arthurlleite) |
