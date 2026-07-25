# Contributing — SandBox Monorepo

## Branching Model

```text
master ──── production releases
    └── development ──── integration branch
            ├── feat/<project>/<short-description>
            ├── fix/<project>/<short-description>
            ├── refactor/<project>/<short-description>
            ├── docs/<project>/<short-description>
            └── chore/<project>/<short-description>
```

| Branch | Purpose | Protected | PR target |
| -------- | --------- | ----------- | ----------- |
| `master` | Production-ready code | Yes | — |
| `development` | Active integration | Yes | ← all PRs |
| `production` | Release mirror | Yes | ← `master` hotfixes |

## Branch Naming Convention

```text
<type>/<project>/<kebab-case-description>
```

**Examples:**

- `feat/resume-maker/add-html-output`
- `fix/bash/install-script-permissions`
- `docs/root/update-readme`
- `chore/root/upgrade-bun-version`
- `refactor/ecom/cleanup-models`

**Types:** `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`

**Project:** one of the 18 sub-projects under `projects/`, or `root` for workspace-level changes (CI, config, docs, tooling).

## Workflow

```bash
# 1. Start from a clean development
git checkout development
git pull origin development

# 2. Create your feature branch
git checkout -b feat/resume-maker/add-html-output

# 3. Make changes — scope them to the project
#    (don't touch unrelated projects in the same branch)

# 4. Commit early, commit often
git add <files>
git commit -m "feat: add HTML output option to resume generator"

# 5. Keep your branch up to date
git fetch origin
git rebase origin/development

# 6. Push and open a PR
git push origin feat/resume-maker/add-html-output
# → Open PR at https://github.com/rhixecompany/sandbox/compare
#   Base: development  ←  Compare: feat/resume-maker/add-html-output
```

## Commit Message Format

Follow conventional commits:

```text
<type>: <description>

feat: add HTML output option
fix: handle empty resume data gracefully
docs: update README with new flags
chore: upgrade markdown-pdf to 11.0.0
refactor: extract PDF generation to separate module
```

## PR Best Practices

1. **One concern per PR** — don't mix a bug fix with a refactor or a new feature
2. **Scope to the project** — changes outside the declared project get flagged in review
3. **Keep it small** — aim for <300 lines changed. Large PRs are harder to review and more likely to have issues
4. **Rebase, don't merge** — keep a linear history on `development`
5. **Clean working tree** — only files relevant to the PR should be changed (no drive-by formatting, no stray untracked files)

## CI Expectations

When you open a PR, the PR CI workflow automatically:

1. Detects which project(s) changed
2. Runs the appropriate checks per project (type-check, lint, tests)
3. Validates the PR template is filled out
4. Checks for forbidden files (`.env`, credentials, large binaries)

All checks must pass before merging.

## Before Opening a PR

```bash
# Verify your changes are scoped correctly
git diff --stat origin/development

# Run checks in affected project(s)
cd projects/<name>
bun run typecheck && bun run lint

# Or at root if root-level change
bun run typecheck && bun run lint

# Review your own diff
git diff origin/development
```
