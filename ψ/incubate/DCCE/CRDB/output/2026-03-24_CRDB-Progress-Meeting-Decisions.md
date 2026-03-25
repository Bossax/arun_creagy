# CRDB — Climate Adaptation Team Meeting Decisions (2026-03-24)

## Context

- Source transcripts:
  - Base team meeting transcript: [`ψ/inbox/2026-03-24-transcript-climate-adapataiton-team.txt`](ψ/inbox/2026-03-24-transcript-climate-adapataiton-team.txt)
  - Additional context: [`ψ/inbox/2026-03-24-team-meeting-additional-context-transcript.md`](ψ/inbox/2026-03-24-team-meeting-additional-context-transcript.md)
- Focus: Decisions and directions affecting the **CRDB** project, especially the upcoming **progress meeting** and interim-report revision.

---

## 1. Scheduling and mode of work

### 1.1 Progress meeting with Boss (Thursday)

- The Thursday **progress meeting** with Boss is confirmed as a key checkpoint for:
  - reviewing CRDB progress (NCAIF, CDM, governance); and
  - setting direction for the next interim-report revision.
- Other meetings and fieldwork are scheduled around this slot; it is treated as **fixed**, not tentative.

### 1.2 Downstream timeline (shared across CRI / CRDB / BTR)

- Agreed time structure:
  - **April**: intensive data-acquisition month (especially for CRI impact index and related datasets).
  - **May**: site visits and fieldwork in pilot areas.
  - **June**: follow-up consultations and stakeholder sessions.
  - **July–early August**: committee/board meetings, dissemination, and finalisation of deliverables.
- Implication for CRDB:
  - CRDB must work **within this fixed window**; there is no expectation of additional large discovery phases after August.

### 1.3 Interim-report revision after the progress meeting

- The 23 March interim report has been submitted once; the team agreed that:
  - There will be **another interim-report revision** after the upcoming progress report.
  - That revision will be **anchored** on:
    - the writing plan [`ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim Report Writing Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-12-Interim%20Report%20Writing%20Plan.md); and
    - the latest chapter drafts listed in [`ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md).

---

## 2. Role of CRDB in the multi-project landscape

### 2.1 CRDB as librarian/architect, not primary modeller

- Reconfirmed division of labour:
  - **CRI**: builds indices and impact measures.
  - **BTR**: drives baseline framework and Data Reference Sheet (DRS).
  - **CRDB**: acts as **librarian/architect**
    - structures **NCAIF**;
    - maintains the **CDM** and evidence system;
    - governs datasets and models; and
    - provides standardised climate inputs for downstream models.
- Decision: In Phase 1, CRDB will **not** attempt to own full impact models; it will:
  - supply climate/impact inputs in **standard, documented formats**; and
  - focus on **catalog, CDM, and governance**.

### 2.2 Using CRDB outputs inside line-agency models (DPT example)

- Example agreed in discussion:
  - DPT already runs **in-house flood models** (drainage/pipe models) needing rainfall intensity and duration inputs.
  - CRDB/CRI are expected to provide rainfall/climate scenarios (e.g. return periods, IDF-like statistics) that DPT can plug into those models.
- Direction: CRDB’s climate outputs (hazard variables) must be **usable inputs**, not standalone end-products.

---

## 3. Data dependencies and internal vs external sources

### 3.1 Follow-up on impact-related datasets
- Reminder and agreement:
	- Formal follow-ups are needed (starting next week) on **impact index inputs**, including casualty/loss data from DPT and related agencies.
	- These are required for CRI, and also for **CRDB’s Loss & Damage and readiness narratives**.

### 3.2 Internal DCCE research data vs external outputs
- Concern from Director Toey:
	- Current reliance on external platforms is risky when DCCE’s own **research centre** may hold relevant climate/weather data.
- Direction and planned action:
	- Arrange/confirm a meeting with the **DCCE research centre director** to:
		- inventory internal climate/weather datasets; and
		- clarify how these could serve as **reference/baseline** in CRDB.
	- Preference: where feasible, use **internal DCCE data** as authoritative baselines, with external sources referenced and linked via the catalog.
 
### 3.3 DCCE 6th-floor IT/data platform project

- From the additional-context transcript:
  - The **IT department on the 6th floor** is running a project to design a **central data system for DCCE**, with a consultant already engaged.
  - The current DCCE website is a **landing-page structure** organised by departmental units, linking to:
    - PDF-based reports, news, and project pages;
    - a CCE climate/environmental data centre tab;
    - tools such as the **risk map**, **SPI drought index**, and **T‑GHG** GHG-accounting system;
    - a non-clickable **climate change adaptation** tab.
  - Existing tools (e.g. risk map) appear to run on platforms like **Tableau**, hosted on DCCE virtual machines, with limited shared data-governance structure.
- Direction for CRDB:
  - The **NCAIF, CDM, sitemap, and governance gates** defined by CRDB should be treated as **requirements artifacts** for this 6th-floor project.
  - The progress meeting should position CRDB as providing the **semantic and governance backbone** for the central data system, rather than as just another content producer.

---

## 4. Governance: data and models

### 4.1 Data governance

- Reaffirmed that Phase 1 governance will follow the gates defined in [`ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md):
	- classification (internal/exchange/open);
	- minimum metadata;
	- baseline endorsement;
	- boundary/crosswalk governance;
	- revision history and timeliness, especially for event/impact data.

### 4.2 Model governance (new emphasis)

- New emphasis from the meeting:
  - Governance must cover **models**, not only datasets.
  - Key concerns:
    - which models are treated as reference for specific domains (e.g. flood, impact, economic analysis);
    - how model versions and assumptions are documented;
    - who maintains and endorses these models.
- Direction:
  - CRDB’s governance design and the interim report should explicitly distinguish **data governance** from **model governance**.
  - Future work should plan for a register of **approved/known models** and their relationship to CRDB datasets.

---

## 5. Technical debt and tooling

- Acknowledged issues:
	- Legacy content (e.g. LPA indicators, long textual reports) is hard to structure manually.
	- Current practice often copies content into reports without mapping it into CDM/metadata structures.
- Direction:
 	- Plan for a **tooling layer** (templates, data product cards, semi-automated extraction/normalisation, AI-assisted parsing) as part of CRDB’s evidence system.
	- Avoid over-promising full manual clean-up in the short term; focus on scoping which indicators and datasets must be structured before August.

---

## 6. Implications for upcoming progress meeting, workshop, and interim-report revision

- Use the progress meeting to:
  - Confirm CRDB’s **Phase 1 role** (catalog + governance + climate inputs, not primary modeller).
  - Get management alignment on **model governance** being in scope alongside data governance.
  - Discuss how internal DCCE research data will be brought into CRDB as reference baselines.
	- Clarify expectations for the **next interim-report revision** (what can change before the late-April workshop, and what must wait for later phases).
	- Present and stress-test the **preliminary workshop design** in [`ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-Workshop-Preliminary-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-Workshop-Preliminary-Plan.md), especially:
		- the morning vs afternoon split;
		- breakout grouping hypotheses (by product/MVP, sector, and user tier/capacity);
		- how the workshop adds value beyond the 10+ in-depth interviews.

- These decisions should feed directly into:
  - updates to the progress-meeting agenda: [`ψ/incubate/DCCE/CRDB/output/CRDB_Director_Toey_Progress_Meeting_Agenda.md`](ψ/incubate/DCCE/CRDB/output/CRDB_Director_Toey_Progress_Meeting_Agenda.md);
	- the next revision of the interim report based on the 2026-03-12 writing plan and current chapter drafts; and
	- refinement of the workshop plan and stakeholder list in [`ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-Workshop-Preliminary-Plan.md`](ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-Workshop-Preliminary-Plan.md).
