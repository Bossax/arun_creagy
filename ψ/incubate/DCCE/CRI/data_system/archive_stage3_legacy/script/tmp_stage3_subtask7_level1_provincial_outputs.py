from __future__ import annotations

import json
import re
import sys
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
    return pd.to_numeric(cleaned, errors="coerce").fillna(0.0)


def normalize_province_name(value: Any) -> str:
    text = norm_text(value)
    if text in {"กรุงเทพ", "กทม.", "กรุงเทพฯ"}:
        return "กรุงเทพมหานคร"
    return text


def run() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")

    base_dir = Path(__file__).resolve().parent.parent

    in_denominator = base_dir / "data/2_gold/stage3_dim_denominator_province_worldpop_2020.csv"
    in_impact_tambon = base_dir / "data/2_gold/stage3_fact_impact_tambon_numerator.csv"
    in_relief_redistributed = base_dir / "data/2_gold/stage3_fact_relief_tambon_redistributed_by_sector.csv"
    in_relief_source = base_dir / "data/1_silver/ddpm/master_financial_relief_by_sector.csv"
    in_dim = base_dir / "data/2_gold/dim_location_master.csv"
    in_policy = base_dir / "artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md"
    in_subtask4_validation = base_dir / "artifacts/reports/stage3_subtask4_provincial_denominator_validation.json"
    in_subtask5_validation = base_dir / "artifacts/reports/stage3_subtask5_tambon_numerator_validation.json"
    in_subtask6_validation = base_dir / "artifacts/reports/stage3_subtask6_relief_redistribution_validation.json"

    out_impact_level1 = base_dir / "data/2_gold/stage3_fact_level1_impact_province_year_disaster.csv"
    out_relief_level1 = base_dir / "data/2_gold/stage3_fact_level1_relief_province_year_sector.csv"
    out_validation = base_dir / "artifacts/reports/stage3_subtask7_level1_provincial_validation.json"
    out_report = base_dir / "artifacts/reports/CRI_Phase1_Stage3_Subtask7_Level1_Provincial_Outputs_Report.md"

    blockers: list[Blocker] = []

    for p in [
        in_denominator,
        in_impact_tambon,
        in_relief_redistributed,
        in_relief_source,
        in_dim,
        in_policy,
        in_subtask4_validation,
        in_subtask5_validation,
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
                    "module": "Subtask 7 Level 1 Provincial Outputs",
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 1

    denominator_df = pd.read_csv(in_denominator, low_memory=False)
    impact_tambon_df = pd.read_csv(in_impact_tambon, low_memory=False)
    relief_redistributed_df = pd.read_csv(in_relief_redistributed, low_memory=False)
    relief_source_df = pd.read_csv(in_relief_source, dtype=str, low_memory=False)
    dim_df = pd.read_csv(in_dim, dtype=str, low_memory=False)

    required_denominator_cols = [
        "province_code",
        "province_name_th",
        "province_location_id",
        "worldpop_population_2020",
        "match_status",
    ]
    required_impact_cols = [
        "year_be",
        "disaster_type",
        "province_code",
        "province_name_th",
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
        "village_event_row_count",
        "unique_village_code_count",
    ]
    required_redist_cols = [
        "year_be",
        "province_code",
        "relief_sector",
        "provincial_relief_baht",
        "redistributed_relief_baht",
    ]
    required_relief_source_cols = [
        "จังหวัด",
        "ปี",
        "ด้านดำรงชีพ",
        "ด้านสังคมสงเคราะห์",
        "ด้านการแพทย์และสาธารณสุข",
        "ด้านเกษตร_พืช",
        "ด้านเกษตร_ประมง",
        "ด้านเกษตร_ปศุสัตว์",
        "ด้านเกษตร_อื่น",
        "ด้านบรรเทาสาธารณภัย",
        "ด้านการปฏิบัติงานบรรเทาทุกข์",
        "เชิงป้องกันหรือยับยั้ง",
    ]
    required_dim_cols = ["province_code", "province_name_th"]

    miss_denom = [c for c in required_denominator_cols if c not in denominator_df.columns]
    miss_impact = [c for c in required_impact_cols if c not in impact_tambon_df.columns]
    miss_redist = [c for c in required_redist_cols if c not in relief_redistributed_df.columns]
    miss_source = [c for c in required_relief_source_cols if c not in relief_source_df.columns]
    miss_dim = [c for c in required_dim_cols if c not in dim_df.columns]

    if miss_denom:
        blockers.append(Blocker(code="missing_denominator_columns", message=f"Missing denominator columns: {miss_denom}"))
    if miss_impact:
        blockers.append(Blocker(code="missing_impact_columns", message=f"Missing impact columns: {miss_impact}"))
    if miss_redist:
        blockers.append(Blocker(code="missing_redistributed_columns", message=f"Missing redistributed relief columns: {miss_redist}"))
    if miss_source:
        blockers.append(Blocker(code="missing_relief_source_columns", message=f"Missing relief source columns: {miss_source}"))
    if miss_dim:
        blockers.append(Blocker(code="missing_dim_columns", message=f"Missing dim columns: {miss_dim}"))

    if blockers:
        ensure_parent(out_validation)
        out_validation.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "module": "Subtask 7 Level 1 Provincial Outputs",
                    "input_inspection": {
                        "denominator_columns": list(denominator_df.columns),
                        "impact_tambon_columns": list(impact_tambon_df.columns),
                        "relief_redistributed_columns": list(relief_redistributed_df.columns),
                        "relief_source_columns": list(relief_source_df.columns),
                        "dim_columns": list(dim_df.columns),
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

    # Canonical province map from observed dim_location_master province rows.
    dim_work = dim_df.copy()
    dim_work["province_code_norm"] = dim_work["province_code"].apply(lambda x: norm_code(x, 2))
    dim_work["province_name_norm"] = dim_work["province_name_th"].apply(normalize_province_name)
    province_map = (
        dim_work[["province_code_norm", "province_name_norm"]]
        .drop_duplicates()
        .query("province_code_norm != '' and province_name_norm != ''")
        .copy()
    )

    # Level 1 impact output from Subtask 5 tambon numerator.
    impact = impact_tambon_df.copy()
    impact["year_be"] = impact["year_be"].apply(lambda x: norm_code(x, 4))
    impact["province_code"] = impact["province_code"].apply(lambda x: norm_code(x, 2))
    impact["province_name_th"] = impact["province_name_th"].apply(norm_text)

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
    for c in impact_metrics:
        impact[c] = to_number(impact[c])

    impact_level1 = (
        impact.groupby(["year_be", "province_code", "province_name_th", "disaster_type"], dropna=False)[impact_metrics]
        .sum()
        .reset_index()
    )
    impact_level1["module"] = "stage3_subtask7_level1_provincial_outputs"
    impact_level1["impact_source"] = "stage3_fact_impact_tambon_numerator"
    impact_level1["bangkok_policy_note"] = "bangkok_not_present_in_subtask5_shared_level2_input"

    # Level 1 relief output from source provincial relief + Subtask 6 redistributed evidence.
    sector_cols = [
        "ด้านดำรงชีพ",
        "ด้านสังคมสงเคราะห์",
        "ด้านการแพทย์และสาธารณสุข",
        "ด้านเกษตร_พืช",
        "ด้านเกษตร_ประมง",
        "ด้านเกษตร_ปศุสัตว์",
        "ด้านเกษตร_อื่น",
        "ด้านบรรเทาสาธารณภัย",
        "ด้านการปฏิบัติงานบรรเทาทุกข์",
        "เชิงป้องกันหรือยับยั้ง",
    ]

    relief_source = relief_source_df.copy()
    relief_source["year_be"] = relief_source["ปี"].apply(lambda x: norm_code(x, 4))
    relief_source["province_name_norm"] = relief_source["จังหวัด"].apply(normalize_province_name)
    for c in sector_cols:
        relief_source[c] = to_number(relief_source[c])

    relief_source = relief_source.merge(province_map, on="province_name_norm", how="left")
    relief_source = relief_source.rename(columns={"province_code_norm": "province_code"})
    relief_source["province_code"] = relief_source["province_code"].apply(lambda x: norm_code(x, 2))

    relief_source_unmatched = relief_source[relief_source["province_code"] == ""].copy()
    relief_source_matched = relief_source[relief_source["province_code"] != ""].copy()

    relief_source_long = relief_source_matched[
        ["year_be", "province_code", "province_name_norm"] + sector_cols
    ].melt(
        id_vars=["year_be", "province_code", "province_name_norm"],
        value_vars=sector_cols,
        var_name="relief_sector",
        value_name="provincial_relief_baht_source",
    )
    relief_source_long = relief_source_long[relief_source_long["provincial_relief_baht_source"] > 0].copy()

    relief_redist = relief_redistributed_df.copy()
    relief_redist["year_be"] = relief_redist["year_be"].apply(lambda x: norm_code(x, 4))
    relief_redist["province_code"] = relief_redist["province_code"].apply(lambda x: norm_code(x, 2))
    relief_redist["redistributed_relief_baht"] = to_number(relief_redist["redistributed_relief_baht"])

    relief_redist_level1 = (
        relief_redist.groupby(["year_be", "province_code", "relief_sector"], dropna=False)
        .agg(redistributed_relief_baht_from_subtask6=("redistributed_relief_baht", "sum"))
        .reset_index()
    )

    relief_level1 = relief_source_long.merge(
        relief_redist_level1,
        on=["year_be", "province_code", "relief_sector"],
        how="left",
    )
    relief_level1["redistributed_relief_baht_from_subtask6"] = (
        relief_level1["redistributed_relief_baht_from_subtask6"].fillna(0.0)
    )
    relief_level1["unallocated_relief_gap_baht"] = (
        relief_level1["provincial_relief_baht_source"] - relief_level1["redistributed_relief_baht_from_subtask6"]
    )

    def relief_status(row: pd.Series) -> str:
        if row["province_code"] == "10":
            return "bangkok_level1_source_only_policy"
        if np.isclose(float(row["unallocated_relief_gap_baht"]), 0.0, atol=1e-6):
            return "reconciled_with_subtask6_redistribution"
        if np.isclose(float(row["redistributed_relief_baht_from_subtask6"]), 0.0, atol=1e-6):
            return "no_shared_lower_level_basis_or_unallocated"
        return "partial_allocation_gap"

    relief_level1["redistribution_coverage_status"] = relief_level1.apply(relief_status, axis=1)
    relief_level1["module"] = "stage3_subtask7_level1_provincial_outputs"
    relief_level1["relief_source"] = "master_financial_relief_by_sector"
    relief_level1["redistribution_reference"] = "stage3_fact_relief_tambon_redistributed_by_sector"

    # Denominator checks.
    denominator = denominator_df.copy()
    denominator["province_code"] = denominator["province_code"].apply(lambda x: norm_code(x, 2))
    denominator["worldpop_population_2020"] = to_number(denominator["worldpop_population_2020"])

    denom_codes = sorted(denominator["province_code"].dropna().unique().tolist())
    impact_codes = sorted(impact_level1["province_code"].dropna().unique().tolist())
    relief_codes = sorted(relief_level1["province_code"].dropna().unique().tolist())

    ensure_parent(out_impact_level1)
    impact_level1.to_csv(out_impact_level1, index=False, encoding="utf-8-sig")

    ensure_parent(out_relief_level1)
    relief_level1.to_csv(out_relief_level1, index=False, encoding="utf-8-sig")

    # Reconciliation evidence.
    impact_reconciliation: dict[str, dict[str, float | bool]] = {}
    for metric in impact_metrics:
        src_total = float(impact[metric].sum())
        out_total = float(impact_level1[metric].sum())
        impact_reconciliation[metric] = {
            "source_total_from_subtask5": src_total,
            "level1_output_total": out_total,
            "difference": out_total - src_total,
            "reconciled": bool(np.isclose(out_total, src_total, atol=1e-6)),
        }

    relief_source_total = float(relief_source_long["provincial_relief_baht_source"].sum())
    relief_output_source_total = float(relief_level1["provincial_relief_baht_source"].sum())
    relief_output_redistributed_total = float(relief_level1["redistributed_relief_baht_from_subtask6"].sum())
    relief_output_gap_total = float(relief_level1["unallocated_relief_gap_baht"].sum())

    validation = {
        "status": "ok",
        "generated_utc": utc_now_iso(),
        "module": "Subtask 7 Level 1 Provincial Outputs",
        "inputs": {
            "denominator": in_denominator.as_posix(),
            "impact_tambon_numerator": in_impact_tambon.as_posix(),
            "relief_tambon_redistributed": in_relief_redistributed.as_posix(),
            "relief_source": in_relief_source.as_posix(),
            "dim_location_master": in_dim.as_posix(),
            "bangkok_policy_resolution": in_policy.as_posix(),
            "subtask4_validation": in_subtask4_validation.as_posix(),
            "subtask5_validation": in_subtask5_validation.as_posix(),
            "subtask6_validation": in_subtask6_validation.as_posix(),
        },
        "input_inspection": {
            "denominator_columns": list(denominator_df.columns),
            "impact_tambon_columns": list(impact_tambon_df.columns),
            "relief_redistributed_columns": list(relief_redistributed_df.columns),
            "relief_source_columns": list(relief_source_df.columns),
            "dim_columns": list(dim_df.columns),
            "denominator_row_count": int(len(denominator_df)),
            "impact_tambon_row_count": int(len(impact_tambon_df)),
            "relief_redistributed_row_count": int(len(relief_redistributed_df)),
            "relief_source_row_count": int(len(relief_source_df)),
            "dim_row_count": int(len(dim_df)),
        },
        "output_schemas": {
            "impact_level1_columns": list(impact_level1.columns),
            "relief_level1_columns": list(relief_level1.columns),
        },
        "coverage_checks": {
            "denominator_province_count": int(len(denom_codes)),
            "impact_level1_province_count": int(len(impact_codes)),
            "relief_level1_province_count": int(len(relief_codes)),
            "impact_province_codes_missing_from_denominator": sorted(list(set(impact_codes) - set(denom_codes))),
            "relief_province_codes_missing_from_denominator": sorted(list(set(relief_codes) - set(denom_codes))),
            "denominator_province_codes_missing_from_impact": sorted(list(set(denom_codes) - set(impact_codes))),
            "denominator_province_codes_missing_from_relief": sorted(list(set(denom_codes) - set(relief_codes))),
            "relief_source_unmatched_province_rows": int(len(relief_source_unmatched)),
        },
        "bangkok_policy_checks": {
            "bangkok_present_in_denominator": bool((denominator["province_code"] == "10").any()),
            "bangkok_rows_in_impact_level1": int((impact_level1["province_code"] == "10").sum()),
            "bangkok_rows_in_relief_level1": int((relief_level1["province_code"] == "10").sum()),
            "bangkok_relief_source_total_baht": float(
                relief_level1.loc[relief_level1["province_code"] == "10", "provincial_relief_baht_source"].sum()
            ),
            "bangkok_relief_redistributed_total_baht": float(
                relief_level1.loc[
                    relief_level1["province_code"] == "10", "redistributed_relief_baht_from_subtask6"
                ].sum()
            ),
            "bangkok_level1_policy_note": "Bangkok included at Level 1 via denominator and provincial relief source; shared lower-level redistributed stream remains zero by policy.",
        },
        "denominator_integrity_checks": {
            "denominator_unique_province_codes": int(denominator["province_code"].nunique()),
            "denominator_null_population_rows": int(denominator["worldpop_population_2020"].isna().sum()),
            "denominator_nonpositive_population_rows": int((denominator["worldpop_population_2020"] <= 0).sum()),
            "denominator_non_matched_rows": int((denominator["match_status"].astype(str) != "matched").sum()),
        },
        "reconciliation_checks": {
            "impact_from_subtask5_to_level1": impact_reconciliation,
            "relief_source_total_baht": relief_source_total,
            "relief_level1_source_total_baht": relief_output_source_total,
            "relief_level1_redistributed_total_baht": relief_output_redistributed_total,
            "relief_level1_unallocated_gap_total_baht": relief_output_gap_total,
            "relief_source_to_level1_source_reconciled": bool(
                np.isclose(relief_source_total, relief_output_source_total, atol=1e-6)
            ),
            "relief_source_equals_redistributed_reconciled": bool(
                np.isclose(relief_output_source_total, relief_output_redistributed_total, atol=1e-6)
            ),
        },
        "outputs": {
            "impact_level1_csv": out_impact_level1.as_posix(),
            "relief_level1_csv": out_relief_level1.as_posix(),
            "validation_json": out_validation.as_posix(),
            "report_md": out_report.as_posix(),
            "impact_level1_row_count": int(len(impact_level1)),
            "relief_level1_row_count": int(len(relief_level1)),
        },
        "blockers": [asdict(b) for b in blockers],
        "unresolved_blockers": [
            {
                "code": "level1_impact_bangkok_not_observed_in_shared_input",
                "message": "Bangkok impact rows are not present in stage3_fact_impact_tambon_numerator because shared Level 2 excludes Bangkok by policy; no Bangkok impact contribution is fabricated in Level 1 impact output.",
            },
            {
                "code": "relief_unallocated_gaps_from_subtask6_persist",
                "message": "Subtask 6 unallocated province-year-sector gaps remain visible in Level 1 relief output via unallocated_relief_gap_baht and are not silently corrected.",
            },
            {
                "code": "non_spatial_relief_rows_unmatched",
                "message": "Some relief source rows (e.g., non-spatial agency rows) remain unmatched to canonical province codes and are excluded from Level 1 province output.",
            },
        ],
    }

    ensure_parent(out_validation)
    out_validation.write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")

    report_lines = [
        "# CRI Phase 1 Stage 3 — Subtask 7 Level 1 Provincial Outputs Report",
        "",
        f"Generated (UTC): {validation['generated_utc']}",
        "",
        "## Inputs",
        f"- Denominator: `{in_denominator.as_posix()}`",
        f"- Tambon numerator (Subtask 5): `{in_impact_tambon.as_posix()}`",
        f"- Redistributed relief (Subtask 6): `{in_relief_redistributed.as_posix()}`",
        f"- Provincial relief source: `{in_relief_source.as_posix()}`",
        f"- Canonical spine: `{in_dim.as_posix()}`",
        f"- Bangkok policy note: `{in_policy.as_posix()}`",
        "",
        "## Output artifacts",
        f"- Level 1 impact CSV: `{out_impact_level1.as_posix()}`",
        f"- Level 1 relief CSV: `{out_relief_level1.as_posix()}`",
        f"- Validation JSON: `{out_validation.as_posix()}`",
        "",
        "## Implemented Level 1 logic",
        "- Impact Level 1 is aggregated from `stage3_fact_impact_tambon_numerator` by (`year_be`, `province_code`, `province_name_th`, `disaster_type`).",
        "- Relief Level 1 uses province-year-sector values from `master_financial_relief_by_sector` mapped to canonical province codes via observed `dim_location_master` province names.",
        "- Subtask 6 redistributed relief is aggregated to province-year-sector and joined for explicit allocation-gap accounting.",
        "- Bangkok is included at Level 1 through denominator and provincial relief source; lower-level redistributed Bangkok remains zero by policy.",
        "",
        "## Validation highlights",
        f"- Denominator province coverage: {validation['coverage_checks']['denominator_province_count']} provinces.",
        f"- Impact Level 1 province coverage: {validation['coverage_checks']['impact_level1_province_count']} provinces.",
        f"- Relief Level 1 province coverage: {validation['coverage_checks']['relief_level1_province_count']} provinces.",
        f"- Bangkok rows in impact Level 1: {validation['bangkok_policy_checks']['bangkok_rows_in_impact_level1']}.",
        f"- Bangkok rows in relief Level 1: {validation['bangkok_policy_checks']['bangkok_rows_in_relief_level1']}.",
        f"- Relief source total equals Level 1 source total: {validation['reconciliation_checks']['relief_source_to_level1_source_reconciled']}.",
        f"- Relief source total equals redistributed total: {validation['reconciliation_checks']['relief_source_equals_redistributed_reconciled']}.",
        "",
        "## Unresolved blockers preserved",
        "- Bangkok impact is absent from shared Level 2-derived impact input and is not fabricated.",
        "- Subtask 6 unallocated redistribution gaps are retained as explicit residuals.",
        "- Unmatched non-spatial relief rows remain excluded from province outputs.",
    ]

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

