# Quick Reference: Core Patterns

> Extracted from `plan-dev.prompt.md`.

## Quick Reference: Core Patterns

### Server Action Pattern

```typescript
"use server";
type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

export async function myAction(
  input: unknown
): Promise<ActionResult<MyType>> {
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };

  const parsed = schema.safeParse(input);
  if (!parsed.success)
    return { ok: false, error: parsed.error.errors[0]?.message };

  try {
    const result = await dal.create(parsed.data);
    revalidatePath("/path");
    return { ok: true, data: result };
  } catch (error) {
    console.error("[myAction]", error);
    return { ok: false, error: "Operation failed" };
  }
}
```

### DAL Pattern

```typescript
export class MyDal extends BaseDal<MyType> {
  async list(options?: { limit?: number; offset?: number }) {
    return db.query.myTable.findMany({
      limit: options?.limit ?? 20,
      offset: options?.offset ?? 0,
      with: {
        /* eager load relationships */
      },
      orderBy: t => desc(t.createdAt)
    });
  }

  async getById(id: number) {
    return db.query.myTable.findFirst({
      where: eq(myTable.id, id),
      with: {
        /* relationships */
      }
    });
  }
}
```

### Protected Route Pattern

```typescript
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function AdminPage() {
  const session = await auth();
  if (!session?.user) redirect("/auth/signin");

  const user = session.user as { role?: unknown };
  if (typeof user.role !== "string" || user.role !== "admin") {
    redirect("/");
  }

  return <div>Admin Content</div>;
}
```

---
