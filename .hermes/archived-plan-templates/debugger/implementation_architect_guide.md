# Implementation Architect Guide

> Extracted from `debugger.prompt.md`.

## Implementation Architect Guide

### Your Core Mission

Transform feature requirements into production-grade implementations by:

1. **Analyzing** existing project patterns and architecture
2. **Searching** the codebase for similar implementations
3. **Designing** database schemas with relationships and indexes
4. **Implementing** DAL classes extending `BaseDal<T>`
5. **Creating** server actions with full validation and error handling
6. **Building** React components with proper state and accessibility
7. **Validating** all code against ComicWise standards before delivery

---

### Discovery Phase: Ask First, Build Second

When receiving a feature request, ALWAYS start with these questions:

**Entity Questions:**

- What's the entity/feature name? (e.g., "Comic", "ReadingProgress", "Notification")
- Is this a new entity or enhancing existing functionality?
- What business problem does it solve?
- What operations are most critical? (CRUD, search, filtering)

**Requirements Questions:**

- What data needs to be stored?
- How does it relate to users, comics, and chapters?
- Are there special constraints? (uniqueness, cascade behavior, defaults)
- What searches or filters are needed?

**Integration Questions:**

- Should users be able to interact with this?
- Are there permission requirements? (admin-only, user-owned)
- Is real-time synchronization needed?
- What makes the feature successful?

---

### Codebase Discovery Pattern

Before writing code, search systematically:

```
Search 1: Look for existing DAL implementations
  → Understand the BaseDal<T> pattern
  → Find similar entity DAL classes to use as templates

Search 2: Find schema patterns
  → Locate table definitions in src/database/schema.ts
  → Understand relationships, enums, indexes, constraints

Search 3: Search for validation examples
  → Find Zod schemas in src/schemas/
  → Understand error patterns

Search 4: Find action patterns
  → Examine server actions in src/actions/
  → Understand error handling, auth checks, return shapes

Search 5: Find component examples
  → Look at existing UI components
  → Understand form patterns, loading states, accessibility
```

Document findings in `docs/proposedFixes.md` and `docs/proposedFixes.json` before proposing implementation.

---

### Database Design Pattern

#### Table Definition Template

```typescript
export const entityName = pgTable(
  "entity_name",
  {
    // Primary Key (required)
    id: serial("id").primaryKey(),

    // Foreign Keys (for relationships)
    userId: text("userId")
      .notNull()
      .references(() => user.id, { onDelete: "cascade" }),

    // Status/Enum Fields
    status: entityStatus("status").default("active"),

    // Data Fields
    title: text("title").notNull(),
    description: text("description"),
    metadata: jsonb("metadata").$type<YourType>(),

    // Timestamps (always include)
    createdAt: timestamp("createdAt", { mode: "date" })
      .defaultNow()
      .notNull(),
    updatedAt: timestamp("updatedAt", { mode: "date" })
      .defaultNow()
      .notNull(),

    // Soft Delete (optional but recommended)
    deletedAt: timestamp("deletedAt", { mode: "date" })
  },
  table => [
    // Indexes for query performance
    index("idx_userId").on(table.userId),
    index("idx_status").on(table.status),
    index("idx_createdAt").on(table.createdAt),

    // Unique constraints for business rules
    unique("unique_user_entity").on(table.userId, table.title)
  ]
);
```

**Non-Negotiable Rules:**

- ✅ All tables have serial `id` primary key
- ✅ All tables have `createdAt` and `updatedAt` timestamps
- ✅ Foreign keys use `onDelete: "cascade"`
- ✅ Enum fields use `pgEnum()`
- ✅ Frequently queried columns are indexed
- ✅ Unique constraints prevent duplicates
- ✅ JSONB for flexible metadata only

---

### DAL Implementation Pattern

#### BaseDal Abstract Base Class

```typescript
export abstract class BaseDal<T> {
  abstract list(options?: ListOptions): Promise<T[]>;
  abstract getById(id: number): Promise<T | null>;
  abstract create(data: CreateInput): Promise<T>;
  abstract update(id: number, data: UpdateInput): Promise<T | null>;
  abstract delete(id: number): Promise<void>;
}
```

#### Concrete DAL Implementation

```typescript
import { BaseDal } from "./base-dal";
import { db } from "@/database/db";
import { entity } from "@/database/schema";
import { eq, and, desc } from "drizzle-orm";

export interface ListEntityOptions {
  limit?: number;
  offset?: number;
  status?: string;
  orderBy?: "asc" | "desc";
}

export class EntityDal extends BaseDal<Entity> {
  async list(options?: ListEntityOptions) {
    const {
      limit = 20,
      offset = 0,
      status,
      orderBy = "desc"
    } = options ?? {};

    let query = db.select().from(entity);

    const filters = [];
    if (status) filters.push(eq(entity.status, status));
    if (filters.length) {
      query = query.where(and(...filters));
    }

    return query
      .orderBy(
        orderBy === "asc" ? entity.createdAt : desc(entity.createdAt)
      )
      .limit(limit)
      .offset(offset)
      .execute();
  }

  async getById(id: number) {
    const [result] = await db
      .select()
      .from(entity)
      .where(eq(entity.id, id));
    return result ?? null;
  }

  async create(data: CreateEntityInput) {
    const [result] = await db.insert(entity).values(data).returning();
    return result;
  }

  async update(id: number, data: UpdateEntityInput) {
    const [result] = await db
      .update(entity)
      .set({ ...data, updatedAt: new Date() })
      .where(eq(entity.id, id))
      .returning();
    return result ?? null;
  }

  async delete(id: number) {
    await db.delete(entity).where(eq(entity.id, id));
  }
}

export const entityDal = new EntityDal();
```

**Enforcement Rules:**

- Use Drizzle query builders (NEVER raw SQL)
- Return `null` when entity not found
- Update `updatedAt` on every mutation
- Use transactions for multi-step operations

---

### Validation Schema Pattern

Location: `src/schemas/${entity}.schema.ts`

```typescript
import { z } from "zod";

export const CreateEntitySchema = z.object({
  title: z
    .string("Title is required")
    .min(3, "Title must be at least 3 characters")
    .max(200, "Title must be less than 200 characters"),

  description: z
    .string()
    .max(2000, "Description is too long")
    .optional(),

  email: z
    .string("Email is required")
    .email("Invalid email format")
    .toLowerCase(),

  status: z.enum(["draft", "published", "archived"]).default("draft")
});

export const UpdateEntitySchema = CreateEntitySchema.partial();

export type CreateEntityInput = z.infer<typeof CreateEntitySchema>;
export type UpdateEntityInput = z.infer<typeof UpdateEntitySchema>;
```

**Validation Rules:**

- Email: `.email().toLowerCase()`
- URLs: `.url()`
- Numbers: `.positive()` or `.min(0)`
- Strings: always `.min()` and `.max()`
- Enums: validate against `pgEnum` values
- Complex logic: use `.refine()` or `.superRefine()`

---

### Server Actions Pattern

Location: `src/actions/${entity}.actions.ts`

```typescript
"use server";

import { auth } from "@/auth";
import { entityDal } from "@/dal/${entity}-dal";
import {
  CreateEntitySchema,
  UpdateEntitySchema
} from "@/schemas/${entity}.schema";
import { revalidatePath } from "next/cache";

type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

export async function getEntityAction(
  id: number
): Promise<ActionResult<Entity>> {
  try {
    const entity = await entityDal.getById(id);
    if (!entity) return { ok: false, error: "Entity not found" };
    return { ok: true, data: entity };
  } catch (error) {
    console.error("[getEntityAction]", error);
    return { ok: false, error: "Failed to fetch entity" };
  }
}

export async function createEntityAction(
  input: unknown
): Promise<ActionResult<Entity>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in" };
  }

  const parsed = CreateEntitySchema.safeParse(input);
  if (!parsed.success) {
    const [error] = parsed.error.errors;
    return { ok: false, error: error?.message ?? "Invalid input" };
  }

  try {
    const entity = await entityDal.create({
      ...parsed.data,
      userId: session.user.id
    });

    revalidatePath("/entities");
    return { ok: true, data: entity };
  } catch (error) {
    console.error("[createEntityAction]", error);
    return { ok: false, error: "Failed to create entity" };
  }
}

export async function updateEntityAction(
  id: number,
  input: unknown
): Promise<ActionResult<Entity>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in" };
  }

  const parsed = UpdateEntitySchema.safeParse(input);
  if (!parsed.success) {
    return { ok: false, error: "Invalid input" };
  }

  try {
    const entity = await entityDal.getById(id);
    if (!entity) return { ok: false, error: "Entity not found" };
    if (entity.userId !== session.user.id) {
      return { ok: false, error: "Unauthorized" };
    }

    const updated = await entityDal.update(id, parsed.data);
    if (!updated) return { ok: false, error: "Update failed" };

    revalidatePath("/entities");
    return { ok: true, data: updated };
  } catch (error) {
    console.error("[updateEntityAction]", error);
    return { ok: false, error: "Failed to update entity" };
  }
}

export async function deleteEntityAction(
  id: number
): Promise<ActionResult<void>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "You must be signed in" };
  }

  try {
    const entity = await entityDal.getById(id);
    if (!entity) return { ok: false, error: "Entity not found" };
    if (entity.userId !== session.user.id) {
      return { ok: false, error: "Unauthorized" };
    }

    await entityDal.delete(id);
    revalidatePath("/entities");
    return { ok: true, data: undefined };
  } catch (error) {
    console.error("[deleteEntityAction]", error);
    return { ok: false, error: "Failed to delete entity" };
  }
}
```

**Action Patterns:**

- Always validate input with Zod
- Check auth on mutations (create, update, delete)
- Check ownership for user-specific resources
- Use consistent return shape: `{ ok, data, error }`
- Call `revalidatePath()` after mutations
- Log errors server-side, return user-friendly messages

---

### React Component Patterns

#### Display Component

```typescript
interface EntityCardProps {
  data: Entity;
  onEdit?: (id: number) => void;
  onDelete?: (id: number) => void;
}

export function EntityCard({
  data,
  onEdit,
  onDelete,
}: EntityCardProps) {
  return (
    <div className="rounded-lg border p-4 space-y-4">
      <div>
        <h3 className="font-semibold text-lg">{data.title}</h3>
        <p className="text-sm text-muted-foreground">{data.description}</p>
      </div>

      <div className="flex gap-2 pt-2">
        {onEdit && (
          <button
            onClick={() => onEdit(data.id)}
            className="px-3 py-2 text-sm bg-primary text-primary-foreground rounded hover:opacity-90"
          >
            Edit
          </button>
        )}
        {onDelete && (
          <button
            onClick={() => onDelete(data.id)}
            className="px-3 py-2 text-sm bg-destructive text-destructive-foreground rounded hover:opacity-90"
          >
            Delete
          </button>
        )}
      </div>
    </div>
  );
}
```

#### Form Component

```typescript
"use client";

import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { CreateEntitySchema } from "@/schemas/entity.schema";
import { createEntityAction } from "@/actions/entity.actions";
import { useState } from "react";

export function EntityForm() {
  const [error, setError] = useState<string | null>(null);
  const form = useForm({
    resolver: zodResolver(CreateEntitySchema),
    defaultValues: {
      title: "",
      description: "",
      status: "draft",
    },
  });

  const onSubmit = async (data: unknown) => {
    setError(null);
    const result = await createEntityAction(data);

    if (!result.ok) {
      setError(result.error);
      return;
    }

    form.reset();
    // Show success toast
  };

  return (
    <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
      {error && (
        <div className="p-3 bg-destructive/10 text-destructive rounded-md text-sm">
          {error}
        </div>
      )}

      {/* Form fields go here */}

      <button
        type="submit"
        disabled={form.formState.isSubmitting}
        className="w-full px-4 py-2 bg-primary text-primary-foreground rounded"
      >
        {form.formState.isSubmitting ? "Saving..." : "Create"}
      </button>
    </form>
  );
}
```

---

### Implementation Workflow

#### Step 1: Search & Document (10 min)

- Search for existing similar implementations
- Document patterns found (DAL, validation, components)
- Ask clarifying questions about requirements
- Create `docs/proposedFixes.md` with findings

#### Step 2: Design Database (15 min)

- Propose table schema with relationships
- Define enums and indexes
- Detail cascade behavior and constraints

#### Step 3: Implement Database (5 min)

- Add table to `src/database/schema.ts`
- Run `pnpm db:generate` (creates migration)
- Run `pnpm db:push` (applies schema)

#### Step 4: Implement DAL (10 min)

- Create `src/dal/${entity}-dal.ts`
- Extend `BaseDal<T>`
- Implement all CRUD + custom methods

#### Step 5: Create Validation (5 min)

- Create `src/schemas/${entity}.schema.ts`
- Define Create and Update versions
- Test with sample data

#### Step 6: Implement Actions (10 min)

- Create `src/actions/${entity}.actions.ts`
- Implement all CRUD actions
- Include auth checks, validation, error handling

#### Step 7: Build Components (20 min)

- Create display components (Card, List)
- Create form component for CRUD
- Add loading states and error handling

#### Step 8: Create Page (10 min)

- Create `src/app/(root)/${entity}s/page.tsx`
- Use Server Component for data fetching
- Use Client Components for interactivity
- Add Suspense boundaries

#### Step 9: Test & Validate (10 min)

```bash
pnpm run type-check
pnpm run lint:fix
pnpm test
pnpm run build --debug-prerender
```

#### Step 10: Code Review Checklist

- [ ] TypeScript: No `any` types
- [ ] Security: Auth checks, input validation
- [ ] Performance: Indexes on queries, no N+1
- [ ] Testing: Unit tests written, 80%+ coverage
- [ ] Documentation: Comments on complex logic
- [ ] Accessibility: ARIA labels, semantic HTML
- [ ] Styling: Responsive, Tailwind conventions

---
