# Arquitetura de Referência Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture — Customer Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A referência consolida as capacidades específicas do domínio Customer.

## Camadas

1. canais e jornadas;
2. experience APIs e journey orchestration;
3. Identity, Profile, Consent, Preference, Loyalty e Audience;
4. decisioning e personalização;
5. Customer Data Products do Programa 02;
6. APIs e eventos do Programa 03;
7. fontes autoritativas;
8. controles transversais.

## Regra de Composição

Cada camada possui contrato e accountability próprios; dependências somente atravessam interfaces governadas.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Application Landscape](../application-architecture/application-landscape.md)
- [Target State](../architecture-target-state.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
