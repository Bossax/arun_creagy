---
type: idea
status: '["archived"]'
tags: []
created: 2025-11-24
AI_prompt: false
---



Based on the principles of **Enterprise Data Modeling (EDM)** and modern **Data Architecture**, I have revised the implementation plan.

The core shift here is moving from "Static Lists" (Inventories/Frameworks) to "Active Metadata" (Catalogs/Ontologies). In data engineering, we do not just "list" things; we model their relationships and constraints.

### 1. The Translation Layer: Terminology Mapping

Before the detailed revision, here is the dictionary mapping the original policy language to standard Data Architecture/Engineering terminology.

| **Original Term**                 | **New Data Engineering Term**                                 | **Rationale**                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **NCAIF**                         | **Enterprise Conceptual Data Model (ECDM) & Domain Ontology** | "Framework" is vague. An ECDM defines the entities; an Ontology defines the semantic relationships (e.g., "Flood" _causes_ "Damage"). |
| **Baseline Data Inventory**       | **Data Dictionary & Technical Metadata Catalog**              | "Inventory" implies a warehouse list. "Data Dictionary" describes schemas, types, and constraints (Technical Metadata).               |
| **Information Product Inventory** | **Data Product Registry (Business Metadata)**                 | Analytical outputs are "Data Products." A Registry tracks their business value, ownership, and versioning.                            |
| **MVD (Minimum Viable Dataset)**  | **Canonical Logical Schema (Interoperability Standard)**      | MVD is a set of requirements. In engineering, this is a "Canonical Schema" that disparate systems must map to.                        |
| **Data System Design**            | **Data Platform Reference Architecture**                      | This encompasses the Lakehouse patterns, lineage, and integration standards.                                                          |

---

### 2. Revised Deliverables (Technical Reframing)

#### 1. Enterprise Conceptual Data Model (ECDM) & Domain Ontology

Formerly: National Climate Adaptation Information Framework (NCAIF)

Instead of a "framework," this deliverable is the Semantic Layer of the platform. It defines the Business Glossary and the high-level Entity-Relationship (ER) Model independent of physical storage.

- **Engineering Goal:** Develop a machine-readable Ontology (e.g., using SKOS or OWL standards) that enforces the relationships between `Hazard`, `Exposure`, and `Impact`.
    
- **Function:** It acts as the "Graph" that allows queries to traverse from a policy goal (Adaptation) down to a specific physical dataset.
    

#### 2. Data Platform Reference Architecture (Lakehouse Pattern)

Formerly: Data System Design

This defines the Solution Architecture for the Data Lakehouse.

- **Bronze Layer (Raw Zone):** Specifications for immutable ingestion logs and object storage partitioning (e.g., `s3://landing/source/date/`).
    
- **Silver Layer (Conformed Zone):** Specifications for data cleaning, deduplication, and standardizing types (casting strings to integers, normalizing spatial reference systems).
    
- **Gold Layer (Curated Zone):** Dimensional modeling (Star Schemas) optimized for BI tools and the Data Product Registry.
    

#### 3. Enterprise Data Catalog (The Metadata Repository)

Formerly: Data and Knowledge Assets

We replace the two "inventories" with a unified Data Catalog implementation that segregates metadata types:

- **Technical Metadata (Source-Aligned):** Automated crawling of schemas, file formats (Parquet/CSV), and column-level profiling from the Bronze/Silver layers.
    
- **Business Metadata (Consumer-Aligned):** The "Data Product Registry." This maps the Gold Layer tables to the ECDM entities, adding context (e.g., "This dataset supports Indicator 13.1").
    
- **Data Lineage:** Visualizing the path from Raw Data -> Transformation Logic -> Final Report.
    

#### 4. Canonical Logical Schema for Loss & Damage

Formerly: Minimum Viable Dataset (MVD)

The MVD is redefined as the Target Logical Schema for disaster reporting.

- **Engineering Goal:** Define a platform-agnostic schema (JSON Schema or XSD) that specifies mandatory fields, data types (e.g., `ISO 8601` for dates), and cardinality rules.
    
- **Integration:** This schema serves as the "Contract" that DDPM and other agencies must satisfy when pushing data to the platform.


> The **Minimum Viable Dataset (MVD)** is essentially a **specific "View" or "Slice"** of the broader **Enterprise Data Model (EDM)**.


| **Layer**                 | **The Artifact**  | **Description**                                                                              | **Relation to MVD**                                                                     |
| ------------------------- | ----------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **1. Conceptual**         | **EDM (NCAIF)**   | Defines abstract concepts: _"A Hazard causes an Impact on an Asset."_                        | The MVD **inherits** these definitions. It cannot invent a new definition for "Hazard." |
| **2. Logical**            | **EDM (Logical)** | Defines attributes: _"An Impact must have a Value and a Unit."_                              | The MVD **selects** the mandatory attributes needed for reporting.                      |
| **3. Physical/Canonical** | **The MVD**       | Defines the strict schema: _"field: `impact_cost`, type: `decimal(10,2)`, required: `true`"_ | The MVD is the **implementation contract** ensuring data fits the Logical model.        |

---

### 3. Revised Work Packages & Task Requirements

Here is how the specific tasks within the Work Packages (WPs) should be rewritten to reflect this engineering rigor.

#### **Revised WP 2: Data Landscape & Profiling**

_Objective: Assess Technical Feasibility and Data Quality._

- **Task 2.1: Source System Analysis (formerly Desk Research).** Analyze source systems (DCCE, DDPM) for connection protocols (API vs. FTP), volume, and velocity.
    
- ~~**Task 2.2: Data Profiling (formerly Current-state assessment).** Run automated profiling tools on sample data to identify null rates, distinct value counts, and schema drift risks.~~
    
- **Task 2.3: Structural Gap Analysis (formerly GIS readiness).** Determine if existing datasets have valid spatial indices and coordinate reference systems (CRS) compatible with the proposed Lakehouse.
    

#### **Revised WP 3: Architecture & Modeling**

_Objective: Define the EDM and Platform Blueprints._

- **Task 3.1: Develop Conceptual Data Model (formerly Refine NCAIF).** Model the entities (Hazards, Assets) and relationships (One-to-Many, Many-to-Many) using standard notation (UML or ERD).
    
- **Task 3.2: Design Logical Data Models.** Define the specific attributes, primary keys, and foreign keys for the Silver and Gold layers.
    
- **Task 3.3: Metadata Metamodel Design (formerly Metadata service).** Define the schema _for the catalog itself_. (e.g., "Every Data Product must have an Owner, a Refresh Schedule, and a Quality Score").
    

#### **Revised WP 4: Catalog Implementation & Schema Definition**

_Objective: Populate the Metadata Repository and Define Contracts._

- **Task 4.1: Data Catalog Configuration (formerly Inventory template).** Configure the Data Catalog software (or structured repository) to ingest Technical Metadata.
    
- **Task 4.2: Metadata Enrichment (formerly Registration).** Tag ingested datasets with Business Glossary terms from the ECDM (Task 3.1).
    
- **Task 4.3: Define Canonical Schema (formerly Design MVD).** Author the schema specifications and validation rules (e.g., "If `Event_Type` = 'Flood', `Water_Level` is mandatory").
    

---

### 4. Why This Modification Matters (The "Why")

**1. "Inventory" vs. "Catalog":**

- _Modification:_ An inventory is a static spreadsheet. A Catalog is an active system.
    
- _Reason:_ In data engineering, metadata changes constantly. A "Catalog" implies we are setting up a system that can eventually automate the scanning of new data. If you deliver a spreadsheet (Inventory), it is obsolete the day you finish it.
    

**2. "Framework" vs. "Conceptual Model / Ontology":**

- _Modification:_ "Framework" implies a document. "Conceptual Model" implies a diagrammatic structure.
    
- _Reason:_ Developers cannot code against a "Framework document." They can code against a Conceptual Model because it explicitly maps to database tables. This bridges the gap between the "Semantic Layer" (Policy) and the "Physical Layer" (Database).
    

**3. "MVD" vs. "Canonical Schema":**

- _Modification:_ MVD sounds like a product. Canonical Schema is an interface contract.
    
- _Reason:_ This clarifies that the project is not just listing variables, but defining strict **Data Quality (DQ) rules** that other agencies must follow to achieve interoperability.
    

