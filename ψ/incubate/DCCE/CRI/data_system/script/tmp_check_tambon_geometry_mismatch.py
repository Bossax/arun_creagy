"""Check DDPM tambon codes vs tambon boundary shapefile for Chiang Rai (climate hazards only).

Purpose
-------
Prints a mismatch report:
- # unique tambon codes in DDPM subset
- # unique tambon codes in tambon shapefile
- missing DDPM codes (no geometry)
- extra shapefile codes (not present in DDPM subset)

This script is non-destructive: read-only.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import geopandas as gpd


ROOT = Path(r"c:\Users\sitth\OracleWorkspace\Arun_Creagy")

DDPM_CSV = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "1_silver" / "ddpm" / "master_village_disaster_stat_2557_2567.csv"
HAZ_DIM = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "2_gold" / "dim_hazard_canonical.csv"
TAMBON_SHP = ROOT / "ψ" / "incubate" / "DCCE" / "CRI" / "data_system" / "data" / "1_silver" / "dopa" / "tambon_boundaries_enriched.shp"


def first_col(df: pd.DataFrame, candidates: list[str]) -> str:
    for c in candidates:
        if c in df.columns:
            return c
    raise KeyError(f"None of columns found: {candidates}. Available: {list(df.columns)}")


def read_ddpm(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, encoding="cp874", low_memory=False)
    except Exception:
        return pd.read_csv(path, encoding="utf-8", low_memory=False)


def main() -> int:
    # Ensure Thai text can be printed in Windows terminals
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # py3.7+
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
        df["Disaster Type"]
        .astype(str)
        .str.strip()
        .replace({"ดินโคลนถล่ม/ดินถล่ม": "ดินโคลนถล่ม"})
    )
    mask = hazard_norm.isin(climate) | hazard_norm.str.contains(
        "ดินถล่ม|ดินโคลนถล่ม", regex=True
    )
    df = df.loc[mask].copy()
    df["Disaster Type (normalized)"] = hazard_norm.loc[mask].values

    prov = df["Province Code"].astype(str).str.strip()
    year = pd.to_numeric(df["ปี"], errors="coerce")
    df = df.loc[prov.eq("57") & year.between(2560, 2567, inclusive="both")].copy()

    df["subdistrict_code"] = df["Subdistrict Code"].astype(str).str.strip()
    ddpm_codes = set(df["subdistrict_code"].dropna())
    ddpm_codes = {c for c in ddpm_codes if str(c).strip() not in ("", "nan", "None")}

    name_lu = (
        df[["subdistrict_code", "Subdistrict"]]
        .dropna()
        .assign(Subdistrict=lambda d: d["Subdistrict"].astype(str).str.strip())
        .groupby("subdistrict_code")["Subdistrict"]
        .agg(lambda s: s.value_counts().index[0])
    )

    geo = gpd.read_file(TAMBON_SHP)
    geo_code_col = first_col(
        geo, ["subdist_cd", "subdistrict_code", "SUBDIST_CD", "tambon_cd", "TAM_CODE"]
    )
    geo_codes = set(geo[geo_code_col].astype(str).str.strip().dropna())

    # Ensure stable sorting (some shapefile rows can yield non-string values)
    missing = sorted((ddpm_codes - geo_codes), key=str)
    extra = sorted((geo_codes - ddpm_codes), key=str)

    print("DDPM subset: Chiang Rai (57), climate hazards only, years 2560–2567")
    print(f"- Unique DDPM tambon codes: {len(ddpm_codes)}")
    print(f"- Unique shapefile tambon codes: {len(geo_codes)}")
    print(f"- Missing geometries for DDPM codes: {len(missing)}")
    print(f"- Extra geometries not in DDPM subset: {len(extra)}")

    if missing:
        print("\nMissing code -> DDPM tambon name (mode):")
        for c in missing:
            nm = name_lu.get(c, "")
            # Avoid hard failure if terminal encoding still can't render Thai
            try:
                print(f"{c}, {nm}")
            except UnicodeEncodeError:
                print(f"{c}, {nm.encode('utf-8', errors='replace').decode('utf-8')}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

