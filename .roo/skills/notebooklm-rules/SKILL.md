---
name: notebooklm-rules
description: Strict guardrails for using NotebookLM MCP. Enforces parameter discipline, extraction-only prompts, and source-fidelity gates.
---

# NotebookLM MCP Rules Guardrail

This skill defines the mandatory constraints and workflow for any NotebookLM MCP usage, specifically calls to mcp--notebooklm--ask_question.

## When to use this skill

Use this skill before any NotebookLM MCP work when:

Extracting data, quotes, or evidence from a NotebookLM notebook.

A plan requires reliable, evidence-grade outputs where source fidelity is critical.

## 1. The Iron Rules (System Constraints)

You must follow these rules without exception. Do not attempt to bypass them to save steps.

### A. Parameter Discipline

Never assume a state. Every NotebookLM call requires explicit parameters:

notebook_id: Must be explicitly resolved from project config or user input. No "active notebook" defaults.

session_id: Must be explicitly declared. Reuse a known ID or generate a new one and log it immediately.

browser_options: Do not add or modify variables here unless explicitly commanded by the user.

stealth: Keep this empty. Do not add or modify variables here unless explicitly commanded by the user.

## B. Extraction-Only (No Harmonizing)

NotebookLM is an extraction engine only.

Allowed in prompt: "Extract", "list", "identify", "quote", "cite".

Forbidden in prompt: "Harmonize", "deduplicate", "merge", "QC", "rewrite".

All merging, flattening, and deduplication must happen locally in the repo, not inside NotebookLM.

## C. Source-Fidelity Gate (Fail-Fast)

If a batch targets specific sources (Source-bound):

You must group runs into packets of 1–3 exact NotebookLM titles.

You must resolve local filenames to exact NotebookLM titles before calling the tool.

The Gate: The prompt must instruct NotebookLM to stop and report if any named title is missing or ambiguous. NotebookLM must not substitute nearby literature.

# 2. Execution Workflow

Follow these 5 steps for every NotebookLM extraction task:

### Step 1: Pre-Flight Check

Check that authenticated = true using MCP health tools.

If auth has drifted, trigger a controlled re-auth workflow (clean session, then re-auth). Do not blindly retry.

### Step 2: Parameter & Title Resolution

call `list_notebook` to find the notebook_id.

If this is a source-bound batch, verify you have the exact NotebookLM titles, not just local filenames.

### Step 3: Prompt Construction

Write a concise, extraction-only prompt.

If source-bound, include the exact titles and the "Fail-Fast" instruction.

Keep the expected response short to avoid timeouts.

### Step 4: Execute & Save Verbatim

Call mcp--notebooklm--ask_question with your explicit parameters.

Mandatory: Save the raw NotebookLM response verbatim to a local file immediately upon success. Do not clean or format it in memory before saving.

### Step 5: Local Processing

Once the raw output is saved, you may use standard code tools or local editing to flatten and harmonize the data into the project's canonical registers.

## 3. Failure Protocol

If a call fails, log the issue in ψ/inbox/NotebookLM-MCP-troubleshooting.md and apply these fixes:

Timeout (Request timed out): The prompt is too complex or the output is too long. Simplify the prompt or adjust MCP environment timeouts.

Missing Source / Gate Failure: NotebookLM reported a title is missing. Stop the extraction. Do not proceed until the sources or prompts are corrected.

Auth Error: Run the re-auth workflow. Do not attempt ad hoc retries.