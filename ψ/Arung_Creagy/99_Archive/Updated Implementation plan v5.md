---
type: ai_output
tags: []
status: archived
capture_date: 2025-10-31
origin_prompt: "[[]]"
relevance_to: "[[Projects/2025-11_DCCE-CRDB/archived/(Archived) Project implementation revision .md]]"
---


Here is the updated implementation plan. I have reconciled the new Enterprise Data Model (EDM) direction, the specific distinction between logical/physical models, and the updated list of deliverables (Glossaries, Dictionaries, and Spreadsheet Catalog).

Updates are integrated directly into the text, shifting the language from "platform building" to "data architecture."

---

## CRDB - Implementation Plan (v5)

---

type: strategy 

status:

- current
    
    version: 5
    
    created: 2025-11-28
    
    project:
    
- DCCE_CRDB
    
    related_hypothesis:
    
- "[[Refine CRDM implementation using data architecture jargon]]"
    

---

> [!note] Change log
> 
> v2-v4: Timeline and granularity updates.
> 
> v5 (Current): Realigned deliverables to Enterprise Data Architecture standards.

- **NCAIF** is now defined as the **Enterprise Data Model (EDM)**.
- Scope shifted to **Conceptual and Logical Models**; Physical schemas are explicitly out of scope (except for Data Products).
- **Data Catalog** implementation defined as a low-code **Spreadsheet** solution.
- Distinct separation of **Business Metadata** (Glossary) and **Technical Metadata** (Data Dictionaries).
    

This implementation plan translates the Terms of Reference (TOR) and technical proposal into a coherent Data Architecture roadmap. It emphasizes designing the **Enterprise Data Model (EDM)** and **Governance Artifacts** rather than building physical software infrastructure. The goal is to create the "blueprint" (Business Logic, Conceptual & Logical Models) and the "handbook" (Glossary, Dictionaries, Governance) that DCCE requires to manage climate adaptation data.

## Key Project Deliverables and Strategic Framing

### 1. National Climate Adaptation Information Framework (NCAIF) & Enterprise Data Model (EDM)

The NCAIF serves as the **Business and Conceptual Layer** of the Enterprise Data Model. It maps the business logic of climate adaptation into a structured hierarchy.

- **Business Artifact (The NCAIF):** A hierarchical knowledge structure derived from the four TOR domains (Meteorology, Risk, Adaptation, Results) plus mapped subject areas. It acts as the "Business Logic" layer, helping non-technical stakeholders navigate the domain.
    
- **Enterprise Data Model (EDM):** A view of all relevant data entities across the enterprise (DCCE and partners). This includes **Conceptual Models** (high-level entities and relationships) and **Logical Models** (attributes, keys, and definitions). **Physical Models** (database schemas) are out of scope as data resides in external databases.
    

### 2. Analytical Data Product Specifications

While the general EDM remains logical, the project will dive deeper into the **"Gold Layer" (Analytical Data Products)**. For specific high-value analytical products (e.g., Risk Indices, Maps), the project will design:

- **Business Metadata:** Definitions of the product's value, usage, and logic.
    
- **Physical Schema:** The specific structure required to generate these analytical outputs.
    

### 3. Data and Knowledge Assets (The Catalog)

The project will implement a functional **Data Catalog** using a structured **Spreadsheet** approach to enable search and discovery. This includes two distinct layers of metadata:

- **Business Glossary:** A dictionary of business terms and definitions (e.g., "Flood Exposure," "Vulnerability") linked to the NCAIF structure.
- **Data Dictionaries (Technical Metadata):** Detailed technical descriptions of datasets (tables, columns, data types) drafted for essential risk assessment areas.
    

### 4. Logical Model for Loss & Damage (MVD)

Formerly referred to as the "Minimum Viable Dataset," this deliverable is now framed as the **Logical Data Model** for the Loss & Damage subject area. It will detail the entities (events, impacts, costs) and relationships required to report on disaster losses, aligned with Sendai Framework and DDPM requirements.

### 5. Data Governance Artifacts

A framework ensuring data quality and accountability. This is not just a policy document but a set of specific **governance artifacts**:

- **Data Owner & Custodian:** Definitions of roles and assignments for key datasets.
- **Data Quality:** Standards and validation rules.
- **Data Lineage:** Documentation of data flow from source to product.
    

---

## Work Packages and Activities

## Work Package 1 – Project Initiation and Inception

**Objective:** Establish shared understanding of the move toward "Enterprise Data Architecture" and refine the scope with DCCE.

- **Kick-off & Scope Refinement (Nov 2025):** Clarify the distinction between Logical Models (business view) and Physical Schemas (database view). Confirm the "Spreadsheet Catalog" approach.
    
- **Work Plan & Inception Report (Nov–Dec 2025):** Finalize the roadmap.
    
- **Stakeholder Mapping (Nov–Dec 2025):** Identify interview targets for "Business Logic" mapping.
    
- **Baseline Review (Nov 2025 – Jan 2026):** Review existing systems to inform the Conceptual Model.
    

**Deliverable:** Inception report (clarifying EDM scope) and stakeholder engagement plan.

## Work Package 2 – Data Landscape and Requirements Assessment

**Objective:** Map the business logic and assess technical readiness for Logical Modeling.

- **Document Business Logic (Dec 2025 – Jan 2026):** Interview DCCE staff and stakeholders to map out subject areas beyond the initial four TOR domains.
    
- **Current-State Assessment (Dec 2025 – Jan 2026):** Audit existing data flows to identify key entities.
    
- **User-Requirement Interviews (Feb – Mar 2026):** Focus on how users "search" for data to inform the Business Glossary and Catalog structure.
    
- **Data Quality & Schema Assessment (Feb 2026):** Evaluate "Risk Assessment" datasets to prepare for Technical Metadata extraction.
    

**Deliverable:** Data Landscape report & Gap Analysis.

## Work Package 3 – Enterprise Data Model (EDM) & NCAIF Design

**Objective:** Design the Business Artifacts, Conceptual Models, and specific Logical Models.

- **Draft Business Logic & Hierarchy (Jan – Feb 2026):** Create the **Hierarchical Knowledge Structure** (the NCAIF Business Artifact).
    
- **Develop Conceptual Data Model (Jan – Feb 2026):** Identify key entities and relationships across all domains.
    
- **Design Logical Models (Feb – Mar 2026):**
    
    - Develop the **Logical Model** for the **Loss & Damage** entities.
        
    - Draft **EDM Logical Models** for essential risk assessment areas.
        
- **Design Data Product Schemas (Mar 2026):** Design the **Physical Schemas** and **Business Metadata** specifically for Analytical Data Products (Gold Layer).
    
- **Validation (Jan – May 2026):** Focus groups to validate that the Business Logic (NCAIF) matches stakeholder mental models.
    

**Deliverables:**

1. NCAIF Business Artifact (Hierarchy/Glossary).
    
2. Enterprise Data Model (Conceptual & Logical).
    
3. Loss & Damage Logical Model.
    
4. Data Product Physical Schemas.
    

## Work Package 4 – Development of Data Assets (Catalog & Dictionaries)

**Objective:** Create the metadata content and the spreadsheet-based catalog tool.

- **Create Business Glossary (Mar – Apr 2026):** Define business terms associated with the NCAIF entities.
    
- **Draft Technical Metadata & Data Dictionaries (Mar – Apr 2026):** Create detailed data dictionaries for the identified "essential risk assessment" areas.
    
- **Implement Data Catalog (Apr – May 2026):** Build the **Spreadsheet-based Data Catalog** that allows users to search through the Data Dictionaries and Data Products.
    
- **Map Data Lineage (May 2026):** Document the flow from Bronze (Raw) to Gold (Product) for key indicators.
    

**Deliverables:**

1. Business Glossary.
    
2. Technical Data Dictionaries.
    
3. Functional Spreadsheet Data Catalog.
    

## Work Package 5 – Governance, Synthesis & Dissemination

**Objective:** Define governance artifacts and synthesize knowledge.

- **Develop Governance Artifacts (Feb – Apr 2026):** Define specific definitions for **Data Owner, Data Custodian, Data Quality rules, and Data Lineage standards**.
    
- **Knowledge Synthesis (Feb – Apr 2026):** Review literature to ensure the NCAIF Business Logic aligns with national NAP sectors.
    
- **Communication Materials (Apr – Jun 2026):** Create visual representations of the EDM to explain the "Data Architecture" to non-technical staff.
    
- **Dissemination (Jun – Jul 2026):** Workshops to train staff on how to use the Spreadsheet Catalog and interpret the Logical Models.
    

**Deliverables:**

1. Data Governance Artifacts (Roles, Quality, Lineage).
    
2. Knowledge Synthesis Report.
    
3. Training on Catalog Usage.
    

## Work Package 6 – Evaluation & Closure

**Objective:** Evaluate the utility of the models and catalog.

- **Evaluation (Jun – Aug 2026):** Assess if the Spreadsheet Catalog and Logical Models effectively support DCCE's data discovery needs.
    
- **Recommendations (Aug 2026):** Roadmap for future _Physical_ implementation (e.g., moving from Spreadsheet to a dedicated Data Catalog software, or implementing the Data Lakehouse).
    

**Deliverables:** Final Project Report & Roadmap for Physical Implementation.

---

## Timeline Summary

| **WP**             | **Nov-25** | **Dec-25** | **Jan-26** | **Feb-26** | **Mar-26** | **Apr-26** | **May-26** | **Jun-26** | **Jul-26** | **Aug-26** |
| ------------------ | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| **1. Initiation**  | ✓          | ✓          | ✓          |            |            |            |            |            |            |            |
| **2. Landscape**   |            | ✓          | ✓          | ✓          | ✓          |            |            |            |            |            |
| **3. EDM Design**  |            |            | ✓          | ✓          | ✓          | ✓          | ✓          |            |            |            |
| **4. Data Assets** |            |            |            |            | ✓          | ✓          | ✓          | ✓          |            |            |
| **5. Governance**  |            |            |            | ✓          | ✓          | ✓          | ✓          | ✓          | ✓          |            |
| **6. Closure**     |            |            |            |            |            |            |            | ✓          | ✓          | ✓          |

## Risks and Mitigation (Updated)

| **Risk**                                   | **Potential Impact**                                          | **Mitigation**                                                                                                                                           |
| ------------------------------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Confusion over "Logical" vs "Physical"** | Stakeholders expect a built database but get a diagram/model. | **Early Expectation Management:** Explicitly define "EDM" and "Logical Model" in the Kick-off. Emphasize that physical data stays in source databases.   |
| **Spreadsheet Limitations**                | The catalog becomes too large or complex for a spreadsheet.   | **Strict Scope Control:** Focus the catalog on "Essential Risk Assessment" areas first. Design the spreadsheet with a future database migration in mind. |
| **Complexity of Business Logic**           | NCAIF hierarchy becomes too academic and unusable.            | **User-Centric Validation:** Treat the NCAIF as a "Business Artifact" and validate it with non-technical staff early (WP3).                              |