# Domínios de Negócio e Operação

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Observability Platform |
| Domínio Arquitetural | Business Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O modelo define accountabilities entre plataforma, produtos e funções corporativas.

## Domínios

| Domínio | Accountability |
| --- | --- |
| Product Domains | Instrumentação, SLO, on-call e resposta |
| Observability Platform | Pipeline, stores, tooling e golden paths |
| SRE/Reliability | Práticas, coaching e riscos de confiabilidade |
| Business Operations | Impacto, jornadas e comunicação |
| Security Operations | Detecção e resposta de segurança |
| Data & AI Operations | Pipelines, qualidade, modelos e drift |
| Governance/FinOps | Políticas, evidências, capacidade e custo |

## Fronteira

A plataforma não se torna owner dos serviços observados nem único centro de resposta.

## Guardrails

- service ownership, criticidade e finalidade explícitos;
- segurança, privacidade, retenção e custo por design;
- contratos e padrões abertos antes de ferramentas;
- evidências operacionais sustentam decisões e exceções.

## Relação com Outros Artefatos

- [Operating Model](../observability-architecture/observability-operating-model.md)
- [Capability Map](./capability-map.md)

## Decisões Arquiteturais

Este artefato integra o baseline normativo da Release 1.0.
