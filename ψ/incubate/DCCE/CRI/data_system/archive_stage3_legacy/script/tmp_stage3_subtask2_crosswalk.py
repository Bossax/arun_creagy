from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass
class JoinSummary:
    total_boundary_rows: int
    matched_rows: int
    unmatched_rows: int
    ambiguous_rows: int

    @property
    def match_rate(self) -> float:
        if self.total_boundary_rows == 0:
            return 0.0
        return self.matched_rows / self.total_boundary_rows


def normalize_admin_name(value: str) -> str:
    if value is None:
        return ""
    s = str(value)
    s = s.replace("\u200b", "").replace("\xa0", " ").strip()
    s = re.sub(r"\s+", " ", s)
    # Common Thai administrative prefixes/suffixes
    prefixes = [
        "จังหวัด",
        "จ.",
        "อำเภอ",
        "อ.",
        "เขต",
        "ตำบล",
        "ต.",
        "แขวง",
    ]
    for p in prefixes:
        if s.startswith(p):
            s = s[len(p) :].strip()
    s = s.replace("ฯ", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def main() -> None:
    base = Path(__file__).resolve().parents[1]

    dim_location_master_path = base / "data/2_gold/dim_location_master.csv"
    province_shp_path = (
        base
        / "data/0_bronze/dopa/thailanda-administrative-boundary/THA_Province.shp"
    )
    tambon_shp_path = (
        base
        / "data/0_bronze/dopa/thailanda-administrative-boundary/THA_Tambon.shp"
    )

    out_dir = base / "data/1_silver/dopa"
    report_dir = base / "artifacts/reports"

    province_crosswalk_csv = out_dir / "stage3_dopa_province_boundary_code_crosswalk.csv"
    tambon_crosswalk_csv = out_dir / "stage3_dopa_tambon_boundary_code_crosswalk.csv"
    province_gpkg = out_dir / "stage3_dopa_province_geometry_enriched.gpkg"
    tambon_gpkg = out_dir / "stage3_dopa_tambon_geometry_enriched.gpkg"

    province_mismatch_csv = (
        report_dir / "stage3_subtask2_province_boundary_mismatch.csv"
    )
    tambon_mismatch_csv = report_dir / "stage3_subtask2_tambon_boundary_mismatch.csv"
    province_ambiguity_csv = report_dir / "stage3_subtask2_province_spine_ambiguity.csv"
    tambon_ambiguity_csv = report_dir / "stage3_subtask2_tambon_spine_ambiguity.csv"
    blocker_md = report_dir / "stage3_subtask2_blockers.md"
    summary_json = report_dir / "stage3_subtask2_crosswalk_summary.json"

    for p in [
        province_crosswalk_csv,
        tambon_crosswalk_csv,
        province_gpkg,
        tambon_gpkg,
        province_mismatch_csv,
        tambon_mismatch_csv,
        province_ambiguity_csv,
        tambon_ambiguity_csv,
        blocker_md,
        summary_json,
    ]:
        ensure_parent(p)

    # Canonical spine read
    spine = pd.read_csv(dim_location_master_path, dtype=str, keep_default_na=False)

    required_spine_cols = {
        "province_code",
        "province_name_th",
        "district_code",
        "district_name_th",
        "subdistrict_code",
        "subdistrict_name_th",
    }
    missing = sorted(required_spine_cols - set(spine.columns))
    if missing:
        raise RuntimeError(
            f"Missing required columns in dim_location_master.csv: {missing}"
        )

    # Build canonical province lookup
    province_spine = spine[["province_code", "province_name_th"]].copy()
    province_spine = province_spine[
        (province_spine["province_code"] != "")
        & (province_spine["province_name_th"] != "")
    ].drop_duplicates()
    province_spine["province_name_norm"] = province_spine["province_name_th"].map(
        normalize_admin_name
    )

    province_ambiguity = (
        province_spine.groupby("province_name_norm", dropna=False)["province_code"]
        .nunique()
        .reset_index(name="n_province_codes")
    )
    province_ambiguity = province_ambiguity[
        (province_ambiguity["province_name_norm"] != "")
        & (province_ambiguity["n_province_codes"] > 1)
    ]
    province_ambiguity.to_csv(province_ambiguity_csv, index=False, encoding="utf-8-sig")

    # Build canonical tambon lookup
    tambon_spine = spine[
        [
            "province_code",
            "province_name_th",
            "district_code",
            "district_name_th",
            "subdistrict_code",
            "subdistrict_name_th",
        ]
    ].copy()
    tambon_spine = tambon_spine[
        (tambon_spine["province_code"] != "")
        & (tambon_spine["district_code"] != "")
        & (tambon_spine["subdistrict_code"] != "")
        & (tambon_spine["province_name_th"] != "")
        & (tambon_spine["district_name_th"] != "")
        & (tambon_spine["subdistrict_name_th"] != "")
    ].drop_duplicates()
    tambon_spine["province_name_norm"] = tambon_spine["province_name_th"].map(
        normalize_admin_name
    )
    tambon_spine["district_name_norm"] = tambon_spine["district_name_th"].map(
        normalize_admin_name
    )
    tambon_spine["subdistrict_name_norm"] = tambon_spine["subdistrict_name_th"].map(
        normalize_admin_name
    )

    tambon_key_cols = ["province_name_norm", "district_name_norm", "subdistrict_name_norm"]
    tambon_ambiguity = (
        tambon_spine.groupby(tambon_key_cols, dropna=False)["subdistrict_code"]
        .nunique()
        .reset_index(name="n_subdistrict_codes")
    )
    tambon_ambiguity = tambon_ambiguity[
        (tambon_ambiguity["province_name_norm"] != "")
        & (tambon_ambiguity["district_name_norm"] != "")
        & (tambon_ambiguity["subdistrict_name_norm"] != "")
        & (tambon_ambiguity["n_subdistrict_codes"] > 1)
    ]
    tambon_ambiguity.to_csv(tambon_ambiguity_csv, index=False, encoding="utf-8-sig")

    # Geospatial read/write dependency check
    try:
        import geopandas as gpd
    except Exception as exc:  # pragma: no cover - environment dependent
        blocker_text = "\n".join(
            [
                "# Stage 3 Subtask 2 Blockers",
                "",
                "- Geospatial read/write dependency unavailable: geopandas import failed.",
                f"- Error: `{type(exc).__name__}: {exc}`",
                "- Cannot produce enriched geometry outputs without geospatial IO support.",
            ]
        )
        blocker_md.write_text(blocker_text, encoding="utf-8")
        summary = {
            "status": "blocked",
            "blocker": "geopandas_missing",
            "error": f"{type(exc).__name__}: {exc}",
        }
        summary_json.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return

    # Read boundaries
    province_gdf = gpd.read_file(province_shp_path)
    tambon_gdf = gpd.read_file(tambon_shp_path)

    province_required = {"P_NAME_T"}
    tambon_required = {"P_NAME_T", "A_NAME_T", "T_NAME_T"}
    missing_province_fields = sorted(province_required - set(province_gdf.columns))
    missing_tambon_fields = sorted(tambon_required - set(tambon_gdf.columns))
    if missing_province_fields or missing_tambon_fields:
        problems = {
            "missing_province_fields": missing_province_fields,
            "missing_tambon_fields": missing_tambon_fields,
        }
        blocker_md.write_text(
            "# Stage 3 Subtask 2 Blockers\n\n"
            + "Boundary shapefile fields missing for join logic.\n\n"
            + json.dumps(problems, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        summary = {
            "status": "blocked",
            "blocker": "missing_boundary_fields",
            **problems,
        }
        summary_json.write_text(
            json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return

    # Province join
    province_join = province_gdf.copy()
    province_join["province_name_norm"] = province_join["P_NAME_T"].map(normalize_admin_name)

    province_lookup = (
        province_spine[["province_code", "province_name_th", "province_name_norm"]]
        .drop_duplicates()
        .copy()
    )
    province_lookup_counts = (
        province_lookup.groupby("province_name_norm")["province_code"]
        .nunique()
        .reset_index(name="province_match_count")
    )
    province_lookup = province_lookup.merge(
        province_lookup_counts, on="province_name_norm", how="left"
    )

    province_enriched = province_join.merge(
        province_lookup,
        on="province_name_norm",
        how="left",
        suffixes=("", "_spine"),
    )
    province_enriched["match_status"] = "matched"
    province_enriched.loc[
        province_enriched["province_code"].isna(), "match_status"
    ] = "unmatched"
    province_enriched.loc[
        province_enriched["province_match_count"].fillna(0) > 1, "match_status"
    ] = "ambiguous"

    province_summary = JoinSummary(
        total_boundary_rows=len(province_enriched),
        matched_rows=int((province_enriched["match_status"] == "matched").sum()),
        unmatched_rows=int((province_enriched["match_status"] == "unmatched").sum()),
        ambiguous_rows=int((province_enriched["match_status"] == "ambiguous").sum()),
    )

    # Tambon join
    tambon_join = tambon_gdf.copy()
    tambon_join["province_name_norm"] = tambon_join["P_NAME_T"].map(normalize_admin_name)
    tambon_join["district_name_norm"] = tambon_join["A_NAME_T"].map(normalize_admin_name)
    tambon_join["subdistrict_name_norm"] = tambon_join["T_NAME_T"].map(normalize_admin_name)

    tambon_lookup = (
        tambon_spine[
            [
                "province_code",
                "province_name_th",
                "district_code",
                "district_name_th",
                "subdistrict_code",
                "subdistrict_name_th",
                "province_name_norm",
                "district_name_norm",
                "subdistrict_name_norm",
            ]
        ]
        .drop_duplicates()
        .copy()
    )
    tambon_lookup_counts = (
        tambon_lookup.groupby(tambon_key_cols)["subdistrict_code"]
        .nunique()
        .reset_index(name="tambon_match_count")
    )
    tambon_lookup = tambon_lookup.merge(
        tambon_lookup_counts, on=tambon_key_cols, how="left"
    )

    tambon_enriched = tambon_join.merge(
        tambon_lookup,
        on=tambon_key_cols,
        how="left",
        suffixes=("", "_spine"),
    )
    tambon_enriched["match_status"] = "matched"
    tambon_enriched.loc[
        tambon_enriched["subdistrict_code"].isna(), "match_status"
    ] = "unmatched"
    tambon_enriched.loc[
        tambon_enriched["tambon_match_count"].fillna(0) > 1, "match_status"
    ] = "ambiguous"

    tambon_summary = JoinSummary(
        total_boundary_rows=len(tambon_enriched),
        matched_rows=int((tambon_enriched["match_status"] == "matched").sum()),
        unmatched_rows=int((tambon_enriched["match_status"] == "unmatched").sum()),
        ambiguous_rows=int((tambon_enriched["match_status"] == "ambiguous").sum()),
    )

    # Persist crosswalk tables
    province_crosswalk_cols = [
        "P_NAME_T",
        "P_NAME_E",
        "Area_km2",
        "province_name_norm",
        "province_code",
        "province_name_th",
        "province_match_count",
        "match_status",
    ]
    province_crosswalk_cols = [c for c in province_crosswalk_cols if c in province_enriched.columns]
    province_enriched[province_crosswalk_cols].to_csv(
        province_crosswalk_csv, index=False, encoding="utf-8-sig"
    )

    tambon_crosswalk_cols = [
        "P_NAME_T",
        "P_NAME_E",
        "A_NAME_T",
        "A_NAME_E",
        "T_NAME_T",
        "T_NAME_E",
        "Area_km2",
        "province_name_norm",
        "district_name_norm",
        "subdistrict_name_norm",
        "province_code",
        "province_name_th",
        "district_code",
        "district_name_th",
        "subdistrict_code",
        "subdistrict_name_th",
        "tambon_match_count",
        "match_status",
    ]
    tambon_crosswalk_cols = [c for c in tambon_crosswalk_cols if c in tambon_enriched.columns]
    tambon_enriched[tambon_crosswalk_cols].to_csv(
        tambon_crosswalk_csv, index=False, encoding="utf-8-sig"
    )

    # Persist mismatch reports
    province_enriched[province_enriched["match_status"] != "matched"][province_crosswalk_cols].to_csv(
        province_mismatch_csv, index=False, encoding="utf-8-sig"
    )
    tambon_enriched[tambon_enriched["match_status"] != "matched"][tambon_crosswalk_cols].to_csv(
        tambon_mismatch_csv, index=False, encoding="utf-8-sig"
    )

    # Persist enriched geometry layers (GeoPackage)
    province_enriched.to_file(province_gpkg, layer="province_enriched", driver="GPKG")
    tambon_enriched.to_file(tambon_gpkg, layer="tambon_enriched", driver="GPKG")

    # Bangkok-specific blocker tracking
    bkk_code = "10"
    bkk_prov_unresolved = province_enriched[
        (province_enriched.get("province_code", "") == bkk_code)
        & (province_enriched["match_status"] != "matched")
    ]
    bkk_tambon_unresolved = tambon_enriched[
        (tambon_enriched.get("province_code", "") == bkk_code)
        & (tambon_enriched["match_status"] != "matched")
    ]

    blocker_lines = ["# Stage 3 Subtask 2 Blockers", ""]
    blocker_lines.extend(
        [
            "- Policy-level Bangkok integration for downstream Stage 3 modules remains unresolved in the parent plan and is preserved as an explicit blocker outside this geometry crosswalk step.",
            "- Subtask 2 scope only verifies boundary-to-spine join status; it does not finalize Bangkok treatment for impact/relief integration.",
            "",
        ]
    )
    if len(bkk_prov_unresolved) > 0 or len(bkk_tambon_unresolved) > 0:
        blocker_lines.extend(
            [
                "- Bangkok-specific unresolved boundary joins detected.",
                f"- Unresolved province rows (code 10): {len(bkk_prov_unresolved)}",
                f"- Unresolved tambon rows (code 10): {len(bkk_tambon_unresolved)}",
                "- These rows are retained as explicit blockers for downstream modules.",
            ]
        )
    else:
        blocker_lines.append("- No Bangkok-specific unresolved joins detected in Subtask 2 outputs.")
    blocker_md.write_text("\n".join(blocker_lines) + "\n", encoding="utf-8")

    summary = {
        "status": "ok",
        "inputs": {
            "dim_location_master": str(dim_location_master_path.relative_to(base)),
            "province_shp": str(province_shp_path.relative_to(base)),
            "tambon_shp": str(tambon_shp_path.relative_to(base)),
        },
        "observed_columns": {
            "dim_location_master": list(spine.columns),
            "province_boundary": list(province_gdf.columns),
            "tambon_boundary": list(tambon_gdf.columns),
        },
        "province_join": {
            "total": province_summary.total_boundary_rows,
            "matched": province_summary.matched_rows,
            "unmatched": province_summary.unmatched_rows,
            "ambiguous": province_summary.ambiguous_rows,
            "match_rate": round(province_summary.match_rate, 6),
        },
        "tambon_join": {
            "total": tambon_summary.total_boundary_rows,
            "matched": tambon_summary.matched_rows,
            "unmatched": tambon_summary.unmatched_rows,
            "ambiguous": tambon_summary.ambiguous_rows,
            "match_rate": round(tambon_summary.match_rate, 6),
        },
        "outputs": {
            "province_crosswalk_csv": str(province_crosswalk_csv.relative_to(base)),
            "tambon_crosswalk_csv": str(tambon_crosswalk_csv.relative_to(base)),
            "province_enriched_geometry_gpkg": str(province_gpkg.relative_to(base)),
            "tambon_enriched_geometry_gpkg": str(tambon_gpkg.relative_to(base)),
            "province_mismatch_csv": str(province_mismatch_csv.relative_to(base)),
            "tambon_mismatch_csv": str(tambon_mismatch_csv.relative_to(base)),
            "province_ambiguity_csv": str(province_ambiguity_csv.relative_to(base)),
            "tambon_ambiguity_csv": str(tambon_ambiguity_csv.relative_to(base)),
            "blocker_md": str(blocker_md.relative_to(base)),
        },
        "notes": {
            "join_policy": "Province join on normalized Thai province name; Tambon join on normalized (province,district,subdistrict) Thai names",
            "bangkok_blocker_policy": "Preserve unresolved Bangkok rows as explicit blockers; do not silently patch",
        },
    }

    summary_json.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

