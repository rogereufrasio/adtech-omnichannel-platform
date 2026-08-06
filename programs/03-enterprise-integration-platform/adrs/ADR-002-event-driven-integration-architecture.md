# ADR-002 — Arquitetura de Integração Orientada a Eventos

## Informações da Decisão

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Integration Platform |
| Status | Aceito |
| Versão | 1.0 |
| Decisor | Architecture Review Board |

## Contexto

A integração baseada apenas em padrões síncronos não atende aos requisitos de escalabilidade e desacoplamento exigidos pelos processos de negócio em tempo real.

## Objetivo

Adotar uma arquitetura orientada a eventos para permitir comunicação assíncrona, maior resiliência e flexibilidade na evolução de sistemas.

## Visão Geral da Arquitetura

Eventos de negócio são tratados como primeiro cidadão na plataforma. Produtores publicam eventos em tópicos ou streams, e consumidores se inscrevem de modo independente. Um registro de esquemas garante interoperabilidade e compatibilidade.

## Decisões Arquiteturais

- Utilizar um event bus/streaming platform para eventos corporativos.
- Separar comandos de eventos de domínio para claridade de propósito.
- Aplicar design de mensagens idempotente e processamento de replay quando necessário.
- Impor gerenciamento de esquema e versionamento em registro central.

## Considerações de Governança

- Estabelecer políticas de governança para contratos de evento e versionamento.
- Garantir documentação de eventos no catálogo com proprietário e ciclo de vida.
- Rastrear assinaturas de consumidores e dependências de evento.
- Validar mudanças em eventos com análise de impacto e testes de compatibilidade.

## Decisão Formal

Adotar Event-Driven Architecture para fatos de negócio e desacoplamento assíncrono, com eventos imutáveis, owner de domínio e AsyncAPI.

## Alternativas Consideradas

Polling; chamadas síncronas encadeadas; compartilhamento de banco de dados.

## Consequências

### Positivas

Desacoplamento, escala e propagação tempestiva.

### Trade-offs e Riscos

Consistência eventual, maior exigência de observabilidade e tratamento de duplicidade.

## Critérios de Revisão

A decisão será reavaliada quando houver mudança material de requisitos regulatórios, escala, modelo operacional ou capacidades corporativas relacionadas. Exceções exigem registro, owner, controles compensatórios e validade.

## Referências

- TOGAF Standard
- Princípios de Arquitetura Empresarial
- Guia de Event Driven Architecture
- Registro de Schemas
