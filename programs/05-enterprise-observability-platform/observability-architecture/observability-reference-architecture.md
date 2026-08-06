# Arquitetura de Referência de Observabilidade

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Observability Platform |
| Domínio Arquitetural | Application Architecture — Observability Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A referência organiza capacidades de ponta a ponta.

## Camadas

1. instrumentation and sources;
2. collectors and transport;
3. processing and control;
4. signal stores;
5. query and correlation;
6. SLO, alerting and incident intelligence;
7. persona experiences;
8. catalog, security, governance and FinOps.

## Regra

A plataforma nunca será dependência síncrona crítica para a execução do produto observado.

## Critérios Arquiteturais

Contratos, ownership, SLO, segurança, privacidade, resiliência, capacidade e custo são obrigatórios. Padrões abertos e automação devem ser priorizados.

## Relação com Outros Artefatos

- [Application Landscape](../application-architecture/application-landscape.md)
- [Target State](../architecture-target-state.md)

## Decisões Arquiteturais

Este artefato integra o baseline normativo da Release 1.0.
