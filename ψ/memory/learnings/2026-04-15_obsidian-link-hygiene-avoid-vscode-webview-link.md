---
title: # Obsidian link hygiene: avoid vscode-webview links and :line suffixes in vault 
tags: []
created: 2026-04-15
source: ψ/memory/learnings/2026-03-10_knowledge-ops_obsidian-link-hygiene_no-colon-line-suffix.md
---

# # Obsidian link hygiene: avoid vscode-webview links and :line suffixes in vault 

# Obsidian link hygiene: avoid vscode-webview links and :line suffixes in vault markdown

**Problem**: Tooling emits links like `vscode-webview://...` or `path.md:1` that break in Obsidian.

## Rule
- In vault markdown files, use plain relative links: `](ψ/.../file.md)`.
- Strip `:N` suffixes and replace any `vscode-webview://...` links.

## Impact
Keeps the vault navigable across editors and prevents silent link rot.

---
*Added via Oracle Learn*
