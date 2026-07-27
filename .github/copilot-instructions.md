# Enterprise Architecture Portfolio - Copilot Instructions

## Context

This repository contains an Enterprise Architecture portfolio based on TOGAF principles.

The repository documents enterprise transformation programs using:
- Business Architecture
- Application Architecture
- Data Architecture
- Technology Architecture
- Governance
- Roadmaps
- Architecture Decision Records (ADR)

---

# General Rules

## Documentation Structure

Every program must follow the standard structure:

- docs/
- architecture/
- business-architecture/
- application-architecture/
- information-architecture/
- technology-architecture/
- governance/
- roadmap/
- adrs/

---

# Architecture Principles

Always consider:

- API First
- Event Driven Architecture
- Data as a Product
- Metadata First
- Security by Design
- Cloud Native
- Vendor Agnostic
- Observability by Design

---

# Document Creation Rules

When creating architectural documents:

- Start with business context.
- Define purpose and scope.
- Explain architectural decisions.
- Reference related documents.
- Keep alignment with target state.
- Use ADRs for significant decisions.

---

# Diagrams

When creating Mermaid diagrams:

Follow:
.github/instructions/mermaid.instructions.md

---

# Quality Validation

Before proposing completion:

Execute:

python tools/architecture/run-documentation-check.py

Ensure:
- links valid
- documentation quality checked
- report generated

---

# Naming Convention

Use lowercase filenames with hyphen separation.

Examples:

architecture-vision.md
implementation-roadmap.md
security-architecture.md