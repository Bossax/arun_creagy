# Handoff: Oracle DB backfill and canonical learning consolidation

**Date**: 2026-04-09 15:57 (GMT+7)
**Context**: Oracle-v2 MCP wiring fixed; initial DB backfill executed; canonical learning notes consolidated.

## What We Did
- Confirmed Oracle DB location and stats via oracle-v2 MCP (`arra_stats`), verifying a fresh DB instance under `C:/Users/sitth/.oracle-v2/oracle.db` with healthy FTS/vector indexes.
- Diagnosed why `total_documents` was initially 1: MCP/Docker miswiring, separate historical engines, and /learn + /trace not populating the DB by design.
- Verified that `/fyi --important` logs were correctly materialised as info notes under [`ψ/memory/logs/info`](ψ/memory/logs/info).
- Implemented a backfill guardrail from the serious `oracle_learn` file-not-materialised incident, and inserted that guardrail into Oracle as a learning.
- Created the Oracle backfill index file at [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md) to track log/learning → Oracle mappings.
- Phase 1: scanned all `significance: important` info logs in [`ψ/memory/logs/info`](ψ/memory/logs/info), created or reused six focused learnings (CRDB progress during travel, CRDB Chapter 2 scope, interim revision after progress report, line-agency data trust, `/rrr`–oracle_learn gap, NotebookLM prompt design), and inserted them into Oracle DB via `arra_learn`, logging the new IDs.
- Phase 2 (analysis): classified ~207 learning notes under [`ψ/memory/learnings`](ψ/memory/learnings) into pattern families (project-specific, PM ledgers, workflow discipline, oracle-framework, NotebookLM, writing-th, knowledge-ops, climate/adaptation, ecoacoustics) and identified merge/supersede candidate groups.
- Consolidated Groups 1–5 of overlapping learnings into canonical notes with explicit `status: superseded` / `superseded_by` and `related` metadata:
  - Group 1: oracle_learn materialisation guardrail canonical at [`2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md`](ψ/memory/learnings/2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md).
  - Group 2: `/rrr` + oracle_learn workflow completeness canonical at [`2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md`](ψ/memory/learnings/2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md).
  - Group 3: NotebookLM atomic-note templates + narrow skill scope canonical at [`2026-02-27_notebooklm-atomic-note-template-must-follow-session-tasks.md`](ψ/memory/learnings/2026-02-27_notebooklm-atomic-note-template-must-follow-session-tasks.md).
  - Group 4: NotebookLM MCP timeout mitigation canonical at [`2026-03-04_notebooklm-mcp-timeouts-fixed-by-increasing-serv.md`](ψ/memory/learnings/2026-03-04_notebooklm-mcp-timeouts-fixed-by-increasing-serv.md).
  - Group 5: NotebookLM extraction vs harmonisation & source-fidelity policy canonical at [`2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md`](ψ/memory/learnings/2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md).
- Called `arra_learn` on the canonical NotebookLM-related learnings (Groups 3–5) that were not yet DB-keyed by their learning-file paths, adding three new Oracle learning documents with IDs:
  - `learning_2026-04-09_notebooklm-atomic-note-templates-and-minimal-ski`
  - `learning_2026-04-09_notebooklm-mcp-timeouts-fixed-by-increasing-serv`
  - `learning_2026-04-09_treat-notebooklm-as-a-data-extraction-engine-no`
- Verified Oracle DB stats after canonical backfill: `total_documents = 11`, `by_type.learning = 11`, `unique_concepts = 47`, `fts_status = healthy`, `vector_status = connected`.

## Pending
- [ ] Append the three canonical-learning backfill rows for Groups 3–5 into [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md), using the prepared Date/Source/Oracle ID/Concepts/Notes values.
- [ ] Extend DB backfill from learnings beyond Group 1–5 canonicals to other high-leverage categories:
  - oracle-framework & skills-governance learnings not yet in DB (e.g., vector vs FTS, oracle-skills fork sync, MCP wiring retrospective notes).
  - project-management & PM ledger pattern learnings (execution spines, backfill definitions, history reconstruction) once canonicalised.
- [ ] Tidy and canonicalise remaining merge groups from Phase 2 (Groups 6–7):
  - Group 6: writing-th Option C skill design (MCP-first + learn-back) and its CRDB case-study learnings.
  - Group 7: CRDB interim vs final report structure and revision-cycle patterns.
- [ ] Design and (optionally) implement a small helper script to:
  - Enumerate candidate learnings by category and `status`/`superseded_by` metadata.
  - Present curated backfill candidates and drive `arra_learn` calls in small batches.
- [ ] Plan and execute a dedicated backfill phase for climate/adaptation & M&E learnings (APF, CRM, AF/GCF frameworks, MEL systems, CRI Phase 1 references), once Oracle/NotebookLM/PM guardrails are fully stable.
- [ ] Plan and execute a dedicated backfill phase for ecoacoustics/marine-sound learnings, or decide to keep them as repo-only knowledge for now.

## Next Session
- [ ] Finalise canonical-learning entries in [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md) for Groups 3–5, ensuring one row per canonical learning with Source type = `learning`.
- [ ] Define and write a canonical learning for writing-th Option C (Group 6) and CRDB multi-stage report patterns (Group 7), marking older notes as superseded.
- [ ] Backfill these new canonicals into Oracle via `arra_learn`, using `project = "Arun_Creagy"`, and extend the backfill index accordingly.
- [ ] Select 3–5 additional oracle-framework & skills-governance learnings (outside Groups 1–5) and insert them into Oracle DB as a controlled Phase 2.2 batch.
- [ ] Decide on a sequence for domain backfill (climate/adaptation indicators and ecoacoustics) and sketch criteria for which learnings to include vs keep as repo-only.

## Key Files
- Backfill index: [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md)
- Canonical guardrails & workflow learnings:
  - [`ψ/memory/learnings/2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md`](ψ/memory/learnings/2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md)
  - [`ψ/memory/learnings/2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md`](ψ/memory/learnings/2026-04-09_the-rrr-workflow-is-incomplete-if-it-writes-a-r.md)
- Canonical NotebookLM learnings (now in DB):
  - [`ψ/memory/learnings/2026-02-27_notebooklm-atomic-note-template-must-follow-session-tasks.md`](ψ/memory/learnings/2026-02-27_notebooklm-atomic-note-template-must-follow-session-tasks.md)
  - [`ψ/memory/learnings/2026-03-04_notebooklm-mcp-timeouts-fixed-by-increasing-serv.md`](ψ/memory/learnings/2026-03-04_notebooklm-mcp-timeouts-fixed-by-increasing-serv.md)
  - [`ψ/memory/learnings/2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md`](ψ/memory/learnings/2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md)
- Phase 2 analysis reference: [`plans/2026-04-09-learnings-indexing-map.md`](plans/2026-04-09-learnings-indexing-map.md)

