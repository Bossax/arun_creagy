# Lesson: System File Handling in Node.js Scripts

**Context**:
During a `/recap` execution, the script crashed when iterating through the `retrospectives` directory because it encountered `desktop.ini`, a Windows system file, and tried to treat it as a directory.

**Lesson**:
When using `fs.readdirSync` to iterate over directories that are expected to contain subdirectories (like the retrospective date structure), **always** strictly filter the results. Do not just rely on `!d.startsWith('.')`. Explicitly filter known OS artifacts or use `fs.statSync(path).isDirectory()` to confirm the type before recursion.

**Pattern**:
```typescript
const items = readdirSync(path)
  .filter(f => !f.startsWith(".") && f !== "desktop.ini" && f !== "Thumbs.db");
// OR better:
const dirs = readdirSync(path).filter(f => statSync(join(path, f)).isDirectory());
```

**Application**:
Applied this fix to `recap-rich.ts` to prevent `ENOTDIR` errors on Windows environments. This ensures the agent's self-reflection tools are robust against environmental noise.
