# Modelo de Integração Orientado a Eventos

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Contexto

Uma estratégia event-driven é necessária para suportar integração assíncrona, desacoplamento e processos em tempo real no Programa 03.

## Objetivo

Definir o modelo arquitetural de eventos que habilita publicação, inscrição, processamento e governança de eventos de negócio.

## Visão Geral da Arquitetura

O modelo utiliza uma malha de eventos ou plataforma de streaming, com produtores, consumidores, tópicos/esquemas e um registro de contratos. Ele suporta assinaturas independentes e permite que múltiplos consumidores processem eventos de maneira resiliente.

## Critérios Arquiteturais

- padrão de interação selecionado por semântica, temporalidade e acoplamento;
- contrato, owner, consumidores, versão e SLO registrados no catálogo;
- regras de domínio permanecem na aplicação proprietária;
- resiliência, idempotência e tratamento de falhas definidos por criticidade;
- segurança e correlação ponta a ponta incorporadas ao design;

## Decisões Arquiteturais

- Adotar publish/subscribe como padrão para eventos de domínio.
- Gerenciar esquemas e contratos de eventos em repositório central.
- Separar eventos de notificação de eventos de mudança de estado.
- Suportar replay e idempotência quando necessário.

## Considerações de Governança

- Estabelecer nomenclatura consistente e versionamento de eventos.
- Validar impacto de mudanças em contratos de evento.
- Monitorar qualidade e latência de eventos.
- Documentar proprietários e ciclo de vida de cada evento.

## Referências

- TOGAF Standard
- Princípios de Arquitetura Empresarial
- Programa 03 README
- Event Driven Architecture
