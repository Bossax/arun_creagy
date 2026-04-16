---
title: # Learning: /watch failure diagnosis checklist (mosquitto + JS runtime + caption
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-03_watch-failure-diagnosis-mosquitto-js-runtime-captions.md
---

# # Learning: /watch failure diagnosis checklist (mosquitto + JS runtime + caption

# Learning: /watch failure diagnosis checklist (mosquitto + JS runtime + captions mode)

## What happened
The `/watch` run produced artifacts under `output/watch/` but did not yield a real transcript. Diagnostics in [`output/watch/_diag.log`](output/watch/_diag.log:1) show:

- `mosquitto_pub` and `mosquitto_sub` are **missing** → MQTT publish/subscribe steps cannot run.
- yt-dlp warns: **no supported JavaScript runtime found** (only `deno` enabled by default) → YouTube extraction is degraded and may miss formats.
- Subtitles ambiguity:
  - yt-dlp lists **available automatic captions** (many languages)
  - then reports the video **“has no subtitles”** (manual subs absent)

## Pattern
This class of failure looks like “transcription failed,” but it is actually a *multi-dependency preflight* problem. Fixing it is faster if we check dependencies in a strict order and treat “auto captions vs subtitles” as an explicit choice.

## Checklist (run in order)
1) MQTT prerequisites
   - Ensure `mosquitto_pub` and `mosquitto_sub` exist in PATH.
   - If missing: install Mosquitto client tools.

2) yt-dlp extraction prerequisites
   - Ensure yt-dlp has a supported JS runtime configured (`deno`, `node`, `bun`, etc.).
   - If you see “No supported JavaScript runtime could be found,” fix this before debugging anything else.

3) Captions strategy (decide explicitly)
   - Manual subtitles only: expect some videos to fail.
   - Auto-captions allowed: use the yt-dlp mode/flags that download automatic captions when manual subtitles are missing.
   - Treat “Available automatic captions” as success *only if* the workflow consumes auto-captions.

## Evidence
- Primary log: [`output/watch/_diag.log`](output/watch/_diag.log:1)

## Implication for workflow design
Add a structured diagnostic summary:
- Primary blocker (hard fail)
- Secondary warnings
- Suggested fixes

This prevents spending time on caption flags when the actual failure is missing MQTT tooling.

---
*Added via Oracle Learn*
