# Programa Estratégico 04 — Enterprise Customer Platform

> Landing page executiva do programa responsável por estabelecer Customer 360, identidade, consentimento, loyalty e personalização como capacidades corporativas integradas.

---

## Informações do Documento

| Item | Valor |
| --- | --- |
| Documento | Landing Page Executiva do Programa |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Foundation |
| Responsável | Enterprise Architecture Practice |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O Programa Estratégico **Enterprise Customer Platform** cria uma visão confiável, consentida e acionável do cliente para sustentar jornadas omnicanal, atendimento contextualizado, loyalty e personalização. A plataforma coordena capacidades de identidade, perfil, preferências, consentimento e ativação sem transferir o ownership dos dados de origem ou das decisões de negócio.

O Programa 02 é o baseline de dados, qualidade, analytics e IA. O Programa 03 é o baseline de APIs, eventos, contratos e mensageria. O Programa 04 reutiliza essas capacidades e estabelece o modelo específico do domínio Customer, evitando duplicidade de ingestão, integração e governança.

## Propósito

Transformar interações fragmentadas em relacionamentos coerentes, respeitando finalidade, privacidade e preferências do cliente em todo o ciclo de vida.

## Objetivos Estratégicos

| Objetivo | Resultado esperado |
| --- | --- |
| Unificar identidade | Golden Customer ID e vínculos explicáveis |
| Consolidar Customer 360 | Perfil governado, atual e consumível |
| Orquestrar consentimento | Uso de dados compatível com finalidade e canal |
| Habilitar personalização | Contexto confiável para decisões e experiências |
| Evoluir loyalty e atendimento | Relacionamentos consistentes entre canais |

## Business Outcomes

- maior reconhecimento do cliente entre canais;
- redução de registros duplicados e conflitos de identidade;
- experiências contextualizadas com consentimento verificável;
- menor tempo para disponibilizar segmentos e atributos;
- aumento de retenção, satisfação e efetividade de loyalty;
- evidências auditáveis sobre uso de dados pessoais.

## Diagrama Executivo

Consulte o [Diagrama Executivo do Estado-Alvo](./diagrams/executive-target-state.md).

## Escopo

### Incluído

- Customer Identity, Customer Profile, Consent & Preferences;
- Customer 360, loyalty, segmentação e personalização;
- serviços, aplicações e tecnologia específicos do domínio Customer;
- governança, métricas, roadmap e decisões arquiteturais.

### Fora do escopo

- plataforma corporativa de dados e IA, pertencente ao Programa 02;
- plataforma corporativa de integração, pertencente ao Programa 03;
- execução de mídia e AdTech, pertencente ao Programa 01;
- plataforma corporativa de observabilidade, pertencente ao Programa 05;
- substituição integral de CRM, commerce ou atendimento.

## Princípios Orientadores

| Princípio | Direcionamento |
| --- | --- |
| Customer Trust by Design | Transparência, escolha e proteção incorporadas |
| Privacy by Design | Finalidade, minimização, retenção e acesso governados |
| Domain Ownership | Fontes autoritativas preservam accountability |
| Identity before Profile | Identidade resolvida antes da consolidação |
| Data as a Product | Customer 360 com owner, qualidade, SLO e consumidores |
| API & Event First | Interações por contratos do Programa 03 |
| AI with Human Accountability | Personalização governada pelo Programa 02 |

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
| Application Architecture | [application-architecture](./application-architecture/) e [customer-architecture](./customer-architecture/) |
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
- [Business Context](./docs/business-context.md)
- [Programa Estratégico 02](../02-enterprise-data-ai-platform/README.md)
- [Programa Estratégico 03](../03-enterprise-integration-platform/README.md)
- [Princípios de Arquitetura Corporativa](../../docs/architecture-principles.md)

## Decisões Arquiteturais

### DA-FND-01 — Reutilização dos baselines corporativos

Dados, IA e integração reutilizam as capacidades aprovadas nos Programas 02 e 03.

### DA-FND-02 — Customer Platform não é sistema de registro universal

A plataforma consolida e serve contexto; fontes autoritativas permanecem responsáveis pelos dados mestres e transacionais.

### DA-FND-03 — Aprovação por blocos

Somente artefatos aprovados em Architecture Review integram o baseline.
