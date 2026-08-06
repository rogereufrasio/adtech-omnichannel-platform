# Mapa de Capacidade de Integração

## Informações do Documento

| Item | Valor |
| --- | --- |
| Domínio Arquitetural | Business Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Contexto

O Programa 03 requer um mapa de capacidades de integração para definir os serviços essenciais que sustentam a entrega de APIs, eventos, mensageria e governança.

## Objetivo

Documentar as capacidades de integração fundamentais do programa e relacioná-las com os domínios de negócio e os requisitos operacionais.

## Visão Geral da Arquitetura

O mapa de capacidades organiza a plataforma de integração em camadas: governança, interface, transporte, processamento e operações. Cada capacidade representa um serviço reutilizável, como gerenciamento de APIs, broker de eventos, transformação de dados, catálogo de contratos e observabilidade.

## Mapa de Capacidades

| Nível | Capacidade | Responsabilidade |
| --- | --- | --- |
| L1 | Gestão de Produtos de Integração | Portfólio, ownership, descoberta e ciclo de vida |
| L1 | Engenharia de Integração | Design, implementação, testes e entrega |
| L1 | Operação de Integração | SLO, observabilidade, incidentes e capacidade |
| L2 | API Management | Exposição, proteção, análise e versionamento |
| L2 | Event & Messaging | Publicação, consumo, retenção e entrega confiável |
| L2 | Contract Management | Schemas, compatibilidade, catálogo e linhagem |
| L2 | Integration Governance | Políticas, conformidade, risco e exceções |

O mapa é independente de fornecedores e orienta priorização, funding e métricas da plataforma.

## Decisões Arquiteturais

- Estruturar capacidades em níveis que reflitam responsabilidade e reutilização.
- Priorizar capacidades que suportem integração síncrona e assíncrona de forma consistente.
- Desenvolver capacidades de governança e automação como componentes de plataforma.
- Focar em capacidades que permitam rápida adaptação a novos domínios de negócio.

## Considerações de Governança

- Definir SLAs e métricas para cada capacidade de integração.
- Revisar periodicamente o mapa de capacidades para incorporar novas demandas.
- Garantir que as capacidades estejam alinhadas com políticas de segurança, conformidade e qualidade de dados.
- Documentar as interfaces de cada capacidade no catálogo de integração.

## Relação com Outros Artefatos

- [Domínios de Negócio](./business-domains.md)
- [Modelo Operacional de Integração](./integration-operating-model.md)
- [Architecture Vision](../docs/architecture-vision.md)

## Referências

- TOGAF Standard
- Princípios de Arquitetura Empresarial
- Programa 03 README
- Integration Capability Mapping
