# Patch Classification & Debugging

Systematic method for classifying git patch files (from `git format-patch` or V4A format) into known states.

## Classification Categories

| Status | Meaning | Action |
|--------|---------|--------|
| **pre-applied** | All commit SHAs from the patch already exist in the target project's git history via `git cat-file -t` and `git log`. | Move to `patches/pre-applied/` — no action needed |
| **applied** | Patch was applied this session (new project creation or cleanup). | Document the commit hash and changes |
| **missing-target** | Target project directory doesn't exist. Check if the patch needs a new project or maps to an existing one with a different name. | Either create project from patch OR apply to the correct existing project |
| **truly-obsolete** | Cookie-cutter template, scaffolding, or dead patch. No project target. | Keep in `patches/obsolete/` with rationale |
| **reclassified** | Was in `patches/obsolete/` but proven to be `pre-applied` to an existing project. | Move to `patches/enhanced/` |

## Debugging Workflow

### Step 1: Test Applicability
```bash
cd <project-dir>
git apply --check ../<patch>.patch
```

### Step 2: Commit SHA Verification
```bash
# Extract commit SHAs from the patch header
grep '^From [a-f0-9]' ../<patch>.patch

# Verify each SHA exists in the target repo
git cat-file -t <SHA>             # returns "commit" if found
git log --oneline | grep <SHA>    # confirm in history
```

### Step 3: Handle "already exists" Errors
When `git apply --check` returns `error: <file>: already exists in working directory`:
- This means the patch creates files that already exist — common for initial-commit patches
- NOT a failure — verify commits are in history (Step 2) to confirm pre-applied status
- If commits are NOT in history but files exist, the project was seeded differently; classify as divergent

### Step 4: Reclassification Test
```bash
# Test obsolete patches against ALL project directories
for dir in projects/*/; do
    echo "=== $dir ==="
    cd "$dir"
    git apply --check ../patches/obsolete/<patch>.patch 2>&1 | head -3
    cd -
done
```

### Step 5: Final Organization
```
patches/
├── pre-applied/         # Commits already in project history
├── enhanced/            # Valid patches (reclassified from obsolete)
├── obsolete/            # Truly dead patches
├── archive/             # Historical backups
└── regenerate/          # Queued for regeneration
```

## Caveats

- **Large patches (>100 files)**: `git apply --check` may timeout. Use individual commit SHA checks instead.
- **Absolute Windows paths**: Run `grep -n 'C:\\\\Users' <patch>` — if found, the patch may need path normalization.
- **V4A multi-file patches**: Check if content already exists in the target file rather than using `git apply --check`.
