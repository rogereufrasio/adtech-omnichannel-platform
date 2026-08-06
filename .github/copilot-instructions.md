# Instruções do Copilot para a Enterprise Architecture Practice

## Contexto

Este repositório documenta Programas Estratégicos de transformação corporativa com princípios inspirados no TOGAF.

## Estrutura Obrigatória

Cada programa deve seguir o blueprint disponível em `standards/program-blueprint/`, incluindo Foundation, Business Architecture, Information Architecture, Application Architecture, Technology Architecture, Governance, Roadmap e ADRs.

## Princípios Arquiteturais

- API First;
- Event-Driven Architecture;
- Data as a Product;
- Metadata First;
- Security by Design;
- Cloud Native;
- Vendor Agnostic;
- Observability by Design.

## Regras de Documentação

- iniciar pelo contexto de negócio;
- definir propósito, escopo e boundaries;
- explicar decisões arquiteturais;
- relacionar artefatos dependentes;
- preservar alinhamento com o estado-alvo;
- registrar decisões estruturantes em ADRs;
- manter conteúdo em português, exceto termos técnicos consolidados.

## Diagramas

Seguir `.github/instructions/mermaid.instructions.md`.

## Validação

Antes de concluir alterações, executar:

```powershell
python tools/architecture/run-documentation-check.py
```

Todos os links e critérios documentais devem ser aprovados.

## Nomenclatura

Arquivos e diretórios utilizam letras minúsculas, nomes descritivos e separação por hífen. ADRs preservam numeração sequencial.
