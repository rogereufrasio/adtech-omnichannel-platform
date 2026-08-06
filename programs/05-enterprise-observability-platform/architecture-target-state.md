# Architecture Target State

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Foundation |
| Versão | 1.0 |
| Status | Aprovado |

## Estado Atual e Alvo

| Dimensão | Atual | Alvo |
| --- | --- | --- |
| Instrumentação | Específica por time | Contratos e SDKs padronizados |
| Correlação | Por ferramenta | Contexto ponta a ponta |
| Alertas | Volume e thresholds | SLO e impacto |
| Ownership | Implícito | Catálogo e on-call explícitos |
| Retenção | Uniforme | Tiered por valor e risco |
| Operação | Reativa | Data-driven e automatizada |

## Arquitetura-Alvo

Sources → collectors → processing/control → signal stores → query/analytics → SLO/incident experiences, com catálogo, segurança e FinOps transversais.

## Dependências

Programas 02, 03 e 04; plataformas de identidade, CI/CD, ITSM e segurança corporativa.

## Relação com Outros Artefatos

- [Architecture Vision](./docs/architecture-vision.md)
- [Diagrama Executivo](./diagrams/executive-target-state.md)
- [Maturity Assessment](./maturity-assessment.md)
