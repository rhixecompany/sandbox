# Project Folder Structure Blueprint

## Project: Bash — Bun/TypeScript Automation Toolkit

**Generated:** 2026-06-25  
**Project Type:** Bun/TypeScript CLI Automation Toolkit  
**Auto-detected:** Yes (Bun/TypeScript project — `bun.lock`, `tsconfig.json`, `package.json`, `.lintstagedrc.ts`, `eslint.config.mts`)

---

## Directory Tree

```
Bash/
├── .gitignore
├── .husky/                  # Git hooks (husky)
├── .lintstagedrc.ts
├── .markdownlintrc.json
├── .prettierrc.ts
├── .vscode/
├── AGENTS.md
├── Banking/                 # Banking project resources
│   ├── install/
│   │   └── lib/
│   └── scripts/
├── archive/
│   ├── artifacts/
│   │   └── context-maps/
│   └── skills-commit-batches/
│       └── retired/
├── bun.lock
├── bunfig.toml
├── cache-clean.bat / .ps1 / .sh
├── clean-dependency-folders.bat / .ps1 / .sh
├── comicwise/
├── create_skills.ps1
├── disk-analysis.ps1
├── docs/
│   └── Project_Architecture/
├── ecom/
├── edits/
├── eslint.config.mts
├── execute-real.sh
├── git-commit-batches.ps1 / .sh
├── lib/
│   ├── log-rotate.ps1
│   └── log-rotate.sh
├── migrations/
│   ├── banking/
│   ├── comicwise/
│   ├── ecom/
│   ├── rhixe_scans/
│   └── root/
├── orchestrator-unified.bat / .ps1 / .sh
├── package.json
├── rhixe_scans/
├── root/
├── scripts/
│   ├── BATCHES.json
│   ├── BATCH_LOGS/
│   ├── CONSOLIDATED_PROPOSED_FIXES.md
│   ├── config/
│   ├── lib/
│   │   ├── core/
│   │   ├── data/
│   │   └── domain/
│   ├── orchestrator.ps1
│   ├── *.ps1 / *.sh
│   └── *.js
├── src/
│   ├── cache-clean.ts
│   ├── clean-dep.ts
│   ├── core/
│   ├── git-commit-batches.ts
│   ├── lib/
│   ├── migration/
│   │   ├── __tests__/
│   │   └── templates/
│   └── upgrade.ts
├── tests/
│   └── verify-dryrun.sh
├── tsconfig.json
├── types.d.ts
├── upgrade.bat / .ps1 / .sh
└── upgrade-native.ps1
```

---

## Naming Conventions

| Convention | Pattern | Examples |
|---|---|---|
| **Directories** | kebab-case / lowercase | `scripts/`, `src/core/`, `archive/artifacts/` |
| **TypeScript files** | kebab-case.ts | `cache-clean.ts`, `git-commit-batches.ts` |
| **Shell scripts** | kebab-case.sh | `execute-real.sh`, `clean_dependency_folders.sh` |
| **PowerShell scripts** | kebab-case.ps1 | `disk-analysis.ps1`, `upgrade-native.ps1` |
| **Batch files** | kebab-case.bat | `cache-clean.bat`, `upgrade.bat` |
| **Config** | dotted-prefix | `.lintstagedrc.ts`, `.prettierrc.ts` |

---

## File Placement Patterns

- **Source code**: `src/` directory with `core/`, `lib/`, `migration/` subdirectories
- **Shell scripts (cross-platform)**: Root level `.bat`, `.ps1`, `.sh` variants
- **Migration scripts**: `migrations/<project-name>/`
- **Orchestration scripts**: `scripts/` with multi-phase pipeline scripts
- **Project-specific resources**: `Banking/`, `comicwise/`, `ecom/`, etc.
- **Tests**: `src/migration/__tests__/` and `tests/`
- **Documents**: `docs/`

---

## Project Type Indicators

| Indicator | Value |
|---|---|
| Has `package.json` | ✅ Node.js / Bun project |
| Has `bun.lock` | ✅ Uses Bun package manager |
| Has `tsconfig.json` | ✅ TypeScript |
| Has `eslint.config.mts` | ✅ ESLint flat config |
| Has `.husky/` | ✅ Git hooks via Husky |
| Cross-platform scripts | ✅ Supports bat/ps1/sh |
| Multi-project migration scripts | ✅ Targets multiple sub-projects |

---

## Key Architecture Decisions

1. **Hybrid cross-platform support** — Every script exists in `.bat` (cmd), `.ps1` (PowerShell), and `.sh` (bash) variants.
2. **TypeScript source** with Bun runtime — Modern JS tooling for automation.
3. **Orchestrator pattern** — Multi-phase pipeline scripts in `scripts/` handle discovery, triage, consolidation, execution, and verification.
4. **Per-project migrations** — Each sub-project gets its own migration directory.
5. **Heavy archive** — `archive/` contains historical artifacts and context maps from prior automation runs.
