"""Migrate ψ/writing/*/output into ψ/incubate/<Client>/<Project>/.

Rules implemented:
- Move everything under each output/ into incubate project root.
- Do not delete ψ/writing; leave empty output/ folders in place.
- Log each move to ψ/archive/migration-log.md.
- Avoid overwriting via __dupN suffix.

Run:
  python3 tools/migrate_writing_output_to_incubate.py
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
import shutil


BKK = timezone(timedelta(hours=7))


@dataclass(frozen=True)
class Mapping:
    writing_output: Path
    incubate_root: Path


MAPPINGS: list[Mapping] = [
    Mapping(Path("ψ/writing/2025-11_DCCE-CRDB/output"), Path("ψ/incubate/DCCE/CRDB")),
    Mapping(Path("ψ/writing/2025-11_DCCE-CRI/output"), Path("ψ/incubate/DCCE/CRI")),
    Mapping(Path("ψ/writing/2025-11_UNDP-BTR/output"), Path("ψ/incubate/UNDP/BTR")),
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
    log_path = Path("ψ/archive/migration-log.md")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    moves: list[tuple[Path, Path]] = []

    for m in MAPPINGS:
        if not m.writing_output.exists():
            print(f"[skip] not found: {m.writing_output.as_posix()}")
            continue

        m.incubate_root.mkdir(parents=True, exist_ok=True)

        for item in sorted(m.writing_output.iterdir(), key=lambda p: p.name.lower()):
            dest = unique_dest(m.incubate_root / item.name)
            shutil.move(str(item), str(dest))
            moves.append((item, dest))

    if moves:
        with log_path.open("a", encoding="utf-8") as f:
            t = hhmm_bkk()
            for src, dest in moves:
                f.write(
                    f"| {t} | move | {src.as_posix()} | {dest.as_posix()} | ψ/writing/*/output → ψ/incubate |\n"
                )

    print(f"Moved {len(moves)} items into ψ/incubate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

