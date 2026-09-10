# repair-official — Restoring Missing Official Skills

## When to Run
After `hermes skills audit` shows many "path missing" warnings on official skills.

## Command
```
hermes skills repair-official --restore --yes all
```

## What It Does
- Rescans the official skill manifest
- Recreates SKILL.md for any official skill missing from disk
- Backfills provenance metadata (keeps origin tracking)
- Backs up old versions to `.restore-backups/official-optional-<timestamp>/`

## Typical Results
- ~97 official optional skills restored
- ~18 provenances backfilled
- Existing user-modified skills are preserved
- Backup dirs are created under `~/AppData/Local/hermes/skills/.restore-backups/`

## Effects on the Pipeline

### Positive
- Eliminates "path missing" warnings for official skills
- Prevents dozens of spurious BLOCKED/DANGEROUS entries
- Enables the judge to score skills it couldn't find before

### Negative (be aware)
- **Count inflation:** The judge (`batch_skill_judge.py`) walks directories recursively including `.restore-backups/`. After repair-official, the judge sees each skill twice (live + backup copy), inflating the judged count. The `hermes skills list` command filters correctly (~221 local skills), but the judge may report 360-370.
- **fix_fail_skills.py target ambiguity:** Post-repair, some FAIL skills may be resolved to their backup path instead of the live path. The live SKILL.md stays frozen while the backup gets fixed. Check `skill_dir` before running fix scripts.

## Recommendation
Run repair-official before the full pipeline, then ignore the count inflation in the judge output — focus on the ratio instead (PASS/WARN/FAIL %).