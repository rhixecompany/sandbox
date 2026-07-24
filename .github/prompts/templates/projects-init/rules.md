# Rules

> Extracted from `projects-init.prompt.md`.

## Rules

1. **Strict sequential execution** — Phase 1 → Phase 2 → Phase 3. Each phase must complete (including verification) before the next starts.
2. **Verify before delete** — Always confirm the canonical copy exists at the target path before removing a source file.
3. **Count and report** — Log file counts before and after each phase. Report deltas in the phase summary.
4. **No destructive operations without confirmation** — For `rm` operations over 3+ files, show the list and ask before executing.
