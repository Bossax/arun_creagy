"""Delete ψ/active/ only if it contains no files.

Rationale:
- We only remove the legacy 'active' caveat folder after migration.
- Enforces 'Nothing is Deleted' by refusing to delete if any files remain.

Run:
  python3 tools/cleanup_active_if_empty.py
"""

from __future__ import annotations

from pathlib import Path
import shutil


def main() -> int:
    active = Path("ψ/active")
    if not active.exists():
        print("ψ/active does not exist; nothing to delete")
        return 0

    remaining = [p for p in active.rglob("*") if p.is_file()]
    if remaining:
        print(f"Refusing to delete ψ/active: {len(remaining)} files remain")
        for p in remaining[:20]:
            print(" -", p.as_posix())
        return 2

    shutil.rmtree(active)
    print("Deleted ψ/active (was empty)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

