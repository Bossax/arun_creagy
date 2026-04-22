from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.features import rasterize
from rasterio.mask import mask


@dataclass
class Blocker:
    code: str
    message: str


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def norm_code(value: Any, width: int) -> str:
    if pd.isna(value):
        return ""
    s = str(value).strip()
    if not s:
        return ""
    digits = re.sub(r"\D", "", s)
    if not digits:
        return ""
    return digits.zfill(width)[-width:]


def run() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

    base = Path(__file__).resolve().parent.parent

    in_raster = base / "data/0_bronze/worldpop/tha_pop_2020_CN_100m_R2025A_v1.tif"
    in_tambon_geom = base / "data/1_silver/dopa/stage3_dopa_tambon_geometry_enriched.gpkg"
    in_tambon_crosswalk = base / "data/1_silver/dopa/stage3_dopa_tambon_boundary_code_crosswalk.csv"
    in_level2_impact = base / "data/2_gold/stage3_fact_level2_impact_tambon_year_disaster.csv"
    in_level2_relief = base / "data/2_gold/stage3_fact_level2_relief_tambon_year_sector.csv"
    in_policy = base / "artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md"
    in_subtask8_validation = base / "artifacts/reports/stage3_subtask8_level2_tambon_validation.json"
    in_subtask6_validation = base / "artifacts/reports/stage3_subtask6_relief_redistribution_validation.json"

    out_level3_raster = base / "data/2_gold/stage3_level3_worldpop_2020_non_bangkok_matched_tambon.tif"
    out_level3_mask = base / "data/2_gold/stage3_level3_tambon_eligibility_mask_non_bangkok.tif"
    out_key_coverage = base / "artifacts/reports/stage3_subtask9_level3_tambon_key_coverage.csv"
    out_validation = base / "artifacts/reports/stage3_subtask9_level3_spatial_validation.json"
    out_report = base / "artifacts/reports/CRI_Phase1_Stage3_Subtask9_Level3_Spatial_Outputs_Report.md"

    blockers: list[Blocker] = []
    for p in [
        in_raster,
        in_tambon_geom,
        in_tambon_crosswalk,
        in_level2_impact,
        in_level2_relief,
        in_policy,
        in_subtask8_validation,
        in_subtask6_validation,
    ]:
        if not p.exists():
            blockers.append(Blocker(code="missing_input", message=f"Missing required input: {p.as_posix()}"))

    if blockers:
        ensure_parent(out_validation)
        out_validation.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "module": "Subtask 9 Level 3 Spatial Outputs",
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 1

    geom = gpd.read_file(in_tambon_geom)
    crosswalk = pd.read_csv(in_tambon_crosswalk, dtype=str, low_memory=False)
    impact = pd.read_csv(in_level2_impact, dtype=str, low_memory=False)
    relief = pd.read_csv(in_level2_relief, dtype=str, low_memory=False)
    subtask8_validation = json.loads(in_subtask8_validation.read_text(encoding="utf-8"))
    subtask6_validation = json.loads(in_subtask6_validation.read_text(encoding="utf-8"))

    required_geom = ["province_code", "district_code", "subdistrict_code", "match_status", "geometry"]
    required_crosswalk = ["province_code", "district_code", "subdistrict_code", "match_status"]
    required_impact = ["province_code", "district_code", "subdistrict_code", "geometry_match_status"]
    required_relief = ["province_code", "district_code", "subdistrict_code", "geometry_match_status"]

    miss_geom = [c for c in required_geom if c not in geom.columns]
    miss_crosswalk = [c for c in required_crosswalk if c not in crosswalk.columns]
    miss_impact = [c for c in required_impact if c not in impact.columns]
    miss_relief = [c for c in required_relief if c not in relief.columns]

    if miss_geom:
        blockers.append(Blocker(code="missing_geometry_columns", message=f"Missing tambon geometry columns: {miss_geom}"))
    if miss_crosswalk:
        blockers.append(Blocker(code="missing_crosswalk_columns", message=f"Missing tambon crosswalk columns: {miss_crosswalk}"))
    if miss_impact:
        blockers.append(Blocker(code="missing_level2_impact_columns", message=f"Missing Level 2 impact columns: {miss_impact}"))
    if miss_relief:
        blockers.append(Blocker(code="missing_level2_relief_columns", message=f"Missing Level 2 relief columns: {miss_relief}"))

    if blockers:
        ensure_parent(out_validation)
        out_validation.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "module": "Subtask 9 Level 3 Spatial Outputs",
                    "input_inspection": {
                        "geometry_columns": list(geom.columns),
                        "crosswalk_columns": list(crosswalk.columns),
                        "impact_columns": list(impact.columns),
                        "relief_columns": list(relief.columns),
                    },
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 2

    for df in [geom, crosswalk, impact, relief]:
        df["province_code"] = df["province_code"].apply(lambda x: norm_code(x, 2))
        df["district_code"] = df["district_code"].apply(lambda x: norm_code(x, 4))
        df["subdistrict_code"] = df["subdistrict_code"].apply(lambda x: norm_code(x, 6))

    # Shared Stage 3 policy: Level 3 excludes Bangkok.
    eligible_geom = geom[
        (geom["match_status"].astype(str) == "matched") & (geom["province_code"] != "10")
    ].copy()

    if eligible_geom.empty:
        blockers.append(Blocker(code="no_eligible_geometry", message="No non-Bangkok matched tambon geometry available for Level 3 shared outputs."))

    if eligible_geom.geometry.is_empty.any() or eligible_geom.geometry.isna().any():
        blockers.append(
            Blocker(
                code="invalid_geometry",
                message="Eligible tambon geometry contains empty/null geometry; cannot safely build Level 3 raster outputs.",
            )
        )

    if blockers:
        ensure_parent(out_validation)
        out_validation.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "module": "Subtask 9 Level 3 Spatial Outputs",
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 3

    impact_key_counts = (
        impact.groupby(["province_code", "district_code", "subdistrict_code"], dropna=False)
        .size()
        .reset_index(name="level2_impact_row_count")
    )
    relief_key_counts = (
        relief.groupby(["province_code", "district_code", "subdistrict_code"], dropna=False)
        .size()
        .reset_index(name="level2_relief_row_count")
    )

    eligible_keys = eligible_geom[["province_code", "district_code", "subdistrict_code"]].drop_duplicates().copy()
    key_coverage = eligible_keys.merge(impact_key_counts, on=["province_code", "district_code", "subdistrict_code"], how="left")
    key_coverage = key_coverage.merge(relief_key_counts, on=["province_code", "district_code", "subdistrict_code"], how="left")
    key_coverage["level2_impact_row_count"] = key_coverage["level2_impact_row_count"].fillna(0).astype(int)
    key_coverage["level2_relief_row_count"] = key_coverage["level2_relief_row_count"].fillna(0).astype(int)
    key_coverage["in_level2_impact"] = key_coverage["level2_impact_row_count"] > 0
    key_coverage["in_level2_relief"] = key_coverage["level2_relief_row_count"] > 0

    ensure_parent(out_key_coverage)
    key_coverage.sort_values(["province_code", "district_code", "subdistrict_code"]).to_csv(
        out_key_coverage, index=False, encoding="utf-8-sig"
    )

    with rasterio.open(in_raster) as src:
        raster_meta = {
            "path": in_raster.as_posix(),
            "driver": src.driver,
            "width": int(src.width),
            "height": int(src.height),
            "count": int(src.count),
            "dtype": str(src.dtypes[0]),
            "crs": str(src.crs),
            "nodata": None if src.nodata is None else float(src.nodata),
            "bounds": {
                "left": float(src.bounds.left),
                "bottom": float(src.bounds.bottom),
                "right": float(src.bounds.right),
                "top": float(src.bounds.top),
            },
            "transform": [float(x) for x in src.transform],
        }

        geom_proj = eligible_geom.to_crs(src.crs) if str(eligible_geom.crs) != str(src.crs) else eligible_geom

        masked_pop, masked_transform = mask(
            src,
            [g for g in geom_proj.geometry],
            crop=True,
            nodata=src.nodata,
            filled=True,
        )

        pop_arr = masked_pop[0]
        shapes = ((g, 1) for g in geom_proj.geometry)
        eligibility_mask = rasterize(
            shapes,
            out_shape=pop_arr.shape,
            transform=masked_transform,
            fill=0,
            dtype="uint8",
            all_touched=False,
        )

        pop_profile = src.profile.copy()
        pop_profile.update(
            {
                "height": int(pop_arr.shape[0]),
                "width": int(pop_arr.shape[1]),
                "transform": masked_transform,
                "count": 1,
                "dtype": str(pop_arr.dtype),
                "compress": "deflate",
            }
        )
        ensure_parent(out_level3_raster)
        with rasterio.open(out_level3_raster, "w", **pop_profile) as dst:
            dst.write(pop_arr, 1)

        mask_profile = src.profile.copy()
        mask_profile.update(
            {
                "height": int(eligibility_mask.shape[0]),
                "width": int(eligibility_mask.shape[1]),
                "transform": masked_transform,
                "count": 1,
                "dtype": "uint8",
                "nodata": 0,
                "compress": "deflate",
            }
        )
        ensure_parent(out_level3_mask)
        with rasterio.open(out_level3_mask, "w", **mask_profile) as dst:
            dst.write(eligibility_mask, 1)

        eligible_pixel_count = int((eligibility_mask == 1).sum())
        nodata_value = src.nodata
        if nodata_value is None:
            masked_valid_pixels = int(np.isfinite(pop_arr).sum())
        else:
            masked_valid_pixels = int((pop_arr != nodata_value).sum())

    inherited_blockers: list[dict[str, str]] = []
    for item in subtask8_validation.get("unresolved_blockers", []):
        inherited_blockers.append({
            "code": f"inherited_{item.get('code', 'unknown')}",
            "message": str(item.get("message", "")),
        })

    unallocated_groups = int(
        subtask6_validation.get("coverage_checks", {}).get("unallocated_province_year_sector_rows", 0)
    )
    if unallocated_groups > 0:
        inherited_blockers.append(
            {
                "code": "inherited_subtask6_unallocated_groups",
                "message": (
                    f"Subtask 6 preserved {unallocated_groups} unallocated province-year-sector groups; "
                    "Level 3 shared outputs preserve this inherited allocation gap without silent correction."
                ),
            }
        )

    validation = {
        "status": "ok",
        "generated_utc": utc_now_iso(),
        "module": "Subtask 9 Level 3 Spatial Outputs",
        "inputs": {
            "worldpop_raster": in_raster.as_posix(),
            "tambon_geometry_enriched": in_tambon_geom.as_posix(),
            "tambon_crosswalk": in_tambon_crosswalk.as_posix(),
            "level2_impact": in_level2_impact.as_posix(),
            "level2_relief": in_level2_relief.as_posix(),
            "bangkok_policy": in_policy.as_posix(),
            "subtask8_validation": in_subtask8_validation.as_posix(),
            "subtask6_validation": in_subtask6_validation.as_posix(),
        },
        "input_inspection": {
            "raster": raster_meta,
            "tambon_geometry_crs": str(geom.crs),
            "tambon_geometry_row_count": int(len(geom)),
            "tambon_crosswalk_row_count": int(len(crosswalk)),
            "crosswalk_match_status_counts": crosswalk["match_status"].astype(str).value_counts(dropna=False).to_dict(),
            "level2_impact_row_count": int(len(impact)),
            "level2_relief_row_count": int(len(relief)),
        },
        "policy_checks": {
            "bangkok_rows_in_level2_impact_input": int((impact["province_code"] == "10").sum()),
            "bangkok_rows_in_level2_relief_input": int((relief["province_code"] == "10").sum()),
            "bangkok_rows_in_level3_eligible_geometry": int((eligible_geom["province_code"] == "10").sum()),
            "bangkok_exclusion_compliant": bool((eligible_geom["province_code"] == "10").sum() == 0),
            "policy_note": "Shared Level 3 excludes Bangkok per Stage 3 Bangkok policy resolution.",
        },
        "spatial_coverage_checks": {
            "eligible_tambon_geometry_rows": int(len(eligible_geom)),
            "eligible_unique_tambon_keys": int(len(eligible_keys)),
            "level3_mask_eligible_pixel_count": eligible_pixel_count,
            "level3_population_valid_pixel_count": masked_valid_pixels,
            "eligible_keys_with_level2_impact": int(key_coverage["in_level2_impact"].sum()),
            "eligible_keys_without_level2_impact": int((~key_coverage["in_level2_impact"]).sum()),
            "eligible_keys_with_level2_relief": int(key_coverage["in_level2_relief"].sum()),
            "eligible_keys_without_level2_relief": int((~key_coverage["in_level2_relief"]).sum()),
        },
        "inherited_gap_checks": {
            "subtask8_impact_rows_missing_matched_geometry": int(
                subtask8_validation.get("geometry_join_checks", {}).get("impact_rows_missing_matched_geometry", 0)
            ),
            "subtask8_relief_rows_missing_matched_geometry": int(
                subtask8_validation.get("geometry_join_checks", {}).get("relief_rows_missing_matched_geometry", 0)
            ),
            "subtask8_bangkok_subtask2_mismatch_rows": int(
                subtask8_validation.get("policy_checks", {}).get("bangkok_subtask2_mismatch_rows", 0)
            ),
            "subtask6_unallocated_province_year_sector_rows": unallocated_groups,
        },
        "outputs": {
            "level3_population_raster": out_level3_raster.as_posix(),
            "level3_eligibility_mask_raster": out_level3_mask.as_posix(),
            "tambon_key_coverage_csv": out_key_coverage.as_posix(),
            "validation_json": out_validation.as_posix(),
            "report_md": out_report.as_posix(),
        },
        "blockers": [asdict(b) for b in blockers],
        "unresolved_blockers": inherited_blockers,
    }

    ensure_parent(out_validation)
    out_validation.write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")

    report_lines = [
        "# CRI Phase 1 Stage 3 — Subtask 9 Level 3 Spatial Outputs Report",
        "",
        f"Generated (UTC): {validation['generated_utc']}",
        "",
        "## Inputs",
        f"- WorldPop raster: `{in_raster.as_posix()}`",
        f"- Tambon geometry enriched: `{in_tambon_geom.as_posix()}`",
        f"- Tambon crosswalk: `{in_tambon_crosswalk.as_posix()}`",
        f"- Level 2 impact: `{in_level2_impact.as_posix()}`",
        f"- Level 2 relief: `{in_level2_relief.as_posix()}`",
        f"- Bangkok policy: `{in_policy.as_posix()}`",
        "",
        "## Level 3 outputs",
        f"- Population raster (non-Bangkok, matched tambon mask): `{out_level3_raster.as_posix()}`",
        f"- Eligibility mask raster (1=eligible, 0=outside): `{out_level3_mask.as_posix()}`",
        f"- Tambon key coverage CSV: `{out_key_coverage.as_posix()}`",
        f"- Validation JSON: `{out_validation.as_posix()}`",
        "",
        "## Validation highlights",
        f"- Raster CRS: {raster_meta['crs']}",
        f"- Raster dimensions: {raster_meta['width']} x {raster_meta['height']}",
        f"- Eligible tambon geometry rows: {validation['spatial_coverage_checks']['eligible_tambon_geometry_rows']}",
        f"- Eligible mask pixels: {validation['spatial_coverage_checks']['level3_mask_eligible_pixel_count']}",
        f"- Bangkok exclusion compliant: {validation['policy_checks']['bangkok_exclusion_compliant']}",
        f"- Inherited Subtask 8 impact rows missing matched geometry: {validation['inherited_gap_checks']['subtask8_impact_rows_missing_matched_geometry']}",
        f"- Inherited Subtask 8 relief rows missing matched geometry: {validation['inherited_gap_checks']['subtask8_relief_rows_missing_matched_geometry']}",
        f"- Inherited Subtask 6 unallocated province-year-sector rows: {validation['inherited_gap_checks']['subtask6_unallocated_province_year_sector_rows']}",
        "",
        "## Scope guardrail",
        "- This subtask publishes only shared Level 3 spatial outputs and module-level validation.",
        "- Final end-to-end integrity checks are intentionally out of scope and preserved for later stage work.",
    ]

    ensure_parent(out_report)
    out_report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "status": validation["status"],
                "outputs": validation["outputs"],
                "policy_checks": validation["policy_checks"],
                "spatial_coverage_checks": validation["spatial_coverage_checks"],
            },
            ensure_ascii=True,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

