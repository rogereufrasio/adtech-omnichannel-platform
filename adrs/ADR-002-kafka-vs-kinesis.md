# ADR-002 — Kafka versus AWS Kinesis

## Status

Aprovado

## Contexto

A nova plataforma AdTech necessita de uma infraestrutura de streaming capaz de suportar distribuição de eventos em larga escala, múltiplos consumidores e independência tecnológica.

As alternativas avaliadas foram Apache Kafka e AWS Kinesis.

---

## Decisão

Adotar Apache Kafka como plataforma padrão de streaming corporativo.

---

## Justificativa

Apache Kafka apresentou vantagens relacionadas a:

* Independência de fornecedor;
* Ecossistema maduro;
* Ampla adoção de mercado;
* Flexibilidade de implantação;
* Capacidade de suportar múltiplos consumidores.

---

## Trade-offs

### Benefícios

* Menor lock-in tecnológico;
* Maior flexibilidade arquitetural;
* Comunidade ampla.

### Desvantagens

* Maior esforço operacional;
* Necessidade de governança adicional.

---

## Consequência

Kafka passa a ser o barramento padrão para eventos corporativos da plataforma AdTech.
