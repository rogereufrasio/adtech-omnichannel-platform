# ADR-001 - Event Driven Architecture

## Status

Accepted

## Date

2026-06-16

## Context

The current platform relies heavily on batch integrations between marketing, analytics and customer platforms.

This model introduces:

- High latency
- Tight coupling
- Operational complexity
- Limited scalability

The target architecture requires near real-time processing and improved integration flexibility.

---

## Decision

Adopt an Event-Driven Architecture using Apache Kafka as the enterprise event backbone.

---

## Rationale

Kafka provides:

- High throughput
- Scalability
- Event replay
- Decoupled integrations
- Multi-consumer support

---

## Consequences

### Positive

- Real-time processing
- Better scalability
- Improved resiliency
- Reduced integration coupling

### Negative

- Additional operational complexity
- New monitoring requirements
- Increased platform governance needs