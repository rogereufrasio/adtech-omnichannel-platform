# Riscos Arquiteturais

## Objetivo

Identificar os principais riscos associados à implementação e operação da plataforma AdTech, bem como suas respectivas estratégias de mitigação.

---

# Risco ARQ-001

## Dependência Excessiva de Fornecedores

### Descrição

Parte significativa das capacidades da solução depende de plataformas especializadas de mercado.

### Impacto

Alto

### Probabilidade

Média

### Estratégias de Mitigação

- Uso de APIs padronizadas;
- Contratos desacoplados;
- Estratégia de substituição gradual;
- Avaliações periódicas de mercado.

---

# Risco ARQ-002

## Crescimento dos Custos Operacionais

### Descrição

O aumento do volume de eventos pode elevar custos de processamento, armazenamento e transferência de dados.

### Impacto

Médio

### Probabilidade

Alta

### Estratégias de Mitigação

- Práticas de FinOps;
- Retenção baseada em domínio;
- Compressão e arquivamento;
- Monitoramento contínuo de consumo.

---

# Risco ARQ-003

## Duplicidade de Identidade de Clientes

### Descrição

Um mesmo cliente pode ser representado por múltiplos identificadores em diferentes canais.

### Impacto

Alto

### Probabilidade

Alta

### Estratégias de Mitigação

- Identity Resolution;
- Golden Record;
- Regras de deduplicação;
- Governança de identificadores.

---

# Risco ARQ-004

## Falta de Governança de Eventos

### Descrição

A expansão da plataforma pode gerar eventos inconsistentes ou sem padronização.

### Impacto

Alto

### Probabilidade

Média

### Estratégias de Mitigação

- Schema Registry;
- Catálogo corporativo;
- Processo de revisão arquitetural;
- Ownership obrigatório para eventos.

---

# Risco ARQ-005

## Não Conformidade com LGPD

### Descrição

Uso inadequado de dados pessoais ou ativação sem consentimento válido.

### Impacto

Crítico

### Probabilidade

Baixa

### Estratégias de Mitigação

- Gestão centralizada de consentimento;
- Auditoria contínua;
- Privacy by Design;
- Revisões periódicas de compliance.