"""Diagnose whether tambon geometries exist but are missing subdistrict codes.

This script:
- reads `tambon_boundaries_enriched.shp`
- detects which column is used as subdistrict code
- reports blank/NaN/invalid codes
- attempts a best-effort lookup for specific missing DDPM codes by matching on names

Non-destructive: read-only.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import geopandas as gpd


ROOT = Path(r"c:\Users\sitth\OracleWorkspace\Arun_Creagy")
SHP = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "1_silver" / "dopa" / "tambon_boundaries_enriched.shp"
DDPM_CSV = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "1_silver" / "ddpm" / "master_village_disaster_stat_2557_2567.csv"

MISSING_CODES = [
    "571701",
    "571702",
    "571703",
    "571801",
    "571802",
    "571803",
]


def first_col(df: pd.DataFrame, candidates: list[str]) -> str | None:
    for c in candidates:
        if c in df.columns:
            return c
    return None


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    gdf = gpd.read_file(SHP)
    print(f"Loaded: {SHP}")
    print(f"Rows: {len(gdf):,}")
    print("Columns:")
    print("- " + "\n- ".join(map(str, list(gdf.columns))))

    code_col = first_col(gdf, ["subdistrict_code", "subdist_cd", "SUBDIST_CD", "tambon_cd", "TAM_CODE"])
    prov_col = first_col(gdf, ["province_code", "prov_code", "PROV_CODE", "prov_cd"])
    name_th_col = first_col(gdf, ["subdist_th", "subdistrict_th", "tambon_th", "TAM_NAMT", "TAM_NAME_T"])
    amphoe_th_col = first_col(gdf, ["amp_th", "amphoe_th", "AMP_NAMT", "A_NAME_T"])
    prov_th_col = first_col(gdf, ["prov_th", "province_th", "PROV_NAMT", "P_NAME_T"])

    print("\nDetected columns:")
    print(f"- code_col: {code_col}")
    print(f"- prov_col: {prov_col}")
    print(f"- name_th_col: {name_th_col}")
    print(f"- amphoe_th_col: {amphoe_th_col}")
    print(f"- prov_th_col: {prov_th_col}")

    if code_col is None:
        print("\nNo obvious subdistrict-code column found. This file cannot be joined by code without enrichment.")
        return 0

    codes = gdf[code_col].astype(str).str.strip()
    invalid = codes.isna() | codes.eq("") | codes.str.lower().isin({"nan", "none"})
    # also flag non-digit or wrong length
    non_digit = ~codes.str.fullmatch(r"\d+")
    wrong_len = codes.str.fullmatch(r"\d+") & ~codes.str.len().isin([6])

    print("\nCode quality summary:")
    print(f"- blank/NaN-like: {int(invalid.sum()):,}")
    print(f"- non-digit: {int((~invalid & non_digit).sum()):,}")
    print(f"- digit but length != 6: {int((~invalid & wrong_len).sum()):,}")

    if int(invalid.sum()) > 0:
        sample = gdf.loc[invalid, [c for c in [prov_col, prov_th_col, amphoe_th_col, name_th_col, code_col] if c is not None]].head(20)
        print("\nSample rows with missing code:")
        print(sample.to_string(index=False))

    # Try to see if the missing DDPM codes exist as geometries but with missing code by matching names from DDPM
    try:
        df = pd.read_csv(DDPM_CSV, encoding="cp874", low_memory=False)
    except Exception:
        df = pd.read_csv(DDPM_CSV, encoding="utf-8", low_memory=False)

    df["Subdistrict Code"] = df["Subdistrict Code"].astype(str).str.strip()
    df["Province Code"] = df["Province Code"].astype(str).str.strip()
    df["Subdistrict"] = df.get("Subdistrict", "").astype(str).str.strip()
    df["District"] = df.get("District", "").astype(str).str.strip()

    ddpm_lookup = (
        df.loc[df["Province Code"].eq("57") & df["Subdistrict Code"].isin(MISSING_CODES), ["Subdistrict Code", "District", "Subdistrict"]]
        .drop_duplicates()
    )
    if len(ddpm_lookup) == 0:
        print("\nNo DDPM rows found for the missing codes (unexpected).")
        return 0

    print("\nAttempt name-based matching for missing codes (Chiang Rai) against shapefile:")
    for _, row in ddpm_lookup.iterrows():
        code = row["Subdistrict Code"]
        dname = row["District"]
        tname = row["Subdistrict"]
        if not tname or tname.lower() in {"nan", "none"}:
            continue

        # Candidate match on Thai names if available, else skip.
        if name_th_col is None:
            print(f"- {code}: cannot match by name; shapefile has no Thai tambon name column")
            continue

        cand = gdf.copy()
        if prov_col is not None:
            cand = cand[cand[prov_col].astype(str).str.strip().eq("57")]
        if prov_th_col is not None:
            cand = cand[cand[prov_th_col].astype(str).str.strip().eq("เชียงราย")]
        if amphoe_th_col is not None and dname:
            cand = cand[cand[amphoe_th_col].astype(str).str.strip().eq(dname)]
        cand = cand[cand[name_th_col].astype(str).str.strip().eq(tname)]

        print(f"- {code} ({tname}): matches in shapefile by name = {len(cand)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

