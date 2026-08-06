# Arquitetura de Consentimento e Preferências

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture — Customer Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A capacidade transforma escolhas do cliente em políticas consultáveis e executáveis.

## Modelo de Política

| Elemento | Exemplo |
| --- | --- |
| Subject | Customer/identifier |
| Purpose | Personalização ou comunicação |
| Channel | Email, push, SMS ou on-site |
| Legal Basis | Consentimento ou outra base aprovada |
| Status | Permitido, negado, expirado |
| Evidence | Origem, timestamp e versão do texto |
| Jurisdiction | Regra territorial aplicável |

## Enforcement

Canais consultam política efetiva antes de ativar; alterações propagam eventos e invalidam caches.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Data Lifecycle](../information-architecture/data-lifecycle-model.md)
- [Governança de Dados](../governance/customer-data-governance.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
