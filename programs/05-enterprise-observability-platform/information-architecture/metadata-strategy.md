# Estratégia de Metadados de Observabilidade

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Observability Platform |
| Domínio Arquitetural | Information Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

Metadados conectam telemetria a serviços, owners, mudanças e outcomes.

## Metadados Obrigatórios

| Categoria | Conteúdo |
| --- | --- |
| Serviço | Nome, domínio, owner, tier e on-call |
| Runtime | Ambiente, região, versão e deployment |
| Telemetria | Signal type, schema, unit e cardinalidade |
| Reliability | SLI, SLO, error budget e dependency |
| Governance | Classificação, retenção, acesso e custo center |
| Change | Commit, build, release e feature flag |

## Fontes

Service catalog, CI/CD, cloud inventory e contracts alimentam enrichment automatizado.

## Guardrails

- service ownership, criticidade e finalidade explícitos;
- segurança, privacidade, retenção e custo por design;
- contratos e padrões abertos antes de ferramentas;
- evidências operacionais sustentam decisões e exceções.

## Relação com Outros Artefatos

- [Service Catalog](../observability-architecture/service-catalog-and-topology.md)
- [Telemetry Model](./telemetry-data-model.md)

## Decisões Arquiteturais

Este artefato integra o baseline normativo da Release 1.0.
