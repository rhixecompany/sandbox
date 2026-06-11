# Repo audit notes

Use this when auditing or regenerating documentation in a multi-repo workspace.

## Durable checks

- Verify claims against the live filesystem, not only against existing indexes or summaries.
- Treat master indexes as stale until the listed files are confirmed present.
- Record both the claimed artifact set and the actual artifact set.
- Call out missing files explicitly; do not assume they will be recreated later.
- When a workspace has many repos, summarize per-repo instructions separately before writing a cross-repo synthesis.
- Keep cross-reference docs honest: note archival, stale, or orphaned documents instead of smoothing them over.

## Common drift patterns

- A master index can overstate coverage after files are deleted or consolidated.
- A “quick start” doc can still point at a superseded report set.
- Per-repo AGENTS files often contain the most current setup and validation commands, even when higher-level docs are stale.
- Ignore-file audits are useful as a hygiene snapshot, but they need to be labeled as point-in-time data.

## Output pattern

Prefer three layers:

1. inventory snapshot
2. per-repo instruction summary
3. cross-reference / drift report

This keeps the workspace docs honest and prevents stale indexes from being mistaken for source of truth.
