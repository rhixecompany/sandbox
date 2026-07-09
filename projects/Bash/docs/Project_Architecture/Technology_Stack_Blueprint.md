# Technology Stack Blueprint

## Project: Bash — Automation Toolkit

> **Generated:** 2026-06-25  
> **Generator:** technology-stack-blueprint-generator  
> **Analysis Depth:** Comprehensive

---

## Overview

The Bash module is the primary automation toolkit for the SandBox workspace. It provides TypeScript-based utility scripts for cache cleaning, dependency management, git operations, cross-referencing, and orchestration.

**Project Type:** Bun/TypeScript Automation Toolkit  
**Stack Type:** Bun/TypeScript

---

## Technology Stack

### Languages & Runtimes

| Technology | Version | Usage |
|---|---|---|
| TypeScript | latest (via Bun) | Primary scripting language |
| Bun | >=1.3.14 | JavaScript/TypeScript runtime & package manager |
| Node.js | >=18 | Fallback runtime |
| Bash | — | Shell scripts (cross-platform wrappers) |
| PowerShell | 5.1+ | Windows orchestration |

### Package Manager

| Tool | Version |
|---|---|
| bun | 1.3.14 |

### Core Dependencies

| Dependency | Version | Purpose |
|---|---|---|
| yaml | ^2.9.0 | YAML parsing |
| zod | ^4.4.3 | Schema validation |

### Development Dependencies

| Dependency | Version | Purpose |
|---|---|---|
| typescript | latest | Type checking |
| eslint | ^10.4.0 | Linting framework |
| @typescript-eslint/parser | ^8.59.4 | TypeScript ESLint parser |
| typescript-eslint | ^8.59.4 | TypeScript ESLint config |
| prettier | ^3.8.3 | Code formatting |
| husky | ^9.1.7 | Git hooks |
| lint-staged | ^16.4.0 | Staged file linting |
| cspell | ^10.0.0 | Spell checking |
| markdownlint-cli2 | ^0.22.1 | Markdown linting |
| tsx | ^4.22.3 | TypeScript execution |
| vitest | ^4.1.7 | Testing framework |
| jsdom | ^29.1.1 | DOM environment for tests |
| rimraf | ^6.1.3 | File cleanup |

---

## Scripts & Utilities

| Script | Description |
|---|---|
| `clean:cache` | Clear cache files (with `--dry-run` support) |
| `clean:deps` | Clean dependencies (with `--dry-run` support) |
| `commit:batches` | Batch git commits |
| `cross-ref` | Cross-reference validation |
| `upgrade` | Dependency upgrade tool |
| `format` | Prettier formatting |
| `typecheck` | TypeScript type checking |
| `lint:strict` | ESLint with zero warnings policy |

---

## Licensing

| Component | License |
|---|---|
| Bash toolkit | ISC (inherited from root `package.json`) |

---

## Coding Conventions

- **TypeScript strict mode**: Full strict type checking enabled
- **ES Modules**: `"type": "module"` in package.json
- **Wrapper parity**: Maintain `.sh`, `.ps1`, `.bat` equivalents
- **`--help`/`--dry-run`**: All scripts support help and dry-run flags
- **Logging**: Logs to `logs/` directory with timestamps
- **Prettier + ESLint**: Dual formatting/linting pipeline

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│              Bash Automation Toolkit                  │
├─────────────────────────────────────────────────────┤
│  src/                                                │
│  ├── cache-clean.ts          Cache management        │
│  ├── clean-dep.ts           Dependency cleanup       │
│  ├── git-commit-batches.ts  Git batch operations     │
│  ├── upgrade.ts             Dependency upgrades      │
│  └── ... (utility scripts)                           │
├─────────────────────────────────────────────────────┤
│  scripts/                                            │
│  ├── phase-5-verify-install.sh                       │
│  ├── phase-6-cross-ref.sh                            │
│  └── phase-6-cross-ref.ps1                           │
├─────────────────────────────────────────────────────┤
│  tests/                                              │
│  ├── verify-dryrun.sh                                │
│  └── test-all.sh                                     │
├─────────────────────────────────────────────────────┤
│  Configuration: .prettierrc.ts, eslint.config.mts    │
│  CI: .github/workflows/bash-scripts-ci.yml           │
└─────────────────────────────────────────────────────┘
```

---

## Usage Patterns

- All commands run via `bun run <script>` or `bunx tsx <file>`
- Dry-run mode available for destructive operations
- Cross-platform via `.sh`/`.ps1`/`.bat` wrappers
- Orchestrator entry: `powershell -File orchestrator-unified.ps1 -Mode discover`

---

## CI/CD

| Pipeline | File | Trigger |
|---|---|---|
| Bash Scripts CI | `.github/workflows/bash-scripts-ci.yml` | Push/PR |
| Copilot Setup | `.github/workflows/copilot-setup-steps.yml` | Setup |
