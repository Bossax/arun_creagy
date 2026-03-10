---
type: strategy
status: archived
version: 6
created: 2025-12-03
project:
  - DCCE_CRDB
related_projects:
  - UNDP_BTR (ADPC Risk Platform)
---
>[!note] Change log
v4: increased temporal resolution to week.
v5: Realigned deliverables to Enterprise Data Architecture standards (EDM focus).
v6: **Incorporated synchronization with UNDP/ADPC BTR Project.** - Defined dependencies on ADPC's "Risk Platform" deliverables.
- Aligned timeline to piggyback on ADPC's consultation (Dec) and training (May/Jun).

This implementation plan translates the Terms of Reference (TOR) and the accompanying technical proposal into a coherent technical roadmap. It emphasizes designing conceptual frameworks, metadata specifications and workflows rather than building software. The goal is to create a shared understanding among the project team, DCCE and stakeholders about how climate‑adaptation data and knowledge should be organized, catalogued and governed.

## Strategic Alignment with UNDP-BTR (ADPC)

To ensure efficiency and avoid duplication with the parallel **UNDP-BTR Project (Task 2 implemented by ADPC)**, this project adopts a specific "Curator vs. Manager" distinction:

| Feature     | **ADPC (BTR Project)**                                                            | **CRDB (This Project)**                                                                                            |
| :---------- | :-------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Role**    | **The Builder & Curator**                                                         | **The Architect & Librarian**                                                                                      |
| **Scope**   | **Visualizing** 5 Official Historical Hazards (Flood, Drought, Heat, Storm, SLR). | **Managing** the full Adaptation Data Ecosystem (Risk gaps, Future projections, Vulnerability, Strategy, Results). |
| **Output**  | **Physical Risk Platform** (The "Showroom").                                      | **Enterprise Data Model & Governance** (The "Archive System").                                                     |
| **Synergy** | ADPC collects the specific files; CRDB catalogs them.                             | CRDB codifies ADPC's operational rules into long-term DCCE policy.                                                 |

---

## Key Project Deliverables

### 1. National Climate Adaptation Information Framework (NCAIF)
The NCAIF serves as the **Business and Conceptual Layer** of the Enterprise Data Model.
* **Business Artifact:** A hierarchical knowledge structure derived from NAP sectors and the four TOR domains.
* **Enterprise Data Model (EDM):** Includes **Conceptual Models** and **Logical Models**. *Note: For the Risk Domain, the Logical Model will be reverse-engineered from ADPC’s physical SQL schema.*

### 2. Data System Design (Data Management Framework)
Adopts a **Data Lakehouse (Medallion architecture)** design.
* **Bronze/Silver/Gold:** Conceptual design only.
* **Integration:** The ADPC Risk Platform is mapped as a **Gold Layer Data Product** within this framework.

### 3. Data and Knowledge Assets
1.  **Baseline Data Inventory:** A **data catalog** (Spreadsheet). *Strategy: This inventory will be seeded using the "Consolidated Hazard List" provided by ADPC in Dec 2025.*
2.  **Information Product Inventory:** Captures analytical products. *Strategy: Will register the ADPC Risk Platform as a key asset.*

### 4. Logical Model for Loss & Damage
Formerly the "MVD," this is the **Logical Data Model** for reporting disaster losses, aligned with Sendai/PDNA.

### 5. Data Governance Framework
Establishes roles (Owners, Custodians) and Policies.
* *Strategy:* The "Data Quality Rules" for Risk data will be derived by **codifying the validation protocols** ADPC establishes for their platform.

---

## Work Packages and Activities

### Work Package 1 – Project Initiation and Inception
**Objective:** Establish shared scope and align with parallel initiatives.

* **Kick-off & Scope Refinement (Dec 2025):** Explicitly present the "Showroom vs. Archive" strategy to DCCE to alleviate "double-work" concerns.
* **Inception Report (Dec 2025):** Include the **Dependency Matrix** (see Section 8) confirming reliance on ADPC's Dec 11 outputs.

### Work Package 2 – Data Landscape and Requirements Assessment
**Objective:** Understand data flows and user needs.

* **Risk Landscape "Harvest" (Dec 2025 - Jan 2026):**
    * *Synergy Action:* Instead of separate interviews, **piggyback on ADPC’s Task 2.1 Consultation Meeting**.
    * *Task:* Distribute the **CRDB Metadata Template** to stakeholders during ADPC's session to capture "Data Ownership" and "Availability" without scheduling a new meeting.
* **Non-Risk Assessment (Feb - Mar 2026):** Conduct deep-dive interviews focused on **Adaptation Strategy, Results, and non-hazard sectors** (Agriculture, Tourism) which ADPC is *not* covering.

### Work Package 3 – Enterprise Data Model (EDM) Design
**Objective:** Develop Conceptual and Logical Models.

* **Reverse-Engineer Risk Model (Jan - Feb 2026):**
    * *Synergy Action:* Request ADPC’s **Physical SQL Schema** (Task 2.1.4).
    * *Task:* Abstract this SQL schema into the **Business Logical Model** for the Risk Domain.
* **Design Logical Models (Loss & Damage / Adaptation) (Feb - Mar 2026):** Develop original models for domains outside ADPC's scope.

### Work Package 4 – Development of Data Assets
**Objective:** Populate Inventories and Catalogs.

* **Seed Inventory (Dec 2025 - Jan 2026):**
    * *Synergy Action:* Import ADPC’s **"Consolidated Hazard & Exposure List"** (due Dec 11) directly into the Baseline Data Inventory.
* **Product Registration (Mar - Apr 2026):** Register the **ADPC Risk Platform (Beta)** into the Product Catalog, documenting its lineage and limitations.
* **Gap Analysis (Apr - May 2026):** Identify "Necessary Risk Data" that ADPC rejected (e.g., unofficial/academic data) and flag it for future acquisition.

### Work Package 5 – Knowledge Synthesis & Governance
**Objective:** Synthesis knowledge and define Governance.

* **Codify Governance Rules (Feb - Apr 2026):**
    * *Synergy Action:* Review ADPC’s **"Derived Data Validation Protocol."**
    * *Task:* Adopt this protocol as the standard **Data Quality Policy** in the DCCE Governance Framework.

### Work Package 6 – Evaluation & Closure
**Objective:** Evaluation and Knowledge Transfer.

* **Joint Training Session (May - Jun 2026):**
    * *Synergy Action:* Coordinate with ADPC’s **Task 2.6 Administrator Training**.
    * *Task:* Organize a "Data Day" where staff learn to *use* the Platform (ADPC) in the morning and *manage* the Catalog (CRDB) in the afternoon.

---

## Integrated Timeline & Dependencies (ADPC x CRDB)

This table highlights critical dependencies where CRDB relies on ADPC outputs to proceed.

| Timeline | **ADPC (BTR) Milestone** | **CRDB Dependency / Action** |
| :--- | :--- | :--- |
| **Dec 2025** | **Dec 11:** Submits "Consolidated Hazard & Exposure List" (Official Data). | **WP-4 Action:** Import this list to seed the "Risk" section of the Baseline Data Inventory. |
| **Dec 2025** | **Late Dec:** Consultation Meeting (Data Collection). | **WP-2 Action:** CRDB team attends to distribute Metadata Templates (Harvesting Landscape data). |
| **Jan 2026** | **Task 2.1.4:** Finalizes Database Design & SQL Schema. | **WP-3 Action:** Request Schema to reverse-engineer the "Risk Domain Logical Model." |
| **Jan 2026** | **Task 2.5.1:** Defines Data Sharing & Validation Policies. | **WP-5 Action:** Codify these policies into the DCCE Data Governance Framework. |
| **Mar 2026** | **Task 2.3:** Risk Platform Beta / Interactive Map. | **WP-4 Action:** Register the Platform in the "Information Product Catalog" as a Gold Layer asset. |
| **Apr 2026** | *(ADPC Testing Phase)* | **WP-3 Action:** CRDB Workshops A & B (Broad Stakeholder Design Validation) – *No conflict.* |
| **May 2026** | **Task 2.6:** Dissemination & Admin Training (Accelerated for Budget). | **WP-6 Action:** Co-host "Knowledge Transfer" session to maximize attendance and budget. |
| **Jul 2026** | *(ADPC Final Handover prep)* | **WP-5 Action:** CRDB Major Dissemination Workshop (Launch of Framework). |

## Summary of Active Work Packages

| **WP**                  |    **Dec-25**     |    **Jan-26**    |   **Feb-26**    |   **Mar-26**    | **Apr-26** | **May-26**  | **Jun-26** | **Jul-26** |
| :---------------------- | :---------------: | :--------------: | :-------------: | :-------------: | :--------: | :---------: | :--------: | :--------: |
| **ADPC Major Activity** | *Lists & Consult* |    *DB Build*    | *Risk Analysis* | *Platform Beta* | *Testing*  | *Training*  | *Handover* |            |
| **1. Initiation**       |         ✓         |        ✓         |                 |                 |            |             |            |            |
| **2. Landscape**        |   ✓ *(Harvest)*   |        ✓         | ✓ *(Non-Risk)*  |        ✓        |            |             |            |            |
| **3. EDM Design**       |                   | ✓ *(Risk Logic)* |        ✓        |        ✓        |     ✓      |      ✓      |            |            |
| **4. Data Assets**      |                   |    ✓ *(Seed)*    |                 |        ✓        |     ✓      |      ✓      |     ✓      |            |
| **5. Governance**       |                   |                  |  ✓ *(Codify)*   |        ✓        |     ✓      |      ✓      |     ✓      |     ✓      |
| **6. Closure**          |                   |                  |                 |                 |            | ✓ *(Joint)* |     ✓      |     ✓      |