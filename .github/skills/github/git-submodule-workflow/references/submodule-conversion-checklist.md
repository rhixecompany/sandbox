# Submodule Conversion Checklist

Use this checklist when converting N local project directories to git submodules.

## Phase 1: Inventory & Planning

- [ ] List all projects under the parent (e.g., `projects/`): `ls -la projects/`
- [ ] For each project, verify it's a git repo: `cd projects/<name> && git status`
- [ ] For each project, check remotes: `git remote -v`
  - [ ] If no `origin` remote, add it: `git remote add origin https://github.com/org/<name>.git`
- [ ] Decide on branch tracking (main vs develop vs custom)
- [ ] Write conversion plan to `thoughts/plans/submodule-conversion-plan.md`

**Verification:**
```bash
for dir in projects/*/; do
  echo "=== $dir ==="
  (cd "$dir" && git remote -v)
done
```

## Phase 2: Conversion

- [ ] Remove all projects from git index (non-destructive):
  ```bash
  for dir in projects/*/; do
    git rm -r --cached "$dir"
  done
  ```
- [ ] Verify: `git status` shows all projects as deleted (directories still exist on disk)
- [ ] Create/update `.gitmodules` with all projects:
  ```bash
  git config -f .gitmodules submodule."projects/<name>".path "projects/<name>"
  git config -f .gitmodules submodule."projects/<name>".url "https://github.com/org/<name>.git"
  git config -f .gitmodules submodule."projects/<name>".branch "main"  # or other branch
  ```
- [ ] Verify `.gitmodules` is complete: `cat .gitmodules`
- [ ] Initialize submodules: `git submodule update --init --recursive`
- [ ] Verify all submodules initialized: `git submodule status`

**Troubleshooting:**
- [ ] If "destination path already exists" error: move directory, init, then remove backup
- [ ] If submodules show "modified content": expected after fresh conversion, no action needed

## Phase 3: Commit & Documentation

- [ ] Write workflow guide to `docs/git-submodules-setup-report.md`
- [ ] Commit `.gitmodules`: `git add .gitmodules && git commit -m "chore: configure N projects as submodules"`
- [ ] Commit documentation: `git add docs/git-submodules-setup-report.md && git commit -m "docs: submodules setup guide"`
- [ ] Verify: `git log --oneline` shows both commits

## Phase 4: Verification

- [ ] Status check: `git submodule status` — all show commit hashes, no errors
- [ ] Detailed check: `git submodule foreach git status`
- [ ] Remote check: `git submodule foreach git remote -v`
- [ ] Test fresh clone in `/tmp`:
  ```bash
  git clone <parent-url> test-clone
  cd test-clone
  git submodule update --init --recursive
  git submodule status
  ```
- [ ] Performance: `time git status` and `time git log` (should be fast)

## Post-Conversion

- [ ] Update project README to document submodule initialization step
- [ ] Add submodule pull instructions to developer onboarding docs
- [ ] If applicable, add CI/CD step to initialize submodules during build: `git submodule update --init --recursive`
