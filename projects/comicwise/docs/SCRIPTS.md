# ComicWise Script Registry & Documentation

**Last Updated**: $(date) **Status**: Phase 3 - Initial Implementation

## 📋 Complete Script Inventory

### Overview

ComicWise includes 81 npm scripts organized into 5 functional tiers for developers. All scripts support common options like `--dry-run`, `--json`, `--verbose`, and `--backup`.

---

## TIER 1: Essential Workflow (22 scripts)

Core development commands for daily work.

| Script | Command | Purpose | Options |
| --- | --- | --- | --- |
| `dev` | `pnpm dev` | Start dev server (Turbopack, port 3000) | - |
| `build` | `pnpm build` | Production build (Turbopack, ~24s) | - |
| `build:analyze` | `pnpm build:analyze` | Build with bundle analysis | `ANALYZE=true` |
| `build:debug` | `pnpm build:debug` | Build with debug output | - |
| `build:standalone` | `pnpm build:standalone` | Standalone production build | - |
| `start` | `pnpm start` | Run production build locally | - |
| `prebuild` | (automatic) | Runs before build (type-gen) | - |
| `postbuild` | (automatic) | Runs after build | - |
| `predev` | (automatic) | Runs before dev (type-gen) | - |
| `type-check` | `pnpm type-check` | Validate TypeScript (tsc --noEmit) | - |
| `type-check:watch` | `pnpm type-check:watch` | Type-check in watch mode | - |
| `type-gen` | `pnpm type-gen` | Generate next-env.d.ts | - |
| `lint` | `pnpm lint` | Run ESLint (diagnostic mode) | - |
| `lint:fix` | `pnpm lint:fix` | ESLint + Prettier auto-fix | - |
| `lint:strict` | `pnpm lint:strict` | Lint with zero warnings | - |
| `format` | `pnpm format` | Prettier format all files | - |
| `format:check` | `pnpm format:check` | Check formatting (non-destructive) | - |
| `test` | `pnpm test` | Run Vitest unit tests (jsdom) | `[file]` |
| `test:watch` | `pnpm test --watch` | Run tests in watch mode | - |
| `test:ui` | `pnpm test:ui` | Run Playwright E2E tests | - |
| `test:ui:codegen` | `pnpm test:ui:codegen` | Playwright code generator | - |
| `clean` | `pnpm clean` | Remove build artifacts (.next, .turbo, etc) | - |

### Quality Gates (Required Before PR)

```bash
pnpm type-check && pnpm lint:fix && pnpm test && pnpm build
# All four must pass. Type errors block deployment.
```

---

## TIER 2: Database & Seeding (18 scripts)

Database schema management and test data seeding.

| Script | Command | Purpose | Notes |
| --- | --- | --- | --- |
| `db:push` | `pnpm db:push` | Apply schema changes (dev only) | Use after schema.ts modifications |
| `db:studio` | `pnpm db:studio` | Drizzle Studio browser UI | Visual DB viewer/editor |
| `db:generate` | `pnpm db:generate` | Generate SQL migration files | From schema changes |
| `db:migrate` | `pnpm db:migrate` | Run pending migrations (prod) | Safe for production |
| `db:pull` | `pnpm db:pull` | Introspect database | Reverse engineering |
| `db:check` | `pnpm db:check` | Validate schema vs database | Catch drift early |
| `db:reset` | `pnpm db:reset` | Drop + regenerate + push | **DESTRUCTIVE** - dev only |
| `db:drop` | `pnpm db:drop` | Drop all tables | Use with caution |
| `seed` | `pnpm seed` | Seed all entities | Default: interactive |
| `seed:all` | `pnpm seed:all` | Seed all (CLI-driven) | Dependency orchestration |
| `seed:dry` | `pnpm seed --dry-run` | Preview seeding | Non-destructive |
| `seed:verbose` | `pnpm seed --verbose` | Detailed seed output | With progress info |
| `seed:validate` | `pnpm seed:validate` | Validate seed data | --dry-run --verbose |
| `seed:clear` | `pnpm seed:clear` | Clear all seed data | Via REST API |
| `seed:reset` | `pnpm seed:reset` | Clear all seed data | DELETE operation |
| Seeding entities: `seed:comics`, `seed:chapters`, `seed:types`, `seed:authors`, `seed:artists`, `seed:genres` | - | Entity-specific seeding | One script per entity |

---

## TIER 3: Health & Monitoring (14 scripts)

Service health checks and cache statistics.

| Script | Command | Purpose | Output |
| --- | --- | --- | --- |
| `health:all` | `pnpm health:all` | Check db, redis, general | Summary |
| `health:check` | `pnpm health:check` | General health check | CLI output |
| `health:check:json` | `pnpm health:check --json` | Health check (JSON) | Machine-readable |
| `health:check:verbose` | `pnpm health:check --verbose` | Detailed health check | Full details |
| `health:db` | `pnpm health:db` | Database connectivity | Status + latency |
| `health:db:json` | `pnpm health:db --json` | DB health (JSON) | For parsing |
| `health:db:verbose` | `pnpm health:db --verbose` | DB health (detailed) | Version, latency, status |
| `health:redis` | `pnpm health:redis` | Redis connectivity | Memory, response, latency |
| `health:redis:json` | `pnpm health:redis --json` | Redis health (JSON) | Machine-readable |
| `health:redis:verbose` | `pnpm health:redis --verbose` | Redis health (detailed) | Full metrics |
| `cache:clear` | `pnpm cache:clear` | Clear Redis cache | All keys or pattern |
| `cache:clear:dry` | `pnpm cache:clear --dry-run` | Preview cache clear | Non-destructive |
| `cache:stats` | `pnpm cache:stats` | Cache statistics | Memory, hit rates, keys |
| `cache:stats:json` | `pnpm cache:stats --json` | Cache stats (JSON) | For monitoring |

---

## TIER 4: Optimization & Code Quality (14 scripts)

Type inference, naming conventions, import optimization.

| Script | Command | Purpose | Safe? |
| --- | --- | --- | --- |
| `optimize:types` | `pnpm optimize:types` | Replace 'any' with proper types | --dry-run to preview |
| `optimize:types:dry` | `pnpm optimize:types --dry-run` | Preview type replacements | Read-only |
| `optimize:types:backup` | `pnpm optimize:types --backup` | Create backup before modifying | In .backups/ dir |
| `optimize:camelcase` | `pnpm optimize:camelcase` | Convert to camelCase | --dry-run available |
| `optimize:camelcase:dry` | `pnpm optimize:camelcase --dry-run` | Preview casing changes | Read-only |
| `optimize:kebabcase` | `pnpm optimize:kebabcase` | Convert to kebab-case | Rare usage |
| `optimize:kebabcase:check` | `pnpm optimize:kebabcase --check` | Check without modifying | Read-only |
| `imports:check` | `pnpm imports:check` | Check import path aliases | --dry-run (no changes) |
| `imports:optimize` | `pnpm imports:optimize` | Rewrite to use proper aliases | --dry-run available |
| `imports:optimize:dry` | `pnpm imports:optimize --dry-run` | Preview import changes | Read-only |
| `analyze` | `pnpm analyze` | Find unused dependencies | Analysis only |
| `analyze:packages` | `pnpm analyze:packages` | Detailed package analysis | --dry-run |
| `check-updates` | `pnpm check-updates` | List available updates | Information only |
| `upstash` | `pnpm upstash` | Upstash Redis management | Admin operations |

---

## TIER 5: Code Generation & Utilities (17 scripts)

Scaffolding, git operations, documentation generation.

| Script | Command | Purpose | Generates |
| --- | --- | --- | --- |
| `scaffold` | `pnpm scaffold` | Create new files/dirs | Interactive |
| `scaffold:action` | `pnpm scaffold:action` | Create Server Action | boilerplate |
| `scaffold:component` | `pnpm scaffold:component` | Create React Component | With props/types |
| `scaffold:hook` | `pnpm scaffold:hook` | Create custom hook | With types |
| `git:commit` | `pnpm git:commit` | Conventional commit helper | Assisted message |
| `git:init` | `pnpm git:init` | Initialize git repo | Setup |
| `git:push` | `pnpm git:push` | Push with message | Interactive |
| `docs:all` | `pnpm docs:all` | Generate all docs | Markdown files |
| `docs:generate` | `pnpm docs:generate` | Generate API docs | From code |
| `docs:prompts` | `pnpm docs:prompts` | Generate prompt docs | From .prompt files |
| `docs:readme` | `pnpm docs:readme` | Generate/update README | Markdown |
| `validate` | `pnpm validate` | Run all quality checks | format, type, lint, test |
| `prepare` | (automatic) | Runs before commit (husky) | Pre-commit hook |
| `posttest` | (automatic) | Runs after tests | Coverage reporting |
| `clean:all` | `pnpm clean:all` | Full cleanup + node_modules | Reset state |
| `clean:cache` | `pnpm clean:cache` | Clear build cache | .turbo, .next |

---

## 🔍 Using Scripts Effectively

### Common Patterns

**Development Workflow**:

```bash
pnpm dev              # Start dev server
pnpm type-check:watch # Type-check in watch mode (separate terminal)
pnpm test --watch     # Unit tests in watch mode (separate terminal)
```

**Before Committing**:

```bash
pnpm validate    # Runs: format, type-check, lint, test
# Then manually: pnpm build (validation)
```

**Database Changes**:

```bash
# 1. Modify src/database/schema.ts
pnpm db:push     # Apply changes to dev database
pnpm seed:all    # Repopulate test data
pnpm dev         # Restart dev server
```

**Optimization**:

```bash
pnpm optimize:types --dry-run      # Preview changes
pnpm optimize:types --backup       # Create backup before applying
pnpm optimize:types                # Apply optimization
```

### Script Option Patterns

All scripts that modify files support these options:

- **`--dry-run`**: Preview changes without applying (read-only)
- **`--backup`**: Create `.backups/` directory with originals
- **`--verbose`**: Show detailed progress and logging
- **`--json`**: Output as JSON for automation/parsing
- **`--yes`** or **`-y`**: Skip confirmation prompts (CI/CD compatible)

---

## 📊 Script Dependency Graph

```
dev, build
  ├─ prebuild (type-gen)
  ├─ predev (type-gen)
  └─ lint, format, type-check

test, test:ui
  ├─ test depends on: build success
  └─ posttest (coverage)

health:all
  ├─ health:db
  ├─ health:redis
  └─ health:check

seed:all (orchestrated)
  └─ Resolves dependencies between seeders

validate
  └─ Runs: format → type-check → lint → test (sequential)
```

---

## 📱 Common Tasks

### "I just cloned the repo"

```bash
pnpm install
cp .env.local.example .env.local  # Edit DATABASE_URL, AUTH_SECRET
pnpm db:push
pnpm seed:all
pnpm dev
```

### "I modified a schema"

```bash
pnpm db:push      # Apply changes
pnpm seed:all     # Repopulate test data
```

### "I want to commit code"

```bash
pnpm validate     # Format + type-check + lint + test
pnpm build        # Verify production build works
git add .
git commit -m "feat: description"
```

### "I need clean state"

```bash
pnpm clean:all    # Remove node_modules + lock
pnpm install
pnpm db:reset     # Drop + regenerate database
pnpm seed:all
```

### "CI/CD Pipeline Mode"

```bash
# Add --yes and --json to skip prompts
pnpm cache:clear --yes --json
pnpm seed:all --dry-run --json
pnpm health:all --json
pnpm type-check && pnpm lint:fix && pnpm test && pnpm build
```

---

## 🔧 Troubleshooting

### Type-check fails

```bash
pnpm type-check        # See detailed errors
pnpm lint:fix          # Auto-fix where possible
# Fix remaining manually
```

### Build fails

```bash
pnpm clean           # Remove build cache
pnpm build           # Retry
```

### Tests fail

```bash
pnpm test --watch    # Run in watch mode for debugging
pnpm test src/file.test.tsx  # Run single file
```

### Database sync issues

```bash
pnpm db:check        # Detect schema vs database drift
pnpm db:push         # Apply pending changes (dev)
pnpm db:migrate      # Apply migrations (prod)
pnpm db:pull         # Reverse-engineer from database
```

### Cache problems

```bash
pnpm cache:clear     # Clear all cache
pnpm cache:stats     # View cache statistics
pnpm health:redis    # Check Redis connection
```

---

## 📚 Running Specific Tests

```bash
# Single test file
pnpm test src/app/comics/page.test.tsx

# Watch mode for development
pnpm test --watch

# With coverage
pnpm test --coverage

# E2E tests
pnpm test:ui

# E2E with code generation
pnpm test:ui:codegen
```

---

## 🚀 Performance Notes

| Script       | Typical Time | Notes                 |
| ------------ | ------------ | --------------------- |
| `dev`        | ~5s          | Turbopack startup     |
| `build`      | ~24s         | Full production build |
| `type-check` | ~8-10s       | Full TypeScript check |
| `lint`       | ~15s         | All files             |
| `test`       | ~5-10s       | Depends on test count |
| `test:ui`    | ~30s         | Full E2E suite        |

---

## 📖 Documentation

For more detailed information:

- **Architecture**: See [docs/DEVELOPMENT.md](../DEVELOPMENT.md)
- **Database**: See [docs/DATABASE_SETUP.md](../DATABASE_SETUP.md)
- **Deployment**: See [docs/DEPLOYMENT.md](../DEPLOYMENT.md)
- **Implementation Status**: See [docs/IMPLEMENTATION_MASTER.md](../IMPLEMENTATION_MASTER.md)

---

**Last Updated**: Phase 3 Implementation **Maintainer**: ComicWise Development Team
