# Padrões Tecnológicos de Observabilidade

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Observability Platform |
| Domínio Arquitetural | Technology Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

Padrões preservam interoperabilidade e qualidade.

## Padrões

| Área | Diretriz |
| --- | --- |
| Instrumentation | OpenTelemetry APIs/SDKs e semantic conventions |
| Metrics | Unidades, temporality e cardinalidade controladas |
| Logs | Estruturados, schemas e sem segredos |
| Traces | W3C Trace Context e sampling governado |
| APIs/Events | OpenAPI/AsyncAPI e identidade do Programa 03 |
| Security | Encryption, least privilege e audit |
| Delivery | IaC, policy as code e provenance |
| SLO | SLIs reproduzíveis e janelas explícitas |

## Critérios Arquiteturais

Contratos, ownership, SLO, segurança, privacidade, resiliência, capacidade e custo são obrigatórios. Padrões abertos e automação devem ser priorizados.

## Relação com Outros Artefatos

- [Programa 03](../../03-enterprise-integration-platform/README.md)
- [Compliance](../governance/reference-architecture-compliance.md)

## Decisões Arquiteturais

Este artefato integra o baseline normativo da Release 1.0.
