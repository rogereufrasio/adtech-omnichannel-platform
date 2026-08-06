# Company Profile

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Integration Platform |
| Domínio Arquitetural | Foundation |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A organização opera um ecossistema omnicanal composto por canais digitais, lojas, plataformas corporativas, parceiros e capacidades de dados e IA. A evolução descentralizada ampliou a velocidade local, mas também criou integrações ponto a ponto, contratos implícitos e níveis desiguais de segurança e operação.

## Perfil Corporativo

| Dimensão | Característica relevante para integração |
| --- | --- |
| Modelo operacional | Domínios de negócio com autonomia crescente |
| Ecossistema | Aplicações próprias, SaaS, legado e parceiros externos |
| Canais | Web, mobile, atendimento, lojas e mídia digital |
| Dados e IA | Plataforma corporativa estabelecida pelo Programa 02 |
| Regulação | Requisitos de privacidade, segurança, auditoria e continuidade |

## Jornada de Evolução Digital

1. digitalização de processos e integrações orientadas a projeto;
2. expansão omnicanal com crescimento de APIs e fluxos assíncronos;
3. evolução para produtos digitais e de dados com dependências entre domínios;
4. industrialização da integração como capacidade corporativa.

## Desafios Estratégicos Atuais

- acoplamento e dependências não catalogadas;
- duplicidade de interfaces e transformações;
- mudanças incompatíveis detectadas tardiamente;
- ownership e suporte operacional difusos;
- controles heterogêneos para integrações internas e externas.

## Direcionadores Estratégicos

| Direcionador | Implicação arquitetural |
| --- | --- |
| Velocidade de negócio | Autosserviço e reutilização com guardrails |
| Omnicanalidade | Contratos consistentes entre jornadas e domínios |
| Dados e IA em escala | Eventos e APIs confiáveis para o Programa 02 |
| Ecossistema de parceiros | Exposição controlada e políticas diferenciadas |
| Resiliência operacional | SLOs, desacoplamento e recuperação verificável |

## Papel da Arquitetura Corporativa

A Enterprise Architecture Practice define os guardrails, arbitra decisões transversais, mantém rastreabilidade entre outcomes e capacidades e assegura coerência com o baseline do Programa 02. Domínios e times de plataforma respondem pela entrega e operação dentro desse modelo.

## Relação com Outros Artefatos

- [Business Context](./business-context.md)
- [Architecture Vision](./architecture-vision.md)
- [Programa Estratégico 02](../../02-enterprise-data-ai-platform/README.md)

## Decisões Arquiteturais

### DA-FND-04 — Plataforma compartilhada, ownership federado

A organização proverá capacidades comuns de integração sem transferir aos times centrais a responsabilidade pelos contratos dos domínios.
