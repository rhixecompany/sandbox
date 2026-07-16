# projects/Bash — Folder Structure Blueprint

## Overview
- Namespace: `projects/Bash`
- Folder model: top-level components plus tooling/config directories.

## Directory Tree
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

## Placement Rules
- Keep code in the existing top-level component directories.
- Keep config files at the project root or `.vscode/`.
- Keep docs under `docs/` if the project already uses a docs folder.

## Naming Conventions
- Preserve the current folder naming style for this project.
- Do not normalize dots, hyphens, or underscores.

## Update Notes
- Refresh after any folder move, rename, or new top-level component.
