"""Update Obsidian-style embeds from ![[pic/...]] to ![[incubate/_shared_assets/pic/...]].

This keeps embedded-image references working after migrating ψ/active/pic → ψ/incubate/_shared_assets/pic.

Scope:
- Only *.md under ψ/
- Only replaces the exact prefix '![[pic/'
- Does NOT touch '00_Meta/pic' or other paths.

Run:
  python3 tools/update_pic_links.py
"""

from __future__ import annotations

from pathlib import Path


SRC = "![[pic/"
DST = "![[incubate/_shared_assets/pic/"


def main() -> int:
    root = Path("ψ")
    changed = 0
    files = 0

    for p in root.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # Some md files may not be utf-8; skip rather than corrupt.
            continue

        files += 1
        if SRC not in text:
            continue

        new = text.replace(SRC, DST)
        if new != text:
            p.write_text(new, encoding="utf-8")
            changed += 1

    print(f"Updated embeds in {changed} markdown files (scanned {files}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

