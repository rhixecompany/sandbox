# Batch PR workflow for a multi-repo workspace

Use this when a sandbox contains many independent git repos and the task is to commit, push, and open PRs across all of them.

## What changed in practice
- The workspace may contain both real git repos and plain folders.
- Some repos may already be in a rebase state; `git switch -C` will fail until the rebase is quit.
- The root workspace repo may track nested repos or helper folders and must be staged carefully.
- `gh pr create` should be guarded with `gh pr list --head <branch> --state open --json url` so existing PRs are reused.

## Batch order
1. Leaf repos with changes.
2. Repos that need repo initialization.
3. Root workspace repo last.

## Reliable per-repo sequence
1. Inspect state: `git status --short`, `git branch --show-current`, `git log -1 --oneline`.
2. If the repo is mid-rebase, run `git rebase --quit` first.
3. Switch/create branch: `git switch -C chore/workspace-maintenance-YYYYMMDD`.
4. Stage: `git add -A`.
5. Commit: `git commit --no-verify -m 'chore: snapshot local workspace updates'` when snapshotting unrelated generated files.
6. Push: `git push -u origin <branch>`.
7. PR: reuse an existing open PR for that branch if present.

## Root repo caution
If the root repo contains nested git repos or local helper folders, exclude them from the root snapshot rather than staging them accidentally.
- For one-off local-only folders, `.git/info/exclude` is safer than committing ignore rules.
- If the workspace uses submodules, confirm with `git submodule status --recursive` before staging.

## Initialization of plain folders
Only initialize non-git folders when the user explicitly asked for them to become separate repos.
Suggested sequence:
- `git init -b development`
- commit the initial snapshot
- create the remote repo with `gh repo create OWNER/REPO --public --source . --remote origin --push`
- then create or confirm the PR
