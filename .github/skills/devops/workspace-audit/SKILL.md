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

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

