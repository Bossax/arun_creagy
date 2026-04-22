from __future__ import annotations

import csv
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List


BASE = Path("ψ/incubate/DCCE/CRI/data_system")


@dataclass
class CsvAudit:
    rel_path: str
    exists: bool
    columns: List[str]
    row_count_estimate: int | None


def read_csv_header_and_count(path: Path) -> tuple[list[str], int | None]:
    if not path.exists():
        return [], None
    header: list[str] = []
    row_count = 0
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, [])
        for _ in reader:
            row_count += 1
    return header, row_count


def read_dbf_fields(dbf_path: Path) -> list[str]:
    if not dbf_path.exists():
        return []
    data = dbf_path.read_bytes()
    if len(data) < 32:
        return []
    header_len = int.from_bytes(data[8:10], "little")
    fields: list[str] = []
    offset = 32
    while offset + 32 <= header_len:
        desc = data[offset : offset + 32]
        if desc[0] == 0x0D:
            break
        name = desc[0:11].split(b"\x00", 1)[0].decode("ascii", errors="ignore").strip()
        if name:
            fields.append(name)
        offset += 32
    return fields


def read_prj(prj_path: Path) -> str | None:
    if not prj_path.exists():
        return None
    return prj_path.read_text(encoding="utf-8", errors="ignore").strip()


def inspect_raster(path: Path) -> dict[str, Any]:
    out: dict[str, Any] = {
        "exists": path.exists(),
        "file_size_bytes": path.stat().st_size if path.exists() else None,
    }
    if not path.exists():
        return out
    try:
        import rasterio  # type: ignore

        with rasterio.open(path) as ds:  # type: ignore
            out.update(
                {
                    "driver": ds.driver,
                    "width": ds.width,
                    "height": ds.height,
                    "count": ds.count,
                    "crs": str(ds.crs) if ds.crs else None,
                    "dtype": ds.dtypes[0] if ds.dtypes else None,
                    "nodata": ds.nodata,
                    "bounds": [ds.bounds.left, ds.bounds.bottom, ds.bounds.right, ds.bounds.top],
                }
            )
    except Exception as e:  # pragma: no cover
        out["rasterio_error"] = f"{type(e).__name__}: {e}"
    return out


def main() -> None:
    audited_csvs = [
        "data/2_gold/dim_location_master.csv",
        "data/2_gold/dim_location.csv",
        "data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv",
        "data/1_silver/ddpm/master_financial_relief_by_sector.csv",
        "data/1_silver/bma/bkk_hazard_impact_yearly.csv",
    ]

    csv_results: list[CsvAudit] = []
    for rel in audited_csvs:
        p = BASE / rel
        cols, rows = read_csv_header_and_count(p)
        csv_results.append(
            CsvAudit(rel_path=rel, exists=p.exists(), columns=cols, row_count_estimate=rows)
        )

    shape_base = BASE / "data/0_bronze/dopa/thailanda-administrative-boundary"
    shape_targets = ["THA_Province", "THA_Amphoe", "THA_Tambon"]
    shapes: dict[str, Any] = {}
    for stem in shape_targets:
        shp = shape_base / f"{stem}.shp"
        dbf = shape_base / f"{stem}.dbf"
        prj = shape_base / f"{stem}.prj"
        shx = shape_base / f"{stem}.shx"
        cpg = shape_base / f"{stem}.CPG"
        shapes[stem] = {
            "shp_exists": shp.exists(),
            "dbf_exists": dbf.exists(),
            "shx_exists": shx.exists(),
            "cpg_exists": cpg.exists(),
            "dbf_fields": read_dbf_fields(dbf),
            "prj": read_prj(prj),
        }

    worldpop_rel = "data/0_bronze/worldpop/tha_ppp_2020.tif"
    worldpop_tiff_rel = "data/0_bronze/worldpop/tha_ppp_2020.tiff"
    raster = inspect_raster(BASE / worldpop_rel)

    out = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "base": str(BASE),
        "csv_audit": [asdict(x) for x in csv_results],
        "shapefile_audit": shapes,
        "worldpop": {
            "expected_tif_rel_path": worldpop_rel,
            "alt_tiff_rel_path": worldpop_tiff_rel,
            "tif_exists": (BASE / worldpop_rel).exists(),
            "tiff_exists": (BASE / worldpop_tiff_rel).exists(),
            "raster_details": raster,
        },
    }

    out_json = BASE / "artifacts/reports/stage3_input_audit_snapshot.json"
    out_json.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    lines: list[str] = []
    lines.append("# Stage 3 Input Baseline Audit Snapshot")
    lines.append("")
    lines.append(f"Generated (UTC): {out['generated_at_utc']}")
    lines.append("")
    lines.append("## CSV Inputs")
    for c in out["csv_audit"]:
        lines.append(f"- `{c['rel_path']}`: exists={c['exists']}, rows={c['row_count_estimate']}")
        if c["columns"]:
            lines.append(f"  - columns: {', '.join(c['columns'])}")
    lines.append("")
    lines.append("## DOPA Boundary Assets")
    for k, v in out["shapefile_audit"].items():
        lines.append(
            f"- `{k}`: shp={v['shp_exists']}, dbf={v['dbf_exists']}, shx={v['shx_exists']}, cpg={v['cpg_exists']}"
        )
        lines.append(f"  - dbf_fields: {', '.join(v['dbf_fields']) if v['dbf_fields'] else '(none)'}")
        lines.append(f"  - prj: {v['prj'][:160] + '...' if v['prj'] and len(v['prj']) > 160 else v['prj']}")
    lines.append("")
    lines.append("## WorldPop Asset")
    wp = out["worldpop"]
    lines.append(
        f"- expected `.tif` exists={wp['tif_exists']}; alternate `.tiff` exists={wp['tiff_exists']}"
    )
    rd = wp["raster_details"]
    lines.append(
        "- raster details: "
        + ", ".join(
            [
                f"driver={rd.get('driver')}",
                f"width={rd.get('width')}",
                f"height={rd.get('height')}",
                f"count={rd.get('count')}",
                f"crs={rd.get('crs')}",
                f"dtype={rd.get('dtype')}",
                f"nodata={rd.get('nodata')}",
                f"bounds={rd.get('bounds')}",
                f"rasterio_error={rd.get('rasterio_error')}",
            ]
        )
    )

    out_md = BASE / "artifacts/reports/CRI_Phase1_Stage3_Input_Baseline_Audit.md"
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Intentionally no console path printing to avoid Windows cp1252 unicode issues
    # when the repository path contains non-ASCII characters.


if __name__ == "__main__":
    main()

