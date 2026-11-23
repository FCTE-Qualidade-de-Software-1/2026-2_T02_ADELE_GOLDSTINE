# Artigo - Entrega Final

Artigo final da avaliação (Fases 1 a 4, julgamento, matriz multiplataforma, ação de melhoria e conclusão), com 12 páginas, no modelo IEEE para conferências (IEEEtran), conforme a premissa 7 do roteiro. A versão da Entrega 1 está na [release 1.0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/releases).

- **PDF:** [baixar o artigo](artigo.pdf){ download="artigo-adele-goldstine-final.pdf" } ou [abrir em nova aba](artigo.pdf){ target="_blank" }
- **Fonte LaTeX:** pasta [`artigo/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_ADELE_GOLDSTINE/tree/main/artigo) do repositório
- **Overleaf:** <https://www.overleaf.com/project/6b04809b6bd87c703701ebf4/share#ec4b766bf0e081e6b89f4427f7486bd96f1c4c0347d4e6d0>

## Resumo

O Sistema Integrado de Gestão de Atividades Acadêmicas (SIGAA) é o ponto único de acesso do estudante da Universidade de Brasília (UnB) a notas, horários, documentos e turmas virtuais. Este artigo apresenta a avaliação da sua qualidade segundo o processo da ISO/IEC 25040 e o modelo da ISO/IEC 25010:2023, do ponto de vista do estudante de graduação. Uma matriz Impacto x Risco priorizou Capacidade de Interação, Adequação Funcional e Flexibilidade, desdobradas pelo método *Goal-Question-Metric* em três objetivos, 16 questões com hipóteses e 16 métricas com níveis fixados antes da coleta. A coleta combinou teste com cinco estudantes (30 tentativas de seis tarefas), questionário com o SUS, inspeção por pares, a ferramenta WAVE e *scripts* que operam navegadores reais; uma matriz complementar executou as tarefas em 20 perfis de sistema, aparelho e navegador (Windows, macOS, Linux, Android, iOS e iPadOS; sete navegadores). Capacidade de Interação **não atende** (média 0,90 de 3): os estudantes concluíram 83,3% das tentativas, mas levaram 4,39 vezes o tempo de um especialista e deram 32,5 pontos no SUS, e as páginas têm 13,17 erros de acessibilidade em média. Adequação Funcional e Flexibilidade **atendem parcialmente** (1,00 e 1,33): os dados estão corretos (97%), mas 60% planejam o curso fora do SIGAA; as tarefas funcionam em todos os navegadores, mas nenhuma página se adapta ao celular, em nenhum dos perfis móveis. Das 16 hipóteses, 7 foram confirmadas e 9 refutadas, cinco delas para pior. A ação de melhoria, um protótipo *mobile-first* das seis tarefas, levou as páginas adaptadas de 0 para 12 de 12 e os erros de acessibilidade de 13,17 para 0 por página, medidos com os mesmos *scripts*.

**Palavras-chave:** qualidade de produto de software, SQuaRE, ISO/IEC 25010, GQM, usabilidade, flexibilidade, acessibilidade, SIGAA.

## Estrutura do artigo

*Tabela 1 - Seções do artigo e páginas correspondentes na GitPage.*

| Seção do artigo | Página na GitPage |
| --------------- | ----------------- |
| I. Introdução | [Introdução](introducao.md) |
| II. Referencial teórico | [Referencial Teórico](referencial-teorico.md) |
| III. Metodologia de desenvolvimento do projeto | [Metodologia](metodologia.md) (a gestão da equipe não faz parte da versão final do artigo) |
| IV. Fase 1: requisitos da avaliação | [Fase 1](../fase-1/index.md) |
| V. Fase 2: especificação da avaliação | [Fase 2](../fase-2/index.md) |
| VI. Fase 3: projeto da avaliação | [Fase 3](../fase-3/index.md) |
| VII. Fase 4: execução, resultados e julgamento | [Julgamento](../fase-4/julgamento.md), [Flexibilidade](../fase-4/flexibilidade.md), [Matriz Multiplataforma](../fase-4/matriz-multiplataforma.md) e [Desempenho](../fase-4/desempenho.md) |
| VIII. Ação de melhoria | [Protótipo Mobile](../fase-4/prototipo-mobile.md) |
| IX. Conclusão | [Síntese e Conclusão](../fase-4/sintese-final.md) |
| Referências | [Referências do Artigo](referencias.md) |

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
| 3.0 | 23/11/2026 | Versão final: resumo, palavras-chave e mapa das seções (Fase 4 completa, ação de melhoria e conclusão; sem gestão da equipe nem apêndice de contribuição) | [arthurlleite](https://github.com/arthurlleite) |
| 3.1 | 23/11/2026 | Novo link do projeto no Overleaf | [arthurlleite](https://github.com/arthurlleite) |
