# 2. Essential Commands

> Extracted from `setup.prompt.md`.

## 2. Essential Commands

```bash
# ── Development ──
pnpm dev                         # Start dev server (Turbopack, port 3000)
pnpm type-check                  # tsc --noEmit — must be 0 errors before PR
pnpm type-check:watch            # tsc --noEmit --watch (continuous checking)
pnpm lint:fix                    # ESLint flat config + Prettier auto-fix
pnpm lint:strict                 # ESLint with --max-warnings=0
pnpm build                       # Production build (prebuild runs clean:cache + type-gen)
pnpm build:debug                 # Build with --debug-prerender
pnpm format                      # Prettier --write .
pnpm format:check                # Prettier --check .
pnpm type-gen                    # next typegen (runs automatically in prebuild/predev)

# ── Database ──
pnpm db:push                     # Apply schema changes (dev only, no migration files)
pnpm db:generate                 # Generate migration SQL files from schema changes
pnpm db:migrate                  # Run migration files (production)
pnpm db:studio                   # Open Drizzle Studio (browser DB viewer)
pnpm db:reset                    # Drop + regenerate + push (dev only!)
pnpm db:check                    # Verify migration consistency
pnpm db:drop                     # Drop migrations
pnpm db:pull                     # Introspect existing DB into schema

# ── Testing ──
pnpm test                        # Vitest unit tests (jsdom env)
pnpm test:ui                     # Playwright E2E tests
pnpm test:ui:codegen             # Playwright test code generator

# ── Seeding (CLI — direct, no server required) ──
pnpm seed --dry-run --verbose    # Validate all seed data without writing
pnpm seed:all                    # Seed all entities (respects dependency order)
pnpm seed:comics --force         # Upsert comics (idempotent)
pnpm seed:chapters --image-strategy=local --batch-size=500
pnpm seed:validate               # Dry-run validation only (alias)

# ── Seeding (REST API — requires dev server running) ──
pnpm seed:clear                  # DELETE via curl — clear all seed data
pnpm seed:reset                  # PUT via curl — delete + reseed all
curl http://localhost:3000/api/seed                        # GET — validate
curl -X POST http://localhost:3000/api/seed \
  -H 'Content-Type: application/json' \
  -d '{"entities":"all"}'                                  # POST — seed
curl -X DELETE http://localhost:3000/api/seed              # DELETE — clear

# ── Setup Automation ──
bash scripts/setup-dev.sh        # Linux/macOS dev environment setup
.\scripts\setup-dev.ps1          # Windows PowerShell dev environment setup
```

### Quality Gate (Required Before PR)

```bash
pnpm type-check          # Must be 0 TypeScript errors
pnpm lint:fix            # ESLint + Prettier auto-fix
pnpm test                # Vitest unit tests pass
pnpm build               # Production build succeeds
```

---
