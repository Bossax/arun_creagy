---
title: ---
tags: [oracle-db, notebooklm, extraction, harmonisation, source-fidelity, guardrails, prompt-design]
created: 2026-04-15
source: ψ/memory/learnings/2026-04-11_oracle-db-backfill-group5-notebooklm-extraction-harmonisation-guardrails.md
---

# ---

---
title: Oracle DB backfill — Group 5 NotebookLM extraction vs harmonisation & source-fidelity guardrails
created: 2026-04-11
type: learning
concepts:
  - oracle-db
  - notebooklm
  - extraction
  - harmonisation
  - source-fidelity
  - guardrails
  - prompt-design
source: rrr: Arun_Creagy
---

# Oracle DB backfill — Group 5 NotebookLM extraction vs harmonisation & source-fidelity guardrails

## Scope

This canonical learning represents **Group 5 – NotebookLM extraction vs harmonisation & source-fidelity guardrails** from the indexing map in [`plans/2026-04-09-learnings-indexing-map.md`](plans/2026-04-09-learnings-indexing-map.md).

It encodes the policy that **NotebookLM should be treated as a pure data‑extraction engine**: prompts stay short and atomic; harmonisation and quality control happen locally; and strict source‑fidelity and parameter‑discipline guardrails are enforced (including title probes).

## Source artefacts

Group 5 member files (from the indexing map):

- [`ψ/memory/learnings/2026-04-08_notebooklm-prompt-design-principles-of-extraction.md`](ψ/memory/learnings/2026-04-08_notebooklm-prompt-design-principles-of-extraction.md)
- [`ψ/memory/learnings/2026-04-08_notebooklm-extraction-vs-local-harmonisation.md`](ψ/memory/learnings/2026-04-08_notebooklm-extraction-vs-local-harmonisation.md)
- [`ψ/memory/learnings/2026-04-08_notebooklm-source-fidelity-and-parameter-discipline.md`](ψ/memory/learnings/2026-04-08_notebooklm-source-fidelity-and-parameter-discipline.md)
- [`ψ/memory/learnings/2026-04-08_notebooklm-title-probe-and-guardrail-implementation.md`](ψ/memory/learnings/2026-04-08_notebooklm-title-probe-and-guardrail-implementation.md)
- [`ψ/memory/learnings/2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md`](ψ/memory/learnings/2026-04-09_treat-notebooklm-as-a-data-extraction-engine-not.md) **(proposed primary)**

The proposed primary note provides the overarching policy; the others contribute specific prompt‑design patterns and guardrail mechanisms.

## Stable patterns

- Treat NotebookLM as a **data‑extraction engine**, not a free‑form summariser or harmoniser.
- Keep prompts **short, atomic, and extraction‑focused**, targeting clear fields or facts rather than open‑ended synthesis.
- Perform **harmonisation, schema alignment, and interpretation locally** (for example in this repo) where versioning and provenance can be controlled.
- Enforce **source fidelity and parameter discipline**:
  - Always specify which sources are in scope.
  - Avoid hidden or default context that could leak unrelated material into answers.
  - Use title probes and similar checks to verify that NotebookLM is actually reading the intended document.
- Treat deviations from these rules as guardrail violations and capture them as learnings when they occur.

## One-off decisions

- In this corpus, NotebookLM is not used as a harmonisation engine; any harmonised artefact must be clearly marked as such and traceable back to source‑level extracts.
- Guardrail implementations (for example title‑probe patterns) are allowed to evolve, but the **policy boundary** between extraction and harmonisation is stable.

## Open questions

- How should Oracle DB represent the distinction between extraction patterns and harmonisation patterns when both coexist in the same project?
- What additional automated checks could be added to detect when NotebookLM is over‑summarising or hallucinating beyond the provided sources?
- How should multi‑document extraction sessions be modelled so that source‑fidelity guarantees remain strong?

## Relationship to Oracle DB backfill

- Oracle DB should receive **one canonical learning** for NotebookLM extraction vs harmonisation and source‑fidelity guardrails, tied to this file.
- Individual prompt‑design and guardrail implementation notes remain as detailed references but can be marked as superseded for the purposes of DB backfill.
- Oracle DB backfill should:
  - Create or confirm a `learning` entry linked to this canonical file.
  - Tag it with concepts: `oracle-db`, `notebooklm`, `extraction`, `harmonisation`, `source-fidelity`, `guardrails`, `prompt-design`.
  - Record the Oracle ID in [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md) under *Group 5 canonical backfill*.


---
*Added via Oracle Learn*
