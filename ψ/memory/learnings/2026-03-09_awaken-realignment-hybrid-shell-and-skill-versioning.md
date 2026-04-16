# Learning — Awaken realignment in hybrid shell + skill version layers

When running `/awaken` (or any skills workflow) in a hybrid Windows environment, two failure modes recur:

1) **Shell ambiguity** (PowerShell/cmd vs Git Bash) breaks quoting and pipelines.
   - Adopt a single “primary shell” discipline (here: Git Bash).
   - Use forward slashes in paths and POSIX commands (`date`, `mkdir -p`, `cat`, `sed`) consistently.

2) **Version-layer mismatch** between:
   - the `oracle-skills` *CLI binary* on PATH, and
   - the installed *skill bundles* that agents actually load.

Evidence pattern: `bunx --bun oracle-skills@...#<tag> list -g` shows newer versions, while `oracle-skills list -g` still prints older versions until the agent restarts and/or PATH resolves.

**Practice**
- Treat `bunx ... list -g` as a verification channel for what’s installed.
- Restart the agent after installing/updating skills to activate them.
- In an existing Oracle repo, frame `/awaken` as a continuity audit: add constitution + traces + commits, avoid overwriting prior soul files.


---
*Added via Oracle Learn*
