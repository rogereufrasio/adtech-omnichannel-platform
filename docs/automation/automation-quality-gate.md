# Automation Quality Gate

## Objetivo

Definir o processo oficial de validação da documentação arquitetural antes da criação de commits.

A automação estabelece um mecanismo simples de governança contínua para garantir consistência, qualidade e rastreabilidade dos artefatos.

---

# Fluxo de Validação

Antes de qualquer commit relacionado à documentação arquitetural, executar:

```powershell
python tools\architecture\inventory.py

python tools\architecture\validate_links.py

python tools\architecture\document_report.py

python tools\architecture\document-quality-check.py
```

O gate somente é considerado concluído quando todos os validadores terminam sem erros.
