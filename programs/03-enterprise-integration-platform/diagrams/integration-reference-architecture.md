# Arquitetura de Referência de Integração

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Contexto

A arquitetura de referência de integração define os componentes, padrões e fluxos que sustentam a conectividade entre sistemas na plataforma do Programa 03.

## Objetivo

Representar visualmente a arquitetura de referência para APIs, eventos, mensageria e runtime de integração.

```mermaid
flowchart LR
    subgraph Fronteira
        GW[API Gateway]
        DEV[Portal de Desenvolvedores]
    end

    subgraph Integração
        ESB[Motor de Integração]
        BUS[Event Bus / Message Broker]
        TRANS[Transformação de Dados]
        AUTH[Segurança / Autenticação]
        MQ[Filas e Tópicos]
    end

    subgraph Suporte
        OBS[Observabilidade]
        GOV[Governança]
        CATALOG[Catálogo de APIs e Esquemas]
    end

    GW --> ESB
    GW --> BUS
    ESB --> TRANS
    TRANS --> MQ
    BUS --> OBS
    BUS --> GOV
    CATALOG --> GW
    CATALOG --> BUS
    AUTH --> GW
    AUTH --> BUS
```

## Critérios de Leitura

- fronteiras de domínio e plataforma devem permanecer explícitas;
- fluxos síncronos e assíncronos devem ser diferenciados;
- controles de segurança e observabilidade aplicam-se transversalmente;
- componentes representam capacidades lógicas, não produtos selecionados.

## Referências

- Programa 03 README
- Integration Architecture
- Governance Framework
- Princípios de Arquitetura Empresarial
