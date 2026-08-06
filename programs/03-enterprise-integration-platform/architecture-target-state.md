# Estado-Alvo da Arquitetura

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Integration Platform |
| Domínio Arquitetural | Foundation |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O estado-alvo estabelece integração empresarial como uma capacidade corporativa compartilhada, composta por APIs, eventos e mensageria sob contratos, segurança, observabilidade e governança comuns.

## Arquitetura-Alvo

| Camada | Capacidades |
| --- | --- |
| Experiência | Portal, catálogo, documentação e autosserviço |
| Produtos de integração | APIs, eventos, mensagens e schemas |
| Plataforma | API Management, streaming, mensageria e runtime |
| Operação | SLOs, telemetria, incidentes e capacidade |
| Controle | Segurança, governança, compliance e FinOps |

## Princípios Arquiteturais

- API First e Contract First;
- Event-Driven Architecture;
- domain ownership;
- Security e Observability by Design;
- conformidade automatizada;
- evolução compatível e baixo acoplamento.

## Boundaries

A plataforma executa e governa interações, mas não assume ownership de dados, regras ou processos dos domínios. Dados e IA pertencem ao Programa 02; Customer Platform pertence ao Programa 04; observabilidade corporativa pertence ao Programa 05.

## Relação com Outros Artefatos

- [Architecture Vision](./docs/architecture-vision.md)
- [Diagrama Executivo](./diagrams/executive-target-state.md)
- [Arquitetura de Referência](./integration-architecture/enterprise-integration-reference-architecture.md)
- [Landing Page](./README.md)
