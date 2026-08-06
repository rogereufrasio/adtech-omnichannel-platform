# ADR-006 — Segurança por Design em Integração

## Informações da Decisão

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Integration Platform |
| Status | Aceito |
| Versão | 1.0 |
| Decisor | Architecture Review Board |

## Contexto

A plataforma de integração expõe APIs, eventos e mensagens através de fronteiras internas e externas, exigindo controles de segurança consistentes.

## Objetivo

Incorporar segurança por design em todos os componentes de integração, protegendo dados e serviços durante o transporte, processamento e consumo.

## Visão Geral da Arquitetura

A segurança é aplicada em camadas: gateway, transporte, mensagem e runtime. Autenticação, autorização, criptografia e validação de payload são parte integrada da arquitetura de plataforma.

## Decisões Arquiteturais

- Adotar autenticação forte e autorização baseada em políticas para APIs e mensageria.
- Garantir criptografia em trânsito e em repouso para dados sensíveis.
- Validar esquemas e payloads como controle de integridade e segurança.
- Implementar segredos e credenciais de forma segura e auditável.

## Considerações de Governança

- Definir políticas de segurança de integração e requisitos de conformidade.
- Realizar modelagem de ameaças e revisões de segurança durante o design.
- Monitorar incidentes e acessos em trilhas de auditoria.
- Alinhar práticas de segurança com normas corporativas de TI e privacidade.

## Decisão Formal

Aplicar identidade de workload e usuário, menor privilégio, proteção de dados, gestão de segredos e policy enforcement em design, pipeline e runtime.

## Alternativas Consideradas

Controles apenas no perímetro; revisão manual tardia; credenciais compartilhadas.

## Consequências

### Positivas

Redução de exposição e evidências auditáveis.

### Trade-offs e Riscos

Maior esforço inicial e dependência de capacidades corporativas de identidade.

## Critérios de Revisão

A decisão será reavaliada quando houver mudança material de requisitos regulatórios, escala, modelo operacional ou capacidades corporativas relacionadas. Exceções exigem registro, owner, controles compensatórios e validade.

## Referências

- TOGAF Standard
- Princípios de Arquitetura Empresarial
- Diretrizes de Segurança de APIs
- Normas de Segurança de Mensageria
