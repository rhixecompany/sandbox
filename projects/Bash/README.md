# Bash — Automation Toolkit

> **Stack:** Bun / TypeScript | **Type:** Automation Toolkit | **Status:** Active

A comprehensive automation toolkit for the SandBox workspace, providing TypeScript-based utility scripts for cache cleaning, dependency management, git operations, cross-referencing, and multi-phase project orchestration.

---

## Technology Stack

| Category | Technology |
|---|---|
| **Runtime** | Bun >=1.3.14, Node.js >=18 |
| **Language** | TypeScript (strict), PowerShell 5.1+, Bash |
| **Linting** | ESLint 10.x, Prettier 3.x, Markdownlint, CSpell |
| **Type Check** | TypeScript (`tsc --noEmit`) |
| **Testing** | Vitest, shell tests (`verify-dryrun.sh`) |
| **Git Hooks** | Husky 9.x, lint-staged |
| **CI/CD** | GitHub Actions |

## Architecture

The toolkit follows a **Phase-Based Orchestration Pattern** with a multi-phase pipeline:

1. **Phase 1 — Discovery**: Inventory repositories and dependencies
2. **Phase 2 — Clone**: Clone repositories locally
3. **Phase 3 — Triage**: Analyze and categorize issues
4. **Phase 4 — Debug**: Deep debugging of identified issues
5. **Phase 5 — Remediation**: Apply fixes and remediations
6. **Phase 6 — Cross-Reference**: Cross-reference across repos

### Multi-Platform Wrapper Pattern

Every tool has wrapper parity across platforms:
- `.ps1` — PowerShell (Windows)
- `.sh` — Shell (Linux/Mac)
- `.bat` — Batch (Windows fallback)

```
User Invocation → bun run → TypeScript Script
                              ↓
                       PowerShell Orchestrator
                              ↓
                   ┌──────────┼──────────┐
                   ↓          ↓          ↓
            Phase Scripts  Lib Modules  Utilities
                   ↓          ↓          ↓
             Reports & Outputs / Logs
```

## Project Structure

```
Bash/
├── src/                     # TypeScript source scripts
│   ├── cache-clean.ts       # Cache cleaning
│   ├── clean-dep.ts         # Dependency cleaning
│   ├── git-commit-batches.ts# Batch git commits
│   ├── upgrade.ts           # Upgrade utilities
│   └── core/                # Core libraries
├── scripts/                 # PowerShell orchestration
│   ├── lib/                 # PowerShell library modules
│   ├── phase-1-discovery.ps1
│   ├── phase-2-clone.ps1
│   ├── phase-3-triage.ps1
│   ├── phase-4-debug.ps1
│   ├── phase-5-remediation.ps1
│   └── phase-6-cross-ref.ps1
├── tests/                   # Test files
│   └── verify-dryrun.sh
├── migrations/              # Per-project migrations
└── docs/Project_Architecture/
```

## Getting Started

```bash
# Install dependencies
bun install --frozen-lockfile

# Run available scripts
bun run format        # Prettier formatting
bun run typecheck     # TypeScript type checking
bun run lint:strict   # ESLint with zero warnings policy

# Run tests
bash tests/verify-dryrun.sh && bash test-all.sh

# PowerShell orchestrator
powershell -File orchestrator-unified.ps1 -Mode discover
```

## Key Features

- **Cache Cleaning** — Clear cache files with `--dry-run` support
- **Dependency Management** — Clean and upgrade dependencies
- **Git Operations** — Batch git commits and repository management
- **Cross-Reference** — Validate and cross-reference across repositories
- **Multi-Platform** — Full `.sh` / `.ps1` / `.bat` wrapper parity
- **Dry-Run Support** — All destructive operations support `--dry-run`

## Development Workflow

```bash
bun install --frozen-lockfile || bun install
bun run format && bun run typecheck && bun run lint:strict
bash tests/verify-dryrun.sh && bash test-all.sh
```

## Coding Standards

- **TypeScript strict mode**: Full strict type checking
- **ES Modules**: `"type": "module"` in package.json
- **Wrapper parity**: Maintain `.sh`, `.ps1`, `.bat` equivalents
- **`--help`/`--dry-run`**: All scripts support help and dry-run flags
- **Logging**: Logs to `logs/` directory with timestamps
- **Prettier + ESLint**: Dual formatting/linting pipeline

## Testing

- **Vitest**: TypeScript unit testing
- **Shell tests**: `tests/verify-dryrun.sh` for dry-run verification
- **CI tests**: Automated via GitHub Actions

## Contributing

Refer to [AGENTS.md](./AGENTS.md) and `copilot-instructions.md` for detailed development guidelines.

## License

ISC (inherited from root `package.json`)
