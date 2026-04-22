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
    try:
        n = float(s)
        if np.isfinite(n) and n.is_integer():
            s = str(int(n))
    except Exception:
        pass
    digits = re.sub(r"\D", "", s)
    if not digits:
        return ""
    return digits.zfill(width)[-width:]


def norm_text(value: Any) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def to_number(series: pd.Series) -> pd.Series:
    cleaned = series.astype(str).str.replace(",", "", regex=False).str.strip()
    return pd.to_numeric(cleaned, errors="coerce").fillna(0.0)


def key_df(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["province_code"] = out["province_code"].apply(lambda x: norm_code(x, 2))
    out["district_code"] = out["district_code"].apply(lambda x: norm_code(x, 4))
    out["subdistrict_code"] = out["subdistrict_code"].apply(lambda x: norm_code(x, 6))
    return out


def run() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

    base_dir = Path(__file__).resolve().parent.parent

    in_impact = base_dir / "data/2_gold/stage3_fact_impact_tambon_numerator.csv"
    in_relief = base_dir / "data/2_gold/stage3_fact_relief_tambon_redistributed_by_sector.csv"
    in_geom = base_dir / "data/1_silver/dopa/stage3_dopa_tambon_geometry_enriched.gpkg"
    in_crosswalk = base_dir / "data/1_silver/dopa/stage3_dopa_tambon_boundary_code_crosswalk.csv"
    in_policy = base_dir / "artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md"
    in_subtask2_mismatch = base_dir / "artifacts/reports/stage3_subtask2_tambon_boundary_mismatch.csv"
    in_subtask5_validation = base_dir / "artifacts/reports/stage3_subtask5_tambon_numerator_validation.json"
    in_subtask6_validation = base_dir / "artifacts/reports/stage3_subtask6_relief_redistribution_validation.json"
    in_subtask7_validation = base_dir / "artifacts/reports/stage3_subtask7_level1_provincial_validation.json"

    out_impact = base_dir / "data/2_gold/stage3_fact_level2_impact_tambon_year_disaster.csv"
    out_relief = base_dir / "data/2_gold/stage3_fact_level2_relief_tambon_year_sector.csv"
    out_geom_missing_impact = base_dir / "artifacts/reports/stage3_subtask8_level2_impact_geometry_join_failure.csv"
    out_geom_missing_relief = base_dir / "artifacts/reports/stage3_subtask8_level2_relief_geometry_join_failure.csv"
    out_validation = base_dir / "artifacts/reports/stage3_subtask8_level2_tambon_validation.json"
    out_report = base_dir / "artifacts/reports/CRI_Phase1_Stage3_Subtask8_Level2_Tambon_Outputs_Report.md"

    blockers: list[Blocker] = []

    for p in [
        in_impact,
        in_relief,
        in_geom,
        in_crosswalk,
        in_policy,
        in_subtask2_mismatch,
        in_subtask5_validation,
        in_subtask6_validation,
        in_subtask7_validation,
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
                    "module": "Subtask 8 Level 2 Tambon Outputs",
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 1

    impact_df = pd.read_csv(in_impact, dtype=str, low_memory=False)
    relief_df = pd.read_csv(in_relief, dtype=str, low_memory=False)
    crosswalk_df = pd.read_csv(in_crosswalk, dtype=str, low_memory=False)
    subtask2_mismatch_df = pd.read_csv(in_subtask2_mismatch, dtype=str, low_memory=False)
    geom_gdf = gpd.read_file(in_geom)

    required_impact = [
        "year_be",
        "disaster_type",
        "province_code",
        "province_name_th",
        "district_code",
        "district_name_th",
        "subdistrict_code",
        "subdistrict_name_th",
        "village_event_row_count",
        "unique_village_code_count",
        "affected_people",
        "affected_households",
        "deaths",
        "housing_damage",
        "business_damage",
        "agriculture_damage",
        "livestock_damage",
        "fishing_damage",
        "transport_damage",
        "health_damage",
        "utilities_damage",
    ]
    required_relief = [
        "year_be",
        "province_code",
        "district_code",
        "subdistrict_code",
        "district_name_th",
        "subdistrict_name_th",
        "relief_sector",
        "provincial_relief_baht",
        "redistributed_relief_baht",
        "redistribution_basis",
        "module",
        "redistribution_policy",
    ]
    required_crosswalk = [
        "province_code",
        "district_code",
        "subdistrict_code",
        "match_status",
    ]

    miss_impact = [c for c in required_impact if c not in impact_df.columns]
    miss_relief = [c for c in required_relief if c not in relief_df.columns]
    miss_crosswalk = [c for c in required_crosswalk if c not in crosswalk_df.columns]
    if miss_impact:
        blockers.append(Blocker(code="missing_impact_columns", message=f"Missing impact columns: {miss_impact}"))
    if miss_relief:
        blockers.append(Blocker(code="missing_relief_columns", message=f"Missing relief columns: {miss_relief}"))
    if miss_crosswalk:
        blockers.append(Blocker(code="missing_crosswalk_columns", message=f"Missing crosswalk columns: {miss_crosswalk}"))

    if blockers:
        ensure_parent(out_validation)
        out_validation.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "module": "Subtask 8 Level 2 Tambon Outputs",
                    "input_inspection": {
                        "impact_columns": list(impact_df.columns),
                        "relief_columns": list(relief_df.columns),
                        "crosswalk_columns": list(crosswalk_df.columns),
                        "geometry_columns": list(geom_gdf.columns),
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

    # Canonical join base for geometry eligibility: only matched crosswalk rows.
    crosswalk_work = key_df(crosswalk_df[["province_code", "district_code", "subdistrict_code", "match_status"]].copy())
    matched_geom_keys = (
        crosswalk_work[crosswalk_work["match_status"].astype(str) == "matched"]
        [["province_code", "district_code", "subdistrict_code"]]
        .drop_duplicates()
        .copy()
    )

    # Level 2 impact output: preserve Subtask 5 grain, enforce shared Bangkok exclusion.
    impact = key_df(impact_df.copy())
    for c in [
        "village_event_row_count",
        "unique_village_code_count",
        "affected_people",
        "affected_households",
        "deaths",
        "housing_damage",
        "business_damage",
        "agriculture_damage",
        "livestock_damage",
        "fishing_damage",
        "transport_damage",
        "health_damage",
        "utilities_damage",
    ]:
        impact[c] = to_number(impact[c])

    impact = impact[impact["province_code"] != "10"].copy()
    impact["module"] = "stage3_subtask8_level2_tambon_outputs"
    impact["impact_source"] = "stage3_fact_impact_tambon_numerator"
    impact["level2_policy"] = "exclude_bangkok_from_shared_level2"

    impact = impact.merge(
        matched_geom_keys.assign(geometry_match_status="matched"),
        on=["province_code", "district_code", "subdistrict_code"],
        how="left",
    )
    impact["geometry_match_status"] = impact["geometry_match_status"].fillna("missing_in_matched_geometry")

    # Level 2 relief output: aggregate Subtask 6 redistributed amounts to tambon-year-sector.
    relief = key_df(relief_df.copy())
    relief["district_name_th"] = relief["district_name_th"].apply(norm_text)
    relief["subdistrict_name_th"] = relief["subdistrict_name_th"].apply(norm_text)
    relief["relief_sector"] = relief["relief_sector"].apply(norm_text)
    relief["redistribution_basis"] = relief["redistribution_basis"].apply(norm_text)
    relief["redistributed_relief_baht"] = to_number(relief["redistributed_relief_baht"])
    relief["provincial_relief_baht"] = to_number(relief["provincial_relief_baht"])

    relief = relief[relief["province_code"] != "10"].copy()

    relief_out = (
        relief.groupby(
            [
                "year_be",
                "province_code",
                "district_code",
                "subdistrict_code",
                "district_name_th",
                "subdistrict_name_th",
                "relief_sector",
                "redistribution_basis",
            ],
            dropna=False,
        )
        .agg(
            redistributed_relief_baht=("redistributed_relief_baht", "sum"),
            contributing_row_count=("subdistrict_code", "size"),
            provincial_relief_baht_reference=("provincial_relief_baht", "sum"),
        )
        .reset_index()
    )
    relief_out["module"] = "stage3_subtask8_level2_tambon_outputs"
    relief_out["relief_source"] = "stage3_fact_relief_tambon_redistributed_by_sector"
    relief_out["level2_policy"] = "exclude_bangkok_from_shared_level2"

    relief_out = relief_out.merge(
        matched_geom_keys.assign(geometry_match_status="matched"),
        on=["province_code", "district_code", "subdistrict_code"],
        how="left",
    )
    relief_out["geometry_match_status"] = relief_out["geometry_match_status"].fillna("missing_in_matched_geometry")

    # Geometry join failure artifacts.
    impact_missing_geom = (
        impact[impact["geometry_match_status"] != "matched"]
        [["province_code", "district_code", "subdistrict_code", "province_name_th", "district_name_th", "subdistrict_name_th"]]
        .drop_duplicates()
        .sort_values(["province_code", "district_code", "subdistrict_code"])
        .reset_index(drop=True)
    )
    relief_missing_geom = (
        relief_out[relief_out["geometry_match_status"] != "matched"]
        [["province_code", "district_code", "subdistrict_code", "district_name_th", "subdistrict_name_th"]]
        .drop_duplicates()
        .sort_values(["province_code", "district_code", "subdistrict_code"])
        .reset_index(drop=True)
    )

    # Reconciliation checks to parent subtasks.
    impact_metrics = [
        "village_event_row_count",
        "unique_village_code_count",
        "affected_people",
        "affected_households",
        "deaths",
        "housing_damage",
        "business_damage",
        "agriculture_damage",
        "livestock_damage",
        "fishing_damage",
        "transport_damage",
        "health_damage",
        "utilities_damage",
    ]
    impact_reconciliation: dict[str, dict[str, float | bool]] = {}
    for m in impact_metrics:
        src_total = float(to_number(impact_df[m]).sum())
        out_total = float(impact[m].sum())
        impact_reconciliation[m] = {
            "source_total_from_subtask5": src_total,
            "level2_output_total": out_total,
            "difference": out_total - src_total,
            "reconciled": bool(np.isclose(out_total, src_total, atol=1e-6)),
        }

    relief_source_total = float(to_number(relief_df["redistributed_relief_baht"]).sum())
    relief_out_total = float(relief_out["redistributed_relief_baht"].sum())

    # Bangkok and crosswalk evidentiary signals.
    bkk_crosswalk_issue_mask = (
        crosswalk_df.get("P_NAME_T", pd.Series(dtype=str)).astype(str).str.strip() == "กรุงเทพมหานคร"
    ) & (crosswalk_df["match_status"].astype(str).str.strip() != "matched")
    bkk_crosswalk_issue_rows = int(bkk_crosswalk_issue_mask.sum())
    bkk_mismatch_rows_subtask2 = 0
    if "P_NAME_T" in subtask2_mismatch_df.columns:
        bkk_mismatch_rows_subtask2 = int(
            (subtask2_mismatch_df["P_NAME_T"].astype(str).str.strip() == "กรุงเทพมหานคร").sum()
        )

    ensure_parent(out_impact)
    impact.to_csv(out_impact, index=False, encoding="utf-8-sig")
    ensure_parent(out_relief)
    relief_out.to_csv(out_relief, index=False, encoding="utf-8-sig")
    ensure_parent(out_geom_missing_impact)
    impact_missing_geom.to_csv(out_geom_missing_impact, index=False, encoding="utf-8-sig")
    ensure_parent(out_geom_missing_relief)
    relief_missing_geom.to_csv(out_geom_missing_relief, index=False, encoding="utf-8-sig")

    unresolved_blockers: list[dict[str, str]] = []
    if len(impact_missing_geom) > 0 or len(relief_missing_geom) > 0:
        unresolved_blockers.append(
            {
                "code": "level2_geometry_join_incomplete",
                "message": "Some published Level 2 tambon keys are not present in matched tambon geometry crosswalk and remain in explicit join-failure artifacts.",
            }
        )
    if bkk_mismatch_rows_subtask2 > 0:
        unresolved_blockers.append(
            {
                "code": "bangkok_tambon_crosswalk_mismatch_persist",
                "message": "Bangkok tambon mismatch rows from Subtask 2 remain unresolved and are preserved as policy evidence for lower-level exclusion.",
            }
        )

    validation = {
        "status": "ok",
        "generated_utc": utc_now_iso(),
        "module": "Subtask 8 Level 2 Tambon Outputs",
        "inputs": {
            "impact_tambon_numerator": in_impact.as_posix(),
            "relief_tambon_redistributed": in_relief.as_posix(),
            "tambon_geometry_enriched": in_geom.as_posix(),
            "tambon_crosswalk": in_crosswalk.as_posix(),
            "bangkok_policy_resolution": in_policy.as_posix(),
            "subtask2_tambon_mismatch": in_subtask2_mismatch.as_posix(),
            "subtask5_validation": in_subtask5_validation.as_posix(),
            "subtask6_validation": in_subtask6_validation.as_posix(),
            "subtask7_validation": in_subtask7_validation.as_posix(),
        },
        "input_inspection": {
            "impact_row_count": int(len(impact_df)),
            "relief_row_count": int(len(relief_df)),
            "crosswalk_row_count": int(len(crosswalk_df)),
            "geometry_row_count": int(len(geom_gdf)),
            "impact_columns": list(impact_df.columns),
            "relief_columns": list(relief_df.columns),
            "crosswalk_columns": list(crosswalk_df.columns),
            "geometry_columns": list(geom_gdf.columns),
            "geometry_crs": str(geom_gdf.crs),
            "crosswalk_match_status_counts": crosswalk_df["match_status"].astype(str).value_counts(dropna=False).to_dict(),
        },
        "policy_checks": {
            "bangkok_rows_in_impact_level2": int((impact["province_code"] == "10").sum()),
            "bangkok_rows_in_relief_level2": int((relief_out["province_code"] == "10").sum()),
            "policy_compliant": bool((impact["province_code"] == "10").sum() == 0 and (relief_out["province_code"] == "10").sum() == 0),
            "bangkok_crosswalk_nonmatched_rows": bkk_crosswalk_issue_rows,
            "bangkok_subtask2_mismatch_rows": bkk_mismatch_rows_subtask2,
            "policy_note": "Shared Level 2 excludes Bangkok per Subtask 3 resolution.",
        },
        "geometry_join_checks": {
            "impact_rows_with_matched_geometry": int((impact["geometry_match_status"] == "matched").sum()),
            "impact_rows_missing_matched_geometry": int((impact["geometry_match_status"] != "matched").sum()),
            "impact_unique_tambon_missing_geometry": int(len(impact_missing_geom)),
            "relief_rows_with_matched_geometry": int((relief_out["geometry_match_status"] == "matched").sum()),
            "relief_rows_missing_matched_geometry": int((relief_out["geometry_match_status"] != "matched").sum()),
            "relief_unique_tambon_missing_geometry": int(len(relief_missing_geom)),
        },
        "reconciliation_checks": {
            "impact_from_subtask5": impact_reconciliation,
            "relief_subtask6_redistributed_total": relief_source_total,
            "relief_level2_output_total": relief_out_total,
            "relief_difference": relief_out_total - relief_source_total,
            "relief_reconciled": bool(np.isclose(relief_out_total, relief_source_total, atol=1e-6)),
        },
        "outputs": {
            "impact_level2_csv": out_impact.as_posix(),
            "relief_level2_csv": out_relief.as_posix(),
            "impact_geometry_join_failure_csv": out_geom_missing_impact.as_posix(),
            "relief_geometry_join_failure_csv": out_geom_missing_relief.as_posix(),
            "validation_json": out_validation.as_posix(),
            "report_md": out_report.as_posix(),
            "impact_level2_row_count": int(len(impact)),
            "relief_level2_row_count": int(len(relief_out)),
        },
        "blockers": [asdict(b) for b in blockers],
        "unresolved_blockers": unresolved_blockers,
    }

    ensure_parent(out_validation)
    out_validation.write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")

    report_lines = [
        "# CRI Phase 1 Stage 3 — Subtask 8 Level 2 Tambon Outputs Report",
        "",
        f"Generated (UTC): {validation['generated_utc']}",
        "",
        "## Inputs",
        f"- Impact tambon numerator: `{in_impact.as_posix()}`",
        f"- Relief tambon redistributed: `{in_relief.as_posix()}`",
        f"- Tambon geometry enriched: `{in_geom.as_posix()}`",
        f"- Tambon boundary crosswalk: `{in_crosswalk.as_posix()}`",
        f"- Bangkok policy note: `{in_policy.as_posix()}`",
        "",
        "## Output artifacts",
        f"- Level 2 impact CSV: `{out_impact.as_posix()}`",
        f"- Level 2 relief CSV: `{out_relief.as_posix()}`",
        f"- Impact geometry join-failure CSV: `{out_geom_missing_impact.as_posix()}`",
        f"- Relief geometry join-failure CSV: `{out_geom_missing_relief.as_posix()}`",
        f"- Validation JSON: `{out_validation.as_posix()}`",
        "",
        "## Implemented Level 2 logic",
        "- Impact Level 2 persists tambon-year-disaster facts from Subtask 5 with explicit geometry eligibility status against crosswalk `match_status=matched` keys.",
        "- Relief Level 2 aggregates Subtask 6 redistributed tambon rows to tambon-year-sector totals with explicit geometry eligibility status.",
        "- Shared Bangkok exclusion (`province_code=10`) is enforced for both outputs.",
        "",
        "## Validation highlights",
        f"- Impact rows with matched geometry: {validation['geometry_join_checks']['impact_rows_with_matched_geometry']}",
        f"- Impact rows missing matched geometry: {validation['geometry_join_checks']['impact_rows_missing_matched_geometry']}",
        f"- Relief rows with matched geometry: {validation['geometry_join_checks']['relief_rows_with_matched_geometry']}",
        f"- Relief rows missing matched geometry: {validation['geometry_join_checks']['relief_rows_missing_matched_geometry']}",
        f"- Bangkok rows in Level 2 impact output: {validation['policy_checks']['bangkok_rows_in_impact_level2']}",
        f"- Bangkok rows in Level 2 relief output: {validation['policy_checks']['bangkok_rows_in_relief_level2']}",
        f"- Relief total reconciliation to Subtask 6 redistributed source: {validation['reconciliation_checks']['relief_reconciled']}",
        "",
        "## Unresolved blockers preserved",
    ]

    if unresolved_blockers:
        for b in unresolved_blockers:
            report_lines.append(f"- {b['code']}: {b['message']}")
    else:
        report_lines.append("- None in this run.")

    ensure_parent(out_report)
    out_report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "status": validation["status"],
                "outputs": validation["outputs"],
                "policy_checks": validation["policy_checks"],
                "geometry_join_checks": validation["geometry_join_checks"],
                "reconciliation_checks": {
                    "relief_reconciled": validation["reconciliation_checks"]["relief_reconciled"],
                    "relief_difference": validation["reconciliation_checks"]["relief_difference"],
                },
            },
            ensure_ascii=True,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

