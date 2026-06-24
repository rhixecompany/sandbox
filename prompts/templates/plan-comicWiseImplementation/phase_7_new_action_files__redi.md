# Phase 7: New Action Files + Redis Cache (7 new files)

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Phase 7: New Action Files + Redis Cache (7 new files)

### 7.1 — `src/lib/cache/redis.ts`

```ts
import { env } from "@/lib/env";

type RedisClient = {
  get: (key: string) => Promise<string | null>;
  set: (
    key: string,
    value: string,
    options?: { ex?: number }
  ) => Promise<void>;
  del: (key: string) => Promise<void>;
};

let redisClient: RedisClient | null = null;

async function getRedis(): Promise<RedisClient | null> {
  if (!env.UPSTASH_REDIS_REST_URL || !env.UPSTASH_REDIS_REST_TOKEN)
    return null;
  if (!redisClient) {
    const { Redis } = await import("@upstash/redis");
    redisClient = new Redis({
      url: env.UPSTASH_REDIS_REST_URL,
      token: env.UPSTASH_REDIS_REST_TOKEN
    });
  }
  return redisClient;
}

export async function cacheGet<T>(key: string): Promise<T | null> {
  try {
    const redis = await getRedis();
    if (!redis) return null;
    const value = await redis.get(key);
    if (!value) return null;
    return JSON.parse(value) as T;
  } catch {
    return null; // graceful fallback
  }
}

export async function cacheSet<T>(
  key: string,
  value: T,
  ttlSeconds = 300
): Promise<void> {
  try {
    const redis = await getRedis();
    if (!redis) return;
    await redis.set(key, JSON.stringify(value), { ex: ttlSeconds });
  } catch {
    // graceful fallback — no-op
  }
}

export async function cacheDel(key: string): Promise<void> {
  try {
    const redis = await getRedis();
    if (!redis) return;
    await redis.del(key);
  } catch {
    // graceful fallback
  }
}

export const CACHE_KEYS = {
  comics: {
    list: (page: number, limit: number) =>
      `comics:list:${page}:${limit}`,
    detail: (id: number) => `comics:detail:${id}`,
    bySlug: (slug: string) => `comics:slug:${slug}`
  },
  genres: { all: () => "genres:all" },
  authors: { all: () => "authors:all" },
  artists: { all: () => "artists:all" },
  types: { all: () => "types:all" }
} as const;
```

### 7.2 — `src/actions/artist.actions.ts`

```ts
"use server";
import { auth } from "@/auth";
import { artistDal } from "@/dal/artist-dal";
import { revalidatePath } from "next/cache";
import { z } from "zod";

const ArtistSchema = z.object({
  name: z.string().min(1, "Name required").max(255),
  bio: z.string().optional(),
  imageUrl: z.string().url().optional().or(z.literal(""))
});

type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };
type ArtistType = Awaited<ReturnType<typeof artistDal.getById>>;

export async function createArtistAction(
  input: unknown
): Promise<ActionResult<NonNullable<ArtistType>>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin")
    return { ok: false, error: "Forbidden" };
  const parsed = ArtistSchema.safeParse(input);
  if (!parsed.success)
    return {
      ok: false,
      error: parsed.error.errors[0]?.message ?? "Invalid"
    };
  try {
    const artist = await artistDal.create(parsed.data);
    revalidatePath("/admin/artists");
    return { ok: true, data: artist };
  } catch (e) {
    console.error("[createArtistAction]", e);
    return { ok: false, error: "Failed to create artist" };
  }
}

export async function updateArtistAction(
  id: number,
  input: unknown
): Promise<ActionResult<NonNullable<ArtistType>>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin")
    return { ok: false, error: "Forbidden" };
  const parsed = ArtistSchema.partial().safeParse(input);
  if (!parsed.success)
    return {
      ok: false,
      error: parsed.error.errors[0]?.message ?? "Invalid"
    };
  try {
    const artist = await artistDal.update(id, parsed.data);
    if (!artist) return { ok: false, error: "Artist not found" };
    revalidatePath("/admin/artists");
    return { ok: true, data: artist };
  } catch (e) {
    console.error("[updateArtistAction]", e);
    return { ok: false, error: "Failed to update artist" };
  }
}

export async function deleteArtistAction(
  id: number
): Promise<ActionResult<void>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin")
    return { ok: false, error: "Forbidden" };
  try {
    await artistDal.delete(id);
    revalidatePath("/admin/artists");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[deleteArtistAction]", e);
    return { ok: false, error: "Failed to delete artist" };
  }
}
```

### 7.3 — `src/actions/author.actions.ts`

_(Same structure as artist.actions.ts, replace `artist` with `author`)_

### 7.4 — `src/actions/genre.actions.ts`

_(Same structure, replace with genre, use genreDal)_

### 7.5 — `src/actions/notification.actions.ts`

```ts
"use server";
import { auth } from "@/auth";
import { notificationDal } from "@/dal/notification-dal";
import { revalidatePath } from "next/cache";

type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

export async function markNotificationReadAction(
  id: number
): Promise<ActionResult<void>> {
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };
  try {
    await notificationDal.markRead(id);
    revalidatePath("/notifications");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[markNotificationReadAction]", e);
    return {
      ok: false,
      error: "Failed to mark notification as read"
    };
  }
}

export async function markAllNotificationsReadAction(): Promise<
  ActionResult<void>
> {
  const session = await auth();
  if (!session?.user?.id)
    return { ok: false, error: "Not authenticated" };
  try {
    await notificationDal.markAllRead(session.user.id);
    revalidatePath("/notifications");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[markAllNotificationsReadAction]", e);
    return {
      ok: false,
      error: "Failed to mark notifications as read"
    };
  }
}
```

### 7.6 — `src/actions/admin.actions.ts`

```ts
"use server";
import { auth } from "@/auth";
import { userDal } from "@/dal/user-dal";
import { revalidatePath } from "next/cache";
import { z } from "zod";

type ActionResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: string };

async function requireAdmin() {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") {
    throw new Error("Forbidden");
  }
  return session!;
}

const UpdateRoleSchema = z.object({
  userId: z.string().min(1),
  role: z.enum(["user", "admin", "moderator"])
});

export async function updateUserRoleAction(
  input: unknown
): Promise<ActionResult<void>> {
  try {
    await requireAdmin();
  } catch {
    return { ok: false, error: "Forbidden" };
  }
  const parsed = UpdateRoleSchema.safeParse(input);
  if (!parsed.success)
    return {
      ok: false,
      error: parsed.error.errors[0]?.message ?? "Invalid"
    };
  try {
    await userDal.updateRole(parsed.data.userId, parsed.data.role);
    revalidatePath("/admin/users");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[updateUserRoleAction]", e);
    return { ok: false, error: "Failed to update user role" };
  }
}

export async function deleteUserAction(
  userId: string
): Promise<ActionResult<void>> {
  try {
    await requireAdmin();
  } catch {
    return { ok: false, error: "Forbidden" };
  }
  try {
    await userDal.delete(userId);
    revalidatePath("/admin/users");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[deleteUserAction]", e);
    return { ok: false, error: "Failed to delete user" };
  }
}
```

---
