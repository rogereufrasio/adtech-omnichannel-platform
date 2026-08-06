# Plataforma Tecnológica Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Technology Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A plataforma tecnológica suporta serviços Customer componíveis sobre capacidades corporativas.

## Capacidades Tecnológicas

| Camada | Capacidade |
| --- | --- |
| Serving | Profile, Identity, Consent e Decision APIs |
| Processing | Identity resolution, profile assembly e policy evaluation |
| State | Profile store, identity graph, consent ledger e cache |
| Data & AI | Lakehouse, feature/model services e catalog do Programa 02 |
| Integration | Gateway, event streaming e schema registry do Programa 03 |
| Platform | Containers, pipelines, secrets e configuration |

## Seleção

Produtos serão avaliados por aderência funcional, interoperabilidade, segurança, operação, custo e exit strategy.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Infrastructure](./infrastructure-architecture.md)
- [Standards](./technology-standards.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
