# Research Prompts - Deep Research and Literature Review

Purpose:
- ใช้เป็น prompt bank สำหรับ workstreams ที่ต้องการ **deep research** หรือ **literature review** มากกว่าการจัดระเบียบไฟล์ภายในโครงการ
- แต่ละ prompt ถูกออกแบบให้ป้อนเข้า LLM researcher หรือ workflow แบบ deep research ได้โดยตรง

Primary context files:
- [`base_report.md`](ψ/lab/foresight-report-wrting/artifacts/base_report.md)
- [`Research Plan - Desk Research to Close Evidence Gaps.md`](ψ/lab/foresight-report-wrting/artifacts/Research%20Plan%20-%20Desk%20Research%20to%20Close%20Evidence%20Gaps.md)
- [`Evidence Pack - Youth Baseline.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20Pack%20-%20Youth%20Baseline.md)
- [`Evidence Pack - Education Governance and Legal Feasibility.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20Pack%20-%20Education%20Governance%20and%20Legal%20Feasibility.md)

Research rules for all prompts:
- Prioritize sources from the last 5–10 years unless a classic legal or conceptual source is necessary.
- Separate **direct evidence for the Deep South** from **Thai national evidence** and **comparative international evidence**.
- Mark every finding with locality and confidence.
- Do not fabricate data. If no direct Deep South source exists, say so explicitly.
- Output should always distinguish: fact, interpretation, implication for report.

---

## Workstream 1 — Economy opportunity pack

### Research goal
Build a strong evidence base for whether and how the southern border provinces can generate realistic youth pathways through halal economy, creative economy, language advantage, digital work, and Nusantara-facing markets.

### Deep research prompt

```text
Conduct a deep research review on realistic economic opportunity pathways for vulnerable youth in Thailand’s three southern border provinces Pattani Yala and Narathiwat toward 2047–2590.

I need a desk-research synthesis for a foresight report. Focus on whether halal economy, creative economy, Malay language capability, cross-border trade, digital work, tourism, local food systems, and cultural industries can become credible pathways for youth income and mobility.

Please answer the following:
1. What are the major current and emerging economic sectors in the three southern border provinces that are plausibly relevant for youth employment or entrepreneurship?
2. Which sectors are evidence-backed versus merely aspirational in policy discourse?
3. What specific skill gaps or comparative advantages do youth in the region plausibly have, especially related to Malay language, Islamic culture, halal value chains, cultural production, or cross-border positioning?
4. What barriers block youth from moving from education into these sectors, including credentialing, capital, geography, digital access, gender norms, safety, or market access?
5. What evidence exists on halal economy growth, creative economy growth, and Nusantara-linked labour demand that is directly relevant to southern Thailand?
6. Which international or regional comparators are useful as mechanisms, not as direct analogies?

Required output structure:
- Section A: Direct evidence from Pattani Yala Narathiwat
- Section B: Thailand-level evidence relevant to the area
- Section C: Comparative international mechanisms
- Section D: Youth pathway model from school or pondok to skill to work to income
- Section E: Risks of over-claiming the opportunity narrative
- Section F: 8 to 12 report-usable claims with source notes

Source priorities:
- Thai government and provincial data
- NESDC, Ministry of Commerce, Ministry of Labour, Ministry of Higher Education, Ministry of Industry, depa, CEA, BOI if relevant
- World Bank, ADB, UNDP, ILO, UNICEF, UNESCAP
- academic literature on halal economy, border economy, cultural economy, and regional labour mobility
```

### Expected artifact from the research
- `Evidence Pack - Economy Opportunity.md`
- `Analysis Note - Youth pathways into halal and creative economy.md`

---

## Workstream 2 — Actor-network and implementation-capacity map

### Research goal
Identify which actors actually have implementation capacity, legitimacy, and convening power across education, youth development, social welfare, local economy, religion, and community trust.

### Deep research prompt

```text
Conduct a desk-research mapping of the actor ecosystem relevant to children, youth, education, welfare, community trust, and local development in Thailand’s three southern border provinces.

The purpose is to build an implementation-capacity map for a foresight report. I need to understand which actors are symbolic, which actors actually deliver, and which actors can serve as lead, broker, enabler, funder, regulator, or blocker.

Please answer the following:
1. Which categories of actors matter most in the three southern border provinces for youth futures: local government, schools, pondoks, Islamic committees, CSOs, women’s groups, youth groups, universities, provincial agencies, SBPAC, security-related institutions, private sector, social enterprises, cooperatives, zakat or waqf actors?
2. What is each actor category’s likely comparative strength in delivery, legitimacy, finance, data, convening, trust, and policy authority?
3. Which actor relationships appear cooperative, fragmented, duplicative, or distrustful?
4. What evidence exists on CSOs or local networks acting as brokers between state and community?
5. Which actors are most relevant specifically for alternative education, welfare access, creative-halal economy pathways, and protection of vulnerable youth?

Required output structure:
- Section A: Actor categories and functions
- Section B: Trust and legitimacy profile
- Section C: Delivery and implementation capacity profile
- Section D: Key coordination gaps and bottlenecks
- Section E: Suggested actor roles in H1 H2 H3 transition
- Section F: Table with actor, role, asset, trust position, constraint, and likely function in the report

Use only desk research and clearly separate documented evidence from informed inference.
```

### Expected artifact from the research
- `Actor Map - Implementation Capacity.md`

---

## Workstream 3 — Youth baseline completion via desk research

### Research goal
Close the remaining factual gaps in the youth baseline without interviews, using administrative, statistical, and policy sources.

### Literature review prompt

```text
Conduct a desk-research baseline review of vulnerable children and youth in Thailand’s three southern border provinces with a specific focus on orphans, youth at risk of leaving school, youth already out of school, and youth in religious or alternative education pathways.

Please focus on building a report-ready baseline, not a general essay.

Questions to answer:
1. What direct data exists on vulnerable youth, orphans, school access, school dropout, non-formal education, and welfare access in Pattani Yala and Narathiwat?
2. What can be said with confidence and what cannot be said due to missing data?
3. What household-level pressures are most consistently documented: poverty, debt, migration, skipped-generation households, care burdens, violence-related trauma, digital exclusion?
4. What is known about barriers to welfare access in practice, especially documentation, administrative complexity, mismatch with Muslim lifeworlds, or trust barriers?
5. What evidence exists for different education pathways: mainstream schooling, pondok or Islamic schooling, alternative/community learning, and out-of-system trajectories?

Required output structure:
- Baseline table with source, locality, year, and confidence
- Pathway summary for at least 3 youth trajectories
- Welfare-access gap summary
- 8 report-usable claims
- explicit unresolved gaps
```

### Expected artifact from the research
- update [`Evidence Pack - Youth Baseline.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20Pack%20-%20Youth%20Baseline.md)
- `Analysis Note - Youth baseline and life-path constraints.md`

---

## Workstream 4 — Education governance and legal feasibility completion

### Research goal
Strengthen the legal and governance base behind alternative education, Article 12, pondok recognition, and sandbox-style institutional flexibility.

### Literature review prompt

```text
Conduct a legal and policy desk review on education governance flexibility in Thailand, with focus on what is actually possible for community-based, Islamic, alternative, and locally designed education in the three southern border provinces.

The review must help a foresight report answer who can govern education, what can legally be changed, and what remains institutionally blocked.

Questions to answer:
1. What does Article 12 of the National Education Act actually allow in practice for families, communities, religious institutions, and non-state providers?
2. What is the real status of education innovation areas in Pattani Yala and Narathiwat, and what do they actually permit?
3. What evidence exists on pondok, Islamic schools, or community learning models being recognized or not recognized by formal systems?
4. What are the major legal or administrative constraints related to credential recognition, block grants, curriculum design, procurement, local authority, and inter-agency governance?
5. What role can SBPAC, local government, education authorities, and other institutions realistically play in scaling alternative education?
6. Which parts of the current argument rely on legal possibility and which parts still rely on political will or institutional experimentation?

Required output structure:
- Legal matrix with law, enabling clause, practical use, current bottleneck, and relevance to youth futures
- distinction between text of law and practice on the ground
- decision points that could trigger scenario shifts
- leverage points for Chapter 4
```

### Expected artifact from the research
- update [`Evidence Pack - Education Governance and Legal Feasibility.md`](ψ/lab/foresight-report-wrting/artifacts/Evidence%20Pack%20-%20Education%20Governance%20and%20Legal%20Feasibility.md)
- `Legal Matrix - Education Governance.md`
- `Analysis Note - Education governance, Article 12, and credential recognition.md`

---

## Workstream 5 — Scenario descriptor matrix support

### Research goal
Gather enough comparative and contextual evidence to define each scenario quadrant consistently on the same descriptor set.

### Deep research prompt

```text
Conduct a desk-research synthesis to support scenario design for youth futures in Thailand’s three southern border provinces.

The report now uses a scenario frame that combines changes in education governance and changes in economic structure. I need evidence and comparative mechanisms that help specify scenario descriptors consistently.

Please build evidence around the following descriptor fields:
- education model and governance
- credential recognition
- youth work and livelihood structure
- household economic resilience
- welfare and protection
- digital access and digital trust
- role of community and religious institutions
- trust between state and community
- youth agency and participation

For each descriptor, provide:
1. current baseline condition
2. plausible worsening pathway
3. plausible improving pathway
4. indicators or early signals to watch

The output should support a scenario descriptor matrix, not a narrative essay.
```

### Expected artifact from the research
- `Scenario Descriptor Matrix.md`

---

## Workstream 6 — Strategy build sheet support

### Research goal
Gather the comparative and policy evidence needed to turn the three strategies into H1/H2/H3 sequences with credible leverage points and quick wins.

### Deep research prompt

```text
Conduct a comparative policy and implementation review to support a foresight strategy build sheet for Thailand’s three southern border provinces.

The three strategy domains are:
1. alternative and plural education
2. youth livelihood and creative-halal economy
3. community empowerment, trust, and peaceful futures

I need desk research that helps translate these into H1 H2 H3 strategy logic.

Please answer:
1. What types of interventions count as realistic H1 incremental reforms versus H2 transitional innovations versus H3 transformational shifts in each strategy domain?
2. What leverage points appear strongest from comparative evidence?
3. What quick wins are often used to seed longer-term institutional change?
4. What actor configurations are required for each strategy type?
5. What common implementation failures or path dependencies should be anticipated?
6. Which strategy components appear robust across multiple futures and which depend on optimistic assumptions?

Required output structure:
- one section per strategy domain
- H1 H2 H3 table
- leverage points
- actor ownership
- quick wins
- risks and dependencies
- robustness judgment
```

### Expected artifact from the research
- `Strategy Build Sheet.md`

---

## 6. Recommended order of execution

1. Workstream 3 — youth baseline completion
2. Workstream 4 — education governance and legal feasibility completion
3. Workstream 1 — economy opportunity pack
4. Workstream 2 — actor-network and implementation-capacity map
5. Workstream 5 — scenario descriptor matrix support
6. Workstream 6 — strategy build sheet support

Reason:
- baseline and legal feasibility are the strongest dependencies for everything else
- economy and actors are the two next missing pillars
- scenario and strategy architecture should be built after those four are stronger

