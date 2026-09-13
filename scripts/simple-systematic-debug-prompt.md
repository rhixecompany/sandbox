# Systematic-Debug Prompt: Workspace bun run check

## Task
Debug and fix ALL runtime errors, warnings, and issues when running `bun run check` in the SandBox workspace.

## Procedure
1. Run `bun run check` and capture ALL output (stdout + stderr)
2. Categorize each error/warning by type (parse, type, lint, config, missing-dep, etc.)
3. For each category, apply the `systematic-debugging` 4-phase protocol:
   - Phase A: Understand the failure class
   - Phase B: Root-cause investigation
   - Phase C: Minimal fix
   - Phase D: Verify fix (re-run check)
4. Iterate until `bun run check` exits 0 with zero errors/warnings
5. Report final summary: errors-fixed count, remaining issues (should be 0)

## Success Criterion
- `bun run check` exits with code 0
- Zero error/warning output (except documented pre-existing issues)
- All fixes verified via real tool execution