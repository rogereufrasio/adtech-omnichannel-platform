# ADR-002 — Event Driven Architecture

## Status

Aceito

## Data

2026-07-27

## Contexto

A evolução da Enterprise Data & AI Platform exige integração entre múltiplos domínios, aplicações e capacidades digitais.

Arquiteturas baseadas exclusivamente em chamadas síncronas apresentam limitações em cenários de grande escala:

- alto acoplamento entre sistemas;
- dependência de disponibilidade imediata;
- dificuldade de processamento em larga escala;
- baixa flexibilidade para evolução.

A arquitetura orientada a eventos permite que sistemas produtores publiquem mudanças relevantes sem depender diretamente dos consumidores.

Essa abordagem favorece:

- desacoplamento;
- escalabilidade;
- processamento distribuído;
- integração entre domínios.

Eventos representam fatos relevantes do negócio e permitem que diferentes consumidores reajam de forma independente.

---

## Decisão

Adotar **Event Driven Architecture** como padrão arquitetural para integrações que demandem desacoplamento, processamento assíncrono ou distribuição de informações entre domínios.

Eventos deverão ser utilizados especialmente para:

- comunicação entre domínios;
- propagação de mudanças relevantes;
- integração de processos distribuídos;
- processamento analítico e inteligente.

Eventos deverão possuir:

- contratos definidos;
- versionamento;
- governança;
- rastreabilidade;
- observabilidade.

---

## Princípios derivados

### Eventos representam fatos de negócio

Eventos devem representar acontecimentos relevantes.

Exemplos:

- cliente criado;
- contrato atualizado;
- pagamento realizado;
- sinistro registrado.

---

### Produtores e consumidores desacoplados

Produtores não devem possuir conhecimento direto dos consumidores.

Cada consumidor deve evoluir de forma independente.

---

### Contratos de eventos

Eventos devem possuir contratos explícitos contendo:

- estrutura;
- significado;
- versão;
- regras de evolução.

---

### Processamento orientado a reações

Consumidores devem reagir aos eventos conforme suas próprias necessidades.

Isso permite:

- novos consumidores sem alteração no produtor;
- evolução independente;
- maior flexibilidade.

---

## Consequências da decisão

A adoção de Event Driven Architecture estabelece uma base de integração distribuída, permitindo maior escalabilidade e evolução independente dos domínios.

---

## Impactos positivos

### Redução de acoplamento

Sistemas deixam de depender diretamente uns dos outros para comunicação.

---

### Maior escalabilidade

Consumidores podem processar eventos conforme sua capacidade.

---

### Maior capacidade de inovação

Novos consumidores podem utilizar eventos existentes sem alterar sistemas produtores.

---

### Melhor suporte para dados e IA

Eventos permitem captura de mudanças em tempo próximo ao real para:

- análises;
- automações;
- modelos inteligentes.

---

## Impactos negativos e desafios

### Maior complexidade operacional

Arquiteturas orientadas a eventos exigem:

- monitoramento;
- rastreamento;
- tratamento de falhas.

---

### Necessidade de governança

Grande quantidade de eventos exige controle sobre:

- contratos;
- versões;
- ownership.

---

### Consistência eventual

Alguns cenários deixam de possuir atualização imediata entre todos os componentes.

---

## Alternativas consideradas

### Alternativa 1 — Integração síncrona tradicional

**Descrição**

Utilizar chamadas diretas entre sistemas.

**Vantagens**

- modelo simples;
- resposta imediata.

**Desvantagens**

- alto acoplamento;
- menor escalabilidade.

**Decisão**

Não adotada como padrão principal.

---

### Alternativa 2 — Integração baseada em arquivos

**Descrição**

Trocar informações através de arquivos periódicos.

**Vantagens**

- simples implementação;
- baixo custo inicial.

**Desvantagens**

- baixa velocidade;
- pouca rastreabilidade;
- dificuldade de evolução.

**Decisão**

Não adotada.

---

### Alternativa 3 — Event Driven Architecture

**Descrição**

Utilizar eventos como mecanismo de comunicação entre componentes.

**Vantagens**

- desacoplamento;
- escalabilidade;
- flexibilidade.

**Desvantagens**

- maior maturidade necessária.

**Decisão**

Adotada.

---

## Relação com princípios arquiteturais

| Princípio | Relação |
|---|---|
| Event Driven Integration | Define eventos como padrão de integração distribuída |
| API First | APIs e eventos são mecanismos complementares |
| Data as a Product | Eventos podem alimentar produtos de dados |
| Metadata First | Eventos precisam de contexto e documentação |
| Cloud Native Platform | Arquiteturas distribuídas suportam processamento escalável |

---

## Roadmap de implementação

### Fase 1 — Fundação

Objetivos:

- definir padrões de eventos;
- estabelecer governança;
- identificar eventos prioritários.

---

### Fase 2 — Evolução

Objetivos:

- implementar plataforma de eventos;
- migrar integrações prioritárias;
- criar contratos versionados.

---

### Fase 3 — Escala

Objetivos:

- ampliar uso entre domínios;
- integrar analytics e IA;
- evoluir arquitetura orientada a eventos corporativa.

---

## Status

Aceito