# AI Reference Architecture Diagram

## Context

A AI Reference Architecture define a visão estrutural da capacidade de Inteligência Artificial dentro do Enterprise Data & AI Platform.

O objetivo é estabelecer como dados, modelos, serviços de IA, governança e capacidades de consumo se conectam para permitir adoção corporativa de Inteligência Artificial de forma escalável, segura e governada.

A arquitetura segue os princípios:

- AI by Design
- Data as a Product
- API First
- Metadata First
- Security and Privacy by Design
- Responsible AI
- Cloud Native Platform
- Vendor Agnostic AI

---

# 1. Visão Geral da Arquitetura

A arquitetura de referência é organizada em camadas:

```mermaid
flowchart TB

A[Business Domains]

B[AI Consumption Layer]

C[AI Services Layer]

D[AI Platform Layer]

E[Data Foundation Layer]

F[Governance & Security Layer]


A --> B
B --> C
C --> D
D --> E

F -. governs .-> A
F -. governs .-> B
F -. governs .-> C
F -. governs .-> D
F -. governs .-> E