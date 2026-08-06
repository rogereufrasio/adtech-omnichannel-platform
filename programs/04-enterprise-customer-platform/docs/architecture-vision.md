# Architecture Vision

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Foundation |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A visão-alvo combina identidade, consentimento, perfil unificado, segmentação, decisioning, loyalty e serviços de ativação em uma arquitetura modular. Dados permanecem sob ownership dos domínios e são disponibilizados pelo Programa 02; interações utilizam contratos do Programa 03.

## Capacidades-Alvo

| Camada | Capacidades |
| --- | --- |
| Experiência | Jornadas, atendimento, loyalty e personalização |
| Serviços Customer | Profile, Identity, Consent, Preference e Audience |
| Inteligência | Segmentação, propensão e next-best-action |
| Dados | Customer Data Products e qualidade |
| Integração | APIs, eventos e contratos governados |
| Controle | Privacidade, segurança, observabilidade e decisão |

## Guardrails

- nenhum perfil sem owner, finalidade e classificação;
- nenhuma ativação sem base legal ou consentimento aplicável;
- atributos sensíveis não serão replicados sem necessidade comprovada;
- regras determinísticas e modelos terão versionamento e explicabilidade;
- fontes autoritativas e precedência de atributos serão explícitas.

## Business Outcomes

Customer 360 confiável, reconhecimento omnicanal, personalização responsável e menor tempo de integração de jornadas.

## Relação com Outros Artefatos

- [Business Context](./business-context.md)
- [Estado-Alvo](../architecture-target-state.md)
- [Diagrama Executivo](../diagrams/executive-target-state.md)

## Decisões Arquiteturais

A arquitetura será componível, orientada por produtos de dados e contratos, com privacidade e accountability humana por design.
