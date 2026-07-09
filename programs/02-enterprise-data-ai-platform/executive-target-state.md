# Arquitetura Executiva

```mermaid
flowchart LR

ERP[ERP]
CRM[CRM]
ECOM[E-commerce]
APP[Mobile]

ERP --> LAKEHOUSE
CRM --> LAKEHOUSE
ECOM --> LAKEHOUSE
APP --> LAKEHOUSE

LAKEHOUSE[Lakehouse Corporativo]

LAKEHOUSE --> BI[Analytics Platform]

LAKEHOUSE --> MLOPS[MLOps]

MLOPS --> GENAI[GenAI Platform]

GENAI --> RAG[RAG Services]

RAG --> AGENTS[AI Agents]

BI --> USERS[Business Users]

AGENTS --> USERS