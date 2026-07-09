# Bash — Automation Toolkit Architecture Blueprint

## Project Overview

- **Project Name:** Bash (opencode)
- **Project Type:** Automation Toolkit
- **Architecture Pattern:** Script Orchestration / Modular Library
- **Technology Stack:** Bun/TypeScript, PowerShell 5.1+, Shell
- **Package Manager:** Bun 1.3.14+
- **Stack Type:** Bun/TypeScript

## Technology Stack Details

| Category | Technology |
|---|---|
| Runtime | Bun 1.3.14+, Node.js >= 18 |
| Language | TypeScript (strict), PowerShell, Bash |
| Linting | ESLint 10.x, Prettier 3.x, Markdownlint, CSpell |
| Type Check | TypeScript (tsc --noEmit) |
| Testing | Vitest, shell test (`verify-dryrun.sh`) |
| Git Hooks | Husky 9.x, lint-staged |
| CI/CD | GitHub Actions (`.github/workflows/bash-scripts-ci.yml`) |

## Directory Structure

```
Bash/
├── AGENTS.md                    # Project context
├── package.json                 # Dependencies & scripts
├── .prettierrc.ts               # Formatting config
├── eslint.config.mts            # ESLint config
├── tsconfig.json                # TypeScript config
├── src/                         # TypeScript source scripts
│   ├── cache-clean.ts           # Cache cleaning
│   ├── clean-dep.ts             # Dependency cleaning
│   ├── git-commit-batches.ts    # Batch git commits
│   ├── upgrade.ts               # Upgrade utilities
│   └── ...                      # Other utilities
├── scripts/                     # PowerShell orchestration
│   ├── lib/                     # PowerShell library modules
│   │   ├── clone-utils.ps1      # Repository cloning
│   │   ├── dependency-scanner.ps1
│   │   ├── git-operations.ps1   # Git operations
│   │   ├── github-mcp.ps1       # GitHub MCP integration
│   │   ├── package-managers.ps1 # Package manager support
│   │   ├── repo-analyzer.ps1    # Repository analysis
│   │   └── triage-utils.ps1     # Triage utilities
│   ├── phase-1-discovery.ps1    # Phase 1: Discovery
│   ├── phase-1-deep-triage.ps1  # Deep triage
│   ├── phase-2-clone.ps1        # Phase 2: Cloning
│   ├── phase-3-triage.ps1       # Phase 3: Triage
│   ├── phase-4-debug.ps1        # Phase 4: Debugging
│   ├── phase-5-remediation.ps1  # Phase 5: Remediation
│   └── phase-6-cross-ref.ps1    # Phase 6: Cross-reference
├── Banking/scripts/             # Banking sub-project scripts
│   ├── orchestrator.bat         # Windows orchestrator
│   ├── opencode-mcp.bat         # MCP runner
│   └── ...                      # Other batch scripts
├── tests/                       # Test files
│   └── verify-dryrun.sh         # Dry-run verification
├── docs/                        # Documentation
│   ├── AGENTS.md
│   └── Project_Architecture/    # Architecture docs
└── .vscode/                     # VS Code config
    ├── launch.json
    └── extensions.json
```

## Architectural Patterns

### Phase-Based Orchestration Pattern
The toolkit follows a multi-phase pipeline:

1. **Phase 1 — Discovery**: Inventory repositories and dependencies
2. **Phase 2 — Clone**: Clone repositories locally
3. **Phase 3 — Triage**: Analyze and categorize issues
4. **Phase 4 — Debug**: Deep debugging of identified issues
5. **Phase 5 — Remediation**: Apply fixes and remediations
6. **Phase 6 — Cross-Reference**: Cross-reference across repos

### Modular Library Pattern
PowerShell scripts in `scripts/lib/` provide reusable modules:
- `dependency-scanner.ps1` — Scans for dependency issues
- `repo-analyzer.ps1` — Analyzes repository structure
- `git-operations.ps1` — Handles git operations
- `package-managers.ps1` — Multi-package-manager support

### Multi-Platform Wrapper Pattern
Each tool has wrapper parity across platforms:
- `.ps1` — PowerShell (Windows)
- `.sh` — Shell (Linux/Mac)
- `.bat` — Batch (Windows fallback)

## Data Flow

```
User Invocation → npm/bun run → TypeScript Script
                                     ↓
                              PowerShell Orchestrator
                                     ↓
                          ┌──────────┼──────────┐
                          ↓          ↓          ↓
                   Phase Scripts  Lib Modules  Utilities
                          ↓          ↓          ↓
                    Reports & Outputs / Logs
```

## Key Dependencies

- **TypeScript:** `zod`, `yaml`, `tsx`, `typescript`, `eslint`
- **Dev:** `prettier`, `husky`, `lint-staged`, `vitest`, `cspell`, `markdownlint`
- **Scripting:** PowerShell 5.1+, Bash

## Architecture Decisions

1. **Bun-first** — All TypeScript execution uses Bun runtime for speed
2. **PowerShell for orchestration** — Complex multi-phase workflows use PowerShell 5.1+
3. **Wrapper parity** — Every tool has `.sh`, `.ps1`, `.bat` versions for cross-platform support
4. **Dry-run by default** — All destructive operations support `--dry-run`
5. **Modular library** — Shared PowerShell functions in `scripts/lib/` for reusability

## Extensibility Points

- Add new phases as `phase-N-<name>.ps1`
- Add new library modules in `scripts/lib/`
- Add new TypeScript utilities in `src/`
- Add new CI workflows in `.github/workflows/`

## Implementation Patterns

### Dry-Run Pattern
```typescript
// All operations support --dry-run
if (args.dryRun) {
  console.log(`[DRY-RUN] Would ${operation}`);
  return;
}
```

### Logging Pattern
```bash
# All scripts log to logs/ with timestamps
LOG_FILE="logs/$(date +%Y%m%d-%H%M%S)-${SCRIPT_NAME}.log"
```

---

*Generated by architecture-blueprint-generator — comprehensive analysis*
