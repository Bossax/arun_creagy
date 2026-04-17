Using the current evidence coverage map in [`ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Coverage-Map.md), here is how to sharpen the Director Toey agenda into three blocks:

- What is already defensible
- What is still weak (needs decisions)
- What the late‑April workshop should validate

---

## 1. What is already defensible

### 1.1 Product and content (strong)

Defensible talking points:
- The **current DCCE portal surface** is clearly mapped and shows major content gaps relative to what NCAIF requires (policy-maker front door, area profiles, measures, tools & catalog, results/M&E).
- A **future-facing NCAIF structure** is already articulated and is consistent with climate-service UX best practice and stakeholder needs.
- UX principles (information scent, shallow navigation, matrix entry routes, progressive disclosure, tools vs catalog separation) for NCAIF are backed by a dedicated UX evidence review, not just internal taste.

### 1.2 Data and method (conceptual strength, moderate coverage)
Defensible talking points:
- The CDM is a **necessary conceptual bridge** between TOR requirements and any implementation of NCAIF/CRDB; this is supported by both the TOR and comparative data-architecture literature.
- There is a clear, documented logic from **use cases → CDM → MVPs**, not just a schema invented in isolation. %% aren't there two lines of logic? 1) interview results => Use cases => MVPs => Sitemap? and 2) Literature review => CDM => Sitemap? %%
- Pack A risk-map evidence and its limitations are explicitly acknowledged; CDM design deliberately avoids over-claiming what current risk maps can do.

### 1.3 Evidence-pack and translation layer (strong)

Defensible talking points:
- Stakeholder needs are **systematically synthesized** and cross-checked across agencies; design choices are grounded in this matrix, not a single workshop.
- There is a clear **traceability chain** from interview statements to use cases, gap clusters, and design decisions.
- You can explain how newer interviews (e.g., FTI, UDDC, BMA, DPT) actually shifted or reinforced earlier assumptions.

---

## 2. What is still weak (needs decisions from Director Toey and DCCE)

### 2.1 Governance and operating model

Evidence base:
- [`2026-03-23-general-execution-gaps-for-NCAIF-CDM-and-data-governance.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-general-execution-gaps-for-NCAIF-CDM-and-data-governance.md)
- [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/archive/phase1_decision_log.md)
- [`2026-03-11_FGD2_action_summary.md`](ψ/incubate/DCCE/CRDB/inbox_source/2026-03-11_FGD2_action_summary.md)

Weak / under-specified areas to put on agenda as **decision questions**:
- Who will actually perform **owner / steward / custodian / reviewer / approver** roles for priority topics (e.g., baselines, risk layers, evidence packs)?
- What is the **decision-rights model** for:
  - endorsing a dataset as a national baseline,
  - superseding or deprecating outdated baselines,
  - approving public-facing products?
- How will **publishing rails** (what can go out, at what level of detail, with what caveats) differ by:
  - dataset class (indicators, raw data, model results),
  - surface (portal pages vs download vs API)?
- What is an acceptable **operating rhythm** for governance (who meets, how often, and with what agenda)?

### 2.2 Data and method (execution side)

Evidence base:
- Same as 1.2 above.

Weak / under-specified areas:
- Confirm **first domains** for implementation (e.g., “for Phase 1 we will operationalize X hazards/Y sectors first”).
- Make explicit **hosted / mirrored / linked / interpreted** boundaries for those domains.
- Decide on **baseline endorsement logic** at least for 1–2 flagship topics:
  - what minimum metadata and uncertainty notes are required,
  - how often updates are expected,
  - what is the process when new evidence conflicts with existing baselines.

### 2.3 Evidence-pack layer

Evidence base:
- Strong synthesis; see 1.3.

Weak / under-specified areas:
- There are no finalized **short evidence packs** specifically designed for:
  - Director-level progress reporting,
  - late‑April workshop materials.
- Validation status is not clearly labeled:
  - which statements are “safe to treat as settled,”
  - which are explicitly “for testing” in upcoming engagements.

---

## 3. What the late‑April workshop should validate (derived from coverage map)

### 3.1 Product and content (validate direction and ownership, not re-open architecture)

Based on lines 35–38 of the coverage map:
- **Direction**: Use the workshop to test whether stakeholders agree with the proposed NCAIF surface built from:
  - current content gaps (website inventory/matrix/summary),
  - NCAIF structure document,
  - UX evidence base.
- **Ownership**: Validate which parts of the surface:
  - DCCE will actively curate and maintain (e.g., policy-maker front door, area profiles, key measures pages),
  - will remain as catalog entries referencing external systems.
- **Prioritization**: Ask which product changes and surfaces are **most urgent** to show in the 2026 window vs which can wait.

### 3.2 Data and method (validate domain and boundary choices)

From lines 51–54:
- Test a **shortlist of priority domains** (hazard/sector combinations) for Phase 1 implementation.
- For each shortlisted domain, use the workshop to validate proposed **host / link / interpret** boundaries:
  - e.g., “For L&D, CRDB will host metadata and summary statistics, but link out to underlying microdata.”
- Present candidate **baseline endorsement rules** (for 1–2 topics) and ask stakeholders whether:
  - the requirements are realistic,
  - the caveats and uncertainty language are sufficient,
  - any additional conditions are needed before public use.

### 3.3 Governance and operating model (prototype roles and rhythms)

From lines 68–71:
- Bring strawman **role maps** (owner, steward, custodian, reviewer, approver for 1–2 datasets or services) and use breakout discussions to:
  - confirm whether they align with real mandates,
  - identify missing or overloaded roles.
- Present a draft **decision-rights matrix** (data changes, baselines, deprecation, publishing approvals) and ask:
  - “What here would be difficult to implement under current structures?”
  - “What must be escalated vs can stay at working level?”
- Co-design a **governance rhythm**:
  - what a minimal, realistic review cadence looks like,
  - how CRDB governance connects to existing DCCE committees.

### 3.4 Evidence pack and translation (test pack shapes and asks)

From lines 85–87:
- Prepare 2–3 prototype **short evidence packs** (e.g., for policy-maker briefing, for a line agency, for BTR alignment) and ask workshop participants:
  - whether the pack structure helps them make decisions,
  - what’s missing or redundant.
- Mark inside each pack what is **already validated** vs **for testing** and use reactions to refine:
  - which claims can be upgraded to “settled,”
  - which areas clearly need follow-up research or more cautious language.
- Explicitly link each major evidence cluster to a **workshop objective**:
  - “We are showing you this gap matrix because we want you to rank which gaps are most critical for Phase 1.”
  - “We are showing you this use-case cluster because we want you to confirm which ones CRDB should serve now vs later.”

This agenda framing lets you walk Director Toey through:
- what is already defensible to present as “current state,”
- what is weak and needs her decision or guidance,
- and what you propose to validate with a broader stakeholder group in the late‑April workshop, all grounded directly in the current evidence coverage map.