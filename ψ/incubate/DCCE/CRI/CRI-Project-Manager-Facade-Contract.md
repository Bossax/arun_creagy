# CRI Project-Manager Facade — Contract (Controlled facade)

## Purpose

Define a **dry-run-only project-manager facade** for CRI that:

- exposes how the CRI project-management modules are used,
- surfaces inferred state for the human, with emphasis on hearings, claims, and evidence,
- recommends low-risk actions and ledger updates, and
- never performs high-agency changes without explicit confirmation.

This contract follows the **controlled facade** posture used in CRDB, but is tuned to CRI’s hearing workflow and evidence backbone.

## Non-goals

The CRI facade is explicitly **not**:

- a singleton autonomous manager or coordinator of hearings,
- an opaque orchestrator of background tasks,
- a replacement for human judgment (especially on claims and positions),
- a direct writer to ledgers without human review.

## Operating posture

The facade acts as a **transparent dispatcher and advisor** that:

1. Reads the current state via the **state sensing** module.
2. Optionally prepares **trigger capture**, **deliverable trace**, **claim–evidence linkage**, or **submission/change recording** suggestions.
3. Presents a **human-readable report** that includes:
   - inferred state,
   - modules used or recommended,
   - artifacts read,
   - artifacts it proposes to write,
   - decisions it leaves to the human.
4. Waits for explicit human direction before any write.

All behavior must be explainable in terms of the ledgers and modules defined in:

- [`CRI-Project-Management-Modules.md`](ψ/incubate/DCCE/CRI/CRI-Project-Management-Modules.md)
- [`CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md)
- [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md)
- [`CRI-Claim-Register.md`](ψ/incubate/DCCE/CRI/CRI-Claim-Register.md)
- [`CRI-Submission-Log.md`](ψ/incubate/DCCE/CRI/CRI-Submission-Log.md)
- [`CRI-Change-Log.md`](ψ/incubate/DCCE/CRI/CRI-Change-Log.md)
- [`CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md)
- [`CRI-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Coverage-Map.md)

## Contract: inputs

The facade accepts a **request** that may include:

- high-level intent (e.g. "where are we on Public Hearing 1?", "prepare CRI management evidence pack outline"),
- optional focus (time window, workstream, hearing ID, deliverable ID, claim or evidence ID),
- risk tolerance (e.g. "orientation only", "draft ledger suggestions allowed").

## Contract: outputs

The facade returns a **facade report** that must include the following sections.

### 1. Inferred state

A short summary of CRI project context, derived exclusively from:

- the five CRI project-management ledgers,
- evidence and coverage anchors,
- any future CRI plan/navigation file (used as context, not as a ledger).

Typical content:

- recent hearing-related activity and upcoming milestones,
- state of key claims and their evidence coverage,
- status of important deliverables and any known submissions,
- gaps or inconsistencies visible from the ledgers.

### 2. Modules invoked or recommended

- A list of modules actually used (e.g. state sensing, deliverable trace, claim–evidence linkage).
- A list of modules that are recommended for follow-up (e.g. trigger capture, submission/change recording) but not yet invoked.

### 3. Artifacts read

An explicit list of artifacts consulted while generating the report, grouped by type, for example:

- triggers and changes,
- claims and deliverables,
- evidence and coverage,
- submissions and freezes.

### 4. Proposed artifacts to write or update

- A list of **concrete proposals**, such as:
  - new trigger log rows,
  - new deliverable map rows,
  - new or updated claim–evidence links,
  - new submission or change-log entries,
  - suggested notes or reminders in a plan/navigation file.
- Each proposal must specify:
  - which ledger it targets,
  - a draft row or edit description,
  - the rationale (linking back to evidence, claims, triggers, or decisions).

No proposal is applied automatically. The facade has **no commit authority**.

### 5. Decisions left to the human

An explicit checklist of decisions that remain with the human, for example:

- whether to accept, modify, or reject each proposed ledger row,
- whether to create a new deliverable or reuse an existing one,
- whether to formalize a hearing outcome as a claim or keep it as background context,
- whether to treat an event as a formal submission or an informal exchange,
- whether to widen or tighten the scope of project-management automation.

## Guardrails

To preserve the controlled-facade boundaries and CRI’s low-agency stance:

1. **No hidden orchestration**
   - All module calls and data sources must be listed in the facade report.
   - The facade cannot trigger side effects in other systems (e.g. email, file sync, external CRI platforms).

2. **No autonomous high-agency changes**
   - The facade cannot directly modify markdown files.
   - Any code or skill implementation must route write-intent through an explicit human confirmation step.

3. **Mandatory uncertainty disclosure**
   - Whenever a conclusion depends on incomplete or ambiguous ledger data, the report must say so.
   - The facade must distinguish between **observed facts** (from ledgers) and **inferences or guesses**.
   - For submissions in particular, the facade must be explicit when "no verified freeze/submission has yet been identified" and avoid upgrading that to implied certainty.

4. **Append-only traceability**
   - All accepted changes arising from facade proposals must be captured as **fresh rows** in the relevant ledgers, not silent edits to existing entries.
   - Where a correction is needed, the recommended pattern is:
     - append a new change-log row describing the correction, and
     - if a ledger row is edited, keep enough context in the change log to reconstruct intent.

5. **Receipts for operations**
   - When the human approves a proposed change, the implementing agent should emit a short **operation receipt** that includes:
     - what was changed,
     - which proposal it came from,
     - where it was written (file and section).
   - Receipts should be linkable from future change-log entries.

## Minimal interface sketch

This contract is intentionally **documentation-only** at this stage. A future skill or script that follows it might expose callable operations such as:

- cri_project_manager.state_sense(request)
- cri_project_manager.trace_deliverable(request)
- cri_project_manager.link_claims_and_evidence(request)
- cri_project_manager.propose_trigger_entries(request)
- cri_project_manager.propose_submission_and_change_entries(request)

Any such implementation must:

- use the CRI ledgers in this folder as the **source of truth**,
- conform to the guardrails above,
- keep behavior **CRI-first and artifact-centered**, and
- respect the low-agency, append-first design that underpins the CRI project.

