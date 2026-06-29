# 7. Server Actions — Primary Mutation Pattern

> Extracted from `setup.prompt.md`.

## 7. Server Actions — Primary Mutation Pattern

### ActionResult Type (`src/actions/types.ts`)

```typescript
export type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };
```

### Standard Pattern (`src/actions/comic.actions.ts`)

```typescript
"use server";

import { auth } from "@/auth";
import { revalidatePath } from "next/cache";
import { CreateComicSchema } from "@/schemas/comic.schema";
import { comicDal } from "@/dal/comic-dal";
import type { ActionResult } from "./types";

export async function createComicAction(
  input: unknown
): Promise<ActionResult<ComicType>> {
  // 1. Auth check
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  // 2. Zod validation
  const parsed = CreateComicSchema.safeParse(input);
  if (!parsed.success)
    return {
      ok: false,
      error: parsed.error.errors[0]?.message ?? "Invalid"
    };

  // 3. DAL operation
  try {
    const comic = await comicDal.create(parsed.data);
    revalidatePath("/comics");
    return { ok: true, data: comic };
  } catch (e) {
    return { ok: false, error: "Failed to create comic" };
  }
}
```

### Rules

- **All app mutations** go through Server Actions — NOT API routes
- **Always validate** with Zod before passing to DAL
- **Always check auth** as first step
- **Return `ActionResult<T>`** — never throw from actions
- **Call `revalidatePath()`** after mutations to bust Next.js cache

---
