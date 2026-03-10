---
status: draft
type: sop
title: Knowledge Organization & Indexing SOP
project:
  - Meta
---
# Knowledge Organization & Indexing SOP

## 1. Purpose

This SOP defines how to run a **Knowledge Organization & Indexing** pass so that raw notes and research (especially `AI_output` research notes) are compressed into reusable, project‑aligned knowledge artifacts and evidence indices.

The goals are to:

- Turn scattered research into a small number of synthesis notes and methodology updates.
- Make the provenance of key design choices auditable via evidence indices.
- Improve searchability and re‑use across projects.

## 2. Inputs

Default inputs:

- **AI_output research notes** in project `sources/` folders (files with `AI_output: true` in front‑matter).

Optional additional inputs:

- Manual literature notes (papers, web pages, reports).
- Meeting notes or transcripts.
- Prior synthesis notes that need consolidation or revision.

## 3. When to run this SOP

Run a Knowledge Organization & Indexing pass when:

- You have completed a research‑heavy work session (e.g., literature review, AI deep research).
- You are about to make or revise a **methodology**, **framework**, or **implementation plan** and want the evidence clearly documented.
- You are preparing a handoff or retrospective and want a concise, evidence‑backed summary.

The session workflow treats this as a step between **Execute** and **Reflect**.
Always ask the user before execution. 
## 4. Workflow Overview

High‑level flow:

1. **Gather candidates**
2. **Cluster by questions/themes**
3. **Draft synthesis notes**
4. **Build or update an evidence index**
5. **Align or update methodology / guidance docs**
6. **Run QA and finalize metadata**

### Step 1 – Gather candidate inputs

1. Identify the relevant project folder (e.g., `src/01_Projects/2025-11_DCCE-CRI/`).
2. Within the project, scan for inputs:
   - All files with `AI_output: true` under `sources/`.
   - Any other notes you know are relevant (literature notes, meeting notes, etc.).
3. Create a short working list of candidate files for this pass.

### Step 2 – Cluster by questions and themes

1. From the session plan or project plan, list the **key questions** you are trying to answer (e.g., "How should we define adaptive vs transformative capacity?", "How do we estimate loss and damage with limited data?").
2. Group candidate inputs by which questions they inform.
3. If a source touches multiple questions, either:
   - Assign a primary question and record cross‑links later; or
   - Split your notes from that source across multiple synthesis notes.

### Step 3 – Draft synthesis notes

For each cluster of sources/questions, create a synthesis note in the project `output/` directory. Use a light structure inspired by the templates (see `src/00_Meta/template/`):

- **Title**: The question or theme (e.g., "Resilience Measurement & Indicator Design").
- **Purpose / framing**: Why this synthesis exists and how it will be used.
- **Landscape / options**: What the literature or cases say.
- **Implications for this project**: Design implications, trade‑offs, constraints.
- **Consequences for methodology / implementation**: Explicit recommendations for methodology sections, tagging rules, or plans.

Keep these notes flexible. They are structured **synthesis**, not final doctrine.

### Step 4 – Build or update an evidence index

Create or update an **evidence index** in the project `output/` directory that:

- Groups evidence by guiding questions or themes.
- Lists **primary sources** (AI_output and others) for each theme.
- Points to the relevant synthesis notes.
- Points to the specific sections of methodology or guidance documents that use this evidence.

For example, in the CRI project this pattern is implemented in `CRI_AI_sources_index.md`, which maps:

- Guiding questions → AI_output sources → methodology sections for Phase 1 and Phase 2.

### Step 5 – Align or update methodology / guidance

Use the synthesis notes and evidence index to:

- Update methodology docs so that key design decisions reference the relevant synthesis notes.
- Ensure that any new rules, equations, or frameworks have a clear evidence trail.
- Record open questions and uncertainties explicitly.

Methodology documents should remain **human‑written and flexible**, using guidance from `src/00_Meta/Methodology_Guidance.md` rather than a rigid template.

### Step 6 – QA and metadata

Before closing the session:

- Check that each new synthesis note has front‑matter with at least:
  - `type: knowledge_artifact`
  - `status: current` or `status: draft`
  - `project:` list including the relevant project code
- Verify that the evidence index has valid links to sources and synthesis notes.
- Note any major gaps in evidence as explicit "Open questions" or "Limitations".

## 5. Output Types

This SOP typically produces:

- **Synthesis notes** in project `output/` (e.g., capacity concepts, measurement approaches, loss‑and‑damage methods).
- **Evidence index** notes mapping sources → syntheses → methodology sections.
- **Methodology or guidance updates** that cite the syntheses and index.

These outputs should be stored inside the relevant project folder so they are discoverable by project context.

## 6. Relationship to the Session Workflow

In the session workflow (`00_WORKFLOW.md` in `src/00_Meta/`), Knowledge Organization & Indexing is a distinct step between **Execute** and **Reflect**:

- **Plan**: Define objectives, hypotheses, and tasks.
- **Execute**: Do the work, including research and drafting.
- **Knowledge Organization & Indexing**: Compress the day’s research into structured, evidence‑linked artifacts.
- **Reflect**: Capture what was accomplished, what was learned, and what comes next.

Treat this SOP as a default pattern, not a rigid requirement. You can run a lightweight version (quick synthesis + minimal index) or a heavier pass depending on session importance.

## 7. References

- Templates: [[Knowledge Artifact]]
- Methodology guidance: [[00_Meta/# Methodology Documentation Guidance]]

