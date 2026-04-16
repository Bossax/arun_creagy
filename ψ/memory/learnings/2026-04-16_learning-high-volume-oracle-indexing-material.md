---
title: # Learning: High-Volume Oracle Indexing & Materialization Guardrails
tags: [knowledge-ops, oracle-v2, batch-indexing, materialization, agentic-delegation, provenance]
created: 2026-04-16
source: rrr: REPO
---

# # Learning: High-Volume Oracle Indexing & Materialization Guardrails

# Learning: High-Volume Oracle Indexing & Materialization Guardrails

## Context
During a knowledge reclamation session, I needed to index ~140 legacy learning files into the Oracle database. The session revealed critical behavior in the `arra_learn` tool and the most stable pattern for batch ingestion.

## Patterns & Lessons

1. **The Materialization Law**:
   - `arra_learn` is designed to materialize new, canonical disk records for every entry indexed.
   - When registering *existing* local files, this results in duplicates (e.g., `2026-02-09_topic.md` and a new `2026-04-15_materialized_topic.md`).
   - **Fix**: Adopt a "Sync Signature" (`*Added via Oracle Learn*`). Before indexing a file, check for this signature. After indexing, append it immediately to the original file to prevent redundant materialization loops.

2. **Agentic Batch Ingestion (Date-Scoped)**:
   - Attempting to index 100+ files in a single main-agent pass causes context bloat and increases failure risk.
   - **Stable Strategy**: Group unindexed files by their date-prefixes (YYYY-MM-DD). Delegate each date-group to a specialized `generalist` sub-agent.
   - This keeps the main session history lean and allows sub-agents to focus on surgical registration and verification.

3. **Sub-agent Timeout Management**:
   - Even date-scoped tasks can hit the 10-minute timeout for high-volume dates (e.g., Mar 10, 2026).
   - **Operational Rule**: If a sub-agent times out, the main agent must identify exactly which files were missed and either manually complete the set or launch a narrower sub-task.

4. **The Parity Check**:
   - Always run `arra_stats()` at the start of a session to verify DB-filesystem parity. An empty database despite populated disk folders is a high-priority trigger for a sync pass.

## Implementation Guardrail
Before running `arra_learn` on a batch:
1. List all target files.
2. Filter for those *not* containing `*Added via Oracle Learn*`.
3. Launch sub-agents with specific date-scoped prompts.
4. Append signature to originals upon successful materialization verification.

## Tags
`#knowledge-ops` `#oracle-v2` `#batch-indexing` `#materialization` `#agentic-delegation` `#provenance`

---
*Added via Oracle Learn*
