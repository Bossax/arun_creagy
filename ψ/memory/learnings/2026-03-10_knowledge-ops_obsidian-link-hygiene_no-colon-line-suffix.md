# Obsidian link hygiene: avoid vscode-webview links and :line suffixes in vault markdown

**Problem**: Tooling emits links like `vscode-webview://...` or `path.md:1` that break in Obsidian.

## Rule
- In vault markdown files, use plain relative links: `](ψ/.../file.md)`.
- Strip `:N` suffixes and replace any `vscode-webview://...` links.

## Impact
Keeps the vault navigable across editors and prevents silent link rot.


---
*Added via Oracle Learn*
