# Workspace Cleanup Manifest

Date: 2026-05-30 Scope: initial implementation wave Mode: archive + migrate +
dedupe + targeted reference updates

## Canonical Anchors Preserved

- reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
- AGENTS.md references to the canonical inventory report were left intact.
- .github/copilot-instructions.md references to the canonical inventory report
  were left intact.

## New Centralized Folders Created

- artifacts/archive/cleanup-2026-05-30
- reports/inventory
- reports/migrations/bash-scripts-fix
- reports/migrations/skills-fix
- docs/archive/legacy-reports

## Files Migrated

### Root -> reports/migrations/bash-scripts-fix

- BASH_SCRIPTS_FIX_COMPLETION_CERTIFICATE.md
- BASH_SCRIPTS_FIX_DELIVERABLES_MANIFEST.txt
- BASH_SCRIPTS_FIX_FINAL_SUMMARY.md
- BASH_SCRIPTS_FIX_IMPLEMENTATION_VERIFIED.md
- BASH_SCRIPTS_FIX_INDEX.txt
- BASH_SCRIPTS_FIX_PHASE3_CODE_REVIEW_REPORT.md
- BASH_SCRIPTS_FIX_PHASE4_EXECUTION_REPORT.md
- BASH_SCRIPTS_FIX_PHASE4_MIGRATION_LOG.md
- BASH_SCRIPTS_FIX_PHASE4_REPORT.md
- BASH_SCRIPTS_FIX_PHASE5_EXECUTION_REPORT.md
- BASH_SCRIPTS_FIX_PHASE5_REAL_EXECUTION_REPORT.md
- BASH_SCRIPTS_FIX_PHASE5_TESTING_REPORT.md
- BASH_SCRIPTS_FIX_PHASE6_CLEANUP_REPORT.md
- BASH_SCRIPTS_FIX_PHASE6_EXECUTION_REPORT.md
- BASH_SCRIPTS_FIX_PHASE6_REAL_CLEANUP_REPORT.md
- BASH_SCRIPTS_FIX_PHASES_3_6_READINESS.md
- BASH_SCRIPTS_FIX_PROJECT_SUMMARY.md
- BASH_SCRIPTS_MIGRATION_COMPLETION_CERT.md

### Root -> reports/migrations/skills-fix

- SKILLS_FIX_COMPLETION_CERT.md
- SKILLS_FIX_INDEX.txt
- SKILLS_FIX_PHASE_1_3_REPORT.md
- SKILLS_FIX_PHASE_3_EXECUTION_REPORT.md

### reports -> reports/inventory

- reports/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md
- reports/copilot-cli-vscode-copilot-chat-priority-categories-20260530.md
- reports/copilot-inventory-summary-2026-05-30.md

## Dedupe Actions

- Archived and deleted duplicate inventory report:
  - removed: reports/skills-agents-hooks-plugins-prompts-instructions-report.md
  - canonical kept:
    reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md

## Archived Snapshots

All files migrated/deleted above were snapshotted to:

- artifacts/archive/cleanup-2026-05-30

## Reference Updates Applied

- docs/workspace-consolidation-summary.md
  - updated phase final reports location to
    reports/migrations/bash-scripts-fix/BASH*SCRIPTS_FIX*\*
- docs/skills-debug-final-report.md
  - updated certification certificate path to
    reports/migrations/skills-fix/SKILLS_FIX_COMPLETION_CERT.md
- reports/inventory/copilot-cli-vscode-copilot-chat-priority-categories-20260530.md
  - updated internal link to
    reports/inventory/copilot-cli-vscode-copilot-chat-inventory-summary-20260530.md

## Verification Results (post-wave)

- Root cluster files no longer exist at workspace root.
- reports now contains only:
  - copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
  - inventory/
  - migrations/
  - cleanup-2026-05-30-manifest.md
- Stale-reference scan for BASH*SCRIPTS_FIX*,
  BASH*SCRIPTS_MIGRATION_COMPLETION_CERT, SKILLS_FIX* outside archive/migration
  folders shows only intentional updated mentions in docs.

## Wave 2: Index Consolidation And Report Dedupe

### Docs Index Family Consolidated

- `docs/INDEX.md` promoted to canonical documentation hub.
- `docs/HERMES_DOCUMENTATION_INDEX.md` converted to compatibility landing page.
- `docs/CONTEXT-MAP-WORKFLOW-INDEX.md` converted to compatibility landing page.
- `docs/dev-init-index.md` converted to compatibility landing page.
- Pre-consolidation versions archived under:
  - `docs/archive/legacy-reports/index-family/`
  - `artifacts/archive/cleanup-2026-05-30/index-family/`

### Project Report Dedupe

- Archived and deleted obsolete report variant:
  - removed: `projects/comicwise/docs/TRIAGE_REPORT.md`
  - canonical kept: `projects/comicwise/docs/triage-report.md`
- Updated `projects/comicwise/docs/QUALITY_GATE_FIX_REPORT.md` to reference the
  canonical lowercase report path.

### Broader Sweep Outcome

- Exact duplicate scanning across `docs/` and `projects/` identified many vendor
  licenses, static asset readmes, font notices, and generated project changelog
  placeholders.
- Those files were intentionally not auto-deleted in this wave because they are
  embedded in project-local vendor or static trees and require project-scoped
  ownership review.

### Final Reports Produced

- `reports/post-cleanup-summary-2026-05-30.md`
- `reports/manual-review-queue-2026-05-30.md`

## Remaining Implementation Work

- Remaining work is now limited to the manual-review items listed in
  `reports/manual-review-queue-2026-05-30.md`.
