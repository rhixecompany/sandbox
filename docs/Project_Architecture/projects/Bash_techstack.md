# 🏗 Technology Stack Blueprint - Bash Automation Toolkit

**Project Path:** `projects/Bash`
**Generated:** 2026-07-28
**Type:** TypeScript/Bun Automation Toolkit (6-Phase Orchestrator)

---

## Core Technologies

| Category | Technology | Version | License |
|----------|-----------|---------|---------|
| **Runtime** | Bun | 1.3.14+ | MIT |
| **Language** | TypeScript (strict) | Latest | Apache 2.0 |
| **Package Manager** | Bun | 1.3.14+ | MIT |
| **Linting** | ESLint 10 (flat config) | ^10.4.0 | MIT |
| **Formatting** | Prettier 3 | ^3.8.3 | MIT |
| **Testing** | Vitest | ^4.1.7 | MIT |
| **Validation** | zod | ^4.4.3 | MIT |
| **YAML Parsing** | yaml | ^2.9.0 | ISC |
| **Environment** | dotenv + dotenv-safe | ^17.4.2 / ^9.1.0 | MIT |

---

## Architecture Pattern

**6-Phase Orchestration Pipeline:**
```
Discovery → Clone → Triage → Debug → Remediation → Cross-Reference
```

Each phase is a separate TypeScript module with CLI entry point.

### Multi-Wrapper Parity
Every destructive script has 3 equivalents:
- `script.sh` (Bash)
- `script.ps1` (PowerShell 5.1+)
- `script.bat` (Windows Batch)

All support `--help` and `--dry-run` for safe preview.

---

## Key Dependencies

### Production (2 packages)
| Package | Version | Purpose |
|---------|---------|---------|
| `yaml` | ^2.9.0 | YAML parsing for config files |
| `zod` | ^4.4.3 | Schema validation |

### Development (~70 packages)
| Category | Key Packages |
|----------|-------------|
| **TypeScript** | `typescript`, `@types/node`, `@types/bun`, `@types/fs-extra`, `@types/js-yaml` |
| **ESLint** | `eslint`, `@typescript-eslint/parser`, `@typescript-eslint/eslint-plugin`, `@eslint-react/eslint-plugin`, `eslint-config-prettier`, `eslint-plugin-*` (15+ plugins) |
| **Prettier** | `prettier`, `prettier-plugin-organize-imports`, `prettier-plugin-packagejson`, `prettier-plugin-sort-json`, `prettier-plugin-tailwindcss` |
| **Testing** | `vitest`, `@vitest/browser-playwright`, `@vitest/coverage-v8`, `happy-dom`, `jsdom`, `@playwright/test` |
| **Utilities** | `tsx`, `ts-morph`, `ts-node`, `dts-gen`, `ts-stub`, `globby`, `glob`, `commander`, `inquirer`, `ora`, `chalk`, `cross-env`, `rimraf` |
| **Spell Check** | `cspell` |

---

## TypeScript Configuration

```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "Preserve",
    "moduleResolution": "bundler",
    "strict": true,
    "skipLibCheck": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "verbatimModuleSyntax": true,
    "noEmit": true
  }
}
```

---

## Scripts & Commands

| Script | Command | Description |
|--------|---------|-------------|
| `typecheck` | `tsc --noEmit --pretty` | Strict type checking |
| `lint` | `eslint --config eslint.config.mts .` | Lint with flat config |
| `lint:fix` | `eslint --fix` | Auto-fix lint issues |
| `lint:strict` | `eslint --max-warnings=0` | Zero-warnings gate |
| `format` | `prettier --write .` | Format all files |
| `format:check` | `prettier --check .` | Verify formatting |
| `test` | `vitest run` | Run unit tests |
| `clean:cache` | `tsx src/cache-clean.ts` | Clean caches (dry-run supported) |
| `clean:deps` | `tsx src/clean-dep.ts` | Clean unused deps (dry-run supported) |
| `upgrade` | `tsx src/upgrade.ts` | Upgrade dependencies |
| `commit:batches` | `tsx src/git-commit-batches.ts` | Batch commits |
| `cross-ref` | `bash Bash/scripts/phase-6-cross-ref.sh` | Cross-reference phase |

---

## Project Structure

```
projects/Bash/
├── src/
│   ├── cache-clean.ts          # Cache cleaning utility
│   ├── clean-dep.ts            # Dependency cleanup
│   ├── git-commit-batches.ts   # Git batch commits
│   ├── upgrade.ts              # Dependency upgrades
│   └── scripts/                # Phase scripts
├── scripts/                    # Shell/PowerShell wrappers
├── tests/                      # Vitest tests
├── eslint.config.mts           # ESLint flat config
├── .prettierrc.ts              # Prettier config
├── .lintstagedrc.ts            # Lint-staged config
├── package.json
├── tsconfig.json
└── bun.lock
```

---

## Conventions

### Code Style
- **TypeScript strict mode** — no `any`, no implicit returns
- **Zod v4** for all runtime validation
- **2-space indent**, single quotes (TS/JS), LF endings (enforced by EditorConfig)
- **No backup files** — use git for rollback

### Shell Scripts
- **Kebab-case** filenames: `phase-6-cross-ref.sh`
- **ShellCheck validated** — all `.sh` files pass ShellCheck
- **`--dry-run` mandatory** for destructive operations
- **Logs** to `logs/action_YYYYMMDD_HHMMSS.log`

### Testing
- **Vitest** for TypeScript unit tests (`*.test.ts`)
- **Shell tests** via `test-all.sh` and `tests/verify-dryrun.sh`
- **Coverage** via `@vitest/coverage-v8`

---

## CI/CD Pipeline

**Workflow:** `.github/workflows/bash-scripts-ci.yml`

1. **Setup** → `bun install --frozen-lockfile`
2. **Format** → `bun run format:check`
3. **Type Check** → `bun run typecheck`
4. **Lint** → `bun run lint:strict`
5. **Test** → `bun run test`
6. **Shell Verify** → `bash tests/verify-dryrun.sh && bash test-all.sh`

---

## License Summary

| License | Count |
|---------|-------|
| MIT | ~65 |
| ISC | ~3 |
| Apache 2.0 | ~2 |

---

*Generated by Hermes Agent Technology Stack Blueprint Generator*