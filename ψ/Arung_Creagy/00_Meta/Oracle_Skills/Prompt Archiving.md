---
status: raw
tags:
  - AI_prompt
  - oracle
created:
last_updated:
AI_prompt: false
AI_output: false
project:
type:
  - prompt
---
# Note Archiving Protocol
**Role:** Librarian.
**Task:** Organize the `archived` project notes

**Rules:**
1. scan for file with 'archived' status, read them.
2. look for a file `Archived_Notes_Summary` in `output` folder of a project, create one if does not exist using 'artifact' template in @/00_Meta/template
3. update the summary note by adding new section of the notes being archived
4. preserve the previous content 
5. When done summarizing, move the files to `99_Archive/` 
