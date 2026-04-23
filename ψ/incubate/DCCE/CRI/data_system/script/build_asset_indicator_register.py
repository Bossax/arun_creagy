import json
from pathlib import Path


INPUT_FILENAME = "2026-04-22_asset_indicator_rows_flattened_qc.json"
OUTPUT_FILENAME = "asset_indicator_register.md"


def sanitize_markdown_cell(value: object) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    text = text.replace("|", "\\|")
    text = text.replace("\r\n", "<br>").replace("\n", "<br>")
    return text


def build_register_markdown(rows: list[dict]) -> str:
    lines: list[str] = []
    lines.append("# Asset Indicator Register")
    lines.append("")
    lines.append(
        "- Purpose: local synthesis register built directly from flattened/QC asset rows for downstream mismatch crosswalk."
    )
    lines.append(f"- Source artifact: `{INPUT_FILENAME}`")
    lines.append(f"- Total register entries: {len(rows)}")
    lines.append(
        "- Register policy: one register entry per flattened row; duplicates and competing labels preserved; no concept collapsing performed."
    )
    lines.append("")

    headers = [
        "register_id",
        "source_batch_file",
        "source_row_index",
        "source_id_reference",
        "candidate_asset_label",
        "sets_domain",
        "capacity_category",
        "activation_hint",
        "lock_in_risk_if_mentioned",
        "citation",
        "row_kind",
        "potential_energy_description",
        "quoted_or_close_paraphrase",
        "provenance_key",
    ]

    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|")

    for idx, row in enumerate(rows, start=1):
        register_id = f"AIR-{idx:03d}"
        source_batch_file = sanitize_markdown_cell(row.get("source_batch_file", ""))
        source_row_index = sanitize_markdown_cell(row.get("source_row_index", ""))
        provenance_key = f"{source_batch_file}#{source_row_index}"

        values = [
            register_id,
            source_batch_file,
            source_row_index,
            sanitize_markdown_cell(row.get("source_id_reference", "")),
            sanitize_markdown_cell(row.get("candidate_asset_label", "")),
            sanitize_markdown_cell(row.get("sets_domain", "")),
            sanitize_markdown_cell(row.get("capacity_category", "")),
            sanitize_markdown_cell(row.get("activation_hint", "")),
            sanitize_markdown_cell(row.get("lock_in_risk_if_mentioned", "")),
            sanitize_markdown_cell(row.get("citation", "")),
            sanitize_markdown_cell(row.get("row_kind", "")),
            sanitize_markdown_cell(row.get("potential_energy_description", "")),
            sanitize_markdown_cell(row.get("quoted_or_close_paraphrase", "")),
            sanitize_markdown_cell(provenance_key),
        ]

        lines.append("| " + " | ".join(values) + " |")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    data_system_dir = Path.cwd()
    input_path = (
        data_system_dir
        / ".."
        / "output"
        / "asset_indicator_dictionary"
        / "working"
        / INPUT_FILENAME
    ).resolve()
    output_path = (
        data_system_dir
        / ".."
        / "output"
        / "asset_indicator_dictionary"
        / "synthesis"
        / OUTPUT_FILENAME
    ).resolve()

    rows = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise ValueError("Flattened QC input is not a JSON array")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_register_markdown(rows), encoding="utf-8")

    safe_output_path = str(output_path).encode("ascii", "backslashreplace").decode("ascii")
    print(f"OUTPUT_FILE={safe_output_path}")
    print(f"TOTAL_REGISTER_ROWS={len(rows)}")


if __name__ == "__main__":
    main()

