---
status: archived
tags: []
created: 2026-02-16
last_updated: 2026-02-16
AI_prompt: false
AI_output: true
project:
  - DCCE_CRDB
type: artifact
---
# Adaptation Planning Subject Area Design Options

## Option 1: Minimum Viable Design

This design focuses on the core entities required to support DCCE's immediate needs for adaptation planning, based on existing data and established workflows.

```mermaid
erDiagram
    ADAPTATION_PROJECT ||--o{ RISK_ASSESSMENT : "addresses"
    ADAPTATION_PROJECT }|--|| SPATIAL_UNIT : "located_at"
    ADAPTATION_PROJECT ||--o{ FUNDING_SOURCE : "funded_by"

    ADAPTATION_PROJECT {
        string project_id PK
        string name
        string description
        string status
    }

    RISK_ASSESSMENT {
        string assessment_id PK
        string risk_type
        string risk_level
    }

    SPATIAL_UNIT {
        string unit_id PK
        string name
        string type
    }

    FUNDING_SOURCE {
        string source_id PK
        string name
        string type
    }
```

### Key Entities

*   **`ADAPTATION_PROJECT`**: The central entity, representing a specific adaptation intervention.
*   **`RISK_ASSESSMENT`**: Links the adaptation project to the specific climate risk it is designed to address.
*   **`SPATIAL_UNIT`**: Defines the geographic location of the project.
*   **`FUNDING_SOURCE`**: Tracks the financial resources for the project.

---

## Option 2: Ideal Workflow Design (ISO/IPCC/UNDRR-aligned)

This design incorporates a more comprehensive set of entities and relationships to support a best-practice adaptation planning lifecycle, aligned with international standards.

```mermaid
erDiagram
    DECISION_CONTEXT ||--|{ ADAPTATION_PORTFOLIO : "informs"
    ADAPTATION_PORTFOLIO ||--|{ ADAPTATION_OPTION : "contains"
    ADAPTATION_OPTION ||--o{ APPRAISAL_EVENT : "is_appraised_by"
    APPRAISAL_EVENT ||--|{ APPRAISAL_METRIC : "has"
    ADAPTATION_OPTION ||--o{ ADAPTATION_PROJECT : "is_implemented_as"

    ADAPTATION_PROJECT ||--o{ RISK_ASSESSMENT : "addresses"
    ADAPTATION_PROJECT }|--|| SPATIAL_UNIT : "located_at"
    ADAPTATION_PROJECT ||--o{ FUNDING_SOURCE : "funded_by"
    ADAPTATION_PROJECT ||--o{ INTERVENTION_RESULT : "achieves"
    INTERVENTION_RESULT }|--|| COMPOSITE_INDEX : "improves"

    RISK_TOLERANCE_PROFILE ||--|{ DECISION_CONTEXT : "guides"


    DECISION_CONTEXT {
        string context_id PK
        string name
        string description
        string uncertainty_level
    }

    RISK_TOLERANCE_PROFILE {
        string profile_id PK
        string stakeholder
        string risk_appetite
    }

    ADAPTATION_PORTFOLIO {
        string portfolio_id PK
        string name
        string description
    }

    ADAPTATION_OPTION {
        string option_id PK
        string name
        string description
        string ktm_type
    }

    APPRAISAL_EVENT {
        string appraisal_id PK
        string method
        date appraisal_date
    }

    APPRAISAL_METRIC {
        string metric_id PK
        string metric_name
        string metric_value
    }

    INTERVENTION_RESULT {
        string result_id PK
        string kpi
        string value
    }
```

### Key Enhancements

*   **`DECISION_CONTEXT`**: Frames the adaptation problem and its uncertainty.
*   **`RISK_TOLERANCE_PROFILE`**: Captures stakeholder risk appetite to guide decision-making.
*   **`ADAPTATION_PORTFOLIO`**: Allows for the evaluation of bundles of adaptation options.
*   **`ADAPTATION_OPTION`**: A library of potential solutions, decoupled from specific projects.
*   **`APPRAISAL_EVENT` & `APPRAISAL_METRIC`**: Creates a detailed and transparent record of the project evaluation process.
*   **`INTERVENTION_RESULT`**: Tracks the performance of implemented projects.
*   **`COMPOSITE_INDEX`**: Connects project outcomes back to resilience indicators.
