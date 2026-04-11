---
title: Guardrail: verify oracle_learn materializes a repo-local file (create-if-missing)
tags: [oracle, oracle_learn, guardrail, db-filesystem-mismatch, workflow-discipline]
created: 2026-03-27
source: Session debugging (Arun_Creagy)
status: superseded
superseded_by: 2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md
---

> This learning has been superseded by [`2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md`](ψ/memory/learnings/2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md); kept here for historical context and debugging detail.

# Guardrail: verify oracle_learn materializes a repo-local file (create-if-missing)

## Pattern

After every `oracle_learn()` call, treat the returned `source_file` path as a claim, then **verify** the file exists on disk.

If a read returns `ENOENT`, immediately **create** the repo-local markdown file at that exact path with the learning content, then re-read to confirm.

## Why

This prevents Oracle DB/index entries from becoming “invisible” when the MCP server reports success but does not materialize the file in the repo (DB↔disk mismatch).

