from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
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


def norm_text(value: Any) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def to_number(series: pd.Series) -> pd.Series:
    cleaned = series.astype(str).str.replace(",", "", regex=False).str.strip()
    return pd.to_numeric(cleaned, errors="coerce").fillna(0)


def run() -> int:
    base_dir = Path(__file__).resolve().parent.parent

    in_ddpm = base_dir / "data/1_silver/ddpm/master_village_disaster_stat_2557_2567.csv"
    in_dim = base_dir / "data/2_gold/dim_location_master.csv"
    in_policy = base_dir / "artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md"
    in_subtask2_mismatch = base_dir / "artifacts/reports/stage3_subtask2_tambon_boundary_mismatch.csv"

    out_numerator = base_dir / "data/2_gold/stage3_fact_impact_tambon_numerator.csv"
    out_unmatched = base_dir / "artifacts/reports/stage3_subtask5_tambon_numerator_unmatched_village_code.csv"
    out_null_village = base_dir / "artifacts/reports/stage3_subtask5_tambon_numerator_null_village_code.csv"
    out_validation = base_dir / "artifacts/reports/stage3_subtask5_tambon_numerator_validation.json"
    out_report = base_dir / "artifacts/reports/CRI_Phase1_Stage3_Subtask5_Tambon_Numerator_Report.md"

    blockers: list[Blocker] = []

    for p in [in_ddpm, in_dim, in_policy, in_subtask2_mismatch]:
        if not p.exists():
            blockers.append(Blocker(code="missing_input", message=f"Missing required input: {p.as_posix()}"))

    if blockers:
        ensure_parent(out_validation)
        out_validation.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "module": "Subtask 5 Tambon Numerator",
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 1

    ddpm_df = pd.read_csv(in_ddpm, dtype=str, low_memory=False)
    dim_df = pd.read_csv(in_dim, dtype=str, low_memory=False)
    subtask2_mismatch_df = pd.read_csv(in_subtask2_mismatch, dtype=str, low_memory=False)

    required_ddpm = [
        "ปี",
        "Disaster Type",
        "Province Code",
        "District Code",
        "Subdistrict Code",
        "Village Code",
        "Affected People",
        "Affected Households",
        "Deaths",
        "Housing Damage",
        "Business Damage",
        "Agriculture Damage",
        "Livestock Damage",
        "Fishing Damage",
        "Transport Damage",
        "Health Damage",
        "Utilities Damage",
    ]
    required_dim = [
        "location_id",
        "province_code",
        "province_name_th",
        "district_code",
        "district_name_th",
        "subdistrict_code",
        "subdistrict_name_th",
        "village_code",
        "village_name_th",
        "admin_level",
    ]

    missing_ddpm = [c for c in required_ddpm if c not in ddpm_df.columns]
    missing_dim = [c for c in required_dim if c not in dim_df.columns]
    if missing_ddpm:
        blockers.append(Blocker(code="missing_ddpm_columns", message=f"Missing DDPM columns: {missing_ddpm}"))
    if missing_dim:
        blockers.append(Blocker(code="missing_dim_columns", message=f"Missing dim_location_master columns: {missing_dim}"))

    if blockers:
        ensure_parent(out_validation)
        out_validation.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "module": "Subtask 5 Tambon Numerator",
                    "input_inspection": {
                        "ddpm_columns": list(ddpm_df.columns),
                        "dim_columns": list(dim_df.columns),
                        "ddpm_row_count": int(len(ddpm_df)),
                        "dim_row_count": int(len(dim_df)),
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

    metric_cols = [
        "Affected People",
        "Affected Households",
        "Deaths",
        "Housing Damage",
        "Business Damage",
        "Agriculture Damage",
        "Livestock Damage",
        "Fishing Damage",
        "Transport Damage",
        "Health Damage",
        "Utilities Damage",
    ]

    ddpm_work = ddpm_df.copy()
    ddpm_work["year_be"] = ddpm_work["ปี"].apply(lambda x: norm_code(x, 4))
    ddpm_work["disaster_type"] = ddpm_work["Disaster Type"].apply(norm_text)
    ddpm_work["village_code_norm"] = ddpm_work["Village Code"].apply(lambda x: norm_code(x, 8))
    ddpm_work["province_code_src_norm"] = ddpm_work["Province Code"].apply(lambda x: norm_code(x, 2))
    ddpm_work["district_code_src_norm"] = ddpm_work["District Code"].apply(lambda x: norm_code(x, 4))
    ddpm_work["subdistrict_code_src_norm"] = ddpm_work["Subdistrict Code"].apply(lambda x: norm_code(x, 6))
    ddpm_work["has_village_code"] = ddpm_work["village_code_norm"].ne("")

    for c in metric_cols:
        ddpm_work[c] = to_number(ddpm_work[c])

    dim_work = dim_df.copy()
    dim_work["province_code_norm"] = dim_work["province_code"].apply(lambda x: norm_code(x, 2))
    dim_work["district_code_norm"] = dim_work["district_code"].apply(lambda x: norm_code(x, 4))
    dim_work["subdistrict_code_norm"] = dim_work["subdistrict_code"].apply(lambda x: norm_code(x, 6))
    dim_work["village_code_norm"] = dim_work["village_code"].apply(lambda x: norm_code(x, 8))
    dim_work["admin_level_norm"] = dim_work["admin_level"].apply(lambda x: norm_text(x).lower())

    village_spine = dim_work[dim_work["village_code_norm"].ne("")].copy()
    village_spine = village_spine[
        [
            "village_code_norm",
            "province_code_norm",
            "province_name_th",
            "district_code_norm",
            "district_name_th",
            "subdistrict_code_norm",
            "subdistrict_name_th",
            "village_name_th",
            "location_id",
            "admin_level_norm",
        ]
    ].copy()

    village_unique = village_spine[
        [
            "village_code_norm",
            "province_code_norm",
            "district_code_norm",
            "subdistrict_code_norm",
            "province_name_th",
            "district_name_th",
            "subdistrict_name_th",
        ]
    ].drop_duplicates()

    village_conflicts = (
        village_unique.groupby("village_code_norm", dropna=False)
        .size()
        .reset_index(name="mapping_count")
    )
    village_conflicts = village_conflicts[village_conflicts["mapping_count"] > 1].copy()
    if not village_conflicts.empty:
        blockers.append(
            Blocker(
                code="village_mapping_ambiguous",
                message=(
                    f"Found {len(village_conflicts)} village_code values mapping to multiple canonical tambon paths "
                    "in dim_location_master; cannot run deterministic tambon aggregation."
                ),
            )
        )

    if blockers:
        ensure_parent(out_validation)
        out_validation.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "module": "Subtask 5 Tambon Numerator",
                    "input_inspection": {
                        "ddpm_columns": list(ddpm_df.columns),
                        "dim_columns": list(dim_df.columns),
                        "ddpm_row_count": int(len(ddpm_df)),
                        "dim_row_count": int(len(dim_df)),
                        "village_spine_row_count": int(len(village_spine)),
                        "village_unique_key_count": int(village_unique["village_code_norm"].nunique()),
                        "village_conflict_count": int(len(village_conflicts)),
                    },
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 3

    village_map = village_unique.rename(
        columns={
            "province_code_norm": "province_code",
            "district_code_norm": "district_code",
            "subdistrict_code_norm": "subdistrict_code",
        }
    )

    joined = ddpm_work.merge(village_map, on="village_code_norm", how="left")
    joined["is_matched"] = joined["subdistrict_code"].notna() & joined["subdistrict_code"].ne("")
    joined["is_null_village_code"] = ~joined["has_village_code"]
    joined["match_status"] = np.where(
        joined["is_matched"],
        "matched",
        np.where(joined["is_null_village_code"], "null_village_code", "unmatched_village_code"),
    )

    matched = joined[joined["is_matched"]].copy()
    unmatched = joined[joined["match_status"] == "unmatched_village_code"].copy()
    null_village = joined[joined["match_status"] == "null_village_code"].copy()

    # Bangkok policy for shared Level 2: exclude Bangkok rows from published tambon numerator
    matched["province_code"] = matched["province_code"].astype(str).str.zfill(2)
    matched["district_code"] = matched["district_code"].astype(str).str.zfill(4)
    matched["subdistrict_code"] = matched["subdistrict_code"].astype(str).str.zfill(6)
    matched_non_bangkok = matched[matched["province_code"] != "10"].copy()
    bangkok_excluded_rows = int((matched["province_code"] == "10").sum())

    group_keys = [
        "year_be",
        "disaster_type",
        "province_code",
        "province_name_th",
        "district_code",
        "district_name_th",
        "subdistrict_code",
        "subdistrict_name_th",
    ]

    agg_df = (
        matched_non_bangkok.groupby(group_keys, dropna=False)
        .agg(
            village_event_row_count=("village_code_norm", "size"),
            unique_village_code_count=("village_code_norm", "nunique"),
            affected_people=("Affected People", "sum"),
            affected_households=("Affected Households", "sum"),
            deaths=("Deaths", "sum"),
            housing_damage=("Housing Damage", "sum"),
            business_damage=("Business Damage", "sum"),
            agriculture_damage=("Agriculture Damage", "sum"),
            livestock_damage=("Livestock Damage", "sum"),
            fishing_damage=("Fishing Damage", "sum"),
            transport_damage=("Transport Damage", "sum"),
            health_damage=("Health Damage", "sum"),
            utilities_damage=("Utilities Damage", "sum"),
        )
        .reset_index()
    )
    agg_df["numerator_source"] = "ddpm_master_village_disaster_stat_2557_2567"
    agg_df["module"] = "stage3_subtask5_tambon_numerator"
    agg_df["bangkok_policy_applied"] = "exclude_province_code_10_from_shared_level2"

    agg_df = agg_df.sort_values(["year_be", "disaster_type", "province_code", "district_code", "subdistrict_code"]).reset_index(drop=True)

    # Code consistency checks between source observed codes and canonical mapping (matched rows)
    src_vs_canonical = matched.copy()
    src_vs_canonical["province_code_match"] = src_vs_canonical["province_code_src_norm"] == src_vs_canonical["province_code"]
    src_vs_canonical["district_code_match"] = src_vs_canonical["district_code_src_norm"] == src_vs_canonical["district_code"]
    src_vs_canonical["subdistrict_code_match"] = src_vs_canonical["subdistrict_code_src_norm"] == src_vs_canonical["subdistrict_code"]

    metric_map = {
        "affected_people": "Affected People",
        "affected_households": "Affected Households",
        "deaths": "Deaths",
        "housing_damage": "Housing Damage",
        "business_damage": "Business Damage",
        "agriculture_damage": "Agriculture Damage",
        "livestock_damage": "Livestock Damage",
        "fishing_damage": "Fishing Damage",
        "transport_damage": "Transport Damage",
        "health_damage": "Health Damage",
        "utilities_damage": "Utilities Damage",
    }

    reconciliation: dict[str, dict[str, float]] = {}
    for out_col, src_col in metric_map.items():
        source_total = float(matched_non_bangkok[src_col].sum())
        output_total = float(agg_df[out_col].sum())
        reconciliation[out_col] = {
            "source_total_non_bangkok_matched": source_total,
            "output_total": output_total,
            "difference": output_total - source_total,
            "reconciled": bool(np.isclose(output_total, source_total)),
        }

    bangkok_rows_in_output = int((agg_df["province_code"] == "10").sum())

    # Subtask 2 Bangkok mismatch signal
    bkk_subtask2_mismatch_rows = 0
    if "P_NAME_T" in subtask2_mismatch_df.columns:
        bkk_subtask2_mismatch_rows = int((subtask2_mismatch_df["P_NAME_T"].astype(str).str.strip() == "กรุงเทพมหานคร").sum())

    unmatched_out = unmatched[
        [
            "year_be",
            "disaster_type",
            "Province Code",
            "District Code",
            "Subdistrict Code",
            "Village Code",
            "village_code_norm",
            "Affected People",
            "Affected Households",
            "Deaths",
            "Housing Damage",
            "Business Damage",
            "Agriculture Damage",
            "Livestock Damage",
            "Fishing Damage",
            "Transport Damage",
            "Health Damage",
            "Utilities Damage",
            "match_status",
        ]
    ].copy()

    null_out = null_village[
        [
            "year_be",
            "disaster_type",
            "Province Code",
            "District Code",
            "Subdistrict Code",
            "Village Code",
            "village_code_norm",
            "Affected People",
            "Affected Households",
            "Deaths",
            "Housing Damage",
            "Business Damage",
            "Agriculture Damage",
            "Livestock Damage",
            "Fishing Damage",
            "Transport Damage",
            "Health Damage",
            "Utilities Damage",
            "match_status",
        ]
    ].copy()

    ensure_parent(out_numerator)
    agg_df.to_csv(out_numerator, index=False, encoding="utf-8-sig")

    ensure_parent(out_unmatched)
    unmatched_out.to_csv(out_unmatched, index=False, encoding="utf-8-sig")

    ensure_parent(out_null_village)
    null_out.to_csv(out_null_village, index=False, encoding="utf-8-sig")

    validation = {
        "status": "ok",
        "generated_utc": utc_now_iso(),
        "module": "Subtask 5 Tambon Numerator",
        "inputs": {
            "ddpm_village_impact": in_ddpm.as_posix(),
            "dim_location_master": in_dim.as_posix(),
            "bangkok_policy_resolution": in_policy.as_posix(),
            "subtask2_tambon_mismatch_log": in_subtask2_mismatch.as_posix(),
        },
        "input_inspection": {
            "ddpm_columns": list(ddpm_df.columns),
            "dim_columns": list(dim_df.columns),
            "ddpm_row_count": int(len(ddpm_df)),
            "dim_row_count": int(len(dim_df)),
            "metric_columns_used": metric_cols,
            "canonical_key_columns_used": ["village_code", "province_code", "district_code", "subdistrict_code"],
            "village_spine_rows": int(len(village_spine)),
            "village_unique_key_count": int(village_unique["village_code_norm"].nunique()),
            "village_conflict_count": int(len(village_conflicts)),
        },
        "coverage_checks": {
            "total_ddpm_rows": int(len(joined)),
            "matched_rows": int(len(matched)),
            "matched_non_bangkok_rows": int(len(matched_non_bangkok)),
            "unmatched_village_code_rows": int(len(unmatched)),
            "null_village_code_rows": int(len(null_village)),
            "matched_rate": float(len(matched) / len(joined)) if len(joined) > 0 else 0.0,
            "unique_matched_village_codes": int(matched["village_code_norm"].nunique()),
        },
        "bangkok_policy_checks": {
            "policy_level2_shared": "exclude_bangkok",
            "matched_bangkok_rows_excluded": bangkok_excluded_rows,
            "bangkok_rows_in_output": bangkok_rows_in_output,
            "subtask2_bangkok_boundary_mismatch_rows": bkk_subtask2_mismatch_rows,
            "policy_compliant": bool(bangkok_rows_in_output == 0),
        },
        "code_consistency_checks": {
            "province_code_match_rows": int(src_vs_canonical["province_code_match"].sum()),
            "province_code_mismatch_rows": int((~src_vs_canonical["province_code_match"]).sum()),
            "district_code_match_rows": int(src_vs_canonical["district_code_match"].sum()),
            "district_code_mismatch_rows": int((~src_vs_canonical["district_code_match"]).sum()),
            "subdistrict_code_match_rows": int(src_vs_canonical["subdistrict_code_match"].sum()),
            "subdistrict_code_mismatch_rows": int((~src_vs_canonical["subdistrict_code_match"]).sum()),
        },
        "reconciliation": reconciliation,
        "outputs": {
            "tambon_numerator_csv": out_numerator.as_posix(),
            "unmatched_village_csv": out_unmatched.as_posix(),
            "null_village_code_csv": out_null_village.as_posix(),
            "validation_json": out_validation.as_posix(),
            "report_md": out_report.as_posix(),
            "tambon_numerator_row_count": int(len(agg_df)),
        },
        "blockers": [asdict(b) for b in blockers],
    }

    ensure_parent(out_validation)
    out_validation.write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")

    report_lines = [
        "# CRI Phase 1 Stage 3 — Subtask 5 Tambon Numerator Report",
        "",
        f"Generated (UTC): {validation['generated_utc']}",
        "",
        "## Inputs",
        f"- DDPM village impact: `{in_ddpm.as_posix()}`",
        f"- Canonical spine: `{in_dim.as_posix()}`",
        f"- Bangkok policy note: `{in_policy.as_posix()}`",
        f"- Subtask 2 tambon mismatch log: `{in_subtask2_mismatch.as_posix()}`",
        "",
        "## Canonical key strategy",
        "- Observed join key for tambon assignment: DDPM `Village Code` (normalized to 8 digits) -> canonical `village_code` in dim_location_master.",
        "- Canonical tambon output keys: `province_code` (2), `district_code` (4), `subdistrict_code` (6).",
        "",
        "## Coverage summary",
        f"- Total DDPM rows: {validation['coverage_checks']['total_ddpm_rows']}",
        f"- Matched rows (all provinces): {validation['coverage_checks']['matched_rows']}",
        f"- Matched rows used in shared output (non-Bangkok): {validation['coverage_checks']['matched_non_bangkok_rows']}",
        f"- Unmatched village-code rows: {validation['coverage_checks']['unmatched_village_code_rows']}",
        f"- Null village-code rows: {validation['coverage_checks']['null_village_code_rows']}",
        f"- Match rate: {validation['coverage_checks']['matched_rate']:.6f}",
        "",
        "## Bangkok policy checks",
        f"- Matched Bangkok rows excluded from shared tambon output: {validation['bangkok_policy_checks']['matched_bangkok_rows_excluded']}",
        f"- Bangkok rows present in tambon output: {validation['bangkok_policy_checks']['bangkok_rows_in_output']}",
        f"- Bangkok policy compliance (shared Level 2 exclusion): {validation['bangkok_policy_checks']['policy_compliant']}",
        f"- Bangkok mismatch rows noted from Subtask 2 log: {validation['bangkok_policy_checks']['subtask2_bangkok_boundary_mismatch_rows']}",
        "",
        "## Reconciliation checks (non-Bangkok matched source vs tambon output)",
    ]

    for metric, vals in reconciliation.items():
        report_lines.append(
            f"- {metric}: source={vals['source_total_non_bangkok_matched']:.6f}, output={vals['output_total']:.6f}, diff={vals['difference']:.6f}, reconciled={vals['reconciled']}"
        )

    report_lines.extend(
        [
            "",
            "## Outputs",
            f"- Tambon numerator CSV: `{out_numerator.as_posix()}`",
            f"- Unmatched village-code CSV: `{out_unmatched.as_posix()}`",
            f"- Null village-code CSV: `{out_null_village.as_posix()}`",
            f"- Validation JSON: `{out_validation.as_posix()}`",
            "",
            "## Scope guardrail",
            "- This module implements only Subtask 5 tambon numerator aggregation and validation artifacts.",
            "- Redistribution, provincial risk computation, tambon rendering, and spatial outputs remain out of scope.",
        ]
    )
    ensure_parent(out_report)
    out_report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "status": validation["status"],
                "outputs": validation["outputs"],
                "coverage_checks": validation["coverage_checks"],
                "bangkok_policy_checks": validation["bangkok_policy_checks"],
            },
            ensure_ascii=True,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

