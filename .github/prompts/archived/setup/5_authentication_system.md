# 5. Authentication System

> Extracted from `setup.prompt.md`.

## 5. Authentication System

### Architecture (4 modular files)

```
src/auth.ts             → NextAuth({ ...authConfig })  → exports { handlers, auth, signIn, signOut }
src/auth-config.ts      → session strategy, callbacks (session, jwt, signIn, redirect)
src/auth-providers.ts   → [GitHub, Credentials, Keycloak] provider array
src/auth-adapter.ts     → DrizzleAdapter(db, { usersTable, accountsTable, ... })
```

> **Note:** Auth files (`auth-config.ts`, `auth-providers.ts`, `db.ts`) use raw `process.env` as a known exception — they load before app initialization. Do not follow this pattern elsewhere.

### Session Strategy

- **Database sessions** (not JWT) — `strategy: "database"`, `maxAge: 30 days`, `updateAge: 1 day`
- Session stored in `session` table, linked to `user` via `userId`

### Credentials Provider (`src/auth-providers.ts`)

```typescript
async authorize(
  credentials: Partial<Record<"username" | "password", unknown>>
): Promise<User | null> {
  const username = typeof credentials.username === "string" ? credentials.username : undefined;
  const password = typeof credentials.password === "string" ? credentials.password : undefined;
  if (!username || !password) return null;

  const user = await getUserByUsername(username);      // src/actions/auth-db.ts
  if (user?.passwordHash && (await verifyPassword(password, user.passwordHash))) return user;
  return null;
}
```

### DB Lookup & Password Verification (`src/actions/auth-db.ts`)

```typescript
import bcrypt from "bcryptjs";
import { eq } from "drizzle-orm";
import { db } from "../database/db";
import { user as userTable } from "../database/schema";

export async function getUserByUsername(
  username: string
): Promise<User | null> {
  const result = await db
    .select()
    .from(userTable)
    .where(eq(userTable.name, username));
  if (!result[0]) return null;
  return {
    id: result[0].id,
    name: result[0].name ?? undefined,
    email: result[0].email,
    role: result[0].role,
    passwordHash: result[0].password ?? undefined
  };
}

export async function verifyPassword(
  plain: string,
  hash: string
): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}
```

### Server-Side Usage

```typescript
// Server Component or Server Action
import { auth } from "@/auth";
const session = await auth();
if (!session?.user) redirect("/auth/signin");

// Check admin role
const u = session.user as { role?: unknown };
const isAdmin = typeof u?.role === "string" && u.role === "admin";
```

### Client-Side Usage

```typescript
// Client Component — read session
import { useSession } from "next-auth/react";
const { data: session } = useSession();

// Client Component — OAuth sign-in
import { signIn } from "next-auth/react";
await signIn("github", { redirectTo: "/dashboard" });

// Client Component — Credentials sign-in (no redirect, handle in-page)
const result = await signIn("credentials", {
  username: "user",
  password: "pass",
  redirect: false
});
if (result?.error) showError(result.error);
```

### Auth API Route (`src/app/api/auth/[...nextauth]/route.ts`)

```typescript
export { GET, POST } from "@/auth";
```

### Known Bugs

- `auth-config.ts` `signIn` callback: currently blocks users without email — may need adjustment for OAuth-only providers
- `redirect` callback: falls back to `/dashboard` for external URLs — should respect original intent

---
