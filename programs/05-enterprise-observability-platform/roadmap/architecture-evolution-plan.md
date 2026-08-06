# Plano de Evolução Arquitetural

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Observability Platform |
| Domínio Arquitetural | Roadmap |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A transição preserva continuidade e evita migração big bang.

## Transições

| Atual | Evolução |
| --- | --- |
| Agents proprietários | OpenTelemetry e collectors |
| Silos por sinal | Contexto e query correlacionados |
| Dashboards locais | Golden paths e templates |
| Alertas por threshold | SLO/burn-rate e impacto |
| Inventário manual | Service catalog alimentado por CI/CD |
| Retenção uniforme | Tiering orientado a valor e custo |
| Operação reativa | Learning e automação segura |

## Coexistência

Adapters e dual export temporário possuem prazo, owner e critério de retirada.

## Controles Obrigatórios

Owner, evidência, métrica, risco, capacidade, custo e ciclo de revisão são obrigatórios. Exceções possuem compensação e validade.

## Relação com Outros Artefatos

- [Target State](../architecture-target-state.md)
- [Roadmap](./implementation-roadmap.md)

## Decisões Arquiteturais

Este artefato integra o baseline normativo da Release 1.0.
