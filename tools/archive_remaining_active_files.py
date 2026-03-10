"""Archive any remaining files under ψ/active/ into ψ/archive/legacy-active/.

Purpose
-------
After the main migration, ψ/active may still contain Windows metadata files
like desktop.ini. Rather than deleting them, we preserve them by moving into
archive, logging each move.

Run
---
  python tools/archive_remaining_active_files.py
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
import shutil


BKK = timezone(timedelta(hours=7))


def hhmm_bkk() -> str:
    return datetime.now(BKK).strftime("%H:%M")


def main() -> int:
    active = Path("ψ/active")
    archive_root = Path("ψ/archive/legacy-active")
    log = Path("ψ/archive/migration-log.md")

    if not active.exists():
        print("ψ/active missing; nothing to archive")
        return 0

    archive_root.mkdir(parents=True, exist_ok=True)
    log.parent.mkdir(parents=True, exist_ok=True)

    files = [p for p in active.rglob("*") if p.is_file()]
    if not files:
        print("No files remain under ψ/active")
        return 0

    t = hhmm_bkk()
    moved = 0
    with log.open("a", encoding="utf-8") as f:
        for src in sorted(files, key=lambda p: p.as_posix().lower()):
            rel = src.relative_to(active)
            dest = archive_root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)

            if dest.exists():
                # Avoid overwrite
                stem, suffix = dest.stem, dest.suffix
                i = 2
                while True:
                    alt = dest.with_name(f"{stem}__dup{i}{suffix}")
                    if not alt.exists():
                        dest = alt
                        break
                    i += 1

            shutil.move(str(src), str(dest))
            moved += 1
            f.write(
                f"| {t} | move | {src.as_posix()} | {dest.as_posix()} | archive remaining ψ/active files before deleting folder |\n"
            )

    print(f"Archived {moved} files into {archive_root.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

