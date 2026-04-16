---
title: # Learning — CRI v2 capacity tagging, CBI crosswalk, and subtask discipline
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-04-08_cri-capacity-v2-cbi-crosswalk-subtasking.md
---

# # Learning — CRI v2 capacity tagging, CBI crosswalk, and subtask discipline

# Learning — CRI v2 capacity tagging, CBI crosswalk, and subtask discipline

**Date**: 2026-04-08  
**Project**: DCCE_CRI  
**Tags**: cri, capacity_tagging, cbi, notebooklm, workflow, subtasking

## Pattern

When integrating complex analytical workflows (like CRI Phase 2 capacity tagging with a CBI crosswalk) into a repo, treating the entire workflow as a single “implementation task” hides structure and increases confusion. Track-level plans (B1–B8) need to be mirrored by actual execution units (Code subtasks) that map to conceptual blocks:

- B1–B3: freeze external extraction and design local artifacts/schemas;  
- B4–B5: populate the canonical v2 dictionary from v1.1 + NotebookLM synthesis;  
- B6–B7: build the CBI crosswalk and CBI-integrated variant;  
- B8: wire everything into the evidence spine.

Subtasks should be sized so that each one can be described cleanly and completed in one focused pass, without mixing concerns (e.g. not doing evidence wiring while still arguing about mapping types).

## What happened

- Initially, Track B was drafted as a single Code subtask covering B1–B8. This made it unclear when “execute the plan” was meaningfully done, and led to the human rightly pushing back (“what’s the point of subtasks then?”).
- The workflow was then restructured so that:
  - B1 was handled by updating the NotebookLM execution packet to freeze extraction at M1/F1/A1.
  - B2–B3 became one Code pass: create v2 artifacts and schemas.
  - B4–B5 became another: populate v2 from v1.1 + NotebookLM clusters.
  - B6–B7 became a third: implement the CBI crosswalk and CBI-integrated v2 variant.
- Within B6–B7, the CBI crosswalk was deliberately kept partial but pattern-complete (mapping types, confidence scores, and notes), and the CBI-integrated dictionary variant carried those mappings forward in a concept-first view.

## Why it matters

- **For the human**: Clear subtask boundaries make it easier to decide when to pause, review, or redirect. A plan that lives only on paper but is implemented as a single opaque “do everything” block undermines trust and control.
- **For the repo**: Each subtask now leaves a coherent artifact set behind (schema-only, v2-populated, crosswalk+variant, evidence-wired) that can be understood independently in git history and retrospectives.
- **For AI orchestration**: It reinforces the discipline that high-level plans (B1–B8) are not just commentary but must directly shape how tools are used (new_task boundaries, apply_patch scopes, etc.).

## How to apply

1. When designing a multi-step plan, always map steps to **actual execution units** (subtasks or commits).  
2. Before starting a Code subtask, state explicitly which plan items it covers (e.g. “this subtask is B4–B5 only”).  
3. Prefer to leave a partial but well-documented artifact (e.g. crosswalk with 10–15 rows + mapping types) over trying to “finish everything” in one pass.  
4. Use retrospectives (`/rrr`) to capture these patterns while they are fresh and then encode them into `ψ/memory/learnings` plus any relevant project plans.


---
*Added via Oracle Learn*
