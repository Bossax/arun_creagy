"""Move remaining CRI 'attachments' from ψ/active into incubate assets.

Source:
  ψ/active/2025-11_DCCE-CRI/attachments/

Destination:
  ψ/incubate/DCCE/CRI/assets/attachments/

Behavior:
- Moves files (skips desktop.ini)
- Avoids overwrites via __dupN suffix
- Appends move rows to ψ/archive/migration-log.md
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path
import shutil


BKK = timezone(timedelta(hours=7))


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
    src = Path("ψ/active/2025-11_DCCE-CRI/attachments")
    dst = Path("ψ/incubate/DCCE/CRI/assets/attachments")
    log = Path("ψ/archive/migration-log.md")

    if not src.exists():
        print(f"[skip] missing: {src.as_posix()}")
        return 0

    dst.mkdir(parents=True, exist_ok=True)
    log.parent.mkdir(parents=True, exist_ok=True)

    moves: list[tuple[Path, Path]] = []

    for item in sorted(src.iterdir(), key=lambda p: p.name.lower()):
        if not item.is_file():
            continue
        if item.name.lower() == "desktop.ini":
            continue

        target = unique_dest(dst / item.name)
        shutil.move(str(item), str(target))
        moves.append((item, target))

    if moves:
        with log.open("a", encoding="utf-8") as f:
            t = hhmm_bkk()
            for s, d in moves:
                f.write(
                    f"| {t} | move | {s.as_posix()} | {d.as_posix()} | CRI attachments → incubate assets/attachments |\n"
                )

    print(f"Moved {len(moves)} files into {dst.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

