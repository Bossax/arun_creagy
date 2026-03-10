---
status: raw
tags:
  - AI_prompt
created: 2026-02-23
last_updated: 2026-02-23
AI_prompt: false
AI_output: false
project:
type:
  - prompt
---
# Note Filing Protocol
**Role:** Librarian.
**Task:** Organize the 00_inbox
**Rules:**
1. check `status`
	1. if `evergreen` -> move it to `03_Evergreens/` and add relevant tags  to the the notes
2. check `type`
	1. if `lecture note` -> move it to `03_Evergreens/`
	2. if `literature` -> add relevant tags  and move it to `sources` folder of a project under r `01_Projects/`. If no project match, move to `03_Evergreens/` 
	3. if `note` or `artifact`, check which project under `01_Projects/` it should go. If no project match, learn what the file contains and change the status to `archived` and move it to `99_Archive/` 
	4. if `ai_output` is true or it is `deep_research`, add relevant tags and move it to `05_AI_logs`