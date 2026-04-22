from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


def main() -> int:
    base_dir = Path(__file__).resolve().parent.parent
    in_json = base_dir / "artifacts/reports/stage3_worldpop_raster_diagnose.json"
    out_json = base_dir / "artifacts/reports/stage3_worldpop_raster_diagnose_summary.json"

    data = json.loads(in_json.read_text(encoding="utf-8"))
    block_failures = data.get("raster_block_failures", [])
    mask_failures = data.get("mask_failures", [])

    block_error_counter = Counter(f.get("error_type", "") for f in block_failures)
    mask_error_counter = Counter(f.get("error_type", "") for f in mask_failures)

    rows = [int(f["row_off"]) for f in block_failures if f.get("row_off") is not None]
    cols = [int(f["col_off"]) for f in block_failures if f.get("col_off") is not None]

    summary = {
        "inputs": {"diagnostic_json": in_json.as_posix()},
        "mask_failure_count": int(data.get("mask_failure_count", 0)),
        "raster_block_failure_count": int(data.get("raster_block_failure_count", 0)),
        "mask_error_types": dict(mask_error_counter),
        "block_error_types": dict(block_error_counter),
        "block_failure_row_off_min": min(rows) if rows else None,
        "block_failure_row_off_max": max(rows) if rows else None,
        "block_failure_col_off_min": min(cols) if cols else None,
        "block_failure_col_off_max": max(cols) if cols else None,
        "sample_mask_failure": mask_failures[0] if mask_failures else None,
        "sample_block_failure": block_failures[0] if block_failures else None,
    }

    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

