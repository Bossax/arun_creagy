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
    return pd.to_numeric(cleaned, errors="coerce").fillna(0.0)


def normalize_province_name(value: Any) -> str:
    text = norm_text(value)
    if text in {"กรุงเทพ", "กทม.", "กรุงเทพฯ"}:
        return "กรุงเทพมหานคร"
    return text


def select_basis_metric(total_affected_households: float, total_affected_people: float, total_village_event_rows: float) -> str:
    if total_affected_households > 0:
        return "affected_households"
    if total_affected_people > 0:
        return "affected_people"
    if total_village_event_rows > 0:
        return "village_event_row_count"
    return "none"


def run() -> int:
    base_dir = Path(__file__).resolve().parent.parent

    in_relief_sector = base_dir / "data/1_silver/ddpm/master_financial_relief_by_sector.csv"
    in_tambon_numerator = base_dir / "data/2_gold/stage3_fact_impact_tambon_numerator.csv"
    in_denominator_province = base_dir / "data/2_gold/stage3_dim_denominator_province_worldpop_2020.csv"
    in_dim_location_master = base_dir / "data/2_gold/dim_location_master.csv"
    in_bangkok_policy = base_dir / "artifacts/reports/CRI_Phase1_Stage3_Bangkok_Policy_Resolution.md"

    out_redistributed = base_dir / "data/2_gold/stage3_fact_relief_tambon_redistributed_by_sector.csv"
    out_reconciliation = base_dir / "artifacts/reports/stage3_subtask6_relief_redistribution_reconciliation.csv"
    out_unmatched_province = base_dir / "artifacts/reports/stage3_subtask6_relief_redistribution_unmatched_province.csv"
    out_unallocated = base_dir / "artifacts/reports/stage3_subtask6_relief_redistribution_unallocated_province_year.csv"
    out_validation = base_dir / "artifacts/reports/stage3_subtask6_relief_redistribution_validation.json"
    out_report = base_dir / "artifacts/reports/CRI_Phase1_Stage3_Subtask6_Redistribution_Report.md"

    blockers: list[Blocker] = []
    for p in [
        in_relief_sector,
        in_tambon_numerator,
        in_denominator_province,
        in_dim_location_master,
        in_bangkok_policy,
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
                    "module": "Subtask 6 Relief Redistribution",
                    "blockers": [asdict(b) for b in blockers],
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        print(json.dumps({"status": "blocked", "blockers": [asdict(b) for b in blockers]}, ensure_ascii=False, indent=2))
        return 1

    relief_df = pd.read_csv(in_relief_sector, dtype=str, low_memory=False)
    numerator_df = pd.read_csv(in_tambon_numerator, dtype=str, low_memory=False)
    denominator_df = pd.read_csv(in_denominator_province, dtype=str, low_memory=False)
    dim_df = pd.read_csv(in_dim_location_master, dtype=str, low_memory=False)

    expected_relief_cols = [
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
        "รวมทั้งสิ้น",
        "วงเงินเสนอ",
        "วงเงินอนุมัติ",
        "วงเงินไม่อนุมัติ",
    ]
    expected_numerator_cols = [
        "year_be",
        "province_code",
        "province_name_th",
        "district_code",
        "district_name_th",
        "subdistrict_code",
        "subdistrict_name_th",
        "village_event_row_count",
        "affected_people",
        "affected_households",
    ]
    expected_denominator_cols = [
        "province_code",
        "province_name_th",
        "province_location_id",
        "worldpop_population_2020",
    ]
    expected_dim_cols = ["province_code", "province_name_th"]

    missing_relief = [c for c in expected_relief_cols if c not in relief_df.columns]
    missing_numerator = [c for c in expected_numerator_cols if c not in numerator_df.columns]
    missing_denominator = [c for c in expected_denominator_cols if c not in denominator_df.columns]
    missing_dim = [c for c in expected_dim_cols if c not in dim_df.columns]
    if missing_relief:
        blockers.append(Blocker(code="missing_relief_columns", message=f"Missing relief columns: {missing_relief}"))
    if missing_numerator:
        blockers.append(Blocker(code="missing_numerator_columns", message=f"Missing numerator columns: {missing_numerator}"))
    if missing_denominator:
        blockers.append(Blocker(code="missing_denominator_columns", message=f"Missing denominator columns: {missing_denominator}"))
    if missing_dim:
        blockers.append(Blocker(code="missing_dim_columns", message=f"Missing dim columns: {missing_dim}"))

    if blockers:
        ensure_parent(out_validation)
        out_validation.write_text(
            json.dumps(
                {
                    "status": "blocked",
                    "generated_utc": utc_now_iso(),
                    "module": "Subtask 6 Relief Redistribution",
                    "input_inspection": {
                        "relief_columns": list(relief_df.columns),
                        "numerator_columns": list(numerator_df.columns),
                        "denominator_columns": list(denominator_df.columns),
                        "dim_columns": list(dim_df.columns),
                        "relief_row_count": int(len(relief_df)),
                        "numerator_row_count": int(len(numerator_df)),
                        "denominator_row_count": int(len(denominator_df)),
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

    # Province map from canonical spine.
    dim_work = dim_df.copy()
    dim_work["province_code_norm"] = dim_work["province_code"].apply(lambda x: norm_code(x, 2))
    dim_work["province_name_norm"] = dim_work["province_name_th"].apply(normalize_province_name)
    province_map = dim_work[["province_code_norm", "province_name_norm"]].drop_duplicates()
    province_map = province_map[
        province_map["province_code_norm"].ne("") & province_map["province_name_norm"].ne("")
    ].copy()

    # Relief preparation.
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

    relief_work = relief_df.copy()
    relief_work["year_be"] = relief_work["ปี"].apply(lambda x: norm_code(x, 4))
    relief_work["province_name_norm"] = relief_work["จังหวัด"].apply(normalize_province_name)
    for c in sector_cols + ["รวมทั้งสิ้น", "วงเงินเสนอ", "วงเงินอนุมัติ", "วงเงินไม่อนุมัติ"]:
        relief_work[c] = to_number(relief_work[c])

    relief_work = relief_work.merge(province_map, on="province_name_norm", how="left")
    relief_work = relief_work.rename(columns={"province_code_norm": "province_code"})

    unmatched_relief = relief_work[relief_work["province_code"].isna() | relief_work["province_code"].eq("")].copy()
    matched_relief = relief_work[relief_work["province_code"].notna() & relief_work["province_code"].ne("")].copy()
    matched_relief["province_code"] = matched_relief["province_code"].astype(str).str.zfill(2)

    # Explicit Bangkok exclusion for shared lower-level redistribution.
    bangkok_excluded_relief = matched_relief[matched_relief["province_code"] == "10"].copy()
    matched_non_bangkok_relief = matched_relief[matched_relief["province_code"] != "10"].copy()

    # Candidate redistribution basis from tambon numerator.
    numerator_work = numerator_df.copy()
    numerator_work["year_be"] = numerator_work["year_be"].apply(lambda x: norm_code(x, 4))
    numerator_work["province_code"] = numerator_work["province_code"].apply(lambda x: norm_code(x, 2))
    numerator_work["district_code"] = numerator_work["district_code"].apply(lambda x: norm_code(x, 4))
    numerator_work["subdistrict_code"] = numerator_work["subdistrict_code"].apply(lambda x: norm_code(x, 6))

    for c in ["village_event_row_count", "affected_people", "affected_households"]:
        numerator_work[c] = to_number(numerator_work[c])

    basis_tambon = (
        numerator_work.groupby(
            [
                "year_be",
                "province_code",
                "province_name_th",
                "district_code",
                "district_name_th",
                "subdistrict_code",
                "subdistrict_name_th",
            ],
            dropna=False,
        )
        .agg(
            affected_households=("affected_households", "sum"),
            affected_people=("affected_people", "sum"),
            village_event_row_count=("village_event_row_count", "sum"),
        )
        .reset_index()
    )

    basis_province_year = (
        basis_tambon.groupby(["year_be", "province_code"], dropna=False)
        .agg(
            total_affected_households=("affected_households", "sum"),
            total_affected_people=("affected_people", "sum"),
            total_village_event_rows=("village_event_row_count", "sum"),
            tambon_row_count=("subdistrict_code", "size"),
            unique_tambon_count=("subdistrict_code", "nunique"),
        )
        .reset_index()
    )
    basis_province_year["selected_basis_metric"] = basis_province_year.apply(
        lambda r: select_basis_metric(
            float(r["total_affected_households"]),
            float(r["total_affected_people"]),
            float(r["total_village_event_rows"]),
        ),
        axis=1,
    )

    basis_tambon = basis_tambon.merge(
        basis_province_year[["year_be", "province_code", "selected_basis_metric"]],
        on=["year_be", "province_code"],
        how="left",
    )
    basis_tambon["basis_value"] = np.where(
        basis_tambon["selected_basis_metric"] == "affected_households",
        basis_tambon["affected_households"],
        np.where(
            basis_tambon["selected_basis_metric"] == "affected_people",
            basis_tambon["affected_people"],
            np.where(
                basis_tambon["selected_basis_metric"] == "village_event_row_count",
                basis_tambon["village_event_row_count"],
                0.0,
            ),
        ),
    )
    basis_tambon["basis_total"] = basis_tambon.groupby(["year_be", "province_code"], dropna=False)["basis_value"].transform("sum")
    basis_tambon["allocation_share"] = np.where(
        basis_tambon["basis_total"] > 0,
        basis_tambon["basis_value"] / basis_tambon["basis_total"],
        np.nan,
    )

    relief_long = matched_non_bangkok_relief[
        ["year_be", "province_code", "province_name_norm", "รวมทั้งสิ้น"] + sector_cols
    ].melt(
        id_vars=["year_be", "province_code", "province_name_norm", "รวมทั้งสิ้น"],
        value_vars=sector_cols,
        var_name="relief_sector",
        value_name="provincial_relief_baht",
    )

    relief_long = relief_long[relief_long["provincial_relief_baht"] > 0].copy()

    rel_basis = relief_long.merge(
        basis_tambon,
        on=["year_be", "province_code"],
        how="left",
    )

    rel_basis["can_allocate"] = rel_basis["selected_basis_metric"].notna() & rel_basis["basis_total"].fillna(0).gt(0)
    unallocated = rel_basis[~rel_basis["can_allocate"]].copy()

    allocated = rel_basis[rel_basis["can_allocate"]].copy()
    allocated["redistributed_relief_baht"] = allocated["provincial_relief_baht"] * allocated["allocation_share"]
    allocated["module"] = "stage3_subtask6_relief_redistribution"
    allocated["redistribution_basis"] = allocated["selected_basis_metric"]
    allocated["redistribution_policy"] = "exclude_province_code_10_from_shared_level2_and_level3"
    allocated["relief_source"] = "master_financial_relief_by_sector"
    allocated["basis_source"] = "stage3_fact_impact_tambon_numerator"
    allocated["denominator_reference"] = "stage3_dim_denominator_province_worldpop_2020"

    output_cols = [
        "year_be",
        "province_code",
        "province_name_norm",
        "district_code",
        "district_name_th",
        "subdistrict_code",
        "subdistrict_name_th",
        "relief_sector",
        "provincial_relief_baht",
        "redistributed_relief_baht",
        "redistribution_basis",
        "basis_value",
        "basis_total",
        "allocation_share",
        "module",
        "relief_source",
        "basis_source",
        "denominator_reference",
        "redistribution_policy",
    ]
    out_df = allocated[output_cols].copy()
    out_df = out_df.sort_values(["year_be", "province_code", "relief_sector", "district_code", "subdistrict_code"]).reset_index(drop=True)

    reconciliation = (
        out_df.groupby(["year_be", "province_code", "relief_sector"], dropna=False)
        .agg(
            source_total=("provincial_relief_baht", "first"),
            redistributed_total=("redistributed_relief_baht", "sum"),
            child_row_count=("subdistrict_code", "size"),
        )
        .reset_index()
    )
    reconciliation["difference"] = reconciliation["redistributed_total"] - reconciliation["source_total"]
    reconciliation["reconciled"] = np.isclose(reconciliation["redistributed_total"], reconciliation["source_total"], atol=1e-6)

    unmatched_out = unmatched_relief[
        ["จังหวัด", "ปี", "province_name_norm", "year_be", "รวมทั้งสิ้น"] + sector_cols
    ].copy()
    unmatched_out["unmatched_reason"] = "province_name_not_mapped_to_dim_location_master"

    unallocated_out = unallocated[
        [
            "year_be",
            "province_code",
            "province_name_norm",
            "relief_sector",
            "provincial_relief_baht",
            "selected_basis_metric",
            "basis_total",
        ]
    ].drop_duplicates()
    unallocated_out["unallocated_reason"] = np.where(
        unallocated_out["selected_basis_metric"].isna(),
        "no_tambon_basis_rows_for_province_year",
        "basis_total_not_positive",
    )

    ensure_parent(out_redistributed)
    out_df.to_csv(out_redistributed, index=False, encoding="utf-8-sig")

    ensure_parent(out_reconciliation)
    reconciliation.to_csv(out_reconciliation, index=False, encoding="utf-8-sig")

    ensure_parent(out_unmatched_province)
    unmatched_out.to_csv(out_unmatched_province, index=False, encoding="utf-8-sig")

    ensure_parent(out_unallocated)
    unallocated_out.to_csv(out_unallocated, index=False, encoding="utf-8-sig")

    denominator_work = denominator_df.copy()
    denominator_work["province_code"] = denominator_work["province_code"].apply(lambda x: norm_code(x, 2))
    denominator_codes = sorted(denominator_work["province_code"].dropna().unique().tolist())

    validation = {
        "status": "ok",
        "generated_utc": utc_now_iso(),
        "module": "Subtask 6 Relief Redistribution",
        "inputs": {
            "relief_sector": in_relief_sector.as_posix(),
            "tambon_numerator": in_tambon_numerator.as_posix(),
            "provincial_denominator": in_denominator_province.as_posix(),
            "dim_location_master": in_dim_location_master.as_posix(),
            "bangkok_policy_resolution": in_bangkok_policy.as_posix(),
        },
        "input_inspection": {
            "relief_columns": list(relief_df.columns),
            "numerator_columns": list(numerator_df.columns),
            "denominator_columns": list(denominator_df.columns),
            "dim_columns": list(dim_df.columns),
            "relief_row_count": int(len(relief_df)),
            "numerator_row_count": int(len(numerator_df)),
            "denominator_row_count": int(len(denominator_df)),
            "dim_row_count": int(len(dim_df)),
            "relief_sector_columns_used": sector_cols,
            "candidate_basis_metrics": ["affected_households", "affected_people", "village_event_row_count"],
        },
        "policy_checks": {
            "bangkok_relief_rows_excluded_from_shared_redistribution": int(len(bangkok_excluded_relief)),
            "bangkok_rows_in_redistributed_output": int((out_df["province_code"] == "10").sum()),
            "bangkok_policy_compliant": bool((out_df["province_code"] == "10").sum() == 0),
            "policy_note": "Bangkok excluded from shared lower-level redistribution per Stage 3 policy.",
        },
        "coverage_checks": {
            "matched_relief_rows": int(len(matched_relief)),
            "unmatched_province_rows": int(len(unmatched_out)),
            "matched_non_bangkok_relief_rows": int(len(matched_non_bangkok_relief)),
            "positive_relief_province_year_sector_rows": int(len(relief_long)),
            "allocated_province_year_sector_rows": int(reconciliation.shape[0]),
            "unallocated_province_year_sector_rows": int(len(unallocated_out)),
            "redistributed_output_rows": int(len(out_df)),
            "basis_groups": int(len(basis_province_year)),
            "basis_groups_with_metric_none": int((basis_province_year["selected_basis_metric"] == "none").sum()),
        },
        "basis_selection_summary": {
            "affected_households_groups": int((basis_province_year["selected_basis_metric"] == "affected_households").sum()),
            "affected_people_groups": int((basis_province_year["selected_basis_metric"] == "affected_people").sum()),
            "village_event_row_count_groups": int((basis_province_year["selected_basis_metric"] == "village_event_row_count").sum()),
            "none_groups": int((basis_province_year["selected_basis_metric"] == "none").sum()),
        },
        "reconciliation_checks": {
            "group_count": int(len(reconciliation)),
            "reconciled_group_count": int(reconciliation["reconciled"].sum()),
            "non_reconciled_group_count": int((~reconciliation["reconciled"]).sum()),
            "max_abs_difference": float(reconciliation["difference"].abs().max()) if len(reconciliation) > 0 else 0.0,
        },
        "null_zero_checks": {
            "null_allocation_share_rows": int(out_df["allocation_share"].isna().sum()),
            "zero_allocation_share_rows": int((out_df["allocation_share"] == 0).sum()),
            "null_redistributed_amount_rows": int(out_df["redistributed_relief_baht"].isna().sum()),
            "negative_redistributed_amount_rows": int((out_df["redistributed_relief_baht"] < 0).sum()),
        },
        "denominator_linkage_check": {
            "denominator_province_code_count": int(len(denominator_codes)),
            "redistribution_province_codes_missing_in_denominator": sorted(
                list(set(out_df["province_code"].dropna().unique().tolist()) - set(denominator_codes))
            ),
            "note": "Provincial denominator is inspected and linked by province code as a Stage 3 input dependency for downstream Level 1/Level 2 use.",
        },
        "outputs": {
            "redistributed_csv": out_redistributed.as_posix(),
            "reconciliation_csv": out_reconciliation.as_posix(),
            "unmatched_province_csv": out_unmatched_province.as_posix(),
            "unallocated_csv": out_unallocated.as_posix(),
            "validation_json": out_validation.as_posix(),
            "report_md": out_report.as_posix(),
        },
        "blockers": [asdict(b) for b in blockers],
    }

    ensure_parent(out_validation)
    out_validation.write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding="utf-8")

    report_lines = [
        "# CRI Phase 1 Stage 3 — Subtask 6 Redistribution Report",
        "",
        f"Generated (UTC): {validation['generated_utc']}",
        "",
        "## Inputs",
        f"- Provincial relief (sector): `{in_relief_sector.as_posix()}`",
        f"- Tambon numerator basis: `{in_tambon_numerator.as_posix()}`",
        f"- Provincial denominator reference: `{in_denominator_province.as_posix()}`",
        f"- Canonical spine: `{in_dim_location_master.as_posix()}`",
        f"- Bangkok policy: `{in_bangkok_policy.as_posix()}`",
        "",
        "## Redistribution basis and method",
        "- Basis candidates from observed Stage 3 tambon numerator fields: `affected_households`, `affected_people`, `village_event_row_count`.",
        "- Province-year basis selection priority: `affected_households` -> `affected_people` -> `village_event_row_count` -> unresolved (`none`).",
        "- Relief sectors are redistributed from provincial totals to tambon rows by province-year allocation shares from the selected basis metric.",
        "- Shared lower-level Bangkok exclusion is enforced (`province_code=10` removed before redistribution).",
        "",
        "## Coverage and policy checks",
        f"- Matched relief rows: {validation['coverage_checks']['matched_relief_rows']}",
        f"- Unmatched province rows: {validation['coverage_checks']['unmatched_province_rows']}",
        f"- Positive relief province-year-sector rows: {validation['coverage_checks']['positive_relief_province_year_sector_rows']}",
        f"- Allocated province-year-sector rows: {validation['coverage_checks']['allocated_province_year_sector_rows']}",
        f"- Unallocated province-year-sector rows: {validation['coverage_checks']['unallocated_province_year_sector_rows']}",
        f"- Bangkok relief rows excluded from shared redistribution: {validation['policy_checks']['bangkok_relief_rows_excluded_from_shared_redistribution']}",
        f"- Bangkok rows in redistributed output: {validation['policy_checks']['bangkok_rows_in_redistributed_output']}",
        "",
        "## Reconciliation and quality",
        f"- Reconciliation groups: {validation['reconciliation_checks']['group_count']}",
        f"- Non-reconciled groups: {validation['reconciliation_checks']['non_reconciled_group_count']}",
        f"- Max absolute source-vs-redistributed difference: {validation['reconciliation_checks']['max_abs_difference']}",
        f"- Negative redistributed amount rows: {validation['null_zero_checks']['negative_redistributed_amount_rows']}",
        "",
        "## Outputs",
        f"- Redistributed relief CSV: `{out_redistributed.as_posix()}`",
        f"- Reconciliation CSV: `{out_reconciliation.as_posix()}`",
        f"- Unmatched province CSV: `{out_unmatched_province.as_posix()}`",
        f"- Unallocated province-year-sector CSV: `{out_unallocated.as_posix()}`",
        f"- Validation JSON: `{out_validation.as_posix()}`",
        "",
        "## Scope guardrail",
        "- This module implements only Stage 3 Subtask 6 redistribution outputs and validation evidence.",
        "- Final Level 1/Level 2 products, visualization, and end-to-end integrity checks remain out of scope.",
    ]

    ensure_parent(out_report)
    out_report.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "status": validation["status"],
                "outputs": validation["outputs"],
                "coverage_checks": validation["coverage_checks"],
                "policy_checks": validation["policy_checks"],
                "reconciliation_checks": validation["reconciliation_checks"],
            },
            ensure_ascii=True,
            indent=2,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(run())

