# CRDB and Current DCCE IT / Data Landscape — Working Integration Note

## Purpose

Capture the **current working understanding** of DCCE’s IT and data environment that is relevant to CRDB, and describe how CRDB Phase 1 deliverables are expected to fit into that landscape. This is a source artifact for the progress meeting and for interim-report framing; it is not a complete IT inventory.

---

## 1. Known components in the DCCE / partner environment

### 1.1 Line-agency analytical systems (external but tightly coupled)

- **DPT flood / drainage models**
  - Status: in-house hydraulic models used for drainage and flood analysis.
  - Inputs:
    - Rainfall intensity and duration (IDF-like curves, e.g. 60-year rainfall statistics).
    - Existing pipe and drainage network characteristics.
  - Relevance to CRDB:
    - DPT wants climate rainfall variables from CRDB/CRI to **feed these existing models**, not a replacement model.
    - CRDB climate outputs must be documented as **model-ready inputs** (variables, time horizons, spatial resolution, uncertainty/assumptions).

- **Other line-agency systems (inferred)**
	- Hazard, exposure, and impact systems in agencies such as DDPM, NSO, NESDC, etc., which are being catalogued in the CRDB **data product landscape** and interview matrices.
	- CRDB is expected to connect to these systems via **catalog entries**, not to absorb their infrastructure.

### 1.2 DCCE research centre data holdings (internal, under investigation)

- DCCE’s **research centre** likely maintains internal climate and weather datasets (e.g. time series, gridded analyses), though exact systems and storage patterns are not yet documented in CRDB artifacts.
- Director Toey has requested a dedicated conversation with the research centre to:
	- Clarify **what datasets exist**, how they are maintained, and under what constraints they can be used.
	- Determine when **internal DCCE data** can serve as authoritative baselines for CRDB, instead of relying solely on external platform outputs.

### 1.3 Web and portal surfaces

- Existing **DCCE portal / websites** have been analysed in the gap inventory and matrix:
	- [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Inventory.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Inventory.md)
	- [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Matrix.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Matrix.md)
	- [`ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-DCCE_Website_Content_Gap_Summary.md)
	- Current gaps (summarised):
- Content is fragmented by project and initiative.
- Navigation does not align with user demand/use cases.
- Technical architecture does not yet reflect the NCAIF structure.

### 1.4 DCCE IT department (6th-floor) data-platform project

- **Organisational location and mandate**
  - Hosted by the **IT department on the 6th floor**, described in the meeting as the unit leading a project to **develop a central data system for DCCE**.
  - A consulting firm has already been engaged to **study and design** this system.

- **Current known scope and uncertainties** (from [[ψ/inbox/2026-03-24-team-meeting-additional-context-transcript|2026-03-24-team-meeting-additional-context-transcript]])
  - Intends to **connect and consolidate disparate DCCE data platforms and databases** into a shared architecture for the department.
  - It is not yet clear from available documents whether the study is being framed primarily as an **engineering/IT exercise** or whether it is also grounded in **scientific and domain requirements** (adaptation, risk, mitigation, etc.).
  - We do **not yet know**:
    - Where the **scientific requirements** are sourced from (e.g. from CCE, research centre, line programmes).
    - What **artifacts** (conceptual models, schemas, standards, governance documents) the consultants are expected to produce.

- **Signals from FGD2 and internal discussions**
  - Staff from the 6th floor indicated in **FGD2** that there will be:
    - a **data governance meeting**;
    - explicit discussion of **data stewards**; and
    - attention to **data standards** for DCCE data.
  - This suggests the project is not only about a web front-end or landing page but also about **underlying data architecture and governance**.

- **Relationship to existing DCCE web structure**
  - The current **DCCE website** is primarily a **landing page structured by departmental organisation**, with sub-tabs for:
    - news and project pages;
    - PDF-based reports and information;
    - a tab for the **CCE Climate Change Environmental Data Center**, which currently contains limited structured data;
    - links to tools such as the **risk map**, **SPI drought index map**, and **T-GHG** greenhouse-gas accounting system;
    - a **"climate change adaptation"** tab that currently cannot be clicked (no content yet).
  - The 6th-floor IT project appears to be the candidate platform that will **underpin or replace parts of this structure** once it matures.

- **Platform and hosting hints**
  - Some existing tools (e.g. the **spatial risk map**) appear to run on platforms such as **Tableau**, likely hosted on **virtual machines provided by DCCE**.
  - Beyond provision of VMs, there is **no strong evidence yet** of a coherent, department-wide **data platform or governance framework** supporting these tools.

- **Key integration question for CRDB**
  - The progress meeting with Director Toey needs to make explicit **how CRDB’s outputs (NCAIF, CDM, sitemap, governance gates)** will serve as **requirements and guardrails** for this 6th-floor project, so that the central DCCE data system does not evolve independently of adaptation and climate-risk needs.

---

## 2. CRDB Phase 1 deliverables and how they fit

### 2.1 NCAIF and CDM as logical/semantic backbone

- **NCAIF** (National Climate Adaptation Information Framework)
  - Captures how adaptation-related content should be organised for users (policy makers, implementers, analysts).
  - Described in detail in [`ψ/incubate/DCCE/CRDB/output/National Climate Adaptation Information Framework.md`](ψ/incubate/DCCE/CRDB/output/National%20Climate%20Adaptation%20Information%20Framework.md).
  - IT implication: NCAIF defines the **semantic structure** and page archetypes the portal must support, regardless of hosting stack.

- **CDM** (Conceptual Data Model)
  - Provides the **entity-relationship** and subject-area logic across climate, risk, impact, resilience, and adaptation planning.
  - Core reference: [`ψ/incubate/DCCE/CRDB/output/Conceptual Data Model for climate risk and adaptation data system.md`](ψ/incubate/DCCE/CRDB/output/Conceptual%20Data%20Model%20for%20climate%20risk%20and%20adaptation%20data%20system.md).
  - IT implication: informs downstream logical and physical schemas; also underpins **metadata fields, crosswalks, and baselines**.

### 2.2 Catalog-first and link-first integration stance

- CRDB Phase 1 is anchored on **catalog-first, link-first** architecture, consistent with DGA rails:
  - Open data → data.go.th and public catalogs.
  - Non-open/shared data → GDX and controlled channels.
  - Sensitive/internal data → internal-only stores governed by DCCE and partner agencies.
- For IT/infrastructure:
	- CRDB is expected to produce and maintain:
		- A **catalog layer** (metadata, endpoints, ownership, access rules).
		- Integration points that **link out** to agency systems and portals, not rehost all data centrally.
	- For the 6th-floor IT project specifically:
		- CRDB’s **NCAIF, CDM, sitemap, and governance gates** should be treated as **upstream requirements artifacts** informing the consultants’ design of the central DCCE data system.
		- The central system should expose services and storage that allow **CRDB catalogs, baselines, and governance decisions** to be implemented cleanly, rather than forcing CRDB into an after-the-fact integration.

### 2.3 Governance gates as integration constraints

- Phase 1 governance gates (from [`ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/archive/phase1_decision_log.md)) define how data move into and through CRDB:
  - G1: classification (internal/exchange/open).
  - G2: minimum metadata and preview.
  - G3: baseline endorsement (who endorses what, for which uses and scales).
  - G4: boundary and crosswalk governance.
  - G5: event/impact schema + timeliness and revision tracking.
- IT implication:
  - Existing DCCE and partner systems must expose enough metadata and structure to satisfy these gates.
  - CRDB deliverables (catalog, CDM, NCAIF pages) must embed these gates into workflows and user interfaces.

### 2.4 Interaction with line-agency models

- CRDB will deliver **model-ready inputs** rather than full pipelines:
  - Example: provide rainfall/climate variables with clear semantics and units that DPT can drop into its flood models.
  - The catalog will record how these variables relate to subject areas in the CDM and to specific models.
- IT implication:
  - Integration is primarily at the **data and metadata interface** (file formats, APIs, schema definitions), not at the level of shared compute environments.

---

## 3. Gaps and open questions (for progress meeting)

- Internal DCCE research data:
  - What exactly is stored, where, and under which governance rules?
  - How can CRDB reference these datasets in catalogs and baselines?

- Model governance:
  - Which models will CRDB explicitly recognise and describe (e.g. DPT flood model, impact estimation models)?
  - How will versions and validation status be tracked in the catalog?

- Technical implementation options:
	- Given existing DCCE IT constraints (not yet fully documented), what are feasible options for:
		- the NCAIF front-end (portal pages, navigation);
		- the catalog/store of metadata and crosswalks;
		- compliance with DGA rails and hosting norms.
		- **alignment with the 6th-floor IT project** so that CRDB requirements (NCAIF/CDM/governance) are built in from the start, rather than bolted on.

This note should be treated as a **living integration note** to be updated as the team learns more from the research centre, DCCE IT, and line agencies.

