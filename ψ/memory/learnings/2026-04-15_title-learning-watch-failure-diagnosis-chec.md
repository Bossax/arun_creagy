---
title: ---
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-03_learning-watch-failure-diagnosis-checklist-mosq.md
---

# ---

---
title: Learning: /watch failure diagnosis checklist (mosquitto + JS runtime + captions 
tags: [watch, diagnostics, yt-dlp, mqtt, mosquitto, javascript-runtime, captions, retrospective]
created: 2026-03-03
source: rrr: Knowledge_System
---

# Learning: /watch failure diagnosis checklist (mosquitto + JS runtime + captions 

Learning: /watch failure diagnosis checklist (mosquitto + JS runtime + captions mode)

What happened:
- /watch produced artifacts under output/watch/ but did not yield a real transcript.
- Diagnostics show mosquitto_pub and mosquitto_sub are missing → MQTT publish/subscribe steps cannot run.
- yt-dlp warns: no supported JavaScript runtime found (only deno enabled by default) → YouTube extraction is degraded and may miss formats.
- Captions ambiguity: automatic captions are available, but the video reports “has no subtitles” (manual subs absent).

Pattern:
This looks like “transcription failed,” but it’s actually a multi-dependency preflight problem. Fix faster by checking in order and making captions mode explicit.

Checklist (run in order):
1) MQTT prerequisites: ensure mosquitto_pub/mosquitto_sub exist in PATH.
2) yt-dlp extraction prerequisites: configure a supported JS runtime (deno/node/bun/etc.) before debugging other layers.
3) Captions strategy: decide whether auto captions are allowed; treat “available automatic captions” as success only if the workflow consumes them.

Evidence:
- Primary log at output/watch/_diag.log

Workflow implication:
Add structured diagnostic summary: primary blocker, secondary warnings, suggested fixes. Prevents chasing caption flags when the actual issue is missing MQTT tooling.

---
*Added via Oracle Learn*

---
*Added via Oracle Learn*
