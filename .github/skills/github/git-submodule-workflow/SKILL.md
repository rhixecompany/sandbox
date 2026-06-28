---
name: git-submodule-workflow
title: "Git Submodule Configuration & Workflow"
description: >
version: 1.0.0
author: Alexa
license: MIT
tags: [git, submodules, monorepo, multi-project, github]
---
## Workflow
### Phase 1: Preparation

- Understand the context and requirements.
- Gather necessary tools and resources.

### Phase 2: Execution

- Perform the core actions required by the skill.
- Apply the techniques and procedures outlined.

### Phase 3: Verification

- Verify the results against the expected outcomes.
- Confirm that the task has been completed successfully.


## Phase 3: Commit & Cleanup

**Goal:** Commit `.gitmodules` and record conversion in version control.

### Step 3.1 — Commit `.gitmodules`

```bash
git add .gitmodules
git commit -m "chore: configure <N> projects as git submodules"
```

**Example message:**
```
chore: configure 13 project repositories as git submodules

Convert projects/ directories to git submodules with remote GitHub URLs.
Submodules tracked against main (8 projects) and develop/feature branches (5 projects).
See thoughts/plans/submodule-conversion-plan.md for inventory.
```

### Step 3.2 — Document Workflow

Write a reference guide for future submodule operations. Save to `docs/git-submodules-setup-report.md`:

```markdown
# Git Submodules Setup & Workflow

## Submodule Inventory

Generated: {date}

| Path | Remote | Branch | Last Updated |
| ---- | ------ | ------ | ------------ |
| projects/repo-a | https://github.com/org/repo-a.git | main | {commit-sha} |
| projects/repo-b | https://github.com/org/repo-b.git | develop | {commit-sha} |

## Initialization (first clone)

After cloning the parent repo, initialize all submodules:
\`\`\`bash
git submodule update --init --recursive
\`\`\`

## Updating Submodules

### Fetch latest commits from remote
\`\`\`bash
git submodule update --remote
\`\`\`

### Update specific submodule
\`\`\`bash
git -C projects/repo-a pull origin main
\`\`\`

### Commit submodule state changes
\`\`\`bash
git add projects/repo-a
git commit -m "chore: update submodule projects/repo-a to latest main"
\`\`\`

## Removing a Submodule

\`\`\`bash
git rm projects/repo-to-remove
git config -f .gitmodules --remove-section submodule.projects/repo-to-remove
git add .gitmodules
git commit -m "chore: remove submodule projects/repo-to-remove"
\`\`\`

## Resolving "modified content" State

After adding new submodules, status may show "modified content". This is normal.
To synchronize:

\`\`\`bash
git submodule status       # see current state
git submodule update       # revert to tracked commits
\`\`\`

## Branch Tracking

To change which branch a submodule tracks:

\`\`\`bash
git config -f .gitmodules submodule.projects/repo-a.branch "develop"
git submodule update --remote projects/repo-a
git add .gitmodules projects/repo-a
git commit -m "chore: change projects/repo-a branch from main to develop"
\`\`\`
```

### Step 3.3 — Commit Documentation

```bash
git add docs/git-submodules-setup-report.md thoughts/plans/submodule-conversion-plan.md
git commit -m "docs: submodules setup and workflow documentation"
```

---
metadata:
  hermes:
    tags: []


## Phase 4: Verification

**Goal:** Confirm all submodules are properly initialized and reachable.

### Step 4.1 — Status Check

Run comprehensive status:

```bash
git submodule status                   # shows commit hashes and branches
git submodule foreach git status       # shows status of each submodule
git submodule foreach git remote -v    # shows remotes for each submodule
```

**Expected:** All submodules show their tracked commit and no errors.

### Step 4.2 — Test Clone

To verify the setup works for fresh clones, test in a temporary directory:

```bash
cd /tmp
git clone https://github.com/myorg/parent-repo.git test-clone
cd test-clone
git submodule update --init --recursive
git submodule status
```

**Expected:** All submodules initialize without errors.

### Step 4.3 — Performance Check

Large monorepos with many submodules can slow down common git operations. Check:

```bash
time git status           # how long does status take?
time git log --oneline    # how long does log take?
```

**If slow:** Consider shallow cloning submodules (add `shallow = true` to `.gitmodules` for non-critical projects) or using `git clone --depth 1` during initialization.

---

## Ongoing Operations

### Updating a Submodule to Latest Remote

```bash
cd projects/repo-a
git pull origin main     # or whatever branch it tracks
cd ../..
git add projects/repo-a
git commit -m "chore: update submodule projects/repo-a to latest main"
```

### Switching a Submodule to a Different Branch

```bash
git config -f .gitmodules submodule.projects/repo-a.branch "develop"
git submodule update --remote projects/repo-a
git add .gitmodules projects/repo-a
git commit -m "chore: change projects/repo-a branch to develop"
```

### Adding a New Submodule

```bash
git config -f .gitmodules submodule."projects/new-repo".path "projects/new-repo"
git config -f .gitmodules submodule."projects/new-repo".url "https://github.com/org/new-repo.git"
git config -f .gitmodules submodule."projects/new-repo".branch "main"
git submodule update --init --recursive projects/new-repo
git add .gitmodules projects/new-repo
git commit -m "chore: add submodule projects/new-repo"
```

## Pitfalls & Troubleshooting

### Pitfall 1: "fatal: could not read Username"

**Symptom:** When initializing submodules with HTTPS URLs, git prompts for credentials.

**Fix:** Either (1) provide credentials when prompted, (2) configure SSH keys and use SSH URLs in `.gitmodules`, or (3) use `git config credential.helper store` to cache credentials locally (not recommended for sensitive repos).

### Pitfall 2: "fatal: destination path already exists and is not an empty directory"

**Symptom:** Directory exists locally but is not registered as a submodule yet.

**Fix:** Move the directory temporarily, initialize submodules, then remove the backup:
```bash
mv projects/repo-a projects/repo-a.backup
git submodule update --init --recursive
rm -rf projects/repo-a.backup
```

### Pitfall 3: Submodule Shows "modified content, untracked content"

**Symptom:** `git submodule status` shows the submodule state as dirty (modified or untracked files).

**Cause:** Local changes in the submodule that haven't been committed.

**Resolution options:**
- (A) Commit the changes in the submodule and push: `cd projects/repo-a && git add -A && git commit -m "..." && git push`
- (B) Discard local changes and revert to tracked commit: `git submodule update` or `git -C projects/repo-a reset --hard`
- (C) Ignore for now: submodule is still usable; no action needed unless you want a clean state.

### Pitfall 4: Different Team Members Using Different Branches

**Symptom:** One person updates a submodule to a feature branch; another pulls and expects main.

**Prevention:** Document which branch each submodule tracks in `.gitmodules` and enforce via policy. Use continuous integration to validate submodule branch alignment.

### Pitfall 5: `.gitmodules` Out of Sync with Actual Submodule State

**Symptom:** `.gitmodules` lists a submodule, but `.git/modules/<path>/config` or local checkout is out of sync.

**Fix:** Re-initialize:
```bash
git submodule deinit -f projects/repo-a
git submodule update --init --recursive projects/repo-a
```

---

## References

- `references/submodule-conversion-checklist.md` — step-by-step checklist for Phase 1–4
- `references/branch-tracking-patterns.md` — common branch strategies and when to use each
- `references/monorepo-performance-tuning.md` — optimization tips for large submodule sets

---

## Actions Summary

1. Inventory all local projects and their remotes (Phase 1)
2. Remove projects from git index without deleting directories (Phase 2.1)
3. Configure `.gitmodules` with paths, URLs, and branch tracking (Phase 2.2)
4. Initialize submodules and verify state (Phase 2.3–2.4)
5. Commit `.gitmodules` and document workflow (Phase 3)
6. Verify initialization works on fresh clones (Phase 4)
7. Reference provided guide for ongoing updates, branch switching, and removal


## When to Use


- When you need to perform Git Submodule Configuration & Workflow operations or tasks
- When managing Git Submodule Configuration & Workflow infrastructure or configurations
- When automating or debugging Git Submodule Configuration & Workflow workflows
- **Triggers**: "git submodule configuration & workflow" required for a project
```

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

