# Plan: Continue updating CRDB PM ledgers (maintenance + execution loop)

**Date**: 2026-03-30 (Asia/Bangkok)

## Goal

Maintain CRDB project state as **artifact-first truth**, using the PM ledgers as canonical navigation + audit surfaces, without introducing a high-agency automation skill.

This plan continues the Option B posture documented in:

- [`ψ/incubate/DCCE/CRDB/CRDB-Project-Manager-Facade-Contract.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Manager-Facade-Contract.md)
- [`plans/2026-03-27-project-management-anchor-implementation-plan.md`](plans/2026-03-27-project-management-anchor-implementation-plan.md)

## PM artifacts in scope (source of truth)

Ledgers:

- [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md`](ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md)

Anchors to keep in sync (navigation + evidence):

- [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md)
- [`ψ/incubate/DCCE/CRDB/Hub.md`](ψ/incubate/DCCE/CRDB/Hub.md)
- [`ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Registry.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Registry.md)
- [`ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Workstreams-Index.md)

## Execution loop (repeatable)

### Step 0 — Choose the “event in scope”

Pick exactly **one** concrete event to process in this pass (examples):

- Sponsor/progress meeting outcome: [`ψ/incubate/DCCE/CRDB/output/2026-03-27_progress-meeting-summary_dir-toey.md`](ψ/incubate/DCCE/CRDB/output/2026-03-27_progress-meeting-summary_dir-toey.md)
- Submission/freeze point already recorded or newly discovered.
- Workshop planning shift (new constraint, logistics deadline, or agenda decision).

**Rule**: one event → one incremental set of ledger updates.

### Step 1 — State sensing (read-only)

Read, in order:

1) [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md) (current priorities + anchors)
2) [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md) (does the event already exist as a trigger?)
3) [`ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md) (which deliverables are impacted?)
4) [`ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md) (is there a freeze/submission implication?)
5) [`ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md) (does this event represent a direction shift?)

Output of this step (internal): a short “state note” listing existing IDs (T-*, D-*, S-*, CH-*, C-*).

### Step 2 — Trigger Log update (T-*)

If the event is not yet present:

- Add **one new row** to [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md).
- Link:
  - the origin/source artifact,
  - evidence IDs via [`ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Registry.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Registry.md),
  - decision anchors (typically [`ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md) and/or meeting decision artifacts).

If the trigger exists:

- Update only **Status** and/or add **Notes**; avoid rewriting history.

### Step 3 — Deliverable Map update (D-*)

For each deliverable impacted by the event:

- Ensure the deliverable exists in [`ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md).
- If it is “Planned” but execution has started, update **Current status** and add the first real artifact link.

**Priority deliverables to materialize next (from retros):**

- D-006 workshop invite + logistics package (v0) (create the actual output artifact under [`ψ/incubate/DCCE/CRDB/output/`](ψ/incubate/DCCE/CRDB/output/)).
- D-001 management evidence pack v1 (draft the pack artifact; keep the trace as a separate audit artifact).

### Step 4 — Claim Register update (C-*)

Add claims only if they are **actually used** in:

- sponsor-facing narrative,
- meeting positioning,
- deliverable packaging.

Rules:

- If a claim meaningfully changes, add a **new C-ID**; don’t silently rewrite.
- Tie claims to triggers and deliverables.

### Step 5 — Submission Log update (S-*)

If the event implies a send/freeze:

- Add a submission/freeze row to [`ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md).
- Ensure it references:
  - the deliverable ID (D-*),
  - trigger(s) (T-*),
  - decision basis,
  - evidence basis.

### Step 6 — Change Log update (CH-*)

Add a change entry when the event represents a true direction shift:

- “what changed / why / what it affects”
- point to the trigger(s), decisions, and deliverables.

### Step 7 — Manual facade “receipt” (operation record)

For the event you processed, produce a short receipt that matches the facade disclosure sections.

- If one already exists, confirm whether it is still current.
- Otherwise create a new receipt under [`ψ/incubate/DCCE/CRDB/output/`](ψ/incubate/DCCE/CRDB/output/).

Reference example receipt:

- [`ψ/incubate/DCCE/CRDB/output/2026-03-27_CRDB-Project-Manager-Facade-Receipt_PM-Dir-Toey.md`](ψ/incubate/DCCE/CRDB/output/2026-03-27_CRDB-Project-Manager-Facade-Receipt_PM-Dir-Toey.md)

## Quality gates (definition of “done” for a ledger-update pass)

1) Every new/updated item has an ID and is linkable (T/D/C/S/CH).
2) At least one of the following is true:
   - a “planned” deliverable gained a real artifact link, or
   - a new trigger was logged, or
   - a new submission/freeze point was recorded.
3) The pass results in **no orphan references** (e.g. a deliverable points to a trigger that doesn’t exist).
4) The update is append-only in spirit: old meaning preserved; changes are captured as new entries or status updates.

## Next planned increment (recommended)

Process the 2026-03-27 Dir Toey meeting outcome as the scope event and **materialize D-006** into a real output artifact (invite inputs + headcounts + venue + agenda split + breakout prompts) anchored to:

- [`ψ/incubate/DCCE/CRDB/output/2026-03-27_progress-meeting-summary_dir-toey.md`](ψ/incubate/DCCE/CRDB/output/2026-03-27_progress-meeting-summary_dir-toey.md)
- T-004 in [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
- D-006 row in [`ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)

