# Customer Identity Resolution

## Informações da Decisão

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Status | Aceito |
| Versão | 1.0 |
| Decisor | Architecture Review Board |

## Contexto

A transformação Customer exige uma decisão uniforme, rastreável e coerente com os baselines dos Programas 02 e 03.

## Decisão

Adotar Golden Customer ID, identity graph e resolução híbrida determinística/probabilística, com confidence, histórico, reversibilidade e stewardship.

## Alternativas Consideradas

Chave única imposta a todas as fontes; matching apenas determinístico; produto fechado sem explicabilidade.

## Consequências

### Positivas

Reconhecimento omnicanal com vínculos auditáveis.

### Trade-offs e Riscos

Risco de false merge/split e necessidade de operação de stewardship.

## Critérios de Conformidade

A decisão deve ser verificável por design, contrato, testes, telemetria e evidências operacionais. Exceções exigem owner, risco, controle compensatório e validade.

## Gatilhos de Revisão

Mudança regulatória, de escala, modelo operacional, premissa de qualidade ou capacidade corporativa relacionada.

## Relação com Outros Artefatos

- [Architecture Vision](../docs/architecture-vision.md)
- [Decision Governance](../governance/decision-governance.md)
- [Customer Reference Architecture](../customer-architecture/customer-reference-architecture.md)
