# Bash - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\Bash`
**Generated:** 2026-07-10
**Stack:** Bun/TypeScript

## Directory Tree

```
Bash/
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── architecture.md
├── archive/
│   ├── artifacts/
│   │   ├── agents-pr-branches.json
│   │   ├── agents-pr-reconciliation.json
│   │   ├── agents_git_audit.json
│   │   ├── agentsmd-workflow-results-20260529.json
│   │   ├── context-maps/
│   │   │   ├── agents-fix.context.json
│   │   │   ├── bash-scripts-fix.context.json
│   │   │   ├── commands-fix.context.json
│   │   │   ├── dev-init.context.json
│   │   │   ├── general.context.json
│   │   │   ├── repo.context.json
│   │   │   └── skills-fix.context.json
│   │   ├── push_comicwise_fallback_20260529.ps1
│   │   ├── reconcile_agents_branches.ps1
│   │   ├── run_agentsmd_workflow_20260529.ps1
│   │   └── update_agentsmd_results_20260529.ps1
│   └── skills-commit-batches/
│       ├── README.md
│       └── retired/
│           ├── README.md
│           ├── skills-commit-batch-1.ps1
│           ├── skills-commit-batch-1.sh
│           ├── skills-commit-batch-10.ps1
│           ├── skills-commit-batch-10.sh
│           ├── skills-commit-batch-11.ps1
│           ├── skills-commit-batch-11.sh
│           ├── skills-commit-batch-12.ps1
│           ├── skills-commit-batch-12.sh
│           ├── skills-commit-batch-13.ps1
│           ├── skills-commit-batch-13.sh
│           ├── skills-commit-batch-14.ps1
│           ├── skills-commit-batch-14.sh
│           ├── skills-commit-batch-15.ps1
│           ├── skills-commit-batch-15.sh
│           ├── skills-commit-batch-16.ps1
│           ├── skills-commit-batch-16.sh
│           ├── skills-commit-batch-17.ps1
│           ├── skills-commit-batch-17.sh
│           ├── skills-commit-batch-18.ps1
│           ├── skills-commit-batch-18.sh
│           ├── skills-commit-batch-19.ps1
│           ├── skills-commit-batch-19.sh
│           ├── skills-commit-batch-2.ps1
│           ├── skills-commit-batch-2.sh
│           ├── skills-commit-batch-20.ps1
│           ├── skills-commit-batch-20.sh
│           ├── skills-commit-batch-21.ps1
│           ├── skills-commit-batch-21.sh
│           ├── skills-commit-batch-22.ps1
│           ├── skills-commit-batch-22.sh
│           ├── skills-commit-batch-23.ps1
│           ├── skills-commit-batch-23.sh
│           ├── skills-commit-batch-24.ps1
│           ├── skills-commit-batch-24.sh
│           ├── skills-commit-batch-25.ps1
│           ├── skills-commit-batch-25.sh
│           ├── skills-commit-batch-26.sh
│           ├── skills-commit-batch-3.ps1
│           ├── skills-commit-batch-3.sh
│           ├── skills-commit-batch-4.ps1
│           ├── skills-commit-batch-4.sh
│           ├── skills-commit-batch-5.ps1
│           ├── skills-commit-batch-5.sh
│           ├── skills-commit-batch-6.ps1
│           ├── skills-commit-batch-6.sh
│           ├── skills-commit-batch-7.ps1
│           ├── skills-commit-batch-7.sh
│           ├── skills-commit-batch-8.ps1
│           ├── skills-commit-batch-8.sh
│           ├── skills-commit-batch-9.ps1
│           └── skills-commit-batch-9.sh
├── Banking/
│   ├── install/
│   │   └── lib/
│   │       ├── 00-config.sh
│   │       ├── 01-utils.sh
│   │       ├── 02-paths.sh
│   │       ├── 03-deps.sh
│   │       ├── 04-registry.sh
│   │       ├── 05-selection.sh
│   │       ├── 06-modes.sh
│   │       ├── 07-preview.sh
│   │       └── 08-install.sh
│   ├── install-agents.sh
│   ├── install.sh
│   └── scripts/
│       ├── aggressive-capture.ps1
│       ├── branch-compare.sh
│       ├── delete-gone-branches.sh
│       ├── diagnose-and-fix-git.ps1
│       ├── diagnose-and-fix-git.sh
│       ├── opencode-mcp.bat
│       ├── opencode-mcp.ps1
│       ├── opencode-mcp.sh
│       ├── opencode-plugin-repair.bat
│       ├── opencode-plugin-repair.ps1
│       ├── opencode-plugin-repair.sh
│       ├── opencode-plugin-verify.bat
│       ├── opencode-plugin-verify.ps1
│       ├── opencode-plugin-verify.sh
│       ├── orchestrator.bat
│       ├── orchestrator.ps1
│       ├── orchestrator.sh
│       ├── plan-ensure.bat
│       ├── plan-ensure.ps1
│       ├── plan-ensure.sh
│       ├── run-verify-and-validate.ps1
│       ├── verify-agents.ps1
│       └── verify-agents.sh
├── bun.lock
├── bunfig.toml
├── cache-clean.bat
├── cache-clean.ps1
├── cache-clean.sh
├── clean-dependency-folders.bat
├── clean-dependency-folders.ps1
├── clean_dependency_folders.sh
├── CLEANUP-REPORT.md
├── comicwise/
│   ├── cleanup.ps1
│   ├── cleanup.sh
│   ├── dev.ps1
│   ├── dev.sh
│   ├── install-vscode-extensions.ps1
│   ├── install-vscode-extensions.sh
│   ├── quality-gate.ps1
│   ├── quality-gate.sh
│   ├── setup-dev.ps1
│   └── setup-dev.sh
├── copilot-instructions.md
├── create_skills.ps1
├── disk-analysis.ps1
├── docs/
│   ├── AGENTS.md
│   ├── ARCHITECTURE.md
│   ├── bash-scripts-safety-audit.md
│   ├── CODE_STYLE.md
│   ├── FINAL-SUMMARY.md
│   ├── MIGRATION-GUIDE.md
│   ├── phase5-verification-report.md
│   ├── Project_Architecture/
│   │   ├── exemplars.md
│   │   ├── Project_Architecture_Blueprint.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Technology_Stack_Blueprint.md
│   │   └── Workflow_Analysis.md
│   └── README.md
├── ecom/
│   └── install.sh
├── edits/
│   └── run-audit.sh.patch
├── eslint.config.mts
├── execute-real.sh
├── folder-structure.md
├── git-commit-batches.ps1
├── git-commit-batches.sh
├── lib/
│   ├── log-rotate.ps1
│   └── log-rotate.sh
├── migrations/
│   ├── banking/
│   │   ├── install/
│   │   │   └── lib/
│   │   │       ├── 00-config.sh
│   │   │       ├── 01-deps.sh
│   │   │       ├── 02-docker.sh
│   │   │       ├── 03-node.sh
│   │   │       ├── 04-python.sh
│   │   │       ├── 05-postgres.sh
│   │   │       ├── 06-redis.sh
│   │   │       ├── 07-mcp.sh
│   │   │       └── 08-install.sh
│   │   ├── install-agents.sh
│   │   ├── install.sh
│   │   └── scripts/
│   │       ├── aggressive-capture.ps1
│   │       ├── branch-compare.sh
│   │       ├── delete-gone-branches.sh
│   │       ├── diagnose-and-fix-git.ps1
│   │       ├── diagnose-and-fix-git.sh
│   │       ├── opencode-mcp.bat
│   │       ├── opencode-mcp.ps1
│   │       ├── opencode-mcp.sh
│   │       ├── opencode-plugin-repair.bat
│   │       ├── opencode-plugin-repair.ps1
│   │       ├── opencode-plugin-repair.sh
│   │       ├── opencode-plugin-verify.bat
│   │       ├── opencode-plugin-verify.ps1
│   │       ├── opencode-plugin-verify.sh
│   │       ├── orchestrator.bat
│   │       ├── orchestrator.ps1
│   │       ├── orchestrator.sh
│   │       ├── plan-ensure.bat
│   │       ├── plan-ensure.ps1
│   │       ├── plan-ensure.sh
│   │       ├── run-verify-and-validate.ps1
│   │       ├── verify-agents.ps1
│   │       └── verify-agents.sh
│   ├── comicwise/
│   │   ├── cleanup.ps1
│   │   ├── cleanup.sh
│   │   ├── dev.ps1
│   │   ├── dev.sh
│   │   ├── install-vscode-extensions.ps1
│   │   ├── install-vscode-extensions.sh
│   │   ├── quality-gate.ps1
│   │   ├── quality-gate.sh
│   │   ├── setup-dev.ps1
│   │   └── setup-dev.sh
│   ├── ecom/
│   │   └── install.sh
│   ├── rhixe_scans/
│   │   ├── docker-clean.sh
│   │   ├── git-setup.sh
│   │   ├── install_chrome.sh
│   │   ├── install_firefox.sh
│   │   ├── prod-dev.sh
│   │   ├── prod.sh
│   │   └── setup.sh
│   └── root/
│       ├── analyze-scripts.sh
│       └── sandbox-runtime-commands.ps1
├── OPERATIONS-GUIDE.md
├── ORCHESTRATOR-CHECKLIST.md
├── ORCHESTRATOR-DEBUG-FIXES.md
├── ORCHESTRATOR-DEBUG-SUMMARY.txt
├── ORCHESTRATOR-FILES.txt
├── ORCHESTRATOR-IMPLEMENTATION.md
├── ORCHESTRATOR-README.md
├── orchestrator-unified.bat
├── orchestrator-unified.ps1
├── orchestrator-unified.sh
├── ORCHESTRATOR_DEBUG_REPORT.md
├── package.json
├── PLAN.md
├── PROJECT-COMPLETE.md
├── QUICK-START.md
├── README-ORCHESTRATOR.md
├── README.md
├── REAL-WORLD-EXAMPLES.md
├── rhixe_scans/
│   ├── docker-clean.sh
│   ├── git-setup.sh
│   ├── install_chrome.sh
│   ├── install_firefox.sh
│   ├── prod-dev.sh
│   ├── prod.sh
│   └── setup.sh
├── root/
│   ├── analyze-scripts.sh
│   └── sandbox-runtime-commands.ps1
├── scripts/
│   ├── BATCH_LOGS/
│   │   ├── BATCH-001_log.json
│   │   ├── BATCH-002_log.json
│   │   └── BATCH-003_log.json
│   ├── BATCHES.json
│   ├── config/
│   │   ├── clone-config.json
│   │   ├── diagnostics-config.json
│   │   ├── discovery-config.json
│   │   ├── repo-inventory.json
│   │   └── triage-config.json
│   ├── CONSOLIDATED_PROPOSED_FIXES.md
│   ├── FINAL_AUDIT_SUMMARY.md
│   ├── lib/
│   │   ├── clone-utils.ps1
│   │   ├── core/
│   │   │   ├── config-loader.psm1
│   │   │   ├── dir-manager.psm1
│   │   │   ├── git-utils.psm1
│   │   │   ├── logger.psm1
│   │   │   └── path-utils.psm1
│   │   ├── data/
│   │   │   ├── batch-template.json
│   │   │   ├── catalog-template.md
│   │   │   ├── clone-template.json
│   │   │   ├── discovery-template.json
│   │   │   ├── report-schemas.json
│   │   │   └── triage-template.json
│   │   ├── dependency-scanner.ps1
│   │   ├── domain/
│   │   │   ├── batch-service.psm1
│   │   │   ├── clone-service.psm1
│   │   │   ├── discovery-service.psm1
│   │   │   ├── scanning-service.psm1
│   │   │   └── triage-service.psm1
│   │   ├── finding-parser.js
│   │   ├── git-operations.ps1
│   │   ├── github-mcp.ps1
│   │   ├── package-manager-scanners.ps1
│   │   ├── package-managers.ps1
│   │   ├── repo-analyzer.ps1
│   │   ├── repo-scanner.js
│   │   ├── triage-utils.ps1
│   │   └── validation.ps1
│   ├── orchestrator.ps1
│   ├── phase-1-deep-triage.ps1
│   ├── phase-1-deep-triage.sh
│   ├── phase-1-discovery.ps1
│   ├── phase-2-clone-local.ps1
│   ├── phase-2-clone.ps1
│   ├── phase-2-light-inventory.ps1
│   ├── phase-2-light-inventory.sh
│   ├── phase-3-consolidation.js
│   ├── phase-3-triage.ps1
│   ├── phase-4-batch-executor.js
│   ├── phase-4-debug.ps1
│   ├── phase-5-final-summary.js
│   ├── phase-5-remediation.ps1
│   ├── phase-5-verify-install.sh
│   ├── phase-6-cross-ref.ps1
│   ├── phase-6-cross-ref.sh
│   ├── README.md
│   ├── run-audit.sh
│   ├── score-docs.sh
│   ├── test-all-scanners.ps1
│   └── test-single-repo.ps1
├── SCRIPTS-INVENTORY.md
├── SPECS.md
├── src/
│   ├── cache-clean.ts
│   ├── clean-dep.ts
│   ├── core/
│   │   ├── ast-transformer.ts
│   │   ├── behavior-test.ts
│   │   ├── dry-run.ts
│   │   └── script-runner.ts
│   ├── git-commit-batches.ts
│   ├── lib/
│   │   ├── cli.ts
│   │   ├── colors.ts
│   │   ├── errors.ts
│   │   ├── logging.ts
│   │   └── README.md
│   ├── migration/
│   │   ├── __tests__/
│   │   │   └── ts-module-template.test.ts
│   │   ├── templates/
│   │   │   └── ts-module-template.ts
│   │   └── ts-morph-helper.ts
│   └── upgrade.ts
├── SUMMARY.md
├── tech-stack.md
├── test-all.sh
├── tests/
│   └── verify-dryrun.sh
├── TRIAGE-REPORT.txt
├── tsconfig.json
├── types.d.ts
├── upgrade-native.ps1
├── upgrade.bat
├── upgrade.ps1
├── upgrade.sh
├── USAGE-REPORT.md
└── verify_cleanup.ps1
```

## Key Directories

| Directory | Purpose | Convention |
|-----------|---------|------------|
| `src/` | TypeScript source | Feature-based |
| `scripts/` | Build/deploy scripts | kebab-case |

## Naming Conventions

- **Directories:** kebab-case (multi-word) or lowercase
- **Files:** Match language convention (PascalCase for React, snake_case for Python)
- **Configs:** lowercase with extension (.json, .yaml, .toml)

## File Placement Patterns

- Tests: co-located (`__tests__/`) or mirrored `tests/` structure
- Types: `types/` or co-located with implementation
- Config: Root level for tool configs

---
*Generated by agents-system-prompt-context-fix-runner*
