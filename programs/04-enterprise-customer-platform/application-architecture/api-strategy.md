# Estratégia de APIs Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

APIs Customer fornecem acesso governado a identidade, perfil, consentimento, loyalty e decisões.

## Portfólio de APIs

| API | Tipo | Consumidores |
| --- | --- | --- |
| Customer Identity | Domain/System | Profile, Service, Fraud |
| Customer Profile | Experience/Domain | Channels e Service |
| Consent & Preference | Domain | Channels, Activation, Compliance |
| Loyalty | Domain | Commerce, Channels, Service |
| Audience & Decision | Experience | Canais e Journey |
| Privacy Rights | Process | Privacy Operations |

## Ciclo de Vida

OpenAPI, versionamento semântico, compatibilidade, autenticação, quotas, SLO e depreciação seguem o Programa 03.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Interaction Model](./application-interaction-model.md)
- [Programa 03](../../03-enterprise-integration-platform/README.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
