from __future__ import annotations

import json
from pathlib import Path
import sys

import pandas as pd


BASE = Path(__file__).resolve().parents[1]

INPUTS = {
    "denominator": BASE / "data/2_gold/stage3_dim_denominator_province_worldpop_2020.csv",
    "impact_tambon": BASE / "data/2_gold/stage3_fact_impact_tambon_numerator.csv",
    "relief_tambon": BASE / "data/2_gold/stage3_fact_relief_tambon_redistributed_by_sector.csv",
    "dim_location_master": BASE / "data/2_gold/dim_location_master.csv",
}

OUT = BASE / "artifacts/reports/stage3_subtask7_level1_schema_inspection.json"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

    report: dict[str, object] = {"inputs": {}, "derived": {}}

    for k, p in INPUTS.items():
        df = pd.read_csv(p, low_memory=False)
        report["inputs"][k] = {
            "path": str(p),
            "row_count": int(len(df)),
            "columns": list(df.columns),
            "dtypes": {c: str(t) for c, t in df.dtypes.items()},
            "sample": df.head(3).to_dict(orient="records"),
        }

    impact = pd.read_csv(INPUTS["impact_tambon"])
    relief = pd.read_csv(INPUTS["relief_tambon"])
    denom = pd.read_csv(INPUTS["denominator"])

    report["derived"] = {
        "impact_group_keys_present": [
            c
            for c in ["province_code", "year_be", "year_ce"]
            if c in impact.columns
        ],
        "relief_group_keys_present": [
            c
            for c in ["province_code", "year_be", "year_ce"]
            if c in relief.columns
        ],
        "denominator_keys_present": [
            c
            for c in ["province_code", "province_name_th", "worldpop_population_2020"]
            if c in denom.columns
        ],
        "impact_province_count": int(impact["province_code"].nunique()) if "province_code" in impact.columns else None,
        "relief_province_count": int(relief["province_code"].nunique()) if "province_code" in relief.columns else None,
        "denom_province_count": int(denom["province_code"].nunique()) if "province_code" in denom.columns else None,
    }

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(OUT.as_posix())


if __name__ == "__main__":
    main()

