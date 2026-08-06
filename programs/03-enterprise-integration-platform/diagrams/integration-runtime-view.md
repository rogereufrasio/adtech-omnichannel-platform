# Visão de Runtime da Integração

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Contexto

A visão de runtime descreve como o ambiente de execução processa APIs, mensagens e eventos na plataforma de integração.

## Objetivo

Mostrar a topologia de runtime, incluindo gateways, brokers, motores de integração e subsistemas de observabilidade.

```mermaid
flowchart LR
    subgraph Entrada
        CLIENTE[Cliente / Aplicação]
        SISTEMA[Sistemas Legados]
    end

    subgraph Runtime
        GW[API Gateway]
        AUTH[Autenticação / Autorização]
        ESB[Motor de Integração]
        TRANS[Transformação / Enriquecimento]
        MQ[Message Broker]
        EVENT[Event Mesh]
        SCHEMA[Registro de Schemas]
    end

    subgraph Operação
        LOGS[Logging Centralizado]
        TRACE[Rastreamento Distribuído]
        METRICS[Métricas / Observabilidade]
        ALERT[Alertas]
    end

    CLIENTE --> GW
    SISTEMA --> ESB
    GW --> AUTH
    AUTH --> ESB
    ESB --> TRANS
    TRANS --> MQ
    MQ --> EVENT
    EVENT --> SISTEMA
    EVENT --> CLIENTE
    SCHEMA --> EVENT
    SCHEMA --> ESB

    MQ --> LOGS
    MQ --> TRACE
    ESB --> METRICS
    GW --> ALERT
    TRACE --> METRICS
    METRICS --> ALERT
```

## Critérios de Leitura

- fronteiras de domínio e plataforma devem permanecer explícitas;
- fluxos síncronos e assíncronos devem ser diferenciados;
- controles de segurança e observabilidade aplicam-se transversalmente;
- componentes representam capacidades lógicas, não produtos selecionados.

## Referências

- Programa 03 README
- Technology Architecture
- Observability Architecture
- Runtime Architecture
