---
name: disk-space-cleanup
description: "Free disk space: delete venvs, node_modules, caches, logs."
---

# Disk Space Cleanup (full-sweep)

## Trigger
User wants more disk space; wants to delete stale/unused venv, .venv, myvenv, node_modules, .archive, __pycache__, python/node caches in repos/subrepos/hermes root; delete backup files/folders; clean temp/tmp/logs; verify disk space; or uninstall unused apps.

## Canonical script
`~/Desktop/SandBox/scripts/cleanup_disk.py` — Python, dry-run-first, categories, dedup, safe hermes-root filtering.

## Workflow

1. **Measure first** — always record before/after free space:
   ```bash
   df -h /c   # or target drive
   du -sh <root>  # find big roots first
   ```

2. **Run the script dry-run** (default — nothing deleted):
   ```bash
   python scripts/cleanup_disk.py --verify --min-size 5 \
     "C:/path/to/repo" "C:/path/to/subrepos" ...
   ```
   - Categories: `deps` (node_modules, venv, .venv, myvenv, __pycache__, dist, build, .next, .tox), `archive` (.archive, backup, *.bak, *.orig, *.rej, *~), `cache` (.cache, npm-cache), `logs` (*.log, *.tmp).
   - `--cats deps,archive,cache,logs` restricts scope.
   - `--include-os-caches` adds pip/npm/bun/Temp OS-level caches.
   - MSYS pitfall on Windows: pass **Windows-style** paths (`C:/...`) to native Python, not MSYS `/c/...`, and use `MSYS_NO_PATHCONV=1`.

3. **Get approval** for destructive apply (SOUL rule: destructive ops need approval). Then:
   ```bash
   python scripts/cleanup_disk.py --apply --min-size 5 <roots>
   ```

4. **Hermes root — never delete runtime deps.** Use conservative cats only:
   ```bash
   python scripts/cleanup_disk.py --apply --cats cache,logs,archive "C:/Users/<user>/AppData/Local/hermes"
   ```
   Active log files (e.g. `mcp-stderr.log`) may be locked → script logs the error and continues; that's expected.

5. **Temp folder — don't rmtree wholesale** (files in use). Delete only entries older than ~3 days + empty dirs via a small Python one-liner (see pitfalls).

6. **Bloated `.git`** — check `git count-objects -vH`; if `size-garbage` or giant unreachable packs, run `git gc --prune=now` (safe, non-history-rewriting, can reclaim GBs). Never run `filter-repo`/`filter-branch` without explicit approval — that rewrites history.

7. **App uninstall** — inventory first, present deletion list for approval:
   ```bash
   winget list | sort  # inventory
   winget uninstall --id <id> --silent  # only after approval
   ```
   Never uninstall without an approved list.

8. **Verify** — `df -h /c` after; report before → after deltas and any locked/error items.

## Pitfalls

- **argparse abbreviation**: `--roots` partially matches `--roots-file`. Use `allow_abbrev=False` in the script.
- **Double-counting**: scanning a parent root AND a subroot duplicates entries — dedupe by resolved path.
- **Windows native Python** can't resolve MSYS `/c/...` paths; convert to `C:/...`.
- **Temp rmtree** fails on in-use files; use age-based cleanup (`mtime < now-3d`).
- **Hermes root** contains runtime node_modules/venv needed by the agent — never sweep deps there.
- **`du -sh` on huge roots** (e.g. hermes root with caches) can exceed terminal timeouts — run bounded `du` per known subdir or background it.

## Verification

- `df -h` shows free space increased by the expected amount.
- `scripts/cleanup_disk.py --verify` (no --apply) shows 0 remaining targets for the categories swept.
- Audit log at `results/cleanup_disk.log` lists every deletion.

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Disk Space Cleanup (full-sweep) operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## When to Use


- When you need to perform Disk Space Cleanup (full-sweep) operations or tasks
- When managing Disk Space Cleanup (full-sweep) infrastructure or configurations
- When automating or debugging Disk Space Cleanup (full-sweep) workflows
- **Triggers**: "disk space cleanup (full-sweep)" required for a project

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
