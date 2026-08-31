# Hermes Diagnostic Sweep — 2026-08-31 15:23 WCAST

## Result: ✓ PASS (12/12 + bun check green)

## Commands Run

| # | Command | Result |
|---|---|---|
| 1 | `hermes doctor` | ✓ no active advisories; all packages, configs, dirs OK |
| 2 | `hermes doctor --fix` | ✓ no fixes needed (already clean) |
| 3 | `hermes security audit` | ✓ no advisories |
| 4 | `hermes status` | ✓ clean |
| 5 | `hermes insights` | ✓ 351 skill loads, 71 distinct skills |
| 6 | `hermes logs list` | ✓ 38 log files |
| 7 | `hermes logs errors` | ⚠ warnings present (see Known Issues) |
| 8 | `hermes logs desktop` | ✓ last entry 2026-08-24 |
| 9 | `hermes logs gateway` | ✓ active (last 7m ago) |
| 10 | `hermes logs gui` | ✓ last 2026-08-25 |
| 11 | `hermes logs agent` | ✓ active (1.6MB, 7m ago) |
| 12 | `bun run check` | ✓ 0 errors (after fixes) |

## Fixes Applied (root-cause)

| Issue | Root Cause | Fix |
|---|---|---|
| Prettier flagged 27 `judge_results/*.{md,json}` files | `judge_results/` was never excluded from Prettier — these are runtime judge-skill CLI outputs | Added `judge_results/` to `.prettierignore` |
| markdownlint flagged same files | Same — `.markdownlint-cli2.jsonc` ignored `.hermes/**` but not root-level `judge_results/` | Added `judge_results/**` to markdownlint ignores |
| cspell flagged 3 unknown words | Same — `cspell.json` had no ignore for `judge_results/` | Added `judge_results/**` to `ignorePaths` |
| markdownlint flagged duplicate `## Artifacts (this turn)` | Previous 2026-08-29 superseded section reused the same heading as today's | Renamed to `## Artifacts (2026-08-29)` |
| `bun run check` exit 1 (downstream of all above) | Cascade from Prettier failure | All 4 upstream fixes resolved |

## Known Warnings (logged, non-blocking)

| Source | Message | Status |
|---|---|---|
| `plugins.memory.honcho.session` | Insufficient credits — Honcho dialectic disabled | User-owned (billing) |
| `agent.title_generator` | 429 upstream capacity | Transient, retries |
| `agent.skill_commands` | `audit-prompts`/`status`/`rollback`/`plan` collide with core commands | Auto-skipped |
| `tools.registry` | Browser/messaging check_fn returns False (cosmetic) | Tool gating |

## Modified Files

```
.prettierignore                     (+2 lines)
.markdownlint-cli2.jsonc            (+1 line)
cspell.json                         (+1 line)
SESSION_REPORT.md                   (prettier-formatted, heading rename)
```

## Artifacts

```
.hermes/plans/hermes-diagnostic-2026-08-31_152354/
  diagnostic.txt     531 lines (hermes doctor/--fix/security/status/insights)
  logs.txt           279 lines (6 log streams)
  bun-check.txt      final pass output
  report.json        machine-readable summary
  report.md          this file
```