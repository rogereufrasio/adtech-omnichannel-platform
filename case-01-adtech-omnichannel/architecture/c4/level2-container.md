# C4 - Nível 2 (Containers)

## Objetivo

Descrever os principais componentes que compõem a Plataforma AdTech da ShopSphere e suas respectivas responsabilidades.

---

## Serviço de Coleta de Eventos

Responsável pela captura e validação das interações realizadas pelos clientes nos canais digitais.

### Responsabilidades

- Receber eventos de navegação e conversão;
- Validar estrutura dos eventos;
- Padronizar payloads;
- Publicar eventos na plataforma de streaming.

### Tecnologias

- APIs REST
- Server-Side Tracking
- SDKs Web e Mobile

---

## Plataforma de Streaming

Responsável pela distribuição e persistência dos eventos de negócio.

### Responsabilidades

- Distribuição de eventos;
- Persistência temporária;
- Reprocessamento de eventos;
- Desacoplamento entre produtores e consumidores.

### Tecnologias

- Apache Kafka
- Schema Registry
- Dead Letter Queue

---

## Customer Data Platform (CDP)

Responsável pela consolidação da visão unificada do cliente.

### Responsabilidades

- Resolução de Identidade;
- Consolidação de perfis;
- Gestão de audiências;
- Enriquecimento de atributos.

### Tecnologia

- Adobe Experience Platform

---

## Plataforma de Dados

Responsável pelo armazenamento e processamento analítico dos dados.

### Responsabilidades

- Armazenamento histórico;
- Analytics;
- Modelagem de dados;
- Suporte a Machine Learning.

### Tecnologias

- BigQuery
- Data Lake
- Feature Store

---

## Serviço de Ativação

Responsável pela distribuição de audiências e atributos para plataformas externas.

### Responsabilidades

- Sincronização de audiências;
- Publicação de segmentos;
- Ativação de campanhas.

### Integrações

- Google Ads
- Meta Ads
- CRM

---

## Serviços de Governança

Responsáveis por garantir qualidade, conformidade e observabilidade da plataforma.

### Responsabilidades

- Gestão de consentimento;
- Qualidade de dados;
- Catálogo de metadados;
- Monitoramento operacional;
- Auditoria e rastreabilidade.

### Tecnologias

- OneTrust
- Data Catalog
- Datadog