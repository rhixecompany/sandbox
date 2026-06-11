# Bulk Install / Audit Session Context

Use this reference when asked to "list everything, filter top 30 skills, install them, security scan, audit, then debug."

## What actually happened

- `hermes skills browse` returned paginated official skills only; the full registry is too large for one pass.
- `hermes skills list` confirmed a large installed base: 271 enabled skills.
- Broad `hermes skills search` queries for automation, DevOps, productivity, testing, QA, security, media, and workflows returned empty or narrow results.
- `hermes skills install --help` showed no dedicated pre-install security-scan option; `--force` only bypasses blocked verdicts.
- `systematic-debugging` is not exposed as a top-level `hermes` subcommand in this environment.
- Hub-index files exist but are inconsistent: some sources are empty, others are populated.

## Lessons

1. Do not treat bulk skill discovery/install as a single linear command chain.
2. Discovery must be multi-source: installed inventory, official optional skills, Hermes index cache, and workspace-known equivalents.
3. Install only after manual inspect; avoid blind batch installs.
4. Security review is per-skill, not a single black-box gate.
5. Audit commands have limited scope; document coverage before declaring success.

## Preferred workflow

- Enumerate installed skills.
- Narrow candidates with category-specific searches and source-specific filters.
- Inspect each candidate.
- Install in small batches with confirmation.
- Re-run audit on hub-installed skills only; do not assume local/builtin coverage.

## Windows/local path notes

- Skill maintenance scripts must normalize backslashes from `os.walk` before matching or reporting.
