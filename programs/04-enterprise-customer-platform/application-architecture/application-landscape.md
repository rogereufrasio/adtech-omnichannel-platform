# Landscape de Aplicações Customer

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Customer Platform |
| Domínio Arquitetural | Application Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O landscape organiza aplicações por responsabilidade e evita que Customer 360 se torne um monólito.

## Landscape Alvo

| Zona | Aplicações/serviços | Responsabilidade |
| --- | --- | --- |
| Engagement | Web, mobile, service, marketing e loyalty | Experiência e captura |
| Customer | Identity, Profile, Consent, Preference e Audience | Contexto compartilhado |
| Systems of Record | CRM, commerce, service e loyalty | Registros autoritativos |
| Data & AI | Data products, analytics e modelos | Inteligência corporativa |
| Integration | API management, events e messaging | Contratos e transporte |

## Fronteiras

Canais não persistem cópias não governadas do perfil; Customer Services não absorvem lógica transacional.

## Critérios Arquiteturais

- contrato, owner, SLO, classificação e consumidores explícitos;
- segurança, privacidade, resiliência e observabilidade por design;
- baixo acoplamento e compatibilidade evolutiva;
- reutilização obrigatória dos baselines 02 e 03.

## Relação com Outros Artefatos

- [Interaction Model](./application-interaction-model.md)
- [Customer Reference Architecture](../customer-architecture/customer-reference-architecture.md)

## Decisões Arquiteturais

A solução será componível e vendor-agnostic no nível lógico; seleção de produto não altera as fronteiras aprovadas.
