---
title: ---
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-04-09_guardrail-after-every-oraclelearn-call-immedi.md
---

# ---

---
title: Guardrail: After every oracle_learn() call, immediately verify materialisation
tags: [oracle, oracle_learn, guardrail, durable-capture, workflow-integrity]
created: 2026-04-09
source: fyi: ψ/memory/logs/info/2026-03-27_16-01_oracle-learn-file-not-materialized-serious.md
---

# Guardrail: After every oracle_learn() call, immediately verify materialisation

## Guardrail

- After every `oracle_learn()` call, treat the returned `file` / `source_file` path as a **claim**, then immediately verify that the file exists on disk.
- If the file is missing (read returns `ENOENT`), treat this as a **serious workflow integrity failure** because it breaks durable capture and creates false confidence in non-existent artifacts.
- On missing file: immediately materialize the referenced learning file at the exact path with the learning content, commit it, and log the incident as a reliability issue.

## Rationale

This guardrail prevents Oracle DB/index entries from becoming "invisible" when the MCP server reports success but does not materialize the backing markdown file in the repo. In this hybrid Windows + Docker + Git Bash environment, we must assume that `oracle_learn` updates Oracle's internal memory but may fail to create a Git-visible file unless we explicitly enforce this check-and-create discipline.

## Provenance

This consolidated guardrail is informed by earlier anomaly and guardrail notes:

- [`2026-03-27_guardrail-after-every-oraclelearn-call-treat.md`](ψ/memory/learnings/2026-03-27_guardrail-after-every-oraclelearn-call-treat.md)
- [`2026-03-27_oracle-learn-file-materialization-guardrail.md`](ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md)
- [`2026-04-07_oracle-learn-file-sync-anomaly.md`](ψ/memory/learnings/2026-04-07_oracle-learn-file-sync-anomaly.md)


---
*Added via Oracle Learn*
