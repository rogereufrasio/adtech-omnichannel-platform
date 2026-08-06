# Arquitetura Orientada a Eventos Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

Eventos propagam fatos Customer sem criar dependência temporal entre produtores e consumidores.

## Eventos Prioritários

| Evento | Owner | Característica |
| --- | --- | --- |
| CustomerIdentified | Identity | Vínculo criado ou confirmado |
| CustomerProfileUpdated | Profile | Mudança consolidada permitida |
| ConsentChanged | Consent | Alteração de política aplicável |
| PreferenceChanged | Preference | Escolha de canal ou conteúdo |
| LoyaltyTierChanged | Loyalty | Mudança de relacionamento |
| CustomerInteractionRecorded | Domínio produtor | Interação observada |

## Semântica

Eventos são fatos imutáveis; schemas usam AsyncAPI, classificação, versionamento e compatibilidade do Programa 03.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Integration Patterns](./integration-patterns.md)
- [Programa 03](../../03-enterprise-integration-platform/README.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
