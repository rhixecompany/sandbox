---
name: monorepo-pr-workflow
title: Monorepo PR Workflow (branching, CI, PR templates)
description: Setup a clean GitHub PR workflow for monorepos with multiple sub-projects — branch naming, CONTRIBUTING.md, PR template, and CI auto-detection.
author: Hermes Agent
license: MIT
version: 1.0.0
platforms: [linux, macos, windows]
---
# Monorepo PR Workflow

Class-level skill for setting up a clean PR workflow in a multi-project monorepo (e.g. a `projects/` directory with 10+ independent sub-projects). Covers the four files you need and their interdependencies.


## When to Use

- When you need to automate or structure workflows for `monorepo-pr-workflow`.
- When executing multi-step tasks that benefit from phased orchestration.
- When you need deterministic, verifiable tool execution.

## Overview

Automated reasoning and workflow tool for `monorepo-pr-workflow`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## The Four Files

| File | Purpose | Created once |
|------|---------|-------------|
| `CONTRIBUTING.md` | Branching model, naming conventions, commit format, step-by-step workflow | Yes |
| `.github/pull_request_template.md` | PR scope checklist, type-of-change, quality gates | Yes |
| `.github/workflows/pr-ci.yml` | Auto-detect changed projects, per-project checks, matrix strategy | Yes |
| Root project context file | Section pointing agents to the workflow | Update |

## Branching Model

```
master ──── production
    └── development ──── PR target
            ├── feat/<project>/<description>
            ├── fix/<project>/<description>
            ├── refactor/<project>/<description>
            ├── docs/<project>/<description>
            └── chore/<project>/<description>
```

Key rules:
- **PRs target `development`**, not `master`
- **Branch naming:** `<type>/<project>/<kebab-description>` — e.g. `feat/resume-maker/add-html-output`
- **One project per PR** — root-level CI/config changes are the only exception
- **Commits:** conventional commits scoped to the project

## CONTRIBUTING.md Structure

Document these sections:

1. **Branching Model** — diagram and table of branch roles
2. **Branch Naming Convention** — `<type>/<project>/<description>` with examples
3. **Step-by-step Workflow** — `git checkout -b`, commit, rebase, push, PR
4. **Commit Message Format** — conventional commits (`feat:`, `fix:`, `docs:`, `chore:`)
5. **PR Best Practices** — one concern per PR, scope to project, rebase over merge
6. **CI Expectations** — what the workflow checks per project
7. **Before Opening a PR** — the checklist commands to run

## PR Template Design

Include these sections:

- **Description** — what the PR does
- **Scope** — checkbox list of all sub-projects, plus "Root"
- **Type of Change** — conventional commit types as checkboxes
- **Checklist** — scoped changes, typecheck/lint passed, diff reviewed, no secrets
- **Related** — issue links

Derive the scope list from `ls -d projects/*/`.

## CI Pattern: Auto-Detect Changed Projects

The workflow needs a `validate-pr` job that detects changed projects, then fans out to per-project checks via a matrix strategy.

Key design decisions:

1. **`validate-pr` job** — `git diff --name-only origin/$BASE...HEAD --` to find changed files, then `grep '^projects/' | sed` to extract project names, output as JSON array for the matrix.
2. **Matrix job** — `strategy.matrix.project` from the validate-pr output. Each matrix instance checks one project.
3. **Toolchain detection** — inside the matrix job, detect if the project is Bun/Node, Python, or unknown, then run appropriate checks.
4. **Forbidden file check** — grep for `.env`, `.pem`, `.key`, `credentials` in the diff.
5. **PR size warning** — flag PRs with >100 changed files.

### validate-pr output shape

```yaml
outputs:
  projects: ${{ steps.detect-projects.outputs.projects }}  # JSON array
  has_root_changes: ${{ steps.detect-projects.outputs.has_root_changes }}
```

The `projects` output must be a **JSON array** (not space-separated) so the matrix can consume it via `fromJson()`:

```bash
PROJECTS=$(echo "$CHANGED" | grep '^projects/' | sed 's|^projects/\([^/]*\)/.*|\1|' | sort -u)
JSON_ARRAY=$(echo "$PROJECTS" | jq -R -s -c 'split("\n") | map(select(length > 0))')
echo "projects=$JSON_ARRAY" >> "$GITHUB_OUTPUT"
```

## Pitfalls

- **YAML `on:` key in PyYAML** — PyYAML 1.1 treats `on` as a boolean. GitHub Actions' parser handles it correctly. If you're validating the YAML locally with PyYAML, you'll get a false positive error from the `on:` key. Use a workaround (replace `on:` with `on_key:` before parsing) or use a GitHub-specific YAML linter.
- **Matrix with empty result** — when no projects changed, output `"projects=[]"` so `fromJson('[]')` produces an empty matrix and GitHub Actions skips the matrix job automatically. Check against `'[]'` in the `if` condition.
- **`needs:` syntax** — `needs: validate-pr` (scalar) is valid for a single dependency, but `needs: [validate-pr]` (list) is more explicit. Both work.
- **`||` in GitHub expressions** — GitHub Actions `||` is logical OR, not null-coalescing. Don't rely on it for default values in `fromJson()`. Always output a well-formed value.
- **Matrix fail-fast** — set `fail-fast: false` on matrix jobs so one project's failure doesn't cancel other project checks.

## Verification

After creating the files:
1. Validate YAML with `python3 -c "import yaml; yaml.safe_load(open('path/to/workflow.yml'))"` (ignore the `on:` key false positive)
2. Confirm PR template has scope checkboxes for all projects
3. Confirm CONTRIBUTING.md covers branching model, naming, and step-by-step flow
4. Verify the root context file references the workflow

## Related Skills

- `github` — PR lifecycle, authentication, code review, issues (single-repo focused)
- `ci-cd-pipeline-builder` — generates CI/CD pipelines from stack detection
- `finishing-a-development-branch` — completion workflow for finished branches
- `hermes-setup` — quick commands, display settings, and broader Hermes config tuning
