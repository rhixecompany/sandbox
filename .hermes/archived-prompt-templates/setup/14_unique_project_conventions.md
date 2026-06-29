# 14. Unique Project Conventions

> Extracted from `setup.prompt.md`.

## 14. Unique Project Conventions

### React Compiler is ON

**Do NOT** manually add `useMemo`, `useCallback`, or `memo()`. The React Compiler handles memoization automatically. Adding manual memoization will conflict.

> **⚠ Conflict note:** `.github/instructions/performance.instructions.md` says "Use `React.memo` for expensive components" — this directly contradicts the React Compiler rule. **This setup prompt is authoritative.** `memo()`, `useMemo`, `useCallback` are all forbidden. The performance instructions file needs updating.

### Next.js 16 `searchParams` is a Promise

In Next.js 16, `searchParams` must be `await`ed:

```typescript
// ❌ WRONG (Next.js 15 pattern)
export default function Page({
  searchParams
}: {
  searchParams: { page?: string };
}) {
  const page = searchParams.page;
}

// ✅ CORRECT (Next.js 16)
export default async function Page({
  searchParams
}: {
  searchParams: Promise<{ page?: string }>;
}) {
  const params = await searchParams;
  const page = params.page;
}
```

### Next.js App Router Rules

From `.github/instructions/nextjs.instructions.md`:

- Every route directory needs `loading.tsx` + `error.tsx`
- Never access `Date.now()`, `localStorage`, `window`, `document` in Server Components
- Use Next.js `<Image>` for all images — never raw `<img>`
- Use `next/font` for all fonts — never manual `@font-face`
- Prefer static generation over SSR when possible
- All code must be Turbopack-compatible

### SSR-Safe Date Handling

```typescript
// WRONG in Server Component or shared code
const year = new Date().getFullYear();

// CORRECT — use SSR-safe hook
("use client");
import { useCurrentYear } from "@/hooks/use-now";
const year = useCurrentYear(); // null during SSR, number after hydration
```

### Error Handling with `cause`

```typescript
// Pattern used in src/lib/env.ts
throw new Error(`Validation failed:\n${errors}`, {
  cause: originalError
});
```

### Force-Dynamic Ban

Never use `export const dynamic = "force-dynamic"` at page level. Use `<Suspense>` boundaries or small `"use client"` wrappers instead.

### Zustand Store Pattern

```typescript
"use client";
import { create } from "zustand";
import { devtools, persist } from "zustand/middleware";

export const useMyStore = create<State>()(
  devtools(
    persist(
      set => ({
        /* initial state + actions */
      }),
      { name: "store-name" }
    ),
    { name: "MyStore" }
  )
);
```

### Tailwind Conventions

- Container queries: `@container/card`, `@[540px]/card:hidden`
- Important modifier: `h-4!` (not `!h-4`)
- Class ordering follows Tailwind Merge conventions

### Charts (Recharts)

`ResponsiveContainer` must be guarded with `isMounted` state — see `src/components/ui/chart.tsx`.

### Security Rules

From `.github/instructions/security.instructions.md`:

- Validate on both client AND server
- Never string-concatenate DB queries — always use Drizzle query builders
- Rate limiting for API routes
- Never expose stack traces in production
- Escape user-generated content (XSS prevention)
- Don't store sensitive data in `localStorage` / `sessionStorage`

---
