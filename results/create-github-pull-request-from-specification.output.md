# Dry-Run: create-github-pull-request-from-specification

**Date:** 2026-07-09  
**Source prompt:** `prompts/create-github-pull-request-from-specification.prompt.md`  
**Mode:** DRY-RUN — no live GitHub API calls were made.

---

## Phase 1 — Intake

**Specification file:** Not explicitly named in workspace. Searched for `pull_request_template.md`, `*.spec.md`, and `*.spec.*` — none found.

**Template looked up:** `${workspaceFolder}/.github/pull_request_template.md` — **not present** (`.github/` directory exists but contains only agent definitions and skill hub caches).

**Git state:** Branch `development` — 50+ changed files (staged + unstaged, including deletions). This would be the PR source branch.

---

## Phase 2 — Execution (Dry-Run)

The prompt prescribes this sequence (all skipped):

| Step | Action | Status |
|------|--------|--------|
| 1 | Analyze `pull_request_template.md` via `search` tool | ❌ Skipped — file missing |
| 2 | Create draft PR with `create_pull_request` tool on `targetBranch` | ❌ Skipped — no spec, no template, no target branch provided |
| 3 | Get diff with `get_pull_request_diff` | ❌ Skipped |
| 4 | Update PR body/title with `update_pull_request` | ❌ Skipped |
| 5 | Switch PR from draft → ready with `update_pull_request(state=ready)` | ❌ Skipped |
| 6 | Assign PR creator via `get_me` → `update_issue` | ❌ Skipped |
| 7 | Return PR URL | ❌ Skipped |

---

## Phase 3 — Verification

**Inputs required but missing:**
- Specification file path or content (the `input` the prompt is meant to act on)
- `${input:targetBranch}` — no target branch provided
- `.github/pull_request_template.md` — template not present in workspace

---

## Phase 4 — Hand-off

### What would happen with real inputs
1. A spec file (e.g., a `.spec.md` or specification prompt output) would be read.
2. The PR template at `.github/pull_request_template.md` would supply structured fields (title, description, changes, testing notes).
3. `get_pull_request` would check for existing PRs on the current branch (`development`).
4. A new draft PR would be created, its body filled from the template + spec content.
5. The diff would be fetched to enrich the PR with change analysis.
6. The PR would be marked ready-for-review.
7. The creator would be assigned via `update_issue`.

**To unblock real execution, provide:**
- A specification `.md` file (or the spec content inline)
- The target branch name (e.g. `main`, `production`)
- Optionally, create `.github/pull_request_template.md` with the desired PR format