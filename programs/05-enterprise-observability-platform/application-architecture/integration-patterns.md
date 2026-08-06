# Padrões de Integração de Observabilidade

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Observability Platform |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

Padrões aprovados evitam pipelines frágeis e alertas isolados.

## Padrões

| Padrão | Uso |
| --- | --- |
| OpenTelemetry Export | Instrumentação portável |
| Collector Gateway | Processamento e roteamento central |
| Edge Collector | Buffering próximo à fonte |
| Event Notification | Alertas e mudanças assíncronas |
| Context Enrichment | Owner, deploy, service e environment |
| Tiered Storage | Retenção por valor e custo |
| Federated Query | Consulta sem cópia ampla |

## Antipadrões

Vendor SDK obrigatório, payload pessoal em logs, alerta sem owner e cardinalidade ilimitada são proibidos.

## Critérios Arquiteturais

Contratos, ownership, SLO, segurança, privacidade, resiliência, capacidade e custo são obrigatórios. Padrões abertos e automação devem ser priorizados.

## Relação com Outros Artefatos

- [Telemetry Pipeline](../observability-architecture/telemetry-pipeline-architecture.md)
- [Programa 03](../../03-enterprise-integration-platform/README.md)

## Decisões Arquiteturais

Este artefato integra o baseline normativo da Release 1.0.
