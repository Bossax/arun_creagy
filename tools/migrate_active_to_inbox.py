"""Migrate ψ/active project captures into ψ/inbox triage.

Design goals:
- Preserve history (no deletion) by moving + logging every move.
- Keep assets out of the first-pass move (exclude top-level 'pic' and per-project 'attachments').
- Be safe with collisions (auto-suffix duplicates).

Run:
  python3 tools/migrate_active_to_inbox.py
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

EXCLUDE_TOP_LEVEL_NAMES = {"attachments", "pic"}


def hhmm_bkk() -> str:
    return datetime.now(BKK).strftime("%H:%M")


def ensure_migration_log(log_path: Path) -> None:
    if log_path.exists():
        return
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text(
        """# Migration Log

Records file moves performed during the `ψ/active` → `ψ/inbox` and `ψ/writing/*/output` → `ψ/incubate` migration.

## 2026-03-10

| Time (Asia/Bangkok) | Action | From | To | Notes |
|---|---|---|---|---|
""",
        encoding="utf-8",
    )


def unique_dest(dest: Path) -> Path:
    """Return a non-existing path by suffixing __dupN."""
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
    active = vault / "active"
    inbox_root = vault / "inbox" / "_triage_from_active"
    log_path = vault / "archive" / "migration-log.md"

    if not active.exists():
        raise SystemExit(f"Missing folder: {active.as_posix()}")

    inbox_root.mkdir(parents=True, exist_ok=True)
    ensure_migration_log(log_path)

    moves: list[tuple[Path, Path]] = []

    for spec in PROJECTS:
        src_dir = active / spec.src_folder
        if not src_dir.exists():
            print(f"[skip] not found: {src_dir.as_posix()}")
            continue

        dest_dir = inbox_root / spec.label
        dest_dir.mkdir(parents=True, exist_ok=True)

        for item in sorted(src_dir.iterdir(), key=lambda p: p.name.lower()):
            if item.name in EXCLUDE_TOP_LEVEL_NAMES:
                continue

            dest = unique_dest(dest_dir / item.name)
            shutil.move(str(item), str(dest))
            moves.append((item, dest))

    if moves:
        with log_path.open("a", encoding="utf-8") as f:
            t = hhmm_bkk()
            for src, dest in moves:
                f.write(
                    f"| {t} | move | {src.as_posix()} | {dest.as_posix()} | ψ/active → ψ/inbox triage (excluding attachments/pic) |\n"
                )

    print(f"Moved {len(moves)} items into {inbox_root.as_posix()}")

    for spec in PROJECTS:
        src_dir = active / spec.src_folder
        if not src_dir.exists():
            continue
        remaining = sorted([p.name for p in src_dir.iterdir()])
        print(f"Remaining in {src_dir.as_posix()}: {remaining}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

