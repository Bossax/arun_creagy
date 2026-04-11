---
type: plan
status: draft
project:
  - DCCE_CRI
title: CRI PM Ledger Update Plan after v3 Governance Freeze
description: Controlled-facade plan for updating CRI PM ledgers using the CRDB PM logic, adapted to CRI hearing, claim, evidence, and Phase 2 governance work.
---

# CRI PM Ledger Update Plan after v3 Governance Freeze

## Why this plan exists

The CRI PM system already adopts the same **controlled facade + append-first + artifact-centered** logic developed in CRDB, as documented in:

- [`ψ/incubate/DCCE/CRDB/CRDB-Project-Manager-Facade-Contract.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Manager-Facade-Contract.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Project-Management-Modules.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Management-Modules.md)
- [`ψ/incubate/DCCE/CRI/CRI-Project-Manager-Facade-Contract.md`](ψ/incubate/DCCE/CRI/CRI-Project-Manager-Facade-Contract.md)
- [`ψ/incubate/DCCE/CRI/CRI-Project-Management-Modules.md`](ψ/incubate/DCCE/CRI/CRI-Project-Management-Modules.md)

What is missing is not the PM logic itself, but a **ledger refresh** so the current CRI state is visible in the canonical PM surfaces.

The main gap is that the CRI PM ledgers still reflect:

- Hearing-1 and v2/CBI milestones,
- but not the newer **2026-04-10 governance-v3 freeze**, concept-definition hardening, and the move toward indicator vetting.

This note proposes the first, lowest-risk package of ledger updates.

---

## Transferable PM logic from CRDB to apply in CRI

The CRDB → CRI PM logic that should govern updates is:

1. **State is inferred from ledgers, not from prose memory**
   - Use Trigger / Deliverable / Claim / Submission / Change + Evidence as the operational source of truth.

2. **Append-first, artifact-centered**
   - Add fresh rows for meaningful new events.
   - Avoid silent rewriting of historical intent.

3. **Controlled facade, low agency**
   - Propose rows first; human approves before write.
   - Every proposal must say what ledger it targets, why, and what it links to.

4. **Deliverable traceability is mandatory**
   - New methodological states should appear not only as notes/files but as:
     - trigger(s),
     - deliverable(s),
     - claim(s),
     - evidence rows,
     - change summaries,
     - submission/freeze rows if relevant.

5. **Uncertainty must be explicit**
   - If something is not yet formally submitted or not yet linked to a verified evidence row, the ledger should say so explicitly rather than imply completion.

---

## Current CRI ledger state: what is already good

### Strong foundations already present

- Trigger layer exists in [`ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md), including:
  - backfilled conceptual pivots,
  - `T-CRI-001` for Public Hearing 1.
- Deliverable layer exists in [`ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md), including:
  - hearing outputs,
  - v2 capacity-tagging pack as `D-CRI-005`.
- Claim layer exists in [`ψ/incubate/DCCE/CRI/CRI-Claim-Register.md`](ψ/incubate/DCCE/CRI/CRI-Claim-Register.md), with hearing-derived methodological claims.
- Submission layer exists in [`ψ/incubate/DCCE/CRI/CRI-Submission-Log.md`](ψ/incubate/DCCE/CRI/CRI-Submission-Log.md), although it is still effectively placeholder-only.
- Change layer exists in [`ψ/incubate/DCCE/CRI/CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md), covering the major pivots up to the v2/CBI phase.

### Main PM visibility gap

The ledgers do **not yet fully encode** the new v3 governance state represented by:

- [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md)
- [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Concept_Summary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Concept_Summary_v3.md)
- [`ψ/incubate/DCCE/CRI/inbox_source/Urban_Resilience_Concept_Check.md`](ψ/incubate/DCCE/CRI/inbox_source/Urban_Resilience_Concept_Check.md)
- [`ψ/inbox/handoff/2026-04-10_15-10_cri-v3-structure-locked.md`](ψ/inbox/handoff/2026-04-10_15-10_cri-v3-structure-locked.md)

This creates a mismatch between the actual working baseline and the PM surfaces.

---

## Proposed first update package: exact ledgers to update

### 1. Trigger Log
Target: [`ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md)

**Add 1 new trigger row first**

#### Proposed row type
- **New trigger** for the 2026-04-10 governance-v3 freeze.

#### Draft intent
- A trigger capturing that CRI Phase 2 governance framing was frozen around the **Institutional Readiness** lens, with 6 functional pillars and a transition from v2/CBI bridge work into v3 concept hardening + indicator-vetting preparation.

#### Why this comes first
- It gives every downstream update a stable “why did this change?” anchor.

#### Suggested linkage
- Evidence:
  - [`ψ/inbox/handoff/2026-04-10_15-10_cri-v3-structure-locked.md`](ψ/inbox/handoff/2026-04-10_15-10_cri-v3-structure-locked.md)
  - [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md)
  - [`ψ/incubate/DCCE/CRI/inbox_source/Urban_Resilience_Concept_Check.md`](ψ/incubate/DCCE/CRI/inbox_source/Urban_Resilience_Concept_Check.md)
- Deliverables:
  - new v3 dictionary deliverable row
  - new concept-summary deliverable row

---

### 2. Deliverable Map
Target: [`ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)

**Add 2 new deliverable rows**

#### Proposed row type A
- Deliverable for [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md)

#### Proposed purpose
- Canonical v3 governance worksheet and definition anchor for Phase 2 indicator vetting.

#### Proposed row type B
- Deliverable for [`ψ/incubate/DCCE/CRI/output/CRI_Capacity_Concept_Summary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Concept_Summary_v3.md)

#### Proposed purpose
- Compact operational concept map used to bridge literature-backed definitions to indicator-vetting work.

#### Why these are needed
- Right now the deliverable map stops at the v2 pack (`D-CRI-005`), which makes the current working baseline invisible.

---

### 3. Claim Register
Target: [`ψ/incubate/DCCE/CRI/CRI-Claim-Register.md`](ψ/incubate/DCCE/CRI/CRI-Claim-Register.md)

**Add 2–3 new claims, not many**

#### Proposed claim family
1. Governance in Phase 2 should be represented through the **Institutional Readiness** lens rather than value-based good-governance framing.
2. The six governance pillars (Planning, Finance, Coordination, Service Delivery, Data, HR) are the canonical functional decomposition for v3 indicator vetting.
3. Some emergent concepts (e.g. Asset Mobilization Velocity, Distributed Command Agility, Transboundary Feedbacks, Digital Social Mediation) remain **adjacency / placeholder concepts** until stronger evidence is added.

#### Why this matters
- The claim layer is where reusable, quotable project stances should live.
- At the moment, the claim register reflects Hearing-1 methodology stances, but not the newer v3 governance freeze.

---

### 4. Evidence Registry
Target: [`ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md)

**Add 3 new evidence rows first**

#### Proposed row types
1. `CRI_Capacity_Tagging_Dictionary_v3.md` as a Phase 2 methodology/output artifact.
2. `Urban_Resilience_Concept_Check.md` as a concept-definition evidence surface.
3. `CRI_Capacity_Concept_Summary_v3.md` as an operational summary / synthesis artifact.

#### Why these evidence rows matter
- Without registry entries, the new v3 work cannot be cleanly referenced from claims, change log, or coverage map.

---

### 5. Change Log
Target: [`ψ/incubate/DCCE/CRI/CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md)

**Add 1 new change row**

#### Proposed row type
- Narrative change entry summarising the 2026-04-10 shift from the v2/CBI bridge as working pack to the v3 governance freeze as the new canonical governance lens for Phase 2 indicator vetting.

#### Why this is important
- The change log should explain the turning point in plain language, while the trigger log records the event and the deliverable map records the artifacts.

---

### 6. Submission Log
Target: [`ψ/incubate/DCCE/CRI/CRI-Submission-Log.md`](ψ/incubate/DCCE/CRI/CRI-Submission-Log.md)

**Do not force a new row unless a real freeze/submission exists**

#### Controlled recommendation
- Keep the explicit uncertainty pattern already present unless you can verify that:
  - the v3 dictionary was sent externally, or
  - a real internal freeze point was declared.

This follows the CRI facade contract’s uncertainty rule.

---

### 7. Plan / navigation surface
Targets:

- [`ψ/incubate/DCCE/CRI/plan.md`](ψ/incubate/DCCE/CRI/plan.md)
- optionally [`ψ/incubate/DCCE/CRI/output/CRI_management_surfaces_consolidation.md`](ψ/incubate/DCCE/CRI/output/CRI_management_surfaces_consolidation.md)

**Small prose updates only**

#### Proposed update in `plan.md`
- Add the v3 dictionary and concept-summary outputs to the current execution focus under Track B / current governance work.
- Reframe the near-term priority from only “v2 + CBI bridge” to “v2 bridge + v3 governance freeze + first indicator-vetting pass”.

#### Proposed update in `CRI_management_surfaces_consolidation.md`
- Clarify that the PM ledgers are now active management surfaces alongside plan / hub / methodologies / evidence.

---

## Recommended execution order

1. **Evidence Registry** — make the new artifacts visible.
2. **Trigger Log** — log the v3 governance-freeze trigger.
3. **Deliverable Map** — map the new v3 artifacts as deliverables.
4. **Claim Register** — formalize reusable governance-v3 claims.
5. **Change Log** — narrate the turning point.
6. **Plan / management-surface notes** — align navigation and current focus.
7. **Submission Log** — only if a real freeze/submission can be verified.

This order mirrors the CRDB PM logic: evidence and trigger first, then deliverable/claim/change linkage.

---

## Human decisions required before implementation

These decisions should be made explicitly before writing ledger rows:

1. **Trigger granularity**
   - Should the 2026-04-10 work be logged as:
     - one trigger for the full v3 governance freeze, or
     - two triggers: structure freeze and concept hardening / NotebookLM extraction completion?

2. **Deliverable identity**
   - Should [`CRI_Capacity_Concept_Summary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Concept_Summary_v3.md) be treated as:
     - a standalone deliverable, or
     - a companion artifact under the same deliverable family as [`CRI_Capacity_Tagging_Dictionary_v3.md`](ψ/incubate/DCCE/CRI/output/CRI_Capacity_Tagging_Dictionary_v3.md)?

3. **Claim strength**
   - Should the v3 governance-lens claims be registered as:
     - `Draft`, because they are internally frozen but not yet externally tested, or
     - `Active`, because they are now the working contract for indicator vetting?

4. **Submission/freeze status**
   - Was there a real internal freeze point on 2026-04-10 for the v3 dictionary, or should the submission log remain explicitly unverified?

5. **Plan framing**
   - Should `plan.md` continue to show **v2 + CBI bridge** as the dominant current focus, or should it now elevate **v3 governance freeze + indicator vetting prep** as the top active Phase 2 track?

---

## Minimal proposed write package for the next implementation pass

If you want a low-risk first implementation, the smallest coherent package is:

- 3 evidence rows
- 1 trigger row
- 2 deliverable rows
- 1 change-log row
- 1 short `plan.md` prose update

This gives CRI a coherent PM refresh without yet forcing claim proliferation or fake submission certainty.

After that, a second pass can add:

- 2–3 new claims,
- the first indicator-vetting evidence rows,
- and any verified submission/freeze entries.

---

## My read

The CRI PM architecture already contains the CRDB logic you want. The real task is now **state synchronization**: the ledgers must catch up with the actual project baseline established by the v3 governance freeze and concept-hardening work. The safest path is to update the evidence / trigger / deliverable / change surfaces first, then layer claims and first-pass indicator vetting once you confirm the human decisions above.
