# Modelo de Domínios de Dados Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Information Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O modelo distribui ownership e torna explícitas as fronteiras de Customer 360.

## Domínios de Dados

| Domínio | Dados | Relação com Customer 360 |
| --- | --- | --- |
| Identity | Identificadores, vínculos e confiança | Resolve referência |
| Profile | Atributos e precedência | Compõe visão unificada |
| Consent & Preference | Finalidade, canal e evidência | Controla uso |
| Commerce | Pedido, carrinho e compra | Contexto transacional |
| Engagement | Interações e respostas | Contexto comportamental |
| Service | Casos e resolução | Contexto de atendimento |
| Loyalty | Conta, pontos e benefícios | Contexto de relacionamento |

## Ownership

O produtor mantém dados de origem; Profile mantém composição e precedência.

## Guardrails

- ownership e accountability devem ser explícitos;
- privacidade, segurança e observabilidade são requisitos de design;
- capacidades dos Programas 02 e 03 serão reutilizadas;
- exceções exigem risco, controle compensatório, owner e validade.

## Benefícios Esperados

Coerência omnicanal, menor duplicidade, decisões rastreáveis e evolução desacoplada dos domínios.

## Relação com Outros Artefatos

- [Enterprise Information Model](./enterprise-information-model.md)
- [Data Ownership Model](./data-ownership-model.md)
- [Business Domains](../business-architecture/business-domains.md)

## Decisões Arquiteturais

As estruturas deste artefato integram o baseline normativo da Release 1.0 e orientam design, priorização e Architecture Review.
