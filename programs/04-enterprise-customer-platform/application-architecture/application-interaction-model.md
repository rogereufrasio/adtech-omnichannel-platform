# Modelo de Interação de Aplicações Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O modelo define quando usar APIs, eventos e dados para experiências Customer.

## Interações

| Cenário | Padrão | Consistência |
| --- | --- | --- |
| Consultar perfil/consentimento | API síncrona | Leitura atual e autorizada |
| Atualizar preferência | Comando/API + evento | Confirmação e propagação |
| Publicar interação | Evento de negócio | Eventual e idempotente |
| Atualizar Customer 360 | Pipeline/data product | Governada por qualidade |
| Solicitar decisão | API de decisioning | Baixa latência e fallback |
| Propagar direito do titular | Workflow + mensagens | Rastreável ponta a ponta |

## Falhas

Timeouts, retries, idempotência, DLQ, circuit breaker e fallback são definidos por criticidade.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [API Strategy](./api-strategy.md)
- [Event-Driven Architecture](./event-driven-architecture.md)
- [Programa 03](../../03-enterprise-integration-platform/README.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
