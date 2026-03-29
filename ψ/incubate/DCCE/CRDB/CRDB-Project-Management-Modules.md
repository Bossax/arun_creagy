# CRDB Project Management Modules

## Purpose

This note defines the **initial project-management modules** for the CRDB work cycle, aligned with the architecture plan in [`plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md).

The goal is to make project-management behavior **explicit and artifact-centered**, without introducing hidden orchestration or high-agency automation. Each module describes **what a well-behaved helper may do** when assisting a human.

## Design stance

- Modules are **callable patterns**, not autonomous daemons.
- All behavior is **append-first** and uses existing ledgers as the source of truth.
- Every module must:
  - state its **inputs and outputs**,
  - list the **artifacts it reads**, and
  - list the **artifacts it may propose to write**.
- Write operations should be considered **proposals** unless explicitly confirmed by the human.

The three initial modules are:

1. **State sensing** — build a situational view from ledgers and plan.
2. **Trigger capture** — normalize new triggers into the trigger log and related ledgers.
3. **Deliverable trace** — map a deliverable to its triggers, decisions, evidence, and submissions.

---

## Module 1 — State sensing

### Purpose

Provide a **read-only situational snapshot** of the CRDB project that a human can use to decide what to do next.

### Inputs

- Optional focus hints, such as:
  - time window (e.g. "last 7 days"),
  - focus area (e.g. "governance", "interim report"),
  - deliverable ID (e.g. `D-002`).

### Reads from

- [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md)
- [`CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
- [`CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
- [`CRDB-Claim-Register.md`](ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md)
- [`CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md)
- [`CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md)
- [`CRDB-Evidence-Registry.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Registry.md)
- [`CRDB-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Coverage-Map.md)
- [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md)

### Writes to

- No direct writes.
- May **propose**:
  - new reminder bullets for [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md), and
  - new rows that the human may add to the ledgers above.

### Output shape (conceptual)

- Inferred project state, including:
  - latest triggers and change entries,
  - key open decisions and their evidence basis,
  - deliverables in progress or recently submitted,
  - obvious gaps visible from coverage and claim usage.
- Suggested **next questions or actions**, clearly marked as advice.

This module is the **primary dependency** for any controlled facade that wants to describe "where we are".

---

## Module 2 — Trigger capture

### Purpose

Help the human convert messy project events (notes, emails, meetings, submissions) into **normalized trigger entries** and associated link updates.

### Inputs

- A short description of the event (e.g. "Dir Toey progress meeting", "interim report submission").
- Pointers to raw artifacts (e.g. meeting notes, logs, source files).

### Reads from

- Raw notes and logs in `ψ/memory/logs/info/`, `ψ/incubate/DCCE/CRDB/inbox_source/`, and `ψ/incubate/DCCE/CRDB/inbox_note/`.
- Existing trigger entries in [`CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md) to avoid duplicates.
- Decision and evidence anchors:
  - [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md)
  - [`CRDB-Evidence-Registry.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Registry.md)
  - [`CRDB-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Coverage-Map.md)

### Writes to (proposed)

- New rows for [`CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md).
- Optional updates or clarifications to:
  - [`CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
  - [`CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md)

All write actions must be presented as **draft rows** or edit suggestions, not silently applied changes.

### Output shape (conceptual)

- A proposed trigger entry with:
  - Trigger ID suggestion,
  - normalized fields (date, origin, type, impact zone, urgency),
  - linked evidence and decisions,
  - suggested status and notes.
- Optional **cross-link suggestions** in the deliverable and change logs.

---

## Module 3 — Deliverable trace

### Purpose

Given a specific deliverable, produce a **traceability view** that shows which triggers, decisions, evidence, and submissions it depends on.

### Inputs

- A deliverable identifier, such as:
  - Deliverable ID (e.g. `D-002`), or
  - Direct path to a deliverable artifact.

### Reads from

- [`CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
- [`CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
- [`CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md)
- [`CRDB-Claim-Register.md`](ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md)
- [`CRDB-Evidence-Registry.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Registry.md)
- [`CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md)
- [`phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md)

### Writes to

- No canonical ledgers.
- May **propose** annotations or cross-links for human confirmation.

### Output shape (conceptual)

- A structured trace view that includes:
  - Deliverable metadata (audience, purpose, status),
  - Upstream triggers and change entries,
  - Decisions and claims that underpin the deliverable,
  - Evidence assets used (by ID and artifact path),
  - Submissions and freeze points.

This module is the main building block for future **audit, narrative, and workshop preparation** tasks.

