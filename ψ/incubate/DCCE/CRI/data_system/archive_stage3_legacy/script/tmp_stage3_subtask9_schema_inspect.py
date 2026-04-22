from __future__ import annotations

import json
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd
import rasterio


BASE = Path(__file__).resolve().parents[1]

INPUTS = {
    "worldpop_raster": BASE / "data/0_bronze/worldpop/tha_pop_2020_CN_100m_R2025A_v1.tif",
    "tambon_geometry_enriched": BASE / "data/1_silver/dopa/stage3_dopa_tambon_geometry_enriched.gpkg",
    "tambon_crosswalk": BASE / "data/1_silver/dopa/stage3_dopa_tambon_boundary_code_crosswalk.csv",
    "level2_impact": BASE / "data/2_gold/stage3_fact_level2_impact_tambon_year_disaster.csv",
    "level2_relief": BASE / "data/2_gold/stage3_fact_level2_relief_tambon_year_sector.csv",
    "subtask8_validation": BASE / "artifacts/reports/stage3_subtask8_level2_tambon_validation.json",
    "subtask6_validation": BASE / "artifacts/reports/stage3_subtask6_relief_redistribution_validation.json",
}

OUT = BASE / "artifacts/reports/stage3_subtask9_level3_schema_inspection.json"


def norm_code(series: pd.Series, width: int) -> pd.Series:
    return (
        series.astype(str)
        .str.replace(r"\D", "", regex=True)
        .str.zfill(width)
        .str[-width:]
    )


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

    for p in INPUTS.values():
        if not p.exists():
            raise FileNotFoundError(str(p))

    impact = pd.read_csv(INPUTS["level2_impact"], low_memory=False)
    relief = pd.read_csv(INPUTS["level2_relief"], low_memory=False)
    crosswalk = pd.read_csv(INPUTS["tambon_crosswalk"], low_memory=False)
    gdf = gpd.read_file(INPUTS["tambon_geometry_enriched"])

    with rasterio.open(INPUTS["worldpop_raster"]) as src:
        raster_meta = {
            "path": INPUTS["worldpop_raster"].as_posix(),
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

    impact_codes = (
        pd.DataFrame(
            {
                "province_code": norm_code(impact["province_code"], 2),
                "district_code": norm_code(impact["district_code"], 4),
                "subdistrict_code": norm_code(impact["subdistrict_code"], 6),
            }
        )
        .drop_duplicates()
        .reset_index(drop=True)
    )
    relief_codes = (
        pd.DataFrame(
            {
                "province_code": norm_code(relief["province_code"], 2),
                "district_code": norm_code(relief["district_code"], 4),
                "subdistrict_code": norm_code(relief["subdistrict_code"], 6),
            }
        )
        .drop_duplicates()
        .reset_index(drop=True)
    )

    crosswalk_work = pd.DataFrame(
        {
            "province_code": norm_code(crosswalk["province_code"], 2),
            "district_code": norm_code(crosswalk["district_code"], 4),
            "subdistrict_code": norm_code(crosswalk["subdistrict_code"], 6),
            "match_status": crosswalk["match_status"].astype(str),
        }
    )
    matched_crosswalk_codes = (
        crosswalk_work[crosswalk_work["match_status"] == "matched"]
        [["province_code", "district_code", "subdistrict_code"]]
        .drop_duplicates()
    )

    gdf_key = pd.DataFrame(gdf.drop(columns="geometry", errors="ignore")).copy()
    gdf_key["province_code"] = norm_code(gdf_key["province_code"], 2)
    gdf_key["district_code"] = norm_code(gdf_key["district_code"], 4)
    gdf_key["subdistrict_code"] = norm_code(gdf_key["subdistrict_code"], 6)
    gdf_codes = gdf_key[["province_code", "district_code", "subdistrict_code"]].drop_duplicates()

    report = {
        "inputs": {k: v.as_posix() for k, v in INPUTS.items()},
        "input_inspection": {
            "raster": raster_meta,
            "tambon_geometry": {
                "row_count": int(len(gdf)),
                "columns": list(gdf.columns),
                "crs": str(gdf.crs),
                "geom_types": sorted([str(x) for x in gdf.geom_type.dropna().unique()]),
            },
            "tambon_crosswalk": {
                "row_count": int(len(crosswalk)),
                "columns": list(crosswalk.columns),
                "match_status_counts": crosswalk["match_status"].astype(str).value_counts(dropna=False).to_dict(),
            },
            "level2_impact": {
                "row_count": int(len(impact)),
                "columns": list(impact.columns),
            },
            "level2_relief": {
                "row_count": int(len(relief)),
                "columns": list(relief.columns),
            },
        },
        "derived_key_coverage": {
            "impact_unique_tambon_keys": int(len(impact_codes)),
            "relief_unique_tambon_keys": int(len(relief_codes)),
            "crosswalk_matched_unique_tambon_keys": int(len(matched_crosswalk_codes)),
            "geometry_unique_tambon_keys": int(len(gdf_codes)),
            "impact_bangkok_rows": int((norm_code(impact["province_code"], 2) == "10").sum()),
            "relief_bangkok_rows": int((norm_code(relief["province_code"], 2) == "10").sum()),
        },
    }

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(OUT.as_posix())


if __name__ == "__main__":
    main()

