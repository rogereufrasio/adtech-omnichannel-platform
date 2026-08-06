# Diagrama Executivo do Estado-Alvo

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Foundation |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A visão em camadas separa jornadas, serviços Customer e baselines corporativos, tornando ownership e controles explícitos.

## Diagrama Executivo

```mermaid
flowchart TB
    O[Outcomes<br/>Confiança · Retenção · Experiência · Eficiência]
    X[Experiências<br/>Commerce · Atendimento · Marketing · Loyalty · Parceiros]
    C[Customer Services<br/>Identity · Profile · Consent · Preference · Audience]
    D[Decisioning<br/>Segmentação · Propensão · Next Best Action]
    B[Baselines Corporativos<br/>Programa 02 Data & AI · Programa 03 Integration]
    S[Fontes Autoritativas<br/>CRM · Commerce · Service · Loyalty · Digital]
    G[Controles Transversais<br/>Privacy · Security · Governance · Observability]

    O --> X --> C --> D --> B --> S
    G -. políticas e evidências .-> C
    G -. controles .-> D
    G -. guardrails .-> B
```

## Leitura Executiva

A plataforma coordena contexto Customer e decisões de experiência. Data & AI mantém produtos de dados e modelos; Integration transporta contratos; fontes continuam responsáveis pelos registros de origem.

## Relação com Outros Artefatos

- [Architecture Vision](../docs/architecture-vision.md)
- [Architecture Target State](../architecture-target-state.md)
- [Landing Page](../README.md)

## Decisões Arquiteturais

A arquitetura executiva preserva separação entre experiência, domínio Customer e capacidades corporativas compartilhadas.
