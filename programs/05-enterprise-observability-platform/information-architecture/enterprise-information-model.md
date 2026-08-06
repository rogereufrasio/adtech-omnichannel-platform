# Modelo Corporativo de Informação de Observabilidade

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Observability Platform |
| Domínio Arquitetural | Information Architecture |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

O modelo estabelece conceitos comuns para correlacionar sinais e decisões.

## Entidades

| Entidade | Definição |
| --- | --- |
| Service | Unidade operável com owner e SLO |
| Service Instance | Execução implantada em ambiente |
| Telemetry Signal | Metric, log, trace, event ou profile |
| Resource | Infraestrutura ou runtime associado |
| Journey | Fluxo de valor atravessando serviços |
| SLI/SLO | Medida e objetivo de confiabilidade |
| Alert | Condição acionável ligada a impacto |
| Incident | Interrupção gerenciada com timeline |
| Change | Alteração correlacionável ao comportamento |

## Identificadores

service.name, environment, trace_id, span_id, deployment/version e owner são contexto mínimo.

## Guardrails

- service ownership, criticidade e finalidade explícitos;
- segurança, privacidade, retenção e custo por design;
- contratos e padrões abertos antes de ferramentas;
- evidências operacionais sustentam decisões e exceções.

## Relação com Outros Artefatos

- [Metadata Strategy](./metadata-strategy.md)
- [Telemetry Data Model](./telemetry-data-model.md)

## Decisões Arquiteturais

Este artefato integra o baseline normativo da Release 1.0.
