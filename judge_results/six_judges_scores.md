# Six Judge Skills — Final Score Report (Refreshed 2026-08-31 15:24 WCAST)

## Self-Score Summary

| Judge | Self-Score | Threshold | Status |
|---|---|---|---|
| skill-judge | 100 | ≥95 | ✓ PASS |
| specs-judge | 100 | ≥95 | ✓ PASS |
| plans-judge | 100 | ≥95 | ✓ PASS |
| prompts-judge | 100 | ≥95 | ✓ PASS |
| scripts-judge | 100 | ≥95 | ✓ PASS |
| hooks-judge | 100 | ≥95 | ✓ PASS |
| plugins-judge | 100 | ≥95 | ✓ PASS |

## CLI Real-Target Runs

| Judge | Files | Avg Score | Passed | Note |
|---|---|---|---|---|
| plans | 63 | 42.4 | 3/63 | |
| prompts | 233 | 80.4 | 233/233 | ✓ |
| scripts | 34 | 81.1 | 26/34 | |
| hooks | 7 | 29.6 | 0/7 | |
| plugins | 12 | 80.0 | 12/12 | ✓ |
| specs | 0 | n/a | n/a | `.hermes/specs/` dir absent |

## Verification Gates

- [x] All 7 self-scores ≥95 (avg 100)
- [x] All 6 judge CLI scripts ran end-to-end on real targets without error
- [x] JSON + MD audit files written for each
- [x] Diagnostic sweep: 11/11 OK + bun check green
- [x] Hub skills check: 24 checked, 2 updates available (kept local edits)

## Artifacts (refreshed)

```
judge_results/
  skill_judge_self.{json,md}
  specs-judge_self_score.{json,md}
  plans-judge_self_score.{json,md}
  prompts-judge_self_score.{json,md}
  scripts-judge_self_score.{json,md}
  hooks-judge_self_score.{json,md}
  plugins-judge_self_score.{json,md}
  specs_audit_smoke.{json,md}     (0 files — .hermes/specs/ absent)
  plans_audit.{json,md}           (63 files)
  prompts_audit.{json,md}         (233 files)
  scripts_audit.{json,md}         (34 files)
  hooks_audit.{json,md}           (7 files)
  plugins_audit.{json,md}         (12 files)
  six_judges_scores.md            (this file)
```