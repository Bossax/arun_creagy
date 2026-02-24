---
query: "workflow"
target: "Knowledge_System"
mode: smart
timestamp: 2026-02-24 09:41 GMT+7
---

# Trace: workflow

**Target**: Knowledge_System  
**Mode**: smart  
**Time**: 2026-02-24 09:41 GMT+7

## Oracle Results

- [`2026-02-17_structured-workflow-setup.md`](psi/memory/learnings/2026-02-17_structured-workflow-setup.md:1) – high-level learning capturing why a structured Plan → Execute → Reflect workflow is needed for consultancy sessions.
- [`2026-02-12_recap-workflow-diagnosis.md`](psi/memory/learnings/2026-02-12_recap-workflow-diagnosis.md:1) – learning note explaining shortcomings in the original `/recap` workflow and the subsequent fixes.
- [`2026-02-18_rrr-recap-rrr-workflow-fix.md`](psi/memory/learnings/2026-02-18_rrr-recap-rrr-workflow-fix.md:1) – historical context for an earlier iteration of the recap/RRR workflow and its repair.
- [`2026-02-18_rrr-recap-rrr-session-wrap-up.md`](psi/memory/learnings/2026-02-18_rrr-recap-rrr-session-wrap-up.md:1) – follow-up learning summarizing the finalized recap + `/rrr` workflow and Git Bash execution discipline.
- [`2026-02-18_shell-and-recap-discipline.md`](psi/memory/learnings/2026-02-18_shell-and-recap-discipline.md:1) – captures failure patterns and prescribes a **file-first** recap/RRR workflow using `psi/memory/retrospectives` and `psi/memory/learnings` as the primary truth.
- [`05.52_interview-question-design-retrospective.md`](psi/memory/retrospectives/2026-02/13/05.52_interview-question-design-retrospective.md:1) – mentions workflow implications for interview-question design.
- [`06.06_structured-workflow-setup.md`](psi/memory/retrospectives/2026-02/17/06.06_structured-workflow-setup.md:1) – retrospective documenting creation of the structured session workflow, including new plan and template files.
- [`15.29_recap-workflow-diagnosis.md`](psi/memory/retrospectives/2026-02/12/15.29_recap-workflow-diagnosis.md:1) – retrospective narrating diagnosis of the recap workflow, reading of `tools/fix_focus.md`, and implementation of fixes.
- [`11.38_rrr-recap-rrr-workflow-fix.md`](psi/memory/retrospectives/2026-02/18/11.38_rrr-recap-rrr-workflow-fix.md:1) – documents aligning `/rrr` workflow with SKILL.MD and environment realities (Git Bash, pulse discipline).
- [`15.40_rrr-recap-rrr-workflow-session.md`](psi/memory/retrospectives/2026-02/18/15.40_rrr-recap-rrr-workflow-session.md:1) – wrap-up retrospective confirming recap + `/rrr` workflow repairs and pulse integration.
- [`21.45_recap-fix.md`](psi/memory/retrospectives/2026-02/09/21.45_recap-fix.md:1) – notes on improving recap error handling and integrating the `pulse` system into the workflow.
- [`13.34_cri-data-lineage.md`](psi/memory/retrospectives/2026-02/18/13.34_cri-data-lineage.md:40) – reflects on manual nature of data-lineage workflows and the need for better automation.

These Oracle entries collectively define two main workflow themes:

1. **Session-level meta-workflow** – how consultancy sessions are structured (planning, execution, retrospectives) and how recap/`/rrr` fit into that.
2. **Operational discipline** – especially around recap/RRR on Windows with Git Bash, emphasizing a file-first approach and guardrails against fragile shell workflows.

## Files Found

- [`00_WORKFLOW.md`](src/plans/00_WORKFLOW.md:1) – canonical description of the session workflow (Plan → Execute → Reflect), roles, and expectations for atomic commits and retrospectives.
- [`2026-02-17_structured-workflow-setup.md`](src/99_Archive/2026-02-17_structured-workflow-setup.md:1) – archived plan describing tasks and outcomes for introducing the structured workflow and associated templates.
- [`Phase 1 and 2 workflow.md`](src/01_Projects/2025-11_DCCE-CRI/notes/Phase 1 and 2 workflow.md:11) – high-level CRI project workflows for Phase 1 ("what do we have in hand?") and Phase 2 (defining resilience/readiness).
- [`CRDB - Implementation Plan.md`](src/01_Projects/2025-11_DCCE-CRDB/output/CRDB - Implementation Plan.md:30) – emphasizes IVRA-first risk assessment workflows and spreadsheet-based cataloging.
- [`Data Model for Decision-Support Frameworks.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Data Model for Decision-Support Frameworks.md:16) – surveys decision-support frameworks and details three exemplar adaptation planning workflows with associated data-model requirements.
- [`BTR Implementation plan.md`](src/01_Projects/2025-11_UNDP-BTR/output/BTR Implementation plan.md:191) – defines baseline indicator review workflows and supervision tasks.
- [`Comprehensive Risk Management (CRM) - Full structure.md`](src/03_Evergreens/Comprehensive Risk Management (CRM) - Full structure.md:88) – includes a dedicated "Risk assessment workflow" section.
- [`Land Sector and Removals Standard (Version 1.0) Consolidated Guide.md`](src/00_Inbox/Land Sector and Removals Standard (Version 1.0) Consolidated Guide.md:136) – describes a sophisticated workflow for attributing regional emissions under limited traceability.

These files show that "workflow" is used both for **meta-process** (how we run sessions) and **domain processes** (how climate risk, adaptation, and emissions analyses are operationalized).

## Git History

Not inspected for this trace. The `--smart` mode returned ample Oracle and file-level matches, so escalation to git-history analysis was not required.

## GitHub Issues/PRs

Not inspected. This local knowledge system is not being queried against remote GitHub issues/PRs in this trace.

## Cross-Repo Matches

Not inspected. This trace focused on the current `Knowledge_System` repository and its embedded Oracle memory.

## Oracle Memory

The most important Oracle memory for workflows is concentrated in:

- **Session Workflow & Structure**:
  - [`2026-02-17_structured-workflow-setup.md`](psi/memory/learnings/2026-02-17_structured-workflow-setup.md:1)
  - [`06.06_structured-workflow-setup.md`](psi/memory/retrospectives/2026-02/17/06.06_structured-workflow-setup.md:1)
  - [`00_WORKFLOW.md`](src/plans/00_WORKFLOW.md:1)

  Together, these define the canonical **Plan → Execute → Reflect** session lifecycle, backed by explicit session plans in `src/plans/` and retrospectives in `psi/memory/retrospectives/`.

- **Recap / RRR Workflow & Discipline**:
  - [`2026-02-12_recap-workflow-diagnosis.md`](psi/memory/learnings/2026-02-12_recap-workflow-diagnosis.md:1)
  - [`15.29_recap-workflow-diagnosis.md`](psi/memory/retrospectives/2026-02/12/15.29_recap-workflow-diagnosis.md:1)
  - [`2026-02-18_shell-and-recap-discipline.md`](psi/memory/learnings/2026-02-18_shell-and-recap-discipline.md:1)
  - [`11.38_rrr-recap-rrr-workflow-fix.md`](psi/memory/retrospectives/2026-02/18/11.38_rrr-recap-rrr-workflow-fix.md:1)
  - [`15.40_rrr-recap-rrr-workflow-session.md`](psi/memory/retrospectives/2026-02/18/15.40_rrr-recap-rrr-workflow-session.md:1)

  These codify that recap/`/rrr` must be **file-first** (reading and writing markdown under `psi/memory/`) with Git Bash wrappers used carefully, and they warn against brittle shell-based workflows.

- **Domain-Specific Analytical Workflows**:
  - [`Data Model for Decision-Support Frameworks.md`](src/01_Projects/2025-11_DCCE-CRDB/sources/Data Model for Decision-Support Frameworks.md:16)
  - [`CRDB - Implementation Plan.md`](src/01_Projects/2025-11_DCCE-CRDB/output/CRDB - Implementation Plan.md:93)
  - [`Phase 1 and 2 workflow.md`](src/01_Projects/2025-11_DCCE-CRI/notes/Phase 1 and 2 workflow.md:11)
  - [`Comprehensive Risk Management (CRM) - Full structure.md`](src/03_Evergreens/Comprehensive Risk Management (CRM) - Full structure.md:88)

  These provide detailed, project-specific workflows for IVRA, CRI phases, adaptation planning, and risk assessment, connecting conceptual data models to real decision-making sequences.

## Summary

For the query **"workflow"**, this trace reveals a layered structure:

1. **Canonical Session Workflow**:
   - Defined in [`00_WORKFLOW.md`](src/plans/00_WORKFLOW.md:1) and reinforced by [`2026-02-17_structured-workflow-setup.md`](src/99_Archive/2026-02-17_structured-workflow-setup.md:1).
   - Operates on a Plan → Execute → Reflect cycle with session plans in `src/plans/` and retrospectives in `psi/memory/retrospectives/`.

2. **Recap / RRR Operational Workflow**:
   - Diagnosed and repaired across multiple retrospectives and learnings (notably [`2026-02-12_recap-workflow-diagnosis.md`](psi/memory/learnings/2026-02-12_recap-workflow-diagnosis.md:1) and [`2026-02-18_shell-and-recap-discipline.md`](psi/memory/learnings/2026-02-18_shell-and-recap-discipline.md:1)).
   - The stable pattern is: **use markdown memory as the source of truth**, treat shell scripts like `pulse.sh` as small utilities, and respect Git Bash constraints on Windows.

3. **Domain-Specific Analytical Workflows**:
   - Climate risk, adaptation planning, and emissions accounting projects each define their own workflows (CRI Phase 1 & 2, IVRA workflows, adaptation planning workflows, land-sector attribution workflows).
   - These workflows are tightly coupled to conceptual data models, emphasizing the repository’s role as a **knowledge/decision system**, not just note storage.

Overall, "workflow" in this repository is not a single construct but a **hierarchy of processes**: session meta-workflow → recap/RRR operational workflow → project-specific analytical workflows. The canonical entry point for how to work in a session is [`00_WORKFLOW.md`](src/plans/00_WORKFLOW.md:1), while project notes under `src/01_Projects/` specify domain workflows that this meta-process should help execute and reflect upon.

