# 11. React Query Keys (`src/lib/query-client.ts`)

> Extracted from `setup.prompt.md`.

## 11. React Query Keys (`src/lib/query-client.ts`)

```typescript
export const queryKeys = {
  comics: {
    all: ["comics"],
    list: (filters: Record<string, unknown>) => [
      "comics",
      "list",
      filters
    ],
    detail: (slug: string) => ["comics", "detail", slug],
    chapters: (comicId: string) => ["comics", comicId, "chapters"]
  },
  bookmarks: {
    all: ["bookmarks"],
    list: (userId: string) => ["bookmarks", "list", userId],
    check: (userId: string, comicId: string) => [
      "bookmarks",
      "check",
      userId,
      comicId
    ]
  },
  readingProgress: {
    /* ... */
  },
  users: {
    /* ... */
  },
  search: {
    /* ... */
  },
  genres: { all: ["genres"] },
  authors: { all: ["authors"] }
};
```

- **Server**: new `QueryClient` per request
- **Browser**: singleton with `staleTime: 60s`, `gcTime: 5min`, retry 3 exponential backoff

---
