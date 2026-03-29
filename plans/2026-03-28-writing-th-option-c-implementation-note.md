# writing-th Option C — implementation note (design + ops)

**Date**: 2026-03-28

## Decision

Adopt **Option C (Hybrid)** for Thai writing workflows:

- Every writing session produces a **Session Style Pack Summary** appended into the writing plan (append-only).
- Session packs are reusable by explicit reference.
- Stable rules can be **promoted to resonance** (append-only) after repeated use or explicit approval.

## Two-skill architecture

1) Execution + drafting:

- [`/writing-th`](.roo/skills/writing-th/SKILL.md)
- Responsibilities:
  - MCP-first retrieval (resonance + learnings)
  - Example report style mimicry (terminology + section flow)
  - Write Session Style Pack Summary into the plan
  - Outline-stop boundary
  - Produce draft files without overwrite (versioned)

2) Learning from edits:

- [`/writing-th-learn`](.roo/skills/writing-th-learn/SKILL.md)
- Responsibilities:
  - Read the session plan + style summary context
  - Compare draft vs edited and distill patterns (word choice + semantic arrangement)
  - Write durable learning notes under `ψ/memory/learnings/`
  - Apply the `oracle_learn()` materialization guardrail

## Guardrails

- Example report is **style reference only**; no verbatim copying.
- Resonance safety rails always apply (citations, hedging, no hallucinated sources).
- External deliverables must not contain repo-internal links/scaffolding.

## Trace

- Discovery trace for the redesign: [`ψ/memory/traces/2026-03-28/1157_thai-report-writing_redesign-writing-th-skill.md`](ψ/memory/traces/2026-03-28/1157_thai-report-writing_redesign-writing-th-skill.md)

## Operational risk

`oracle_learn()` may report success but not materialize a file on disk immediately.

- Guardrail reference: [`ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md`](ψ/memory/learnings/2026-03-27_oracle-learn-file-materialization-guardrail.md)

