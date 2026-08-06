# ADR-004 — Integração Contract First

## Informações da Decisão

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Integration Platform |
| Status | Aceito |
| Versão | 1.0 |
| Decisor | Architecture Review Board |

## Contexto

Projetos de integração apresentam riscos de incompatibilidade devido a contratos mal definidos ou documentação desatualizada.

## Objetivo

Adotar uma abordagem contract first para garantir que todas as interfaces sejam definidas, validadas e governadas antes da implementação.

## Visão Geral da Arquitetura

Contratos são a fonte de verdade. APIs e eventos são projetados com especificações de contrato formais, gerenciados em um repositório central e utilizados para geração de código, testes e validação de integração.

## Decisões Arquiteturais

- Exigir definição de contrato antes de iniciar desenvolvimento.
- Utilizar OpenAPI e AsyncAPI como artefatos contratuais padrão.
- Sincronizar contratos com o catálogo de integração e registro de esquemas.
- Automatizar validação de contrato na pipeline de CI/CD.

## Considerações de Governança

- Implementar gates de revisão de contrato em pontos de controle de arquitetura.
- Validar compatibilidade e versão de contrato antes de alterações em produção.
- Garantir que os contratos contemplem requisitos de segurança e observabilidade.
- Fornecer governança de ciclo de vida de contrato para descontinuação e migração.

## Decisão Formal

Exigir contratos versionados e testes de compatibilidade antes da implementação e publicação de APIs, eventos e mensagens.

## Alternativas Consideradas

Code first; validação manual; contratos implícitos.

## Consequências

### Positivas

Falhas detectadas cedo e mudanças previsíveis.

### Trade-offs e Riscos

Pipelines e governança de schemas tornam-se dependências críticas.

## Critérios de Revisão

A decisão será reavaliada quando houver mudança material de requisitos regulatórios, escala, modelo operacional ou capacidades corporativas relacionadas. Exceções exigem registro, owner, controles compensatórios e validade.

## Referências

- TOGAF Standard
- Princípios de Arquitetura Empresarial
- Documentação de Contract First
- Catálogo de Integração
