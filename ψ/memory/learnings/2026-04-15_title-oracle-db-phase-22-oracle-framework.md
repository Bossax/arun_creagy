---
title: ---
tags: [oracle-db, oracle-framework, skills-governance, mcp, vector-search, fts, oracle-skills, hybrid-shell]
created: 2026-04-15
source: ψ/memory/learnings/2026-04-11_oracle-db-phase2.2-oracle-framework-and-skills-governance-backfill.md
---

# ---

---
title: Oracle DB Phase 2.2 — oracle-framework & skills-governance learning backfill
created: 2026-04-11
type: learning
concepts:
  - oracle-db
  - oracle-framework
  - skills-governance
  - mcp
  - vector-search
  - fts
  - oracle-skills
  - hybrid-shell
source: synthesis: Arun_Creagy
---

# Oracle DB Phase 2.2 — oracle-framework & skills-governance learning backfill

Scope: oracle DB backfill – Phase 2.2 batch of oracle-framework and skills-governance patterns, distilled from existing learnings and aligned with the Group 6–7 canonicalisation pattern.

## Source artefacts

- [`ψ/memory/learnings/2026-03-28_important-issue-to-revisit-oracle-mcp-vector-sear.md`](ψ/memory/learnings/2026-03-28_important-issue-to-revisit-oracle-mcp-vector-sear.md)
- [`ψ/memory/learnings/2026-03-04_oracle-skills-updates-use-sync-branch-pr.md`](ψ/memory/learnings/2026-03-04_oracle-skills-updates-use-sync-branch-pr.md)
- [`ψ/memory/learnings/2026-03-09_awaken-realignment-hybrid-shell-and-skill-versioning.md`](ψ/memory/learnings/2026-03-09_awaken-realignment-hybrid-shell-and-skill-versioning.md)
- [`ψ/memory/learnings/2026-04-09_oracle-mcp-wiring-and-skills-governance-in-aruncr.md`](ψ/memory/learnings/2026-04-09_oracle-mcp-wiring-and-skills-governance-in-aruncr.md)

These notes were previously analysed under the “oracle-framework & skills-governance” category in [`plans/2026-04-09-learnings-indexing-map.md`](plans/2026-04-09-learnings-indexing-map.md). This canonical learning captures the stable, cross-project rules they imply.

## Stable patterns

### 1. Treat FTS as the baseline and design around vector-search fragility

- Oracle MCP may temporarily report `vector search unavailable` while `fts_status: healthy`.
- During such periods, `oracle_search()` falls back to keyword-only FTS, but all documents remain discoverable.
- Design skills and backfill selections so they:
  - never *depend* on semantic/vector search for correctness,
  - lean on strong filenames, tags, and concepts (`oracle`, `writing-th`, `crdb`, project names) for retrieval,
  - treat vector search as an optimisation that can be restored later without changing knowledge structure.

### 2. Run Oracle MCP inside the same container/runtime as the HTTP engine

- Run the Oracle MCP entrypoint (for example, `src/index.ts`) inside the **same Bun Docker container** as the HTTP engine.
- Ensure both share:
  - the same Linux runtime and Bun version,
  - the same `/vault` path mapping for repository files,
  - the same SQLite DB and vector index files.
- Treat `.roo/mcp.json` as code, not just config:
  - keep the command, args, cwd, and env explicitly wired to the docker-compose setup,
  - avoid `docker run src/index.ts` style invocations that confuse image vs script paths.

### 3. Separate “family skills” from project-local Roo skills

- Distinguish two layers of skills:
  - **Agent / family skills** installed by `oracle-skills-cli` under `~/.claude` and `~/.codex`.
  - **Roo and project skills** anchored under `~/.roo` and [`.roo`](.roo).
- Treat `oracle-skills` updates as affecting the family layer only; they do **not** rewrite Roo’s internal skill tree inside this repo.
- When maintaining skills:
  - avoid `git push --force` in the skills repositories (honour “Nothing is Deleted”),
  - prefer a patch-carrying fork + sync-branch workflow (see Group 2 below) when integrating upstream changes.

### 4. Keep `~/.roo/skills` as a patch-carrying fork via sync branches

- Treat the installed skills directory as a Git repo with two remotes:
  - `origin` = your fork that mirrors what is actually installed (e.g. `Bossax/my-oracle-skills`).
  - `upstream` = the mother-oracle source (e.g. `Soul-Brews-Studio/oracle-skills-cli`).
- For each upstream release tag:
  - fetch tags from `upstream`,
  - create a `sync/<tag>` branch from the installed tree,
  - merge the upstream tag with `--allow-unrelated-histories` if needed,
  - push the sync branch to `origin` and review/merge via PR before reinstalling.
- This workflow preserves Windows/Git Bash fixes, avoids force pushes, and makes skill updates reviewable.

### 5. Align shell and skills version layers in hybrid environments

- Adopt a single primary shell (here: Git Bash) for skills workflows, and standardise on POSIX-style commands and forward-slash paths.
- Recognise two distinct version layers:
  - the `oracle-skills` CLI binary on PATH,
  - the installed skill bundles agents actually load.
- Use commands like `bunx --bun oracle-skills@...#<tag> list -g` to verify what is installed versus what PATH resolves.
- After installing or updating skills:
  - restart the agent so new bundles are actually loaded,
  - treat `/awaken` in existing repos as a continuity audit (add constitution and traces without overwriting prior soul files).

## One-off decisions and local choices

- Concrete container names, host paths, and docker-compose service names used in earlier sessions are **examples**, not part of the canonical rule.
- Specific Git remote names (`origin`, `upstream`) and GitHub repository URLs are examples; the pattern is “fork + sync branches + PR review”, not those exact identifiers.
- The exact log file path for Chroma debug output (`c:/tmp/oracle-chroma-debug.log`) is local to this workstation; the durable rule is to ensure Chroma has a writable log path and to monitor `oracle_stats()` for vector backend health.

## Open questions / future refinement

- Restore and stabilise the Chroma/vector backend for this Oracle instance, ensuring that:
  - vector indexes persist across container restarts,
  - debug logs are written to a cross-platform path that exists inside the container.
- Decide on a standard location and naming convention for any helper scripts that automate `oracle_stats()` checks and surface vector/FTS health in `/recap`.
- Clarify how often to run a skills-governance audit (e.g. via `/awaken` plus manual checks) to catch drift between agent-installed skills and project-local overrides.

## Relationship to Oracle DB backfill

- This canonical learning is a **Phase 2.2 oracle-framework batch**: it does not introduce new domain knowledge, but stabilises how Oracle MCP, skills, and DB wiring behave.
- When selecting future DB backfill candidates in this category:
  - treat this note as the primary “oracle-framework & skills governance” pattern for wiring and skills updates,
  - keep more granular notes (vector outage incident, specific sync-branch walkthroughs) as provenance examples linked from this file,
  - ensure backfill tooling and logs (e.g. [`ψ/memory/logs/info/backfill-index.md`](ψ/memory/logs/info/backfill-index.md)) reference this canonical when recording Oracle IDs for this pattern.


---
*Added via Oracle Learn*
