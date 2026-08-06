# Architecture Vision

## Informações do Documento

| Item | Valor |
| --- | --- |
| Programa Estratégico | Enterprise Integration Platform |
| Domínio Arquitetural | Foundation |
| Versão | 1.0 |
| Status | Aprovado |

## Executive Summary

A visão-alvo estabelece uma plataforma empresarial de integração que combina APIs, eventos e mensageria sob um modelo comum de contratos, descoberta, segurança, observabilidade e governança. Domínios publicam produtos de integração com autonomia responsável; consumidores reutilizam interfaces confiáveis sem conhecer detalhes internos dos provedores.

## Visão de Futuro

Integrações serão projetadas contract first, publicadas por pipelines automatizados, descobertas em catálogo e operadas segundo SLOs. O padrão de interação será escolhido pela semântica do caso — requisição síncrona, evento ou mensagem — e não pela preferência de uma tecnologia.

## Capacidades-Alvo

| Camada | Capacidades |
| --- | --- |
| Experiência | Portal, catálogo, documentação e autosserviço |
| Contratos | Design, versionamento, schemas, compatibilidade e descoberta |
| Interação | APIs, eventos, filas, transformação e orquestração controlada |
| Plataforma | Gateway, streaming, mensageria, runtime e pipelines |
| Controle | Identidade, políticas, observabilidade, FinOps e auditoria |

## Modelo Operacional Alvo

O Platform Team opera as capacidades compartilhadas e oferece golden paths. Domain Owners respondem por semântica, qualidade, SLO e evolução dos contratos. A governança define políticas e exceções; a Enterprise Architecture Practice mantém coerência entre programas e decisões estruturantes.

## Princípios da Visão

- contrato antes da implementação;
- baixo acoplamento e compatibilidade evolutiva;
- domínio como owner da interface publicada;
- segurança e observabilidade por design;
- automação de conformidade;
- portabilidade baseada em padrões abertos quando justificável.

## Restrições e Guardrails

- dados sensíveis exigem classificação e política de acesso;
- breaking changes exigem nova versão e plano de transição;
- integrações críticas exigem SLO, runbook e testes de resiliência;
- orquestrações centrais não podem absorver regras pertencentes aos domínios;
- toda interface produtiva deve possuir owner e registro no catálogo.

## Relação com o Programa 02

O Programa 03 transporta e expõe dados; o Programa 02 governa produtos de dados, qualidade, analytics e IA. Eventos e APIs destinados à plataforma de dados preservam ownership, classificação, linhagem técnica e compromissos de serviço definidos entre os programas.

## Business Outcomes

Menor lead time, maior reutilização, mudanças compatíveis, operação previsível e redução de dependências ponto a ponto.

## Relação com Outros Artefatos

- [Business Context](./business-context.md)
- [Diagrama Executivo](../diagrams/executive-target-state.md)
- [Princípios de Arquitetura Corporativa](../../../docs/architecture-principles.md)

## Decisões Arquiteturais

### DA-FND-06 — Padrão de interação orientado ao contexto

APIs, eventos e mensagens coexistirão; a escolha será guiada por temporalidade, acoplamento, consistência e responsabilidade de negócio.

### DA-FND-07 — Controles incorporados ao fluxo de entrega

Políticas verificáveis serão automatizadas nos pipelines e runtimes sempre que tecnicamente possível.
