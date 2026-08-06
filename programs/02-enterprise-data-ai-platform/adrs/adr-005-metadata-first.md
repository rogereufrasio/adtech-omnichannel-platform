# ADR-005 — Metadata First

## Status

Aceito

## Data

2026-07-27

## Contexto

A Enterprise Data & AI Platform depende da capacidade de encontrar, compreender, confiar e utilizar dados corporativos de forma eficiente.

Em ambientes corporativos complexos, a quantidade de dados, fontes e consumidores cresce continuamente, tornando insuficientes abordagens baseadas apenas em armazenamento e integração técnica.

Sem uma estratégia consistente de metadados, surgem problemas como:

- dificuldade de descoberta dos dados;
- falta de entendimento semântico;
- baixa confiança nas informações;
- dificuldade de governança;
- pouca rastreabilidade;
- duplicação de ativos.

Metadados representam informações sobre os próprios dados, permitindo compreender:

- origem;
- significado;
- proprietário;
- qualidade;
- relacionamento;
- utilização.

O princípio **Metadata First** estabelece que metadados devem ser tratados como uma capacidade arquitetural fundamental da plataforma.

---

## Decisão

Adotar **Metadata First** como princípio arquitetural para gestão, governança e consumo de dados na Enterprise Data & AI Platform.

Toda capacidade relacionada a dados deverá considerar a criação e manutenção de metadados como requisito arquitetural.

A plataforma deverá suportar:

- catálogo de dados;
- glossário corporativo;
- classificação de informações;
- linhagem;
- ownership;
- indicadores de qualidade;
- contexto de consumo.

---

## Princípios derivados

### Metadados como ativo corporativo

Metadados devem ser tratados como informações estratégicas e não apenas documentação técnica.

---

### Contexto antes do consumo

Dados devem possuir contexto suficiente para permitir entendimento adequado antes da utilização.

Informações importantes incluem:

- significado;
- origem;
- responsável;
- regras de utilização.

---

### Catálogo como capacidade fundamental

Consumidores devem conseguir descobrir ativos disponíveis.

O catálogo deve permitir:

- busca;
- entendimento;
- solicitação de acesso;
- acompanhamento de qualidade.

---

### Governança baseada em informação

Decisões de governança devem utilizar metadados para controlar:

- acesso;
- classificação;
- qualidade;
- impacto de mudanças.

---

## Consequências da decisão

A adoção de Metadata First estabelece uma base de conhecimento sobre os dados corporativos, aumentando confiança, governança e reutilização.

---

## Impactos positivos

### Maior descoberta dos dados

Usuários conseguem localizar ativos existentes com maior facilidade.

---

### Maior entendimento semântico

Glossários e documentação reduzem interpretações divergentes.

---

### Melhor governança

Metadados permitem aplicar controles relacionados a:

- segurança;
- qualidade;
- conformidade;
- responsabilidade.

---

### Melhor suporte para IA

Modelos inteligentes se beneficiam de dados contextualizados e rastreáveis.

---

## Impactos negativos e desafios

### Necessidade de manutenção contínua

Metadados precisam acompanhar a evolução dos dados.

---

### Esforço inicial de organização

A criação de catálogo, glossário e classificação exige investimento inicial.

---

### Integração entre ferramentas

Diferentes plataformas precisam compartilhar informações de metadados.

---

## Alternativas consideradas

### Alternativa 1 — Documentação manual descentralizada

**Descrição**

Manter informações sobre dados em documentos individuais.

**Vantagens**

- baixo investimento inicial;
- implementação simples.

**Desvantagens**

- difícil manutenção;
- baixa confiabilidade;
- pouca escala.

**Decisão**

Não adotada.

---

### Alternativa 2 — Metadados apenas técnicos

**Descrição**

Controlar somente informações de infraestrutura e schemas.

**Vantagens**

- implementação mais simples;
- foco técnico.

**Desvantagens**

- ausência de contexto de negócio;
- baixa utilidade para consumidores.

**Decisão**

Não adotada.

---

### Alternativa 3 — Metadata First

**Descrição**

Tratar metadados como capacidade arquitetural essencial.

**Vantagens**

- governança;
- descoberta;
- confiança;
- escalabilidade.

**Desvantagens**

- exige disciplina contínua.

**Decisão**

Adotada.

---

## Relação com princípios arquiteturais

| Princípio | Relação |
|---|---|
| Metadata First | Define metadados como fundamento da plataforma |
| Data as a Product | Produtos de dados precisam de contexto e documentação |
| Data Governance Federated | Governança depende de informações confiáveis |
| Data Quality by Design | Qualidade deve ser registrada e acompanhada |
| Vendor Agnostic AI | IA depende de dados contextualizados |

---

## Roadmap de implementação

### Fase 1 — Fundação

Objetivos:

- definir modelo de metadados;
- criar padrões;
- identificar ativos prioritários.

---

### Fase 2 — Evolução

Objetivos:

- implementar catálogo;
- criar glossário corporativo;
- integrar fontes de dados.

---

### Fase 3 — Escala

Objetivos:

- automatizar captura de metadados;
- ampliar governança;
- integrar IA e analytics.

---

## Relação com Outros Artefatos

- [Metadata Strategy](../information-architecture/metadata-strategy.md)
- [Data Product Model](../information-architecture/data-product-model.md)
- [Data Governance Framework](../governance/data-governance-framework.md)
