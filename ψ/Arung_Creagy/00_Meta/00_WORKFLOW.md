---
project: ""
---
# Research Workflow

This document outlines a structured workflow for a research‑focused session, designed to enhance focus, document strategic reasoning, and ensure a clear audit trail of decisions and actions.

## The Workflow Cycle

The workflow is a cycle of **Plan -> Execute -> Knowledge Organization & Indexing -> Reflect**.

### 0. Pre-flight: Load Workflow (Research Only)

Use this workflow only when the session is research‑heavy (explicitly invoked by the user).

*   **Skim the cycle** to confirm you will complete Plan → Execute → Knowledge Organization & Indexing → Reflect.
*   **Decide the intensity** of the Knowledge Organization & Indexing pass (lightweight vs full) based on session scope.
*   **Confirm the SOP** reference if the session involves research synthesis: `src/00_Meta/Knowledge_Organization_and_Indexing_SOP.md`.

### 1. Plan: The Session Plan

At the start of each session, create a new session plan. This is a markdown file in the `src/plans` directory, named with the date and a brief description of the session's focus (e.g., `2026-02-17_data-governance-strategy.md`).

The session plan should contain the following sections:

*   **Objective**: A clear, concise statement of what you want to achieve in this session.
*   **Hypothesis**: What do you believe to be true that this session will test or validate? This is where you document your strategic reasoning.
*   **Tasks**: A checklist of the specific actions you will take to achieve the objective.
*   **Expected Outcome**: What will be the tangible output of this session? (e.g., a refined document, a set of interview questions, a committed change to the codebase).

### 2. Execute: The Work Session

During the session, work through the tasks outlined in your session plan. The key here is to stay focused on the objective and to document your work as you go.

*   **Atomic Commits**: Use git to make small, atomic commits that correspond to the tasks in your session plan. Each commit message should be clear and reference the task it completes. This creates a granular history of your work.
*   **Feature Branches**: For any significant piece of work, create a dedicated feature branch. This keeps your main branch clean and allows for focused development and review.

### 2.1 Research Workflow (Optional)

For research‑heavy sessions, follow this optional flow. This is **separate** from the NotebookLM skill, which only feeds prompts and archives notes.

1. **Define research questions** in the session plan.
2. **Run AI research tools** (e.g., Deep Research, Consensus) using those questions.
3. **Capture AI responses** in the session plan.
4. **Select sources** to upload into NotebookLM based on the AI responses.
5. **Record the NotebookLM prompt** and **NotebookLM session link** in the session plan.
6. **Run** [`/notebookLM-research`](../../.roo/skills/notebookLM-research/SKILL.md:1) **to send the prompt and archive atomic notes.**

**Session plan sections used by the NotebookLM skill:**
- `## NotebookLM Prompt`
- `## NotebookLM Session Link`

### 3. Knowledge Organization & Indexing

After sometime, ask the user if they want to run a **Knowledge Organization & Indexing** pass for the session. The goal is to compress raw notes and research into structured, project‑aligned knowledge artifacts and indices.

At a minimum:
*   **Scan and select inputs**: Identify candidate inputs from the session (by default, files with `AI_output: true` plus any other relevant notes such as web pages, literature summaries, or meeting notes).
*   **Synthesize**: Produce one or more synthesis notes or artifacts that answer specific project questions, using [[Knowledge Artifact]] template.
*   **Index the evidence**: Update or create an evidence index for the project that maps sources → synthesis notes → methodology or guidance sections.
*   **Align methodologies**: Where relevant, update methodology or guidance documents so that key design choices are explicitly anchored to synthesis notes and indexed evidence.

For details, see the dedicated SOP in [[00_Meta/Knowledge_Organization_and_Indexing_SOP.md|Knowledge_Organization_and_Indexing_SOP.md]].

### 4. Reflect: The Retrospective

At the end of each session, a retrospective is created. This is a chance to reflect on the session and capture key learnings. The retrospective should include:

*   **What was accomplished**: A summary of the work done, linking back to the session plan.
*   **Key Learnings**: What did you learn during the session? This could be about the project, the stakeholders, the technology, or your own workflow.
*   **Decisions Made**: A record of any significant decisions made during the session.
*   **Next Steps**: What are the immediate next steps that will inform the plan for the next session?

## Your Role and My Role in this Workflow

*   **Your Role (The Human Consultant)**:
    *   You define the **Objective** and **Hypothesis** in the session plan. This is where you exercise your strategic vision and judgment.
    *   You make the **Decisions** during the session, navigating the complexities and nuances of the project.
    *   You provide the **Key Learnings** in the retrospective, synthesizing your experience and insights.

*   **My Role (The AI Agent)**:
    *   I help you create the session plan template and the retrospective structure.
    *   I execute the technical tasks, such as creating files, running commands, and committing changes to git.
    *   I provide information and analysis to support your decision-making process.
    *   I maintain the history and context of the project, ensuring that nothing is lost.
