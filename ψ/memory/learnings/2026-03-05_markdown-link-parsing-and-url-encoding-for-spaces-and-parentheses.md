# Learning — Markdown link parsing + URL encoding (spaces, parentheses, unicode)

When writing repo-internal markdown links, **spaces, parentheses, and unicode punctuation** are the most common sources of silently-broken links.

## What happened

Several artifacts referenced files whose names include:

- spaces (common)
- parentheses `(...)` (very common in versioned artifact names)
- an em dash `—`

Simple regex checks (like `\]\(([^)]+)\)`) falsely “truncate” links at the first `)` and report missing files even when the files exist. This creates noise and increases the chance of shipping broken internal navigation.

## Practical rule

1) **If the destination includes parentheses, URL-encode them**:
   - `(` → `%28`
   - `)` → `%29`

2) For reliability, **validate links with a parser that balances parentheses**, or support the `<...>` destination form and then decode.

3) If you want links to work across multiple markdown renderers, prefer:

- URL-encoded destinations when special characters exist
- consistent relative paths from repo root

## Why this matters

In this repo, many files follow “human title + date/version” naming that naturally includes parentheses. A small investment in encoding + robust checking prevents broken cross-navigation inside decision packs (FGD decks, governance strategies, NCAIF specs).


---
*Added via Oracle Learn*
