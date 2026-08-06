# Domínios de Negócio Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Business Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O modelo delimita responsabilidades entre Customer e domínios que originam ou consomem contexto do cliente.

## Domínios e Accountabilities

| Domínio | Accountability |
| --- | --- |
| Customer | Identidade consolidada, perfil, consentimento, preferência e experiência |
| Commerce | Pedidos, pagamentos, carrinho e comportamento transacional |
| Marketing | Estratégia de audiência, campanhas e mensuração |
| Service | Casos, interações e resolução |
| Loyalty | Regras, benefícios, pontos e parceiros |
| Data & AI | Produtos de dados, qualidade, analytics e modelos |
| Integration | APIs, eventos, contratos e entrega |
| Privacy & Security | Políticas, riscos, acesso e evidências |

## Fronteiras

Customer não assume ownership dos registros transacionais; consolida contexto sob regras aprovadas.

## Guardrails

- ownership e accountability devem ser explícitos;
- privacidade, segurança e observabilidade são requisitos de design;
- capacidades dos Programas 02 e 03 serão reutilizadas;
- exceções exigem risco, controle compensatório, owner e validade.

## Benefícios Esperados

Coerência omnicanal, menor duplicidade, decisões rastreáveis e evolução desacoplada dos domínios.

## Relação com Outros Artefatos

- [Capability Map](./capability-map.md)
- [Data Domain Model](../information-architecture/data-domain-model.md)
- [Programa 02](../../02-enterprise-data-ai-platform/README.md)

## Decisões Arquiteturais

As estruturas deste artefato integram o baseline normativo da Release 1.0 e orientam design, priorização e Architecture Review.
