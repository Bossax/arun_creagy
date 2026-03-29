# Plan: CRDB Project-Management Ecosystem Test Session (Option B Facade)

## Background
We implemented the CRDB project-management ecosystem according to:
- Architecture: [`plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md)
- Implementation anchor: [`plans/2026-03-27-project-management-anchor-implementation-plan.md`](plans/2026-03-27-project-management-anchor-implementation-plan.md)

The ecosystem now includes:
- Five canonical ledgers under CRDB output:
  - [`ψ/incubate/DCCE/CRDB/output/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md)
  - [`ψ/incubate/DCCE/CRDB/output/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md)
  - [`ψ/incubate/DCCE/CRDB/output/CRDB-Claim-Register.md`](ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md)
  - [`ψ/incubate/DCCE/CRDB/output/CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md)
  - [`ψ/incubate/DCCE/CRDB/output/CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md)
- A project-management modules spec:
  - [`ψ/incubate/DCCE/CRDB/output/CRDB-Project-Management-Modules.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Management-Modules.md)
- A controlled `project-manager` facade contract:
  - [`ψ/incubate/DCCE/CRDB/output/CRDB-Project-Manager-Facade-Contract.md`](ψ/incubate/DCCE/CRDB/CRDB-Project-Manager-Facade-Contract.md)

This plan defines the next session, which is focused on *testing* this ecosystem in practice without yet adding new automation.

## Pending from Handoff
From [`ψ/inbox/handoff/2026-03-27_13-12_crdb-project-management-ecosystem-test-session.md`](ψ/inbox/handoff/2026-03-27_13-12_crdb-project-management-ecosystem-test-session.md):
- [ ] Backfill additional high-impact triggers, deliverables, claims, submissions, and changes.
- [ ] Align ID and naming conventions if we want cross-project reuse.
- [ ] Choose the first governance deliverable to fully trace.
- [ ] Decide how much of the facade behavior should be implemented as a skill vs kept as a checklist.

## Next Session Goals
- [ ] Stress-test the ledgers by walking one concrete governance or progress event end-to-end through Trigger Log, Claim Register, Deliverable Map, Submission Log, and Change Log.
- [ ] Produce at least one fully traced deliverable entry (including upstream triggers, decisions, claims, evidence, and submissions) and verify that the trace is readable to a human who did not attend the meeting.
- [ ] Perform a manual "project-manager" run using the facade contract, producing a written operation receipt that can serve as a template for future automation.
- [ ] Decide and record the next incremental step: deeper backfill, section-trace template + first traced section, or a read-only state-sensing helper.

## Proposed Session Flow
1. **Warm-up orientation (10–15 min)**
   - Run [`/recap`](tools/recap_diag.ts) to confirm repo status.
   - Re-open the architecture and implementation anchor plans plus the new ledgers.

2. **Select a test event and deliverable (10–15 min)**
   - From CRDB notes and progress documents, agree on one concrete event (e.g. the 2026-03-24 progress meeting or a specific governance decision).
   - Pick a closely related deliverable (e.g. management evidence pack v1 or a governance role-mapping note).

3. **Ledger population + trace (30–40 min)**
   - Update Trigger Log with any missing triggers for the chosen event.
   - Update Deliverable Map, Claim Register, Submission Log, and Change Log to reflect the chosen deliverable and its upstream/downstream links.
   - Check that IDs and links are consistent and that the story reads coherently when starting from any ledger.

4. **Manual facade exercise (20–30 min)**
   - Follow the `project-manager` facade contract manually:
     - infer state from ledgers,
     - list modules used or recommended (state sensing, trigger capture, deliverable trace),
     - list artifacts read,
     - propose any new writes,
     - explicitly list decisions left to the human.
   - Capture this as a short markdown "operation receipt" (file path to be decided in-session) to serve as a reference example.

5. **Wrap + decision on next increment (10–15 min)**
   - Evaluate whether the ecosystem felt usable and non-fragile.
   - Decide whether to prioritize:
     - richer backfill,
     - a section-trace template and one traced section,
     - or a read-only helper (e.g. a small script) implementing the state-sensing module.

## Reference
- Handoff: [`ψ/inbox/handoff/2026-03-27_13-12_crdb-project-management-ecosystem-test-session.md`](ψ/inbox/handoff/2026-03-27_13-12_crdb-project-management-ecosystem-test-session.md)
- Architecture plan: [`plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md`](plans/2026-03-27-crdb-oracle-project-work-cycle-architecture-plan.md)
- Implementation anchor plan: [`plans/2026-03-27-project-management-anchor-implementation-plan.md`](plans/2026-03-27-project-management-anchor-implementation-plan.md)
- Retro: [`ψ/memory/retrospectives/2026-03/27/13.09_project-management-ecosystem-facade.md`](ψ/memory/retrospectives/2026-03/27/13.09_project-management-ecosystem-facade.md)
- Learning: [`ψ/memory/learnings/2026-03-27_project-management-ecosystem-facade.md`](ψ/memory/learnings/2026-03-27_project-management-ecosystem-facade.md)

