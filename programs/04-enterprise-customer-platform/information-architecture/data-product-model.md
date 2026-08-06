# Modelo de Produtos de Dados Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Information Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

Produtos Customer tornam informações reutilizáveis com contrato, qualidade e accountability.

## Produtos Release 1.0

| Produto | Conteúdo | Consumidores |
| --- | --- | --- |
| Customer Identity Map | Golden ID, identificadores e confidence | Profile, Service, Fraud |
| Customer 360 Profile | Atributos permitidos, origem e temporalidade | Channels, Analytics |
| Consent & Preference | Finalidade, canal, status e evidência | Activation, Compliance |
| Customer Interaction Timeline | Interações normalizadas e lineage | Service, Analytics |
| Loyalty Relationship | Conta, tier e benefícios | Channels, Service |

## Contrato

Owner, propósito, schema, qualidade, SLO, classificação, consumidores e lineage são obrigatórios.

## Guardrails

- ownership e accountability devem ser explícitos;
- privacidade, segurança e observabilidade são requisitos de design;
- capacidades dos Programas 02 e 03 serão reutilizadas;
- exceções exigem risco, controle compensatório, owner e validade.

## Benefícios Esperados

Coerência omnicanal, menor duplicidade, decisões rastreáveis e evolução desacoplada dos domínios.

## Relação com Outros Artefatos

- [Data Domain Model](./data-domain-model.md)
- [Data Lifecycle](./data-lifecycle-model.md)
- [Programa 02](../../02-enterprise-data-ai-platform/README.md)

## Decisões Arquiteturais

As estruturas deste artefato integram o baseline normativo da Release 1.0 e orientam design, priorização e Architecture Review.
