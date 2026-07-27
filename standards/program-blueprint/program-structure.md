# Enterprise Architecture Program Structure

## Objetivo

Este documento define a estrutura padrão que deve ser utilizada por todos os Enterprise Architecture Programs deste repositório.

A padronização da estrutura garante consistência entre programas, facilita a navegação, reduz o esforço de manutenção e permite a automação da criação de novos programas.

---

# Estrutura padrão

Todo programa deve seguir a seguinte organização de diretórios:

```text
programs/
└── NN-program-name/
    ├── README.md
    ├── architecture-target-state.md
    ├── executive-target-state.md
    ├── maturity-assessment.md
    │
    ├── adrs/
    │   ├── README.md
    │   └── adr-xxx-*.md
    │
    ├── business-architecture/
    │
    ├── application-architecture/
    │
    ├── information-architecture/
    │
    ├── technology-architecture/
    │
    ├── governance/
    │
    ├── roadmap/
    │
    └── diagrams/
```

---

# Diretório raiz

O diretório principal representa um programa completo de Arquitetura Corporativa.

O nome deve seguir o padrão:

```text
NN-program-name
```

Onde:

- **NN** corresponde ao número sequencial do programa;
- **program-name** corresponde ao nome do domínio utilizando letras minúsculas e hífens.

Exemplos:

```text
01-enterprise-business-architecture
02-enterprise-data-ai-platform
03-enterprise-integration-platform
04-enterprise-security-platform
```

---

# Documentos da raiz

Os documentos localizados na raiz representam a visão geral do programa.

## README.md

Documento de entrada do programa.

Deve apresentar:

- propósito;
- escopo;
- objetivos;
- organização;
- documentos relacionados.

---

## architecture-target-state.md

Define a arquitetura alvo completa do programa.

Deve conter:

- visão arquitetural;
- capacidades;
- componentes;
- princípios;
- direcionadores.

---

## executive-target-state.md

Versão executiva da arquitetura alvo.

Destinada à comunicação com liderança e stakeholders.

---

## maturity-assessment.md

Avaliação do estado atual da arquitetura.

Pode incluir:

- maturidade;
- lacunas;
- riscos;
- oportunidades.

---

# Diretório adrs

Contém todos os Architecture Decision Records (ADR).

Estrutura:

```text
adrs/
├── README.md
├── adr-001-*.md
├── adr-002-*.md
└── ...
```

Cada ADR representa uma decisão arquitetural registrada e aprovada.

---

# Business Architecture

```text
business-architecture/
```

Reúne toda a documentação relacionada ao negócio.

Exemplos:

- Business Domains
- Capability Map
- Business Value Streams
- Organization Mapping
- Business Processes

---

# Application Architecture

```text
application-architecture/
```

Reúne toda a documentação da arquitetura de aplicações.

Exemplos:

- Application Landscape
- API Strategy
- Integration Strategy
- Event-Driven Architecture
- Service Landscape

---

# Information Architecture

```text
information-architecture/
```

Centraliza a documentação relacionada aos dados corporativos.

Exemplos:

- Enterprise Information Model
- Data Domain Model
- Data Product Model
- Metadata Strategy
- Master Data

---

# Technology Architecture

```text
technology-architecture/
```

Define os componentes tecnológicos da solução.

Exemplos:

- Technology Platform
- Security Architecture
- Observability
- Infrastructure
- Cloud Platform

---

# Governance

```text
governance/
```

Documenta os processos de governança da arquitetura.

Exemplos:

- Architecture Governance
- Data Governance
- AI Governance
- Standards
- Review Process

---

# Roadmap

```text
roadmap/
```

Contém o planejamento evolutivo do programa.

Exemplos:

- Implementation Roadmap
- Architecture Evolution Plan
- Transformation Backlog
- Releases
- Milestones

---

# Diagrams

```text
diagrams/
```

Armazena diagramas utilizados pela documentação.

Sempre que possível:

- utilizar Mermaid;
- manter diagramas próximos aos documentos relacionados;
- evitar duplicação.

---

# Convenções de nomenclatura

Todos os arquivos devem utilizar:

- letras minúsculas;
- palavras separadas por hífen;
- nomes descritivos;
- extensão `.md`.

Exemplo:

```text
enterprise-information-model.md
```

Evitar:

```text
EnterpriseInformationModel.md
enterprise_information_model.md
doc1.md
```

---

# Organização dos documentos

Cada documento deve pertencer a apenas uma categoria arquitetural.

Evitar:

- duplicação de conteúdo;
- documentos equivalentes em múltiplas pastas;
- referências cruzadas desnecessárias.

Quando necessário, utilizar links relativos entre documentos.

---

# Evolução da estrutura

Novos diretórios somente devem ser adicionados quando houver justificativa arquitetural clara.

Sempre que uma alteração estrutural for incorporada ao blueprint:

1. atualizar este documento;
2. atualizar a matriz documental;
3. atualizar o script de scaffold;
4. manter compatibilidade com os programas futuros.

O Programa 02 permanece como referência histórica da evolução do padrão estrutural.