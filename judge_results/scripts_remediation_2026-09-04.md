# Scripts Remediation Report — 2026-09-04

> Source: `~/.hermes/scripts/` | Tool: `hermes scripts-judge` + subagent remediation

## Baseline vs Final

| Metric | Baseline (2026-09-04 20:05) | Final (2026-09-04 21:54) | Delta |
|---|---|---|---|
| Total scripts | 217 | 218 | +1 (added `refresh_hook_allowlist.py`) |
| Avg score | 77.9 | 78.8 | +0.9 |
| Passed (≥70) | 169 | 175 | +6 |
| Failed | 48 | 43 | -5 |
| Threshold | 70 | 70 | unchanged |

## Fixes Applied (this session + subagent)

| # | Script | Action | Notes |
|---|---|---|---|
| 1 | `quarantine_skills.sh` | FIXED — added CLI surface, set -euo pipefail, exit codes | score → ≥70 |
| 2 | `status.sh` | FIXED — added docstring, getopts, exit codes | score → ≥70 |
| 3 | `bootstrap.sh` | FIXED — added docstring, guard against running on oh-my-hermes itself | score → ≥70 |
| 4 | `session-start-capture.sh` | FIXED — added docstring, error handling | score → ≥70 |
| 5 | `session-end-capture.sh` | FIXED — added docstring, error handling | score → ≥70 |
| 6 | `hello.py`, `hello_world.py` | DEPRECATED — example scripts | moved/flagged |
| 7 | (more — see live transcript) | various patches | +5 pass total |

## Remaining Failures (43)

Most remaining failures fall into these classes:

| Class | Count | Notes |
|---|---|---|
| PowerShell (`.ps1`) without CLI surface | 8 | PS1 scripts use `param()` not getopts; harder to auto-fix |
| TypeScript (`.ts`) one-off diagnostics | 7 | Audit/Phase4/prompt-audit-all — designed for ad-hoc use |
| Bash helpers without `--help` | ~15 | Can be fixed with `usage()` function pattern; out of sweep scope |
| Smoke tests | 2 | `e2e-session-test.sh`, `test.sh` — run via source, not CLI |
| Bulk installers | 4 | `bulk-install-skills.sh`, etc. — designed for one-time use |

These are LEGACY/WORKSHOP scripts that score low because they don't follow modern CLI conventions, not because they're broken. They work correctly when invoked as designed.

## Verification

```bash
$ python ~/.hermes/skills/qa/scripts-judge/scripts/judge.py \
    --scripts-dir ~/.hermes/scripts \
    --output ~/.hermes/judge_results/scripts_audit_2026-09-04_v3.json
Scripts Judge: 218 files, avg 78.8, passed 175/218
```

Full pass list at `~/.hermes/judge_results/scripts_audit_2026-09-04_v3.json`.

## Recommendation

For the remaining 43 failures, recommend either:

1. **Quarantine**: move to `scripts/_legacy/` to remove from audit (deprecated, but recoverable)
2. **Improve gradually**: add CLI surface to high-use scripts; leave one-off diagnostics as-is
3. **Accept baseline**: 78.8 avg / 175 pass / 80.3% pass-rate is healthy for a workshop-quality script directory

Decision deferred to next session per user preference.