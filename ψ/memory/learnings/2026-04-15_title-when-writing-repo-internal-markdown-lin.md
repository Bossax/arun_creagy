---
title: ---
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-05_when-writing-repo-internal-markdown-links-spaces.md
---

# ---

---
title: When writing repo-internal markdown links, spaces/parentheses/unicode punctuatio
tags: [markdown, linking, documentation, tooling, quality]
created: 2026-03-05
source: rrr: Knowledge_System
---

# When writing repo-internal markdown links, spaces/parentheses/unicode punctuatio

When writing repo-internal markdown links, spaces/parentheses/unicode punctuation frequently break navigation across renderers. Regex link extraction like `\]\(([^)]+)\)` is unreliable because it truncates at the first `)`. Practical rule: URL-encode parentheses in destinations (`(`→`%28`, `)`→`%29`) and validate links with a parser that balances parentheses (or supports `<...>` destinations + decode) before shipping stakeholder-facing decision packs.

---
*Added via Oracle Learn*

---
*Added via Oracle Learn*
