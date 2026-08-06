# Ciclo de Vida dos Dados Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Information Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O ciclo controla dados pessoais desde coleta até eliminação ou anonimização.

## Ciclo de Vida

| Etapa | Controle mínimo |
| --- | --- |
| Coletar | Finalidade, transparência e minimização |
| Validar | Qualidade, identidade e proveniência |
| Consolidar | Precedência, temporalidade e explicabilidade |
| Servir | Autorização, finalidade, SLO e auditoria |
| Ativar | Consentimento e política de canal |
| Corrigir | Propagação, lineage e confirmação |
| Reter | Política por categoria e obrigação |
| Eliminar/Anonimizar | Execução verificável em cópias |

## Direitos do Titular

Descoberta, bloqueio, correção, portabilidade e eliminação terão evidências ponta a ponta.

## Guardrails

- ownership e accountability devem ser explícitos;
- privacidade, segurança e observabilidade são requisitos de design;
- capacidades dos Programas 02 e 03 serão reutilizadas;
- exceções exigem risco, controle compensatório, owner e validade.

## Benefícios Esperados

Coerência omnicanal, menor duplicidade, decisões rastreáveis e evolução desacoplada dos domínios.

## Relação com Outros Artefatos

- [Metadata Strategy](./metadata-strategy.md)
- [Data Product Model](./data-product-model.md)
- [Governança de Dados](../governance/customer-data-governance.md)

## Decisões Arquiteturais

As estruturas deste artefato integram o baseline normativo da Release 1.0 e orientam design, priorização e Architecture Review.
