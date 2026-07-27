# Enterprise Architecture Program Document Matrix

## Objetivo

Este documento define o catálogo oficial de documentos que compõem um Enterprise Architecture Program.

Para cada documento são definidos:

- obrigatoriedade;
- objetivo;
- fase em que deve ser produzido;
- responsável por sua manutenção.

Essa matriz serve como referência para:

- criação de novos programas;
- Architecture Reviews;
- validação documental;
- evolução do blueprint.

---

# Legenda

| Campo | Descrição |
|--------|-----------|
| Obrigatório | Indica se o documento faz parte da estrutura mínima do programa. |
| Fase | Momento recomendado para criação do documento. |
| Responsável | Papel responsável pela manutenção do documento. |

---

# Documentos da raiz

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|------------|-------------|----------|-------|-------------|
| README.md | Sim | Apresentar o programa e organizar sua documentação. | Iniciação | Enterprise Architect |
| architecture-target-state.md | Sim | Descrever a arquitetura alvo do programa. | Arquitetura | Enterprise Architect |
| executive-target-state.md | Sim | Comunicar a arquitetura alvo para executivos e stakeholders. | Arquitetura | Enterprise Architect |
| maturity-assessment.md | Sim | Avaliar a maturidade e identificar oportunidades de evolução. | Assessment | Enterprise Architect |

---

# Architecture Decision Records

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|------------|-------------|----------|-------|-------------|
| README.md | Sim | Explicar a organização dos ADRs. | Iniciação | Enterprise Architect |
| ADR | Sim | Registrar decisões arquiteturais relevantes. | Contínua | Enterprise Architect |

---

# Business Architecture

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|------------|-------------|----------|-------|-------------|
| business-domains.md | Sim | Definir os domínios de negócio. | Descoberta | Business Architect |
| business-value-streams.md | Sim | Descrever os fluxos de valor do negócio. | Descoberta | Business Architect |
| capability-map.md | Sim | Mapear capacidades de negócio. | Descoberta | Business Architect |

---

# Application Architecture

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|------------|-------------|----------|-------|-------------|
| application-landscape.md | Sim | Descrever o portfólio de aplicações. | Arquitetura | Solution Architect |
| api-strategy.md | Sim | Definir padrões e estratégia de APIs. | Arquitetura | Integration Architect |
| event-driven-architecture.md | Opcional | Definir arquitetura orientada a eventos quando aplicável. | Arquitetura | Integration Architect |

---

# Information Architecture

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|------------|-------------|----------|-------|-------------|
| enterprise-information-model.md | Sim | Definir o modelo corporativo de informação. | Arquitetura | Data Architect |
| data-domain-model.md | Sim | Organizar os domínios de dados. | Arquitetura | Data Architect |
| data-product-model.md | Opcional | Definir produtos de dados quando adotados. | Arquitetura | Data Architect |

---

# Technology Architecture

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|------------|-------------|----------|-------|-------------|
| technology-platform.md | Sim | Descrever a plataforma tecnológica. | Arquitetura | Enterprise Architect |
| security-architecture.md | Sim | Definir os princípios e componentes de segurança. | Arquitetura | Security Architect |
| observability-architecture.md | Opcional | Definir estratégia de observabilidade. | Arquitetura | Platform Architect |

---

# Governance

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|------------|-------------|----------|-------|-------------|
| architecture-governance.md | Sim | Definir o modelo de governança da arquitetura. | Governança | Enterprise Architect |
| data-governance-framework.md | Opcional | Definir governança de dados. | Governança | Data Architect |
| ai-governance-framework.md | Opcional | Definir governança para soluções de IA. | Governança | AI Architect |

---

# Roadmap

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|------------|-------------|----------|-------|-------------|
| implementation-roadmap.md | Sim | Planejar a implementação da arquitetura. | Planejamento | Enterprise Architect |
| architecture-evolution-plan.md | Sim | Definir a evolução arquitetural do programa. | Planejamento | Enterprise Architect |
| transformation-backlog.md | Sim | Organizar iniciativas e entregas de transformação. | Planejamento | Enterprise Architect |

---

# Diagramas

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|------------|-------------|----------|-------|-------------|
| executive-target-state.md | Sim | Armazenar diagramas executivos da arquitetura. | Arquitetura | Enterprise Architect |

---

# Atualização da matriz

Sempre que um novo tipo de documento for incorporado ao blueprint, esta matriz deverá ser atualizada antes da criação de novos programas.

O script `tools/architecture/create-program.py` deverá permanecer alinhado com esta matriz, garantindo que a estrutura inicial gerada reflita o padrão oficial definido pelo blueprint.