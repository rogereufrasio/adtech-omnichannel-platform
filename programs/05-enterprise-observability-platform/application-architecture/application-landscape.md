# Landscape de Aplicações de Observabilidade

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Observability Platform |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O landscape organiza produtores, plataforma e consumidores sem acoplar instrumentação a um fornecedor.

## Zonas

| Zona | Componentes lógicos |
| --- | --- |
| Producers | Apps, APIs, data pipelines, models, infrastructure e edge |
| Collection | Agents, SDKs, gateways e collectors |
| Processing | Validate, enrich, redact, sample e route |
| Storage | Metrics, logs, traces, profiles e archive stores |
| Intelligence | Query, correlation, alerting, SLO e analytics |
| Experience | Dashboards, exploration, incidents e reporting |
| Context | Service catalog, topology, deployments e ownership |

## Critérios Arquiteturais

Contratos, ownership, SLO, segurança, privacidade, resiliência, capacidade e custo são obrigatórios. Padrões abertos e automação devem ser priorizados.

## Relação com Outros Artefatos

- [Interaction Model](./application-interaction-model.md)
- [Reference Architecture](../observability-architecture/observability-reference-architecture.md)

## Decisões Arquiteturais

Este artefato integra o baseline normativo da Release 1.0.
