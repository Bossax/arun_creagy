# Learning: /watch prerequisites — Mosquitto MQTT tools + yt-dlp JS runtime (node)

## Pattern
`/watch` failures often look like “transcription failed,” but the root cause is usually missing prerequisites.

The reliable order:
1) **MQTT client tools**: `mosquitto_pub` + `mosquitto_sub` must be installed and on PATH.
2) **yt-dlp JS runtime**: yt-dlp should have a JS runtime configured (Node is simplest) to avoid deprecated extraction paths.
3) **Captions strategy**: distinguish auto-captions vs manual subtitles (they are different).

## Evidence signals
- If preflight shows `BLOCKERS: missing mosquitto_pub/mosquitto_sub` → Gemini automation cannot run.
- If yt-dlp prints `No supported JavaScript runtime could be found` → configure `--js-runtimes node`.

## Setup (Windows + Git Bash)

### Verify Mosquitto tools
```bash
command -v mosquitto_sub
command -v mosquitto_pub
mosquitto_sub --help | sed -n '1,25p'
```

### Permanent yt-dlp config
Create:

`C:/Users/sitth/AppData/Roaming/yt-dlp/config.txt`

With:
```text
--js-runtimes node
```

## Repository helpers
- Preflight: [`tools/watch/preflight.sh`](tools/watch/preflight.sh:1) → log: [`output/watch/_preflight.log`](output/watch/_preflight.log:1)
- Captions diagnostics: [`tools/watch/cc_diag.sh`](tools/watch/cc_diag.sh:1) → logs: `output/watch/_cc_diag_*.log`

