---
title: ---
tags: [oracle-db, backfill, canonicalisation, workflow, indexing-map, mcp, rrr]
created: 2026-04-15
source: ψ/memory/learnings/2026-04-11_rrr_oracle-db-backfill-phase2.2-and-groups1-7.md
---

# ---

---
type: learning
date: 2026-04-11
concepts:
  - oracle-db
  - backfill
  - canonicalisation
  - workflow
  - indexing-map
  - mcp
  - rrr
---

# Oracle DB backfill – phase 2.2 and groups 1–7

## Scope

This learning captures how the oracle-DB backfill was executed for:

- Phase 2.2 canonical learnings (oracle-framework & skills governance, PM ledgers & execution spine).
- The seven merge/supersede learning groups defined in [`plans/2026-04-09-learnings-indexing-map.md`](plans/2026-04-09-learnings-indexing-map.md), consolidated into group canonicals and backfilled into Oracle DB.

## Stable Patterns

1. **Canonical-before-DB** – Treat Oracle DB as a projection of canonical patterns, not a mirror of every micro-learning. Use an indexing map to define groups and proposed primaries, then write one canonical note per group that explains scope, member files, and stable patterns.
2. **Filesystem → Index → DB pipeline** – The backfill pipeline has three layers:
   - Canonical notes in [`ψ/memory/learnings`](ψ/memory/learnings).
   - A tabular log in [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md) that records date, source type, canonical path, Oracle ID, concepts, and notes.
   - Oracle DB learning records created via arra_learn.
3. **Use structural templates** – Reuse a strong canonical template (like the group 6–7 canonicalisation note) for other groups: frontmatter, scope, source artefacts, stable patterns vs one-offs, open questions, and relationship to Oracle DB backfill.
4. **Table edits via helper tooling** – For large Markdown tables, use the markdown-table-edit skill and replace-md-table helper script to avoid fragile manual edits.
5. **MCP as the default DB integration path** – In this repo, Oracle DB should be written via the Oracle MCP tool (arra_learn), not via ad hoc HTTP calls, to stay consistent with family tooling and reduce configuration drift.

## One-off Decisions

- Groups 6 and 7 share a single joint canonical note (`2026-04-11_oracle-db-backfill-group6-7-canonicalisation.md`) rather than separate canonicals, because they are tightly coupled in practice (writing_th Option C design and multi‑stage report structure/revision patterns).
- The filenames for the new group canonicals and the rrr learning note are anchored to the backfill date (2026-04-11) to make this wave easy to identify historically.

## Relationship to Oracle DB backfill

This learning should be treated as a meta-pattern for future backfill waves:

- Start by identifying merge/supersede groups where the learning corpus is dense.
- Write or confirm canonical notes for each group.
- Append rows to the backfill index for those canonicals.
- Use the configured Oracle MCP tool to create DB entries, then update the index with the returned IDs.

Future waves (for example, climate-topic learnings or other tooling categories) can reuse this same pipeline.


---
*Added via Oracle Learn*
