# CRI Submission Log

## Purpose

This ledger records **external submissions and key internal freeze points** for CRI deliverables. It implements the "submission creates a freeze point" rule used in [`ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md`](ψ/incubate/DCCE/CRDB/CRDB-Submission-Log.md), adapted for **DCCE / CRI**.

## Usage and maintenance

- Add one row **per submission or freeze event** related to CRI deliverables.
- Treat the **Submission ID** as the canonical handle when referring to a specific sent or frozen state.
- Prefer sorting the table **by Date (ascending)** for historical reconstruction. Submission IDs may therefore appear out of numeric order if earlier IDs were already referenced elsewhere.
- Use this file together with:
  - [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md) for deliverable context
  - [`CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md) for the trigger that led to submission or revision
  - any CRI change log that will be introduced later in the migration
  - the CRI evidence registry [`output/CRI-Evidence-Registry.md`](ψ/incubate/DCCE/CRI/CRI-Evidence-Registry.md) for evidence traceability

> [!pattern]
> A submission is logged when something **leaves the working folder** (sent to DCCE, stakeholders, or public channels) *or* when the team explicitly declares a **freeze point** for comparison.


## Practical reading order

1. Scan this file to understand **what was submitted when** for CRI.
2. Follow **Deliverable ID** to [`CRI-Deliverable-Map.md`](ψ/incubate/DCCE/CRI/CRI-Deliverable-Map.md).
3. Follow **Trigger(s)** to [`CRI-Trigger-Log.md`](ψ/incubate/DCCE/CRI/CRI-Trigger-Log.md).
4. Use **Decision basis** and **Evidence basis** links for audit and explanation once populated.


## Submission table

> No verified external submission or explicit freeze has yet been identified for Public Hearing 1. Add a row below once a concrete submission or freeze event is evidenced.

| Submission ID | Date | Channel / recipient | Deliverable ID | Submitted artifact | Version label | Trigger(s) | Decision basis | Evidence basis | Notes |
|---|---|---|---|---|---|---|---|---|---|
| S-CRI-001 | (YYYY-MM-DD) | (e.g. DCCE, public hearing participants, internal freeze) | (e.g. D-CRI-0XX) | (path to CRI artifact once mapped) | (e.g. v1 draft, vfinal, snapshot) | (link to T-CRI-### once logged) | (link to CRI decision anchors once created) | (E-CRI-### references from the evidence registry) | Placeholder row illustrating how to log a CRI submission/freeze; replace with a real event when ready. |
