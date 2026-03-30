# Plan: Update WMO–NFCS project after consultation meeting (2026-03-27)

## Background
This project’s PM surfaces were bootstrapped and artifacts were migrated into the CRDB-style intake folder. Next step is to make the project “current” by processing the latest consultation meeting (Fri 2026-03-27) into the canonical ledgers and at least one executable output artifact.

## Pending from Last Session
- Replace separate risk registry by incorporating risks into canonical ledgers (done).
- Update the project based on the 27 Mar consultation meeting outcomes.

## Next Session Goals
1) Produce a single **consultation outcome anchor artifact** under `ψ/incubate/WMO-NFCS/output/`.
2) Update the canonical ledgers so the consultation is ledger-addressable.
3) Update `Hub.md`/`plan.md` “current status” to reflect reality post-consultation.

## Execution plan (event-scoped)

### Step 0 — Identify the consultation inputs
Work only from the migrated intake folder:
- [`ψ/incubate/WMO-NFCS/inbox_source/`](ψ/incubate/WMO-NFCS/inbox_source/)

Expected consultation notes include:
- `2026-03-27-WMO-NFCS-consultation-workshop-*`

### Step 1 — Create a consolidated outcome anchor
Create: `ψ/incubate/WMO-NFCS/output/2026-03-27_WMO-NFCS-Consultation-Workshop-Output_v0.md`

Content schema:
- What happened (agenda + participants + context)
- What was validated / contested
- Decisions / agreements (if any)
- Action items (who/what/when)
- Implications for deliverables D-001..D-004

### Step 2 — Update ledgers
- Trigger: add/refresh the consultation trigger row in [`ψ/incubate/WMO-NFCS/WMO-NFCS-Trigger-Log.md`](ψ/incubate/WMO-NFCS/WMO-NFCS-Trigger-Log.md)
- Deliverables: update consultation deliverable status in [`ψ/incubate/WMO-NFCS/WMO-NFCS-Deliverable-Map.md`](ψ/incubate/WMO-NFCS/WMO-NFCS-Deliverable-Map.md)
- Claims: add stable claims/constraints implied by consultation into [`ψ/incubate/WMO-NFCS/WMO-NFCS-Claim-Register.md`](ψ/incubate/WMO-NFCS/WMO-NFCS-Claim-Register.md)
- Submission log: add only if something was formally sent/frozen.
- Change log: add only if the consultation caused a direction shift.

### Step 3 — Update entrypoints
- Update [`ψ/incubate/WMO-NFCS/plan.md`](ψ/incubate/WMO-NFCS/plan.md) “Current status” and “Next working session” section.

## Reference
- Handoff: [`ψ/inbox/handoff/2026-03-30_13-30_wmo-nfcs-project-setup_wrap-and-consultation-update.md`](ψ/inbox/handoff/2026-03-30_13-30_wmo-nfcs-project-setup_wrap-and-consultation-update.md)

