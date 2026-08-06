# Programa Estratégico 01 — Enterprise AdTech Platform

> Landing page executiva do programa responsável por modernizar o ecossistema AdTech, habilitando audiências governadas, ativação omnichannel e mensuração orientada a eventos.

---

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise AdTech Platform |
| Responsável | Enterprise Architecture Practice |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O Programa Estratégico **Enterprise AdTech Platform** define a transformação do ecossistema de marketing da ShopSphere, substituindo integrações batch e silos por coleta padronizada, event streaming, Customer 360, gestão de audiências e ativação governada.

O programa estabelece o primeiro domínio de transformação do portfólio e mantém boundaries explícitos com as capacidades corporativas posteriores de Data & AI, Integration, Customer e Observability.

## Objetivos Estratégicos

- habilitar Customer 360 e identity resolution;
- reduzir latência de segmentação e ativação;
- padronizar tracking, APIs e eventos;
- ampliar rastreabilidade e mensuração de campanhas;
- aplicar consentimento e governança de dados;
- reduzir acoplamento entre canais e plataformas de mídia.

## Diagrama Executivo

Consulte o [Diagrama Executivo do Estado-Alvo](./diagrams/executive-target-state.md).

## Escopo Arquitetural

| Capacidade | Responsabilidade do programa |
| --- | --- |
| Tracking | Coleta e validação de interações digitais |
| Event Streaming | Distribuição desacoplada dos eventos |
| Customer Data Platform | Perfis, identity resolution e audiências |
| Audience Activation | Sincronização com canais pagos e proprietários |
| Measurement | Eventos, atribuição e indicadores de campanha |
| Governance | Consentimento, ownership, schema e revisão |

## Princípios Orientadores

- Event-Driven Architecture;
- API First;
- Domain Ownership;
- Privacy by Design;
- contratos e schemas governados;
- observabilidade e segurança incorporadas.

## Navegação dos Artefatos

| Área | Localização |
| --- | --- |
| ADRs | [adrs](./adrs/) |
| APIs | [api](./api/) |
| Arquitetura | [architecture](./architecture/) |
| Diagramas | [diagrams](./diagrams/) |
| Documentação | [docs](./docs/) |
| Eventos | [events](./events/) |
| Governança | [governance](./governance/) |

## Artefatos Executivos

- [Architecture Vision](./docs/architecture-vision.md)
- [Architecture Target State](./docs/architecture-target-state.md)
- [Business Context](./docs/business-context.md)
- [Capability Map](./docs/capability-map.md)
- [Transformation Roadmap](./docs/transformation-roadmap.md)

## Decisões Arquiteturais

- [ADR-001 — Event-Driven Architecture](./adrs/ADR-001-event-driven-architecture.md)
- [ADR-002 — Kafka versus Kinesis](./adrs/ADR-002-kafka-vs-kinesis.md)
- [ADR-003 — Buy versus Build para CDP](./adrs/ADR-003-buy-vs-build-cdp.md)

## Relação com Outros Programas

- Programa 02 provê a plataforma corporativa de dados e IA;
- Programa 03 provê contratos e serviços corporativos de integração;
- Programa 04 governa a arquitetura corporativa de Customer 360;
- Programa 05 provê observabilidade e confiabilidade compartilhadas.

## Architecture Review

O programa e seus artefatos integram o baseline aprovado da Release 1.0.

**Status final: APPROVED.**
