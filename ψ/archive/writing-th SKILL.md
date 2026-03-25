---
name: writing_th
description: write reports and articles in Thai language
---
---

# /writing-th [--report | --article]

> Thai-first writing skill. Uses **MCP tools** to retrieve your writing patterns from `ψ/` before drafting.

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

After the user provides the edited version or approves the draft:
1) If the users approves the draft without providing an edited version. It could mean the user will provide it later or you do a good job. Leaning will not take place in this session.
2) Compare the `draft` version with the `edited` version. Identify changes made by the users. Call `oracle_learn` to save the changes learned from the user  to `ψ/memory/learnings/`. End the file name with `writing-th` and the mode (`report` or `article`).
3) If the session updated stable voice/citation rules, append them (append-only) to:
   - `ψ/memory/resonance/writing-style-th.md`
   - `ψ/memory/resonance/citation-style-th.md`

- [x] sd


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

