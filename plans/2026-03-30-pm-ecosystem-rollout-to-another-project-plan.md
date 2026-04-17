# Plan: Roll out the PM ecosystem to another project (artifact-first, Option B)

**Date**: 2026-03-30 (Asia/Bangkok)

## Goal

Implement the same project-management ecosystem used in CRDB (canonical ledgers + explicit module specs + controlled, low-agency facade posture) for a **different project** without introducing high-agency automation.

This plan treats the CRDB implementation as the reference pattern and reuses its constraints.

## Reference pattern (CRDB)

CRDB’s PM ecosystem artifacts (reference only):

- [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md`](ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md)

CRDB module spec + facade posture:

- [`ψ/incubate/DCCE/CRDB/CRDB-Project-Management-Modules.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Management-Modules.md)
- [`ψ/incubate/DCCE/CRDB/CRDB-Project-Manager-Facade-Contract.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Manager-Facade-Contract.md)

CRDB’s “keep it live” maintenance loop:

- [`plans/2026-03-30-crdb-pm-ledger-update-plan.md`](plans/2026-03-30-crdb-pm-ledger-update-plan.md)

## Scope

This rollout plan creates:

1) The **five canonical ledgers** for the target project
2) A minimal **module spec** note (state sensing / trigger capture / deliverable trace)
3) A **low-agency facade contract** (documentation-only) to enforce disclosure boundaries
4) Wiring from the target project’s navigation surfaces (`Hub.md` and `plan.md`)
5) One **pilot event** processed end-to-end to prove the system works (manual, read-only first; writes only with explicit intent)

## Step-by-step implementation

### Step 1 — Select the target project folder

Target projects should live under `ψ/incubate/<ORG>/<PROJECT>/` with:

- [`ψ/incubate/<ORG>/<PROJECT>/Hub.md`](ψ/incubate/DCCE/CRDB/archive/Hub.md) *(structure reference)*
- [`ψ/incubate/<ORG>/<PROJECT>/plan.md`](ψ/incubate/DCCE/CRDB/plan.md) *(structure reference)*

Implementation note: the PM ecosystem is **project-local**. Do not attempt to create a global “one manager for everything.”

### Step 2 — Create the five ledgers (copy schemas, reset contents)

Create these files in the target project folder, copying only the structure (purpose, usage rules, table headers), not CRDB’s content:

- `<PROJECT>-Trigger-Log.md` (or `Trigger-Log.md` if project already namespaces at folder level)
- `<PROJECT>-Deliverable-Map.md`
- `<PROJECT>-Claim-Register.md`
- `<PROJECT>-Submission-Log.md`
- `<PROJECT>-Change-Log.md`

Rules:

- Append-only posture (“Nothing is Deleted”).
- Use stable IDs per ledger (T-*, D-*, C-*, S-*, CH-*).
- Keep “evidence basis” and “decision basis” columns if the project needs traceability.

### Step 3 — Add module spec (explicit behaviors)

Create a target-project version of the module spec patterned after:

- [`ψ/incubate/DCCE/CRDB/CRDB-Project-Management-Modules.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Management-Modules.md)

Keep it small:

- state sensing (read-only)
- trigger capture (proposal + human review)
- deliverable trace (from trigger/evidence/decision → deliverable → submission/freeze)

### Step 4 — Add a controlled facade contract (documentation-only)

Create a target-project facade contract patterned after:

- [`ψ/incubate/DCCE/CRDB/CRDB-Project-Manager-Facade-Contract.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Manager-Facade-Contract.md)

Hard boundaries to keep:

- disclose inferred state, modules invoked/recommended, artifacts read, proposed writes, and decisions left to human
- no direct ledger writes without explicit confirmation
- no hidden orchestration

### Step 5 — Wire navigation surfaces

Update the target project’s:

- `Hub.md` (add a “Project Management / Ledgers” section with links)
- `plan.md` (add a short “PM anchors” block + how to use them)

This is critical: the ecosystem fails if the user cannot find it quickly.

### Step 6 — Run one pilot event (prove it works)

Choose one real “event in scope” (meeting, submission, new external instruction, sponsor decision).

Run the maintenance loop (manual):

1) state sensing (read-only)
2) create/confirm one trigger row
3) ensure impacted deliverable row exists
4) create a small “receipt” (operation record) under the target project’s `output/` folder

CRDB example receipts/traces (for pattern reference only):

- [`ψ/incubate/DCCE/CRDB/output/2026-03-27_CRDB-Project-Manager-Facade-Receipt_PM-Dir-Toey.md`](ψ/incubate/DCCE/CRDB/output/2026-03-27_CRDB-Project-Manager-Facade-Receipt_PM-Dir-Toey.md)
- [`ψ/incubate/DCCE/CRDB/output/2026-03-27_CRDB-Deliverable-Trace_D-001-Management-Evidence-Pack-v1.md`](ψ/incubate/DCCE/CRDB/output/2026-03-27_CRDB-Deliverable-Trace_D-001-Management-Evidence-Pack-v1.md)

## Definition of done (rollout)

The PM ecosystem is considered “implemented” for the new project when:

1) The five ledgers exist with correct schemas
2) Module spec + facade contract exist (documentation-only is acceptable)
3) Hub + plan link to the ledgers
4) One pilot event has been processed and resulted in:
   - at least one new trigger row, and
   - at least one deliverable row, and
   - one receipt/trace artifact under `output/`

## Immediate next move

Reuse the event-scoped discipline from [`plans/2026-03-30-crdb-pm-ledger-update-plan.md`](plans/2026-03-30-crdb-pm-ledger-update-plan.md): implement the ledgers first, then run one pilot event, and only then consider any automation.

