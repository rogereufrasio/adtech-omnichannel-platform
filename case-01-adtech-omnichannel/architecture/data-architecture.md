# Arquitetura de Dados

## Objetivo

Definir a estrutura de dados necessária para suportar a estratégia de Customer 360, segmentação de audiências e mensuração de campanhas da ShopSphere.

A arquitetura proposta busca garantir disponibilidade, governança e reutilização dos dados em toda a organização.

---

## Fluxo de Dados

A jornada dos dados inicia nos canais digitais e segue até as plataformas de análise e ativação.

```text
Canais Digitais
      ↓
Coleta de Eventos
      ↓
Streaming (Kafka)
      ↓
Processamento
      ↓
Customer Data Platform
      ↓
BigQuery / Data Lake
      ↓
Ativação e Analytics
```

Essa abordagem permite que diferentes consumidores utilizem os mesmos eventos sem dependências diretas entre sistemas.

---

## Domínios de Dados

A plataforma está organizada em domínios alinhados às capacidades de negócio da organização.

### Cliente

Responsável pelas informações cadastrais, consentimentos, preferências e atributos comportamentais.

Principais ativos:

* Perfil do Cliente
* Consentimentos
* Identificadores
* Customer 360

---

### Comercial

Responsável pelos dados relacionados a produtos, pedidos e transações.

Principais ativos:

* Catálogo de Produtos
* Pedidos
* Itens Vendidos
* Histórico de Compras

---

### Marketing

Responsável pela gestão de campanhas e audiências.

Principais ativos:

* Campanhas
* Audiências
* Segmentações
* Canais de Ativação

---

### Analytics

Responsável pela consolidação de métricas e indicadores de desempenho.

Principais ativos:

* KPIs de Marketing
* Dashboards Executivos
* Modelos de Atribuição
* Indicadores Operacionais

---

## Produtos de Dados

Os dados são disponibilizados como produtos reutilizáveis para diferentes consumidores.

### Customer 360

Visão unificada dos clientes da organização.

Consumidores:

* Marketing
* CRM
* Analytics
* Atendimento

---

### Segmentos de Audiência

Conjunto de segmentos utilizados para campanhas e jornadas personalizadas.

Consumidores:

* Google Ads
* Meta Ads
* CRM

---

### Dataset de Atribuição

Conjunto de dados utilizado para análise da efetividade das campanhas.

Consumidores:

* Marketing
* Analytics

---

### Dataset de Performance

Base consolidada de indicadores de campanhas e canais.

Consumidores:

* Liderança Executiva
* Marketing
* Produto

---

## Princípios de Dados

* Dados são tratados como ativos corporativos;
* Ownership definido por domínio;
* Governança integrada ao ciclo de vida dos dados;
* Catálogo obrigatório para produtos de dados;
* Qualidade monitorada continuamente.
