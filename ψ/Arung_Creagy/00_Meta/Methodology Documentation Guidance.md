---
status: current
type: guidance
title: Methodology Documentation Guidance
project:
---

# Methodology Documentation Guidance

## 1. Purpose

This guidance describes how to write methodology documents that are:

- Clear about objectives and design choices.
- Explicitly linked to evidence (synthesis notes and evidence indices).
- Flexible enough to allow human judgment, narrative, and project‑specific structure.

It is **not** a rigid template. Treat it as a checklist and source of prompts.

## 2. Core questions a methodology should answer

Any methodology document should, in its own words, address:

1. **What problem is this methodology solving?**
2. **What are the key design choices and assumptions?**
3. **What evidence supports those choices?** (including limitations)
4. **How is the methodology implemented in practice?**
5. **How should outputs be interpreted and used?**
6. **What are the known limitations and open questions?**

## 3. Recommended structure (flexible)

You can use the following sections as a starting point and adapt them as needed:

1. **Strategic Context / Objectives**
   - Briefly state the goal of the methodology.
   - Situate it within the broader project or system.

2. **Conceptual Framework**
   - Define key concepts and categories.
   - Explain any tiering or dimensions (e.g., Coping / Adaptive / Transformative capacity).

3. **Design Choices and Rationale**
   - List major design decisions (e.g., why use a Fiscal Relief Index, why emphasize process indicators).
   - For each, reference the relevant synthesis notes and evidence index entries.

4. **Operational Methodology**
   - Describe the concrete steps: data inputs, transformations, tagging protocols, calculation steps.
   - Include tables or pseudo‑algorithms where helpful.

5. **Outputs and Interpretation**
   - Describe the intended outputs (indices, profiles, maps, dashboards).
   - Explain how to interpret the results and what decisions they should inform.

6. **Limitations and Future Extensions**
   - Document known data gaps, conceptual caveats, and political or practical constraints.
   - Note any hypotheses or future research directions.

You are free to merge, rename, or reorder these sections to fit each project.

## 4. Linking to evidence

Methodology docs should not carry the full literature review inside them. Instead, they should:

- Reference **synthesis notes** for detailed reasoning.
- Use an **evidence index** to show where key ideas came from.

Recommended practice:

- When you state a major design choice, add a short note like "See [capacity concepts synthesis]" or "See [loss and damage estimation synthesis]" and link to the appropriate synthesis note in the project `output/` directory.
- In one section (e.g., "Evidence and References"), summarize how the methodology is grounded:
  - Point to the evidence index for a structured mapping.
  - List the most important synthesis notes that underpin the approach.

## 5. Relationship to the Knowledge Organization & Indexing SOP

- The **Knowledge Organization & Indexing SOP** produces synthesis notes and evidence indices.
- This guidance explains how to **consume** those artifacts when drafting or revising methodologies.

Typical flow:
1. Run a Knowledge Organization & Indexing pass after research sessions.
2. Review the resulting synthesis notes and evidence index.
3. Draft or revise the methodology document using the structure above, weaving in references to the syntheses and index where design choices are justified.

## 6. Style and tone

- Favor clear, concrete language over jargon.
- Make assumptions and constraints **explicit.**
- Allow narrative and examples where helpful—methodology docs can tell a story.
- Keep enough structure that future you (or collaborators) can quickly find:
	- Design decisions
	- Implementation details
	- Evidence connections

## 7. Maintenance

- When major design choices change, update the methodology doc and ensure:
  - The relevant synthesis notes are updated or superseded.
  - The evidence index reflects new sources or changed mappings.
- Use versioning in front‑matter (`version:` or `last_updated:`) to track evolution when helpful.

