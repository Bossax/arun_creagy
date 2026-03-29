# CRDB Project-Manager Facade — Contract (Option B: Controlled facade)

## Purpose

Define a **dry-run-only project-manager facade** for CRDB that:

- exposes how project-management modules are used,
- surfaces inferred state for the human,
- recommends low-risk actions, and
- never performs high-agency changes without explicit confirmation.

This contract implements **Option B — Controlled facade** from [`plans/2026-03-27-project-management-anchor-implementation-plan.md`](plans/2026-03-27-project-management-anchor-implementation-plan.md).

## Non-goals

The facade is explicitly **not**:

- a singleton autonomous manager,
- an opaque orchestrator of background tasks,
- a replacement for human judgment,
- a direct writer to ledgers without human review.

## Operating posture

The facade acts as a **transparent dispatcher and advisor** that:

1. Reads the current state via the **state sensing** module.
2. Optionally prepares **trigger capture** or **deliverable trace** suggestions.
3. Presents a **human-readable report** that includes:
   - inferred state,
   - modules used or recommended,
   - artifacts read,
   - artifacts it proposes to write,
   - decisions it leaves to the human.
4. Waits for explicit human direction before any write.

All behavior must be explainable in terms of the ledgers and modules defined in:

- [`CRDB-Project-Management-Modules.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Management-Modules.md)
- [`CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
- [`CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
- [`CRDB-Claim-Register.md`](ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md)
- [`CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md)
- [`CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md)

## Contract: inputs

The facade accepts a **request** that may include:

- high-level intent (e.g. "where are we", "prepare management evidence pack outline"),
- optional focus (time window, workstream, deliverable ID),
- risk tolerance (e.g. "orientation only", "draft suggestions allowed").

## Contract: outputs

The facade returns a **facade report** that must include the following sections.

### 1. Inferred state

A short summary of project context, derived exclusively from:

- [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md)
- the five project-management ledgers
- evidence and decision anchors.

### 2. Modules invoked or recommended

- A list of modules actually used (e.g. state sensing, deliverable trace).
- A list of modules that are recommended for follow-up (e.g. trigger capture) but not yet invoked.

### 3. Artifacts read

An explicit list of artifacts consulted while generating the report, grouped by type, for example:

- plan and navigation
- triggers and changes
- decisions
- evidence and coverage
- deliverables and submissions.

### 4. Proposed artifacts to write or update

- A list of **concrete proposals**, such as:
  - new trigger log rows,
  - new deliverable map rows,
  - new submission log entries,
  - suggested edits or reminders for `plan.md`.
- Each proposal must specify:
  - which ledger it targets,
  - a draft row or edit description,
  - the rationale (linking back to evidence and decisions).

No proposal is applied automatically. The facade has **no commit authority**.

### 5. Decisions left to the human

An explicit checklist of decisions that remain with the human, for example:

- whether to accept or modify each proposed ledger row,
- whether to create a new deliverable or reuse an existing one,
- whether to schedule a workshop or meeting based on identified gaps,
- whether to widen the scope of project-management automation.

## Guardrails

To preserve Option B boundaries:

1. **No hidden orchestration**
   - All module calls and data sources must be listed in the facade report.
   - The facade cannot trigger side effects in other systems.

2. **No autonomous high-agency changes**
   - The facade cannot directly modify markdown files.
   - Any code or skill implementation must route write-intent through an explicit human confirmation step.

3. **Mandatory disclosure**
   - Every response must include the five disclosure sections above.
   - If some information cannot be obtained, the report must say why.

4. **Receipts for operations**
   - When the human approves a proposed change, the implementing agent must emit a short **operation receipt** that includes:
     - what was changed,
     - which proposal it came from,
     - where it was written (file and section).
   - Receipts should be linkable from future change-log entries.

## Minimal interface sketch

This contract is intentionally **documentation-only** at this stage. A future skill or script that follows it might expose callable operations such as:

- project-manager.state_sense(request)
- project-manager.trace_deliverable(request)
- project-manager.propose_trigger_entries(request)

Any such implementation must:

- use the ledgers in this folder as the **source of truth**,
- conform to the guardrails above, and
- keep behavior **CRDB-first and artifact-centered**.

