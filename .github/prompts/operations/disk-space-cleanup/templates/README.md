# disk-space-cleanup Template

Prompt: disk-space-cleanup.prompt.md
Lines: 164
Templates: 1

## Workflow (phases/steps)

1. **Measure first** — record before/after free space:
   - `df -h /c` / `du -sh <root>` to find big roots.
2. **Dry-run** (default, deletes nothing):
   - `python scripts/cleanup_disk.py --verify --min-size 5 "C:/path/to/repo" ...`
   - Categories: `deps` (node_modules, venv, .venv, myvenv, **pycache**, dist, build, .next, .tox), `archive` (.archive, backup, *.bak,*.orig, *.rej, *~), `cache` (.cache, npm-cache), `logs` (*.log,*.tmp).
   - MSYS pitfall: pass Windows-style paths (`C:/...`) to native Python; use `MSYS_NO_PATHCONV=1`.
3. **Get approval** before destructive apply: `python scripts/cleanup_disk.py --apply --min-size 5 <roots>`.
4. **Hermes root** — conservative cats only: `--apply --cats cache,logs,archive "C:/Users/<user>/AppData/Local/hermes"` (never runtime deps; locked logs are expected).
5. **Temp folder** — delete only entries older than ~3 days + empty dirs; never rmtree wholesale.
6. **Bloated `.git`** — `git count-objects -vH`; if garbage is large, `git gc --prune=now` (safe; never filter-repo/filter-branch without approval).
7. **App uninstall** — inventory via `winget list`, present deletion list for approval, `winget uninstall --id <id> --silent` only after approval.

## Verification

- Confirm free-space delta after apply.
- Confirm no runtime deps removed from Hermes root.
- Confirm no history-rewriting git commands were used.

---

> TODO-to-author: mirror skill `devops/disk-space-cleanup` updates into this README.
