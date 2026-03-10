---
status: current
tags:
  - governance
  - classification
  - security
  - policy
  - NCAIF
created: 2026-02-16
last_updated: 2026-02-16
project: DCCE-CRDB
type: artifact
---

# Data Classification Policy

## 1. Purpose

The purpose of this policy is to establish a framework for classifying data based on its level of sensitivity, criticality, and risk of unauthorized disclosure or modification. This classification will determine the security and handling requirements for data within the National Climate Adaptation Information Framework (NCAIF), ensuring that data assets are protected appropriately.

## 2. Scope

This policy applies to all data processed, stored, or transmitted by the NCAIF, regardless of its format or location. All Data Stewards, data users, and IT personnel are required to adhere to this policy.

## 3. Data Classification Levels

All data within the NCAIF must be assigned one of the following three classification levels:

### Level 1: Public

* **Definition:** Data that is intended for public disclosure and has no restrictions on its distribution. Its unauthorized disclosure would result in no or minimal damage to the organization or individuals.
* **Examples:** Published research reports, public announcements, climate awareness materials, anonymized aggregated statistics.
* **Handling Requirements:**
    *   **Access Control:** No restrictions. Openly available.
    *   **Encryption:** Not required for storage or transmission.
    *   **Labeling:** Must be marked as `Public`.

### Level 2: Official Use

* **Definition:** Data that is not intended for public release and is meant for internal use by government agencies and authorized partners. Unauthorized disclosure could cause moderate harm, such as operational disruption, financial loss, or reputational damage.
* **Examples:** Draft policy documents, inter-agency communications, project implementation details, data with some personal identifiers that are not highly sensitive.
* **Handling Requirements:**
    *  **Access Control:** Access is restricted to authorized personnel with a legitimate "need-to-know."
    * **Encryption:** Must be encrypted during transmission over public networks. Encryption at rest is recommended.
    * **Labeling:** Must be marked as `Official Use`.
    * **Sharing:** External sharing requires approval from the designated Data Steward.

### Level 3: Confidential

* **Definition:** Highly sensitive data that, if disclosed, could cause severe damage. This includes compromising national security, violating laws (e.g., Personal Data Protection Act - PDPA), causing significant financial loss, or endangering individuals.
* **Examples:** Personally Identifiable Information (PII) of vulnerable populations, locations of critical infrastructure, unannounced national policy decisions, data under legal privilege.
* **Handling Requirements:**
    *   **Access Control:** Access is strictly limited to a named list of authorized individuals.
    *   **Encryption:** Must be encrypted both in transit and at rest.
    *   **Labeling:** Must be marked as `Confidential`.
    *   **Sharing:** External sharing is prohibited unless explicitly permitted by law and approved by the Data Governance Council (DGC).
    *   **Storage:** Must be stored in secured, access-controlled environments.

## 4. Responsibilities

*   **Data Stewards:** Are responsible for assigning the initial data classification to their data assets. They must review these classifications annually or when the data's context changes.
*   **Data Users:** Are responsible for handling all data according to its classification level and adhering to the required security controls.
*   **IT Department:** Is responsible for implementing and maintaining the technical security controls (e.g., encryption, access controls) that support this policy.
*   **Data Stewardship Committee (DSC):** Is responsible for reviewing and resolving any disputes or ambiguities regarding data classification.

## 5. Procedure for Data Classification

1.  **Initial Classification:** When a new data asset is created or ingested into the NCAIF, the responsible Data Steward must assign a classification level as part of the data registration process in the Data Catalog.
2.  **Review:** Data classifications must be reviewed by the Data Steward at least annually. A review should also be triggered by events such as a change in the data's use, aggregation with other data, or a change in relevant laws.
3.  **Reclassification:** If a review determines that the classification level needs to change, the Data Steward must update the classification in the Data Catalog and ensure that the appropriate handling measures are adjusted accordingly. All reclassification decisions must be logged.

## 6. Policy Enforcement

All users of the NCAIF are required to comply with this policy. Violations may result in disciplinary action, including the suspension of access privileges. Any suspected breach of this policy must be immediately reported to the Data Stewardship Committee.
