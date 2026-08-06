# Customer 360 como Produto de Dados

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

Tratar Customer 360 como produto do domínio Customer sobre o Programa 02, com contrato, owner, qualidade, lineage e SLO; não como novo sistema universal de registro.

## Alternativas Consideradas

Golden record monolítico; data mart analítico sem contrato; cópias independentes por canal.

## Consequências

### Positivas

Reutilização e confiança sem retirar autoridade das fontes.

### Trade-offs e Riscos

Conciliação, precedência e freshness exigem gestão contínua.

## Critérios de Conformidade

A decisão deve ser verificável por design, contrato, testes, telemetria e evidências operacionais. Exceções exigem owner, risco, controle compensatório e validade.

## Gatilhos de Revisão

Mudança regulatória, de escala, modelo operacional, premissa de qualidade ou capacidade corporativa relacionada.

## Relação com Outros Artefatos

- [Architecture Vision](../docs/architecture-vision.md)
- [Decision Governance](../governance/decision-governance.md)
- [Customer Reference Architecture](../customer-architecture/customer-reference-architecture.md)
