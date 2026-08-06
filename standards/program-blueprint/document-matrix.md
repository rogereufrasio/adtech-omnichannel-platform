# Matriz de Documentação dos Programas de Arquitetura Corporativa

## Objetivo

Esta matriz define o conjunto de documentos que compõem um **Enterprise Architecture Program**, estabelecendo sua obrigatoriedade, objetivo, momento de criação e responsabilidade de manutenção.

Ela serve como referência para:

- padronização da documentação;
- criação de novos programas;
- Architecture Reviews;
- automação dos validadores;
- governança documental.

---

# Legenda

| Campo | Descrição |
|--------|-----------|
| Obrigatório | Indica se o documento deve existir em todos os programas. |
| Fase | Momento recomendado para criação. |
| Responsável | Papel responsável pela manutenção do documento. |

---

# Documentos Raiz

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| README.md | Sim | Visão geral do programa. | Inicial | Enterprise Architect |
| architecture-target-state.md | Sim | Estado futuro da arquitetura. | Inicial | Enterprise Architect |
| executive-target-state.md | Sim | Resumo executivo da arquitetura-alvo. | Inicial | Enterprise Architect |
| maturity-assessment.md | Sim | Avaliação da maturidade arquitetural. | Planejamento | Enterprise Architect |

---

# Diretório docs

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| company-profile.md | Sim | Contexto organizacional. | Inicial | Enterprise Architect |
| business-context.md | Sim | Contexto de negócio. | Inicial | Business Architect |
| architecture-vision.md | Sim | Visão arquitetural do programa. | Inicial | Enterprise Architect |

---

# Diretório business-architecture

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| capability-map.md | Sim | Mapa de capacidades de negócio. | Descoberta | Business Architect |
| capability-assessment.md | Sim | Avaliação das capacidades atuais. | Descoberta | Business Architect |
| business-domains.md | Sim | Definição dos domínios de negócio. | Descoberta | Business Architect |
| business-value-streams.md | Sim | Cadeias de valor do negócio. | Descoberta | Business Architect |
| data-ownership-model.md | Opcional | Modelo de ownership dos dados. | Descoberta | Data Architect |

---

# Diretório application-architecture

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| application-landscape.md | Sim | Inventário das aplicações. | Análise | Solution Architect |
| application-interaction-model.md | Sim | Interações entre aplicações. | Análise | Solution Architect |
| application-architecture-principles.md | Sim | Princípios da arquitetura de aplicações. | Inicial | Enterprise Architect |
| api-strategy.md | Sim | Estratégia corporativa de APIs. | Planejamento | Integration Architect |
| integration-patterns.md | Sim | Padrões de integração. | Planejamento | Integration Architect |
| event-driven-architecture.md | Opcional | Estratégia Event-Driven. | Planejamento | Integration Architect |

---

# Diretório information-architecture

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| enterprise-information-model.md | Sim | Modelo corporativo de informações. | Planejamento | Data Architect |
| data-domain-model.md | Sim | Modelo de domínios de dados. | Planejamento | Data Architect |
| data-product-model.md | Opcional | Modelo de Data Products. | Planejamento | Data Architect |
| data-lifecycle-model.md | Sim | Ciclo de vida dos dados. | Planejamento | Data Architect |
| metadata-strategy.md | Sim | Estratégia de metadados. | Planejamento | Data Architect |

---

# Diretório technology-architecture

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| technology-platform.md | Sim | Plataforma tecnológica. | Planejamento | Technology Architect |
| technology-standards.md | Sim | Padrões tecnológicos. | Planejamento | Technology Architect |
| infrastructure-architecture.md | Sim | Arquitetura de infraestrutura. | Planejamento | Infrastructure Architect |
| security-architecture.md | Sim | Arquitetura de segurança. | Planejamento | Security Architect |
| observability-architecture.md | Opcional | Estratégia de observabilidade. | Planejamento | Platform Architect |

---

# Diretório governance

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| architecture-governance.md | Sim | Modelo de governança arquitetural. | Inicial | Enterprise Architect |
| architecture-metrics.md | Sim | Indicadores arquiteturais. | Evolução | Enterprise Architect |
| reference-architecture-compliance.md | Sim | Critérios de conformidade. | Evolução | Enterprise Architect |
| decision-governance.md | Sim | Governança das decisões arquiteturais. | Inicial | Enterprise Architect |
| data-governance-framework.md | Opcional | Governança de dados. | Planejamento | Data Architect |
| ai-governance-framework.md | Opcional | Governança de IA. | Planejamento | AI Architect |

---

# Diretório roadmap

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| implementation-roadmap.md | Sim | Roadmap de implementação. | Planejamento | Enterprise Architect |
| implementation-phases.md | Sim | Fases da transformação. | Planejamento | Enterprise Architect |
| architecture-evolution-plan.md | Sim | Evolução arquitetural. | Planejamento | Enterprise Architect |
| capability-evolution-roadmap.md | Sim | Evolução das capacidades. | Planejamento | Business Architect |
| success-metrics.md | Sim | Indicadores de sucesso. | Planejamento | Enterprise Architect |
| transformation-backlog.md | Opcional | Backlog da transformação. | Evolução | Enterprise Architect |

---

# Diretório adrs

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| README.md | Sim | Organização dos ADRs. | Inicial | Enterprise Architect |
| ADR-XXX.md | Sim | Registro de decisões arquiteturais. | Contínuo | Architecture Review Board |

---

# Diretório diagrams

| Documento | Obrigatório | Objetivo | Fase | Responsável |
|-----------|:-----------:|----------|-------|-------------|
| executive-target-state.md | Sim | Diagrama executivo da arquitetura-alvo. | Inicial | Enterprise Architect |

---

# Extensões por Domínio

Cada programa pode incluir diretórios especializados conforme seu domínio arquitetural.

Exemplos:

| Diretório | Exemplo de Programa |
|-----------|---------------------|
| ai-architecture | Enterprise Data & AI Platform |
| integration-architecture | Enterprise Integration Platform |
| customer-architecture | Enterprise Customer Platform |
| observability-architecture | Enterprise Observability Platform |
| security-architecture | Enterprise Security Platform |

Esses diretórios devem seguir os mesmos padrões de documentação, qualidade e governança definidos neste blueprint.

---

# Critérios de Qualidade

Todo documento deve possuir, no mínimo:

- título;
- objetivo;
- contexto;
- conteúdo estruturado;
- referências;
- linguagem técnica consistente;
- versionamento via Git.

---

# Referências

- `program-structure.md`
- `adr-template.md`
- `checklist.md`
- `../architecture-document-catalog.md`
- `../architecture-documentation-quality-checklist.md`
- `../architecture-review-process.md`