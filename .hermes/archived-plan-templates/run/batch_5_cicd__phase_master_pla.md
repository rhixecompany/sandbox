# Batch 5: CI/CD + Phase Master Plan

> Extracted from `run.prompt.md`.

## Batch 5: CI/CD + Phase Master Plan

**Goal**: Modernize CI/CD workflows, create comprehensive phase task document.

### Part A: CI/CD Workflow Modernization (Implementer)

**test.yml**:

- Node 18→20, pnpm v8→latest via `pnpm/action-setup@v3`
- `actions/cache@v3`→v4, `upload-artifact@v3`→v4, `codecov@v3`→v4
- Add quality gate artifact uploads + triage step

**playwright.yml**:

- Replace `npm install -g pnpm` with `pnpm/action-setup@v3`
- Add pnpm cache, pin Node 20

**deploy.yml**:

- Docker actions: buildx@v2→v3, login@v2→v3, metadata@v4→v5, build-push@v4→v5
- `github-script@v6`→v7, remove non-existent `notify-deployment.yml` reference

**copilot-setup-steps.yml**:

- `checkout@v5`→v4 (v5 doesn't exist)

**All**: Add `.references/` to `paths-ignore`, standardize Node 20 + pnpm latest.

### Part B: Phase Task Master Plan (Architect)

Create `docs/PHASE-MASTER-PLAN.md`:

1. Inventory all phases (1→4.5+) with micro-tasks and status
2. Completed phases: summary + links to completion reports
3. Pending phases: detailed tasks with ID, files, dependencies, complexity
4. Checkpoints: specific `pnpm` commands after each sub-phase
5. Recovery points: `git stash`, `git checkout .`, migration rollback
6. Code samples with diff for key changes
7. Dependency graph between tasks

### Batch 5 Verification

```
All 4 workflow files are valid YAML
No v5 for checkout, no v2 for docker actions
docs/PHASE-MASTER-PLAN.md exists with all phases
Final: pnpm type-check && pnpm lint:fix && pnpm test && pnpm build → ALL PASS
```

---
