# Padrões de Integração Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

Padrões aprovados reduzem soluções específicas e preservam semântica.

## Catálogo de Padrões

| Padrão | Uso |
| --- | --- |
| API Query | Consulta atual de perfil e política |
| Command with Confirmation | Mudança de preferência ou enrollment |
| Domain Event | Fato ocorrido em fonte autoritativa |
| Event-Carried State Transfer | Projeção controlada para leitura |
| Identity Resolution Pipeline | Vinculação governada de identificadores |
| Privacy Workflow | Propagação rastreável de direitos |
| Anti-Corruption Layer | Isolamento de legado |

## Antipadrões

Banco compartilhado, integração ponto a ponto, breaking change silencioso e replicação sem finalidade são proibidos.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Event-Driven Architecture](./event-driven-architecture.md)
- [Interaction Model](./application-interaction-model.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
