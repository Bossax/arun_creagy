from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


@dataclass
class Blocker:
    code: str
    message: str


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def run() -> int:
    script_path = Path(__file__).resolve()
    base_dir = script_path.parent.parent

    in_raster = base_dir / "data/0_bronze/worldpop/tha_pop_2020_CN_100m_R2025A_v1.tif"
    in_province_gpkg = base_dir / "data/1_silver/dopa/stage3_dopa_province_geometry_enriched.gpkg"
    in_province_crosswalk = base_dir / "data/1_silver/dopa/stage3_dopa_province_boundary_code_crosswalk.csv"
    in_dim_location_master = base_dir / "data/2_gold/dim_location_master.csv"

    out_denominator = base_dir / "data/2_gold/stage3_dim_denominator_province_worldpop_2020.csv"
    out_validation_json = base_dir / "artifacts/reports/stage3_subtask4_provincial_denominator_validation.json"
    out_report_md = base_dir / "artifacts/reports/CRI_Phase1_Stage3_Subtask4_Provincial_Denominator_Report.md"

    blockers: list[Blocker] = []

    for p in [in_raster, in_province_gpkg, in_province_crosswalk, in_dim_location_master]:
        if not p.exists():
            blockers.append(Blocker(code="missing_input", message=f"Missing required input: {p.as_posix()}"))

    if blockers:
        ensure_parent(out_validation_json)
        out_validation_json.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 1

    try:
        import fiona
        import geopandas as gpd
        import rasterio
        from rasterio.mask import mask
    except Exception as exc:  # noqa: BLE001
        blockers.append(
            Blocker(
                code="python_dependency_error",
                message=f"Missing geospatial dependency in active Python environment: {type(exc).__name__}: {exc}",
            )
        )
        ensure_parent(out_validation_json)
        out_validation_json.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 2

    # --- 1) Empirical input inspection ---
    gpkg_layers = fiona.listlayers(in_province_gpkg.as_posix())
    if not gpkg_layers:
        blockers.append(Blocker(code="gpkg_no_layers", message="No layers found in province enriched GPKG."))
        ensure_parent(out_validation_json)
        out_validation_json.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 3

    province_layer = gpkg_layers[0]
    gdf = gpd.read_file(in_province_gpkg.as_posix(), layer=province_layer)
    crosswalk_df = pd.read_csv(in_province_crosswalk, dtype=str)
    dim_location_df = pd.read_csv(in_dim_location_master, dtype=str)

    # Ensure required observed fields exist
    required_geom_fields = ["province_code", "province_name_th", "match_status", "geometry"]
    missing_geom_fields = [c for c in required_geom_fields if c not in gdf.columns]
    if missing_geom_fields:
        blockers.append(
            Blocker(
                code="missing_geometry_fields",
                message=f"Missing required columns in province enriched geometry: {missing_geom_fields}",
            )
        )

    required_crosswalk_fields = ["province_code", "province_name_th", "match_status"]
    missing_crosswalk_fields = [c for c in required_crosswalk_fields if c not in crosswalk_df.columns]
    if missing_crosswalk_fields:
        blockers.append(
            Blocker(
                code="missing_crosswalk_fields",
                message=f"Missing required columns in province crosswalk: {missing_crosswalk_fields}",
            )
        )

    if blockers:
        ensure_parent(out_validation_json)
        out_validation_json.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 4

    with rasterio.open(in_raster.as_posix()) as src:
        raster_meta: dict[str, Any] = {
            "path": in_raster.as_posix(),
            "driver": src.driver,
            "width": src.width,
            "height": src.height,
            "count": src.count,
            "dtype": str(src.dtypes[0]),
            "crs": str(src.crs) if src.crs is not None else None,
            "nodata": float(src.nodata) if src.nodata is not None else None,
            "bounds": {
                "left": float(src.bounds.left),
                "bottom": float(src.bounds.bottom),
                "right": float(src.bounds.right),
                "top": float(src.bounds.top),
            },
            "transform": tuple(src.transform),
        }

        # CRS harmonization
        gdf_work = gdf.copy()
        if gdf_work.crs is None:
            blockers.append(
                Blocker(
                    code="vector_crs_missing",
                    message="Province enriched geometry has no CRS; cannot perform raster zonal aggregation safely.",
                )
            )
        elif src.crs is None:
            blockers.append(
                Blocker(
                    code="raster_crs_missing",
                    message="WorldPop raster has no CRS; cannot perform raster zonal aggregation safely.",
                )
            )
        elif str(gdf_work.crs) != str(src.crs):
            gdf_work = gdf_work.to_crs(src.crs)

        if blockers:
            ensure_parent(out_validation_json)
            out_validation_json.write_text(
                json.dumps(
                    {
                        "status": "blocked",
                        "generated_utc": utc_now_iso(),
                        "input_inspection": {
                            "gpkg_layer": province_layer,
                            "gpkg_columns": list(gdf.columns),
                            "gpkg_feature_count": int(len(gdf)),
                            "gpkg_crs": str(gdf.crs) if gdf.crs is not None else None,
                            "crosswalk_columns": list(crosswalk_df.columns),
                            "crosswalk_row_count": int(len(crosswalk_df)),
                            "raster": raster_meta,
                        },
                        "blockers": [asdict(b) for b in blockers],
                    },
                    ensure_ascii=False,
                    indent=2,
                ),
                encoding="utf-8",
            )
            print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
            return 5

        # Apply policy for Stage 3 L1: include Bangkok at province level.
        # Shared lower levels are excluded by policy and are not part of this module.
        gdf_work["province_code"] = gdf_work["province_code"].astype(str).str.zfill(2)
        gdf_work = gdf_work[gdf_work["match_status"].astype(str).str.lower() == "matched"].copy()

        # --- 2) Provincial denominator generation (zonal sum of WorldPop 2020) ---
        rows: list[dict[str, Any]] = []
        for rec in gdf_work[["province_code", "province_name_th", "match_status", "geometry"]].itertuples(index=False):
            province_code = str(rec.province_code).zfill(2)
            province_name_th = rec.province_name_th
            geom = rec.geometry

            if geom is None or geom.is_empty:
                rows.append(
                    {
                        "province_code": province_code,
                        "province_name_th": province_name_th,
                        "province_location_id": f"{province_code}000000",
                        "worldpop_population_2020": np.nan,
                        "valid_pixel_count": 0,
                        "nodata_pixel_count": np.nan,
                        "match_status": rec.match_status,
                        "denominator_source": "worldpop_tha_ppp_2020_tif",
                        "processing_note": "empty_geometry",
                    }
                )
                continue

            try:
                masked, _ = mask(src, [geom], crop=True, nodata=src.nodata, filled=False)
            except Exception as exc:  # noqa: BLE001
                rows.append(
                    {
                        "province_code": province_code,
                        "province_name_th": province_name_th,
                        "province_location_id": f"{province_code}000000",
                        "worldpop_population_2020": np.nan,
                        "valid_pixel_count": np.nan,
                        "nodata_pixel_count": np.nan,
                        "match_status": rec.match_status,
                        "denominator_source": "worldpop_tha_ppp_2020_tif",
                        "processing_note": f"raster_read_error:{type(exc).__name__}:{exc}",
                    }
                )
                continue
            band = masked[0]

            if np.ma.isMaskedArray(band):
                valid = band.compressed()
                valid_count = int(valid.size)
                total_count = int(band.size)
                nodata_count = total_count - valid_count
                pop_sum = float(valid.sum()) if valid_count > 0 else 0.0
            else:
                valid = np.asarray(band).ravel()
                valid_count = int(valid.size)
                nodata_count = 0
                pop_sum = float(valid.sum()) if valid_count > 0 else 0.0

            rows.append(
                {
                    "province_code": province_code,
                    "province_name_th": province_name_th,
                    "province_location_id": f"{province_code}000000",
                    "worldpop_population_2020": pop_sum,
                    "valid_pixel_count": valid_count,
                    "nodata_pixel_count": nodata_count,
                    "match_status": rec.match_status,
                    "denominator_source": "worldpop_tha_ppp_2020_tif",
                    "processing_note": "ok",
                }
            )

    denom_df = pd.DataFrame(rows)
    denom_df = denom_df.sort_values(["province_code"]).reset_index(drop=True)

    # FK-style evidence against dim_location_master province codes
    dim_loc = dim_location_df.copy()
    dim_loc["province_code"] = dim_loc["province_code"].astype(str).str.zfill(2)
    valid_province_code_set = set(dim_loc["province_code"].dropna().unique().tolist())
    denom_df["province_code_exists_in_dim_location_master"] = denom_df["province_code"].isin(valid_province_code_set)

    # --- 3) Validation evidence ---
    total_province_features = int(len(gdf))
    matched_province_features = int((gdf["match_status"].astype(str).str.lower() == "matched").sum())
    denominator_rows = int(len(denom_df))
    null_population_rows = int(denom_df["worldpop_population_2020"].isna().sum())
    zero_population_rows = int((denom_df["worldpop_population_2020"].fillna(0) == 0).sum())
    negative_population_rows = int((denom_df["worldpop_population_2020"].fillna(0) < 0).sum())
    null_valid_pixel_rows = int(denom_df["valid_pixel_count"].isna().sum())
    zero_valid_pixel_rows = int((denom_df["valid_pixel_count"].fillna(0) == 0).sum())
    bangkok_rows = int((denom_df["province_code"] == "10").sum())
    raster_read_error_rows = int(denom_df["processing_note"].astype(str).str.startswith("raster_read_error:").sum())
    raster_read_error_province_codes = sorted(
        denom_df.loc[
            denom_df["processing_note"].astype(str).str.startswith("raster_read_error:"),
            "province_code",
        ]
        .astype(str)
        .tolist()
    )

    missing_from_crosswalk = sorted(set(denom_df["province_code"].tolist()) - set(crosswalk_df["province_code"].astype(str).str.zfill(2).tolist()))
    missing_from_denominator = sorted(
        set(crosswalk_df.loc[crosswalk_df["match_status"].astype(str).str.lower() == "matched", "province_code"].astype(str).str.zfill(2).tolist())
        - set(denom_df["province_code"].tolist())
    )

    validation = {
        "status": "ok",
        "generated_utc": utc_now_iso(),
        "module": "Subtask 4 Provincial Denominator",
        "inputs": {
            "raster": in_raster.as_posix(),
            "province_enriched_geometry": in_province_gpkg.as_posix(),
            "province_crosswalk": in_province_crosswalk.as_posix(),
            "dim_location_master": in_dim_location_master.as_posix(),
        },
        "input_inspection": {
            "gpkg_layers": gpkg_layers,
            "gpkg_layer_used": province_layer,
            "gpkg_columns": list(gdf.columns),
            "gpkg_feature_count": total_province_features,
            "gpkg_crs": str(gdf.crs) if gdf.crs is not None else None,
            "crosswalk_columns": list(crosswalk_df.columns),
            "crosswalk_row_count": int(len(crosswalk_df)),
            "raster": raster_meta,
        },
        "policy_checks": {
            "bangkok_level1_included": bool(bangkok_rows == 1),
            "bangkok_rows_in_denominator": bangkok_rows,
            "note": "Subtask 4 is Level 1 only. Shared Level 2 and Level 3 Bangkok exclusions are out-of-scope for this module.",
        },
        "coverage_checks": {
            "total_province_features": total_province_features,
            "matched_province_features": matched_province_features,
            "denominator_rows": denominator_rows,
            "missing_from_crosswalk": missing_from_crosswalk,
            "missing_from_denominator": missing_from_denominator,
        },
        "quality_checks": {
            "null_population_rows": null_population_rows,
            "zero_population_rows": zero_population_rows,
            "negative_population_rows": negative_population_rows,
            "null_valid_pixel_rows": null_valid_pixel_rows,
            "zero_valid_pixel_rows": zero_valid_pixel_rows,
            "raster_read_error_rows": raster_read_error_rows,
            "all_province_codes_exist": bool(denom_df["province_code_exists_in_dim_location_master"].all()),
            "missing_province_codes": sorted(
                denom_df.loc[~denom_df["province_code_exists_in_dim_location_master"], "province_code"].astype(str).tolist()
            ),
            "raster_read_error_province_codes": raster_read_error_province_codes,
        },
        "output": {
            "denominator_csv": out_denominator.as_posix(),
            "validation_json": out_validation_json.as_posix(),
            "report_md": out_report_md.as_posix(),
            "row_count": denominator_rows,
        },
        "blockers": [asdict(b) for b in blockers],
    }

    if raster_read_error_rows > 0:
        validation["status"] = "blocked"
        validation["blockers"].append(
            {
                "code": "worldpop_raster_read_failure",
                "message": (
                    f"Raster read failed for {raster_read_error_rows} province polygon(s). "
                    "Denominator output is incomplete and must not be used for Stage 3 Level 1 risk computation "
                    "until the WorldPop raster integrity issue is resolved."
                ),
            }
        )

    # Persist outputs
    ensure_parent(out_denominator)
    denom_df.to_csv(out_denominator, index=False, encoding="utf-8-sig")

    ensure_parent(out_validation_json)
    out_validation_json.write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")

    # Minimal human-readable report
    ensure_parent(out_report_md)
    report_lines = [
        "# CRI Phase 1 Stage 3 — Subtask 4 Provincial Denominator Report",
        "",
        f"Generated (UTC): {validation['generated_utc']}",
        "",
        "## Inputs",
        f"- Raster: `{in_raster.as_posix()}`",
        f"- Province enriched geometry: `{in_province_gpkg.as_posix()}`",
        f"- Province crosswalk: `{in_province_crosswalk.as_posix()}`",
        f"- Canonical spine: `{in_dim_location_master.as_posix()}`",
        "",
        "## Output",
        f"- Denominator CSV: `{out_denominator.as_posix()}`",
        "",
        "## Coverage & quality checks",
        f"- Total province features in geometry: {total_province_features}",
        f"- Matched province features used for denominator: {matched_province_features}",
        f"- Denominator rows written: {denominator_rows}",
        f"- Bangkok rows in denominator (province_code=10): {bangkok_rows}",
        f"- Null population rows: {null_population_rows}",
        f"- Zero population rows: {zero_population_rows}",
        f"- Negative population rows: {negative_population_rows}",
        f"- Zero valid-pixel rows: {zero_valid_pixel_rows}",
        f"- Raster read error rows: {raster_read_error_rows}",
        f"- All province codes exist in dim_location_master: {validation['quality_checks']['all_province_codes_exist']}",
        "",
        "## Notes",
        "- This module only produces Level 1 provincial denominator required for later Stage 3 risk computation.",
        "- Shared Level 2 and Level 3 outputs are intentionally out of scope in Subtask 4.",
        "- If raster_read_error_rows > 0, this run is policy-blocked and requires raster integrity remediation before downstream use.",
        f"- Detailed machine-readable validation is stored in `{out_validation_json.as_posix()}`.",
    ]
    out_report_md.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(json.dumps({"status": validation["status"], "output": validation["output"], "quality_checks": validation["quality_checks"]}, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

