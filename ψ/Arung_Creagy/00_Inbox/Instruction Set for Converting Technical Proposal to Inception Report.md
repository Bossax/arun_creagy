---
type: ai_output
status:
  - archived
tags:
  - Productivity
capture_date: 2025-11-10
origin_prompt: combine [[AI Instruction Set (Optimized for LLM Capabilities)]] and [[Instructions for AI_Converting Technical Proposal to Inception Report]] to generate this file
relevance_to: "[[Human Post-Processing Instruction Set for Creating an Inception Report]]"
---
## Purpose

Transform a **technical proposal** into a **draft inception report** by preserving **90% of the original content** (language, tone, structure, and technical detail) while updating **contextual information** (timeline, deliverables, and minor plan adjustments) to reflect confirmed project implementation.

---

## 1. Overall Objective

Produce a complete inception report draft that:

- **Retains 90% plus of the technical proposal content verbatim** (methodology, approach, technical descriptions)
- **Updates 5-10%** with confirmed timelines, specific dates, and minor adjustments
- Confirms shared understanding through minimal contextual refinements
- Maintains the original document's professional tone and structure

**LLM should focus on accurate content preservation and precise timeline conversion**, while **leaving layout, formatting, and final review to the human editor.**

---

## 2. Document Structure to Generate

The AI must produce a full-text inception report with **identical structure** to the technical proposal:

### **Executive Summary**

- **RETAIN**: Most content from proposal executive summary
- **UPDATE**:
    - Add specific confirmed dates where proposal had placeholders
    - Update duration if confirmed (e.g., "26 months")
    - Adjust any timeline references to reflect actual start date

### **Chapter 1: Concept and Implementation Plan**

**1.1 Objective**

- **RETAIN**: Entire section verbatim from proposal
- **UPDATE**: None (unless specific scope changes confirmed)

**1.2 Technical Concept, Approach and Methodology**

- **RETAIN**: All methodology content verbatim
- **UPDATE**: None (technical approach remains as proposed)

**1.3 Conceptual Foundation**

- **RETAIN**: All content verbatim
- **UPDATE**: None

**1.4 Task-Specific Approach and Methodology**

- **RETAIN**: All technical descriptions, phases, methodologies verbatim
- **UPDATE**: None (unless specific tool/method changes confirmed)

**1.5 Workplan**

- **RETAIN**: Task descriptions and structure verbatim
- **UPDATE**:
    - Convert "Month X" to specific calendar dates (e.g., "November 2025")
    - Update Q1/Q2/Q3/Q4 references to actual months
    - Adjust any timeline bars/tables to reflect confirmed start date
    - Update milestone dates if adjusted during contract negotiation

**1.6 Deliverables**

- **RETAIN**: Deliverable descriptions verbatim
- **UPDATE**:
    - Confirm/adjust specific submission dates
    - Update "by [date]" references to agreed dates
    - Adjust review periods if modified

**1.7 Quality Assurance and Risk Mitigation** _(if in proposal)_

- **RETAIN**: All QA procedures and risk descriptions verbatim
- **UPDATE**: None (unless specific protocols adjusted)

### **References**

- **RETAIN**: All references verbatim
- **UPDATE**: Add any new references if required

### **Appendices**

- **RETAIN**: All technical appendices verbatim
- **UPDATE**: None (technical specifications remain as proposed)

---

## 3. What to REMOVE

### **Delete These Sections Entirely:**

```
❌ "Qualifications of the Service Provider"
❌ Company profile, mission, and organizational description
❌ Summary of experiences and track record
❌ Organizational commitment to sustainability
❌ Evidence supporting qualifications
❌ Reference list of high-value contracts
❌ All supporting evidence appendices:
   - Certificate of business registration
   - Tax registration
   - Written self-declaration
   - Audited financial reports
   - Satisfactory performance certificates
   - CVs of key team members (full versions)
   - Track record documentation
   - Legal entity certifications
   - Any other capability-proving documents
```

### **Simplify Team Section:**

- **REMOVE**: Full CVs with employment history, publications, detailed qualifications
- **RETAIN** (if needed): Simple team structure with names, roles, and brief descriptions only
- Place in main body, not as appendix

---

## 4. Timeline Conversion Rules

### **Convert Proposal Timeline to Actual Dates:**

|Proposal Format|Inception Report Format|
|---|---|
|"Month 1-3"|"November 2025 - January 2026"|
|"Q1 2026"|"January - March 2026"|
|"By end of Month 6"|"By 30 April 2026"|
|Timeline bars showing months|Timeline bars showing calendar months|
|"Duration: X months"|"Duration: X months (Nov 2025 - Dec 2027)"|

### **Rules:**

1. Use the confirmed start date from the contract
2. Calculate actual calendar months/dates for all milestones
3. Keep the same duration and sequencing
4. Update deliverable dates to specific calendar dates
5. Preserve all task dependencies and relationships

---

## 5. Minor Adjustments (The 10%)

### **Allowed Minor Updates:**

1. **Timeline/Dates** (primary changes):
    
    - Convert relative dates to calendar dates
    - Adjust milestone dates if contract modified them
    - Update deliverable submission dates
2. **Scope Clarifications** (only if confirmed):
    
    - Add brief clarifications from inception meeting
    - Note any agreed scope adjustments
    - Update participant numbers if changed (e.g., "up to 100 participants")
3. **Contact Information**:
    
    - Update project contact details if changed
    - Confirm submission addresses
4. **Document Metadata**:
    
    - Change title from "Technical Proposal" to "Inception Report"
    - Update submission date
    - Update document version/status

### **DO NOT Change:**

- Technical methodology or approach
- Task descriptions or phases
- Quality assurance procedures
- Tools and technologies
- Team structure or roles
- Technical specifications
- Appendix content (except removing capability proofs)

---

## 6. Content Preservation Rules

|Element|Action|
|---|---|
|**Technical descriptions**|Copy verbatim - 100%|
|**Methodology sections**|Copy verbatim - 100%|
|**Task phases and steps**|Copy verbatim - 100%|
|**Tools and techniques**|Copy verbatim - 100%|
|**Quality assurance**|Copy verbatim - 100%|
|**Risk mitigation**|Copy verbatim - 100%|
|**Deliverable descriptions**|Copy verbatim - 95%, update dates only|
|**Timeline/schedule**|Copy structure, update dates - 70% preserved|
|**Team structure**|Simplify but keep roles - 60% preserved|
|**Capability sections**|Remove entirely - 0%|

---

## 7. Formatting Notes

**AI should:**

- Preserve all section numbering from proposal
- Retain all technical tables (describe if can't format)
- Keep all figure references (note: "[Figure X as in proposal]")
- Maintain paragraph structure and flow
- Preserve bullet points and lists
- Keep all technical terminology exactly as written

**AI should NOT:**

- Rephrase technical content
- Simplify methodology descriptions
- Consolidate sections
- Change heading structure
- Alter technical specifications

---

## 8. Quality Self-Check (for AI)

Before finalizing the draft, verify that:

**Content Preservation:**

- Technical methodology copied verbatim (90%+ match)
- Task descriptions unchanged from proposal
- Tools, techniques, and approaches identical
- Quality assurance section preserved
- Risk mitigation content retained

**Appropriate Updates:**

- All timeline references converted to calendar dates
- Deliverable dates reflect specific agreed dates
- Start date and end date clearly stated
- Milestone dates calculated correctly

**Appropriate Removals:**

- All company qualification sections removed
- CVs and track record removed
- Capability-proving appendices removed
- Marketing/persuasive language removed (if any)

**Structure:**

- Section numbering matches proposal
- All technical appendices retained
- Flow and organization preserved
- Cross-references still valid

**Validation:**

- A technical expert would recognize 90%+ of the content
- Timeline is internally consistent
- All task dependencies preserved
- Deliverable schedule is realistic

---

## 9. Output Format

The AI should produce:

1. **Full narrative text** preserving original wording
2. **Timeline tables** with updated calendar dates (describe if can't format)
3. **Deliverable tables** with confirmed dates
4. **All technical appendices** as in proposal
5. **Placeholder notes** only for:
    - Visual formatting needs
    - Figure recreation
    - Complex table layouts

---

## 10. Special Instructions for Specific Sections

### **Workplan/Timeline Section:**

```
ACTION: Update dates only
PRESERVE: All task descriptions, sequences, dependencies
UPDATE: "Nov 2025" instead of "Month 1"
KEEP: Duration of each task unchanged
VERIFY: Total project duration remains consistent
```

### **Deliverables Section:**

```
ACTION: Update submission dates
PRESERVE: All deliverable descriptions word-for-word
UPDATE: "15 November 2025" instead of "Month 2"
KEEP: Review and approval process unchanged
```

### **Methodology Sections:**

```
ACTION: Copy 100% verbatim
PRESERVE: Every word, phrase, and technical detail
UPDATE: None
```

### **Team Section:**

```
ACTION: Simplify significantly
KEEP: Names, roles, key responsibilities (2-3 lines max per person)
REMOVE: Full employment history, publications, detailed qualifications
LOCATION: Main body, not appendix
```

---

## Summary Principle

**The inception report is the technical proposal with:**

- **90% identical content** (all technical, methodological, and approach sections)
- **Timelines converted** from relative to calendar dates
- **Capability/qualification sections removed**
- **Structure and flow preserved**

Think of it as: **Same technical document + Updated timeline - Capability proofs = Inception Report**

The inception report confirms "This is exactly what we proposed, and here are the specific dates we'll execute it."