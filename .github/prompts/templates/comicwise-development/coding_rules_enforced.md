# Coding Rules (Enforced)

> Extracted from `comicwise-development.prompt.md`.

## Coding Rules (Enforced)

### Type Safety & Code Quality

1. **No `any` types** — ESLint: `no-explicit-any: "error"`
2. **No manual memoization** — React Compiler is ON (`useMemo`/`useCallback`/`memo()` forbidden)
3. **No raw `process.env`** — Use `getEnv()` from `src/lib/env.ts`
4. **No N+1 queries** — Always use `.with()` for eager loading in DAL
5. **No API routes for mutations** — Use Server Actions (`"use server"`)
6. **No `export const dynamic = "force-dynamic"`** — Use `<Suspense>` instead

### Next.js & React

7. **Async params (v16 breaking change)** — `params` and `searchParams` are `Promise`, must `await`
8. **Server Components by default** — Only mark with `"use client"` if hooks/browser APIs needed
9. **No browser APIs in Server Components** — Never `localStorage`, `window`, `Date.now()`

### Database & Mutations

10. **ActionResult<T> pattern** — Server Actions never throw; return `{ ok, data } | { ok, error }`
11. **Auth first** — First line in every Server Action: `const session = await auth()`
12. **Zod validate** — All external input → Zod schema → DB
13. **Cascade deletes preferred** — FK: `{ onDelete: "cascade" }`. Exceptions: `comic.authorId/artistId/typeId`, `bookmark.lastReadChapterId`, `auditLog.userId` (`set null`)
14. **$inferSelect for types** — Use `typeof table.$inferSelect`, not manual types
15. **Return null not undefined** — DAL methods return `null` when not found

### UI & Styling

16. **Tailwind v4 syntax** — `bg-linear-to-br` (not `bg-gradient-to-br`), `aspect-2/3`, `h-4!`
17. **Dark mode via semantic tokens** — `bg-card`, `text-foreground`, `border-muted-foreground` (not hardcoded colors)
18. **shadcn/ui components** — Use established components; add to registry via shadcn-cli if missing
