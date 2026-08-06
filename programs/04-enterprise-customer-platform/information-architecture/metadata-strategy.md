# Estratégia de Metadados Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Information Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

Metadados permitem descobrir, compreender, proteger e operar informações Customer.

## Metadados Obrigatórios

| Categoria | Conteúdo |
| --- | --- |
| Negócio | Definição, owner, finalidade e consumidores |
| Técnico | Schema, contrato, localização, versão e lineage |
| Qualidade | Regras, score, freshness e incidentes |
| Privacidade | Classificação, base legal, consentimento e retenção |
| Operação | SLO, criticidade, volume e suporte |
| Decisioning | Versão, features, regra/modelo e resultado |

## Catálogos

O Programa 02 mantém catálogo de dados; o Programa 03 mantém contratos de integração.

## Guardrails

- ownership e accountability devem ser explícitos;
- privacidade, segurança e observabilidade são requisitos de design;
- capacidades dos Programas 02 e 03 serão reutilizadas;
- exceções exigem risco, controle compensatório, owner e validade.

## Benefícios Esperados

Coerência omnicanal, menor duplicidade, decisões rastreáveis e evolução desacoplada dos domínios.

## Relação com Outros Artefatos

- [Enterprise Information Model](./enterprise-information-model.md)
- [Programa 02](../../02-enterprise-data-ai-platform/README.md)
- [Programa 03](../../03-enterprise-integration-platform/README.md)

## Decisões Arquiteturais

As estruturas deste artefato integram o baseline normativo da Release 1.0 e orientam design, priorização e Architecture Review.
