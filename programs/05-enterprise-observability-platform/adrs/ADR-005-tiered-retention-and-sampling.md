# Retenção e Sampling em Camadas

## Informações da Decisão

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Observability Platform |
| Status | Aceito |
| Versão | 1.0 |
| Decisor | Architecture Review Board |

## Contexto

A plataforma requer uma decisão uniforme, verificável e coerente com os baselines corporativos.

## Decisão

Definir retenção, resolução e sampling por tipo de sinal, criticidade, valor investigativo, risco e custo.

## Alternativas Consideradas

Retenção uniforme; guardar tudo; descarte local não governado.

## Consequências

### Positivas

Sustentabilidade econômica preservando evidência relevante.

### Trade-offs e Riscos

Sampling pode omitir detalhe; políticas exigem validação e exceções controladas.

## Critérios de Conformidade

A decisão deve ser evidenciada por contratos, configuração, testes, telemetria e operação. Exceções exigem owner, risco, compensação e validade.

## Gatilhos de Revisão

Mudanças materiais de escala, regulação, custo, modelo operacional ou capacidade corporativa.

## Relação com Outros Artefatos

- [Architecture Vision](../docs/architecture-vision.md)
- [Decision Governance](../governance/decision-governance.md)
- [Reference Architecture](../observability-architecture/observability-reference-architecture.md)
