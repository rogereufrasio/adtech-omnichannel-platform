# AIOps Governado com Supervisão Humana

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

Usar IA para apoiar detecção, correlação, sumarização e recomendação; ações de alto impacto exigem aprovação humana, auditabilidade e fallback.

## Alternativas Consideradas

Remediação autônoma irrestrita; ausência de IA; black-box vendor decisions.

## Consequências

### Positivas

Reduz toil e acelera diagnóstico com controle.

### Trade-offs e Riscos

False positives, drift e opacidade exigem avaliação contínua e limites operacionais.

## Critérios de Conformidade

A decisão deve ser evidenciada por contratos, configuração, testes, telemetria e operação. Exceções exigem owner, risco, compensação e validade.

## Gatilhos de Revisão

Mudanças materiais de escala, regulação, custo, modelo operacional ou capacidade corporativa.

## Relação com Outros Artefatos

- [Architecture Vision](../docs/architecture-vision.md)
- [Decision Governance](../governance/decision-governance.md)
- [Reference Architecture](../observability-architecture/observability-reference-architecture.md)
