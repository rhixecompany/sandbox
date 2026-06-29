# Phase 5: Route Layouts (3 new files)

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Phase 5: Route Layouts (3 new files)

### 5.1 — `src/app/(root)/layout.tsx`

```tsx
import { auth } from "@/auth";
import { AppSidebar } from "@/components/layout/app-sidebar";
import {
  SidebarProvider,
  SidebarInset
} from "@/components/ui/sidebar";

export default async function RootLayout({
  children
}: {
  children: React.ReactNode;
}) {
  const session = await auth();
  return (
    <SidebarProvider>
      <AppSidebar session={session} />
      <SidebarInset>
        <main className="flex flex-1 flex-col gap-4 p-4">
          {children}
        </main>
      </SidebarInset>
    </SidebarProvider>
  );
}
```

### 5.2 — `src/app/(auth)/layout.tsx`

```tsx
export default function AuthLayout({
  children
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background">
      <div className="w-full max-w-md px-4">{children}</div>
    </div>
  );
}
```

### 5.3 — `src/app/admin/layout.tsx`

```tsx
import { auth } from "@/auth";
import { redirect } from "next/navigation";

export default async function AdminLayout({
  children
}: {
  children: React.ReactNode;
}) {
  const session = await auth();
  if (!session?.user) redirect("/auth/signin");
  const u = session.user as { role?: unknown };
  if (typeof u.role !== "string" || u.role !== "admin") redirect("/");
  return (
    <div className="flex min-h-screen flex-col">
      <header className="border-b px-6 py-3">
        <span className="text-lg font-semibold">ComicWise Admin</span>
      </header>
      <main className="flex-1 p-6">{children}</main>
    </div>
  );
}
```

---
