---
name: writing-th
description: write reports and articles in Thai language. use when user says "write a report in Thai", "create draft in Thai", "write in Thai"
---

# /writing-th [--report | --article]

> Thai-first writing skill. Uses **MCP tools** to retrieve your writing patterns from `ψ/` before drafting.

## Step 0: Decide whether this is a report or article
If user does not specify what type of write-up it is, use the report mode (default).

## Step 1: Agent memory retrieval (MCP)

Hard rule: **Do not use Oracle HTTP APIs** (no `/api/search`, `/api/file`, etc.) for memory.

1.  Call `oracle_concepts` to see available concept tags (helps you choose precise queries).

2. Call `oracle_search` with targeted queries to retrieve relevant documents:
	- `ψ/memory/resonance/writing-style-th.md`
	- `ψ/memory/resonance/citation-style-th.md`
	- `ψ/memory/learnings/*.md` with naming `writing-th` with corresponding mode (`report` , `article`)
	

If the resonance files are missing, proceed using the **Thai-first constraints** below and ask the user for writing samples and/or citation preference so the session can create the first seed patterns.

## Step 2: User handshake (minimal inputs)

Ask for
1) **Writing Plan**:  a markdown file detailing reference files and plan

If the plan exists, ask only for missing inputs:
1) **Mode**: `--report` or `--article`
2) **หัวข้อ + วัตถุประสงค์** (เขียนเรื่องอะไร และต้องการให้ผู้อ่านทำ/ตัดสินใจอะไร)
3) **ผู้อ่าน** (หน่วยงาน/กลุ่มเป้าหมาย)
4) **ความยาวเป้าหมาย** (หน้า/คำ)
5) **ข้อจำกัด** (must-include / must-avoid / deadline)
6) **แหล่งข้อมูล** (ถ้ามี): ไฟล์/ลิงก์/ข้อความที่ให้มาเท่านั้นคือ ground truth

## Step 3: Runner execution (formatting only; optional)

Runner is allowed **only** for formatting or transforming external inputs.

- If you run anything, it may only be:
  - `bun writing-th.ts "$ARGUMENTS"`
- The runner must **not** query Oracle memory (no MCP calls inside it; no HTTP fetch to Oracle).

If no external formatting is needed, skip the runner entirely.

## Step 4: Outline first, then draft

1) Produce a numbered **โครงร่าง** in Thai. Append to the writing plan file.
2) **STOP** and wait for explicit user confirmation.
3) After confirmation, write the full draft. The draft will be put into project output folder. The name must end with `draft`
4) Ask for the user to review and edit by copying the draft and replace `draft` with `edited`
## Step 5: Evolution (learn-back)

> Goal: keep **writing execution** and **style learning** conceptually separate, so learning can also be triggered later (for example from `/rrr`).

After the user provides the edited version or approves the draft:

1) If the user approves the draft without providing an edited version:
   - Treat this as "no learning yet" for this session (the user may still edit later).
   - Do **not** write a learning file in this step.

2) If the user provides an edited version:
   - Ensure there is a clear `draft` vs `edited` pair for this piece (same base name, different suffixes):
     - `...-draft.md`
     - `...-edited.md`
   - Compare the `draft` and `edited` versions focusing on:
     - **Word choice changes** — specific Thai word preferences, recurring replacements, register shifts.
     - **Semantic arrangement changes** — how concepts are reordered or rephrased to sound more natural for the human; reason about why the human rearranged the structure.
   - Summarize what changed into a short, human-readable note (no diff dump), grouped by:
     - "Word choice and phrasing"
     - "Semantic/structure changes"
   - Call `oracle_learn` with these distilled patterns and save them into `ψ/memory/learnings/` using a discoverable naming convention:
     - `ψ/memory/learnings/YYYY-MM-DD_writing-th-<mode>-learn.md` where `<mode>` is `report` or `article`.

3) If the session updated **stable** voice/citation rules (not just one-off edits), append them (append-only) to:
   - `ψ/memory/resonance/writing-style-th.md`
   - `ψ/memory/resonance/citation-style-th.md`

4) When a separate learning skill such as `/writing-th-learn` is available, prefer to:
   - Use `/writing-th` for planning, outlining, and drafting.
   - Use `/writing-th-learn` (potentially triggered from `/rrr`) to run the detailed draft-vs-edited comparison and write the learning files described above.

---

## Modes (required)

Exactly one mode flag must be provided:

- `--report` — รายงานทางการสำหรับหน่วยงานรัฐ/NGO (ข้อเท็จจริง ชัดเจน เชิงข้อเสนอ)
- `--article` — บทความยาวที่อ่านง่าย มีโครงสร้าง และมีจังหวะการเล่าเรื่อง

No other modes are supported.

## Thai-first constraints (always-on)

- ใช้ **ภาษาไทยเป็นหลัก**
- ใช้ภาษาอังกฤษเฉพาะคำทับศัพท์ ตัวย่อ ชื่อองค์กร/มาตรฐาน/ชื่อเฉพาะที่จำเป็น
- **หลีกเลี่ยงวงเล็บพร้อมคำแปลอังกฤษประกบ** (อย่าเขียนไทย (อังกฤษ) เพื่อแปลซ้ำ)
- หลีกเลี่ยงการใช้เครื่องหมายอัญประกาศเพื่อเน้น; ใช้ **ตัวหนา** เพื่อเน้นแทน
- ภาษาตรงไปตรงมา อ่านเป็นมนุษย์ ไม่เติมคำฟุ่มเฟือย

## Grounding + citations

- ห้ามแต่งแหล่งอ้างอิง
- หากมีแหล่งข้อมูลจากผู้ใช้หรือจาก `ψ/` ที่ดึงมาด้วย MCP ให้ใช้อ้างอิงตาม `citation-style-th.md` (ถ้ามี).
- อ้างอิงเฉพาะชื่อผุ้แต่ง ไม่ใช่ชื่อไฟล์ `ψ/`
- หากไม่มีแหล่งข้อมูล ให้เขียนแบบ “ข้อเสนอแนะทั่วไป” และระบุความไม่แน่นอนอย่างเหมาะสม

