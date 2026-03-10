---
status: current
tags:
  - ipcc
created: 2026-02-16
last_updated: 2026-02-16
AI_prompt: false
AI_output: true
project:
  - DCCE_CRDB
type: note
sticker: emoji//1f5d2-fe0f
---
Based on my review of the Sixth Assessment Report, Chapter 17, the design of a data system for adaptation planning must account for decision-making as a non-linear, iterative, and reflexive process rather than a static event. The literature characterizes climate risk decision-making not as a single judgement, but as an ongoing cycle of assessment, action, reassessment, learning, and response (New et al., 2022).

To support robust adaptation planning, your data system should be architected around the following core analytical frameworks and decision-making phases identified in the report.

### 1. The Cognitive Phases of Decision-Making

The decision-making process is conceptually divided into cognitive phases that a data system must support sequentially and iteratively. According to French (2020) and others, these phases are:

- **Sense-making and Modelling:** This initial phase involves framing the problem. It requires "descriptive models" (assessing bio-physical systems and drivers) and "prescriptive models" (capturing stakeholder values and objectives) (French & Argyris, 2018),. Your system needs capabilities to map these relationships and elicit objectives before options are analyzed (Ackermann, 2012).
- **Analysing and Exploring:** In this phase, decision-makers use models and data services to explore the efficacy of adaptation options (French, 2020). This stage often employs sensitivity and robustness analyses to set bounds on residual uncertainty (Borgonovo & Plischke, 2016).
- **Interpreting and Implementing:** This phase interprets analysis to make choices and operationalize them. It is currently the least described in the literature but requires decision process management tools to ensure advice is fit for purpose (Spetzler et al., 2016).

### 2. Analytical Frameworks for Uncertainty (The Cynefin Framework)

To design an effective analytical toolkit, you must categorize decision contexts based on the level of uncertainty. The report utilizes the **Cynefin framework** to categorize contexts into known, knowable, complex, and chaotic (Snowden, 2002; French, 2013).

- **Known/Knowable Contexts:** In these environments, cause and effect are understood. Standard analytical methods like **Cost-Benefit Analysis (CBA)** and **Multi-Criteria Decision Analysis (MCDA)** are appropriate here for optimizing choices (New et al., 2022).
- **Complex/Chaotic Contexts (Deep Uncertainty):** When systems are complex (cause and effect are only coherent in retrospect) or chaotic, standard predictive models fail. Here, the data system must support **Decision Making Under Deep Uncertainty (DMDU)** approaches (Marchau et al., 2019). Key methods include:
    - **Robust Decision Making (RDM):** Focuses on "stress-testing" adaptation options over a wide range of future scenarios to find strategies that perform well across many futures rather than optimizing for one (Lempert, 2019).
    - **Dynamic Adaptive Policy Pathways (DAPP):** Visualizes adaptation as a series of decisions over time, using "tipping points" or "signposts" to trigger new actions when current measures become ineffective (Haasnoot et al., 2013).

### 3. Strategies for Managing Portfolios of Risk

A robust data system must move beyond single-risk management to integrated risk management.

- **Adaptive Feedback Management:** For dynamic risks, particularly in "chaotic" contexts, the system must support adaptive feedback management. This requires designing monitoring programs that provide data to an assessment procedure, which then triggers adjustments to control actions (Hurlbert et al., 2019). This is critical for managing resources like fisheries or water under changing climate conditions (Holsman et al., 2019).
- **Integrated Risk Management:** Because climate risks interact and compound, the system must facilitate cross-sectoral analysis (e.g., the water-energy-food nexus) (Nhamo et al., 2018). This involves mapping steps for adapting to sectoral risks jointly to avoid maladaptation and path dependencies (Lawrence et al., 2019).
- **Risk Layering:** The system should support "risk layering," which coordinates different interventions for different frequencies of risk. This includes risk reduction (prevention), risk financing (insurance for residual risk), and risk retention (managing unavoidable residual impacts) (Mechler et al., 2014).

### 4. Integration of Diverse Knowledge Systems

Finally, the analytical framework must accommodate data from diverse knowledge systems. Effective decision-making relies on **co-production** processes that integrate scientific data with Indigenous knowledge, local knowledge, and practitioner knowledge (Cornell et al., 2013; Cash et al., 2003),. This enhances the usability and acceptability of the decision support provided (Djenontin & Meadow, 2018).



**Summary Table of Analytical Methods for Your Data System Design:**

| Method Class           | Context (Cynefin) | Key Application                                                                          | Citation                 |
| :--------------------- | :---------------- | :--------------------------------------------------------------------------------------- | :----------------------- |
| **Bayesian Methods**   | Knowable/Complex  | Combining observational data with expert judgment to model consequences.                 | (Abbas & Howard, 2015)   |
| **DMDU / RDM**         | Complex           | Identifying "no regrets" options and robust strategies when data is sparse or contested. | (Marchau et al., 2019)   |
| **MCDA**               | Knowable          | Balancing conflicting objectives (e.g., economic vs. social) to rank adaptation options. | (Belton & Stewart, 2002) |
| **Economic/Financial** | Known/Knowable    | Valuing costs/benefits and real options analysis for investment decisions.               | (Watkiss & Hunt, 2013)   |
| **Adaptive Pathways**  | Complex           | Planning sequential decisions based on monitoring triggers (tipping points).             | (Haasnoot et al., 2013)  |