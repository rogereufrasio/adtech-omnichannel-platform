# Programa Estratégico 05 — Enterprise Observability Platform

> Landing page executiva do programa responsável por estabelecer observabilidade, confiabilidade e inteligência operacional como capacidades corporativas compartilhadas.

---

## Informações do Documento

| Item | Valor |
| --- | --- |
| Documento | Landing Page Executiva do Programa |
| Programa Estratégico | Enterprise Observability Platform |
| Domínio Arquitetural | Foundation |
| Responsável | Enterprise Architecture Practice |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O Programa Estratégico **Enterprise Observability Platform** estabelece padrões, serviços e governança para compreender a saúde de jornadas, produtos digitais, integrações, dados, modelos de IA e plataformas. A arquitetura correlaciona métricas, logs, traces, eventos e sinais de negócio, transformando telemetria em decisões operacionais e evidências de confiabilidade.

A plataforma não assume a operação dos produtos. Os times mantêm ownership de instrumentação, SLOs e resposta; o Programa 05 provê contratos de telemetria, ingestão, processamento, armazenamento, análise, alertas e experiência de autosserviço. Os Programas 02, 03 e 04 são baselines para dados/IA, integração e experiência Customer.

## Propósito

Reduzir tempo de detecção e recuperação, tornar confiabilidade mensurável e permitir decisões de operação, capacidade, risco e custo com evidências consistentes.

## Objetivos Estratégicos

| Objetivo | Resultado esperado |
| --- | --- |
| Padronizar telemetria | Sinais correlacionáveis e reutilizáveis |
| Gerir confiabilidade | SLI, SLO e error budgets por serviço e jornada |
| Acelerar resposta | Detecção e diagnóstico ponta a ponta |
| Controlar custo | Retenção, cardinalidade e unit economics governados |
| Habilitar inteligência operacional | Analytics e automação com supervisão |

## Business Outcomes

- menor MTTD e MTTR;
- maior cumprimento de SLOs;
- redução de incidentes recorrentes e toil;
- rastreabilidade de jornadas entre domínios;
- decisões de capacidade e custo baseadas em evidências;
- auditoria e compliance com telemetria protegida.

## Diagrama Executivo

Consulte o [Diagrama Executivo do Estado-Alvo](./diagrams/executive-target-state.md).

## Escopo

### Incluído

- métricas, logs, traces, events e sinais de experiência;
- catálogo de serviços, topology, SLI/SLO e error budgets;
- ingestão, processamento, storage, análise, alertas e incident intelligence;
- governança, segurança, FinOps, roadmap e ADRs.

### Fora do escopo

- ownership operacional dos produtos observados;
- plataforma de dados e IA do Programa 02;
- plataforma de integração do Programa 03;
- Customer Platform do Programa 04;
- substituição de ITSM, CI/CD ou ferramentas de segurança corporativas.

## Princípios Orientadores

| Princípio | Direcionamento |
| --- | --- |
| Observability by Design | Telemetria e SLO definidos no design |
| Service Ownership | Times respondem pelos serviços que operam |
| Open Standards First | Instrumentação e contratos portáveis |
| Signal Correlation | Contexto comum entre métricas, logs e traces |
| Privacy & Security by Design | Minimização, acesso e retenção governados |
| SLO over Alert Volume | Alertas acionáveis orientados ao impacto |
| Cost as Architecture | Cardinalidade, retenção e custo são decisões |

## Evolução Arquitetural

1. Foundation;
2. Business Architecture;
3. Information Architecture;
4. Application Architecture;
5. Technology Architecture;
6. Governance;
7. Roadmap;
8. Architecture Decision Records.

## Estrutura Documental e Navegação

| Bloco | Localização |
| --- | --- |
| Foundation | [docs](./docs/), [diagramas](./diagrams/) e documentos raiz |
| Business Architecture | [business-architecture](./business-architecture/) |
| Information Architecture | [information-architecture](./information-architecture/) |
| Application Architecture | [application-architecture](./application-architecture/) e [observability-architecture](./observability-architecture/) |
| Technology Architecture | [technology-architecture](./technology-architecture/) |
| Governance | [governance](./governance/) |
| Roadmap | [roadmap](./roadmap/) |
| ADRs | [adrs](./adrs/) |

## Roadmap da Documentação

| Ordem | Bloco | Estado no baseline |
| ---: | --- | --- |
| 1 | Foundation | Aprovado |
| 2 | Business Architecture | Aprovado |
| 3 | Information Architecture | Aprovado |
| 4 | Application Architecture | Aprovado |
| 5 | Technology Architecture | Aprovado |
| 6 | Governance | Aprovado |
| 7 | Roadmap | Aprovado |
| 8 | ADRs | Aprovado |

## Relação com Outros Artefatos

- [Architecture Vision](./docs/architecture-vision.md)
- [Architecture Target State](./architecture-target-state.md)
- [Programa Estratégico 02](../02-enterprise-data-ai-platform/README.md)
- [Programa Estratégico 03](../03-enterprise-integration-platform/README.md)
- [Programa Estratégico 04](../04-enterprise-customer-platform/README.md)
- [Princípios de Arquitetura Corporativa](../../docs/architecture-principles.md)

## Decisões Arquiteturais

### DA-FND-01 — Plataforma compartilhada, responsabilidade federada

A plataforma provê capacidades comuns; cada Product Team mantém instrumentação, SLO e resposta.

### DA-FND-02 — Observabilidade orientada a serviços e jornadas

Telemetria técnica será correlacionada a serviços, owners, dependências e outcomes.

### DA-FND-03 — Aprovação por blocos

Somente artefatos aprovados em Architecture Review integram o baseline.
