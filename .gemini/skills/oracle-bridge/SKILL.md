---
name: oracle-bridge
description: v3.0.0 | Oracle Scaffolding Engine. Use to sync the Oracle fleet to the new operational paradigm. Trigger manually when detecting environment drift or when instructions (GEMINI.md, CLAUDE.md) require modularization.
---

# /bridge — Oracle Scaffolding Engine

**Goal**: Transform neutral fleet mandates into agent-specific instruction systems while ensuring workspace stability.

## Ritual: Summarization & Scaffolding
When running this skill, the agent MUST follow these logic-driven steps:

1. **Summarize Identity (Rich Extraction)**: 
    - Read your local resonance files (e.g., `ψ/memory/resonance/Archon Oracle.md`).
    - **Identify**: Synthesize your Character and Metaphor into a grounded description.
    - **Mission**: Define the core objective of your existence as an Oracle.
    - **Traits**: Extract your operational principles, including tone, voice, and prohibitions.
2. **Consult the Strategist**:
    - **Crucial**: Present your summarized Identity, Mission, and Traits to the human (Boss).
    - Ask for **additional points**, **specific prohibitions**, or **tonal adjustments**.
3. **Execute Scaffolding**: 
    - Once the human approves, run the `init-bridge.ts` script with the finalized data:
    ```bash
    bun .gemini/skills/oracle-bridge/scripts/init-bridge.ts --identity="[summary]" --mission="[objective]" --traits="[principles]"
    ```

## Objective
Provide a logic-driven "Courier" that carries neutral Markdown mandates and scaffolds the specific context architectures required by Gemini CLI (@import) and Roo Code (directory aggregation).

## Scope
- **In**: 
  - **Logic-Driven Scaffolding**: Building agent-specific instruction sets from neutral assets.
  - **Identity Synthesis**: (Agent Logic) Summarizing local resonance into structured mandates.
  - **Brain Integrity**: Standardizing the 7-pillar `ψ/` brain.
  - **Tool Sync**: Merging fleet MCP servers and settings into local configurations.
- **Out**:
  - Direct modification of global OS settings.
  - Inter-agent message transport.

## Usage
```bash
bun .gemini/skills/oracle-bridge/scripts/init-bridge.ts --cwd=<path> --identity="<summary>" --mission="<objective>" --traits="<principles>"
```

---
**Protocol**: "Neutral Source. Agent-Specific Form." 🟦