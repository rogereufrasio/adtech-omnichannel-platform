# Architecture Documentation Report
## Summary
- Total documents: 85
- Documents with title: 81
- Documents with context section: 29
- Documents with references: 40

---

## Document Inventory

| Document | Size | Last Modified |
|---|---|---|
| programs\01-enterprise-adtech-platform\adrs\ADR-001-event-driven-architecture.md | 2764 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\adrs\ADR-002-kafka-vs-kinesis.md | 1026 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\adrs\ADR-003-buy-vs-build-cdp.md | 1225 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\architecture\c4\level1-context-diagram.md | 645 bytes | 2026-06-17 |
| programs\01-enterprise-adtech-platform\architecture\c4\level1-context.md | 1948 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\architecture\c4\level2-container-diagram.md | 516 bytes | 2026-06-17 |
| programs\01-enterprise-adtech-platform\architecture\c4\level2-container.md | 2189 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\architecture\data-architecture.md | 2772 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\architecture\reference-architecture.md | 4385 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\diagrams\executive-target-state.md | 1982 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\docs\architecture-risks.md | 2173 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\docs\architecture-target-state.md | 1977 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\docs\architecture-vision.md | 2760 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\docs\business-context.md | 3408 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\docs\capability-map.md | 3975 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\docs\company-profile.md | 1335 bytes | 2026-06-17 |
| programs\01-enterprise-adtech-platform\docs\stakeholder-matrix.md | 1091 bytes | 2026-06-16 |
| programs\01-enterprise-adtech-platform\docs\tradeoffs\kafka-vs-kinesis.md | 772 bytes | 2026-06-17 |
| programs\01-enterprise-adtech-platform\docs\transformation-roadmap.md | 964 bytes | 2026-06-17 |
| programs\01-enterprise-adtech-platform\docs\vendor-assessment.md | 1809 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\events\event-ownership.md | 1469 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\events\event-taxonomy.md | 1824 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\governance\architecture-principles.md | 1893 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\governance\architecture-review-board.md | 2009 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\governance\vendor-onboarding.md | 1495 bytes | 2026-06-22 |
| programs\01-enterprise-adtech-platform\README.md | 4962 bytes | 2026-07-14 |
| programs\02-enterprise-data-ai-platform\adrs\adr-001-api-first.md | 6186 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\adrs\adr-002-event-driven-architecture.md | 5533 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\adrs\adr-003-data-as-a-product.md | 5983 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\adrs\adr-004-vendor-agnostic-ai.md | 5138 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\adrs\adr-005-metadata-first.md | 5457 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\adrs\adr-006-security-by-design.md | 5222 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\adrs\adr-007-cloud-native-platform.md | 6977 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\adrs\README.md | 5382 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\ai-architecture\ai-lifecycle-management.md | 6855 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\ai-architecture\ai-operating-model.md | 1575 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\ai-architecture\ai-platform-architecture.md | 5452 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\ai-architecture\ai-reference-architecture-diagram.md | 1049 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\ai-architecture\genai-reference-architecture.md | 7483 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\ai-architecture\model-governance.md | 6986 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\application-architecture\api-strategy.md | 2717 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\application-architecture\application-architecture-principles.md | 6013 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\application-architecture\application-interaction-model.md | 7050 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\application-architecture\application-landscape.md | 9890 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\application-architecture\event-driven-architecture.md | 7688 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\application-architecture\integration-patterns.md | 3220 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\architecture-target-state.md | 1159 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\business-architecture\business-domains.md | 8749 bytes | 2026-07-20 |
| programs\02-enterprise-data-ai-platform\business-architecture\business-value-streams.md | 8961 bytes | 2026-07-20 |
| programs\02-enterprise-data-ai-platform\business-architecture\capability-assessment.md | 10107 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\business-architecture\capability-map.md | 8283 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\business-architecture\data-ownership-model.md | 8089 bytes | 2026-07-20 |
| programs\02-enterprise-data-ai-platform\diagrams\executive-target-state.md | 6839 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\docs\architecture-vision.md | 4473 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\docs\business-context.md | 9386 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\docs\company-profile.md | 8816 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\executive-target-state.md | 1503 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\governance\ai-governance-framework.md | 3732 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\governance\architecture-governance.md | 4320 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\governance\architecture-metrics.md | 3660 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\governance\data-governance-framework.md | 3789 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\governance\decision-governance.md | 3960 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\governance\reference-architecture-compliance.md | 3714 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\information-architecture\data-domain-model.md | 5941 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\information-architecture\data-lifecycle-model.md | 6644 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\information-architecture\data-product-model.md | 7255 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\information-architecture\enterprise-information-model.md | 6152 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\information-architecture\metadata-strategy.md | 6280 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\maturity-assessment.md | 5519 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\README.md | 9602 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\roadmap\architecture-evolution-plan.md | 2162 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\roadmap\capability-evolution-roadmap.md | 2675 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\roadmap\implementation-phases.md | 3555 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\roadmap\implementation-roadmap.md | 3590 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\roadmap\success-metrics.md | 2190 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\roadmap\transformation-backlog.md | 2865 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\technology-architecture\infrastructure-architecture.md | 6475 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\technology-architecture\observability-architecture.md | 6971 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\technology-architecture\security-architecture.md | 6176 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\technology-architecture\technology-platform.md | 6215 bytes | 2026-07-27 |
| programs\02-enterprise-data-ai-platform\technology-architecture\technology-standards.md | 6341 bytes | 2026-07-27 |
| programs\03-enterprise-integration-platform\README.md | 0 bytes | 2026-06-24 |
| programs\04-enterprise-customer-platform\README.md | 0 bytes | 2026-06-24 |
| programs\05-enterprise-observability-platform\README.md | 0 bytes | 2026-06-24 |
| programs\README.md | 0 bytes | 2026-07-14 |
