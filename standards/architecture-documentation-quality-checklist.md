# Checklist de Qualidade da Documentação de Arquitetura

## Objetivo

Este checklist estabelece os critérios mínimos de qualidade para toda documentação de Arquitetura Corporativa deste repositório.

Ele complementa as validações automatizadas executadas pelos scripts da pasta `tools/architecture` e deve ser utilizado durante Architecture Reviews e Pull Requests.

---

# Estrutura do Documento

## Identificação

- [ ] Possui título (`#`)
- [ ] Nome do arquivo segue o padrão do repositório
- [ ] Está localizado no diretório correto

---

## Objetivo

- [ ] O objetivo do documento está claramente descrito
- [ ] O escopo está definido
- [ ] O público-alvo está identificado quando aplicável

---

## Contexto

- [ ] Existe uma seção de contexto
- [ ] O problema arquitetural está descrito
- [ ] O contexto de negócio foi considerado

---

## Conteúdo

- [ ] Organização lógica das seções
- [ ] Linguagem técnica consistente
- [ ] Não existem ambiguidades
- [ ] Não existem informações duplicadas
- [ ] Não existem placeholders esquecidos

---

## Arquitetura

Quando aplicável:

- [ ] Princípios arquiteturais definidos
- [ ] Decisões justificadas
- [ ] Trade-offs documentados
- [ ] Riscos identificados
- [ ] Impactos descritos

---

## Diagramas

Quando houver diagramas:

- [ ] Utilizam Mermaid
- [ ] Sintaxe válida
- [ ] Compatíveis com o documento
- [ ] Fácil leitura
- [ ] Consistentes com a arquitetura descrita

---

## Referências

- [ ] Referências internas corretas
- [ ] Links válidos
- [ ] ADRs relacionados citados quando aplicável
- [ ] Documentos relacionados referenciados

---

## Qualidade Editorial

- [ ] Ortografia revisada
- [ ] Gramática revisada
- [ ] Terminologia consistente
- [ ] Nomenclatura padronizada

---

## Versionamento

- [ ] Alterações registradas no Git
- [ ] Histórico preservado
- [ ] Não existem arquivos duplicados

---

# Critérios de Aprovação

Um documento é considerado aprovado quando:

- atende aos critérios deste checklist;
- passa nas validações automatizadas;
- apresenta conteúdo consistente com os demais documentos;
- está alinhado ao Enterprise Architecture Program Blueprint.

---

# Ferramentas de Validação

A documentação deve ser validada utilizando:

- `inventory.py`
- `validate_links.py`
- `document_quality_check.py`
- `document_report.py`
- GitHub Actions

---

# Referências

- `program-blueprint/README.md`
- `program-blueprint/checklist.md`
- `architecture-document-catalog.md`
- `architecture-review-process.md`