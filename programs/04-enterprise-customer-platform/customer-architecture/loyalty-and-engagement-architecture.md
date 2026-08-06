# Arquitetura de Loyalty e Engagement

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture — Customer Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A arquitetura integra loyalty e engagement ao perfil sem fundir regras de benefício com Customer 360.

## Fronteiras

| Capacidade | Ownership |
| --- | --- |
| Membership, points, tiers | Loyalty |
| Customer identity/profile | Customer |
| Campaign/journey | Marketing |
| Eligibility/consent | Customer/Privacy |
| Transaction | Commerce |
| Activation contract | Integration |

## Interações

Enrollment e resgate usam APIs; mudanças de tier e pontos geram eventos; benefícios permanecem no sistema autoritativo de loyalty.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Customer Reference Architecture](./customer-reference-architecture.md)
- [Application Interaction Model](../application-architecture/application-interaction-model.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
