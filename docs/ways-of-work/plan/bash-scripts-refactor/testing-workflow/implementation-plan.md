Implementation Plan: Bash Scripts Testing, Debugging, and Fixing Workflow

Overview

Goal

- Provide a reproducible, low-risk workflow to test, debug, and fix every script under ./Bash.
- Make all orchestrator scripts thin and move logic to TypeScript where appropriate (per repo conventions).

Scope

- All files under ./Bash including: .sh, .ps1, .bat, .ts, .js, and library modules under ./Bash/scripts/lib and ./Bash/src.
- Produce: automated test harness, linting and formatting rules, dry-run safety adoption pattern, CI job, and developer debugging playbook.

Out of scope

- Global infra changes (CI runners, host OS installs) beyond CI job definitions.

Constraints & Safety

- Do not run destructive actions by default; adopt a DRY_RUN_SUPPORT marker and --dry-run flag for each script.
- All edits must pass local linters and tests before commit.

Deliverables

- Implementation plan (this document)
- A dry-run verification script: Bash/tests/verify-dryrun.sh (created alongside this plan)
- CI job: .github/workflows/bash-scripts-ci.yml (spec included in this doc)
- Migration checklist & triage report template

High-level Workflow

1. Discovery (automated)

- Run scripts/phase-1-discovery.ps1 or ./Bash/scripts/run-audit.sh to enumerate scripts and their languages.
- Produce docs/bash-scripts-list-context.md (inventory) — already produced by prior audit.

1. Add dry-run support

- For each script that performs side effects, add one of:
    - A --dry-run CLI flag that performs no writes and logs intended actions
    - A DRY_RUN_SUPPORT=true file-header marker (single-line) that signals test harness support
- Prefer TypeScript migration for non-trivial logic; keep orchestrators as thin sh/ps1 wrappers.

1. Linting & Formatting

- Shell: shfmt (format), shellcheck (lint)
- PowerShell: PSScriptAnalyzer (lint)
- Batch: minimal static checks (token patterns), prefer conversion to PowerShell
- TypeScript/JS: ESLint + ts-morph for AST-safe transforms

1. Automated Tests (local & CI)

- Create a verification test that scans the repository for DRY_RUN_SUPPORT markers and runs supported scripts with --dry-run. (Bash/tests/verify-dryrun.sh)
- Unit tests for TypeScript modules (vitest/jest) to be added next to each migrated module.
- Integration tests: isolated Docker/WSL runner that executes end-to-end flows with test fixtures.

1. Debugging Playbook

- Reproduce locally in an isolated environment (Docker image or WSL distro matching CI runner).
- Run: set -x; export LOG_LEVEL=debug; ./Bash/tests/verify-dryrun.sh to capture failures.
- Use verbose logging, or run scripts under strace / pwsh -NoProfile -Command Trace-Command for deep inspection only when safe.

1. Fix, Review, Merge

- TDD approach: write failing unit/integration test first (the verify-dryrun harness qualifies) then implement fix.
- Create a single-purpose branch per consolidated change (eg: refactor/ts-migrate-clone-utils).
- Open PR with descriptive changelog and link to docs/bash-scripts-implementation-plan.md and FINAL_AUDIT_SUMMARY.md.
- PR checklist: format -> lint -> tests pass -> migrates dry-run marker present -> min 1 reviewer.

Tooling & Patterns

Dry-run adoption pattern (recommended header)

- Add the following single-line marker at the top of each script that supports dry-run testing:

    # DRY_RUN_SUPPORT=true

- Implement --dry-run flag that toggles the script into a no-op mode but prints planned actions.
- For TypeScript modules, export a dryRun boolean parameter and unit-test behavior.

Logging

- Standardize on structured logs (JSON lines) for scripts that produce machine-readable output.
- WRITE: ./Bash/logs/<script-name>-<timestamp>.log
- During tests, capture logs to Bash/logs/test-run-<timestamp>.log and attach to CI artifacts.

Testing matrix (local & CI)

- Linters: shellcheck, shfmt, PSScriptAnalyzer, eslint
- Unit tests: ts modules via vitest (node16+ / bun if present)
- Integration: run verify-dryrun.sh on linux runner; run PowerShell verify on windows runner (optional)
- Security: run package-manager-scanners.ps1 in dry-run mode to assert no harmful network calls occur

CI Job (GitHub Actions) - spec

- Name: bash-scripts-ci.yml
- Triggers: pull_request on paths: 'Bash/\*\*'
- Runs-on: ubuntu-latest (matrix for windows-latest when verifying .ps1)
- Steps:
    1. Checkout
    2. Setup Node/Bun toolchain
    3. Install dev dependencies (bun install || npm ci)
    4. Run formatters (shfmt checking mode), ESLint, PSScriptAnalyzer via PowerShell Core
    5. Run Bash/tests/verify-dryrun.sh (capture artifacts)
    6. Run unit tests for TypeScript modules

Debugging & Reproduction Steps (developer)

- Step 1: Run discovery to update inventory
  ./Bash/scripts/phase-1-discovery.ps1 (or ./Bash/scripts/phase-1-discovery.sh)
- Step 2: Run dry-run verification locally
  bash ./Bash/tests/verify-dryrun.sh | tee ./Bash/logs/test-run-$(date +%Y%m%dT%H%M%S).log
- Step 3: If a script fails, open it and check for:
    - Missing DRY_RUN_SUPPORT marker
    - Lack of --dry-run handling
    - Uncaught set -e causing premature exit
    - Missing dependency PATH assumptions
- Step 4: Add a unit test for migrated TypeScript logic
- Step 5: Re-run verify-dryrun until green

Verification

Minimal verification steps (manual)

- Run the verify script locally:
  bash ./Bash/tests/verify-dryrun.sh
- Run linters and unit tests:
  bun run format && bun run lint:strict && bun run test

Failing test requirement

- As part of landing the workflow we add a verification harness that initially fails until scripts adopt DRY_RUN_SUPPORT. This harness is the canonical failing test used to drive fixes.
- File: Bash/tests/verify-dryrun.sh (created alongside this plan).

Migration plan & timeline (suggested)

- Week 0: Inventory & triage (discovery outputs)
- Week 1: Add DRY_RUN_SUPPORT markers to top priority scripts and create test harness
- Week 2-4: Migrate heavy logic to TypeScript modules with unit tests (ts-morph for AST work)
- Week 5: Consolidate orchestrators, update package.json, and CI
- Week 6: Finish validation, documentation, and close audit

Risks & Mitigations

- Risk: Scripts that perform destructive actions without dry-run may be run accidentally in CI
  Mitigation: CI runs verification only; do not enable production-run CI steps until dry-run markers present.
- Risk: PowerShell scripts depend on Windows-only features
  Mitigation: Use matrix runners and prefer pwsh Core compatibility; convert to cross-platform TypeScript where possible.

Next Steps (actionable)

1. Commit this implementation plan at docs/ways-of-work/plan/bash-scripts-refactor/testing-workflow/implementation-plan.md
2. Add the verification harness Bash/tests/verify-dryrun.sh (created in repo root)
3. Run discovery and update docs/bash-scripts-list-context.md if needed
4. Triage scripts: pick 5 highest-impact scripts, add DRY_RUN_SUPPORT marker and tests
5. Create a short-lived branch and land PRs using TDD (failing harness first)

Contacts

- Owner: Alexa (assumed), Technical lead: Senior Script Architect

References

- Prompts/bash-scripts-fix.prompts.md (project audit & refactor rules)
- Bash/AGENTS.md (subagent routing & analysis rules)
  json, and CI
- Week 6: Finish validation, documentation, and close audit

Risks & Mitigations

- Risk: Scripts that perform destructive actions without dry-run may be run accidentally in CI
  Mitigation: CI runs verification only; do not enable production-run CI steps until dry-run markers present.
- Risk: PowerShell scripts depend on Windows-only features
  Mitigation: Use matrix runners and prefer pwsh Core compatibility; convert to cross-platform TypeScript where possible.

Next Steps (actionable)

1. Commit this implementation plan at docs/ways-of-work/plan/bash-scripts-refactor/testing-workflow/implementation-plan.md
2. Add the verification harness Bash/tests/verify-dryrun.sh (created in repo root)
3. Run discovery and update docs/bash-scripts-list-context.md if needed
4. Triage scripts: pick 5 highest-impact scripts, add DRY_RUN_SUPPORT marker and tests
5. Create a short-lived branch and land PRs using TDD (failing harness first)

Contacts

- Owner: Alexa (assumed), Technical lead: Senior Script Architect

References

- Bash/AGENTS.md (subagent routing & analysis rules)
