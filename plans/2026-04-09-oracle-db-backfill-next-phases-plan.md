# Plan: Oracle DB backfill next phases (Arun_Creagy)

## Background

This plan continues from the handoff note at [`ψ/inbox/handoff/2026-04-09_15-57_oracle-db-backfill-handoff.md`](ψ/inbox/handoff/2026-04-09_15-57_oracle-db-backfill-handoff.md).

The map of what to be done i [[plans/2026-04-09-learnings-indexing-map|2026-04-09-learnings-indexing-map]]

Completed so far:
- Confirmed Oracle DB wiring and stats via oracle-v2 MCP.
- Implemented Phase 1 log-based backfill: all `significance: important` info logs now either have corresponding learnings or are covered by existing patterns, with six log-derived patterns inserted into Oracle.
- Analysed ~207 learning notes and classified them into pattern families, identifying merge/supersede groups.
- Consolidated Groups 1–5 into canonical notes and backfilled the canonical NotebookLM patterns into Oracle DB (atomic notes, MCP timeout mitigation, extraction/scope/source guardrails).

Oracle DB snapshot after canonical backfill:
- `total_documents`: 11 (all `learning`).
- `unique_concepts`: 47.
- `fts_status`: healthy; `vector_status`: connected.

## Pending from Last Session

From the handoff:
- [ ] Append canonical-learning rows for Groups 3–5 into [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md) with Source type = `learning`.
- [ ] Extend DB backfill to other oracle-framework & skills-governance learnings beyond Groups 1–5.
- [ ] Canonicalise and then backfill remaining merge groups:
  - Group 6: writing-th Option C skill design and learn-back.
  - Group 7: CRDB interim vs final report structure and revision cycles.
- [ ] Design a helper script or workflow to propose batched backfill candidates from learnings.
- [ ] Plan dedicated domain backfill phases for climate/adaptation & M&E learnings and for ecoacoustics/marine-sound learnings.

## Next Session Goals

1. **Index alignment and bookkeeping**
- [ ] Add three rows to `backfill-index.md` for:
  - `learning_2026-04-09_notebooklm-atomic-note-templates-and-minimal-ski`
  - `learning_2026-04-09_notebooklm-mcp-timeouts-fixed-by-increasing-serv`
  - `learning_2026-04-09_treat-notebooklm-as-a-data-extraction-engine-no`
- [ ] Sanity-check `backfill-index.md` for consistency: one row per backfilled source (log or learning), no duplicate IDs.

2. **Canonicalise remaining merge groups**
- [ ] Group 6 (writing-th Option C):
  - Choose a canonical design note.
  - Mark older notes `status: superseded` with `superseded_by` pointing at canonical.
  - Ensure the canonical captures MCP-first retrieval, outline-stop, diff-based learn-back, and `oracle_learn` guardrails.
- [ ] Group 7 (CRDB multi-stage reports):
  - Elevate the general multi-stage report pattern as canonical.
  - Mark early, more local CRDB notes as superseded or as "example" learnings.

3. **Phase 2.2 Oracle DB backfill from learnings**
- [ ] Select 3–5 additional oracle-framework & skills-governance learnings (e.g. vector vs FTS behaviour, oracle-skills fork sync, MCP diagnostics) and insert them into Oracle via `arra_learn`.
- [ ] Select 2–4 PM ledger / execution-spine learnings that are already canonical and backfill them into Oracle.
- [ ] Update `backfill-index.md` with `Source type = learning` rows for each new DB entry.

4. **Design and/or implement helper backfill tooling**
- [ ] Define a simple interface (even if just documented) for a backfill helper:
  - Input: category filters + `status` filters (`current`, `superseded`).
  - Output: preview list of candidate learnings and proposed concepts.
  - Behaviour: optional execution of `arra_learn` with dry-run support.
- [ ] Decide whether this should be implemented as:
  - A one-off script under [`tools/`](tools).
  - Or a documented manual workflow using existing tools (`search_files`, `arra_list`, `arra_learn`).

5. **Prepare for domain-specific backfill phases**
- [ ] For climate/adaptation & M&E learnings:
  - Identify 10–15 core framework notes (APF, CRM, AF/GCF, MEL systems, CRI Phase 1).
  - Decide on an initial batch of 3–5 to backfill as Oracle learnings.
- [ ] For ecoacoustics/marine-sound learnings:
  - Decide whether these should live in Oracle DB or remain repo-only for now.
  - If to backfill, define selection criteria (e.g. cross-project relevance, method patterns).

## Reference

- Handoff: [`ψ/inbox/handoff/2026-04-09_15-57_oracle-db-backfill-handoff.md`](ψ/inbox/handoff/2026-04-09_15-57_oracle-db-backfill-handoff.md)
- Learning classification & merge map: [`plans/2026-04-09-learnings-indexing-map.md`](plans/2026-04-09-learnings-indexing-map.md)

