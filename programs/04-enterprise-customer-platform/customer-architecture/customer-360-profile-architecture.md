# Arquitetura de Customer 360 Profile

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture — Customer Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O perfil combina atributos permitidos com origem, temporalidade e qualidade.

## Visões

| Visão | Conteúdo |
| --- | --- |
| Core Profile | Identidade e atributos fundamentais |
| Relationship | Loyalty, service e preferências |
| Transaction Summary | Agregados permitidos de commerce |
| Interaction Timeline | Eventos relevantes e lineage |
| Eligibility | Consentimentos e políticas efetivas |
| Insights | Scores e segmentos governados |

## Regra

Todo atributo declara fonte, precedência, timestamp, qualidade, finalidade e política de acesso.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Data Product Model](../information-architecture/data-product-model.md)
- [Identity Architecture](./customer-identity-architecture.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
