# C4 Level 2 - Container Diagram

## Objective

Describe the major containers composing the AdTech Platform.

---

## Event Collection Service

Responsibilities:

* Collect customer interactions
* Validate incoming events
* Publish events to Kafka

Technology:

* REST API
* Server-Side Tracking

---

## Event Streaming Platform

Responsibilities:

* Event distribution
* Event persistence
* Event replay

Technology:

* Apache Kafka
* Schema Registry

---

## Customer Data Platform

Responsibilities:

* Identity Resolution
* Unified Profile
* Audience Management

Technology:

* Adobe Experience Platform

---

## Data Platform

Responsibilities:

* Historical Storage
* Analytics
* Machine Learning

Technology:

* BigQuery

---

## Audience Activation Service

Responsibilities:

* Audience Synchronization
* Campaign Activation

Integrations:

* Google Ads
* Meta Ads
* CRM

---

## Governance Services

Responsibilities:

* Consent Validation
* Data Quality
* Metadata Management
* Monitoring

Technology:

* OneTrust
* Data Catalog
* Datadog
