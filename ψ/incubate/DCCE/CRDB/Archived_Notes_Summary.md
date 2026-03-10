---
status: evergreen
tags:
  - summary
  - archive
created: 02/10/2026
last_updated: 02/10/2026
AI_prompt: false
AI_output: true
project: DCCE_CRDB
type: summary
---

# Summary of Archived Notes

## Overview
This document summarizes key archived notes regarding the DCCE-CRDB project's strategy, specifically its alignment with the UNDP-BTR project (ADPC) and the evolution of its data architecture approach.

## Key Themes

### 1. Strategic Alignment with UNDP-BTR (ADPC)
- **Differentiation:** CRDB acts as the "Architect & Librarian" (managing the ecosystem, cataloging), while ADPC is the "Builder & Curator" (creating the physical risk platform and visualization).
- **Synergy:** CRDB will piggyback on ADPC's consultation and training sessions to save resources.
- **Dependencies:** CRDB relies on ADPC for the "Risk" domain data (gold layer product) and will reverse-engineer ADPC's physical schema to inform the Enterprise Data Model.

### 2. Evolution to Enterprise Data Architecture
- **Terminology Shift:** The project moved away from "Inventories" and "Frameworks" to "Catalogs", "Ontologies", and "Canonical Schemas" to reflect engineering rigor.
- **Architecture:** Adoption of a Data Lakehouse pattern (Bronze/Silver/Gold layers).
- **Deliverables:**
    - **NCAIF** became the **Enterprise Data Model (EDM)** (Conceptual/Logical).
    - **Data Catalog:** Implemented via a structured spreadsheet initially, separating Business Glossary from Technical Data Dictionaries.
    - **Governance:** Codifying rules (Data Owner, Quality, Lineage).

### 3. Specific Initiatives
- **Loss & Damage:** Creation of a Logical Data Model for disaster reporting (aligned with Sendai).
- **Data Product:** The ADPC Risk Platform is treated as a "Gold Layer Data Product".

## Archived Source Files
- `ADPC management strategy.md`
- `Aligning with UNDP-BTR Project.md`
- `Details of data architecture of CRDB.md`
- `Loss and Damage Estimation Ideas.md`
- `Refine CRDM implementation using data architecture jargon.md`
- `Updated Implementation plan v5.md`
