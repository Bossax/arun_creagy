---

installer: oracle-skills-cli v1.5.79

name: notebookLM-research

description: v1.5.79 G-SKLL | AI research prompts → NotebookLM extraction → atomic notes in project source folder

trigger: /notebookLM-research

---

  

# /notebookLM-research — AI research → NotebookLM → atomic notes

  

Translate session-plan research questions into AI research prompts, capture responses, suggest sources for NotebookLM, then extract atomic notes into the project `source` folder.

  

## Usage

  

```

/notebookLM-research <session-plan-path> [--template <path>] [--source <path>]

```

  

Defaults:

- `--template`: `src/00_Meta/template/Deep research.md`

- `--source`: derived from the session plan (first project path → `<project>/source`)

  

## Session Plan Schema (append if missing)

  

Append these sections to the end of the session plan file if they do not exist:

  

```

## Research Questions

  

## AI Research Prompts

### Deep Research

```text

...

```

  

### Consensus

```text

...

```

  

## AI Research Responses

```text

...

```

  

## NotebookLM Prompt

```text

...

```

  

## NotebookLM Session Link

- <notebooklm_share_url>

```

  

## Workflow (gated)

  

### 1) Preflight

1. Read the session plan file. If missing, ask the user for the correct path.

2. Ensure the schema sections above exist; append if missing.

3. If **Research Questions** is empty, ask the user to provide them and insert into the plan.

  

### 2) Resolve project `source` folder

1. Scan the session plan for the **first** project path containing `01_Projects/<project>/...` or `src/01_Projects/<project>/...`.

2. Normalize to `src/01_Projects/<project>` as the project root.

3. Set `source` folder to `<project-root>/source`.

4. If no project path is found, **ask the user** to provide the `source` folder path.

  

### 3) Generate AI research prompts

1. Convert Research Questions into two prompts:

   - **Deep Research prompt** (for broad screening + synthesis)

   - **Consensus prompt** (for peer‑reviewed literature focus)

2. Write them into **AI Research Prompts** section.

  

**Prompt guidance (generate actual prompts from the questions):**

- Ask for screened, citeable sources.

- Require quotes with citations and a short bibliography.

- Return concise findings per question.

  

### 4) Gate — user runs AI research

1. Ask the user to run the Deep Research and Consensus prompts in their tools.

2. Ask the user to paste the responses.

3. Insert responses verbatim into **AI Research Responses** section.

  

### 5) Suggest sources for NotebookLM

1. Read **AI Research Responses** and propose the most relevant sources to upload to NotebookLM.

2. Ask the user to upload those sources.

3. Confirm upload is complete and ask for the NotebookLM share link.

4. Save link to **NotebookLM Session Link** section.

  

### 6) Assemble NotebookLM prompt

1. If **NotebookLM Prompt** already has content, use it as-is.

2. If empty, generate a prompt using:

   - Research Questions

   - Atomic note template (from `--template`)

   - Output format rules (below)

3. Save the prompt into **NotebookLM Prompt** section.

  

**NotebookLM output format (must be enforced in prompt):**

- Return one atomic note per source finding.

- Each note must be wrapped in `[NOTE]` and `[/NOTE]` tags.

- Each note must include a **Dominant question:** line (used for filename).

- Include citations/quotes inside the note body.

  

Example output block:

```

[NOTE]

Dominant question: What are the key dimensions used in urban resilience frameworks?

Title: Dimensions in Urban Resilience Frameworks

Tags: urban-resilience; governance; indicators

Citation: Author, Year, Title, Journal/Publisher, URL

  

Body:

- Key finding 1 (with quote + citation)

- Key finding 2 (with quote + citation)

[/NOTE]

```

  

### 7) Run NotebookLM via MCP

1. Use `mcp--notebooklm--ask_question` with the NotebookLM share link and the NotebookLM Prompt text.

2. Capture the response text.

  

### 8) Write atomic notes

1. Split response by `[NOTE]`...`[/NOTE]` blocks. If none, ask the user to rerun with the required format.

2. For each block:

   - Extract **Dominant question** → slugify for filename.

   - Use the template frontmatter from `--template` as the base.

   - Fill:

     - `created` and `last_updated` with today’s date

     - `project` from session plan frontmatter if available

     - `source` with NotebookLM share link

     - `tags` if provided in the note (optional)

   - Body = remainder of the note content (flexible structure).

3. Write each note to `<project-root>/source/<dominant-question-slug>.md`.

4. **Do not overwrite existing files**. If a filename exists, append `-2`, `-3`, ... until unique.

  

## Notes

- Use `ask_followup_question` for missing user inputs (research questions, responses, or NotebookLM link).

- Keep all user-provided responses verbatim in the session plan for traceability.