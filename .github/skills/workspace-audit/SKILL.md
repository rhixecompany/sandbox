---
author: Alexa
description: 'Multi-repo workspace auditing: batch-scan N repos for branch state,
  ignore files, working-tree dirtiness, research docs, and generate markdown reports.'
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: workspace-audit
tags:
- imported
title: Workspace Audit
version: 1.0.0
---
# Workspace Audit

Batch-scan N repos for branch state, ignore files, working-tree dirtiness, and research docs. Generates standardized markdown documentation.

## Overview

Automated reasoning and workflow tool for `workspace-audit`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- Taking inventory of a multi-repo workspace
- Refreshing stale audit/documentation files
- Before branch normalization or consolidation work
- Checking for repos that drifted from standard branch structure
- "refresh the inventory docs", "audit the workspace", "check repo state", "proceed with the doc refresh"

## Technique

Use `execute_code` with a `terminal()` loop to batch-query all repos in a single call. Each `terminal()` call returns instantly for small commands, so N repos × M queries stays fast.

```python
from hermes_tools import terminal

base = "/c/Users/username/projects"
repos = [("repo-name", "org-or-user"), ...]

results = {}
for name, owner in repos:
    r = terminal(f"cd {base}/{name} && git branch 2>/dev/null | head -20")
    # Parse local branches
    branches = []
    for line in r.get("output","").splitlines():
        line = line.strip()
        if line and not line.startswith("("):
            branches.append(line.replace("*","").strip())

    r2 = terminal(f"gh api repos/{owner}/{name}/branches --paginate --jq '.[].name'")
    remote_branches = [b.strip() for b in r2.get("output","").splitlines() if b.strip()]

    r3 = terminal(f"gh api repos/{owner}/{name} --jq '.default_branch'")
    default = r3.get("output","").strip()

    r4 = terminal(f"cd {base}/{name} && git status --porcelain 2>/dev/null | head -60")
    status_lines = [l for l in r4.get("output","").splitlines() if l.strip()]

    results[name] = {
        "local": sorted(branches),
        "remote": sorted(remote_branches),
        "default": default,
        "dirty": len(status_lines) > 0,
        "dirty_count": len(status_lines),
    }
```

## gh API Field Names

**Critical difference** between REST and GraphQL:

| Context | Convention | Example |
|---------|-----------|---------|
| REST (`gh api repos/o/r`) | `snake_case` | `--jq '.default_branch'` |
| GraphQL (`gh repo view --json`) | `camelCase` | `--json defaultBranch` |

## Ignore File Scanning

Find top-level + nested (depth ≤ 2) ignore files:

```bash
find . -maxdepth 2 -name ".*ignore" -not -path "*/.git/*" -not -path "*/node_modules/*"
```

Categorize by type: `.gitignore`, `.dockerignore`, `.prettierignore`, `.eslintignore`, `.npmignore`, `.gcloudignore`. Track nested `.gitignore` in subdirectories (`frontend/`, `backend/`, `.opencode/`) separately.

## Batch Scan Loop Pattern

For scanning N repos in a single command (fastest approach — each `git -C` call returns instantly):

```bash
# Branch state + remote detection
for dir in projects/*/; do
  name=$(basename "$dir")
  if [ -d "$dir/.git" ]; then
    branches=$(git -C "$dir" branch | tr -d ' *' | tr '\n' ' ')
    remote=$(git -C "$dir" branch -r 2>/dev/null | grep -v HEAD | tr -d '  ' | tr '\n' ' ')
    echo "$name: $branches || $remote"
  fi
done

# Ignore files at depth 1
for dir in projects/*/; do
  name=$(basename "$dir")
  ignores=$(find "$dir" -maxdepth 1 -name '.*ignore' -type f 2>/dev/null | sort | sed 's|.*/||' | tr '\n' ' ')
  echo "$name: $ignores"
done

# Dirty state
for dir in projects/*/; do
  name=$(basename "$dir")
  dirty=$(git -C "$dir" status --short 2>/dev/null)
  if [ -n "$dirty" ]; then
    echo "--- $name ---"
    echo "$dirty"
  fi
done
```

## Submodule Dirty State

When `git status --short` in the parent shows ` m projects/<name>` (staged modified) or ` ? projects/<name>` (untracked submodule), the actual changes are **inside** the submodule, not in the parent:

```bash
# Recurse into each submodule/dirty project to find real changes
for dir in projects/*/; do
  name=$(basename "$dir")
  if [ -d "$dir/.git" ]; then
    dirty=$(git -C "$dir" status --short 2>/dev/null)
    if [ -n "$dirty" ]; then
      echo "--- $name ---"
      echo "$dirty"
    fi
  fi
done
```

Categorize each dirty repo by what it contains:
- **Staged deletions** (`D ` prefix) — intentional cleanup, often `.github/` config purges
- **Modified tracked files** (` M` prefix) — working tree changes, need review
- **Untracked new files** (`??` prefix) — new files not yet added
- **Mixed** — multiple categories present

## Doc Refresh Workflow (Stale Doc Detection)

When audit docs already exist and the task is "refresh" rather than "create":

### 1. Scan Live State (as above)
Get current branch state, dirty state, ignore files, research docs.

### 2. Read Existing Docs
Read the existing `docs/repo-inventory-context.md`, `docs/per-repo-research-summary.md`, `docs/repo-normalization-report.md`, etc.

### 3. Compare & Find Stale Sections
For each data category (branch state, dirty state, ignore files), check if the live scan differs from the doc. Common staleness patterns:
- **Dirty state drifts** — repos get cleaned, new files appear, submodules get touched
- **Ignore files change** — new files added as tool chains are activated
- **Research doc status** — new reports created or old ones removed

### 4. Apply Targeted Patches
Don't rewrite the whole doc. Use `patch` (or the Hermes equivalent) to update only stale sections:
- Update the date/refresh banner in the header
- Update dirty counts and repo-by-repo details
- Leave accurate sections untouched

### 5. Verify & Date
Verify the diff is correct, then update the file's "Generated" or "Refreshed" date.


## When NOT to Use

- When the task is outside this skill's domain
- When simpler approaches are more effective
- When required dependencies are unavailable



## Workflow

### Phase 1: Preparation

_Set up dependencies, gather inputs, validate the environment._

### Phase 2: Execution

_Run the primary workflow._

### Phase 3: Verification & Cleanup

_Validate results, document outcomes, clean up temporary resources._


### Pitfalls
- **Dirty state counts drift between scans** — a repo that had 60 staged deletions is still "dirty" but the count may change as files are committed. Re-count rather than trusting the old number.
- **Submodule dirty state ≠ parent dirty state** — parent may show `m` (staged) while submodule has complex mixed state. Always recurse.
- **comicwise exception** — divergent history repos should be noted as exceptions in every doc refresh, not silently assumed to be like all other repos.
- **profile name mismatch** — local dir `profile` maps to GitHub `rhixecompany/rhixecompany`. Always extract remote URL rather than assuming dir = repo name.

## Dirty State from `git status --porcelain`

| Prefix | Meaning | Category |
|--------|---------|----------|
| `M `, `A `, `D ` | In index | Staged |
| ` M`, ` D` | Working tree | Unstaged |
| `??` | Untracked | Untracked |

## Dependency Manifest Scanning

Detect each repo's package manager and manifest files at depth 1:

```bash
for dir in projects/*/; do
  name=$(basename "$dir")
  manifests=$(ls "$dir"/package.json "$dir"/requirements.txt "$dir"/pyproject.toml \
    "$dir"/Cargo.toml "$dir"/go.mod "$dir"/composer.json 2>/dev/null \
    | sed 's|.*/||' | tr '\n' ',' | sed 's/,$//')
  echo "$name: ${manifests:-none}"
done
```

Categorize each repo by language stack:
- **Node** — `package.json` present (Next.js, React, Express projects)
- **Python** — `requirements.txt` or `pyproject.toml` (Django, DRF, CLI scripts)
- **Dual-stack** — both Node and Python manifests (hybrid Django+Next.js projects)
- **None detected** — flag for review; may use `pip install` or `bun` directly

## CI Workflow Detection

Detect CI/CD configuration per repo:

```bash
for dir in projects/*/; do
  name=$(basename "$dir")
  cis=$(ls "$dir"/.github/workflows/*.yml "$dir"/Jenkinsfile "$dir"/.gitlab-ci.yml \
    2>/dev/null | sed 's|.*/||' | tr '\n' ' ')
  echo "$name: ${cis:-none}"
done
```

Categorize CI posture:
- **Has CI** — at least one workflow file present
- **Missing CI** — no workflow detected; gap for basic lint/test automation
- **Multi-workflow** — multiple CI workflows (build, test, e2e, issue tracking)

## Git Narrative Generation

Produce a repo story time table from commit history:

```bash
for dir in projects/*/; do
  if [ -d "$dir/.git" ]; then
    name=$(basename "$dir")
    echo "=== $name ==="
    echo "Branch: $(git -C "$dir" rev-parse --abbrev-ref HEAD 2>/dev/null)"
    echo "Commits: $(git -C "$dir" log --oneline 2>/dev/null | wc -l)"
    echo "Authors: $(git -C "$dir" log --format='%an' 2>/dev/null | sort -u | tr '\n' ',')"
    echo "Date range: $(git -C "$dir" log --format='%as' 2>/dev/null | tail -1) to $(git -C "$dir" log --format='%as' 2>/dev/null | head -1)"
    echo "Last 5 commits:"
    git -C "$dir" log --oneline -5 2>/dev/null
  fi
done
```

## Commit Convention Audit

Check conventional commit compliance:

```bash
for dir in projects/*/; do
  if [ -d "$dir/.git" ]; then
    name=$(basename "$dir")
    total=$(git -C "$dir" log --oneline 2>/dev/null | wc -l)
    conv=$(git -C "$dir" log --format='%s' 2>/dev/null | grep -cE '^(feat|fix|docs|refactor|test|chore|perf):' || true)
    pct=$([ "$total" -gt 0 ] && echo "$(( conv * 100 / total ))" || echo "N/A")
    echo "$name: $conv/$total conventional ($pct%)"
  fi
done
```

## Research Doc Scanning

```bash
find projects/ -maxdepth 4 -name "*RESEARCH*" -o -name "*_RESEARCH*" \
  2>/dev/null | grep -v node_modules | grep -v .git | sort
```

## Standard Report Files

After collecting live data, write these markdown documents:

| File | Contents |
|------|----------|
| `docs/repo-inventory-context.md` | Full branch/ignore/dirty table + research doc status |
| `docs/repo-normalization-report.md` | Branch normalization verification |
| `docs/ignore-file-audit-report.md` | Per-repo ignore file coverage + nested files |
| `docs/research-doc-cross-reference.md` | RESEARCH_* file presence and staleness |
| `docs/per-repo-research-summary.md` | Repo purpose/stack/dirty matrix |
| `docs/REPO_STORY_TIME.md` | Git narrative per project (branch, commits, timeline, key events) |
| `docs/REPO_MANAGEMENT.md` | Branch norm, .gitignore, deps, CI posture, recommendations |

### Pitfalls

- **Dirty state counts drift between scans** — a repo that had 60 staged deletions is still "dirty" but the count may change as files are committed. Re-count rather than trusting the old number.
- **Submodule dirty state ≠ parent dirty state** — parent may show `m` (staged) while submodule has complex mixed state. Always recurse.
- **comicwise exception** — divergent history repos should be noted as exceptions in every doc refresh, not silently assumed to be like all other repos.
- **profile name mismatch** — local dir `profile` maps to GitHub `rhixecompany/rhixecompany`. Always extract remote URL rather than assuming dir = repo name.
- **Dual-manifest confusion** — repos with both `package.json` and `pyproject.toml` (e.g. Banking, rhixe_scans) need careful lockfile sync. Note both manifests.
- **CI classification drift** — a `.github/workflows/` file with only issue-management actions is not "test CI." Classify workflow purpose, not just presence.
- **Commit count ≠ activity** — repos with 4 commits of "update docs, vscode configs, and research reports" may be more active than count shows if work was squashed.
- **Date range from git log** — `--format='%as'` gives author-date, not committer-date. Squashed merges may show old author dates despite recent work.
- **Conventional commit detection false negatives** — `feat(scope):` and `fix!: breaking` are conventional but basic regex may miss scoped prefixes. Precision is about 85-90%.
- **Missing manifest != missing deps** — a repo with no `package.json`/`requirements.txt` may still use tools via direct install (yt-dlp, bun). Document as "manifest missing" not "no dependencies."
- **Python `Path.exists()` in `execute_code` silently fails on MSYS paths** — on Windows, Python code inside `execute_code` cannot reliably detect `.git` directories or `.gitignore` files when using MSYS paths (`/c/Users/...`). Prefer `terminal()` shell commands (which run through git-bash and handle MSYS path translation) for all filesystem existence checks. See `batch-file-scanning-limits` reference skill for details.
- **Gitignore coverage is pattern-specific** — a `.gitignore` entry may cover `*.pyc` via `*.py[cod]`, or `build/` via `/build`, or `.env` via `.env*`. Straight string-search gives false negatives. Use the grep-based technique in `references/gitignore-audit-patterns.md` with alternative-pattern fallbacks.
- **Generated gitignores can be massive** — Template-generated gitignores (e.g., GitHub's gitignore.io, VS Code extensions) can produce 1000+ line files with duplicated/overlapping patterns. When auditing, distinguish between "hand-crafted minimal" (20-50 lines) vs "generated template" (500-1500 lines). The latter should be replaced with a curated minimal version. Example: rhixe_scans had 1375 lines, replaced with 20 lines covering actual project needs.
- **Doc refresh vs create workflow** — When existing audit docs exist, prefer targeted patches over full rewrites: (1) scan live state, (2) read existing docs, (3) diff to find stale sections, (4) patch only stale sections, (5) update refresh date. Full rewrites lose history and risk introducing errors in accurate sections.
- **Branch normalization end state** — All projects should converge to exactly 2 branches: `development` (working) + `production` (default). Legacy branches (`chore/*`, `master`, `staged`) must be purged both locally and remotely. Verify with `git branch -a` across all projects after cleanup.

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text


## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Workspace Audit operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
