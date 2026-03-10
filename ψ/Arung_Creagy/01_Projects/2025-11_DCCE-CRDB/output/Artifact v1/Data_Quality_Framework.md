---
status: current
tags:
  - governance
  - framework
  - policy
  - NCAIF
  - da
created: 2026-02-16
last_updated: 2026-02-16
project: DCCE-CRDB
type: artifact
---
>[!comment]
>This entire concept is novel to DCCE. Most datasets used by their official data products will be flagged poor quality. In addition, additional effort is needed to assess data quality since most data owners (line agencies) do not have solid quality assurance.

# Data Quality Framework

## 1. Purpose

The purpose of this Data Quality (DQ) Framework is to establish a systematic approach to measuring, monitoring, managing, and improving the quality of data within the National Climate Adaptation Information Framework (NCAIF). This framework ensures that data is fit for its intended purpose, enabling trusted and reliable decision-making for climate adaptation in Thailand.

## 2. Scope

This framework applies to all critical data assets identified and managed within the NCAIF Data Catalog, particularly those used for policy-making, risk assessment, and international reporting. It covers the entire data lifecycle, from creation and ingestion to processing and presentation.

## 3. Data Quality Dimensions

To provide a consistent and comprehensive way of assessing data quality, the NCAIF will adopt the following standard dimensions of data quality:

| Dimension | Description | Example Measurement |
| :--- | :--- | :--- |
| **Accuracy** | The degree to which data correctly represents the "real-world" object or event it describes. | Percentage of provincial rainfall records that match official TMD station readings. |
| **Completeness** | The proportion of stored data against the potential of 100% to be stored. | Percentage of `ADAPTATION_PROJECT` records that have a non-null value for the `BUDGET_THB` field. |
| **Consistency** | The absence of contradiction between data items. Data is consistent within the same dataset and across multiple datasets. | Do all records for a specific province use the same official provincial code? |
| **Timeliness** | The degree to which data is current and available for use in the expected time frame. | The time lag (in days) between the end of a reporting period and the availability of the data in the NCAIF. |
| **Uniqueness** | No entity instance is recorded more than once. The absence of duplication. | Number of duplicate project entries identified in the `ADAPTATION_PROJECT` table. |
| **Validity** | The degree to which data conforms to the syntax (format, type, range) of its definition. | Percentage of records where the `PROJECT_START_DATE` field is a valid date format and is not in the future. |

## 4. Data Quality Management Process

A continuous, proactive process will be implemented to manage data quality.

### Step 1: Define DQ Rules & Thresholds

*   **Action:** For each critical data asset, the responsible Data Steward, in consultation with data consumers, will define specific, measurable Data Quality Rules for each applicable DQ dimension.
*   **Responsibility:** Data Stewards.
*   **Example Rule:** For the `Provincial Flood Risk Index` data asset, the `Completeness` rule for the `RISK_SCORE` field is that it must be 100% populated. The acceptable `Threshold` is 98%.

### Step 2: Measure & Monitor
*   **Action:** Implement automated tools and processes to regularly measure data quality against the defined rules. The results will be visualized in Data Quality Dashboards.
*   **Responsibility:** Technical Stewards / IT Department (implementation), Data Stewards (monitoring).
*   **Tools:** The Data Catalog and dedicated DQ monitoring tools will be used to run DQ checks and display scores.

### Step 3: Analyze & Report
*   **Action:** Data Stewards will review the DQ Dashboards to identify trends, patterns, and data assets that fall below the acceptable quality thresholds.
*   **Responsibility:** Data Stewards.
*   **Reporting:** A quarterly Data Quality Scorecard will be generated and presented to the Data Stewardship Committee (DSC), highlighting problem areas and trends.

### Step 4: Remediate & Improve
*   **Action:** When a DQ issue is identified, a root cause analysis will be performed. A remediation plan will be developed and executed to correct the data and improve the underlying process to prevent recurrence.
*   **Responsibility:** Data Stewards, in collaboration with data producers and IT.
*   **Tracking:** All data quality issues will be logged, tracked, and managed through a centralized issue resolution system.

## 5. Roles and Responsibilities

*   **Data Stewards:** Are the owners of data quality for their respective domains. They are responsible for defining DQ rules, monitoring performance, and leading remediation efforts.
*   **Data Producers:** Are responsible for creating high-quality data at the source and collaborating with Stewards to fix identified issues.
*   **IT Department:** Is responsible for providing and maintaining the tools and infrastructure needed to automate DQ measurement and monitoring.
*   **Data Stewardship Committee (DSC):** Is responsible for overseeing the DQ program, resolving escalated issues, and promoting a culture of data quality.
*   **Data Consumers:** Are responsible for reporting any perceived data quality issues they encounter to the appropriate Data Steward.

## 6. Data Quality Scorecard

To ensure visibility and accountability, a standardized Data Quality Scorecard will be published quarterly. The scorecard will provide a high-level summary of the overall health of the NCAIF's data assets.

**Sample Scorecard Content:**

*   Overall Data Quality Score (weighted average across all critical assets).
*   DQ Score by Data Domain.
*   Trend analysis (improvement or decline over time).
*   Top 5 data assets with the lowest DQ scores.
*   Summary of major remediation activities undertaken in the quarter.

This framework establishes a commitment to treating data as a critical asset and provides the structure needed to ensure it remains a reliable foundation for Thailand's climate adaptation efforts.
