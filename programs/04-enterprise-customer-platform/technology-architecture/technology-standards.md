# Padrões Tecnológicos Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Technology Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

Padrões asseguram interoperabilidade e qualidade sem prescrever fornecedor prematuramente.

## Padrões

| Área | Padrão |
| --- | --- |
| APIs | OpenAPI, OAuth 2.x/OIDC e versionamento |
| Eventos | AsyncAPI, schemas compatíveis e correlation ID |
| Identidade | Identificadores opacos e links auditáveis |
| Dados | Contratos, catálogo, lineage e classificação |
| Segurança | TLS, encryption at rest, secrets e least privilege |
| Observabilidade | Logs estruturados, métricas, traces e SLO |
| Delivery | IaC, policy as code, testes e artifact provenance |

## Governança

Exceções seguem Architecture Review e prazo de remediação.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Technology Platform](./technology-platform.md)
- [Programa 03](../../03-enterprise-integration-platform/README.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
