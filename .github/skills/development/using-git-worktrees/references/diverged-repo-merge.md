# Diverged Repo Merge: Phase 1a (comicwise_push_clean → comicwise)

**Date:** 2026-06-01
**Context:** Real execution of `Prompts/repo.prompts.md` Phase 1a — eliminate `comicwise_push_clean` duplicate by merging unique assets into `comicwise`.

## Repo State

| Property | comicwise | comicwise_push_clean |
|----------|-----------|---------------------|
| Commits | 79+ | 3 |
| Branches | 6 | 3 (main + chore/*) |
| Default | main | main |
| Remote | github.com/Rhixe-company/comicwise.git | same remote |
| History | unrelated to remote | diverged from comicwise |
| Files | 878 | ~400 unique |

## Asset Identification: diff -rq

```bash
cd projects/comicwise
diff -rq --exclude='.git' ../comicwise/ ../comicwise_push_clean/ | grep "Only in ../comicwise_push_clean"
```

This revealed:
- **Root dotfiles:** .editorconfig, .gitattributes, .env.example, .all-contributorsrc, .codespellrc, .cwrc.json (all unique to push_clean)
- **Agent files:** 139 `.agent.md` files under `.github/agents/` (comicwise had 15)
- **GitHub metadata:** copilot/, plugin/, dependabot.yml, instructions/ (3 files), prompts/ (5), skills/ (1), workflows/ (11)
- **Source code:** Extensive differences in src/ (actions, app, components, dal, database, hooks, lib, schemas, services, stores, tests, types)

## Merge Rules Applied

1. **Root dotfiles** — All copied, except `.gitignore` (comicwise's was restored as authoritative)
2. **Agent files** — Merged with "if not exists" guard: kept comicwise's 15, added push_clean's 139 unique → 154 total
3. **GitHub metadata** — Copied all unique subdirectories: copilot, plugin, dependabot, instructions, prompts, skills, workflows
4. **Source code** — Kept comicwise (79 commits of history) as authoritative for overlapping files. Source differences noted but not merged automatically.

## Worktree Isolation

```bash
cd projects/comicwise
git branch feat/merge-push-clean main
git worktree add ../comicwise-merge-wt feat/merge-push-clean
```

After merge commit in worktree:
```bash
cd projects/comicwise
git checkout main
git merge feat/merge-push-clean --no-ff
```

## Windows Worktree Removal

`git worktree remove ../comicwise-merge-wt` failed with `Permission denied`.

**Fix:** `rm -rf ../comicwise-merge-wt && git worktree prune`

## Results

- **Files merged:** 152 (32,379 insertions)
- **Agents:** 15 → 154
- **Commit:** `b282302 chore: merge comicwise_push_clean assets into comicwise`
- **Source deleted:** `comicwise_push_clean/` removed
- **Git status:** Clean after merge
