# ADR-003 — Data as a Product

## Status

Aceito

## Data

2026-07-27

## Contexto

A Enterprise Data & AI Platform tem como objetivo transformar dados corporativos em ativos estratégicos capazes de suportar decisões, automações e soluções inteligentes.

Historicamente, dados corporativos são frequentemente tratados como subprodutos de sistemas transacionais, sendo disponibilizados sem definição clara de responsabilidade, qualidade ou experiência de consumo.

Esse modelo gera desafios como:

- baixa confiança nos dados;
- dificuldade de entendimento semântico;
- ausência de ownership;
- retrabalho por consumidores;
- duplicação de pipelines;
- baixa reutilização.

Com a evolução para uma arquitetura orientada a dados, os dados devem ser tratados como produtos corporativos, possuindo:

- consumidores identificados;
- responsáveis definidos;
- documentação;
- qualidade mensurada;
- ciclo de vida gerenciado.

O conceito de **Data as a Product** estabelece que dados devem ser disponibilizados considerando necessidades dos consumidores, da mesma forma que produtos digitais são desenvolvidos e evoluem.

---

## Decisão

Adotar **Data as a Product** como princípio arquitetural para gestão, disponibilização e consumo dos dados corporativos.

Cada produto de dados deverá possuir:

- domínio responsável;
- proprietário definido;
- documentação;
- catálogo;
- indicadores de qualidade;
- contratos de consumo;
- ciclo de vida.

Os produtos de dados deverão ser projetados considerando:

- descoberta;
- confiabilidade;
- acessibilidade;
- interoperabilidade;
- evolução contínua.

---

## Princípios derivados

### Ownership explícito dos dados

Todo produto de dados deve possuir um responsável claramente definido.

O domínio responsável deve garantir:

- significado;
- qualidade;
- disponibilidade;
- evolução.

---

### Dados orientados ao consumidor

Produtos de dados devem considerar seus consumidores como clientes internos.

Devem responder:

- quem utiliza;
- para qual finalidade;
- quais garantias são necessárias;
- como será consumido.

---

### Qualidade incorporada ao produto

Qualidade deve fazer parte da definição do produto de dados.

Devem existir indicadores relacionados a:

- completude;
- consistência;
- atualidade;
- precisão;
- confiabilidade.

---

### Dados como ativos reutilizáveis

Produtos de dados devem evitar criação de soluções isoladas.

A arquitetura deve incentivar:

- compartilhamento;
- reutilização;
- padronização.

---

## Consequências da decisão

A adoção de Data as a Product transforma dados corporativos em capacidades reutilizáveis, governadas e orientadas ao valor.

---

## Impactos positivos

### Maior confiança nos dados

Consumidores passam a utilizar informações com maior segurança.

---

### Redução de duplicidade

Produtos de dados reutilizáveis reduzem:

- cópias desnecessárias;
- pipelines redundantes;
- interpretações divergentes.

---

### Maior alinhamento entre negócio e tecnologia

Domínios passam a participar diretamente da gestão dos seus ativos de dados.

---

### Melhor suporte para Analytics e IA

Dados contextualizados e governados aumentam a qualidade de:

- análises;
- modelos preditivos;
- automações inteligentes.

---

## Impactos negativos e desafios

### Mudança cultural

Áreas de negócio precisam assumir responsabilidade sobre dados.

---

### Necessidade de novos papéis

A adoção exige definição de responsabilidades como:

- Data Owner;
- Data Steward;
- consumidor de dados.

---

### Investimento inicial

Criar produtos de dados exige:

- documentação;
- governança;
- indicadores;
- processos.

---

## Alternativas consideradas

### Alternativa 1 — Dados como subproduto dos sistemas

**Descrição**

Manter dados como responsabilidade exclusiva dos sistemas de origem.

**Vantagens**

- menor esforço inicial;
- modelo tradicional conhecido.

**Desvantagens**

- baixa reutilização;
- pouca governança;
- dificuldade analítica.

**Decisão**

Não adotada.

---

### Alternativa 2 — Data Warehouse centralizado como solução principal

**Descrição**

Centralizar todos os dados em uma estrutura analítica única.

**Vantagens**

- controle central;
- padronização inicial.

**Desvantagens**

- gargalos;
- baixa autonomia dos domínios;
- dificuldade de escala.

**Decisão**

Não adotada como abordagem exclusiva.

---

### Alternativa 3 — Data as a Product

**Descrição**

Tratar dados como produtos com consumidores, ownership e evolução contínua.

**Vantagens**

- maior confiança;
- escalabilidade;
- alinhamento com negócio.

**Desvantagens**

- exige mudança organizacional.

**Decisão**

Adotada.

---

## Relação com princípios arquiteturais

| Princípio | Relação |
|---|---|
| Data as a Product | Define dados como ativos corporativos evolutivos |
| Metadata First | Produtos precisam de contexto e documentação |
| Data Governance Federated | Domínios são responsáveis pelos dados |
| Security by Design | Produtos devem respeitar políticas de acesso |
| AI by Design | IA depende de dados confiáveis |

---

## Roadmap de implementação

### Fase 1 — Fundação

Objetivos:

- identificar produtos de dados prioritários;
- definir ownership;
- estabelecer padrões;
- criar catálogo inicial.

---

### Fase 2 — Evolução

Objetivos:

- disponibilizar produtos de dados;
- implementar indicadores de qualidade;
- estabelecer contratos de consumo.

---

### Fase 3 — Escala

Objetivos:

- ampliar domínios;
- automatizar governança;
- integrar produtos de dados com IA e analytics.

---

## Status

Aceito