## 2026-04-22 — AS-3 continuation timeout/auth recovery pattern
- **Symptom**: NotebookLM MCP flow encountered timeout/auth friction during AS-3 continuation.
- **Recovery pattern that worked**: re-authenticate, resume in continuation mode (same extraction packet scope), and re-run the pending batch without changing extraction schema.
- **Verification signal**: downstream pipeline closed normally (flatten/QC 57 rows → register 57 entries → mismatch crosswalk 22 grouped entries), indicating recovery did not corrupt packet lineage.
