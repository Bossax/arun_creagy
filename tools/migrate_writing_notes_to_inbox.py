"""Migrate ψ/writing/*/notes into ψ/inbox triage.

Rationale
- Notes are treated as "temp thoughts" and should enter the Inbox queue for triage.
- We *move* (not copy) to avoid duplicated silos, and we log every move.
- We do NOT delete ψ/writing; the project folders remain.

Run:
  python3 tools/migrate_writing_notes_to_inbox.py
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
import shutil


BKK = timezone(timedelta(hours=7))


@dataclass(frozen=True)
class ProjectSpec:
    src_folder: str
    label: str


PROJECTS: list[ProjectSpec] = [
    ProjectSpec("2025-11_DCCE-CRDB", "DCCE-CRDB"),
    ProjectSpec("2025-11_DCCE-CRI", "DCCE-CRI"),
    ProjectSpec("2025-11_UNDP-BTR", "UNDP-BTR"),
]


def hhmm_bkk() -> str:
    return datetime.now(BKK).strftime("%H:%M")


def unique_dest(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    parent = dest.parent
    i = 2
    while True:
        candidate = parent / f"{stem}__dup{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def main() -> int:
    vault = Path("ψ")
    writing = vault / "writing"
    inbox_root = vault / "inbox" / "_triage_from_writing_notes"
    log_path = vault / "archive" / "migration-log.md"

    if not writing.exists():
        raise SystemExit(f"Missing folder: {writing.as_posix()}")

    inbox_root.mkdir(parents=True, exist_ok=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    moves: list[tuple[Path, Path]] = []

    for spec in PROJECTS:
        notes_dir = writing / spec.src_folder / "notes"
        if not notes_dir.exists():
            continue

        dest_dir = inbox_root / spec.label
        dest_dir.mkdir(parents=True, exist_ok=True)

        for item in sorted(notes_dir.iterdir(), key=lambda p: p.name.lower()):
            dest = unique_dest(dest_dir / item.name)
            shutil.move(str(item), str(dest))
            moves.append((item, dest))

    if moves:
        with log_path.open("a", encoding="utf-8") as f:
            t = hhmm_bkk()
            for src, dest in moves:
                f.write(
                    f"| {t} | move | {src.as_posix()} | {dest.as_posix()} | ψ/writing/*/notes → ψ/inbox triage |\n"
                )

    print(f"Moved {len(moves)} items into {inbox_root.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

