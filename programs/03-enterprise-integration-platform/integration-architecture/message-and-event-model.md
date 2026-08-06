# Modelo de Mensagem e Evento

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Contexto

A plataforma de integração deve suportar tanto mensagens transacionais quanto eventos de domínio, garantindo consistência semântica e governança de dados.

## Objetivo

Definir o modelo de mensagens e eventos que orienta estruturas de payload, tipos de canal e contratos de troca de informação.

## Visão Geral da Arquitetura

O modelo classifica artefatos em comandos, notificações, eventos de domínio e documentos. Ele define quando usar filas, tópicos e streams, bem como padrões de schema, metadados e versionamento.

## Critérios Arquiteturais

- padrão de interação selecionado por semântica, temporalidade e acoplamento;
- contrato, owner, consumidores, versão e SLO registrados no catálogo;
- regras de domínio permanecem na aplicação proprietária;
- resiliência, idempotência e tratamento de falhas definidos por criticidade;
- segurança e correlação ponta a ponta incorporadas ao design;

## Decisões Arquiteturais

- Separar mensagens de comando de eventos de mudança de estado.
- Usar filas para processamento ponto a ponto e tópicos/streams para publicação a múltiplos consumidores.
- Definir schemas e metadados obrigatórios para todas as mensagens e eventos.
- Aplicar validação de payload e contratos formais para consistência.

## Considerações de Governança

- Documentar todos os artefatos de mensagem e evento no catálogo de integração.
- Definir proprietários e ciclos de vida para cada artefato.
- Monitorar conformidade de schema e validade de payload.
- Estabelecer processos de revisão para mudanças em mensagens e eventos.

## Referências

- TOGAF Standard
- Princípios de Arquitetura Empresarial
- Programa 03 README
- Message and Event Modeling
