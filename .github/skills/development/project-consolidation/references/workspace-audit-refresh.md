# Workspace Audit Doc Refresh

Refresh stale workspace-level inventory/audit documentation by querying live state from GitHub API + filesystem scans. Produces structured markdown reports that accurately reflect current reality.

## When to Use

- Audit docs (`repo-inventory-context.md`, `repo-normalization-report.md`, `ignore-file-audit-report.md`, `research-doc-cross-reference.md`, `per-repo-research-summary.md`) are stale
- Branch state, ignore file coverage, or research doc presence needs verification
- Workspace documentation drifted from filesystem state

## Workflow

### Phase 1: Gather Live State

#### Remote branch state (all repos)

```bash
# For each repo: get remote branches + default branch
gh api repos/owner/repo/branches --paginate --jq '.[].name'
gh api repos/owner/repo --jq '.default_branch'
```

**Pitfall:** The `gh repo view` JSON field is `defaultBranchRef` (not `defaultBranch`). Use `gh api repos/o/r --jq '.default_branch'` instead — the REST API field is `default_branch`.

#### Local branch state

```bash
cd projects/<name> && git branch | head -20
```

#### Working-tree dirtiness

```bash
cd projects/<name> && git status --porcelain | head -60
```

#### Ignore files (top-level + nested)

```bash
find . -maxdepth 2 -name ".*ignore" -not -path "*/.git/*" -not -path "*/node_modules/*" 2>/dev/null | sort
```

**Pitfall — Windows broken symlinks in node_modules:**
On Windows, `pathlib.rglob` from Python crashes with `FileNotFoundError` when encountering broken symlinks inside `node_modules/.pnpm`. Always use `os.walk` with an exclusion set when scanning a workspace that may contain PNPM node_modules:

```python
EXCLUDE_DIRS = {'node_modules', '.pnpm', '.git', '.next', '.venv',
                '__pycache__', '.mypy_cache', '.pytest_cache'}
for root, dirs, files in os.walk(path):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    ...
```

Or use shell `find` with `-not -path` exclusions (as above).

#### Research doc presence

```bash
find projects/ -maxdepth 4 -name "*RESEARCH*" -o -name "*_RESEARCH*" 2>/dev/null | grep -v node_modules | grep -v .git | sort
```

### Phase 2: Compare With Existing Docs

Read the stale doc to understand what it claims. Then compare with live data:

| Claim | Live Check | Action |
|-------|-----------|--------|
| "13 repos" | Count actual project dirs | Update to 14 (or real count) |
| "No remote configured" | gh api returns remote | Mark as done |
| "Missing ignore file" | find shows file exists | Remove from gap list |
| "Branch normalized" | gh branches show production/development | Confirm or flag |

### Phase 3: Generate Documents

#### Doc 1: repo-inventory-context.md
Branch state table (repo, owner, local/remote branches, default, dirty flag), ignore file matrix with coverage totals, research doc cross-ref, consolidation target status.

#### Doc 2: repo-normalization-report.md
Which repos are normalized (production/development on origin, default=production). Exception list. Working-tree dirtiness table.

#### Doc 3: ignore-file-audit-report.md
Coverage summary per ignore type. Repo-by-repo assessment. Nested gitignore tracking. Verdict on gaps.

#### Doc 4: research-doc-cross-reference.md
Status of each RESEARCH_*.md file. Missing per-project reports table.

#### Doc 5: per-repo-research-summary.md
Repo matrix (purpose, stack, setup, dirty flag). Notable deviations section.

### Phase 4: Verify

```bash
# Confirm no stale "13 repos" references remain
grep -rn "13 repos" docs/ --include="*.md"

# Check file sizes are reasonable
wc -l docs/repo-inventory-context.md docs/repo-normalization-report.md docs/ignore-file-audit-report.md docs/research-doc-cross-reference.md docs/per-repo-research-summary.md
```

## Pitfalls

- **write_file path resolution** — On Windows, `write_file` resolves paths relative to the terminal's CWD, not the filesystem root. Paths starting with `/c/Users/...` get mangled to `C:\c\Users\...` when CWD is a subdirectory. Always use absolute `C:\Users\...` paths for write_file on this host.
- **gh API vs gh repo view field names** — REST API uses `default_branch` (snake_case in `--jq '.default_branch'`); GraphQL (`gh repo view --json`) uses `defaultBranchRef` not `defaultBranch`. Prefer `gh api` for REST consistency.
- **PNPM broken symlinks** — `node_modules/.pnpm` contains symlinks that crash Python's `pathlib.rglob` on Windows with `FileNotFoundError`. Always use `os.walk` with exclusion set.
- **execute_code terminal() workdir param** — When spawning many commands in `execute_code`, passing `workdir` to `terminal()` can be unreliable. Safer to use `cd path && command`.
