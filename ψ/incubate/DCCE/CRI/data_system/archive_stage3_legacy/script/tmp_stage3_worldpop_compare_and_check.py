from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import rasterio


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def inspect_raster(path: Path) -> dict:
    result: dict = {
        "path": path.as_posix(),
        "exists": path.exists(),
    }
    if not path.exists():
        result["error"] = "missing_file"
        return result

    with rasterio.open(path.as_posix()) as src:
        result["meta"] = {
            "driver": src.driver,
            "width": src.width,
            "height": src.height,
            "count": src.count,
            "dtype": str(src.dtypes[0]),
            "crs": None if src.crs is None else str(src.crs),
            "nodata": None if src.nodata is None else float(src.nodata),
            "bounds": {
                "left": float(src.bounds.left),
                "bottom": float(src.bounds.bottom),
                "right": float(src.bounds.right),
                "top": float(src.bounds.top),
            },
            "block_shapes": [list(shape) for shape in src.block_shapes],
        }

        total_blocks = 0
        failed_blocks = 0
        first_errors: list[dict] = []
        for _, win in src.block_windows(1):
            total_blocks += 1
            try:
                _ = src.read(1, window=win, masked=True)
            except Exception as exc:  # noqa: BLE001
                failed_blocks += 1
                if len(first_errors) < 10:
                    first_errors.append(
                        {
                            "col_off": int(win.col_off),
                            "row_off": int(win.row_off),
                            "width": int(win.width),
                            "height": int(win.height),
                            "error_type": type(exc).__name__,
                            "error_message": str(exc),
                        }
                    )

        result["block_read_check"] = {
            "total_blocks": total_blocks,
            "failed_blocks": failed_blocks,
            "first_errors": first_errors,
        }

    return result


def main() -> int:
    base = Path(__file__).resolve().parent.parent
    old_path = base / "data/0_bronze/worldpop/tha_ppp_2020.tif"
    new_path = base / "data/0_bronze/worldpop/tha_pop_2020_CN_100m_R2025A_v1.tif"
    out_path = base / "artifacts/reports/stage3_worldpop_file_compare_check.json"

    output = {
        "generated_utc": utc_now_iso(),
        "old_file": inspect_raster(old_path),
        "new_file": inspect_raster(new_path),
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"report": out_path.as_posix()}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

