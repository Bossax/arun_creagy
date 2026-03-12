# FGD2 — Action-oriented Summary (DCCE / CRDB — NCAIF)

- Date: 2026-03-11
- Source transcript (raw): [`ψ/inbox/(External Onsite) DCCE Focus Group Discussion 2 on National Climate Adaptation Information Framework-20260311_093601.vtt`](ψ/inbox/(External%20Onsite)%20DCCE%20Focus%20Group%20Discussion%202%20on%20National%20Climate%20Adaptation%20Information%20Framework-20260311_093601.vtt:1)
- Source transcript (cleaned): [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11_FGD2_transcript_clean.md`](ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11_FGD2_transcript_clean.md:1)
- In-room meeting minutes (use as ground truth when transcript is imperfect): [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md`](ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md:1)
- Key insight log (decision-maker mental model): [`ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md`](ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md:1)

---

## 1) CRDB status (where we are now)

Phase 1 direction is already aligned and should remain stable:

- **Phase 1 MVP priority**: MVP‑3 (Recommended Baseline Registry) + MVP‑2 (Disaster data ingestion + Loss & Damage groundwork)
- **Sitemap stance**: Option 3 (Hybrid / workflow-pattern-first)
- **Architecture stance**: catalog-first (link-first)
- **Publishing rails**: Open → data.go.th; Non-open → GDX; Sensitive → internal-only
- **Governance gates**: G1–G5

Reference: [`ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md)

---

## 2) What FGD2 added / reinforced (signals to bake into deliverables)

### 2.0 Sitemap-first expectation is a steering constraint (platform framing)

Decision-maker mental model to design for:

- DCCE officials were highly focused on the **sitemap**.
- In leadership’s head, **“website” = “information platform.”**
- Concrete expectation: **baseline data inventory + adaptation information website**.

Packaging implication: present CDM / backend logic as the **reason the sitemap works** (trust, coherence, sustainability), not as the “main output” that competes with the website.

Source: [`ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md`](ψ/memory/logs/info/2026-03-11_16-59_fgd2-sitemap-focus-platform-framing.md:1)

Additional sitemap signal:

- Participants want to see a **more detailed sitemap** (current view is too broad).
- They explicitly asked whether **topics can still change** and whether their teams can **add/modify** topics later.

Source: [`ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md`](ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md:1)

### 2.1 “Endorsed baseline registry” must include **guidance + recency**, not just a list

Stakeholders want:

- A **recommended/endorsed** baseline so users don’t have to audit provenance themselves.
- Clear **“what it’s valid for / not valid for”** guidance (plain language for Tier 1).
- **Last updated** / version visibility to build trust.

Anchor from transcript (cleaned): endorsement + advice + update timing discussed around the “บัญชีชุดข้อมูล…ที่ได้รับการรับรอง” section.

### 2.2 Data catalog must support **multiple access rails** (open, G2G, internal)

FGD2 reinforces that “catalog” is broader than open data:

- Some datasets are publishable openly (harvested to data.go.th through **CKAN** / agency catalogs)
- Some datasets are **G2G** (GDX) and require a data sharing agreement process
- Some datasets are **internal** / sensitive (kept discoverable internally with steward contact)

Note: “SECAN” is the commonly referenced government catalog implementation (CKAN-based).

Anchor from transcript (cleaned): SECAN/data.go.th + GDX described in the DGA alignment section.

### 2.3 “Implementation” is next year; Phase 1 is **business requirements + logical structure**

FGD2 clarifies that the project is delivering:

- A **business requirement / logical architecture** foundation
- Then **implementation choices (DB tech, SQL flavor, physical design)** follow later and depend on the implementation project

This helps expectation management: Phase 1 deliverables must be “usable as specs” and “handoff-ready,” not “build artifacts.”

### 2.4 The “adaptation cycle completeness” ask is explicit

DCCE asked that the framing covers the full adaptation cycle:

- Risk
- Planning
- Implementation
- M&E

Source: [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md`](ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md:13)

### 2.5 Automation expectation should be acknowledged (even if Phase 1 is not a build)

DCCE asked whether the “boxes” need sequencing, how data flows and links between boxes, and stated an interest in making it **as automated as possible**.

Packaging implication: Phase 1 outputs should include a short “automation roadmap” note distinguishing:
- automation by metadata (recommendations, harvesting, discovery)
- automation requiring an integration/build project (APIs, pipelines)

Source: [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md`](ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md:14)

---

## 3) Decisions captured (today)

No new Phase 1 decisions were required beyond what is already confirmed in the decision log; FGD2 mainly **validated** and **clarified what “good” looks like** for the outputs.

---

## 4) Actions (next 2–3 weeks, action-oriented)

### A0) Hard deadline captured in minutes

- Deliverable: send the requested report
- Due: **23 March (before 10:00)**
- Source: [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md`](ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md:51)

### A1) Update “project status” note (supersede the outdated status brief)

- Deliverable: a short **CRDB Project Status (current)** note that reflects:
  - FGD1 + FGD2 completed
  - Interim report practical deadline **27 March** (billing constraint) and formal milestone **7 April**
  - Phase 1 deliverables now shift to: Baseline Registry schema + intake/quarantine templates + governance gates packaging
- Owner: Arun / project team
- Due: 2026-03-12 (first draft)

Anchors:
- Interim deadline note: [`ψ/incubate/DCCE/CRDB/CRDB - Implementation Plan.md`](ψ/incubate/DCCE/CRDB/CRDB%20-%20Implementation%20Plan.md:451)
- Phase 1 decisions: [`ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/inbox/active/phase1_decision_log.md:18)

### A2) Baseline Registry schema — add “endorsement guidance + update cadence” fields

- Deliverable: baseline registry schema table (MVP‑3) updated with:
  - endorsed_by / co-signature model
  - intended_use / not_for_use (plain language)
  - last_updated / version / revision_policy
  - access_rail (Open / GDX / Internal)
- Owner: Arun (draft), validate with DCCE focal points
- Due: 2026-03-14

### A3) Publishing rails checklist — concretize CKAN + GDX narrative

- Deliverable: one-page checklist that explains:
  - what to publish where
  - minimum metadata to make harvesting work
  - what documentation is required for G2G exchange (DSA template usage)
- Owner: Arun
- Due: 2026-03-14

### A4) MVP‑2 groundwork — disaster intake + quarantine + revision flags (template)

- Deliverable: template package (markdown or spreadsheet spec):
  - event registry minimal fields
  - impact observations
  - validation flags + revision history
- Owner: Arun
- Due: 2026-03-18

### A5) Late April workshop design stub (from FGD2)

- Deliverable: 1-page “Late April workshop concept” capturing:
  - objective: bring **providers + processors + users** together
  - example: make visible that some agencies already run advanced analyses (e.g., สนข), and how DCCE can legally reuse/publish
- Owner: Arun
- Due: 2026-03-20

### A6) Create a 1-page narrative: “Backend enables sitemap” (expectation management)

- Deliverable: 1-page explainer that connects:
  - sitemap/website (what leaders want to see)
  - to CDM + governance gates + product logic (what makes it sustainable and trustworthy)
- Owner: Arun
- Due: 2026-03-14

### A7) Produce a drill-down sitemap + define a change process (to match stakeholder expectations)

- Deliverable:
  - **Sitemap vNext** (2–3 levels deep) showing: (a) workflow-pattern-first entry points, (b) where baseline inventory sits, (c) how subject areas surface without becoming the primary nav.
  - A short **sitemap change process** note: what is stable vs flexible, how teams propose new topics, and how changes are reviewed/approved.
- Owner: Arun
- Due: 2026-03-18

Source: [`ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md`](ψ/memory/logs/info/2026-03-11_17-12_fgd2-sitemap-needs-more-detail-and-remains-flexible.md:1)

---

## 5) Risks & watchpoints

- **Scope creep**: avoid turning Phase 1 into a “data lake build.” Keep outputs as specifications + templates.
- **Trust gap**: without endorsement + versioning + “how to use” guidance, the baseline registry will not solve the audit burden.
- **Classification ambiguity**: must agree owners for “what can be open vs GDX vs internal.”

## 6) Operational signals captured (minutes-first)

- **Stewardship**: each subject-area needs a clear admin/steward.
- **AI assistance ask**: DCCE wants AI to help recommend datasets; suggestion system can be metadata-driven.
- **System overlap concern**: participants noted overlap among data catalog / central DB / adaptation system; expectation is eventual consolidation/integration with access controls.
- **Licensing + ownership**: project-funded datasets (e.g., academic outputs) require licensing/terms before publishing; DCCE wants to decide disclosure level.
- **Foreign-source reuse**: ingesting/using IPCC materials requires an internal SOP.

Source: [`ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md`](ψ/incubate/DCCE/CRDB/inbox/writing_notes/2026-03-11-FGD2-Meeting-Minute.md:18)
