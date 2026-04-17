# CRDB — Preliminary Plan for Late-April Workshop

## Purpose

Outline a **preliminary workshop plan** focused on CRDB’s responsibilities (NCAIF, CDM, governance, catalog), so that the progress meeting can refine and confirm it. This isolates workshop design insight from the main progress-meeting agenda.

---

## 1. Workshop position in the overall timeline

- Sits after:
  - April data-acquisition work (especially for CRI impact index and related datasets).
  - Initial fieldwork and site visits planned for May.
- Before:
  - Finalisation of interim-report revisions and preparation of public/external communication.

Implication: the workshop should focus on **validation and convergence**, not on initial data scoping.

---

## 2. Workshop objectives (CRDB-focused, based on 2026-03-24 team meeting + additional context)

1. **Validate demand backbone and service tiers**
   - Confirm the main **use-case clusters** and service tiers documented in:
     - [`ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md`](ψ/incubate/DCCE/CRDB/output/NCAIF_Use_Cases.md)
     - [`ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-stakeholder-needs-synthesis-v2.md)
     - [`ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-Chapter2-interview-comparison-matrix-v2.md)
   - Ensure these use cases align with actual agency workflows and decision needs.

2. **Test baseline rules and access logic**
   - Workshop treatment of **baseline endorsement rules**, scales, and access rails based on:
     - [`ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Coverage-Map.md`](ψ/incubate/DCCE/CRDB/output/CRDB-Evidence-Coverage-Map.md)
   - Clarify which rules can be pre-decided and which are explicitly open for workshop validation.

3. **Shape governance roles and operating rhythm**
   - Use the execution-gap framing in:
     - [`ψ/incubate/DCCE/CRDB/inbox_note/2026-03-23-general-execution-gaps-for-NCAIF-CDM-and-data-governance.md`](ψ/incubate/DCCE/CRDB/output/2026-03-23-general-execution-gaps-for-NCAIF-CDM-and-data-governance.md)
   - Test candidate role mappings (owner, steward, custodian, reviewer, approver) and rhythms (update cycles, review points) against stakeholder expectations.

4. **Align on CRDB’s role in data and model governance**
   - Make explicit where CRDB is expected to:
     - manage data cataloging and baselines;
     - document model usage, assumptions, and validation;
     - coordinate with NFCS for longer-term service governance.

---

## 3. Preliminary structure and sessions

### Session 1 — Setting the frame (Plenary)

- Objectives:
  - Present the shared project timeline and roles of CRI, BTR, CRDB, NFCS.
  - Explain NCAIF and CDM as the underlying architecture.
  - Clarify what the workshop is **not** doing (e.g. redesigning basic TOR, re-opening core architecture).

### Session 2 — Demand backbone and service tiers (Breakout)

- Approach:
  - Use scenario/use-case cards derived from `NCAIF_Use_Cases.md` and the Chapter 2 synthesis.
  - Ask participants to:
    - confirm or adjust **problem statements** and **data needs**;
    - rank which services matter most for Phase 1.

### Session 3 — Baselines, scales, and access rails (Breakout)

- Approach:
  - Present baseline/endpoints candidates and scale options taken from the coverage map and interim report.
  - Discuss:
    - what can be endorsed as baseline now;
    - what should remain as candidate or interpreted datasets;
    - required caveats and metadata.

### Session 4 — Governance roles and operating rhythm (Breakout)

- Approach:
  - Start from the gaps note and Phase 1 decision log.
  - Have participants map roles (owner, steward, custodian, reviewer, approver) onto a small set of critical data domains and services.
  - Capture expectations for update cycles and review processes.

### Session 5 — Synthesis and next steps (Plenary)

- Objectives:
  - Summarize validated elements (demand backbone, baseline rules, governance patterns).
  - Identify unresolved questions that require follow-up or Phase 2 work.
  - Clarify how workshop outcomes will feed:
    - the next interim-report revision;
    - CRDB’s evidence system, catalog, and governance artifacts;
    - NFCS implementation planning.

---

## 4. Stakeholder groups and roles (preliminary)

- **Data providers / managers**: DCCE research centre, ADPC, other line agencies.
- **Data users**: policy makers (ministries, NESDC), local implementers (LAO/municipalities), analysts.
- **Governance actors**: DCCE central team, DGA, NFCS leads.
- **Facilitators / note-takers**: CRDB project team and allied consultants.

## 5. Workshop design notes from 2026-03-24 additional context

- **Morning vs afternoon structure**
  - Morning: primarily presentation of **sitemap / information architecture** and **data-governance structure per TOR**, but must *not* be purely one-way; design should include prompts or light activities that still pull input.
  - Afternoon: main **interactive** component, with breakouts that leverage interview findings and focus on product/MVP, sector, and user-tier perspectives.

- **Core design questions (from transcript)**
  - How to structure the **afternoon facilitation** so that bringing ~80 people together adds value beyond the 10+ in-depth interviews already conducted.
  - How to use existing **findings** from those interviews to seed breakout tasks (e.g. workflow maps, asset tables, gap identification).

- **Breakout grouping hypotheses**
  - By **product/MVP** (e.g. risk/impact services, baseline datasets, service bundles).
  - Cross-product with **sector** (e.g. human settlement, transport, local government).
  - Cross-product with **user tier/capacity**:
    - Tier 1: conceptual/strategic users needing understandable storylines and simple decision-support.
    - Tier 2: technical/operational users needing detailed data for risk analysis and engineering design.

- **Value proposition vs interviews**
  - Use plenary and breakouts to surface **collective intelligence** across agencies: show who holds which assets (data, tools, services) along key workflows.
  - Make visible the gaps and overlaps, and position DCCE/CRDB as convenor and integrator rather than sole data producer.

This plan should be refined during the **progress meeting** and connected explicitly to the validated decisions in [`ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-Progress-Meeting-Decisions.md`](ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-Progress-Meeting-Decisions.md).
