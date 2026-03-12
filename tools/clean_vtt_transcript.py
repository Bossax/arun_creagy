"""Clean a WEBVTT transcript into readable markdown.

Usage:
  python tools/clean_vtt_transcript.py <input.vtt> <output.md>

What it does:
- Removes WEBVTT header, cue IDs, timestamps.
- Normalizes whitespace.
- Applies a small set of common ASR artifact fixes (Thai + English terms).
- Deduplicates consecutive repeated lines.
- Packs lines into short paragraphs for readability.

Notes:
- This is a *lossy* transform intended for reading/summarization, not round-tripping.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import re
from pathlib import Path


_CUE_ID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}-\d+$",
    re.IGNORECASE,
)


def _fix_common_asr_artifacts(line: str) -> str:
    # Normalize whitespace first.
    line = re.sub(r"\s+", " ", line).strip()

    # Known Thai ASR artifact: "ความเ 4 ยง" / "ความเ4ยง" -> "ความเสี่ยง"
    line = re.sub(r"ความเ\s*4\s*ยง", "ความเสี่ยง", line)
    line = line.replace("ความเ4ยง", "ความเสี่ยง")

    # Known Thai ASR artifact: "3 ารถ" / "3ารถ" -> "สามารถ"
    line = re.sub(r"\b3\s*ารถ\b", "สามารถ", line)
    line = line.replace("3ารถ", "สามารถ")

    # A few common romanizations / typos observed in the transcript.
    replacements = {
        "addpation": "adaptation",
        "addication": "adaptation",
        "advication": "adaptation",
        "applation": "application",
        "governament": "government",
        "harvate": "harvest",
        "screap": "scrape",
        "placification": "classification",
    }
    for src, dst in replacements.items():
        line = line.replace(src, dst)

    return line


def clean_vtt_lines(raw_lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    prev: str = ""

    for raw in raw_lines:
        line = raw.strip().replace("\ufeff", "")

        if not line:
            continue
        if line == "WEBVTT":
            continue
        if "-->" in line:
            continue
        if _CUE_ID_RE.match(line):
            continue
        if line.isdigit():
            continue

        line = _fix_common_asr_artifacts(line)
        if not line:
            continue

        # Drop consecutive duplicates (VTT often repeats very short fillers).
        if line == prev:
            continue

        cleaned.append(line)
        prev = line

    return cleaned


def pack_paragraphs(lines: list[str], max_chars: int = 160) -> list[str]:
    paras: list[str] = []
    buf: list[str] = []
    buflen = 0

    for line in lines:
        if not buf:
            buf = [line]
            buflen = len(line)
            continue

        if buflen + 1 + len(line) <= max_chars:
            buf.append(line)
            buflen += 1 + len(line)
        else:
            paras.append(" ".join(buf).strip())
            buf = [line]
            buflen = len(line)

    if buf:
        paras.append(" ".join(buf).strip())

    return [p for p in paras if p]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--max-paragraph-chars", type=int, default=160)
    args = parser.parse_args()

    in_path: Path = args.input
    out_path: Path = args.output

    raw = in_path.read_text(encoding="utf-8", errors="replace").splitlines()
    cleaned_lines = clean_vtt_lines(raw)
    paras = pack_paragraphs(cleaned_lines, max_chars=args.max_paragraph_chars)

    # Prefer timezone-aware UTC timestamps.
    generated_at = (
        _dt.datetime.now(_dt.UTC)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )
    header = [
        "# FGD2 Transcript (Cleaned) — DCCE / NCAIF — 2026-03-11",
        "",
        f"- Source: {in_path.as_posix()}",
        f"- Generated: {generated_at}",
        "- Cleaning: removed WEBVTT cue IDs + timestamps; normalized whitespace; fixed common ASR artifacts (e.g., ความเ 4 ยง→ความเสี่ยง, 3 ารถ→สามารถ).",
        "",
        "---",
        "",
    ]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(header + paras) + "\n", encoding="utf-8")

    print(
        f"Wrote {out_path.as_posix()} ({len(paras)} paragraphs, {len(cleaned_lines)} cue-lines)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

