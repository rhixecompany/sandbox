# Key Patterns

> Extracted from `comicwise-session.prompt.md`.

## Key Patterns

### DAL Pattern

```typescript
import { BaseDal } from "./base-dal";
type EntityType = typeof entity.$inferSelect;

export class EntityDal extends BaseDal<EntityType> {
  async list() {
    return db.query.entity.findMany({
      with: { relations: true } // Always eager load
    });
  }
}
export const entityDal = new EntityDal();
```

### Server Action Pattern

```typescript
"use server";
import { auth } from "@/auth";
import type { ActionResult } from "./types";

export async function actionName(
  input: unknown
): Promise<ActionResult<T>> {
  // 1. Auth first
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  // 2. Validate
  const parsed = Schema.safeParse(input);
  if (!parsed.success)
    return { ok: false, error: parsed.error.errors[0]?.message };

  try {
    // 3. Mutate
    const result = await dal.create(parsed.data);
    revalidatePath("/path");
    return { ok: true, data: result };
  } catch (error) {
    return { ok: false, error: "Failed to create" };
  }
}
```

### Component Pattern (with JSDoc + Dark Mode)

```typescript
/**
 * Component Name
 * Brief description of purpose and usage
 */
interface ComponentNameProps {
  /** Description of required prop */
  title: string;
  /** Optional prop with default */
  variant?: "primary" | "secondary";
}

export function ComponentName({ title, variant = "primary" }: ComponentNameProps) {
  return (
    <article className="rounded-lg border p-4 dark:border-muted-foreground">
      <h2 className="text-lg font-semibold dark:text-foreground">{title}</h2>
    </article>
  );
}
```
