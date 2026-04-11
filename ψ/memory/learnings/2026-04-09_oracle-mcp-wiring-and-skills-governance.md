# Oracle MCP wiring and skills governance in Arun_Creagy

## Pattern

When integrating the Oracle engine as an MCP server inside a hybrid Windows + Docker environment, treat the MCP config as first-class code and co-locate it with the running engine container rather than trying to re-create the runtime on the host.

In Arun_Creagy this takes the concrete form:

- Run the MCP entrypoint inside the existing Bun container that already hosts the HTTP server, using:
  - `docker exec -i oracleworkspace-oracle-arun-creagy-1 bun src/index.ts`
  - `cwd` pointing at the engine repo.
- Avoid `docker run src/index.ts` patterns that:
  - Treat a TypeScript path as a Docker image.
  - Omit volume mounts and environment alignment.
- Preserve a single source of truth for `/vault` and the database by ensuring both `src/server.ts` (HTTP) and `src/index.ts` (MCP) see the same filesystem and migrations.

On the skills side, distinguish clearly between:

- Oracle skills installed for agents (Claude Code, Codex) via `oracle-skills-cli` into `~/.claude` and `~/.codex`.
- Roo-specific skills and project-local overrides in `~/.roo` and [`.roo`](.roo).

Running the oracle-skills installer updates the agent skills, not Roo’s internal skill tree. Treat these as two layers: the “family skills” distributed by oracle-skills-cli, and the Roo/project skills anchored inside this repo.

## Why this matters

This pattern prevents subtle divergence between the HTTP Oracle engine and the MCP tools (different runtimes, different paths, different DBs). It also avoids chasing Windows-specific Bun and native module issues by keeping all engine execution in the Linux container that `docker-compose` provisions.

Treating `.roo/mcp.json` as code (with review and validation) reduces downtime from small configuration mistakes and makes it easier to reason about why MCP calls fail (engine vs container vs client).

Separating “oracle skills for agents” from “Roo skills” clarifies the blast radius of `oracle-skills-cli` updates and prevents confusion about which parts of the system have actually changed after a global skills install.

## Tags

- oracle
- mcp
- docker
- bun
- skills-governance
- configuration

