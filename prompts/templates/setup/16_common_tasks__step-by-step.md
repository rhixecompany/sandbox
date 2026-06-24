# 16. Common Tasks — Step-by-Step

> Extracted from `setup.prompt.md`.

## 16. Common Tasks — Step-by-Step

### Feature Discovery Checklist

Before implementing any feature, answer these questions:

1. **What entity/entities are involved?** → Check `schema.ts` for existing tables
2. **What relationships exist?** → Check FK references + junction tables (remember: no `relations()` — see §6)
3. **What validation rules apply?** → Define/check Zod schemas (separate create + update schemas)
4. **What auth level is required?** → Public, authenticated, admin, or role-based?
5. **What cache paths need invalidation?** → List all `revalidatePath()` targets
6. **Does a DAL already exist?** → Check `src/dal/` for existing implementations (18 DAL files)
7. **Are there composite keys?** → Override BaseDal methods to redirect (e.g., `"Use getUserRating(userId, comicId) instead"`)
8. **What tests are needed?** → Unit (mock DB/auth), integration (real DB), E2E (Playwright)

### Add a New Page

1. Create `src/app/(root)/my-feature/page.tsx` (Server Component by default)
2. Fetch data via DAL in the component body
3. Add `loading.tsx` and `error.tsx` in the same directory
4. Add navigation link in `src/components/layout/app-sidebar.tsx`
5. Add metadata via `export const metadata` or `generateMetadata()`

### Add a New Database Table

1. Define table in `src/database/schema.ts` with proper types, FKs (`onDelete: "cascade"`), indexes
2. Add `relations()` if the table has complex relationships (see §6 warning)
3. Run `pnpm db:push` (dev) or `pnpm db:generate` + `pnpm db:migrate` (prod)
4. Create DAL: `src/dal/my-table-dal.ts` extending `BaseDal<typeof myTable.$inferSelect>`
5. Create Zod schema: `src/schemas/my-table.schema.ts`
6. Create Server Actions: `src/actions/my-table.actions.ts`

### Add Authentication to a Page

```typescript
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function ProtectedPage() {
  const session = await auth();
  if (!session?.user) redirect("/auth/signin");
  return <div>Protected content</div>;
}
```

### Create a Server Action

1. Create `src/actions/my-feature.actions.ts` with `"use server"` directive
2. Check `auth()` → validate with Zod → call DAL → `revalidatePath()` → return `ActionResult<T>`
3. Never throw — always return `{ ok: false, error }` for failures

### Create a Client Component

1. Add `"use client"` at file top
2. Use hooks: `useState`, `useEffect`, event handlers, browser APIs
3. Do NOT use `useMemo`/`useCallback`/`memo` — React Compiler handles this
4. Use `useCurrentYear()` instead of `new Date()` for SSR safety

---
