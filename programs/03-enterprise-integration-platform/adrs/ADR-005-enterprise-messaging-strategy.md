# ADR-005 — Estratégia de Mensageria Corporativa

## Informações da Decisão

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Integration Platform |
| Status | Aceito |
| Versão | 1.0 |
| Decisor | Architecture Review Board |

## Contexto

A troca de mensagens entre sistemas carece de padronização e visibilidade, o que aumenta o risco de falhas operacionais e dificulta a governança.

## Objetivo

Definir uma estratégia de mensageria corporativa que padronize canais, garantias de entrega e operações de mensageria para o Programa 03.

## Visão Geral da Arquitetura

A estratégia de mensageria utiliza filas, tópicos e streams de eventos para suportar comandos, eventos e notificações. A plataforma provê roteamento confiável, persistência e mecanismos de retry e dead-letter.

## Decisões Arquiteturais

- Selecionar middleware de mensageria com suporte a at-least-once e exactly-once quando necessário.
- Definir padrões de payload, roteamento e consumidores idempotentes.
- Separar canais de comando, evento e colaboração de domínio.
- Integrar mensageria com observabilidade e governança de esquema.

## Considerações de Governança

- Estabelecer políticas e padrões para nomeação de canais e tópicos.
- Monitorar métricas de saúde de mensageria, latência e filas.
- Definir processos de resposta a dead-letter e falhas de consumo.
- Garantir propriedade clara de canais e responsabilidade operacional.

## Decisão Formal

Utilizar streaming para eventos persistentes e replay; filas para comandos e distribuição de trabalho, com semântica de entrega e retenção explícitas.

## Alternativas Consideradas

Um único mecanismo para todos os cenários; ESB central; comunicação exclusivamente síncrona.

## Consequências

### Positivas

Ajuste do mecanismo à semântica e maior resiliência.

### Trade-offs e Riscos

Mais de um runtime exige competências e governança consistentes.

## Critérios de Revisão

A decisão será reavaliada quando houver mudança material de requisitos regulatórios, escala, modelo operacional ou capacidades corporativas relacionadas. Exceções exigem registro, owner, controles compensatórios e validade.

## Referências

- TOGAF Standard
- Princípios de Arquitetura Empresarial
- Guia de Mensageria Corporativa
- Framework de Governança de Mensageria
