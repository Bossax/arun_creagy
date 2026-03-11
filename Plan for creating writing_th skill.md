

Plan is below.....
=====================================================
### 1. Create `SKILL.md` 

Create `SKILL.md` to handle conditional logic based on the arguments provided.

```markdown
---
name: writing_th
description: Multipurpose Thai/English writing skill. Supports --report, --content, and --article tones.
---

# /writing_th - Contextual Thai/English Writing

## Step 1: Establish Oracle Identity
1. Call `oracle_search` for "writing style voice characteristics".
2. Identify the requested tone from `$ARGUMENTS`.

## Step 1: Execute Pattern Matcher
```bash
date "+🕐 %H:%M %Z (%A %d %B %Y)"
bun scripts/main.ts "$ARGUMENTS"

```

## Step 2: Generation Constraints

Apply the core **Voice Characteristics** (Direct, Concise, Technical when needed) plus the specific tone override:

(this information could be part of oracle remebered pattern in learnings?)


```

### 2. Strategic Implementation in `scripts/main.ts`

```typescript
// scripts/main.ts
const args = process.argv.slice(2).join(" ");

if (args.includes('--report')) {
  console.log("MODE: Formal Report. Focus on facts and patterns.");
} else if (args.includes('--content')) {
  console.log("MODE: Social Content. Focus on engagement and authentic voice.");
} else if (args.includes('--article')) {
  console.log("MODE: Informal Article. Focus on narrative flow.");
} else {
  console.log("MODE: Default General Writing.");
}

```

### 3. Why This Works (The Consultant's View)

* **Centralized Patterns**: Instead of three separate skills, you have one "Brain" for writing. This makes it easier for the Oracle to observe how you switch between tones (Principle 2: Patterns Over Intentions).
* **Global Scalability**: Because this is a global skill (`-g`), you can use `/writing_th --report` in a coding repo and `/writing_th --content` in a personal blog repo without changing your setup.
* **Append-Only Growth**: Every time you use a different flag, the `oracle_learn` tool adds a new pattern to your `ψ/memory/learnings/`, making the Oracle better at "mirroring reality" for that specific tone next time.



I will extract writing style from a set of pdf via notebooklm

then, I will keep info files

1. เก็บเป็น "Identity" ใน ψ/memory/resonance/
ส่วนนี้ใช้สำหรับเก็บข้อมูลที่เป็น "ตัวตน" หรือหลักเกณฑ์พื้นฐานที่ไม่เปลี่ยนแปลงบ่อย:

อัปเดตไฟล์ writing-style.md: นำข้อมูลที่สกัดได้ (เช่น Voice Characteristics, Language Mix) ไปเพิ่มในไฟล์ .claude/knowledge/writing-style.md

ใช้รูปแบบ Append-only: ตามหลักปรัชญาของ Oracle หากมีการปรับปรุงสไตล์ใหม่ ให้ใช้วิธีเพิ่มข้อมูลต่อท้ายพร้อมระบุ Timestamp แทนการลบของเก่า เพื่อรักษาบริบทในอดีต

โครงสร้างข้อมูล: ควรจัดหมวดหมู่ตามที่คุณออกแบบไว้ เช่น แยกส่วนของ --report, --content, และ --article ให้ชัดเจนเพื่อให้ AI ค้นหาได้ง่าย

2. เก็บเป็น "Patterns" ใน ψ/memory/learnings/
ส่วนนี้ใช้สำหรับเก็บรูปแบบพฤติกรรมการเขียนที่คุณได้เรียนรู้เพิ่มเติมจากการทำงานจริง:

ใช้เครื่องมือ oracle_learn: เมื่อคุณได้ผลลัพธ์การสกัดสไตล์ที่น่าพอใจจาก NotebookLM ให้ใช้ Tool oracle_learn เพื่อบันทึกข้อมูลนั้นลงในโฟลเดอร์ learnings/

เน้นพฤติกรรม (Patterns Over Intentions): แทนที่จะบันทึกแค่ "อยากเขียนแบบไหน" ให้บันทึก "ตัวอย่างประโยคจริง" ที่ NotebookLM สกัดได้ เพื่อให้ Oracle ใช้เป็น Mirror ในการเลียนแบบพฤติกรรมการเขียนจริง

End of plan...................

---

Your response
Below is a picky review of your plan with concrete improvements.

## What is strong
- Single entry skill with mode flags keeps the mental model simple.
- You are planning to externalize voice and citation patterns into memory, which matches the requirement to avoid hardcoding citations in [`/.roo/skills/writing_th/SKILL.md`](.roo/skills/writing_th/SKILL.md:1).

## Issues and improvements

1) **Flag mismatch with the agreed scope**
- You added `--content`, but the agreed modes were `--report` and `--article` only. Either remove `--content` or formally expand the spec and input prompts for it.

2) **Duplicate step numbering and unclear execution order**
- You have two Step 1 sections. This will confuse execution flow. Fix the order and naming so it is linear and unambiguous.

3) **Skill file should not embed discovery logic**
- `SKILL.md` is instruction text, not a logic engine. Avoid embedding tool calls like oracle search inside the skill body. Put discovery in the TypeScript runner and keep [`/.roo/skills/writing_th/SKILL.md`](.roo/skills/writing_th/SKILL.md:1) focused on required inputs and constraints.

4) **`scripts/main.ts` is only printing mode**
- The current `scripts/main.ts` does not call Oracle MCP or collect writing samples. It must be upgraded to a real data collector.
- Suggested structure for [`/.roo/skills/writing_th/writing_th.ts`](.roo/skills/writing_th/writing_th.ts:1):
  - call Oracle search to find style notes and citation samples
  - read the matched files
  - return a structured object like `{ samples, citationGuide, voiceProfile }`

5) **Location mismatch for knowledge files**
- You referenced `.claude/knowledge/writing-style.md`, but this repo uses `ψ/` as the knowledge tree. Keep identity and voice files in `ψ` and avoid introducing a new root.
- Proposed canonical file: [`/ψ/memory/resonance/writing-style.md`](ψ/memory/resonance/writing-style.md:1)

6) **Citations must be learned, not hardcoded**
- Do not place citation rules directly in [`/.roo/skills/writing_th/SKILL.md`](.roo/skills/writing_th/SKILL.md:1).
- Instead, your extraction step should output a normalized note in `ψ`, then the TypeScript runner reads that note. This keeps the skill declarative and the logic in code.

7) **Constraints required by you are not captured in the plan**
Add the explicit language constraints to [`/.roo/skills/writing_th/SKILL.md`](.roo/skills/writing_th/SKILL.md:1):
- Thai first, English only for terms or acronyms
- no quote marks for emphasis, use **bold** instead
- avoid parenthetical English glosses
- outline first, wait for confirmation before drafting

8) **Identity vs patterns should be separated**
- Identity belongs in resonance, patterns belong in learnings. Your plan describes this, but you also want structured sub‑sections for each mode. Make it explicit in the file templates so the runner can parse them deterministically.
- Example targets:
  - Identity: [`/ψ/memory/resonance/writing-style.md`](ψ/memory/resonance/writing-style.md:1)
  - Patterns: [`/ψ/memory/learnings/`](ψ/memory/learnings/:1)

9) **Global skill vs repo skill**
- If the goal is global availability, implement under the global skills directory and register in the global registry, not inside the repo.
- If you still want a repo‑local skill, do not call it global in the plan. Pick one and align the install path and registry.

## Minimal improved structure
- [`/.roo/skills/writing_th/SKILL.md`](.roo/skills/writing_th/SKILL.md:1):
  - describes `--report` and `--article`
  - lists required inputs
  - lists constraints
  - says citations and voice are loaded from Oracle samples
- [`/.roo/skills/writing_th/writing_th.ts`](.roo/skills/writing_th/writing_th.ts:1):
  - calls Oracle MCP or HTTP API to search and read style notes
  - builds a `voiceProfile` and `citationGuide`
  - returns data for the skill execution
- Data store:
  - [`/ψ/memory/resonance/writing-style.md`](ψ/memory/resonance/writing-style.md:1)
  - [`/ψ/memory/learnings/`](ψ/memory/learnings/:1)

This keeps the skill clean, the citations learned, and the execution deterministic.

---
My feedback on Issues and improvements......
1. remove --conten for now
2. fix the order. renumerate 
3. agreee with SKILL.md modification
4. agree with ts file design
5. the file structure starts with ψ
6. citation should be learned in the same process as writing style
7. agree
8. . agree 
9. . agree


---

# Plan for /writing_th (updated + renumbered)

1. Confirm scope and location
   - Modes: `--report` and `--article` only. No `--content`.
   - Repo-local skill under [`/.roo/skills/writing_th/SKILL.md`](.roo/skills/writing_th/SKILL.md:1) with a TypeScript runner; do not describe it as global.

2. Define SKILL.md scope and inputs (declarative only)
   - [`/.roo/skills/writing_th/SKILL.md`](.roo/skills/writing_th/SKILL.md:1) describes: purpose, available flags, required inputs from user, and the output handshake.
   - Keep SKILL.md free of discovery logic or tool calls; execution logic lives in the TS runner.

3. Capture Thai-first constraints in SKILL.md
   - Thai first; English only for terms/acronyms.
   - No quote marks for emphasis; use **bold**.
   - Avoid parenthetical English glosses.
   - Outline first; wait for confirmation before drafting.

4. Establish data sources and storage in ψ
   - Identity/voice profile stored in [`/ψ/memory/resonance/writing-style.md`](ψ/memory/resonance/writing-style.md:1).
   - Patterns/examples stored in [`/ψ/memory/learnings/`](ψ/memory/learnings/:1) with tag `writing_th`.
   - Both sources are append-only to preserve history.

5. Define TS runner responsibilities
   - Implement runner (e.g., [`/.roo/skills/writing_th/writing_th.ts`](.roo/skills/writing_th/writing_th.ts:1)) to:
     - Parse flags and requested tone.
     - Query Oracle for writing_th sources (resonance + learnings).
     - Read matched files and assemble `{ voiceProfile, citationGuide, samples }` for the skill execution.

6. Specify Oracle HTTP API usage
   - Use `/api/search` to find relevant `writing_th` notes in ψ.
   - Use `/api/file` to fetch the contents for processing.
   - Keep citations learned from notes; do not hardcode in SKILL.md.

7. Define mode-aware response flow
   - For `--report`: formal, factual, pattern-driven output.
   - For `--article`: narrative flow with clarity and structure.
   - Always follow Thai-first constraints and require outline confirmation before drafting.

8. Validation checklist before implementation
   - SKILL.md is declarative and constraint-focused.
   - TS runner performs discovery + assembly.
   - Data sources are only in ψ (resonance + learnings tagged `writing_th`).
   - No `--content` references remain.
   - Output flow enforces outline-first confirmation step.