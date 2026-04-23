import json
from pathlib import Path


INPUT_FILES = [
    "2026-04-22_batch_AS1_SETS_lockin_raw.md",
    "2026-04-22_batch_AS2a_IPCC_raw.md",
    "2026-04-22_batch_AS2b_Zeng_Feldmeyer_raw.md",
    "2026-04-22_batch_AS3_socioeconomic_raw.md",
]

REQUIRED_KEYS = [
    "row_kind",
    "source_id_reference",
    "quoted_or_close_paraphrase",
    "candidate_asset_label",
    "sets_domain",
    "capacity_category",
    "potential_energy_description",
    "activation_hint",
    "lock_in_risk_if_mentioned",
    "citation",
]


def extract_json_array(md_text: str) -> list:
    start = md_text.find("[")
    if start < 0:
        raise ValueError("No JSON array start '[' found")

    decoder = json.JSONDecoder()
    payload, _ = decoder.raw_decode(md_text[start:])
    if not isinstance(payload, list):
        raise ValueError("Raw payload is not a JSON array")
    return payload


def main() -> None:
    data_system_dir = Path.cwd()
    response_dir = data_system_dir / ".." / "output" / "asset_indicator_dictionary" / "responses"
    output_dir = data_system_dir / ".." / "output" / "asset_indicator_dictionary" / "working"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "2026-04-22_asset_indicator_rows_flattened_qc.json"

    rows = []
    qc = {
        "missing_required_keys_filled": {k: 0 for k in REQUIRED_KEYS},
        "non_object_rows_skipped": 0,
        "empty_string_fields": 0,
        "null_fields": 0,
        "unexpected_row_kind_count": 0,
        "source_file_row_counts": {},
    }

    for filename in INPUT_FILES:
        path = (response_dir / filename).resolve()
        text = path.read_text(encoding="utf-8")
        payload = extract_json_array(text)
        qc["source_file_row_counts"][filename] = len(payload)

        for i, row in enumerate(payload, start=1):
            if not isinstance(row, dict):
                qc["non_object_rows_skipped"] += 1
                continue

            normalized = dict(row)

            for key in REQUIRED_KEYS:
                if key not in normalized:
                    normalized[key] = "not explicit"
                    qc["missing_required_keys_filled"][key] += 1

            for key, value in normalized.items():
                if value is None:
                    qc["null_fields"] += 1
                elif isinstance(value, str) and value.strip() == "":
                    qc["empty_string_fields"] += 1

            if normalized.get("row_kind") != "stock_indicator_candidate":
                qc["unexpected_row_kind_count"] += 1

            normalized["source_batch_file"] = filename
            normalized["source_row_index"] = i
            rows.append(normalized)

    output_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    safe_output_path = str(output_path.resolve()).encode("ascii", "backslashreplace").decode("ascii")
    print(f"OUTPUT_FILE={safe_output_path}")
    print(f"TOTAL_ROWS={len(rows)}")
    print(f"QC_SOURCE_COUNTS={json.dumps(qc['source_file_row_counts'], ensure_ascii=False)}")
    print(f"QC_MISSING_REQUIRED_KEYS_FILLED={json.dumps(qc['missing_required_keys_filled'], ensure_ascii=False)}")
    print(f"QC_NON_OBJECT_ROWS_SKIPPED={qc['non_object_rows_skipped']}")
    print(f"QC_EMPTY_STRING_FIELDS={qc['empty_string_fields']}")
    print(f"QC_NULL_FIELDS={qc['null_fields']}")
    print(f"QC_UNEXPECTED_ROW_KIND_COUNT={qc['unexpected_row_kind_count']}")


if __name__ == "__main__":
    main()
