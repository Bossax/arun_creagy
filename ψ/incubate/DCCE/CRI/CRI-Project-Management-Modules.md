# CRI Project Management Modules

## Purpose

This note defines the **initial project-management modules** for the CRI work cycle, modeled on the CRDB architecture but adapted to **CRI’s hearing-centric, claim/evidence-heavy workflow**.

The goal is to make CRI project-management behavior **explicit and artifact-centered**, without introducing hidden orchestration or high-agency automation. Each module describes **what a well-behaved helper may do** when assisting a human.

## Design stance

- Modules are **callable patterns**, not autonomous daemons.
- All behavior is **append-first** and uses existing CRI ledgers as the source of truth.
- Every module must:
  - state its **inputs and outputs**,
  - list the **artifacts it reads**, and
  - list the **artifacts it may propose to write**.
- Write operations should be considered **proposals** unless explicitly confirmed by the human.

The initial CRI modules are:

1. **State sensing** — build a situational view from CRI ledgers and plan.
2. **Trigger capture** — normalize new CRI events into the trigger log and related ledgers.
3. **Deliverable trace** — map a CRI deliverable to its triggers, claims, evidence, and submissions.
4. **Claim–evidence linkage** — help maintain explicit, auditable linkage between CRI claims and their evidence base.
5. **Submission and change recording** — support disciplined logging of freezes, submissions, and post-submission changes.

These modules are intentionally **small and composable** so that future skills or scripts can call them without expanding their agency.

---

## Shared CRI artifacts

Unless otherwise stated, modules operate over the following CRI anchors:

- [`CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md)
- [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)
- [`CRI-Claim-Register.md`](ψ/incubate/DCCE/CRI/CRI-Claim-Register.md)
- [`CRI-Submission-Log.md`](ψ/incubate/DCCE/CRI/CRI-Submission-Log.md)
- [`CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md)
- [`CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md)
- [`CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md)

If a CRI plan or navigation note is later introduced (e.g. `ψ/incubate/DCCE/CRI/plan.md`), modules may treat it as **advisory context**, not as a canonical ledger.

---

## Module 1 — State sensing

### Purpose

Provide a **read-only situational snapshot** of the CRI project that a human can use to decide what to do next, with emphasis on:

- status of hearings and related events,
- current claim and evidence coverage,
- known submissions and freezes,
- visible gaps or inconsistencies.

### Inputs

- Optional focus hints, such as:
  - time window (e.g. "last 7 days"),
  - focus area (e.g. "Public Hearing 1", "governance claims"),
  - deliverable ID (e.g. `CRI-D-001`),
  - claim or evidence ID (e.g. `C-CRI-012`, `E-CRI-045`).

### Reads from

- [`CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md)
- [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)
- [`CRI-Claim-Register.md`](ψ/incubate/DCCE/CRI/CRI-Claim-Register.md)
- [`CRI-Submission-Log.md`](ψ/incubate/DCCE/CRI/CRI-Submission-Log.md)
- [`CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md)
- [`CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md)
- [`CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md)

### Writes to

- No direct writes.
- May **propose**:
  - new reminder bullets for a future CRI plan or navigation note,
  - new rows that the human may add to the ledgers above (e.g. missing change-log entries, missing claim–evidence links).

### Output shape (conceptual)

- Inferred project state, including:
  - latest hearing-related triggers and change entries,
  - key open claims and their evidence basis,
  - deliverables in progress or recently touched,
  - obvious gaps visible from coverage and claim usage,
  - submissions identified so far and any noted absence of verified freezes.
- Suggested **next questions or actions**, clearly marked as advice (e.g. "confirm whether PH1 briefing deck was formally submitted", "link claim C-CRI-007 to evidence E-CRI-021").

This module is the **primary dependency** for any controlled CRI facade that wants to describe "where we are".

---

## Module 2 — Trigger capture

### Purpose

Help the human convert messy CRI project events (notes, emails, hearing agendas, chat threads) into **normalized trigger entries** and associated link updates.

### Inputs

- A short description of the event (e.g. "Public Hearing 1 prep meeting", "PH1 evidence pack upload", "verbal instruction from CRI secretariat").
- Pointers to raw artifacts (e.g. meeting notes, slides, email threads, files). These may live in:
  - `ψ/incubate/DCCE/CRI/inbox_note/`,
  - `ψ/incubate/DCCE/CRI/inbox_source/`,
  - relevant `ψ/memory/` logs.

### Reads from

- Raw notes and logs in the CRI inbox folders and related memory locations.
- Existing trigger entries in [`CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md) to avoid duplicates and mis-ordered events.
- Downstream anchors to understand impact:
  - [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)
  - [`CRI-Claim-Register.md`](ψ/incubate/DCCE/CRI/CRI-Claim-Register.md)
  - [`CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md)

### Writes to (proposed)

- New rows for [`CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md).
- Optional updates or clarifications to:
  - [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)
  - [`CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md)

All write actions must be presented as **draft rows** or edit suggestions, not silently applied changes.

### Output shape (conceptual)

- A proposed trigger entry with:
  - Trigger ID suggestion,
  - normalized fields (date, origin, type, relation to hearing or submission, impact zone, urgency),
  - linked deliverables, claims, and evidence where possible,
  - suggested status and notes.
- Optional **cross-link suggestions** in the deliverable and change logs (e.g. "link PH1_trigger_03 to CRI-D-001").

---

## Module 3 — Deliverable trace

### Purpose

Given a specific CRI deliverable (e.g. briefing decks, evidence summaries, hearing scripts), produce a **traceability view** that shows which triggers, claims, evidence, and submissions it depends on.

### Inputs

- A deliverable identifier, such as:
  - Deliverable ID from [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md), or
  - Direct path to a deliverable artifact.

### Reads from

- [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)
- [`CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md)
- [`CRI-Submission-Log.md`](ψ/incubate/DCCE/CRI/CRI-Submission-Log.md)
- [`CRI-Claim-Register.md`](ψ/incubate/DCCE/CRI/CRI-Claim-Register.md)
- [`CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md)
- [`CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md)
- [`CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md)

### Writes to

- No canonical ledgers.
- May **propose** annotations or cross-links for human confirmation (e.g. adding missing claim IDs or evidence references in the deliverable map).

### Output shape (conceptual)

- A structured trace view that includes:
  - Deliverable metadata (audience, purpose, hearing association, status),
  - Upstream triggers and change entries,
  - Claims that the deliverable advances or depends on,
  - Evidence assets used (by ID and artifact path),
  - Submissions and freeze points, including cases where "not yet frozen" is explicit.

This module is a building block for **audit, narrative, and hearing preparation** tasks in the CRI context.

---

## Module 4 — Claim–evidence linkage

### Purpose

Support **disciplined linkage between CRI claims and the evidence base**, using the evidence registry and coverage map as the backbone.

### Inputs

- One or more claim identifiers (e.g. `C-CRI-00X`).
- Optional focus:
  - specific hearing or deliverable,
  - thematic area (e.g. "risk governance", "public participation").

### Reads from

- [`CRI-Claim-Register.md`](ψ/incubate/DCCE/CRI/CRI-Claim-Register.md)
- [`CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md)
- [`CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md)
- [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)

### Writes to (proposed)

- Suggested updates to [`CRI-Claim-Register.md`](ψ/incubate/DCCE/CRI/CRI-Claim-Register.md) to:
  - add or refine evidence references,
  - clarify claim scope or status.
- Suggested updates to [`CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md) where coverage gaps or mis-alignments are detected.

All suggestions must:

- be explicitly marked as **proposed edits**,
- carry a short rationale (e.g. "evidence E-CRI-023 directly supports premise 2 of C-CRI-007").

### Output shape (conceptual)

- For each claim in scope:
  - current linked evidence assets and their roles,
  - inferred coverage or gaps from the coverage map,
  - proposed claim or coverage-map edits,
  - questions for the human where linkage is ambiguous.

This module helps keep CRI’s **claim spine aligned with its evidence spine**.

---

## Module 5 — Submission and change recording

### Purpose

Help the human record **submissions, freezes, and subsequent changes** in a way that is explicit, append-only, and aligned with how CRI actually interacts with counterparties and formal processes.

### Inputs

- A short description of the submission or change event (e.g. "PH1 deck emailed to CRI", "post-hearing revision of slide 12").
- Pointers to relevant artifacts (e.g. file paths, email headers, meeting notes).
- Optional link to related triggers or deliverables.

### Reads from

- [`CRI-Submission-Log.md`](ψ/incubate/DCCE/CRI/CRI-Submission-Log.md)
- [`CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md)
- [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)
- [`CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md)

### Writes to (proposed)

- New rows for [`CRI-Submission-Log.md`](ψ/incubate/DCCE/CRI/CRI-Submission-Log.md), including explicit representation of "no verified submission" where that is the current state.
- New rows for [`CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md) describing post-submission edits or corrections.

All proposed rows must:

- be clearly labelled as **draft**,
- describe how submission/change status was inferred,
- reference any related triggers and deliverables.

### Output shape (conceptual)

- Draft submission and/or change-log entries,
- A brief narrative explaining the sequence (e.g. "PH1 deck prepared under triggers T-CRI-001/002, no verified submission yet; this module proposes a placeholder submission-log entry that keeps that uncertainty explicit"),
- Optional suggestions to backfill earlier events if gaps are detected.

This module ensures that CRI’s **formal interactions and document evolution** are captured in an **append-only, auditable trail**.

