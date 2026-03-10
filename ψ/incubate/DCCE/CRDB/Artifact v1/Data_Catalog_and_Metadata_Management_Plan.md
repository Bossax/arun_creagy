---
status: current
tags:
  - governance
  - metadata
  - policy
  - NCAIF
created: 2026-02-16
last_updated: 2026-02-16
project: DCCE-CRDB
type: artifact
---

# Data Catalog and Metadata Management Plan

## 1. Introduction & Purpose

This document outlines the strategy and plan for implementing and managing a comprehensive Data Catalog for the National Climate Adaptation Information Framework (NCAIF). The Data Catalog is the central pillar of our data governance strategy, designed to make high-quality data easily discoverable, understandable, and trustworthy for all users.

The purpose of this plan is to:
*   Establish a standardized approach for collecting, managing, and publishing metadata.
*   Define the architecture and tools for the Data Catalog.
*   Clarify roles and responsibilities for metadata management.
*   Provide a roadmap for the catalog's implementation and continuous improvement.

## 2. Vision and Objectives

**Vision:** To create a "single source of truth" for information about the NCAIF's data assets, empowering users to find and utilize the right data for their needs with confidence and ease. The catalog will transform our data landscape from a collection of disconnected silos into a fully navigable and interconnected ecosystem.

**Objectives:**
1.  **Improve Data Discovery:** Enable users to easily search for and find relevant data assets using business terms, keywords, and faceted search, regardless of where the data is physically stored.
2.  **Increase Data Understanding:** Provide rich context for each data asset, including clear business definitions, data lineage, quality scores, and classifications.
3.  **Promote Data Trust:** Instill confidence in the data by making its origins, transformations, and quality transparent to all users.
4.  **Enhance Data Governance:** Operationalize data governance policies by using the catalog as the central registry for data stewardship, classification, and access rules.
5.  **Reduce Redundancy:** Identify and reduce duplicate data assets, promoting the use of authoritative data sources.

## 3. Metadata Standard

A standardized set of metadata elements is essential for the catalog's success. All data assets registered in the catalog must be described using the following minimum set of attributes.

### 3.1. Core Metadata Elements

| Element Name                                                                                  | Description                                                      | Example                                                                                                   | Mandatory |
| :-------------------------------------------------------------------------------------------- | :--------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- | :-------- |
| **Asset Name**                                                                                | A clear, human-readable name for the data asset.                 | `Provincial Flood Risk Index`                                                                             | Yes       |
| **Asset Description**                                                                         | A concise summary of the data asset's content and purpose.       | `Annual index of flood risk for all 77 provinces, based on rainfall, topography, and population density.` | Yes       |
| **Data Steward**                                                                              | The primary person accountable for the data asset.               | `[Name], Water Resources Domain Steward`                                                                  | Yes       |
| **==Data Domain==**<!--note:  is this NAP sectors, adaptation themes (GGA), or CDM domain?--> | The logical grouping to which the asset belongs.                 | `Water Management`                                                                                        | Yes       |
| **Data Classification**                                                                       | The assigned security level from the Data Classification Policy. | `Official Use`                                                                                            | Yes       |
| **Source System**                                                                             | The original system or process that created the data.            | `Thai Meteorological Department (TMD) Weather Model`                                                      | Yes       |
| **Update Frequency**                                                                          | How often the data is updated.                                   | `Annually` , 'non-routine'                                                                                | Yes       |
| **Access Method**                                                                             | How users can access the data (e.g., API, CSV download).         | `API Endpoint: /api/v1/floodrisk`                                                                         | Yes       |
| **Format**                                                                                    | File extension                                                   | can be auto harvested                                                                                     | Yes       |

### 3.2. Extended Metadata (Recommended)

- **Data Lineage:** A visual representation of the data's flow and transformation from source to destination. <!--note: this is very desired. can start with the datasets generated by DCCE. From imported datasets, must be traceable to the data owner. -->
* **Data Quality Score:** A summary score based on metrics like completeness, accuracy, and timeliness.
* **Business Glossary Terms:** Links to standardized business terms defined in the enterprise glossary. <!--todo:  to create business glossary-->
* **Technical Metadata:** Data types, column names, table definitions, etc. (Can be auto-harvested <!--note: most data.gov datasets are auto-harvested (table schema)-->).
* **Sample Data:** A small, representative sample of the data to aid in evaluation.

## 4. Data Catalog Architecture & Tooling

The NCAIF will adopt a modern data cataloging tool with the following key capabilities:
1.  **Automated Metadata Harvesting:** Connectors to automatically scan and ingest technical metadata from various source systems (databases, data lakes, APIs).
2.  **AI-Powered Curation:** Use of AI/ML to suggest business terms, link related assets, and identify potential PII. <!--note: AI for metadata discovery through semantic search-->
3.  **Business Glossary Integration:** A built-in or tightly integrated business glossary to manage and link key business terms.
4.  **Collaborative Features:** Workflows for users to ask questions, add comments, and rate data assets. <!--note:  not included-->
5.  **Governance Workflows:** Integration with data governance roles to manage approval processes for metadata changes and access requests. [[Data_Governance_Charter]]

The chosen tool will be deployed as a central, cloud-based service to ensure accessibility for all authorized users.

## 5. Implementation Roadmap (irrelevant)

### Phase 1: Foundation & Pilot (Months 1-3)

*   **Task 1:** Finalize selection and procurement of the Data Catalog tool.
*   **Task 2:** Establish the core metadata standard and business glossary for 2-3 priority data domains.
*   **Task 3:** Appoint and train the initial group of Data Stewards for the pilot domains.
*   **Task 4:** Ingest and manually curate metadata for a limited set of high-value data assets within the pilot domains.
*   **Goal:** Launch a pilot version of the catalog to a select group of users and gather feedback.

### Phase 2: Expansion & Automation (Months 4-9)

*   **Task 1:** Expand the business glossary and metadata standards to cover all major data domains.
*   **Task 2:** Configure automated metadata harvesting connectors for key source systems.
*   **Task 3:** Onboard and train the next wave of Data Stewards.
*   **Task 4:** Launch the Data Catalog to all DCCE staff and key agency partners.
*   **Goal:** Achieve 80% coverage of critical data assets in the catalog, with a focus on automating metadata ingestion.

### Phase 3: Enterprise-wide Adoption & Enrichment (Months 10-12+)

*   **Task 1:** Integrate the Data Catalog with other systems, such as data quality and access control tools.
*   **Task 2:** Implement advanced features like data lineage tracing and collaborative workflows.
*   **Task 3:** Develop and launch a data literacy program to drive adoption and usage of the catalog across all user personas.
*   **Goal:** Make the Data Catalog the default starting point for all data-related activities and a cornerstone of the data-driven culture.

## 6. Roles and Responsibilities

*   **Data Stewardship Committee (DSC):** Oversees the implementation of this plan and approves the metadata standards.
*   **Data Stewards:** Are responsible for creating, maintaining, and certifying the metadata for their assigned data assets.
*   **IT Department:** Is responsible for the technical administration and maintenance of the Data Catalog platform.
*   **All Users:** Are responsible for using the Data Catalog to discover and understand data before use.
