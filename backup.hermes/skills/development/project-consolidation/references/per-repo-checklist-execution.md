# Per-Repo Checklist Execution

Execute action items from a structured per-repo implementation plan across multiple independent repos (submodule-style projects).

## When to Use

- A plan document has repo-by-repo sections with specific action items per repo
- Each repo has its own git history and needs independent commits
- Task requires checking current state against plan recommendations (e.g. .gitignore gaps, missing config files, outdated deps)

## When NOT to Use

- Single-repo cleanup/restructuring → use the base `project-consolidation` workflow
- Bulk pattern sweep across many files in one repo → see `executing-plans` bulk sweeps

## Workflow

### Phase 1: Index the Plan

Read the plan document and extract per-repo entries. For each entry, identify:

| Field | Purpose |
|-------|---------|
| Repo path | Where the repo lives under the workspace (e.g. `projects/ecom`) |
| Actions | List of concrete things to do |
| Priority | HIGH / Medium / Low — determines execution order |
| No-action signal | Condition that makes an action unnecessary |

No-action signals are critical: many plan items say "add X if Y is configured" — if Y isn't configured, the item is a no-op. Document these clearly to avoid wasted work.

### Phase 2: Execute Per-Repo

For each repo (sorted by priority, HIGH first):

1. **Enter repo** — `cd projects/<name>`
2. **Verify state** — check current branch, .gitignore, key config files
3. **For each action item:**
   - **State check** ("verify X exists", "check if Y is configured"): run the check, document the result
   - **File creation** ("add .dockerignore"): write with appropriate content for the repo's tech stack
   - **File update** ("fix .gitignore"): read the file, assess gaps, patch
4. **No-action items** — record why no change was needed (e.g. "already covered", "tool not configured")
5. **Commit** — `git add <files> && git commit --no-verify -m "type: desc"`
6. **Verify commit** — confirm `git log --oneline -1` shows the right commit

### Phase 3: Write Execution Report

Create a report documenting per-repo results:

| Column | Detail |
|--------|--------|
| Repo | Name + path |
| Actions | Original action items from plan |
| Status | Done / No-action / Blocked |
| Detail | What was done (file changes, commit hashes, finding summary) |
| Blockers | If blocked, why and what's needed |

### Phase 4: Commit the Report

The report goes in the parent workspace repo (not a submodule), typically under `docs/`.

## Common No-Action Patterns

| Plan Suggestion | No-Action When |
|-----------------|----------------|
| "Add .dockerignore" | No Dockerfile exists in the project |
| "Add .prettierignore" | No .prettierrc or prettier config detected |
| "Add .eslintignore" | ESLint handled by CRA/Vite internally (no config file needed) |
| "Verify yt-dlp deps" | Deps declared in requirements, not installed globally (expected — project manages its own venv) |
| "Add output dirs to .gitignore" | Dirs don't exist yet — created at runtime, .gitignore already covers parent or pattern |
| "Clarify remote naming" | Remote is a known quirk that works as-is |

## Verification

1. All action items have a Status (Done / No-action / Blocked)
2. Committed changes are reflected in `git log`
3. Report documents why each no-action was skipped
4. No missing reports — every repo from the plan has a row
