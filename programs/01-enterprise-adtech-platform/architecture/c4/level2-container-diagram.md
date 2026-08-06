# C4 - Nível 2 (Containers)

## Contexto

Este diagrama apresenta os containers lógicos da Enterprise AdTech Platform e suas principais interações.

```mermaid
flowchart LR

    Customer["Cliente"]

    Collection["Serviço de Coleta de Eventos"]

    Kafka["Kafka"]

    CDP["Customer Data Platform"]

    BigQuery["BigQuery"]

    Activation["Serviço de Ativação"]

    GoogleAds["Google Ads"]
    MetaAds["Meta Ads"]

    Customer --> Collection

    Collection --> Kafka

    Kafka --> CDP
    Kafka --> BigQuery

    CDP --> Activation

    Activation --> GoogleAds
    Activation --> MetaAds
```


## Relação com Outros Artefatos

- [Landing Page do Programa Estratégico 01](../../README.md)
