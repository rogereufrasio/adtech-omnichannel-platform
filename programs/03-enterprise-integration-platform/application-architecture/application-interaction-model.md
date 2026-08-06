# Modelo de Interação de Aplicações

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Contexto

O modelo de interação define como aplicações se comunicam por meio da plataforma de integração, usando APIs, eventos e mensagens governadas.

## Objetivo

Descrever os padrões de interação entre aplicações e requisitos de comunicação para garantir confiabilidade, desempenho e desacoplamento.

## Visão Geral da Arquitetura

A arquitetura de interação inclui padrões de solicitação/resposta, publish/subscribe, orquestração e coreografia. Ela define como as aplicações publicam e consomem serviços e eventos, além de como são tratadas falhas e retries.

## Critérios Arquiteturais

- padrão de interação selecionado por semântica, temporalidade e acoplamento;
- contrato, owner, consumidores, versão e SLO registrados no catálogo;
- regras de domínio permanecem na aplicação proprietária;
- resiliência, idempotência e tratamento de falhas definidos por criticidade;
- segurança e correlação ponta a ponta incorporadas ao design;

## Decisões Arquiteturais

- Priorizar interações assíncronas sempre que possível para reduzir acoplamento.
- Definir contratos claros para cada ponto de interação.
- Usar padrões de resiliência como retries, circuit breaker e fallback.
- Diferenciar interações síncronas críticas de interações assíncronas de alta latência.

## Considerações de Governança

- Validar fluxos de interação nas revisões de arquitetura.
- Documentar dependências e contratos de interação no catálogo.
- Monitorar o comportamento de chamadas e eventos para detectar falhas.
- Garantir que as interações obedeçam políticas de segurança e compliance.

## Referências

- TOGAF Standard
- Princípios de Arquitetura Empresarial
- Programa 03 README
- Application Interaction Model
