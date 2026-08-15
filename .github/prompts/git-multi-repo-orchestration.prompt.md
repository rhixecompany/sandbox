---
name: git-multi-repo-orchestration
title: git multi repo orchestration
description: Prompt for git-multi-repo-orchestration
version: "1.0.0"
tags: []
trigger: git-multi-repo-orchestration
metadata:
  hermes:
    profile: default
    priority: medium
    categories: []
  copilot:
    model_required: claude-opus
    context_length: medium
  opencode:
    enabled: true
    compatibility: compatible
  codex:
    enabled: false
    model_preferred: text-davinci-003
---

---
name: git-multi-repo-orchestration
title: Git Multi-Repo Orchestration
description: Load and use all git skills to run add/commit/push, submodule sync, create/update/open/close
  PRs (gh pr create, review-then-merge), merge directly into development, and sync
  to production across all repos in ./projects.
version: 1.0.0
license: MIT
author: Alexa
toolsets: null
scripts: []
skills: null
formatter: default
plan: plans/git-multi-repo-orchestration.md
dependencies:
- skill:gh-cli
- skill:git-commit
- skill:git-helper
- skill:git-submodule-workflow
- skill:github-pr-workflow
- skill:github-repo-management
- skill:github-code-review
- skill:finishing-a-development-branch
- skill:git-history-preserving-migration
- skill:workspace-audit
- skill:repo-management
- tool:mcp-github
tags:
- audit
- frontend
- git
- prompts
- skills
- typescript
- workflow
trigger: /git-multi-repo-orchestration
metadata:
  hermes: {}
---

## Goal

Load and use all git skills to run the full git lifecycle across **all repos in `./projects`**:

- `git add` → `git commit` (conventional) → `git push` to `development`
- Submodule sync (foreach, update, parent pointer bump)
- Create, update, open, and close all PRs via `gh pr create` (**review-then-merge**)
- Merge directly into `development` and push
- Sync `development` → `production`

## Prerequisites

- [ ] `gh auth status` — active account + `repo`, `workflow` scopes
- [ ] Working directory is the SandBox root (`~/Desktop/SandBox`)
- [ ] `git submodule status` baseline recorded
- [ ] User approval for the repo batch (no commits/pushes without consent)

## Skill Bundle

Load ALL git skills first: `git-multi-repo-orchestration` (umbrella), `gh-cli`, `git-commit`, `git-helper`, `git-submodule-workflow`, `github-pr-workflow`, `github-repo-management`, `github-code-review`, `finishing-a-development-branch`, `git-history-preserving-migration`, `monorepo-pr-workflow`, `workspace-audit`, `repo-management`.

## Workflow

### Phase 0: Inventory

```bash
cd ~/Desktop/SandBox
gh auth status
git submodule status
for d in projects/*/; do [ -d "$d/.git" ] && echo "${d#projects/}"; done
```

Record dirty baseline per repo. **Do not proceed if auth is missing.**

### Phase 1: Commit & Push to Development

For each repo on `development`:

```bash
cd projects/<repo>
git status --short
git add <files>
git commit -m "type(scope): subject

- bullet detail"
git push origin development
```

- Conventional types: `feat`, `fix`, `refactor`, `docs`, `test`, `ci`, `chore`, `perf`.
- Feature-branch repos: push branch, open PR (Phase 3), do NOT merge directly.

### Phase 2: Submodule Sync

```bash
git submodule foreach 'git status --short && git fetch origin'
git submodule update --remote development
git submodule sync
# From SandBox root, AFTER child pushes:
git add projects/* && git commit -m "chore(submodules): bump project pointers"
git push origin development
```

### Phase 3: PR Lifecycle — Review-Then-Merge

```bash
git checkout -b feat/<description> development
# make changes, commit, push
git push -u origin HEAD

gh pr create \
  --title "feat: <description>" \
  --body "## Summary
- <change 1>
- <change 2>

## Test Plan
- [ ] CI green
- [ ] Reviewed" \
  --base development
```

- **Update:** `gh pr edit <N> --title ... --body ...`
- **Review:** `gh pr diff <N>`, `gh pr checks <N> --watch`, `--add-reviewer <user>`
- **Merge after review:** `gh pr merge <N> --merge --delete-branch` (or `--squash`)
- **Close unmerged:** `gh pr close <N> --comment "<reason>"`
- **After merge:** `git checkout development && git pull origin development`

**Gate:** no `--auto` / admin-merge — wait for review.

### Phase 4: Development → Production Sync

```bash
git checkout production && git pull origin production
git merge --ff-only development
git push origin production
git checkout development
```

**FF failure:** STOP → request explicit user approval → force-push and log to `.copilot/session-state/PRODUCTION_FORCE_PUSH_LOG.md`.

### Phase 5: Verification

```bash
for d in projects/*/; do
  [ -d "$d/.git" ] || continue
  cd "$d" && echo "== ${d#projects/}: $(git branch --show-current) | $(git status --short | wc -l) dirty"
  cd ~/Desktop/SandBox
done
git submodule status | grep -v '^ ' && echo "SUBMODULES DIRTY" || echo "SUBMODULES CLEAN"
gh pr list --state open --limit 50
```

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- **No commit/push unless asked** — approval per repo batch.
- **No force-push** to `production` without explicit user consent (log it).
- **No auto-merge** — review-then-merge is the default PR flow.
- **No branch deletion** without approval.
- **Submodule ordering** — child pushes BEFORE parent pointer commit.
- **Never blind `git add -A`** at SandBox root — `.copilot/` is git-ignored session workspace.

## Verification

- [ ] All repos on `development` pushed with conventional commits
- [ ] `git submodule status` clean (no `+` prefix)
- [ ] PRs review-then-merged (or open for review, as requested)
- [ ] `production` synced to `development` (FF or approved force-push)
- [ ] Final sweep: 0 unexpected dirty repos
- [ ] Audit trail logged

## MCP Servers & Tools

Prefer MCP-first per tooling policy: `github` (repo/PR API), `filesystem` (file ops), `terminal` (git/gh), `sequential-thinking` (planning).

## Tasks

- [ ] Phase 0: verify auth, discover repos, baseline
- [ ] Phase 1: commit + push each repo to development
- [ ] Phase 2: submodule sync + parent pointer bump
- [ ] Phase 3: open/update/review/merge/close PRs
- [ ] Phase 4: sync development → production
- [ ] Phase 5: final sweep + audit trail

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`git-flow-branch-creator.prompt.md`](git-flow-branch-creator.prompt.md)

