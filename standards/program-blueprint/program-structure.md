# Estrutura Padrão de um Enterprise Architecture Program

## Objetivo

Este documento define a estrutura oficial utilizada por todos os Enterprise Architecture Programs deste repositório.

Seu objetivo é garantir padronização, previsibilidade, facilidade de navegação e suporte à automação dos processos de documentação e governança arquitetural.

---

# Estrutura de Diretórios

```text
program-xx-domain-name/
│
├── README.md
├── architecture-target-state.md
├── executive-target-state.md
├── maturity-assessment.md
│
├── adrs/
│   └── README.md
│
├── business-architecture/
├── application-architecture/
├── information-architecture/
├── technology-architecture/
├── governance/
├── roadmap/
├── diagrams/
├── docs/
│
└── <domain-specific-folders>
```

---

# Documentos da Raiz

| Documento | Objetivo |
|-----------|----------|
| README.md | Visão geral do programa |
| architecture-target-state.md | Arquitetura-alvo |
| executive-target-state.md | Resumo executivo |
| maturity-assessment.md | Avaliação de maturidade |

---

# Diretórios Obrigatórios

## adrs

Contém todas as decisões arquiteturais (Architecture Decision Records).

---

## business-architecture

Documentação da arquitetura de negócio.

Exemplos:

- Capability Map
- Value Streams
- Business Domains
- Capability Assessment

---

## application-architecture

Documentação da arquitetura de aplicações.

Exemplos:

- Application Landscape
- API Strategy
- Integration Patterns
- Interaction Model

---

## information-architecture

Modelos de informação corporativa.

Exemplos:

- Enterprise Information Model
- Data Domain Model
- Metadata Strategy
- Data Lifecycle

---

## technology-architecture

Arquitetura tecnológica.

Exemplos:

- Infrastructure
- Technology Platform
- Security Architecture
- Technology Standards

---

## governance

Governança da arquitetura.

Exemplos:

- Architecture Governance
- Decision Governance
- Architecture Metrics
- Compliance

---

## roadmap

Planejamento da evolução arquitetural.

Exemplos:

- Implementation Roadmap
- Architecture Evolution Plan
- Success Metrics

---

## diagrams

Diagramas executivos e arquiteturais.

Preferencialmente utilizando Mermaid.

---

## docs

Documentação de apoio.

Exemplos:

- Company Profile
- Business Context
- Architecture Vision

---

# Diretórios Específicos por Domínio

Cada programa pode incluir diretórios especializados quando necessário.

Exemplos:

| Programa | Diretório |
|----------|-----------|
| Enterprise Data & AI Platform | ai-architecture |
| Enterprise Integration Platform | integration-architecture |
| Enterprise Customer Platform | customer-architecture |
| Enterprise Security Platform | security-architecture |
| Enterprise Observability Platform | observability-architecture |

Esses diretórios complementam a estrutura padrão e não substituem os diretórios obrigatórios.

---

# Convenções de Nomenclatura

## Diretórios

- letras minúsculas;
- separados por hífen (`-`);
- nomes descritivos.

Exemplos:

```text
business-architecture
technology-architecture
integration-architecture
```

---

## Arquivos

- letras minúsculas;
- separados por hífen;
- extensão `.md`.

Exemplos:

```text
application-landscape.md
technology-platform.md
architecture-governance.md
```

---

## ADRs

Formato:

```text
adr-001-nome-da-decisao.md
```

Numeração sequencial.

---

# Organização dos Diagramas

Todos os diagramas devem:

- utilizar Mermaid sempre que possível;
- possuir sintaxe válida;
- ser versionados juntamente com a documentação;
- representar a arquitetura descrita nos documentos relacionados.

---

# Princípios

A estrutura do programa segue os seguintes princípios:

- padronização;
- modularidade;
- reutilização;
- rastreabilidade;
- simplicidade;
- escalabilidade;
- automação.

---

# Referências

- `README.md`
- `document-matrix.md`
- `checklist.md`
- `adr-template.md`
- `../architecture-document-catalog.md`