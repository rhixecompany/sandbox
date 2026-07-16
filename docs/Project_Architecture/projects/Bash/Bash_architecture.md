# projects/Bash — Architecture Blueprint

## Overview
- Detected stack: Bun, TypeScript, ESLint, Prettier
- Architectural pattern: JavaScript/Bun application with feature-oriented source layout
- Top-level components: src, scripts, docs, tests, lib

## Component Map
- `src, scripts, docs, tests, lib`
- Shared config: `.vscode/` when present
- Docs: `docs/` when present

## Top-Level Structure
```text
Bash/
├── .husky/
│   └── _/
├── archive/
│   ├── artifacts/
│   └── skills-commit-batches/
├── Banking/
│   ├── install/
│   ├── install-agents.sh
│   └── install.sh
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
├── ecom/
│   └── install.sh
├── edits/
│   └── run-audit.sh.patch
├── lib/
│   ├── log-rotate.ps1
│   └── log-rotate.sh
├── migrations/
│   ├── banking/
│   ├── comicwise/
│   ├── ecom/
│   ├── rhixe_scans/
│   └── root/
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
├── src/
│   ├── core/
│   ├── lib/
│   ├── migration/
│   ├── cache-clean.ts
│   ├── clean-dep.ts
│   ├── git-commit-batches.ts
│   └── upgrade.ts
├── .lintstagedrc.ts
├── .markdownlintrc.json
├── .prettierrc.ts
├── AGENTS.md
├── architecture.md
├── AUDIT_Bash.md
├── bun.lock
├── bunfig.toml
├── cache-clean.bat
├── cache-clean.ps1
├── cache-clean.sh
├── clean-dependency-folders.bat
├── clean-dependency-folders.ps1
├── clean_dependency_folders.sh
├── CLEANUP-REPORT.md
├── copilot-instructions.md
├── create_skills.ps1
├── disk-analysis.ps1
├── eslint.config.mts
├── execute-real.sh
├── folder-structure.md
├── git-commit-batches.ps1
├── git-commit-batches.sh
├── OPERATIONS-GUIDE.md
├── ORCHESTRATOR-CHECKLIST.md
├── ORCHESTRATOR-DEBUG-FIXES.md
├── ORCHESTRATOR-DEBUG-SUMMARY.txt
├── ORCHESTRATOR-FILES.txt
├── ORCHESTRATOR-IMPLEMENTATION.md
```

## Cross-Cutting Concerns
- Configuration: environment and workspace configs live alongside the project.
- Testing: test locations should follow the existing project layout.
- Tooling: keep formatter/linter/editor settings in `.vscode/`.

## Extension Points
- Add new features within the existing top-level component that matches the current layout.
- Keep new dependencies aligned with the detected stack.

## Update Notes
- Regenerate when component boundaries, package dependencies, or folder structure change.
