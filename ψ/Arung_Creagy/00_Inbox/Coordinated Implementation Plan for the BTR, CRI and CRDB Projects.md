---
type:
  - strategy
status:
  - archived
version: 3
created: 2025-11-05
project:
  - DCCE_CRDB
  - DCCE_CRI
  - UNDP_BTR
related_hypothesis: "[[ ]]"
---
>[!note] Change log
>- V2 update per CRDB and BTR updates
>- V3 update strategy, assign roles to suitable projects, address risks of interdependency among projects' tasks per [[ADPC management strategy]] [[2025-11-06]]

### 1. Purpose and Strategic Framing

This coordinated plan integrates the Biennial Transparency Report (BTR), Climate Risk Index Phase 2 (CRI), and Climate Risk Database (CRDB) projects.

It is based on a critical operational constraint: the **ADPC Climate Risk Platform** (a component of the BTR project) is a fixed deliverable bound by its Terms of Reference (TOR) and its implementation plan cannot be modified.

Therefore, this plan adopts an **adaptive integration** strategy. The inflexible ADPC platform will be treated as the first primary data source. The flexible projects (CRDB and CRI) will be sequenced to **observe, ingest, and leverage** the ADPC platform's outputs. This approach turns a constraint into an advantage, ensuring the national data architecture (NCAIF) designed by CRDB is not theoretical but is "battle-tested" from day one against a real, complex data product.

### 2. Strategic Integration and Data Flow

Instead of mandating standards _to_ the ADPC platform, we will use its outputs as the _input_ to define the national standard. The data flows as follows:

1. **Source (ADPC):** The BTR-ADPC team delivers its Climate Risk Platform and associated data marts as defined in its TOR.
    
2. **Ingest & Standardize (CRDB):** The CRDB team's _first_ technical task is to analyze the ADPC platform's data marts. It will use these to design the "Bronze" (ingestion) and "Silver" (standardized) layers of the DCCE data lakehouse. The NCAIF and metadata standards will be built _from_ this real-world example.
    
3. **Consume & Refine (CRI):** The CRI team acts as the first "customer" of the CRDB's "Silver" layer data. It will use these standardized, GIS-ready datasets (originating from ADPC) to develop and validate its new indices.
    
4. **Consume & Synthesize (BTR):** The BTR Adaptation Chapter team (the final "customer") consumes all outputs: the CRDB-standardized data, the CRI-validated indices, and the M&E framework, to synthesize the final report.
    

### 3. Complementary Roles and Responsibilities (Revised)

- **BTR (ADPC Component):**
    
    - **Role:** Data Source.
        
    - **Responsibility:** Delivers the Climate Risk Platform and its data marts as a self-contained product, per its fixed TOR. Provides technical documentation and a presentation of its data schema (at the Nov 13 workshop) for other teams to observe.
        
- **CRDB (DCCE / Creagy):**
    
    - **Role:** Data Integrator & Architect.
        
    - **Responsibility:** Ingests and maps the ADPC data marts. Designs the **National Climate Adaptation Information Framework (NCAIF)** and data lakehouse architecture _based on_ this ingestion process. Produces standardized, cataloged, and GIS-ready data products (Silver/Gold layers) for use by other projects.
        
- **CRI (Creagy / DCCE):**
    
    - **Role:** First Customer & Analyst.
        
    - **Responsibility:** Consumes the CRDB-standardized data to develop, validate, and pilot the new Impact, Resilience, and Readiness Indices. Provides validated index datasets back to the CRDB for inclusion in the national catalog.
        
- **BTR (M&E and Chapter Component / Creagy):**
    
    - **Role:** Final Synthesizer & End-User.
        
    - **Responsibility:** Designs the conceptual M&E framework. Consumes the final data from CRDB and indices from CRI to populate the M&E baseline and write the national Adaptation Chapter.
        

### 4. Temporal Alignment (Condensed Gantt Overview)

This timeline is re-phased to show the new dependencies. CRDB and CRI tasks are _intentionally_ delayed to wait for the first ADPC outputs.

| Month          | BTR (ADPC Platform)      | CRDB (Data Architecture)                                                   | CRI (Index Development)                                 | BTR (M&E + Chapter)                        | Key Cross-Project Milestones                                           |
| -------------- | ------------------------ | -------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------------------- |
| **Nov 2025**   | Inception & Presentation | **Observe:** Attend ADPC presentation                                      | **Observe:** Attend ADPC presentation                   | Inception, M&E Framework (Conceptual)      | **Nov 13: Joint Kick-off.** ADPC presents its technical schema.        |
| **Dec–Feb 26** | **(BUILDING)** Per TOR   | **Design:** Map ADPC schema to NCAIF. Define metadata specs.               | **Design:** Index methodology (using proxy/old data)    | M&E Framework (Conceptual)                 | ADPC provides v0.1 data schema                                         |
| **Mar–Apr 26** | **(BUILDING)** Per TOR   | **Ingest:** Build "Bronze" pipeline for ADPC data.                         | Methodological validation                               | M&E Data Reference Sheet (Draft)           | **MILESTONE: ADPC delivers v1.0 data marts.**                          |
| **May–Jun 26** | **Handover & Training**  | **Standardize:** Produce "Silver" layers from ADPC data. Populate catalog. | **Build:** Ingest "Silver" data. Calculate new indices. | **Integrate:** Map M&E sheet to CRDB data. | **Joint Validation Workshop:** (CRI, CRDB, BTR) to review new indices. |
| **Jul 2026**   | (Support)                | (Support)                                                                  | Final index datasets & report                           | **Drafting:** Adaptation Chapter           | Data inputs for BTR Chapter are "frozen."                              |
| **Aug 2026**   | (Support)                | (Support)                                                                  | (Support)                                               | **Drafting & Review**                      | **(FLOAT):** 2-3 weeks of contingency buffer for data/index revisions. |
| **Sep 2026**   | (Closed)                 | Final evaluation                                                           | (Closed)                                                | **Final Submission**                       | Final Steering Committee & Closure.                                    |

### 5. Governance and Coordination Mechanisms

- **Joint Steering Committee:** Oversees high-level schedule, dependencies, and resolves cross-project resource conflicts.
    
- **Data Steward Group:** (Critical) One technical lead per project (BTR-ADPC, BTR-M&E, CRI, CRDB).
    
    - **First Task (Nov 13):** Attend the ADPC presentation to capture all technical specifications.
        
    - **Ongoing:** Meets bi-weekly to manage the data-flow, resolve schema/ingestion issues, and ensure CRDB-standardized data meets CRI/BTR needs.
        
- **Monthly Alignment Meetings:** Track deliverables against the revised timeline.
    
- **Cross-Review Protocol:** All major _methodological_ outputs (NCAIF, Index Methodology, M&E Framework) are reviewed by all teams before being finalized.
    

### 6. Key Risks and Mitigation (Revised)

This plan introduces new risks while mitigating old ones.

| Risk                           | Potential Impact                                                                                                                                         | Mitigation                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ADPC Data "Black Box"**      | The ADPC platform's data marts are delivered late, are technically unusable, or have a poorly documented schema, making ingestion by CRDB impossible.    | **(Proactive Observation):** The CRDB/CRI teams will _not_ wait. They will treat the **Nov 13 ADPC presentation** as the primary source of technical specs and begin designing the ingestion pipeline _immediately_ in parallel, based on those (assumed) specs.                                                                |
| **Cascading Schedule Failure** | A delay in the ADPC platform (Mar/Apr 2026) creates a cascading delay for CRDB, CRI, and the final BTR chapter, making the Sep 2026 deadline impossible. | **(Decoupling):** The CRI team will develop its index _methodology_ and _code_ in Jan-Feb using _Phase 1 data_ or _proxy data_. This way, they are "ready to run" the new ADPC data as soon as it comes through the CRDB pipeline. The BTR M&E framework will also be designed conceptually and decoupled from data population. |
| **Data Integration Friction**  | The CRDB-standardized ("Silver") data does not meet the specific analytical needs of the CRI team.                                                       | **(First Customer Principle):** The CRI team is designated as the "first customer." The Data Steward Group will prioritize CRI's data requirements, and the CRI team lead must formally "sign off" on the CRDB "Silver" data schema before beginning their main analysis.                                                       |
| **Stakeholder Data Access**    | Delays from external (non-project) agencies in providing _other_ key datasets (e.g., socioeconomic data) slows all projects.                             | **(Unified Escalation):** All data requests to external agencies will be channeled through the DCCE/CRDB lead. The Joint Steering Committee will be used to provide high-level, official pressure for any delayed datasets.                                                                                                     |

### 7. Strategic Implications

This revised, adaptive plan is more resilient. It accepts the reality of fixed-TOR contracts and builds a flexible, reactive system around them. By using the ADPC platform as the _foundational test case_, we ensure the final DCCE data architecture (NCAIF) is not a theoretical model but a practical system proven to work with complex, real-world data products. This significantly increases the likelihood