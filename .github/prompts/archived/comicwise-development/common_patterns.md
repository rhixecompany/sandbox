# Common Patterns

> Extracted from `comicwise-development.prompt.md`.

## Common Patterns

### DAL Query Pattern (with Eager Loading)

```typescript
import { BaseDal } from "./base-dal";
type ComicType = typeof comic.$inferSelect;

export class ComicDal extends BaseDal<ComicType> {
  async list() {
    return db.query.comic.findMany({
      with: {
        author: true,
        genres: { with: { genre: true } },
        chapters: { orderBy: [c => desc(c.chapterNumber)] }
      }
    });
  }
}
export const comicDal = new ComicDal();
```

### Server Action Pattern (auth → validate → mutate → revalidate)

```typescript
"use server";
import { auth } from "@/auth";
import type { ActionResult } from "./types";

export async function createComicAction(
  input: unknown
): Promise<ActionResult<Comic>> {
  // 1. AUTH FIRST
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  // 2. VALIDATE
  const parsed = CreateComicSchema.safeParse(input);
  if (!parsed.success)
    return { ok: false, error: parsed.error.errors[0]?.message };

  try {
    // 3. MUTATE
    const comic = await comicDal.create(parsed.data);

    // 4. REVALIDATE
    revalidatePath("/comics");
    revalidateTag("comics");

    // 5. RETURN ActionResult
    return { ok: true, data: comic };
  } catch (error) {
    return { ok: false, error: "Failed to create comic" };
  }
}
```

### Component Pattern (with JSDoc + Dark Mode)

```typescript
/**
 * Comic Card Component
 * Displays a comic in grid/list view with optional status/type overlay
 */
interface ComicCardProps {
  /** Comic object with all required fields */
  comic: Comic;
  /** Display variant */
  variant?: "grid" | "list";
}

export function ComicCard({ comic, variant = "grid" }: ComicCardProps) {
  return (
    <article className="rounded-lg border p-4 dark:border-muted-foreground">
      <h2 className="text-lg font-semibold dark:text-foreground">{comic.title}</h2>
      <p className="text-sm text-muted-foreground dark:text-muted-foreground">
        {comic.synopsis}
      </p>
    </article>
  );
}
```

### Zod Schema Composition

```typescript
// Base schema
const BaseComicSchema = z.object({
  title: z.string().min(1).max(255),
  slug: z.string().regex(/^[a-z0-9-]+$/),
  synopsis: z.string().min(10).max(5000)
});

// Extend for create
export const CreateComicSchema = BaseComicSchema.extend({
  authorId: z.string().uuid(),
  genreIds: z.array(z.string().uuid()).min(1)
});

// Extend for update (all optional)
export const UpdateComicSchema = BaseComicSchema.partial();

// Infer type automatically
export type Comic = z.infer<typeof CreateComicSchema>;
```
