---
name: repo-management
description: "Post-research repository maintenance: branch protection, migration (e.g., Bun), CI workflow setup, cross-referencing, and repo health checks. Uses verified preflight checks before applying changes."
author: Alexa
license: MIT
version: 1.1.0
tags: [git, github, ci, migration, bun, branch-protection, workflow]
category: devops
---

# Repo Management

## Overview
This skill defines the class‑level procedures for managing a repository after research and other development phases. It covers:
- Branch normalization (development/production)
- Migration from npm/pnpm to Bun
- CI workflow configuration (GitHub Actions)
- Disk usage analysis and cleanup
- Cross‑repository reference updates
- Verification checks before moving to further phases

## Multi-Repo Bootstrap

- When a workspace contains many repos or subrepos, initialize each repo, attach remotes, and normalize the branch model here rather than keeping a separate one-off skill.
- The absorbed multi-repo path covers missing `.git` roots, initial commits, remote setup, and production/development branch creation.

## Prerequisites
- Authenticated GitHub CLI (`gh`) or the `github-repo-management` skill loaded.
- MCP servers for `mcp-github` and `mcp-filesystem`.
- `bun` ≥ 1.3 installed and on PATH.
- Repository root path known (usually `$HOME/Desktop/SandBox`).

## Phase 0: Preconditions
1. Verify GitHub auth: `gh auth status`.
2. Check `bun --version` > 1.3.
3. Check Git worktree: `git status --porcelain`. Modified files are acceptable (not a hard blocker) but resolve merge conflicts before proceeding.
4. Read branch state from the live API: `gh api repos/<owner>/<repo>/branches --paginate` and inspect `.protected`, `.protection.enabled`, and `.protection.required_status_checks.contexts`. Do not rely on `gh protection list` as the primary source; it may fail while the API response is available.
5. Redact token metadata in tool output. Use `--jq` on `gh api` to show branch names and protection state only; avoid printing token scopes or partial secrets in session logs.

## Phase 0.5: Bun Target Discovery
- Scan all project roots for npm artifacts before migrating: `find projects -name 'package-lock.json' -not -path '*/node_modules/*' | sort`.
- Confirm CI script mappings with live package data: `jq '.scripts' <project>/package.json`, then compare every `bun run <script>` in `.github/workflows/*.yml` against actual keys. Add missing scripts explicitly before committing CI changes.

## Phase 1: Branch Normalization
- Ensure `development` and `production` branches exist.
- Delete stale branches not matching the pattern.
- Apply branch‑protection rules via the `github-repo-management` skill (required status checks, pull‑request review approvals, etc.).
- **Subdirectory vs. standalone repo:** when the task names a subdir (e.g. `docs/`, `projects/*`), verify it is actually its own repo before running branch/default ops. Run `git rev-parse --show-toplevel` and `gh repo view --json name -q .name` from inside the dir. In a monorepo these subdirs are NOT separate repos — branch/default changes apply to the whole parent repo and `gh` targets the parent. Misreading this leads to wrong `gh` targets and unintended whole-repo mutations.
- **Default-branch flip ordering (GitHub refuses to delete the default branch):** before deleting `master`, 1) `gh repo edit <owner>/<repo> --default-branch production`, 2) `git push origin --delete master`, 3) `git fetch -p`, 4) `git remote set-head origin production` to refresh a stale `origin/HEAD`. Flip default FIRST, then delete remote; deleting a default branch fails with a refusal. See `references/branch-normalization-gotchas.md`.
- **Read the CURRENT default branch with `defaultBranchRef`, not `defaultBranch`:** `gh repo view <owner>/<repo> --json defaultBranchRef --jq '.defaultBranchRef.name'` (returns e.g. `master`/`production`). Using `--json defaultBranch` fails with `Unknown JSON field: "defaultBranch"` — `defaultBranch` is not a valid field on Repo; the field is `defaultBranchRef`. Re-run this read AFTER the flip to verify the new default landed.
- **Never `git add -A` on a dirty monorepo tree:** if the working tree has large unrelated uncommitted changes, stage ONLY the intended files (`git add <path1> <path2>`), never `git add -A`/`git add .`. Write a `PRESTATE_*.md` snapshot before mutating so the pre-change branch/default state is recorded.
- Before claiming branch state, reconcile API response fields: `protected`, `protection.enabled`, and `protection.required_status_checks.contexts`. Do not claim patched state from one field when another field still shows old state.

## Phase 2: Bun Migration
- Scan workspace for `package-lock.json` files (`find . -name 'package-lock.json' -not -path '*/node_modules/*'`) to identify projects still using npm.
- For each discovered project:
  - Remove `package-lock.json` and `node_modules/`.
  - Run `bun install --frozen-lockfile` to generate `bun.lock`.
- Replace any `npm`/`pnpm` scripts embedded in `package.json` scripts with `bun` equivalents.
- **Verify scripts referenced by CI commands exist:** before committing CI workflow, run `jq '.scripts' package.json` and confirm every `bun run <script>` in the CI workflow resolves to an actual script (e.g., `typecheck`, `lint:strict`, `test`, `format:check`).
- Run `bun run typecheck`, `bun run lint`, and `bun run test` to confirm the build passes.

## Phase3: CI Workflow Setup
- **Do NOT clobber an existing CI:** before creating a workflow, inspect `ls .github/workflows/` (and `git status --porcelain` for untracked ones). If a real, project-specific CI already exists, KEEP it — writing a generic starter over it is a regression. Extend/adjust the existing file instead of replacing it.
- Add `.github/workflows/ci.yml`. Attempt to source a `templates/ci-workflow.yml` starter; if none exists, create a minimal workflow from scratch (checkout → bun install → typecheck → lint → test → format).
- Verify every `bun run <script>` in the workflow maps to a real script in the target project's `package.json`. The `test` script is frequently missing even when `vitest` is installed — add it explicitly if absent.
- Enable branch protection for CI (requires the `development` branch to pass CI checks).
- Dry-run validation: run each CI step locally in order to confirm they pass before committing.

## Phase 4: Disk Usage & Cleanup
- Run the `scripts/disk-usage.sh` script to list the top 5 largest directories, excluding typical noise directories.

## Phase 5: Cross-Reference Update
- Update `projects/RESEARCH_INDEX.md` and each `RESEARCH_REPORT.md`'s "Related Projects" section to reflect any new or changed references.
- **Verify symmetry explicitly:** for each report, grep its "Related Projects" section for referenced project names. Then grep each referenced project's report for the original project name. If A references B but B does not reference A, patch B to reciprocate.
  ```bash
  # Per-report symmetry check
  for f in projects/*/RESEARCH_REPORT.md; do
    proj=$(echo "$f" | cut -d/ -f2)
    for ref in $(grep -oP '(?<=\*\*)\w+(?=\*\*)' <(sed -n '/^## Related/,/^## /p' "$f")); do
      grep -q "$proj" "projects/$ref/RESEARCH_REPORT.md" 2>/dev/null || echo "MISSING: $proj not referenced by $ref"
    done
  done
  ```

## Verification Checklist
- [ ] Branches normalized and protected.
- [ ] Bun migration successful (`bun run test` passes).
- [ ] CI workflow present and passes on a test commit.
- [ ] Disk usage report generated.
- [ ] Cross‑references symmetric across all reports.

## References
- `references/repo-prompt.md` – source prompt that defines the broader repo workflow.
- `references/workspace-ci-path-drift.md` – post-restructure CI/doc path update checklist and verifier for `Bash/` → `projects/Bash/` and similar moves.
- `references/branch-normalization-gotchas.md` – exact command sequence + failure modes for default-branch flip, remote/local `master` deletion, stale `origin/HEAD`, dirty-tree staging, and stale `index.lock`.
- `scripts/disk-usage.sh` – script for top‑5 directory size listing.
- `references/delegate-task-pattern.md` – usage patterns for the `delegate_task` tool (top-level only, not importable).
- `references/branch-normalization-gotchas.md` – exact command sequence + failure modes for default-branch flip, remote/local `master` deletion, stale `origin/HEAD`, dirty-tree staging, and stale `index.lock`.
- `references/github-actions-yaml-validation.md` – how to validate a committed GitHub Actions YAML locally, including the PyYAML `on:` → bool `True` gotcha.

## Pitfalls
- Forgetting to push branch‑protection changes: ensure `gh api` calls include `--method PATCH`.
- Bun migration may break scripts; always run `bun run lint` after edits.
- CI workflow may reference missing secrets – add placeholder secrets in the workflow file.
- **CI commands may not exist in package.json:** before committing a CI workflow, verify every `bun run <script>` the workflow calls maps to a real script. The `test` script is frequently absent even when `vitest` is installed — add `"test": "vitest run"` explicitly.
- **Scan before migrating:** `package-lock.json` files may live in multiple project subdirectories. Run `find . -name 'package-lock.json' -not -path '*/node_modules/*'` first to discover all npm‑using projects.
- **Workspace CI path drift:** when a project root moves under `projects/*`, old files may still contain active path tokens. Update `.github/workflows/*.yml` and `.github/copilot-instructions.md` in one pass, then verify each changed workflow file contains the new path tokens and stale root paths are no longer used operationally. See `references/workspace-ci-path-drift.md`.
- **Stale `.git/index.lock`:** if git errors `Unable to create '.../.git/index.lock': File exists`, confirm no git process is running (`tasklist | grep -i git` on Windows, `ps aux | grep '[g]it'` on Linux) and check the lock's mtime (`stat -c '%y' .git/index.lock`). If stale (no process, old timestamp), `rm -f .git/index.lock` and retry. Do NOT remove it while a real git process holds it.
- **Subdir is not a repo:** a task naming `docs/` or `projects/X/` may mean a subdir of a monorepo, not a standalone repo. Confirm with `git rev-parse --show-toplevel` + `gh repo view --json name` before branch/default/migration ops.
- **Validate a committed GitHub Actions YAML locally before pushing:** there is no build suite for a workflow config — do a local parse + spec-conformance check instead. PyYAML parses the bare `on:` key as boolean `True`, so read it as `doc.get('on', doc.get(True))`; otherwise `doc.get('on')` returns `None` and trigger assertions mislead. Snippet in `references/github-actions-yaml-validation.md`. A true green CI run only happens after push — do NOT claim "CI passes" from a local parse.

---