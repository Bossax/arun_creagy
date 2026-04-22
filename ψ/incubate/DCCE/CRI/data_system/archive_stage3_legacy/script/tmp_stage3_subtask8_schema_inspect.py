from __future__ import annotations

import json
import sys
from pathlib import Path

import geopandas as gpd
import pandas as pd


BASE = Path(__file__).resolve().parents[1]

INPUTS = {
    "impact_tambon_numerator": BASE / "data/2_gold/stage3_fact_impact_tambon_numerator.csv",
    "relief_tambon_redistributed": BASE / "data/2_gold/stage3_fact_relief_tambon_redistributed_by_sector.csv",
    "tambon_geometry_enriched": BASE / "data/1_silver/dopa/stage3_dopa_tambon_geometry_enriched.gpkg",
    "tambon_boundary_crosswalk": BASE / "data/1_silver/dopa/stage3_dopa_tambon_boundary_code_crosswalk.csv",
}

OUT = BASE / "artifacts/reports/stage3_subtask8_level2_schema_inspection.json"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

    report: dict[str, object] = {"inputs": {}, "derived": {}}

    impact = pd.read_csv(INPUTS["impact_tambon_numerator"], low_memory=False)
    relief = pd.read_csv(INPUTS["relief_tambon_redistributed"], low_memory=False)
    crosswalk = pd.read_csv(INPUTS["tambon_boundary_crosswalk"], low_memory=False)
    tambon_gdf = gpd.read_file(INPUTS["tambon_geometry_enriched"])

    report["inputs"] = {
        "impact_tambon_numerator": {
            "path": INPUTS["impact_tambon_numerator"].as_posix(),
            "row_count": int(len(impact)),
            "columns": list(impact.columns),
        },
        "relief_tambon_redistributed": {
            "path": INPUTS["relief_tambon_redistributed"].as_posix(),
            "row_count": int(len(relief)),
            "columns": list(relief.columns),
        },
        "tambon_boundary_crosswalk": {
            "path": INPUTS["tambon_boundary_crosswalk"].as_posix(),
            "row_count": int(len(crosswalk)),
            "columns": list(crosswalk.columns),
        },
        "tambon_geometry_enriched": {
            "path": INPUTS["tambon_geometry_enriched"].as_posix(),
            "row_count": int(len(tambon_gdf)),
            "columns": list(tambon_gdf.columns),
            "crs": str(tambon_gdf.crs),
            "geom_type": sorted({str(x) for x in tambon_gdf.geom_type.dropna().unique()}),
        },
    }

    derived: dict[str, object] = {}

    for key, df in {
        "impact": impact,
        "relief": relief,
        "crosswalk": crosswalk,
        "geometry": pd.DataFrame(tambon_gdf.drop(columns="geometry", errors="ignore")),
    }.items():
        code_cols = [c for c in df.columns if "code" in c.lower()]
        derived[f"{key}_code_columns"] = code_cols

    if "match_status" in crosswalk.columns:
        derived["crosswalk_match_status_counts"] = (
            crosswalk["match_status"].astype(str).value_counts(dropna=False).to_dict()
        )
    else:
        derived["crosswalk_match_status_counts"] = None

    if "subdistrict_code" in crosswalk.columns:
        cw_codes = (
            crosswalk["subdistrict_code"]
            .astype(str)
            .str.replace(r"\D", "", regex=True)
            .str.zfill(6)
        )
        derived["crosswalk_unique_subdistrict_code_count"] = int(cw_codes[cw_codes != "000000"].nunique())

    if "subdistrict_code" in impact.columns:
        impact_codes = (
            impact["subdistrict_code"].astype(str).str.replace(r"\D", "", regex=True).str.zfill(6)
        )
        derived["impact_unique_subdistrict_code_count"] = int(impact_codes[impact_codes != "000000"].nunique())

    if "subdistrict_code" in relief.columns:
        relief_codes = (
            relief["subdistrict_code"].astype(str).str.replace(r"\D", "", regex=True).str.zfill(6)
        )
        derived["relief_unique_subdistrict_code_count"] = int(relief_codes[relief_codes != "000000"].nunique())

    report["derived"] = derived

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(OUT.as_posix())


if __name__ == "__main__":
    main()

