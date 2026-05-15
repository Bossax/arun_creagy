"""Assess impacts for tambons missing geometries.

Uses the same filters as the mismatch check:
- Chiang Rai province code 57
- climate hazards only (from dim_hazard_canonical.csv)
- years 2560–2567

Then aggregates impacts for a specified list of tambon codes and reports:
- sums for Affected Households / Affected People / Deaths
- rank and percentile among all Chiang Rai tambons in the filtered subset

Non-destructive: read-only.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(r"c:\Users\sitth\OracleWorkspace\Arun_Creagy")

DDPM_CSV = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "1_silver" / "ddpm" / "master_village_disaster_stat_2557_2567.csv"
HAZ_DIM = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "2_gold" / "dim_hazard_canonical.csv"

MISSING_CODES = [
    "571701",
    "571702",
    "571703",
    "571801",
    "571802",
    "571803",
]


def read_ddpm(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, encoding="cp874", low_memory=False)
    except Exception:
        return pd.read_csv(path, encoding="utf-8", low_memory=False)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    haz = pd.read_csv(HAZ_DIM, encoding="utf-8-sig")
    climate = set(
        haz.loc[haz["hazard_group"].eq("climate"), "canonical_hazard_name_th"]
        .dropna()
        .astype(str)
    )

    df = read_ddpm(DDPM_CSV)
    hazard_norm = (
        df["Disaster Type"].astype(str).str.strip().replace({"ดินโคลนถล่ม/ดินถล่ม": "ดินโคลนถล่ม"})
    )
    mask = hazard_norm.isin(climate) | hazard_norm.str.contains("ดินถล่ม|ดินโคลนถล่ม", regex=True)
    df = df.loc[mask].copy()
    df["Disaster Type (normalized)"] = hazard_norm.loc[mask].values

    prov = df["Province Code"].astype(str).str.strip()
    year = pd.to_numeric(df["ปี"], errors="coerce")
    df = df.loc[prov.eq("57") & year.between(2560, 2567, inclusive="both")].copy()

    df["subdistrict_code"] = df["Subdistrict Code"].astype(str).str.strip()
    df["subdistrict_name"] = df["Subdistrict"].astype(str).str.strip()

    # Aggregate to tambon
    agg = (
        df.groupby("subdistrict_code")[["Affected Households", "Affected People", "Deaths"]]
        .sum(numeric_only=True)
        .reset_index()
    )

    # Use mode name per code for display
    name_lu = (
        df[["subdistrict_code", "subdistrict_name"]]
        .dropna()
        .groupby("subdistrict_code")["subdistrict_name"]
        .agg(lambda s: s.value_counts().index[0])
    )
    agg["subdistrict_name"] = agg["subdistrict_code"].map(name_lu)

    # Ranking within Chiang Rai tambons
    for col in ["Affected Households", "Affected People", "Deaths"]:
        # Higher = worse
        agg[f"{col}_rank"] = agg[col].rank(method="min", ascending=False)
        agg[f"{col}_pct"] = agg[col].rank(pct=True, method="max", ascending=True)  # higher value => higher pct

    missing_df = agg[agg["subdistrict_code"].isin(MISSING_CODES)].copy()
    missing_df = missing_df.sort_values("Affected Households", ascending=False)

    print("Missing-geometry tambons impact check (Chiang Rai, climate hazards only, 2560–2567)")
    print(f"Universe tambons in subset: {len(agg)}")
    print("\nTambon impacts + rank (1=highest) and percentile among Chiang Rai tambons:\n")

    cols = [
        "subdistrict_code",
        "subdistrict_name",
        "Affected Households",
        "Affected Households_rank",
        "Affected Households_pct",
        "Affected People",
        "Affected People_rank",
        "Affected People_pct",
        "Deaths",
        "Deaths_rank",
        "Deaths_pct",
    ]

    # Pretty print
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        out = missing_df[cols].copy()
        # Percentiles as 0-100
        for c in ["Affected Households_pct", "Affected People_pct", "Deaths_pct"]:
            out[c] = (out[c] * 100).round(1)
        print(out.to_string(index=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

