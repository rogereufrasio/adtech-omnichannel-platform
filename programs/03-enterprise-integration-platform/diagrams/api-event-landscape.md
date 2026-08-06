# Panorama de APIs e Eventos

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Contexto

O panorama de APIs e eventos mostra a relação entre interfaces síncronas e fluxos assíncronos na plataforma de integração.

## Objetivo

Visualizar o ecossistema de APIs, eventos e consumidores para orientar design, governança e operação.

```mermaid
flowchart LR
    subgraph Fornecedores
        ORD[Ordem de Compra]
        CUST[Gestão de Clientes]
        INVENT[Gestão de Inventário]
    end

    subgraph Plataforma
        GATEWAY[API Gateway]
        EVENTS[Event Mesh]
        SCHEMA[Registro de Schemas]
        CATALOG[Catálogo de APIs/Eventos]
    end

    subgraph Consumidores
        CRM[CRM]
        OPS[Operações]
        ANALYTICS[Analytics]
        PARTNERS[Parceiros]
    end

    ORD --> GATEWAY
    CUST --> GATEWAY
    INVENT --> GATEWAY

    GATEWAY -->|API síncrona| CRM
    GATEWAY -->|API de orquestração| OPS
    GATEWAY --> SCHEMA
    GATEWAY --> CATALOG

    GATEWAY -->|Publica evento| EVENTS
    EVENTS --> ANALYTICS
    EVENTS --> OPS
    EVENTS --> PARTNERS
    EVENTS --> SCHEMA
    EVENTS --> CATALOG
```

## Critérios de Leitura

- fronteiras de domínio e plataforma devem permanecer explícitas;
- fluxos síncronos e assíncronos devem ser diferenciados;
- controles de segurança e observabilidade aplicam-se transversalmente;
- componentes representam capacidades lógicas, não produtos selecionados.

## Referências

- Programa 03 README
- Integration Architecture
- Event Governance
- API Governance
