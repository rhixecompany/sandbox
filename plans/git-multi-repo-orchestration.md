---
status: completed
---

# 🎯 GIT MULTI-REPO ORCHESTRATION PLAN

**Created:** 2026-07-31 21:35 UTC
**Status:** Approved Plan — Ready for Implementation
**Target:** `./projects` — 18 git repos (parent SandBox + 13 submodules + standalone dirs)
**Skill:** `git-multi-repo-orchestration` (loads full git skill bundle)
**Prompt:** `.github/prompts/git-multi-repo-orchestration.prompt.md`

---

## 📌 PLAN OVERVIEW

Execute the complete git lifecycle across every repo in `./projects`:

1. **Commit & Push** — per-repo `git add` → `git commit` (conventional) → `git push origin development`
2. **Submodule Sync** — `git submodule foreach` + `update --remote` + parent pointer bump
3. **PR Lifecycle** — open/update/close PRs via `gh pr create` (review-then-merge)
4. **Branch Sync** — merge directly into `development` and push; sync `development` → `production`

### 5 Sequential Phases

| Phase                  | Duration | Risk   | Focus                                      |
| ---------------------- | -------- | ------ | ------------------------------------------ |
| **0. Inventory**       | 10 min   | Low    | Auth check, repo discovery, dirty baseline |
| **1. Commit & Push**   | 45 min   | Medium | Per-repo add/commit/push to development    |
| **2. Submodule Sync**  | 20 min   | Medium | Child pushes, pointer bump, parent commit  |
| **3. PR Lifecycle**    | 40 min   | Medium | gh pr create/edit/review/merge/close       |
| **4. Dev → Prod Sync** | 20 min   | High   | FF merge, approval-gated force-push        |
| **5. Verification**    | 10 min   | Low    | Dirty sweep, submodule clean, PR list      |

**Total:** ~2.5 hours (excluding user review gates)

---

## 🚀 KEY PRINCIPLES

- **Review-then-merge** — PRs are opened for review; merge only after review (never `--auto`).
- **Merge directly into `development`** — approved work lands on development and is pushed.
- **Production is downstream-only** — synced FROM development; FF preferred; force-push needs explicit approval.
- **Submodule ordering** — child repos push BEFORE parent pointer commit (prevents SHA drift).
- **Full audit trail** — conventional commits, `.copilot/session-state/` logs, PR descriptions.

---

## 📋 PHASE BREAKDOWN

### Phase 0: Inventory (10 min, Low Risk)

- Verify `gh auth status` (active account + `repo`, `workflow` scopes)
- `git submodule status` — record parent + submodule SHAs
- Discover git repos: `for d in projects/*/; do [ -d "$d/.git" ] && echo "${d#projects/}"; done`
- Record dirty baseline per repo (`git status --short | wc -l`)

### Phase 1: Per-Repo Commit & Push (45 min, Medium Risk)

- Loop each repo on `development`:
  1. `git status --short` — review changes
  2. `git add <files>` — stage (never blind `add -A` at root)
  3. `git commit -m "type(scope): subject"` — conventional types
  4. `git push origin development`
- Repos on feature branches: push branch + open PR (Phase 3), do NOT merge directly

### Phase 2: Submodule Sync (20 min, Medium Risk)

- `git submodule foreach 'git status --short && git fetch origin'`
- `git submodule update --remote development && git submodule sync`
- From SandBox root: `git add projects/*` → commit `chore(submodules): bump project pointers` → push

### Phase 3: PR Lifecycle — Review-Then-Merge (40 min, Medium Risk)

- **Open:** `gh pr create --base development --title "feat: ..." --body "<summary + test plan>"`
- **Update:** `gh pr edit <N> --title ... --body ...`; push commits to branch
- **Review:** `gh pr diff <N>`, `gh pr checks <N> --watch`, `--add-reviewer`
- **Merge after review:** `gh pr merge <N> --merge --delete-branch` (or `--squash`)
- **Close unmerged:** `gh pr close <N> --comment "<reason>"`
- **Gate:** NO auto-merge / admin-merge in review-then-merge flow

### Phase 4: Development → Production Sync (20 min, High Risk)

- Per repo: `git checkout production && git pull` → `git merge --ff-only development` → `git push origin production` → `git checkout development`
- **If FF fails:** STOP → request explicit user approval for force-push → log to `.copilot/session-state/PRODUCTION_FORCE_PUSH_LOG.md` (prior convention: 12/14 repos needed this once)
- Optional: tag release `git tag vX.Y.Z && git push origin vX.Y.Z`

### Phase 5: Verification (10 min, Low Risk)

- Per-repo sweep: current branch + dirty count
- `git submodule status | grep -v '^ '` → must be empty (all clean)
- `gh pr list --state open` → only expected PRs

---

## 🛡️ SAFETY GATES

| Gate            | Rule                                          |
| --------------- | --------------------------------------------- |
| Commit/push     | Only when user asked; approval per repo batch |
| Force-push      | Explicit user consent required; logged        |
| PR merge        | Review-then-merge only; no `--auto`           |
| Branch delete   | User approval required                        |
| Destructive ops | Approval file under `.hermes/approvals/`      |

## 🛡️ ROLLBACK

- **Commit mistake:** `git revert <sha>` (never rewrite pushed history)
- **Wrong merge:** revert merge commit, or `git reset --hard` to pre-merge SHA (local only)
- **Pointer drift:** re-run Phase 1 child pushes, re-bump parent
- **Force-push damage:** restore from GitHub reflog/reference SHA recorded before push

---

## ✅ SUCCESS CRITERIA

- [ ] All repos pushed to `development` with conventional commits
- [ ] Submodule pointers clean (`git submodule status` shows no `+`)
- [ ] PRs opened for review-then-merge (or merged after review)
- [ ] `production` in sync with `development` (FF or approved force-push)
- [ ] Final sweep: 0 unexpected dirty repos, expected open PRs only
- [ ] Audit trail complete

---

## 📊 TODOS & TRACKING

**Phase 0 (3):** verify-auth · discover-repos · baseline-dirty
**Phase 1 (2):** commit-push-each-repo · handle-feature-branches
**Phase 2 (3):** submodule-foreach · update-remote · parent-pointer-bump
**Phase 3 (4):** open-prs · update-prs · review-then-merge · close-unmerged
**Phase 4 (2):** ff-sync-dev-prod · force-push-gate (if needed)
**Phase 5 (2):** final-sweep · audit-trail

---

**Plan created:** 2026-07-31 21:35 UTC
**File location:** `plans/git-multi-repo-orchestration.md`
**Status:** Approved — implementation begins with Phase 0 (Inventory)
