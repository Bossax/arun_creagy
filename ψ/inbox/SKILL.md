---

installer: oracle-skills-cli v2.0.10

origin: Arun Creagy — Thai-first writing workflow (voice + citations learned from ψ)

name: writing_th

description: Thai-first writing skill (report/article). Outline-first. Voice + citation rules loaded from ψ; no hardcoded citations.

---

  

# /writing_th — Thai-first Writing (Report / Article)

  

Produce Thai-first writing that follows an outline-first workflow. Writing voice and citation practices are **learned** from Oracle notes under `ψ/` (do not hardcode citation formats in this skill file).

  

## Modes

  

- `--report`  → formal, factual, pattern-driven

- `--article` → narrative flow with clear structure

  

No other modes are supported.

  

## Ground-truth sources (ψ)

  

- Voice profile: `ψ/memory/resonance/writing-style.md`

- Citation guide: `ψ/memory/resonance/citation-style.md`

- Writing samples/patterns (tagged): `ψ/memory/learnings/` (tag: `writing_th`)

  

## Execution handshake (outline-first)

  

1) **Load voice + citation + samples** by running the runner script:

  

```bash

bun writing_th.ts $ARGUMENTS

```

  

2) **Collect required user inputs** (ask if missing):

  

- Topic / objective

- Target audience

- Desired length (approx words/pages) and format constraints

- Must-include points / must-avoid points

  

3) **Return an outline in Thai** (mode-aware) and **stop**.

  

4) Wait for user confirmation.

  

5) Draft the full text in Thai using:

  

- the loaded `voiceProfile`

- the loaded `citationGuide`

- the loaded `samples` as style anchors

  

## Thai-first constraints (always-on)

  

- Thai first; English only for terms/acronyms that do not translate cleanly.

- Do not add parenthetical English glosses.

- Do not use quotation marks for emphasis; use **bold**.

- Avoid invented citations. If a claim needs support but sources are missing, mark as **ต้องการแหล่งอ้างอิง** and proceed without fabricating.

  

## Output constraints

  

- Prefer structured headings and bullet points.

- Keep references/citations consistent with `ψ/memory/resonance/citation-style.md` as loaded by the runner.