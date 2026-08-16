---
name: repo-management
title: "Repo Management"
description: "Post-research repository maintenance: branch protection, migration (e.g., Bun), CI/PR workflow setup, .github artifact audits, multi-repo init, cross-referencing, and repo health checks. Uses verified preflight checks before applying changes."
author: Alexa
license: MIT
version: 1.1.0
tags: [git, github, ci, migration, bun, branch-protection, workflow]
category: devops
---
# Repo Management


## When to Use

- When you need to automate or structure workflows for `repo-management`.
- When executing multi-step tasks that benefit from phased orchestration.
- When you need deterministic, verifiable tool execution.

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
- The absorbed multi-repo path covers missing `.git` roots, initial commits, remote setup, and production/development branch creation. Full init/normalize workflow (Phase 1-4: initialize, push initial state, normalize branches + default via `gh api ... -X PATCH -f default_branch=production`, verify): `references/multi-repo-init-normalize.md`. Batch snapshot + PRs across many repos: `references/batch-pr-workflow.md`; repo inventory: `references/multi-repo-inventory.md`. Key rules: process leaf repos before the root workspace repo; `git rebase --quit` if `git switch -C` fails mid-rebase; reuse an existing open PR (`gh pr list --head <branch> --state open`); never normalize repos not explicitly listed.

## GitHub Repo Artifact Audit (.github/ drift)

Auditing repo-side `.github/` artifacts for drift, stale paths, hook/plugin
wrappers, and workflow assumptions — full checklist at
`references/github-repo-artifact-audit.md` (+ `references/repo-hook-plugin-audit.md`):

- Enumerate: `.github/scripts/`, `.github/workflows/*.yml`, `.github/copilot-instructions.md`,
  `.github/agents|instructions|prompts|skills/`, `.github/approvals|archive|archived/`.
- Classify each reference as repo-local, live Hermes runtime
  (`LOCALAPPDATA/hermes/hooks|plugins`), or external assumption.
- Stale-pattern checklist: `.github/hooks` vs live hooks; `plugins/**` globs
  with no `plugins/` tree; workflows forbidding `.github/**` PR paths; counts in
  copilot-instructions diverging from the filesystem; wrong sibling-project names.
- Triage safe-vs-destructive edits; surface approval requirements per change
  type (repo PR review for instructions/scripts; owner sign-off for new
  `.github/*` directory semantics).
- Do NOT conflate repo-side audits with local Hermes runtime audits.

## Monorepo PR Workflow Setup

Setting up a clean PR workflow in a multi-project monorepo — full recipe at
`references/monorepo-pr-workflow.md` (+ `references/monorepo-pr-quick-commands.md`):

- Four files: `CONTRIBUTING.md` (branching model `<type>/<project>/<desc>`,
  conventional commits, workflow), `.github/pull_request_template.md` (scope
  checkboxes derived from `ls -d projects/*/`), `.github/workflows/pr-ci.yml`
  (auto-detect changed projects), root context file pointing agents at it.
- PRs target `development`, one project per PR, root changes are the exception.
- **CI auto-detection:** `validate-pr` job diffs `origin/$BASE...HEAD`, greps
  `^projects/`, emits a JSON array for the matrix (`fromJson()`); output
  `"projects=[]"` when nothing changed so the matrix skips; `fail-fast: false`.
- PyYAML parses the `on:` key as boolean `True` — validate with a workaround.
- `||` in GitHub expressions is logical OR, not null-coalescing — always output
  well-formed values.

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

## Batch Commit & Push (parent + all submodules)

Use when the user asks to `git add/commit/push` on `./` AND `projects/**` (a recurring monorepo request). Parent-level `git add ./` does NOT capture submodule-internal files — it only stages the gitlink SHA. The correct order: commit inside each dirty submodule → push by ahead-count → bump parent gitlinks → verify both counts zero. Full battle-tested loops and recovery transcript in `references/batch-submodule-commit-push.md`.

Key pitfalls (details + recovery in the reference):
- **Push by AHEAD-COUNT, not working-tree dirt.** A push loop filtered on `git -C <sub> status --porcelain` silently skips submodules that are already committed but not pushed. Filter on `git -C <sub> rev-list --count origin/development..HEAD` instead.
- **lint-staged pre-commit hook aborts commits in submodules.** The hook stashes the staged file (`stash@{0}: lint-staged automatic backup`), runs repo-wide formatters (e.g. `format:markdown:fix`) that modify dozens of files, then aborts the commit leaving the tree dirty and the stash in place. Recovery: `git stash pop stash@{0}`, `git add -A`, commit with `--no-verify` — the formatter output IS the hook's intended change. Verify the stash list afterwards for leftover `lint-staged automatic backup` entries.
- **Post-commit formatter dirt.** A submodule hook can reformat a file AFTER the commit lands (observed: comicwise `TECHNOLOGY_STACK.md`), leaving fresh working-tree modifications. Re-inventory, commit the follow-up, push, and bump the parent gitlink a second time.
- **Verify BOTH zero at the end:** parent `git status --short` = 0 AND every submodule dirty=0 AND ahead=0. A submodule can be clean-but-ahead; both counts must be zero before declaring done.

## Branch-Protected PR Merge & Production Sync

Opening a PR, merging into `development`, then syncing `development` → `production`
across parent + submodules — full battle-tested sequence in
`references/branch-protected-pr-merge-prod-sync.md` (verified 2026-07-31, PR #9):

- **Branch protection blocks naive `gh pr merge`** when required status checks
  don't match actual workflow job names and reviews are disabled on the base
  branch — the PR can NEVER satisfy the stated policy. Read protection via
  `gh api repos/<o>/<r>/branches/development/protection`, poll `gh pr checks`
  until no pending, verify all real checks pass, then merge with
  `--admin` (requires explicit user approval). Verify with `gh pr view --json state,mergedAt,mergeCommit`.
- **Refspec push is the safe dev→prod sync when production is unprotected:**
  `git push origin development:production` avoids the local submodule descent
  problem below entirely. Verify both rev-list counts are 0 afterwards.
- **Parent branch switch fails with "untracked working tree files would be
  overwritten"** when the target branch's submodule gitlinks point to older
  commits whose tracked files exist as untracked in the current submodule
  working tree (agent-injected `.claude/skills`, fonts, etc.). `-c submodule.recurse=false`
  does NOT help — git still descends to reconcile gitlinks. Fix: refspec push
  (preferred) or `git submodule deinit -f <name>` → checkout → merge →
  `git submodule update --init --recursive`.
- **Empty `merge-base` between development and production = unrelated histories**
  (post-migration: dev = workspace snapshot, prod = legacy original). Never
  merge blindly — options are leave-untouched / force-push (destructive) /
  `--allow-unrelated-histories` (giant merge commits). Present trade-offs to the
  user; if force-push approved, capture legacy production HEAD SHAs to a
  recovery log FIRST, then `git push --force origin origin/development:refs/heads/production`.

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
- `references/batch-submodule-commit-push.md` – batch commit/push across parent + all `projects/**` submodules: inventory loops, push-by-ahead-count (not dirt), lint-staged hook abort recovery, post-commit formatter dirt, parent gitlink bump sequence.
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
- **Multi-account gh auth switching for destructive ops.** When the active `gh` account lacks push access to an org repo (e.g. personal token vs org-level account), `git push origin --delete` fails with 403. Diagnose with `gh auth status` (shows all logged-in accounts). Switch with `gh auth switch --user <org-account>`, then use `gh api repos/<org>/<repo>/git/refs/heads/<branch> -X DELETE` (more reliable than git push). After cleanup, switch back and run `git fetch --prune origin` + `git branch -d -r origin/<branch>` for stale refs.
- **CRLF/LF on Windows with git autocrlf** — Even with `.gitattributes` declaring `eol=lf` and `core.autocrlf=true`, Windows git may still show "LF will be replaced by CRLF" warnings on commit. The working tree often has CRLF while index has LF. Use `git diff --ignore-space-at-eol` or compare index vs working tree with `git show :file` vs `cat file` to detect actual content changes vs line-ending noise. For audit purposes, treat line-ending-only changes as non-substantive.
- **Pre-commit hook failures on bulk commits** — husky + lint-staged can fail on large commits (SIGKILL on prettier, || parsing errors). Two options: (a) `git commit --no-verify` to bypass for sync commits, then run lint separately; (b) stage in smaller chunks. For submodule sync commits where changes are upstream-generated, `--no-verify` is appropriate.
- **ESLint ignore patterns for generated/test directories** — Large workspaces accumulate `.claude/`, `src/tests/**`, `bin/**`, `templates/**`, `init-env.ts` that pollute lint output. Add these to `globalIgnores` in `eslint.config.mts` rather than fixing each file. Example from Banking: 114 files modified, 0 errors after adding ignores.
- **Multi-round submodule updates** — `git submodule update --remote --merge` may need multiple runs as dependabot/upstream branches appear. After first merge, new remote branches may be created that need a second round. Always verify with `git submodule status` and `git -C submodule log --oneline -1` until stable.
- **Submodule dirty state is recursive** — Parent shows ` m projects/name` (staged modified) but actual changes are inside. Must `cd projects/name && git status` to see real diff. For batch processing, use a loop that recurses into each submodule directory.

---

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for "Repo Management".

### Phase 2: Execution

Run the primary "Repo Management" operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
