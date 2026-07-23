# 4. 🔧 DRY Implementation Practices

> Extracted from `setup-enhanced.prompt.md` for DRY templating.

## 4. 🔧 DRY Implementation Practices

Every piece of logic should exist in exactly one place. When implementing features, leverage existing abstractions and extend rather than duplicate.

### Strategy 1: DAL Classes — Parameterized Query Methods

Instead of creating separate methods for each query variation, use a single parameterized method with filter options. See `docs/dev.content.md` Section 7 for the complete `BaseDal<T>` pattern and examples.

```
❌ Separate methods: getByType(), getByStatus(), getByRating()
✅ Single method: listWithFilters(filters: QueryFilters)
```

### Strategy 2: Server Actions — Standardized `ActionResult<T>`

All server actions follow the same structure: `auth → validate → DAL → revalidate → result`. See `docs/dev.content.md` Section 9 for the complete pattern with error handling.

```
type ActionResult<T> = { ok: true; data: T } | { ok: false; error: string }
```

### Strategy 3: Zod Schemas — Extract & Reuse Common Validations

Share field-level validations across create/update schemas. See `docs/dev.content.md` Section 8 for Zod schema composition patterns.

```
❌ Duplicating: z.string().min(1).max(255) in both create and update schemas
✅ Extracting: const titleSchema = z.string().min(1).max(255), then reuse
```

### Strategy 4: React Components — Compose from Primitives

Build page-level components by composing shadcn/ui primitives and existing domain components. See `docs/dev.content.md` Section 12 for component composition patterns.

### Cross-Cutting Concerns (Single Source of Truth)

| Concern | Single Source | Usage Pattern |
| --- | --- | --- |
| **Types** | `z.infer<typeof schema>` | Import from schema only, never redefine |
| **Validation** | Zod schema in `src/schemas/` | Single import, reuse everywhere |
| **DB Access** | Specific DAL class | Never raw `db` queries in actions/pages |
| **Error Handling** | `ActionResult<T>` pattern | Same structure for all actions |
| **Timestamps** | Drizzle `.$onUpdate()` | Auto-updates `updatedAt` column |
| **Auth Checks** | `await auth()` helper | First call in every protected action |
| **Cache Invalidation** | `revalidatePath()` | After every mutation |

### Reference-Driven Development Workflow

1. **Search** — Find existing patterns: `grep -r "extends BaseDal" src/dal/`
2. **Understand** — Read the base class, extract only what your entity needs
3. **Compose** — Extend base classes, import types from schemas, build UI from primitives
4. **Validate** — `pnpm type-check && pnpm lint:fix && pnpm test`

---
