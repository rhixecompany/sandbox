# Core Rules (Shared Across Fix Prompts)

These rules apply to most fix/sync workflow prompts. Each prompt may add
domain-specific rules on top.

1. **Map before touch** — Run `context-map` before edits to understand
   dependencies and impact area.
2. **No backup files** — Use git history for rollback; never create `.bak`,
   `.old`, or timestamped backup copies.
3. **Verify after each pass** — After every phase or action, verify the
   result before moving on.
4. **One platform at a time** — When syncing across platforms (Hermes,
   Copilot, Codex), focus on one at a time.
5. **Prefer explicit mappings** — Use explicit cross-reference tables over
   guesswork or heuristics.
6. **Preserve intent** — Unless the user explicitly requests a change,
   preserve existing names, triggers, and registrations.
7. **Idempotent** — The workflow should be safe to re-run without side
   effects.
8. **File-backed evidence** — Prefer file-backed evidence over inference
   or assumptions.
