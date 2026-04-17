
## 1. Locked decision

The following engagement streams are now treated as fixed planning anchors for CRDB:

1. **Discussion with DCCE IT team regarding their data system upgrade** — **2026-04-29**
2. **Consultation workshop / TOR 5.3.3 brainstorming meeting** — **mid-May (target 2026-05-12)**
3. **Focus Group Discussion 3 (FGD3)** — **late May**

This note explains how to use these three conversations to move the project forward, what should be prepared for each stream, which questions can be answered by desk research versus stakeholder engagement, and whether any extra engagement is needed.

Grounding anchors:

- Project plan: [`ψ/incubate/DCCE/CRDB/plan.md`](ψ/incubate/DCCE/CRDB/plan.md)
- **Thaiwater enhancement concept note:** [`2026-04-08_CRDB-Thaiwater-Enhancement-Concept-Note.md`](ψ/incubate/DCCE/CRDB/output/2026-04-08_CRDB-Thaiwater-Enhancement-Concept-Note.md)
- DCCE IT integration note: [`ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-DCCE-IT-Integration-Note.md`](ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-DCCE-IT-Integration-Note.md)
- Workshop plan v3: [`ψ/incubate/DCCE/CRDB/output/2026-03-31_CRDB-Workshop-Plan-v3_TOR533-aligned.md`](ψ/incubate/DCCE/CRDB/output/consultation_workshop/2026-03-31_CRDB-Workshop-Plan-v3_TOR533-aligned.md)
- Internal FGD strategy: [`ψ/incubate/DCCE/CRDB/output/DCCE Focus Group Discussion Plan.md`](ψ/incubate/DCCE/CRDB/output/DCCE Focus Group Discussion Plan.md)
- Confirmed Phase 1 decisions: [`ψ/incubate/DCCE/CRDB/output/phase1_decision_log.md`](ψ/incubate/DCCE/CRDB/archive/phase1_decision_log.md)
- History spine: [`ψ/incubate/DCCE/CRDB/output/CRDB-Project-History-Timeline.md`](ψ/incubate/DCCE/CRDB/archive/CRDB-Project-History-Timeline.md)

---

## 2. Overall strategy across the three streams

The three streams should not be treated as separate meetings. They should function as a **staged progression**:

1. **2026-04-29 IT discussion**
   - Purpose: clarify platform reality, constraints, and integration opportunities.
   - Output type: internal architecture and governance requirements, framed in language the IT team can respond to.

2. **2026-05-12 consultation workshop**
   - Purpose: validate ecosystem needs, data/product exchange realities, and priority service bundles with external and cross-agency stakeholders.
   - Output type: evidence for TOR 5.3.4–5.3.9 (inventories, gap analysis, policy/technical recommendations).

3. **Late-May FGD3**
   - Purpose: convert external feedback and IT realities into an internal DCCE execution stance.
   - Output type: internal ownership, governance decisions, integration roadmap, and budget-justification logic.

In short:

- **IT discussion** = clarify the implementation environment.
- **Workshop** = validate demand, supply, and exchange constraints.
- **FGD3** = commit DCCE to a workable execution and governance pathway.

---

## 3. Stream 1 — DCCE IT team discussion on data system upgrade (2026-04-29)

### 3.1 Strategic role of this stream

This meeting should answer the question:

> “How can CRDB Phase 1 outputs become upstream requirements for DCCE’s data-system upgrade, instead of being treated as a side project that must adapt later?”

This stream is especially important because the current evidence suggests that the 6th-floor IT project may already have consultants working on a central DCCE data system, but its scientific requirements, artifacts, and governance expectations are still unclear in [`2026-03-24_CRDB-DCCE-IT-Integration-Note.md`](ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-DCCE-IT-Integration-Note.md).

### 3.2 Objectives

1. Confirm the **actual scope** of the IT team / consultant study.
2. Identify where CRDB outputs should act as **requirements artifacts**:
	- NCAIF structure and **Thaiwater-inspired architecture slots (standards/governance sections)**
	- CDM subject areas with **observation envelope logic (metadata + payload)**
	- **Reference standards layer (admin boundaries, agency codes, canonical indicators)**
	- **Data quality framework (QC levels and flags)**
	- metadata / catalog requirements
	- governance rails and gates (open / G2G / internal)
3. Clarify whether the IT project is being designed as:
	- infrastructure only,
	- data platform + governance,
	- or end-user portal + data platform.
4. Identify what CRDB must prepare **before** the workshop and FGD3 so DCCE can negotiate from a position of clarity.

### 3.3 Questions this stream must answer

#### Architecture and platform
- What is the target architecture being studied by the IT consultant?
- Will the system include:
	- metadata catalog,
	- integration middleware,
	- **support for reference information layers (admin boundaries, units)**,
	- **support for observation-style data (metadata + payload envelopes)**,
	- storage layer,
	- portal/front-end,
	- access-control / identity layer,
	- workflow for approvals or publication?
- Is the system intended to host data, or mainly coordinate/link existing systems?

#### Governance and standards
- Are data standards, steward roles, and governance flows inside the IT consultant’s scope?
- **How will the system handle cross-domain data quality (QC levels and flags)?**
- **Can the system support Thaiwater-inspired publishing rails (open / G2G / internal)?**
- Which DCCE unit is expected to own:
	- metadata standards,
	- catalog administration,
	- cross-agency coordination,
	- platform operations?
- How is the IT team thinking about open / shared / internal rails?

#### CRDB integration

- Can CRDB’s NCAIF, CDM, baseline registry logic, and governance gates be accepted as upstream design inputs?
- Which CRDB artifacts do they need first in order to use them?
- What is the time window for influencing their design before it solidifies?

### 3.4 What can be prepared by desk research before the meeting

Desk research / internal synthesis should answer as much as possible before the meeting:

1. **Current CRDB stance package**
   - From existing artifacts, prepare a concise pack covering:
     - catalog-first architecture,
     - **Thaiwater-inspired architecture: reference layers, observation envelopes, and QC levels**,
     - publishing rails,
     - governance gates G1–G5,
     - NCAIF as semantic / user-facing structure,
     - CDM as conceptual backbone.

2. **Existing DCCE digital landscape summary**
   - Consolidate known facts from:
     - [`2026-03-24_CRDB-DCCE-IT-Integration-Note.md`](ψ/incubate/DCCE/CRDB/output/2026-03-24_CRDB-DCCE-IT-Integration-Note.md)
     - website gap notes
     - interview syntheses referencing current systems and technical constraints.

3. **Questions matrix for IT team**
   - Prepare a structured question sheet with three sections:
     - current scope of the IT project,
     - governance/standards provisions,
     - required inputs from CRDB.

4. **Candidate non-negotiables**
   - Define CRDB’s minimum requirements for any future DCCE platform:
     - metadata catalog support,
     - boundary/crosswalk capability,
     - support for baseline endorsement,
     - support for event schema with timeliness and revision flags,
     - ability to separate open / G2G / internal rails.

### 3.5 What must come from stakeholder engagement in the meeting

The following can only be obtained from the IT team / consultant side:

- Real scope of the central data-system upgrade project.
- Their proposed architecture and operating model.
- Whether they already have deliverables or deadlines that CRDB must sync to.
- Whether they see CRDB as an input, dependency, or downstream integration problem.
- The identities/job titles of future system owners and custodians.

### 3.6 Target outputs from the stream

Minimum outputs:

1. **IT discussion note / meeting memo**
   - documented scope,
   - integration risks,
   - agreements and unknowns.

2. **CRDB → IT requirements list**
   - short list of requirements artifacts CRDB will provide.

3. **Decision on positioning for workshop + FGD3**
   - what to say publicly,
   - what to hold for internal alignment.

### 3.7 Additional engagement proposed

If the April 29 discussion is limited to IT managers and not the actual consultant/design team, add:

- **One short follow-up technical working session** with the consultant team or system architect.

Reason:

- Without direct access to the designers, CRDB may only get high-level answers and miss the chance to influence concrete architecture.

---

## 4. Stream 2 — Consultation workshop / TOR 5.3.3 brainstorming meeting (target 2026-05-12)

### 4.1 Strategic role of this stream

This workshop should answer:

> “Across the ecosystem, what data, information products, and user needs are real enough to structure CRDB inventories, service bundles, and policy/technical recommendations?”

This is the main external validation stream for TOR 5.3.3 and should feed directly into 5.3.4–5.3.9.

### 4.2 Objectives
1. Capture structured evidence on:
   - datasets and information products,
   - needs/demand,
   - access constraints,
   - maturity and readiness.
2. Use one or two decision journeys to make the exchange concrete.
3. Generate workshop outputs reusable for:
   - information product and baseline data inventories with **rich metadata (reference codes, units, update frequency)**.
   - **Minimum Viable Dataset (MVD)** with **observation envelope logic** and **QC flags**.
   - supply vs demand gap analysis and policy/technical recommendations.

### 4.3 Questions this stream must answer
#### Supply side

- What datasets exist and are relevant to flood / heat / adaptation decisions?
- What products already exist (dashboards, maps, reports, APIs, spreadsheets)?
- What are their owners, formats, update frequencies, spatial scales, and access conditions?

#### Demand side

- What do agencies actually need to perform planning, budgeting, operations, response, and communication?
- Which needs are unmet because:
  - the data do not exist,
  - they exist but are inaccessible,
  - they exist but are unusable,
  - or the product format is wrong?

#### Service bundle / usability side

- Which bundles of data + products would be most useful in the next 3–6 months?
- Which minimum operating touchpoints between agencies are necessary?

### 4.4 What can be prepared by desk research before the workshop

1. **Pre-seeded baseline sheets**
   - Pre-fill capture templates with known datasets/products.
   - **Include slots for reference standards (admin codes, agency codes) and QC flag vocabulary.**

2. **Journey framing**
   - Decide whether to run flood or flood + conditional heat.
   - **Incorporate "observation envelope" thinking (provider, time, location, variable, value, unit) into the journey capture.**

3. **Room structure and capture logic**
   - Prepare breakout sheets and canvases aligned with:
     - data/product inventory logic (metadata + QC),
     - service blueprint logic.

4. **Evidence templates**
   - Registration, sign-in, group assignments, photo checklist, note template, room output template.

### 4.5 What must come from stakeholder engagement in the workshop
- Which datasets/products stakeholders are actually willing to name and exchange.
- Real access/posture constraints that do not appear in desk materials.
- Operational pain points and unmet needs in stakeholders’ own language.
- Priorities: what is worth turning into a Phase 1 service bundle versus what is clearly future work.

### 4.6 Target outputs from the stream

1. **Workshop evidence package** satisfying TOR 5.3.3.
2. **Structured inventory sheets** for datasets and products, including **publishing rail assignments (open/G2G/internal) and QC levels**.
3. **Service bundle shortlist** (Phase 1 vs later).
4. **Gap themes** (missing data, inaccessible data, unusable data, insufficient productization, governance/coordination barriers).
5. **Bridge board / synthesis board** for carrying into FGD3.

### 4.7 Additional engagement proposed

Two optional additions depending on what happens before May 12:

1. **Targeted pre-workshop calls to key anchor agencies**
   - especially if attendance from critical actors (DDPM, NSO, DGA, DPT, local authorities, public-health actors) looks weak.

2. **Post-workshop clarification interviews**
   - short follow-ups with agencies whose outputs are promising but whose access rules or maturity were unclear in the room.

These should only be triggered if workshop evidence is insufficient for 5.3.4–5.3.9.

---

## 5. Stream 3 — FGD3 (late May)

### 5.1 Strategic role of this stream

FGD3 should answer:

> “Given what we learned from the IT stream and the consultation workshop, what exactly will DCCE own, approve, and push forward as the internal execution roadmap?”

This is the internal commitment and handover stream.
### 5.2 Objectives

1. Translate workshop findings into an internal DCCE action plan.
2. Confirm how NCAIF and CRDB outputs fit the future DCCE data system.
3. Clarify governance ownership:
   - **CDM domains and NCAIF content/service domains**,
   - stewards, custodians, and endorsement authority.
4. Formalize **governance control flows (onboarding, revision, publication)**.
5. Decide which elements of the roadmap belong to Phase 1 output vs future build.

### 5.3 Questions this stream must answer

#### Internal ownership and governance

- **Which DCCE group owns each main NCAIF / CDM domain?**
- Who acts as steward vs system custodian?
- Who can endorse baselines and approve publication?
- **How will DCCE operationalize Thaiwater-inspired governance control flows (onboarding, QC check, rail assignment)?**

#### Integration and roadmap

- Which CRDB outputs (Reference layers, QC framework, observation envelopes) should be requirements for the upgraded DCCE data system?
- What can DCCE operationalize immediately using process and templates?
- What requires future budget or platform build?

...
#### Prioritization

- Which service bundles or data domains are the immediate priorities after the workshop?
- Which gaps should become explicit budget justification items?

### 5.4 What can be prepared by desk research before FGD3

1. **Synthesis pack**
   - One short internal synthesis combining:
     - IT discussion findings,
     - workshop outputs,
     - existing Phase 1 decisions,
     - governance enhancement concepts already documented.

2. **Draft ownership matrix**
   - Pre-populate candidate rows for:
     - CDM domains,
     - NCAIF content/service domains,
     - baseline registry,
     - MVD / Loss & Damage domain,
     - metadata/catalog layer.

3. **Roadmap strawman**
   - Immediate (0–3 months), short-term (3–12 months), future build (12+ months).

### 5.5 What must come from stakeholder engagement in FGD3

- Real internal commitment from DCCE units.
- Named ownership and stewardship decisions.
- Acceptance or rejection of the roadmap and integration logic.
- Political realism: what can actually be asked for in future budget / IT planning.

### 5.6 Target outputs from the stream

1. **Internal execution roadmap** for NCAIF / CRDB integration into the DCCE data system.
2. **Governance ownership matrix** with named roles or at least job titles.
3. **Decision log update** for any newly locked internal decisions.
4. **Budget-justification framing** for what needs post-project investment.

### 5.7 Additional engagement proposed

If FGD3 does not include decision-makers with authority to confirm ownership, add:

- **A short leadership confirmation session** with directors / senior officials.

Reason:

- FGD3 only creates real forward motion if ownership and governance decisions are actually ratified.

---

## 6. What should be learned from desk research vs stakeholder engagement

### 6.1 Desk research / internal synthesis should answer
1. What CRDB has already decided:
	- architecture stance,
	- governance gates,
	- MVP priorities,
	- known digital-landscape constraints.
2. What data/products are already known through interviews and existing artifacts.
3. What the current DCCE data system gaps are.
4. What candidate governance and domain-ownership structures could look like.
5. What the initial workshop journey framing and templates should be.

### 6.2 Stakeholder engagement must answer
- Real scope and design direction of the DCCE IT upgrade.
- Real dataset access constraints and willingness to exchange.
- Real product demand, workflow pain points, and priority bundles.
- Real internal DCCE ownership, stewardship, and approval roles.
- Political feasibility and implementation timing.

### 6.3 Rule of thumb
Use **desk research** to avoid wasting meeting time on known facts.  
Use **engagements** to settle only those issues that require negotiation, confirmation, or commitment.

---

## 7. Additional engagement proposals (only if needed)

These are not automatically required, but should be triggered if evidence is weak:

1. **Follow-up technical session with IT consultant / architect**
   - If April 29 does not reach the actual system designers.

2. **Targeted anchor-agency calls before workshop**
   - If key participants are unlikely to attend or arrive prepared.

3. **Post-workshop clarification interviews**
   - If inventory rows or access conditions are ambiguous.

4. **Leadership confirmation session after FGD3**
   - If ownership and governance are discussed but not ratified.

---

## 8. Recommended artifacts to prepare across the three streams

### Before 2026-04-29
- **CRDB → IT requirements brief (including reference layers, observation envelopes, QC framework)**
- IT discussion question matrix
- Current DCCE digital landscape summary

### Before 2026-05-12
- **Pre-seeded inventory sheets (with QC slots and reference codes)**
- Workshop evidence templates
- Breakout canvases and bridge-board synthesis format

### Before late-May FGD3

- IT + workshop synthesis pack
- **Draft governance ownership matrix (CDM and NCAIF domains)**
- **Draft governance control flows (onboarding, revision, publication)**
- Draft 12-month internal execution roadmap

---

## 9. Practical sequencing recommendation

### Phase A — before IT discussion

- Finalize what CRDB wants from the IT stream.
- Package CRDB’s minimum platform requirements.

### Phase B — between IT discussion and workshop

- Use IT findings to refine workshop prompts:
  - especially around access, metadata, integration, and governance constraints.

### Phase C — between workshop and FGD3

- Convert external findings into DCCE choices:
  - what DCCE must own,
  - what DCCE must request from IT,
  - what DCCE must defer.

This sequence makes the three streams cumulative rather than repetitive.

