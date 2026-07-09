# ADR-001 — Adoção de Arquitetura Orientada a Eventos

## Status

Aprovado

## Contexto

A ShopSphere opera múltiplos canais digitais, plataformas de marketing, CRM e parceiros de mídia que necessitam compartilhar informações sobre clientes, campanhas e interações de forma contínua.

A arquitetura atual é baseada predominantemente em integrações ponto a ponto e processos batch executados em intervalos periódicos. Esse modelo gera atrasos na disponibilidade das informações, aumenta o acoplamento entre sistemas e dificulta a evolução da plataforma.

Além disso, a estratégia de Customer 360 e ativação omnichannel exige que eventos de negócio sejam disponibilizados para diferentes consumidores com baixa latência.

---

## Decisão

Adotar uma Arquitetura Orientada a Eventos (Event-Driven Architecture) como padrão para integração entre sistemas e plataformas da solução AdTech.

Eventos de negócio passam a representar o mecanismo preferencial para compartilhamento de informações entre domínios, permitindo que múltiplos consumidores utilizem os mesmos dados sem dependências diretas entre si.

A plataforma de streaming baseada em Apache Kafka será responsável pela distribuição, persistência e disponibilização desses eventos.

---

## Consequências Positivas

- Redução do acoplamento entre sistemas;
- Maior escalabilidade da plataforma;
- Compartilhamento eficiente de eventos entre múltiplos consumidores;
- Menor dependência de integrações batch;
- Possibilidade de processamento em tempo quase real;
- Facilidade para inclusão de novos consumidores sem impacto nos produtores.

---

## Consequências Negativas

- Maior complexidade operacional;
- Necessidade de governança de eventos;
- Curva de aprendizado para equipes de desenvolvimento;
- Necessidade de observabilidade específica para fluxos assíncronos.

---

## Alternativas Avaliadas

### Integrações Ponto a Ponto

Vantagens:

- Simplicidade inicial;
- Menor investimento de curto prazo.

Desvantagens:

- Forte acoplamento;
- Escalabilidade limitada;
- Crescimento exponencial das integrações.

---

### Integrações Batch

Vantagens:

- Modelo conhecido pela organização;
- Baixa complexidade operacional.

Desvantagens:

- Alta latência;
- Dificuldade para ativações em tempo hábil;
- Menor flexibilidade para novos casos de uso.

---

## Justificativa

Considerando os objetivos estratégicos da ShopSphere relacionados a Customer 360, ativação omnichannel e personalização em tempo quase real, a Arquitetura Orientada a Eventos oferece o melhor equilíbrio entre escalabilidade, flexibilidade e capacidade de evolução da plataforma.