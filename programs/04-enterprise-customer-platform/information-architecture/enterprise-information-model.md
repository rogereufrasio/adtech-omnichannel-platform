# Modelo Corporativo de Informação Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Information Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O modelo define conceitos Customer compartilhados sem impor um modelo físico único.

## Conceitos Principais

| Entidade | Definição | Owner |
| --- | --- | --- |
| Customer Party | Pessoa ou organização reconhecida | Customer |
| Identifier | Chave emitida por fonte ou canal | Fonte emissora |
| Identity Link | Relação entre identificadores | Customer Identity |
| Customer Profile | Visão consolidada e temporal | Customer |
| Consent | Evidência de escolha por finalidade | Privacy/Customer |
| Preference | Escolha de canal ou experiência | Customer |
| Interaction | Contato observável | Domínio produtor |
| Loyalty Account | Participação, saldo e benefícios | Loyalty |
| Audience | Critério versionado e elegibilidade | Marketing/Customer |

## Regras Semânticas

Definições, cardinalidade, temporalidade e fonte autoritativa serão catalogadas pelo Programa 02.

## Guardrails

- ownership e accountability devem ser explícitos;
- privacidade, segurança e observabilidade são requisitos de design;
- capacidades dos Programas 02 e 03 serão reutilizadas;
- exceções exigem risco, controle compensatório, owner e validade.

## Benefícios Esperados

Coerência omnicanal, menor duplicidade, decisões rastreáveis e evolução desacoplada dos domínios.

## Relação com Outros Artefatos

- [Data Domain Model](./data-domain-model.md)
- [Metadata Strategy](./metadata-strategy.md)
- [Programa 02](../../02-enterprise-data-ai-platform/README.md)

## Decisões Arquiteturais

As estruturas deste artefato integram o baseline normativo da Release 1.0 e orientam design, priorização e Architecture Review.
