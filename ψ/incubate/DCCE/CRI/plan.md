# plan — DCCE / CRI

## Scope guard
This plan is for **DCCE / CRI only**.

- **In-scope:** CRI Phase 1 (Impact / Fiscal Relief) + CRI Phase 2 (SES pivot; capacity profiles via administrative data tagging).
- **Out-of-scope:** CRDB and other project streams (unless explicitly listed as a dependency below).

## Purpose
Operational plan for CRI: what we are producing, what we depend on, and what to do next.

This plan is **not** a standalone task tracker. It works together with the CRI project-management ledgers, which are the canonical, append-first surfaces for triggers, deliverables, claims, submissions, and changes.

### Project management anchors (CRI canonical ledgers)
For day-to-day management and history, use these ledgers as the primary control surfaces. When tasks, decisions, or scope changes occur, record them by appending new rows to the relevant ledger rather than editing past entries in this plan.

- Trigger Log (why something started or changed): [CRI-Trigger-Log.md](CRI-Trigger-Log.md)
- Deliverable Map (what exists / must exist): [CRI-Deliverable-Map.md](CRI-Deliverable-Map.md)
- Claim Register (what we are asserting): [CRI-Claim-Register.md](CRI-Claim-Register.md)
- Submission Log (what we sent to whom, when): [CRI-Submission-Log.md](CRI-Submission-Log.md)
- Change Log (what we changed and why): [CRI-Change-Log.md](CRI-Change-Log.md)

## Key outputs (deliverables)
1) **Impact Index (Phase 1):** “Fiscal Relief” + Human Impact composite, with explicit data lineage and gap flags.
   - Anchor: [CRI Phase 1 Methodology.md](CRI Phase 1 Methodology.md)
2) **Capacity multi-scores + profiles (Phase 2):** multi-scores by **capacity type** (e.g., Coping / Adaptive / Transformative), communicated profile-first (SES + management science).
   - No single composite resilience score.
   - Within each capacity type, indicators should be structured as **asset vs process** via the tagging dictionary.
   - Anchor: [CRI Phase 2 Methodology.md](CRI Phase 2 Methodology.md)
   - Dictionary: [CRI_Capacity_Tagging_Dictionary.md](CRI_Capacity_Tagging_Dictionary.md)
3) **Gap diagnostics + confidence overlay:** “0 vs missing” treatment for impact data + “data richness/confidence (0–3)” for capacity proxies.
   - Anchor: [output/CRI-Evidence-Registry.md](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md) and [output/CRI-Evidence-Coverage-Map.md](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md)
4) **Consultation storyline & visuals:** profile-first communication; avoid “ranking trap”.
   - Anchor: [CRI_Urban_Resilience_Frameworks_Analysis.md](CRI_Urban_Resilience_Frameworks_Analysis.md)

5) **Scoring harmonization note (Phase 2):** rules for harmonizing mixed indicator types (binary / ordinal / counts / ratios), missingness handling, and cross-pillar consistency.
   - Anchor: [`output/2026-05-01_harmonizing-mixed-indicators_scoring-note.md`](output/2026-05-01_harmonizing-mixed-indicators_scoring-note.md)

### Evidence governance for key outputs

- All key outputs above must be backed by entries in [`output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md).
- The strength and distribution of evidence across dimensions (impact, capacity, SES, governance, data_richness, etc.) should be reflected in [`output/CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md).
- Decisions in this section should be traceable via **E-CRI-###** identifiers shared between the plan, the registry, and the coverage map.

## Dependencies (inputs we must have or confirm)
### Data dependencies
- **DDPM**: deaths + affected series for Human Impact pillar (Phase 1).
- **Fiscal relief / emergency support (Phase 1 economic pillar proxy):** use the **best available proxy for all sectors**, not agriculture-only.
	- **Central emergency funds (เงินทดรองราชการ)** may be the better cross-sector proxy even if incomplete.
	- **OAE** agricultural relief payments remain a useful partial stream (esp. agriculture), but should not be treated as the only numerator by default.
- **NESDC**: GPP denominator (explicitly document whether total vs sectoral; note known bias when only total GPP is available).
- **DOPA**: official population registration (Tabien Baan) totals for constrained redistribution.
- **Global / spatial**: WorldPop, ESA WorldCover, hazard masks (GISTDA) for redistribution and gap-flagging.

### Method dependencies
- **Constrained Redistribution** (non-negotiable): global data used to disaggregate, totals constrained to official stats.
  - Anchor: [[ψ/incubate/DCCE/CRI/output/CRI Phase 1 Methodology|CRI Phase 1 Methodology]]
- **Two-speed measurement stance**: baseline administrative proxies now; target process-quality metrics later.
  - Anchor: [[ψ/incubate/DCCE/CRI/output/CRI Phase 2 Methodology|CRI Phase 2 Methodology]]

## Working baseline (what is already “locked”)
Based on current CRI docs, treat these as the default baseline unless we explicitly revise them:

- Economic pillar is framed as **Fiscal Relief Index**, not total loss.
- “0” in relief/loss series may mean **missing / no report**, so we must apply an **Administrative Gap** flag cross-checked against hazard exposure.
- Urban/industrial “blind spot” requires **exposure proxies** (commercial/industrial land use, industrial GPP) rather than agricultural relief.
- Capacity outputs should be **multi-scores by capacity type + profiles + gap report + confidence overlay**, not a single composite resilience score.
  - Indicators structured as **asset vs process** (via the tagging dictionary).

## Triage (where the working materials now live)
- Source intake (local project inbox for CRI): [inbox_source/](inbox_source/)
- Inbox note (local scratchpad / guidance note for this project): [inbox_note/](inbox_note/)

## Current execution focus (as of 2026-04-22)

- **Experimental Track: WorldPop-Driven Dasymetric Disaggregation**
  - **Context**: Discovery of high-resolution (100m) WorldPop datasets triggered a rethink of the disaggregation pipeline.
  - **Objective**: Brainstorm and test hypotheses for disaggregating 3 core pillars:
    1.  **Casualties**: Deaths and affected people (Pillar 1).
    2.  **GPP**: Provincial economic output (Pillar 3).
    3.  **Financial Relief**: Emergency funds as a proxy for Loss & Damage (Pillar 4).
  - **Status**: **Active Experimentation.** No changes to the production pipeline have been committed. 
  - Active Hypotheses:
    - **Model C Hybrid**: Testing if $W = Pop \times Empirical$ corrects urban risk bias.
  - Evidence linkage: [E-CRI-024 to E-CRI-029](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md).


- **Capacity tagging v2 + CBI bridge (Track B)**
  - Working pack:
    - v3 governance worksheet: [output/CRI_Capacity_Tagging_Dictionary_v3.md](output/CRI_Capacity_Tagging_Dictionary_v3.md)
  - Priorities:
    - Validate Pillar 1 experimental outputs vs empirical ground truth.
    - Brainstorm disaggregation logic for Pillar 2 (Buildings) using WorldPop structural metrics.

## Immediate priorities (next 1–2 weeks)


1) **Finalize Phase 1 data lineage + denominators**
   - Confirm numerator definition(s) for fiscal relief using the **best proxy for all sectors** (central emergency funds may be preferred even if incomplete), and note exclusions.
   - Confirm denominator choice (total GPP vs sectoral) and document bias/mitigation.
   - Incorporate **new DDPM impact and fiscal relief Excel extracts**:
     - Current: review structure and fields in the raw Excel files received from DDPM (impact series and fiscal relief streams), noting column meanings, codes, and any anomalies.
     - Next (planned 2026-04-09): tabulate the DDPM Excel files into standard intake tables (e.g. province × year, with clear IDs and units) as part of Stage 1 inventory / ingest, so they can flow into the Phase 1 pipeline in [output/2026-04-02_cri-phase1-data-pipeline-plan.md](output/2026-04-02_cri-phase1-data-pipeline-plan.md).
   - Anchor: [CRI Phase 1 Methodology.md](CRI Phase 1 Methodology.md)

3) **Capacity tagging: lock v1 of the dictionary + scoring approach**
   - Validate the Coping/Adaptive/Transformative crosswalk + indicator inclusion rules.
   - Confirm the **multi-score approach** (scores by capacity type) and avoid collapsing into a single composite score.
   - Ensure indicators can be grouped as **asset vs process** consistently.
   - Define confidence/data-richness scoring consistently (0–3).
   - Anchor: [CRI_Capacity_Tagging_Dictionary.md](CRI_Capacity_Tagging_Dictionary.md)
   - Scoring harmonization reference: [`output/2026-05-01_harmonizing-mixed-indicators_scoring-note.md`](output/2026-05-01_harmonizing-mixed-indicators_scoring-note.md)

4) **Prototype the Phase 2 “profile-first” product**
   - One sample province: produce a capacity radar/profile + gap diagnostics + confidence overlay.
   - Use the “profiling over ranking” pattern (avoid ranking trap).
   - Anchor: [CRI Phase 2 Methodology.md](CRI Phase 2 Methodology.md)

5) **Consultation storyline (March workshop readiness)**
   - Prepare 3 core messages:
     - Fiscal Relief ≠ Total Loss
     - “0” may be missing ⇒ Administrative Gap
     - Capacity profiles drive action better than a single rank
   - Anchor: [output/CRI_Phase2_Public_Hearing1_decisions_and_signals.md](output/CRI_Phase2_Public_Hearing1_decisions_and_signals.md)

## Open confirmations (capture in this plan)
- Confirm the final naming: “Fiscal Relief Index” vs alternative phrasing in Thai/English.
- Confirm output contract for Phase 2: **multi-scores by capacity type** (with asset/process structure via tagging), with no requirement to collapse into a single composite number.
- Confirm baseline year range for Phase 1 impact calculations and treatment of missing years.

## Risks & mitigations (quick list)
- **Misinterpretation risk (Fiscal vs Loss):** mitigate via explicit definitions + visuals.
- **Binary proxy over-claiming (LPA-style indicators):** mitigate via confidence overlay + two-speed framing.
- **Data gaps (0 vs missing):** mitigate via hazard cross-check + explicit administrative gap flag.
