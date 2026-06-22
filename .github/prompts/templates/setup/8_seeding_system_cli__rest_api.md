# 8. Seeding System (CLI + REST API)

> Extracted from `setup.prompt.md`.

## 8. Seeding System (CLI + REST API)

### When to Use What

| Context | Pattern | Why |
| --- | --- | --- |
| **App code** (UI mutations) | Server Action → DAL | Type-safe, auth, validation, cache invalidation |
| **Seeding** (bulk insert) | Seeder → direct Drizzle | Batch performance (50k items in ~8 min vs hours via DAL) |

### Seeder Template (`BaseSeed<T>`)

All seeders extend `BaseSeed<T>` and override 4 methods:

```typescript
import { BaseSeed } from "./baseSeed";
import { db } from "@/database/db";
import { myEntity } from "@/database/schema";

export class MyEntitySeeder extends BaseSeed<MyEntity> {
  entityName = "MyEntity"; // Display name
  entityDataKey = "myEntities"; // Root key in JSON file
  dependencies = []; // Seeders that must run first
  dataSourceName = "my-entity"; // Filename: src/data/my-entity.json

  protected getDataSources() {
    return [this.dataSourceName];
  }

  protected transformData(items: unknown[]): MyEntity[] {
    return items.map(item => {
      /* normalize raw JSON → typed entity */
    });
  }

  protected async insertBatch(data: MyEntity[]): Promise<void> {
    await db
      .insert(myEntity)
      .values(data)
      .onConflictDoUpdate({
        target: myEntity.id,
        set: { updatedAt: new Date() }
      });
  }
}

export const myEntitySeeder = new MyEntitySeeder(); // Singleton
```

### Dependency Graph

```
types ──┐
        ├─→ authors ──┐
        │             ├─→ comics ──→ chapters
genres ─┤             │
        ├─→ artists ──┘
users (independent)
```

### CLI Flags (Full Reference)

```bash
--dry-run                             # Validate without writing to database
--verbose                             # Detailed output logging
--image-strategy=urls|local|imagekit  # Image handling strategy
--batch-size=N                        # Records per batch (default varies per entity)
--concurrency=N                       # Parallel batch limit (default: 3)
--skip-validation                     # Skip Zod validation (⚠ dangerous)
--no-transaction                      # Disable per-batch transactions
--force                               # Upsert mode (onConflictDoUpdate)
```

### Image Strategies (swap at runtime)

```bash
--image-strategy=urls      # Default: use original URLs as-is
--image-strategy=local     # Download to ./public/comics/{type}/{id}.{ext}
--image-strategy=imagekit  # Upload to ImageKit CDN
```

### REST API (`src/app/api/seed/route.ts`)

| Method   | Purpose                      | Auth Required (prod) |
| -------- | ---------------------------- | -------------------- |
| `GET`    | Validate (dry-run)           | No                   |
| `POST`   | Full seed (clear + populate) | Yes (admin)          |
| `PATCH`  | Upsert only                  | Yes (admin)          |
| `PUT`    | Reset (delete + reseed)      | Yes (admin)          |
| `DELETE` | Clear all seed data          | Yes (admin)          |

### REST API Request Body Schema

```json
{
  "entities": "all | comics | chapters | authors | artists | genres | types",
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

> **Note:** In production, seed API endpoints require admin role authentication (401 without it). `pnpm seed:clear` and `pnpm seed:reset` use `curl` under the hood and require the dev server to be running.

---
