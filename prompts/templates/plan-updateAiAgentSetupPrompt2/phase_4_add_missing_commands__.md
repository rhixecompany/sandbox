# Phase 4: Add Missing Commands & Workflows (4 items)

> Extracted from `plan-updateAiAgentSetupPrompt2.prompt.md`.

## Phase 4: Add Missing Commands & Workflows (4 items)

### Step 22 — Add missing commands to §2

```bash
# ── Database (additional) ──
pnpm db:generate                 # Generate migration SQL files from schema changes
pnpm db:migrate                  # Run migration files (production)
pnpm db:reset                    # Drop + regenerate + push (dev only!)
pnpm db:migration-status         # Check current migration status
pnpm type-gen                    # next typegen (runs automatically in prebuild/predev)

# ── Seeding (additional) ──
pnpm seed:validate               # Dry-run validation only
pnpm seed:clear                  # Clear all seeded data
pnpm seed:reset                  # Delete + reseed (full reset)
```

### Step 23 — Add full seed CLI flags to §8

```bash
--dry-run                        # Validate without writing (already documented)
--verbose                        # Detailed output (already documented)
--image-strategy=urls|local|imagekit  # Image handling (already documented)
--batch-size=N                   # Records per batch (already documented)
--concurrency=N                  # Parallel batch limit (default: 3)
--skip-validation                # Skip Zod validation (dangerous)
--no-transaction                 # Disable per-batch transactions
--force                          # Upsert mode (onConflictDoUpdate)
```

### Step 24 — Add seed REST API request body schema to §8

```json
{
  "entities": "all" | "comics" | "chapters" | "...",
  "options": {
    "batchSize": 100,
    "concurrency": 3,
    "verbose": false,
    "dryRun": false,
    "skipValidation": false,
    "useTransaction": true,
    "forceOverwrite": false,
    "imageStrategy": "urls"
  }
}
```

Note: In production, seed API endpoints require admin role authentication (401 without it).

### Step 25 — Document setup automation scripts

```bash
# Automated dev environment setup
bash scripts/setup-dev.sh        # Linux/macOS
.\scripts\setup-dev.ps1          # Windows PowerShell
```

---
