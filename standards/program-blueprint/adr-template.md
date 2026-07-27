# Architecture Decision Record (ADR) Template

## Objetivo

Este documento define o modelo padrão para registro de **Architecture Decision Records (ADR)** utilizados pelos Enterprise Architecture Programs deste repositório.

Um ADR registra uma decisão arquitetural significativa, seu contexto, as alternativas avaliadas e as consequências decorrentes da decisão.

Todos os ADRs devem seguir este modelo para garantir consistência, rastreabilidade e facilidade de consulta.

---

# Convenções

## Nome do arquivo

Os arquivos devem seguir o padrão:

```text
adr-XXX-short-title.md
```

Onde:

- **XXX** representa um identificador sequencial de três dígitos;
- **short-title** é uma descrição curta utilizando letras minúsculas separadas por hífen.

Exemplos:

```text
adr-001-api-first.md
adr-002-event-driven-architecture.md
adr-003-data-as-a-product.md
```

---

# Template

```markdown
# ADR-XXX — Título da Decisão

## Status

Proposto

> Valores permitidos:
>
> - Proposto
> - Em Análise
> - Aprovado
> - Rejeitado
> - Substituído
> - Obsoleto

---

## Data

AAAA-MM-DD

---

## Autores

- Nome
- Nome

---

## Contexto

Descreva o problema, necessidade ou oportunidade que motivou esta decisão.

Inclua:

- contexto de negócio;
- contexto técnico;
- restrições;
- premissas;
- riscos conhecidos.

---

## Problema

Descreva claramente qual problema precisa ser resolvido.

---

## Decisão

Explique a decisão tomada.

A decisão deve ser objetiva, verificável e suficientemente detalhada para permitir sua compreensão futura.

---

## Alternativas Avaliadas

### Alternativa 1

Descrição.

**Prós**

-

**Contras**

-

---

### Alternativa 2

Descrição.

**Prós**

-

**Contras**

-

---

## Justificativa

Explique por que a alternativa escolhida foi considerada a mais adequada.

Considere aspectos como:

- alinhamento estratégico;
- simplicidade;
- custo;
- escalabilidade;
- segurança;
- governança;
- interoperabilidade;
- manutenção.

---

## Consequências

Descreva os impactos da decisão.

### Positivos

-

### Negativos

-

---

## Dependências

Liste decisões, tecnologias ou documentos relacionados.

Exemplo:

- ADR-001
- Architecture Target State
- Technology Platform

---

## Impactos

Indique quais áreas da arquitetura são afetadas.

Exemplo:

- Business Architecture
- Application Architecture
- Information Architecture
- Technology Architecture
- Governance

---

## Referências

Liste documentos utilizados como apoio para a decisão.

---

## Histórico

| Data | Alteração | Autor |
|------|-----------|-------|
| AAAA-MM-DD | Criação do ADR | Nome |
```

---

# Boas práticas

Um ADR deve:

- registrar apenas uma decisão principal;
- ser escrito de forma objetiva;
- permanecer imutável após aprovação, exceto pelo histórico;
- utilizar linguagem técnica e clara;
- evitar duplicação de conteúdo presente em outros documentos.

---

# Quando criar um ADR

Um ADR deve ser criado sempre que houver decisões relevantes relacionadas a:

- princípios arquiteturais;
- integração;
- APIs;
- eventos;
- dados;
- plataformas;
- segurança;
- observabilidade;
- governança;
- tecnologias estratégicas;
- padrões corporativos.

---

# Relacionamento com outros documentos

Os ADRs complementam a documentação arquitetural do programa.

Sempre que aplicável, um ADR deve referenciar documentos como:

- Architecture Target State;
- Executive Target State;
- Technology Platform;
- API Strategy;
- Event-Driven Architecture;
- Enterprise Information Model.

Da mesma forma, esses documentos podem referenciar ADRs para justificar decisões arquiteturais específicas.

---

# Ciclo de vida

O ciclo de vida recomendado para um ADR é:

```text
Proposto
      │
      ▼
Em Análise
      │
      ▼
Aprovado
      │
      ├──────────────► Obsoleto
      │
      └──────────────► Substituído
```

Caso uma decisão seja descartada antes da aprovação, o status deve ser alterado para **Rejeitado**.

---

# Governança

Os ADRs devem ser armazenados exclusivamente no diretório:

```text
adrs/
```

Todos os ADRs devem possuir numeração sequencial e permanecer versionados juntamente com o restante da documentação do programa.