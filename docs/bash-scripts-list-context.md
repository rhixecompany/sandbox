# Bash Script Inventory

## Summary

- Total script files scanned: 339
- Active scripts: 177
- Archived/migrated scripts: 55

## Triage

| Bucket | Count |
| --- | --- |
| dead|archive | 109 |
| orchestrator|keep | 6 |
| utility | 117 |

## Recommendations

- Keep orchestrators (`Bash/upgrade.*`, `Bash/orchestrator-unified.*`) as-is.
- Do not touch scripts under `Bash/migrations/**` or `Bash/archive/**` during this pass.
- Do not delete or overwrite source scripts without explicit confirmation.
- Update documentation only; leave source files untouched for audit unless user authorizes edits.
