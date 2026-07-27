# Enterprise Architecture Program Checklist

## Objetivo

Este checklist define os critérios mínimos de qualidade para um Enterprise Architecture Program.

Seu objetivo é garantir que todos os programas deste repositório sejam publicados com uma estrutura consistente, documentação completa e aderência aos padrões estabelecidos pelo blueprint.

Este checklist complementa as validações automatizadas disponíveis em:

```text
tools/architecture/
```

---

# Como utilizar

O checklist deve ser executado:

- durante a criação de um novo programa;
- antes de uma Architecture Review;
- antes da publicação de uma nova versão;
- sempre que houver mudanças estruturais significativas.

Cada item deve ser marcado como:

- **[ ]** Não atendido
- **[x]** Atendido
- **N/A** Não aplicável

---

# Estrutura do programa

## Diretório principal

- [ ] O programa segue o padrão `NN-program-name`.
- [ ] O número do programa é único.
- [ ] O nome utiliza letras minúsculas e hífens.
- [ ] A estrutura segue o blueprint oficial.

---

## Documentos da raiz

- [ ] README.md
- [ ] architecture-target-state.md
- [ ] executive-target-state.md
- [ ] maturity-assessment.md

---

## Diretórios obrigatórios

- [ ] adrs/
- [ ] business-architecture/
- [ ] application-architecture/
- [ ] information-architecture/
- [ ] technology-architecture/
- [ ] governance/
- [ ] roadmap/
- [ ] diagrams/

---

# Business Architecture

- [ ] Business Domains documentado.
- [ ] Business Value Streams documentado.
- [ ] Capability Map documentado.

---

# Application Architecture

- [ ] Application Landscape documentado.
- [ ] API Strategy documentada.
- [ ] Estratégia de integração documentada.
- [ ] Arquitetura orientada a eventos documentada quando aplicável.

---

# Information Architecture

- [ ] Enterprise Information Model documentado.
- [ ] Data Domain Model documentado.
- [ ] Data Product Model documentado quando aplicável.

---

# Technology Architecture

- [ ] Technology Platform documentada.
- [ ] Security Architecture documentada.
- [ ] Observability Architecture documentada quando aplicável.

---

# Governance

- [ ] Architecture Governance documentada.
- [ ] Data Governance documentada quando aplicável.
- [ ] AI Governance documentada quando aplicável.

---

# Roadmap

- [ ] Implementation Roadmap documentado.
- [ ] Architecture Evolution Plan documentado.
- [ ] Transformation Backlog documentado.

---

# Architecture Decision Records

- [ ] Diretório `adrs/` criado.
- [ ] README.md presente.
- [ ] ADRs seguem o template oficial.
- [ ] ADRs possuem numeração sequencial.
- [ ] Todos os ADRs possuem status definido.
- [ ] Todos os ADRs possuem contexto, decisão e consequências.

---

# Diagramas

- [ ] Diagramas armazenados no diretório correto.
- [ ] Diagramas atualizados.
- [ ] Diagramas consistentes com a documentação.
- [ ] Diagramas utilizam Mermaid quando possível.

---

# Qualidade documental

- [ ] Todos os documentos possuem título.
- [ ] Todos os documentos possuem objetivo.
- [ ] Não existem documentos duplicados.
- [ ] Não existem links quebrados.
- [ ] Terminologia consistente em todo o programa.
- [ ] Convenções de nomenclatura respeitadas.

---

# Consistência arquitetural

- [ ] Arquitetura alvo consistente com os princípios corporativos.
- [ ] Componentes arquiteturais coerentes entre si.
- [ ] Não existem conflitos entre documentos.
- [ ] ADRs refletem as principais decisões arquiteturais.

---

# Automação

- [ ] O programa pode ser validado pelos scripts de documentação.
- [ ] Não há erros de estrutura.
- [ ] Não há arquivos obrigatórios ausentes.

---

# Critérios para conclusão

Um Enterprise Architecture Program é considerado aderente ao blueprint quando:

- todos os documentos obrigatórios estiverem presentes;
- a estrutura seguir o padrão oficial;
- os documentos atenderem aos critérios mínimos de qualidade;
- as decisões arquiteturais estiverem registradas em ADRs quando aplicável;
- o programa puder ser validado pelos mecanismos automatizados disponíveis no repositório.

---

# Referências

- `README.md`
- `program-structure.md`
- `document-matrix.md`
- `adr-template.md`
- `standards/architecture-documentation-quality-checklist.md`
- `standards/architecture-review-process.md`