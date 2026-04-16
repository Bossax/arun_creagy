---
title: # Learning — CDM review via decision-capture loop
tags: [cdm, decision-capture, attribution, loss-damage, data-modeling]
created: 2026-04-15
source: C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\memory\learnings\2026-02-25_crdb-cdm-review-decisions.md
---

# # Learning — CDM review via decision-capture loop

# Learning — CDM review via decision-capture loop

When refining a Conceptual Data Model (CDM), accuracy improves if the workflow is explicitly staged:

1. **Inventory**: Extract every relationship from the ERD into a normalized list.
2. **Flag**: Create a summary table (cardinality + verb phrase + interpretation) and flag ambiguous semantics.
3. **Decide**: Convert flagged items into a markdown-native decision log with clearly articulated options and inline comment slots.
4. **Apply**: Update ERD + entity definitions only after decisions are captured.
5. **Rationale**: Add a short “reasons behind decisions” section to prevent future re-litigation.

This session also reinforced a modeling principle for climate-risk systems:
- **Attribution should be loss-driven**: keep attribution summaries attached to `LOSS_DAMAGE_RECORD` rather than linking events/drivers directly, to avoid encoding speculative causal claims without impact evidence.


---
*Added via Oracle Learn*
