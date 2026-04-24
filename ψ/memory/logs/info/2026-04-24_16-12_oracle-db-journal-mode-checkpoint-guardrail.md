# Oracle DB journal mode checkpoint guardrail

## Why this note exists

`wal_checkpoint` output can be misread as a malfunction when the runtime journal mode is not WAL. In `DELETE` mode, checkpoint counters are not operationally meaningful in the same way.

## Guardrail

Before diagnosing any "checkpoint malfunction", always check runtime journal mode first.

If `journal_mode != WAL`:
- treat WAL checkpoint counters as non-primary diagnostics,
- prioritize integrity and mode checks,
- avoid concluding corruption from `wal_checkpoint` tuple values alone.

## Read-only validation snippet (PowerShell + Python)

```powershell
powershell -NoProfile -Command "python -c \"import sqlite3, json; db=r'C:\\Users\\sitth\\.oracle-v2\\oracle.db'; con=sqlite3.connect(db); cur=con.cursor(); out={}; out['journal_mode']=cur.execute('PRAGMA journal_mode;').fetchone()[0]; out['integrity_check']=cur.execute('PRAGMA integrity_check;').fetchone()[0]; out['wal_checkpoint_passive']=cur.execute('PRAGMA wal_checkpoint(PASSIVE);').fetchall(); print(json.dumps(out)); con.close()\""
```

Expected interpretation:
- `integrity_check = ok` indicates database integrity passed.
- `journal_mode = delete` means WAL checkpoint metrics are mode-mismatched diagnostics.

## Secondary hygiene note

Nested repositories under `ψ/learn/Soul-Brews-Studio` can create attribution/history confusion during incident reviews. Treat this as a documentation-risk co-factor, not direct evidence of runtime checkpoint failure.
