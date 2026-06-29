# 6. Data Access Layer (DAL)

> Extracted from `setup.prompt.md`.

## 6. Data Access Layer (DAL)

### Base Class (`src/dal/base-dal.ts`)

```typescript
export interface DalOptions {
  limit?: number;
  offset?: number;
}

export abstract class BaseDal<T> {
  abstract list(options?: DalOptions): Promise<T[]>;
  abstract getById(id: string | number): Promise<T | null>;
  abstract create(data: unknown): Promise<T>;
  abstract update(
    id: string | number,
    data: unknown
  ): Promise<T | null>;
  abstract delete?(id: string | number): Promise<void>;

  protected handleError(error: unknown, operation: string): never {
    console.error(
      `[${this.constructor.name}] ${operation} failed:`,
      error
    );
    if (error instanceof Error) {
      if (error.message.includes("UNIQUE"))
        throw new Error("This record already exists");
      if (error.message.includes("FOREIGN KEY"))
        throw new Error("Related record not found");
      if (error.message.includes("NOT NULL"))
        throw new Error("Required field is missing");
    }
    throw new Error(`Failed to ${operation.toLowerCase()}`);
  }
}
```

### Implementation Pattern (`src/dal/comic-dal.ts`)

```typescript
import { db } from "@/database/db";
import { comic } from "@/database/schema";
import { BaseDal, type DalOptions } from "./base-dal";

type ComicType = typeof comic.$inferSelect; // IMPORTANT: use $inferSelect, not raw typeof

export class ComicDal extends BaseDal<ComicType> {
  async list(options?: ComicListOptions) {
    // Uses .with() for eager loading — NEVER loop + query (N+1)
    return db.query.comic.findMany({
      limit: options?.limit ?? 20,
      offset: options?.offset ?? 0,
      with: {
        author: true,
        artist: true,
        type: true,
        comicToGenre: { with: { genre: true } }
      }
    });
  }
  async getById(id: string) {
    /* ... */
  }
  async create(data: CreateComicInput) {
    /* ... */
  }
  async update(id: string, data: UpdateComicInput) {
    /* ... */
  }
}

export const comicDal = new ComicDal(); // Singleton export — REQUIRED
```

### DAL Query Patterns

| Pattern | When | Example |
| --- | --- | --- |
| `db.query.*.findMany/findFirst` with `.with()` | Primary pattern — eager loading of relations | `comic-dal`, `bookmark-dal`, `chapter-dal` |
| `db.select().from(table)` | Simple lookups without relations | `user-dal`, `type-dal`, `notification-dal`, `comic-image-dal` |

### ⚠ CRITICAL: No Explicit `relations()` in Schema

**There are zero `relations()` definitions in `schema.ts`.** DALs rely entirely on Drizzle's FK inference from `.references()` column declarations. This means:

- **Simple FK relations** (`comic.authorId → author.id`) auto-infer → `.with({ author: true })` works.
- **Junction tables** (`comicToGenre`) are inferred from FKs → `.with({ genres: { with: { genre: true } } })` works.
- **`comment.parentId` has NO `.references()` call** → parent/replies relation **cannot** be used with `db.query`. This is a known gap.
- **Self-referential, multi-FK-to-same-table, and custom-named relations** require explicit `relations()` to be added to schema.ts.

Current DALs work because they only use simple FK-inferred relations. **If you need advanced relations, you must add `relations()` definitions to schema.ts first.**

### N+1 Anti-Pattern Catalog

| Trap | ❌ Wrong | ✅ Right |
| --- | --- | --- |
| Comics + Authors | `for (comic of comics) { await getAuthor(comic.authorId) }` | `.with({ author: true })` |
| Bookmarks + Comics + Genres | Loop through bookmarks, fetch each comic | `db.query.bookmark.findMany({ with: { comic: { with: { genres: true } } } })` |
| Comment Threading | `comment.parentId` has no FK ref — can't use `.with()` | Manual SQL JOIN or add `relations()` to schema |
| Reading Progress Dashboard | Separate queries for each stat | `count()`, `sum()`, `avg()` in single aggregate query |

### Pagination Response Shape

```typescript
interface PaginatedResponse<T> {
  success: boolean;
  data: T[];
  meta: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
    hasNextPage: boolean;
    hasPrevPage: boolean;
  };
}
```

### DAL Rules

- **Every DAL** extends `BaseDal<typeof table.$inferSelect>` — NOT raw `typeof table`
- **Use `.with()`** for all related data — never `for` loop + individual queries
- **Singleton exports** at file bottom — required for import consumers
- **DAL is for app code only** — seeders bypass DAL for batch performance (see §8)

---
