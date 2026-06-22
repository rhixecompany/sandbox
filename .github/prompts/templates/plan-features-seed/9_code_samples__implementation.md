# 9. Code Samples & Implementation References

> Extracted from `plan-features-seed.prompt.md`.

## 9. Code Samples & Implementation References

### Core Types (`src/scripts/seed/types.ts`)

```typescript
// TypeScript interfaces for the seeding system
export interface SeedOptions {
  verbose?: boolean;
  dryRun?: boolean;
  skipValidation?: boolean;
  useTransaction?: boolean;
  batchSize?: number;
  concurrency?: number;
  imageStrategy?: "urls" | "local" | "imagekit";
  forceOverwrite?: boolean;
}

export interface SeedConfig {
  entities: (
    | "types"
    | "authors"
    | "artists"
    | "genres"
    | "comics"
    | "chapters"
    | "users"
    | "all"
  )[];
  options: SeedOptions;
  timestamp: Date;
}

export interface EntityResult {
  entityName: string;
  inserted: number;
  updated: number;
  skipped: number;
  errors: SeedError[];
  duration: number;
  success: boolean;
}

export interface SeedReport {
  timestamp: Date;
  success: boolean;
  totalDuration: number;
  results: EntityResult[];
  warnings: string[];
  errors: string[];
  summary: {
    totalInserted: number;
    totalUpdated: number;
    totalSkipped: number;
    totalErrors: number;
  };
}

export interface SeedError {
  itemIndex: number;
  value: unknown;
  message: string;
}

export type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

export interface LookupCache {
  authors: Map<string, { id: string; name: string }>;
  artists: Map<string, { id: string; name: string }>;
  types: Map<string, string>; // name → id
  genres: Map<string, string>;
  comics: Map<string, string>; // slug → id
}
```

### Logger Implementation (`src/scripts/seed/logger.ts`)

```typescript
import chalk from "chalk";

export class Logger {
  private verbose: boolean = false;

  constructor(verbose: boolean = false) {
    this.verbose = verbose;
  }

  info(message: string): void {
    console.log(chalk.blue("ℹ"), message);
  }

  success(message: string): void {
    console.log(chalk.green("✓"), message);
  }

  warn(message: string): void {
    console.log(chalk.yellow("⚠"), message);
  }

  error(message: string): void {
    console.log(chalk.red("✗"), message);
  }

  debug(message: string): void {
    if (this.verbose) {
      console.log(chalk.gray("➤"), message);
    }
  }

  section(title: string): void {
    console.log("\n" + chalk.cyan.bold("━".repeat(50)));
    console.log(chalk.cyan.bold(`  ${title}`));
    console.log(chalk.cyan.bold("━".repeat(50)) + "\n");
  }

  progress(message: string): void {
    console.log(chalk.white("→"), message);
  }

  table(data: Record<string, unknown>[]): void {
    console.table(data);
  }
}

export const logger = new Logger();
```

### Zod Schema Example (`src/schemas/seed/user.seed.ts`)

```typescript
import { z } from "zod";

export const userSeedSchema = z.array(
  z.object({
    id: z.string().uuid().optional(),
    email: z.string().email(),
    name: z.string().min(1),
    password: z.string().min(6),
    role: z.enum(["user", "admin", "moderator"]).default("user"),
    image: z.string().url().nullable().optional(),
    emailVerified: z.coerce.date().nullable().optional(),
    status: z.boolean().default(true),
    createdAt: z.coerce.date().default(() => new Date()),
    updatedAt: z.coerce.date().default(() => new Date()),
    lastActivityDate: z.coerce.date().nullable().optional()
  })
);

export type UserSeed = z.infer<typeof userSeedSchema>;
```

### Comic Schema Example (`src/schemas/seed/comic.seed.ts`)

```typescript
import { z } from "zod";

const comicStatusEnum = z.enum([
  "Ongoing",
  "Completed",
  "Hiatus",
  "Dropped",
  "Season End",
  "Coming Soon"
]);

export const comicSeedSchema = z.array(
  z.object({
    title: z.string().min(1),
    slug: z.string().min(1),
    description: z.string().optional(),
    url: z.string().url().optional(),
    rating: z.coerce.number().min(0).max(10).default(0),
    status: comicStatusEnum.default("Ongoing"),
    serialization: z.string().optional(),
    updatedAt: z.coerce.date().default(() => new Date()),
    views: z.coerce.number().default(0),
    coverImage: z.string().url().nullable(),
    type: z
      .object({
        name: z.string()
      })
      .optional(),
    author: z
      .object({
        name: z.string()
      })
      .nullable()
      .optional(),
    artist: z
      .object({
        name: z.string()
      })
      .nullable()
      .optional(),
    genres: z
      .array(
        z.object({
          name: z.string()
        })
      )
      .default([]),
    images: z
      .array(
        z.object({
          url: z.string().url()
        })
      )
      .default([])
  })
);

export type ComicSeed = z.infer<typeof comicSeedSchema>;
```

### DataLoader Implementation (`src/scripts/seed/dataLoader.ts`)

```typescript
import fs from "fs/promises";
import path from "path";
import { Logger } from "./logger";

export class DataLoader {
  private cache = new Map<string, unknown[]>();
  private logger: Logger;

  constructor(logger: Logger) {
    this.logger = logger;
  }

  async loadWithFallback<T>(baseFileName: string): Promise<T[]> {
    const cacheKey = baseFileName;
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey) as T[];
    }

    const candidates = [
      `${baseFileName}.json`,
      `${baseFileName}-data1.json`,
      `${baseFileName}-data2.json`
    ];

    for (const candidate of candidates) {
      const filePath = path.join(
        process.cwd(),
        "src/data",
        candidate
      );
      try {
        const content = await fs.readFile(filePath, "utf-8");
        const data = JSON.parse(content) as T[];
        this.cache.set(cacheKey, data);
        this.logger.success(
          `Loaded ${data.length} records from ${candidate}`
        );
        return data;
      } catch (error) {
        this.logger.debug(
          `Failed to load ${candidate}, trying next...`
        );
      }
    }

    throw new Error(`No data file found for ${baseFileName}`);
  }

  clearCache(): void {
    this.cache.clear();
  }
}
```

### BaseSeeder Abstract Class Pattern (`src/scripts/seed/seeders/baseSeed.ts`)

```typescript
import { z } from "zod";
import { Logger } from "../logger";
import { EntityResult, LookupCache, SeedOptions } from "../types";

export abstract class BaseSeeder<T> {
  protected entityName: string;
  protected schema: z.ZodType;
  protected cache: LookupCache;
  protected logger: Logger;
  protected options: SeedOptions;
  protected dependencies: string[] = [];

  constructor(
    entityName: string,
    schema: z.ZodType,
    cache: LookupCache,
    logger: Logger,
    options: SeedOptions
  ) {
    this.entityName = entityName;
    this.schema = schema;
    this.cache = cache;
    this.logger = logger;
    this.options = options;
  }

  // Template method pattern
  async seed(): Promise<EntityResult> {
    this.logger.section(`Seeding ${this.entityName}`);

    try {
      const data = await this.loadData();
      const validated = await this.validateData(data);

      if (this.options.dryRun) {
        this.logger.warn("DRY RUN: No data will be persisted");
        return {
          entityName: this.entityName,
          inserted: validated.length,
          updated: 0,
          skipped: 0,
          errors: [],
          duration: 0,
          success: true
        };
      }

      return await this.insertBatch(validated);
    } catch (error) {
      this.logger.error(`Error seeding ${this.entityName}: ${error}`);
      return {
        entityName: this.entityName,
        inserted: 0,
        updated: 0,
        skipped: 0,
        errors: [
          { itemIndex: 0, value: null, message: String(error) }
        ],
        duration: 0,
        success: false
      };
    }
  }

  // Abstract methods - subclasses must implement
  protected abstract getDataSources(): string[];
  protected abstract transformData(raw: T): unknown;
  protected abstract insertBatch(data: T[]): Promise<EntityResult>;

  // Concrete implementations
  protected async loadData(): Promise<T[]> {
    const sources = this.getDataSources();
    // Load from JSON files with fallback pattern
    this.logger.debug(
      `Loading data from sources: ${sources.join(", ")}`
    );
    // Implementation delegates to DataLoader
    return [] as T[];
  }

  protected async validateData(data: T[]): Promise<T[]> {
    if (this.options.skipValidation) {
      return data;
    }

    const validated: T[] = [];
    const errors: Array<{ index: number; error: string }> = [];

    for (let i = 0; i < data.length; i++) {
      const result = this.schema.safeParse(data[i]);
      if (result.success) {
        validated.push(result.data as T);
      } else {
        errors.push({
          index: i,
          error:
            result.error.errors[0]?.message || "Validation failed"
        });
      }
    }

    if (errors.length > 0 && this.options.verbose) {
      this.logger.warn(
        `${errors.length} validation errors encountered`
      );
    }

    return validated;
  }
}
```

### CLI Usage Examples

```bash
# Seed all entities with defaults
pnpm seed

# Seed specific entities
pnpm seed types
pnpm seed authors artists
pnpm seed comics chapters

# Dry-run validation
pnpm seed --dry-run --verbose

# Custom batch and concurrency settings
pnpm seed comics --batch-size=50 --concurrency=3

# Force overwrite (upsert mode)
pnpm seed --force

# No transactions (faster but less safe)
pnpm seed --no-transaction
```

### API Endpoint Examples

```bash
# Validate seeding (no auth required)
curl -X GET http://localhost:3000/api/seed

# Start seeding (admin auth required)
curl -X POST http://localhost:3000/api/seed \
  -H "Content-Type: application/json" \
  -d '{"entities": "all", "options": {"batchSize": 100, "concurrency": 5}}'

# Reset database (delete all seeded data)
curl -X DELETE http://localhost:3000/api/seed

# Upsert with force-overwrite
curl -X PATCH http://localhost:3000/api/seed \
  -H "Content-Type: application/json" \
  -d '{"entities": "comics", "options": {"forceOverwrite": true}}'

# Full reset (delete + reseed)
curl -X PUT http://localhost:3000/api/seed \
  -H "Content-Type: application/json" \
  -d '{"entities": "all"}'
```

### Progress Tracker Output Example

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Seeding Comics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

→ Loading data from sources: comic.json
✓ Loaded 2087 records from comic.json

→ Validating 2087 records...
✓ Validation complete: 2087 valid, 0 errors

→ Processing in batches (batch-size=100, concurrency=5):
  [████████████████████░░░░░░░░░░░░░░░░░░░░░░ ] 52% (1087/2087)
  Inserted 1087 | Speed: 218/sec | ETA: 4.6s

✓ Comics seeding completed
  Inserted: 2087 | Updated: 0 | Skipped: 0 | Errors: 0 | Duration: 9.5s
```

### File Structure Reference

```
src/scripts/seed/
├── types.ts                      # 200+ lines: Core types & interfaces
├── logger.ts                     # 80 lines: Colored logging utility
├── config.ts                     # 120 lines: CLI arg parsing with Commander
├── dataLoader.ts                 # 100 lines: Multi-file JSON loader
├── run.ts                        # 30 lines: CLI entry point
├── index.ts                      # 20 lines: Export all seeders
├── seedOrchestrator.ts          # 180 lines: Orchestrate seeding order
│
├── seeders/
│   ├── baseSeed.ts              # 180 lines: Abstract base class
│   ├── typeSeeder.ts            # 80 lines: Seed predefined types
│   ├── authorSeeder.ts          # 100 lines: Seed authors from JSON
│   ├── artistSeeder.ts          # 100 lines: Seed artists from JSON
│   ├── genreSeeder.ts           # 100 lines: Seed genres from JSON
│   ├── comicSeeder.ts           # 250 lines: Complex comic + image handling
│   └── chapterSeeder.ts         # 200 lines: Chapters + image extraction
│
├── helpers/
│   ├── progressTracker.ts       # 150 lines: Progress metrics & logging
│   ├── creatorNameResolver.ts   # 80 lines: Name splitting & dedup
│   ├── dateParser.ts            # 40 lines: Flexible date parsing
│   └── chapterNumberExtractor.ts # 30 lines: Regex chapter extraction
│
├── database/
│   ├── batchProcessor.ts        # 120 lines: Concurrent batch processing
│   ├── transactionManager.ts    # 40 lines: Drizzle transaction wrapper
│   └── conflictResolver.ts      # 50 lines: Upsert patterns
│
└── images/
    ├── imageDownloader.ts       # 150 lines: Local cache + retries
    ├── imageKitUploader.ts      # 80 lines: ImageKit integration
    └── imageStrategy.ts         # 100 lines: Strategy pattern dispatcher

src/schemas/seed/
├── user.seed.ts                 # 30 lines: User Zod schema
├── comic.seed.ts                # 40 lines: Comic Zod schema
├── chapter.seed.ts              # 35 lines: Chapter Zod schema
└── index.ts                     # 10 lines: Schema exports

src/app/api/seed/
└── route.ts                     # 200 lines: REST API (GET, POST, DELETE, PUT, PATCH)
```

### Config Parser Example (`src/scripts/seed/config.ts`)

```typescript
import { Command } from "commander";
import { z } from "zod";
import { SeedConfig } from "./types";

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  NODE_ENV: z
    .enum(["development", "production"])
    .default("development"),
  IMAGEKIT_PUBLIC_KEY: z.string().optional(),
  IMAGEKIT_PRIVATE_KEY: z.string().optional()
});

export function parseCliArgs(): SeedConfig {
  const program = new Command();

  program
    .command("seed [entities...]")
    .description("Seed database with test data")
    .option(
      "--batch-size <number>",
      "Batch size for processing",
      "100"
    )
    .option("--concurrency <number>", "Concurrent operations", "5")
    .option("--verbose", "Verbose logging")
    .option("--dry-run", "Validate without persisting")
    .option("--force", "Force overwrite existing data")
    .option("--no-transaction", "Disable transactions")
    .option("--skip-validation", "Skip Zod validation")
    .option(
      "--image-strategy <mode>",
      "Image strategy: urls|local|imagekit",
      "urls"
    )
    .action((entities, options) => {
      const env = envSchema.parse(process.env);

      return {
        entities: entities.length === 0 ? ["all"] : entities,
        options: {
          batchSize: parseInt(options.batchSize),
          concurrency: parseInt(options.concurrency),
          verbose: options.verbose,
          dryRun: options.dryRun,
          useTransaction: options.transaction,
          skipValidation: options.skipValidation,
          forceOverwrite: options.force,
          imageStrategy: options.imageStrategy
        },
        timestamp: new Date()
      } satisfies SeedConfig;
    });

  return program.parse().opts();
}
```

---

**Plan Version**: 1.0  
**Status**: Planned  
**Total Tasks**: 83  
**Estimated Effort**: 40-50 hours development + 10 hours testing  
**Next Step**: Begin Implementation Phase 1 (Core Infrastructure & Types)
