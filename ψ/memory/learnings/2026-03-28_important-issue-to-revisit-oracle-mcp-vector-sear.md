# Important issue to revisit — Oracle MCP vector search (Chroma) unavailable

**Date**: 2026-03-28 (Asia/Bangkok)

## Problem

Oracle MCP reports **vector search unavailable** (ChromaDB down), so `oracle_search()` falls back to **FTS-only** (keyword search).

Observed signals:

- `oracle_stats()` shows `chroma_status: unavailable` while `fts_status: healthy`.
- Warning mentions inability to open `c:/tmp/oracle-chroma-debug.log` (Chroma init/log path issue).

## Impact

- **Semantic / fuzzy retrieval** is reduced.
- All Oracle documents remain usable and searchable by **full-text**.

## Operational guidance (until fixed)

1) Treat FTS as baseline guarantee; do not design skills that depend on semantic search.
2) Use strong naming + tags (e.g., `writing-th`, `thai-report`, `crdb`) to keep retrieval reliable.
3) Revisit Oracle Chroma configuration / debug-log path and restore vector backend when possible.

## References

- Guardrail note about `oracle_learn()` file materialization inconsistencies:
  - [`ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md`](ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md)


---
*Added via Oracle Learn*
