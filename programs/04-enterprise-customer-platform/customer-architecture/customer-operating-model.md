# Modelo Operacional Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture — Customer Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O operating model combina ownership de domínio, produtos e controles corporativos.

## Papéis

| Papel | Accountability |
| --- | --- |
| Customer Domain Owner | Outcomes e semântica Customer |
| Product Owners | Identity, Profile, Consent, Loyalty e Decisioning |
| Data Owners/Stewards | Qualidade, definição e acesso |
| Platform Teams | Data, Integration e runtime Customer |
| Privacy & Security | Políticas, risco e evidências |
| Enterprise Architecture | Guardrails, ADRs e stage gates |
| SRE/Operations | SLOs, incidentes e capacidade |

## Fóruns

Product Council prioriza valor; Data Council resolve semântica; Architecture Review Board decide desvios estruturantes.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Architecture Governance](../governance/architecture-governance.md)
- [Business Domains](../business-architecture/business-domains.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
