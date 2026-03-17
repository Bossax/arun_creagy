# Chapter 1 → Chapter 2 handoff analysis

Comparison basis:

- [`2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md`](ψ/incubate/DCCE/CRDB/output/2026-03-13-CRDB-Interim-Report-Section-1.6-1.12-Draft-th-v2.md)
- [`2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-CRDB-Interim-Report-Chapter-1-Draft-v3.md)
- [`2026-03-17-Chapter1-Chapter2-restructuring-decision-note.md`](ψ/incubate/DCCE/CRDB/output/2026-03-17-Chapter1-Chapter2-restructuring-decision-note.md)

## Main finding

The intended split between Chapter 1 and Chapter 2 is **defined clearly in the restructuring decision note**, but it is **not yet fully executed in the prose** of Chapter 1 v3. In practice, the current Chapter 1 still contains mixed paragraphs where description and interpretation remain combined.

This means the handoff to Chapter 2 cannot rely only on what has already been removed from Chapter 1. It must actively identify the descriptive material that still needs to be developed as Chapter 2 landscape prose.

## Keep / move / bridge decisions

| Source location | Current function in v2 / v3 | Keep in Chapter 1 | Move into Chapter 2 | Bridge action |
|---|---|---|---|---|
| **1.6 paragraph opening** — current landscape is fragmented | establishes the core problem of fragmented existing assets | **Yes** — keep the analytical conclusion that fragmentation is the core issue | No | none |
| **1.6 website description** — DCCE adaptation content is scattered across multiple points and not arranged as a continuous cycle | mixed descriptive + analytical | keep only the implication that the current arrangement does not support user logic | **Yes** — fuller description of current website content groups belongs in Chapter 2 landscape review | add a short sentence from Chapter 1 pointing to Chapter 2 for the fuller current-state review |
| **1.6 risk-map existence and bounded scope** — DCCE already has a usable product, but it is bounded by scale and interpretation | mixed descriptive + analytical | keep only the conclusion that the risk map is real but bounded and cannot be over-claimed as a complete platform proof | **Yes** — the three-part product structure, scope, current functions, and caveats should be described in Chapter 2 | use Chapter 1 to signal that Chapter 2 will document current product reality |
| **1.6 NCAIF as reorganizing layer** | architecture interpretation | **Yes** | No | none |
| **1.6 explicit statement that detailed landscape belongs in Chapter 2** | drafting instruction embedded in prose | No as final report prose | No as report prose | transform this into editorial guidance and use the handoff note instead |
| **1.7 UX / IA principles** — information scent, shallow menus, multiple entry routes, progressive disclosure | architecture and experience-design reasoning | **Yes** — this is core Chapter 1 territory | Not as Chapter 2 prose | extract only product expectations that help structure Chapter 2 tables, not the reasoning itself |
| **1.7 examples of user-facing needs** — policy summaries, area-based entry pages, tool/data separation, transparent caveats | partly descriptive expectations for visible products | keep the reasoning in Chapter 1 | selectively **reuse as implications** for how current products should be described in Chapter 2 tables | reflect these as “audience” or “limitation” columns in the landscape table |
| **1.8 onward** — CDM interpretation, workflow patterns, MVPs, design choices | architecture and framework interpretation | **Yes** | No | none |

## Material retained in Chapter 1

Chapter 1 should keep the following as its stable analytical core:

- the conclusion that the current DCCE landscape is fragmented and needs reorganization
- the conclusion that the spatial risk-map product is real but bounded in scope and interpretation
- the explanation of why those realities imply the need for a hidden organizing layer
- UX and information-architecture reasoning
- CDM, workflow-pattern, MVP, and design-choice interpretation

## Material moved into Chapter 2

Chapter 2 should now carry the fuller **descriptive current-state material**, including:

1. the current DCCE website content landscape and its main content groups
2. the current product ecosystem visible across DCCE and partner agencies
3. the spatial risk-map product as a current information product, including:
   - `Data Model & Indices`
   - `User-facing Maps`
   - `Backend Database & Tools`
   - provincial display scope
   - scenario and time-slice coverage
   - usage caveats and non-claims
4. partner-agency systems, dashboards, registries, and data centers referenced in FGD1 and the interviews

## Transitional bridge sentences needed

Suggested bridge logic for Chapter 1:

1. *The current DCCE website and related products already contain important information assets, but their full descriptive landscape is reviewed separately in Chapter 2 so that this chapter can focus on the architectural implications of that current state.*
2. *Likewise, the existing spatial climate risk-map product is treated in Chapter 2 as part of the current information-product landscape, while this chapter retains only the analytical implications of its present scope and limitations.*

## Implications for the current data product landscape table

The comparison confirms that the landscape table must explicitly include the descriptive elements that Chapter 1 should stop carrying in full prose:

- DCCE website-content groups and journey gaps
- the spatial risk-map product as a current three-part product stack
- present scope and limitations of the risk-map product
- other current systems already maintained by DCCE and partner agencies

## Editorial conclusion

The comparison between v2 and v3 shows that **the conceptual split is settled, but the prose split is not yet complete**. The analysis artifacts created for Chapter 2 are therefore not optional side notes; they are the mechanism that will allow the next pass of report drafting to actually enforce the intended division of labor between the two chapters.
