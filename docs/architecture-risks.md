# Architecture Risks

## Risco 1 - Dependência Excessiva de Vendors

### Descrição

Parte relevante da estratégia depende de plataformas de terceiros.

### Impacto

Alto

### Mitigação

* APIs padronizadas
* Contratos desacoplados
* Estratégia de substituição gradual

---

## Risco 2 - Crescimento de Custos Operacionais

### Descrição

O aumento do volume de eventos pode elevar custos de armazenamento e processamento.

### Impacto

Médio

### Mitigação

* Estratégia FinOps
* Retenção por domínio
* Compressão e arquivamento

---

## Risco 3 - Duplicidade de Identidade

### Descrição

Clientes podem ser representados por múltiplos identificadores.

### Impacto

Alto

### Mitigação

* Identity Resolution
* Golden Record
* Regras de deduplicação

---

## Risco 4 - Governança de Eventos

### Descrição

Proliferação de eventos sem padronização.

### Impacto

Alto

### Mitigação

* Schema Registry
* Catálogo corporativo
* Processo de revisão arquitetural
