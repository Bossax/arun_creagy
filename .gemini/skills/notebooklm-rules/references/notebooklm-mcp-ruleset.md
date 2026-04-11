# NotebookLM MCP Ruleset

Canonical guardrails for using NotebookLM MCP in this repo.

This file condenses rules from:

- [`2026-04-08_notebooklm-source-fidelity-and-parameter-discipline.md`](ψ/memory/learnings/2026-04-08_notebooklm-source-fidelity-and-parameter-discipline.md)
- [`2026-04-08_notebooklm-extraction-vs-local-harmonisation.md`](ψ/memory/learnings/2026-04-08_notebooklm-extraction-vs-local-harmonisation.md)
- CRI v2 NotebookLM workflow artifacts under [`ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2)
- MCP infrastructure and auth/timeouts learnings in [`ψ/memory/learnings`](ψ/memory/learnings)
- Any environment-specific issues recorded in [`NotebookLM-MCP-troubleshooting.md`](ψ/inbox/NotebookLM-MCP-troubleshooting.md)

Use this ruleset as the **first reference** before running any structured NotebookLM extraction.

---

## 1. Scope and boundaries

1. NotebookLM is used for **literature-grounded extraction and citation-bearing concept harvesting**.
2. Harmonisation, flattening, de-duplication, QC, and canonical register maintenance are performed **locally in the repo**, not in NotebookLM.
3. NotebookLM runs must produce **raw, row-oriented or atomic-note outputs** that can be saved verbatim and later transformed locally.

Implications:
- Do not ask NotebookLM to "merge", "harmonise", "deduplicate", "rewrite the dictionary", or "QC the register".
- Do ask NotebookLM to "extract", "list", "identify", or "quote" evidence with citations.

---

## 2. Parameter discipline

Every NotebookLM MCP call must make these parameters explicit in the orchestration layer:

1. `notebook_id`
   - Always specify which notebook is being used.
   - Do not rely on the concept of an implicit "active notebook".

2. `session_id`
   - Use a concrete session id for each working session.
   - Either reuse a known open session or create a new one and record it in project context.

3. `browser_options`
   - Set explicit timeouts and stealth options that match the MCP environment config (for example, extended timeouts and stealth disabled for reliability).
   - Treat timeouts as a **latency-budget** problem: long page loads and complex prompts may require longer allowances.

4. Source-binding assumptions
   - For each batch, specify whether it is corpus-wide or tied to a specific packet of named sources.
   - Encode this assumption in the prompt itself.

Nothing about the NotebookLM configuration should be left implicit or delegated to subagents.

---

## 3. Source fidelity as a hard gate

When a batch depends on named sources ("source-bound" batches):

1. **Title resolution**
   - If you only have repo filenames or inbox handles, first run a NotebookLM pass that lists **actual notebook titles** for those documents.
   - Use the titles that NotebookLM sees, not local guesses.

2. **Small, exact-title source packets**
   - Group runs into packets of 1–3 exact titles.
   - Copy titles directly from the NotebookLM source list (no paraphrasing).

3. **Fail-fast behaviour**
   - In the prompt, instruct NotebookLM to **stop and report** when any named title is missing or ambiguous.
   - It must not substitute nearby uploaded literature without reporting.

4. **Gate for evidence validity**
   - Any batch that silently uses substitute sources fails the source-fidelity gate.
   - Such runs may be kept as methodological examples, but not as evidence for the intended packet.

The pipeline should treat this gate as **non-negotiable**. Convenience does not override source fidelity.

---

## 4. Prompt design

Design prompts so that NotebookLM stays in its strongest mode: structured extraction.

1. Single objective per prompt
   - Each prompt should target one theme (e.g., methodological capacities, framework indicators, governance clauses).

2. Extraction-only language
   - Allowed: "extract", "list", "identify", "quote", "cite", "classify within X".
   - Forbidden: "harmonise", "deduplicate", "merge outputs", "QC the register", "rewrite the dictionary".

3. Length and latency
   - Keep prompts concise and avoid overloading NotebookLM with orchestration logic.
   - Shorter, crisply scoped prompts reduce timeouts and behavioural drift.

When prompts drift into long behavioural essays, refocus them on extraction targets and output shape.

---

## 5. MCP health and auth

NotebookLM MCP is sensitive to environment and auth state.

1. Health check before long sessions
   - Use a `get_health`-style check to verify `authenticated = true` and no recent repeated errors.

2. Timeouts
   - Intermittent `Request timed out` errors should first be treated as:
     - insufficient browser timeout, and/or
     - prompts that are too large or complex.
   - Adjust MCP environment timeouts (for example in `/.roo/mcp.json`) and simplify prompts before assuming the system is broken.

3. Auth drift
   - When authentication fails repeatedly:
     - Prefer a controlled re-auth workflow: clean up browser session (while preserving the library) and then re-auth.
     - Avoid random repeated retries with the same bad state.

4. Environment quirks
   - Cross-platform CLI and shell differences (Windows vs Git Bash vs container) can affect MCP startup.
   - Capture such issues in [`NotebookLM-MCP-troubleshooting.md`](ψ/inbox/NotebookLM-MCP-troubleshooting.md) and treat them as additional constraints.

---

## 6. Failure handling and logging

When things go wrong, prefer **explicit logging + rule updates** over silent workarounds.

1. On source-fidelity failure
   - Mark the batch as invalid.
   - Do not ingest rows into canonical registers.
   - Fix titles or prompts, then rerun.

2. On timeouts
   - Shorten or split prompts.
   - Check browser timeouts and environment configuration.

3. On auth failures
   - Run health checks.
   - Apply the re-auth workflow.

4. Logging
   - For each incident, log a short note in:
     - [`NotebookLM-MCP-troubleshooting.md`](ψ/inbox/NotebookLM-MCP-troubleshooting.md); and/or
     - a dated learning note under [`ψ/memory/learnings`](ψ/memory/learnings).

---

## 7. Relationship to project workflows

1. This ruleset is **global to the repo**.
   - It applies to CRI, CRDB, foresight, and other projects that use NotebookLM.

2. Project-specific plans
   - CRI v2: plans under [`notebooklm_capacity_dictionary_v2`](ψ/incubate/DCCE/CRI/output/notebooklm_capacity_dictionary_v2) must comply with these rules.
   - Other projects should reference this ruleset in their own NotebookLM planning notes.

3. Skills separation
   - This ruleset + guardrail skill define **how** NotebookLM may be used.
   - Domain-specific skills and session plans define **what to ask** for each project.

Together, they keep NotebookLM extraction reliable, auditable, and aligned with evidence standards.

