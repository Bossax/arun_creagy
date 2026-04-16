# Learning: Define “backfill complete” + keep PM maintenance event-scoped

## Context

While operating the CRDB project-management ecosystem, the phrase “backfill the ledgers” was ambiguous. Trigger/Deliverable/Submission had already been reconstructed, but the user intended “backfill” to include **all** PM ledgers (Claim Register and Change Log too). This mismatch created unnecessary back-and-forth.

## Learning

1) **Define “backfill complete” explicitly as a checklist**

For an artifact-first PM ecosystem, backfill should be treated as complete only when the following are true:

- [`ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Trigger-Log.md) is chronologically readable and linked to evidence/decisions.
- [`ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md`](ψ/incubate/DCCE/CRDB/CRDB-Deliverable-Map.md) covers all high-leverage deliverables and links to triggers and anchors.
- [`ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md) includes external submissions **and** internal freeze/cutoff points.
- [`ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md`](ψ/incubate/DCCE/CRDB/CRDB-Claim-Register.md) captures the reusable, actually-used claims that justify decisions and sponsor narrative.
- [`ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Change-Log.md) captures major direction shifts in plain language.

If only some ledgers are backfilled, label it as “spine backfilled” (Trigger/Deliverable/Submission) rather than “ledgers backfilled.”

2) **Keep maintenance event-scoped**

Instead of trying to backfill and operate everything at once, pick one concrete event and run a full pass:

- state sensing → update T/D/C/S/CH as needed → create/refresh one executable deliverable artifact.

This keeps the system legible and prevents accidental scope creep into high-agency automation.

3) **Preserve uncertainty explicitly**

When a historical entry lacks transmission proof (email/cover note), log it as “submitted-by-claim” rather than inventing certainty.

## Why it matters

This prevents semantic drift in the system’s operating language and preserves trust: the ledger set is not “done” until all ledgers that create narrative coherence (claims/changes) are also present.

*Added via Oracle Learn*

