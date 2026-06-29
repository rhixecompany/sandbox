# Phase 10: Admin Pages (20 new files)

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Phase 10: Admin Pages (20 new files)

### Admin Route Structure

```
src/app/admin/
├── page.tsx                    (dashboard)
├── layout.tsx                  (Phase 5.3 — done)
├── comics/
│   ├── page.tsx
│   ├── [id]/
│   │   └── page.tsx
│   └── new/
│       └── page.tsx
├── users/
│   ├── page.tsx
│   └── [id]/
│       └── page.tsx
├── genres/
│   └── page.tsx
├── artists/
│   └── page.tsx
├── authors/
│   └── page.tsx
├── chapters/
│   ├── page.tsx
│   └── [id]/
│       └── page.tsx
└── types/
    └── page.tsx
```

### 10.1 — `src/app/admin/page.tsx` (Dashboard)

```tsx
import { db } from "@/database/db";
import { comic, user, chapter, comment } from "@/database/schema";
import { sql } from "drizzle-orm";

async function getMetrics() {
  const [comicCount] = await db
    .select({ count: sql<number>`count(*)` })
    .from(comic);
  const [userCount] = await db
    .select({ count: sql<number>`count(*)` })
    .from(user);
  const [chapterCount] = await db
    .select({ count: sql<number>`count(*)` })
    .from(chapter);
  const [commentCount] = await db
    .select({ count: sql<number>`count(*)` })
    .from(comment);
  return { comicCount, userCount, chapterCount, commentCount };
}

export default async function AdminDashboardPage() {
  const { comicCount, userCount, chapterCount, commentCount } =
    await getMetrics();
  const metrics = [
    { label: "Comics", value: comicCount?.count ?? 0 },
    { label: "Users", value: userCount?.count ?? 0 },
    { label: "Chapters", value: chapterCount?.count ?? 0 },
    { label: "Comments", value: commentCount?.count ?? 0 }
  ];
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Dashboard</h1>
      <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
        {metrics.map(m => (
          <div key={m.label} className="rounded-lg border p-4">
            <p className="text-sm text-muted-foreground">{m.label}</p>
            <p className="text-3xl font-bold">{m.value}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

### 10.2 — `src/app/admin/comics/page.tsx`

```tsx
import { comicDal } from "@/dal/comic-dal";
import { DataTable } from "@/components/ui/data-table";
import Link from "next/link";
import { Button } from "@/components/ui/button";

export default async function AdminComicsPage() {
  const comics = await comicDal.list({ limit: 50 });
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <h1 className="text-2xl font-bold">Comics</h1>
        <Button asChild>
          <Link href="/admin/comics/new">Add Comic</Link>
        </Button>
      </div>
      <DataTable
        data={comics}
        keyExtractor={c => c.id}
        columns={[
          { key: "id", header: "ID" },
          {
            key: "title",
            header: "Title",
            render: c => (
              <Link
                href={`/admin/comics/${c.id}`}
                className="hover:underline"
              >
                {c.title}
              </Link>
            )
          },
          { key: "status", header: "Status" },
          {
            key: "createdAt",
            header: "Created",
            render: c => c.createdAt?.toLocaleDateString() ?? ""
          }
        ]}
      />
    </div>
  );
}
```

### 10.3 — `src/app/admin/users/page.tsx`

```tsx
import { userDal } from "@/dal/user-dal";
import { DataTable } from "@/components/ui/data-table";

export default async function AdminUsersPage() {
  const users = await userDal.list({ limit: 50 });
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Users</h1>
      <DataTable
        data={users}
        keyExtractor={u => u.id}
        columns={[
          {
            key: "id",
            header: "ID",
            render: u => u.id.slice(0, 8) + "…"
          },
          { key: "name", header: "Name" },
          { key: "email", header: "Email" },
          { key: "role", header: "Role" },
          {
            key: "createdAt",
            header: "Joined",
            render: u => u.createdAt?.toLocaleDateString() ?? ""
          }
        ]}
      />
    </div>
  );
}
```

### 10.4 — `src/app/admin/genres/page.tsx`

```tsx
import { genreDal } from "@/dal/genre-dal";
import { DataTable } from "@/components/ui/data-table";

export default async function AdminGenresPage() {
  const genres = await genreDal.list({ limit: 100 });
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Genres</h1>
      <DataTable
        data={genres}
        keyExtractor={g => g.id}
        columns={[
          { key: "id", header: "ID" },
          { key: "name", header: "Name" },
          { key: "slug", header: "Slug" }
        ]}
      />
    </div>
  );
}
```

### 10.5 — `src/app/admin/artists/page.tsx`

```tsx
import { artistDal } from "@/dal/artist-dal";
import { DataTable } from "@/components/ui/data-table";

export default async function AdminArtistsPage() {
  const artists = await artistDal.list({ limit: 50 });
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Artists</h1>
      <DataTable
        data={artists}
        keyExtractor={a => a.id}
        columns={[
          { key: "id", header: "ID" },
          { key: "name", header: "Name" }
        ]}
      />
    </div>
  );
}
```

### 10.6 — `src/app/admin/authors/page.tsx`

```tsx
import { authorDal } from "@/dal/author-dal";
import { DataTable } from "@/components/ui/data-table";

export default async function AdminAuthorsPage() {
  const authors = await authorDal.list({ limit: 50 });
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Authors</h1>
      <DataTable
        data={authors}
        keyExtractor={a => a.id}
        columns={[
          { key: "id", header: "ID" },
          { key: "name", header: "Name" }
        ]}
      />
    </div>
  );
}
```

### 10.7 — `src/app/admin/chapters/page.tsx`

```tsx
import { chapterDal } from "@/dal/chapter-dal";
import { DataTable } from "@/components/ui/data-table";

export default async function AdminChaptersPage() {
  const chapters = await chapterDal.list({ limit: 50 });
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Chapters</h1>
      <DataTable
        data={chapters}
        keyExtractor={c => c.id}
        columns={[
          { key: "id", header: "ID" },
          { key: "title", header: "Title" },
          { key: "chapterNumber", header: "Chapter #" },
          { key: "comicId", header: "Comic ID" }
        ]}
      />
    </div>
  );
}
```

### 10.8 — `src/app/admin/types/page.tsx`

```tsx
import { typeDal } from "@/dal/type-dal";
import { DataTable } from "@/components/ui/data-table";

export default async function AdminTypesPage() {
  const types = await typeDal.list({ limit: 50 });
  return (
    <div>
      <h1 className="mb-6 text-2xl font-bold">Comic Types</h1>
      <DataTable
        data={types}
        keyExtractor={t => t.id}
        columns={[
          { key: "id", header: "ID" },
          { key: "name", header: "Name" }
        ]}
      />
    </div>
  );
}
```

---
