# Modelo de Ownership de Dados Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Information Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O modelo separa accountability de origem, consolidação, governança e consumo.

## Matriz de Accountability

| Ativo | Accountable | Responsible | Consulted |
| --- | --- | --- | --- |
| Identificador de origem | Domínio emissor | Product Team de origem | Customer Identity |
| Golden Customer ID | Customer Domain Owner | Identity Team | Data Governance |
| Perfil consolidado | Customer Domain Owner | Profile Team | Domínios produtores |
| Consentimento | Privacy/Customer | Consent Team | Legal e canais |
| Interação | Domínio produtor | Product Team produtor | Customer/Data |
| Segmento | Marketing/Customer | Decisioning Team | Data & AI |

## Conflitos

Precedência e disputas semânticas são decididas pelo Data Owner; riscos vão a Privacy.

## Guardrails

- ownership e accountability devem ser explícitos;
- privacidade, segurança e observabilidade são requisitos de design;
- capacidades dos Programas 02 e 03 serão reutilizadas;
- exceções exigem risco, controle compensatório, owner e validade.

## Benefícios Esperados

Coerência omnicanal, menor duplicidade, decisões rastreáveis e evolução desacoplada dos domínios.

## Relação com Outros Artefatos

- [Data Domain Model](./data-domain-model.md)
- [Operating Model](../customer-architecture/customer-operating-model.md)
- [Governança de Dados](../governance/customer-data-governance.md)

## Decisões Arquiteturais

As estruturas deste artefato integram o baseline normativo da Release 1.0 e orientam design, priorização e Architecture Review.
