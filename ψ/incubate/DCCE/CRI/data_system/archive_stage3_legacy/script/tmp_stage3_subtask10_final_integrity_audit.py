from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import pandas as pd


def _configure_utf8_output() -> None:
    try:
        import sys

        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _normalize_code(value: Any, width: Optional[int] = None) -> Optional[str]:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    s = str(value).strip()
    if s == "" or s.lower() in {"nan", "none", "null"}:
        return None
    if s.endswith(".0"):
        s = s[:-2]
    if width is not None and s.isdigit():
        s = s.zfill(width)
    return s


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, low_memory=False)


def _artifact_check(path: Path, kind: str) -> Dict[str, Any]:
    row: Dict[str, Any] = {
        "artifact_path": str(path),
        "artifact_kind": kind,
        "exists": path.exists(),
        "is_readable": False,
        "read_error": None,
        "row_count": None,
        "column_count": None,
        "columns": None,
    }
    if not path.exists():
        row["read_error"] = "missing"
        return row

    try:
        if kind == "csv":
            df = _read_csv(path)
            row["is_readable"] = True
            row["row_count"] = int(len(df))
            row["column_count"] = int(len(df.columns))
            row["columns"] = "|".join(map(str, df.columns.tolist()))
        elif kind == "json":
            with path.open("r", encoding="utf-8") as f:
                obj = json.load(f)
            row["is_readable"] = True
            row["row_count"] = None
            row["column_count"] = None
            row["columns"] = f"json_type={type(obj).__name__}"
        elif kind == "md":
            _ = path.read_text(encoding="utf-8")
            row["is_readable"] = True
        elif kind == "tif":
            import rasterio

            with rasterio.open(path) as ds:
                row["is_readable"] = True
                row["row_count"] = int(ds.height)
                row["column_count"] = int(ds.width)
                row["columns"] = f"crs={ds.crs};count={ds.count};nodata={ds.nodata}"
        else:
            _ = path.read_bytes()
            row["is_readable"] = True
    except Exception as e:
        row["read_error"] = f"{type(e).__name__}: {e}"
    return row


def _fk_check_province(df: pd.DataFrame, table_name: str, code_col: str, province_keys: set[str]) -> Dict[str, Any]:
    observed = df[code_col].map(lambda x: _normalize_code(x, 2))
    total = int(len(observed))
    nulls = int(observed.isna().sum())
    missing_mask = observed.notna() & (~observed.isin(province_keys))
    missing = int(missing_mask.sum())
    sample = sorted(set(observed[missing_mask].dropna().tolist()))[:20]
    return {
        "check_name": f"fk_{table_name}_to_dim_location_master_province",
        "table_name": table_name,
        "key_columns": code_col,
        "fk_target": "dim_location_master.province_code",
        "total_rows": total,
        "null_key_rows": nulls,
        "missing_fk_rows": missing,
        "pass": (missing == 0 and nulls == 0),
        "missing_key_sample": "|".join(sample),
    }


def _fk_check_tambon(
    df: pd.DataFrame,
    table_name: str,
    key_cols: Tuple[str, str, str],
    tambon_keys: set[Tuple[str, str, str]],
) -> Dict[str, Any]:
    p, d, s = key_cols
    keys: List[Optional[Tuple[str, str, str]]] = []
    nulls = 0
    for _, r in df[[p, d, s]].iterrows():
        kp = _normalize_code(r[p], 2)
        kd = _normalize_code(r[d], 2)
        ks = _normalize_code(r[s], 2)
        if kp is None or kd is None or ks is None:
            keys.append(None)
            nulls += 1
        else:
            keys.append((kp, kd, ks))

    total = len(keys)
    missing_keys = [k for k in keys if k is not None and k not in tambon_keys]
    missing = len(missing_keys)
    sample = sorted(set(missing_keys))[:20]
    sample_str = "|".join(["-".join(x) for x in sample])
    return {
        "check_name": f"fk_{table_name}_to_dim_location_master_tambon",
        "table_name": table_name,
        "key_columns": ",".join(key_cols),
        "fk_target": "dim_location_master.(province_code,district_code,subdistrict_code)",
        "total_rows": int(total),
        "null_key_rows": int(nulls),
        "missing_fk_rows": int(missing),
        "pass": (missing == 0 and nulls == 0),
        "missing_key_sample": sample_str,
    }


def _sum_shared_numeric(
    upstream: pd.DataFrame,
    downstream: pd.DataFrame,
    keys: List[str],
    exclude_numeric_cols: Optional[Iterable[str]] = None,
) -> Dict[str, Any]:
    exclude = set(exclude_numeric_cols or [])
    shared = [
        c
        for c in upstream.columns
        if c in downstream.columns and c not in keys and pd.api.types.is_numeric_dtype(upstream[c]) and pd.api.types.is_numeric_dtype(downstream[c])
    ]
    shared = [c for c in shared if c not in exclude]

    if not shared:
        return {
            "checked_columns": "",
            "max_abs_diff": None,
            "sum_abs_diff": None,
            "row_mismatch_count": None,
            "pass": False,
            "note": "no_shared_numeric_columns",
        }

    ug = upstream.groupby(keys, dropna=False)[shared].sum(numeric_only=True).reset_index()
    dg = downstream.groupby(keys, dropna=False)[shared].sum(numeric_only=True).reset_index()

    m = ug.merge(dg, on=keys, how="outer", suffixes=("_up", "_down")).fillna(0)
    max_abs = 0.0
    sum_abs = 0.0
    row_mismatch = 0
    for c in shared:
        diff = (m[f"{c}_up"] - m[f"{c}_down"]).abs()
        max_abs = max(max_abs, float(diff.max()))
        sum_abs += float(diff.sum())
        row_mismatch += int((diff > 1e-8).sum())

    return {
        "checked_columns": "|".join(shared),
        "max_abs_diff": max_abs,
        "sum_abs_diff": sum_abs,
        "row_mismatch_count": row_mismatch,
        "pass": max_abs <= 1e-8,
        "note": "",
    }


def main() -> None:
    _configure_utf8_output()

    root = Path(__file__).resolve().parents[1]
    gold = root / "data" / "2_gold"
    silver_dopa = root / "data" / "1_silver" / "dopa"
    reports = root / "artifacts" / "reports"
    reports.mkdir(parents=True, exist_ok=True)

    relief_recon_tolerance = 1e-7

    core_artifacts: List[Tuple[Path, str]] = [
        (gold / "dim_location_master.csv", "csv"),
        (gold / "stage3_dim_denominator_province_worldpop_2020.csv", "csv"),
        (gold / "stage3_fact_impact_tambon_numerator.csv", "csv"),
        (gold / "stage3_fact_relief_tambon_redistributed_by_sector.csv", "csv"),
        (gold / "stage3_fact_level1_impact_province_year_disaster.csv", "csv"),
        (gold / "stage3_fact_level1_relief_province_year_sector.csv", "csv"),
        (gold / "stage3_fact_level2_impact_tambon_year_disaster.csv", "csv"),
        (gold / "stage3_fact_level2_relief_tambon_year_sector.csv", "csv"),
        (gold / "stage3_level3_worldpop_2020_non_bangkok_matched_tambon.tif", "tif"),
        (gold / "stage3_level3_tambon_eligibility_mask_non_bangkok.tif", "tif"),
        (silver_dopa / "stage3_dopa_tambon_boundary_code_crosswalk.csv", "csv"),
        (silver_dopa / "stage3_dopa_province_boundary_code_crosswalk.csv", "csv"),
        (reports / "stage3_subtask6_relief_redistribution_reconciliation.csv", "csv"),
        (reports / "stage3_subtask7_level1_provincial_validation.json", "json"),
        (reports / "stage3_subtask8_level2_tambon_validation.json", "json"),
        (reports / "stage3_subtask9_level3_spatial_validation.json", "json"),
        (reports / "stage3_subtask9_level3_tambon_key_coverage.csv", "csv"),
        (reports / "CRI_Phase1_Stage3_Subtask4_Provincial_Denominator_Report.md", "md"),
        (reports / "CRI_Phase1_Stage3_Subtask5_Tambon_Numerator_Report.md", "md"),
        (reports / "CRI_Phase1_Stage3_Subtask6_Redistribution_Report.md", "md"),
        (reports / "CRI_Phase1_Stage3_Subtask7_Level1_Provincial_Outputs_Report.md", "md"),
        (reports / "CRI_Phase1_Stage3_Subtask8_Level2_Tambon_Outputs_Report.md", "md"),
        (reports / "CRI_Phase1_Stage3_Subtask9_Level3_Spatial_Outputs_Report.md", "md"),
    ]

    artifact_rows = [_artifact_check(p, k) for p, k in core_artifacts]
    artifact_df = pd.DataFrame(artifact_rows)
    artifact_df.to_csv(reports / "stage3_subtask10_final_integrity_artifact_readability.csv", index=False, encoding="utf-8-sig")

    required_csvs = {
        "dim": gold / "dim_location_master.csv",
        "denominator": gold / "stage3_dim_denominator_province_worldpop_2020.csv",
        "impact_tambon": gold / "stage3_fact_impact_tambon_numerator.csv",
        "relief_redistributed": gold / "stage3_fact_relief_tambon_redistributed_by_sector.csv",
        "level1_impact": gold / "stage3_fact_level1_impact_province_year_disaster.csv",
        "level1_relief": gold / "stage3_fact_level1_relief_province_year_sector.csv",
        "level2_impact": gold / "stage3_fact_level2_impact_tambon_year_disaster.csv",
        "level2_relief": gold / "stage3_fact_level2_relief_tambon_year_sector.csv",
        "level3_key_coverage": reports / "stage3_subtask9_level3_tambon_key_coverage.csv",
        "subtask6_recon": reports / "stage3_subtask6_relief_redistribution_reconciliation.csv",
        "crosswalk_tambon": silver_dopa / "stage3_dopa_tambon_boundary_code_crosswalk.csv",
    }

    for name, p in required_csvs.items():
        if not p.exists():
            raise FileNotFoundError(f"Missing required CSV for Subtask 10: {name} -> {p}")

    dim = _read_csv(required_csvs["dim"])
    denominator = _read_csv(required_csvs["denominator"])
    impact_tambon = _read_csv(required_csvs["impact_tambon"])
    relief_redistributed = _read_csv(required_csvs["relief_redistributed"])
    level1_impact = _read_csv(required_csvs["level1_impact"])
    level1_relief = _read_csv(required_csvs["level1_relief"])
    level2_impact = _read_csv(required_csvs["level2_impact"])
    level2_relief = _read_csv(required_csvs["level2_relief"])
    level3_key_coverage = _read_csv(required_csvs["level3_key_coverage"])
    subtask6_recon = _read_csv(required_csvs["subtask6_recon"])
    crosswalk_tambon = _read_csv(required_csvs["crosswalk_tambon"])

    province_col = "province_code"
    district_col = "district_code"
    subdistrict_col = "subdistrict_code"
    for c in [province_col, district_col, subdistrict_col]:
        if c not in dim.columns:
            raise KeyError(f"dim_location_master missing required key column: {c}")

    dim_province = set(
        dim[province_col].map(lambda x: _normalize_code(x, 2)).dropna().tolist()
    )
    dim_tambon_rows = dim.dropna(subset=[province_col, district_col, subdistrict_col])
    dim_tambon = set(
        zip(
            dim_tambon_rows[province_col].map(lambda x: _normalize_code(x, 2)),
            dim_tambon_rows[district_col].map(lambda x: _normalize_code(x, 2)),
            dim_tambon_rows[subdistrict_col].map(lambda x: _normalize_code(x, 2)),
        )
    )

    fk_rows: List[Dict[str, Any]] = []
    fk_rows.append(_fk_check_province(denominator, "stage3_dim_denominator_province_worldpop_2020", "province_code", dim_province))
    fk_rows.append(_fk_check_tambon(impact_tambon, "stage3_fact_impact_tambon_numerator", ("province_code", "district_code", "subdistrict_code"), dim_tambon))
    fk_rows.append(_fk_check_tambon(relief_redistributed, "stage3_fact_relief_tambon_redistributed_by_sector", ("province_code", "district_code", "subdistrict_code"), dim_tambon))
    fk_rows.append(_fk_check_province(level1_impact, "stage3_fact_level1_impact_province_year_disaster", "province_code", dim_province))
    fk_rows.append(_fk_check_province(level1_relief, "stage3_fact_level1_relief_province_year_sector", "province_code", dim_province))
    fk_rows.append(_fk_check_tambon(level2_impact, "stage3_fact_level2_impact_tambon_year_disaster", ("province_code", "district_code", "subdistrict_code"), dim_tambon))
    fk_rows.append(_fk_check_tambon(level2_relief, "stage3_fact_level2_relief_tambon_year_sector", ("province_code", "district_code", "subdistrict_code"), dim_tambon))

    fk_df = pd.DataFrame(fk_rows)
    fk_df.to_csv(reports / "stage3_subtask10_final_integrity_fk_checks.csv", index=False, encoding="utf-8-sig")

    recon_rows: List[Dict[str, Any]] = []

    r1 = _sum_shared_numeric(
        upstream=impact_tambon,
        downstream=level1_impact,
        keys=["year_be", "province_code", "disaster_type"],
    )
    recon_rows.append(
        {
            "check_name": "recon_subtask5_tambon_to_level1_impact",
            "upstream_table": "stage3_fact_impact_tambon_numerator",
            "downstream_table": "stage3_fact_level1_impact_province_year_disaster",
            **r1,
        }
    )

    r2 = _sum_shared_numeric(
        upstream=impact_tambon,
        downstream=level2_impact,
        keys=["year_be", "province_code", "district_code", "subdistrict_code", "disaster_type"],
    )
    recon_rows.append(
        {
            "check_name": "recon_subtask5_tambon_to_level2_impact",
            "upstream_table": "stage3_fact_impact_tambon_numerator",
            "downstream_table": "stage3_fact_level2_impact_tambon_year_disaster",
            **r2,
        }
    )

    # Subtask 6 redistributed value should reconcile to Level 2 relief totals by tambon/year/sector.
    rr_col_candidates = [
        c
        for c in relief_redistributed.columns
        if "redistributed" in c.lower() and pd.api.types.is_numeric_dtype(relief_redistributed[c])
    ]
    lvl2_relief_group_keys = ["year_be", "province_code", "district_code", "subdistrict_code", "relief_sector"]
    lvl2_relief_numeric = [
        c
        for c in level2_relief.columns
        if pd.api.types.is_numeric_dtype(level2_relief[c])
        and c not in lvl2_relief_group_keys
        and "year" not in c.lower()
    ]
    rr_col = rr_col_candidates[0] if rr_col_candidates else None
    lvl2_col = lvl2_relief_numeric[0] if lvl2_relief_numeric else None

    if rr_col and lvl2_col:
        rr_g = (
            relief_redistributed.groupby(
                lvl2_relief_group_keys,
                dropna=False,
            )[rr_col]
            .sum()
            .reset_index(name="upstream_value")
        )
        l2_g = (
            level2_relief.groupby(
                lvl2_relief_group_keys,
                dropna=False,
            )[lvl2_col]
            .sum()
            .reset_index(name="downstream_value")
        )
        m = rr_g.merge(
            l2_g,
            on=lvl2_relief_group_keys,
            how="outer",
        ).fillna(0)
        diff = (m["upstream_value"] - m["downstream_value"]).abs()
        recon_rows.append(
            {
                "check_name": "recon_subtask6_redistributed_to_level2_relief",
                "upstream_table": "stage3_fact_relief_tambon_redistributed_by_sector",
                "downstream_table": "stage3_fact_level2_relief_tambon_year_sector",
                "checked_columns": f"{rr_col}->{lvl2_col}",
                "max_abs_diff": float(diff.max()),
                "sum_abs_diff": float(diff.sum()),
                "row_mismatch_count": int((diff > relief_recon_tolerance).sum()),
                "pass": float(diff.max()) <= relief_recon_tolerance,
                "note": "",
            }
        )
    else:
        recon_rows.append(
            {
                "check_name": "recon_subtask6_redistributed_to_level2_relief",
                "upstream_table": "stage3_fact_relief_tambon_redistributed_by_sector",
                "downstream_table": "stage3_fact_level2_relief_tambon_year_sector",
                "checked_columns": "",
                "max_abs_diff": None,
                "sum_abs_diff": None,
                "row_mismatch_count": None,
                "pass": False,
                "note": "could_not_infer_numeric_value_columns",
            }
        )

    # Subtask 6 redistributed totals to Level 1 relief redistributed column.
    lvl1_rr_col = None
    for c in level1_relief.columns:
        if "redistributed_relief_baht_from_subtask6" == c:
            lvl1_rr_col = c
            break
    if lvl1_rr_col and rr_col:
        rr1 = (
            relief_redistributed.groupby(["year_be", "province_code", "relief_sector"], dropna=False)[rr_col]
            .sum()
            .reset_index(name="upstream_value")
        )
        l1 = (
            level1_relief.groupby(["year_be", "province_code", "relief_sector"], dropna=False)[lvl1_rr_col]
            .sum()
            .reset_index(name="downstream_value")
        )
        m = rr1.merge(l1, on=["year_be", "province_code", "relief_sector"], how="outer").fillna(0)
        diff = (m["upstream_value"] - m["downstream_value"]).abs()
        recon_rows.append(
            {
                "check_name": "recon_subtask6_redistributed_to_level1_relief_rr_column",
                "upstream_table": "stage3_fact_relief_tambon_redistributed_by_sector",
                "downstream_table": "stage3_fact_level1_relief_province_year_sector",
                "checked_columns": f"{rr_col}->{lvl1_rr_col}",
                "max_abs_diff": float(diff.max()),
                "sum_abs_diff": float(diff.sum()),
                "row_mismatch_count": int((diff > relief_recon_tolerance).sum()),
                "pass": float(diff.max()) <= relief_recon_tolerance,
                "note": "",
            }
        )

    # Level 3 key-coverage consistency signal (expected inherited blockers possible).
    key_cols = ["province_code", "district_code", "subdistrict_code"]
    has_key_cols = all(c in level3_key_coverage.columns for c in key_cols)
    if has_key_cols:
        l2_impact_keys = set(
            zip(
                level2_impact["province_code"].map(lambda x: _normalize_code(x, 2)),
                level2_impact["district_code"].map(lambda x: _normalize_code(x, 2)),
                level2_impact["subdistrict_code"].map(lambda x: _normalize_code(x, 2)),
            )
        )
        l2_relief_keys = set(
            zip(
                level2_relief["province_code"].map(lambda x: _normalize_code(x, 2)),
                level2_relief["district_code"].map(lambda x: _normalize_code(x, 2)),
                level2_relief["subdistrict_code"].map(lambda x: _normalize_code(x, 2)),
            )
        )
        l3_keys = set(
            zip(
                level3_key_coverage["province_code"].map(lambda x: _normalize_code(x, 2)),
                level3_key_coverage["district_code"].map(lambda x: _normalize_code(x, 2)),
                level3_key_coverage["subdistrict_code"].map(lambda x: _normalize_code(x, 2)),
            )
        )
        missing_from_l3_impact = [k for k in l2_impact_keys if k not in l3_keys]
        missing_from_l3_relief = [k for k in l2_relief_keys if k not in l3_keys]
        recon_rows.append(
            {
                "check_name": "coverage_level2_keys_vs_level3_key_coverage",
                "upstream_table": "stage3_fact_level2_impact_tambon_year_disaster|stage3_fact_level2_relief_tambon_year_sector",
                "downstream_table": "stage3_subtask9_level3_tambon_key_coverage",
                "checked_columns": "province_code,district_code,subdistrict_code",
                "max_abs_diff": None,
                "sum_abs_diff": None,
                "row_mismatch_count": int(len(missing_from_l3_impact) + len(missing_from_l3_relief)),
                "pass": (len(missing_from_l3_impact) == 0 and len(missing_from_l3_relief) == 0),
                "note": f"missing_impact_keys={len(missing_from_l3_impact)};missing_relief_keys={len(missing_from_l3_relief)}",
            }
        )

    # Subtask 6 internal reconciliation status from persisted artifact.
    recon_diff_col = None
    for c in subtask6_recon.columns:
        if "difference" in c.lower() and pd.api.types.is_numeric_dtype(subtask6_recon[c]):
            recon_diff_col = c
            break
    if recon_diff_col:
        abs_max = float(subtask6_recon[recon_diff_col].abs().max())
        mismatch = int((subtask6_recon[recon_diff_col].abs() > relief_recon_tolerance).sum())
        recon_rows.append(
            {
                "check_name": "recon_subtask6_internal_allocated_groups",
                "upstream_table": "stage3_subtask6_relief_redistribution_reconciliation",
                "downstream_table": "stage3_subtask6_relief_redistribution_reconciliation",
                "checked_columns": recon_diff_col,
                "max_abs_diff": abs_max,
                "sum_abs_diff": float(subtask6_recon[recon_diff_col].abs().sum()),
                "row_mismatch_count": mismatch,
                "pass": abs_max <= relief_recon_tolerance,
                "note": "",
            }
        )

    recon_df = pd.DataFrame(recon_rows)
    recon_df.to_csv(reports / "stage3_subtask10_final_integrity_reconciliation_checks.csv", index=False, encoding="utf-8-sig")

    # Inherited blocker inventory from prior validation artifacts.
    blockers: List[Dict[str, Any]] = []

    def _load_json(path: Path) -> Dict[str, Any]:
        if not path.exists():
            return {}
        with path.open("r", encoding="utf-8") as f:
            obj = json.load(f)
        return obj if isinstance(obj, dict) else {}

    v7 = _load_json(reports / "stage3_subtask7_level1_provincial_validation.json")
    v8 = _load_json(reports / "stage3_subtask8_level2_tambon_validation.json")
    v9 = _load_json(reports / "stage3_subtask9_level3_spatial_validation.json")
    v6 = _load_json(reports / "stage3_subtask6_relief_redistribution_validation.json")

    def _find_key_recursive(obj: Any, target_key: str) -> Optional[Any]:
        if isinstance(obj, dict):
            if target_key in obj:
                return obj[target_key]
            for v in obj.values():
                found = _find_key_recursive(v, target_key)
                if found is not None:
                    return found
        elif isinstance(obj, list):
            for item in obj:
                found = _find_key_recursive(item, target_key)
                if found is not None:
                    return found
        return None

    def _pull(d: Dict[str, Any], keys: Iterable[str]) -> Optional[Any]:
        for k in keys:
            found = _find_key_recursive(d, k)
            if found is not None:
                return found
        return None

    blockers.append(
        {
            "blocker_code": "SUBTASK6_UNALLOCATED_GROUPS",
            "source_artifact": "stage3_subtask6_relief_redistribution_validation.json",
            "metric": "unallocated_province_year_sector_rows",
            "value": _pull(v6, ["unallocated_province_year_sector_rows", "unallocated_rows", "unallocated_groups"]),
            "classification": "inherited_limitation",
            "description": "Redistribution groups with no eligible tambon basis remain unallocated by design and are not silently imputed.",
        }
    )
    blockers.append(
        {
            "blocker_code": "SUBTASK8_GEOMETRY_JOIN_INCOMPLETENESS_IMPACT",
            "source_artifact": "stage3_subtask8_level2_tambon_validation.json",
            "metric": "impact_rows_missing_matched_geometry",
            "value": _pull(v8, ["impact_rows_missing_matched_geometry"]),
            "classification": "inherited_limitation",
            "description": "Level 2 impact rows missing matched geometry keys persist from Subtask 2/8 crosswalk constraints.",
        }
    )
    blockers.append(
        {
            "blocker_code": "SUBTASK8_GEOMETRY_JOIN_INCOMPLETENESS_RELIEF",
            "source_artifact": "stage3_subtask8_level2_tambon_validation.json",
            "metric": "relief_rows_missing_matched_geometry",
            "value": _pull(v8, ["relief_rows_missing_matched_geometry"]),
            "classification": "inherited_limitation",
            "description": "Level 2 relief rows missing matched geometry keys persist from Subtask 2/8 crosswalk constraints.",
        }
    )
    blockers.append(
        {
            "blocker_code": "SUBTASK2_BANGKOK_TAMBON_MISMATCH",
            "source_artifact": "stage3_subtask8_level2_tambon_validation.json|stage3_subtask9_level3_spatial_validation.json",
            "metric": "bangkok_crosswalk_nonmatched_rows",
            "value": _pull(v8, ["bangkok_crosswalk_nonmatched_rows", "bangkok_subtask2_mismatch_rows", "bangkok_nonmatched_rows"])
            or _pull(v9, ["bangkok_subtask2_mismatch_rows", "bangkok_crosswalk_nonmatched_rows"]),
            "classification": "inherited_limitation",
            "description": "Bangkok tambon mismatch evidence remains unresolved and is explicitly preserved under Bangkok policy framing.",
        }
    )

    blockers_path = reports / "stage3_subtask10_final_integrity_inherited_blockers.json"
    blockers_path.write_text(json.dumps(blockers, ensure_ascii=False, indent=2), encoding="utf-8")

    schema_summary = {
        "dim_location_master_columns": dim.columns.tolist(),
        "stage3_dim_denominator_columns": denominator.columns.tolist(),
        "stage3_fact_impact_tambon_numerator_columns": impact_tambon.columns.tolist(),
        "stage3_fact_relief_tambon_redistributed_columns": relief_redistributed.columns.tolist(),
        "stage3_fact_level1_impact_columns": level1_impact.columns.tolist(),
        "stage3_fact_level1_relief_columns": level1_relief.columns.tolist(),
        "stage3_fact_level2_impact_columns": level2_impact.columns.tolist(),
        "stage3_fact_level2_relief_columns": level2_relief.columns.tolist(),
        "stage3_subtask9_level3_key_coverage_columns": level3_key_coverage.columns.tolist(),
        "crosswalk_tambon_columns": crosswalk_tambon.columns.tolist(),
    }
    (reports / "stage3_subtask10_final_integrity_schema_inspection.json").write_text(
        json.dumps(schema_summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    overall = {
        "fk_checks": {
            "total": int(len(fk_df)),
            "passed": int(fk_df["pass"].fillna(False).sum()),
            "failed": int((~fk_df["pass"].fillna(False)).sum()),
        },
        "reconciliation_checks": {
            "total": int(len(recon_df)),
            "passed": int(recon_df["pass"].fillna(False).sum()),
            "failed": int((~recon_df["pass"].fillna(False)).sum()),
        },
        "artifact_readability": {
            "total": int(len(artifact_df)),
            "readable": int(artifact_df["is_readable"].fillna(False).sum()),
            "unreadable_or_missing": int((~artifact_df["is_readable"].fillna(False)).sum()),
        },
        "inherited_blockers": blockers,
    }
    (reports / "stage3_subtask10_final_integrity_validation.json").write_text(
        json.dumps(overall, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    status_line = "PASS_WITH_INHERITED_LIMITATIONS"
    if overall["artifact_readability"]["unreadable_or_missing"] > 0:
        status_line = "FAIL_ARTIFACT_INTEGRITY"
    elif overall["fk_checks"]["failed"] > 0 or overall["reconciliation_checks"]["failed"] > 0:
        status_line = "PARTIAL_PASS_WITH_EXPLICIT_FAILURES"

    report_md = reports / "CRI_Phase1_Stage3_Subtask10_Final_Integrity_Report.md"
    report_md.write_text(
        "\n".join(
            [
                "# CRI Phase 1 Stage 3 — Subtask 10 Final Integrity Report",
                "",
                "## Scope",
                "Final integrity pass over Stage 3 artifacts (Subtasks 4–9): schema/key-path inspection, foreign-key integrity, reconciliation consistency, artifact readability, and inherited blocker inventory.",
                "",
                "## Execution",
                "- Script: `script/tmp_stage3_subtask10_final_integrity_audit.py`",
                "- Environment: project virtual environment (`.\\.venv\\Scripts\\python.exe`)",
                "",
                "## Result Status",
                f"- `{status_line}`",
                f"- FK checks: {overall['fk_checks']['passed']}/{overall['fk_checks']['total']} passed",
                f"- Reconciliation checks: {overall['reconciliation_checks']['passed']}/{overall['reconciliation_checks']['total']} passed",
                f"- Artifact readability: {overall['artifact_readability']['readable']}/{overall['artifact_readability']['total']} readable",
                "",
                "## Integrity Artifacts Produced",
                "- `artifacts/reports/stage3_subtask10_final_integrity_schema_inspection.json`",
                "- `artifacts/reports/stage3_subtask10_final_integrity_fk_checks.csv`",
                "- `artifacts/reports/stage3_subtask10_final_integrity_reconciliation_checks.csv`",
                "- `artifacts/reports/stage3_subtask10_final_integrity_artifact_readability.csv`",
                "- `artifacts/reports/stage3_subtask10_final_integrity_inherited_blockers.json`",
                "- `artifacts/reports/stage3_subtask10_final_integrity_validation.json`",
                "",
                "## Inherited Blockers",
                "The final pass preserves known inherited constraints from Subtasks 2/6/8/9 without silent correction; see `stage3_subtask10_final_integrity_inherited_blockers.json`.",
            ]
        ),
        encoding="utf-8",
    )

    print(json.dumps({"status": status_line, **overall}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
