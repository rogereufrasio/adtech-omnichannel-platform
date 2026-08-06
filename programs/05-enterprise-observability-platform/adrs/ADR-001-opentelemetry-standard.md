# OpenTelemetry como Padrão de Instrumentação

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

Adotar OpenTelemetry APIs, SDKs, Collector e semantic conventions como padrão de instrumentação e transporte.

## Alternativas Consideradas

SDKs proprietários por ferramenta; agentes sem contrato; formato corporativo customizado.

## Consequências

### Positivas

Portabilidade, correlação e redução de acoplamento.

### Trade-offs e Riscos

Cobertura de bibliotecas varia e exige governança de versões e extensões.

## Critérios de Conformidade

A decisão deve ser evidenciada por contratos, configuração, testes, telemetria e operação. Exceções exigem owner, risco, compensação e validade.

## Gatilhos de Revisão

Mudanças materiais de escala, regulação, custo, modelo operacional ou capacidade corporativa.

## Relação com Outros Artefatos

- [Architecture Vision](../docs/architecture-vision.md)
- [Decision Governance](../governance/decision-governance.md)
- [Reference Architecture](../observability-architecture/observability-reference-architecture.md)
