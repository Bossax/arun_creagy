---
type: learning
created: 2026-03-10
tags:
  - migration
  - knowledge-ops
  - provenance
  - nothing-is-deleted
---

# Knowledge migration playbook (repeatable refactors)

## Invariants
- No silent overwrites (use collision-safe naming).
- Every move is logged.
- Verification gates before deleting legacy folders.

## Steps (repeatable)
1) Create destination skeleton (hubs, assets dirs).
2) Move sources/notes into inbox triage.
3) Move outputs into incubate.
4) Normalize entrypoints (e.g., `plan.md`, `Hub.md`).
5) Move assets + update links.
6) Archive leftovers and only then remove empty legacy directories.

## Provenance
- Migration log: [`ψ/archive/migration-log.md`](ψ/archive/migration-log.md:1)

