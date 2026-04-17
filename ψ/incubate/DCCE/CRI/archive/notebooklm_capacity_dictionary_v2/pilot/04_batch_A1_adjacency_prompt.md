# Batch A1: Adjacency and Operational Capacities Extraction

## Objective
Instruct NotebookLM to extract candidate indicator concepts covering adaptation actions, sectoral guidelines, and operational capacities (adjacencies) from the named source packet.

## Source Packet
- `Climate adaptation indicators and metrics - State of local policy practice.pdf`
- `T. Tanner - Urban Governance for Adaptation Assessing Climate Change Resilience in Ten Asian Cities .pdf`
- `Global City Resilience Index.pdf`

## Constraint: Fail-Fast Source Fidelity
If the exact sources listed below are not present, stop and return {"error": "missing_named_sources"}.

## Extraction Requirements
Extract candidate indicator concepts for the CRI capacity tagging dictionary v2. Focus on:
1. **Adaptation Actions**: Tangible steps or projects that increase resilience.
2. **Sectoral Guidelines**: Capacity requirements specific to sectors (e.g., water, health, agriculture).
3. **Operational Capacities**: Practical, agency-level processes or assets.

## Output Format
Return the result as a JSON array of objects. Each object must include:
- `concept_id`: Temporary ID (A1-xx)
- `indicator_concept`: Short name of the indicator or capacity concept
- `definition_context`: Brief explanation from the source
- `capacity_category`: (e.g., Asset, Process, Output)
- `source_reference`: Exact filename from the source packet

Keep the response focused only on the extraction.

```json
[
  {
    "concept_id": "A1-01",
    "indicator_concept": "...",
    "definition_context": "...",
    "capacity_category": "...",
    "source_reference": "..."
  }
]
