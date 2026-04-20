# Mandate: Safety and Data Security (Golden Rules)

These rules are non-negotiable and must be followed in every session to protect the integrity of the project and its history.

## 1. History Preservation
- **No Force Push**: Never use `git push --force`. This violates the "Nothing is Deleted" principle.
- **No Destructive Commands**: Never use `rm -rf` on project-critical directories without a manual backup.
- **Maintain Logs**: Every structural change must be logged in `ψ/memory/logs/`.

## 2. Credential Protection
- **No Secrets**: Never commit or log secrets, API keys, OAuth tokens, private keys, or passwords.
- **File Exclusions**: Rigorously protect `.env` files and credentials stored in `~/.claude/` or `~/.gemini/`.
- **Sanitization**: Ensure no sensitive data is leaked in retrospectives, announcements, or public outputs.

## 3. Human Authorization
- **No Force Merge**: Never merge a Pull Request without explicit human approval.
- **Confirm Destructive Actions**: Always ask for confirmation before performing operations that could lead to significant data loss.
