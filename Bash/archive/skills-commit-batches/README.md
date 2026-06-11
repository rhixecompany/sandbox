# Skills Commit Batches — Archive

These files are **one-shot migration artifacts** from the skills migration project (May 2026). Each batch corresponds to a set of skills with normalized frontmatter that were committed sequentially.

## Content

- `skills-commit-batch-{1-26}.sh` — Bash versions (26 batches)
- `skills-commit-batch-{1-25}.ps1` — PowerShell versions (25 batches)

## Status

✅ **Archived** — No longer needed for normal operation. The consolidated implementation is in `../../src/git-commit-batches.ts` which reads from `../BATCHES.json` for batch definitions.

## Restoration

To re-enable a specific batch from this archive:

```bash
cp bash-commit-batch-N.sh ../../scripts/git-commit-batch-N.sh
```
