/**
 * Bookmark Actions
 * Server actions for managing user bookmarks
 */

"use server";

import { and, eq, sql, type SQL } from "drizzle-orm";
import { revalidatePath } from "next/cache.js";

import { auth } from "@/auth";
import { db } from "@/database/db";
import { bookmark, comic, readingProgress } from "@/database/schema";
import { bookmarkFilterSchema, bookmarkStatusEnum, updateBookmarkStatusSchema } from "@/schemas/bookmark-schema";

import type { BookmarkFilter, BookmarkStatus, UpdateBookmarkStatusInput } from "@/schemas/bookmark-schema";
import type { ActionResult } from "@/types/actions-types";

/**
 * Get user's bookmarks with pagination and filtering
 */
export async function getBookmarksAction(
  filter: BookmarkFilter
): Promise<ActionResult<{ bookmarks: unknown[]; total: number }>> {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Must be signed in" };
    }

    const parsed = bookmarkFilterSchema.safeParse(filter);
    if (!parsed.success) {
      return { ok: false, error: "Invalid filter parameters" };
    }

    const { status, search, sortBy, page, limit } = parsed.data;
    const offset = (page - 1) * limit;

    // Build where conditions
    const conditions: SQL[] = [eq(bookmark.userId, session.user.id)];

    if (status) {
      conditions.push(eq(bookmark.status, status));
    }

    // Get bookmarks with related comic data
    const baseQuery = db.query.bookmark.findMany({
      where: and(...conditions),
      with: {
        comic: {
          columns: {
            id: true,
            title: true,
            slug: true,
            description: true,
            coverImage: true,
            rating: true,
            status: true,
          },
        },
      },
      limit,
      offset,
    });

    const bookmarks = await baseQuery;

    // Apply search and sorting in JavaScript
    let filtered: unknown[] = bookmarks;
    if (search) {
      filtered = filtered.filter((bm: unknown) => {
        const item = bm as Record<string, unknown>;
        const title = (item.comic as Record<string, unknown> | undefined)?.title as string | undefined;
        return (title?.toLowerCase() || "").includes(search.toLowerCase());
      });
    }

    // Apply sorting based on sortBy parameter
    if (sortBy === "title") {
      filtered.sort((a: unknown, b: unknown) => {
        const aItem = a as Record<string, unknown>;
        const bItem = b as Record<string, unknown>;
        const aTitle = (aItem.comic as Record<string, unknown> | undefined)?.title as string | undefined;
        const bTitle = (bItem.comic as Record<string, unknown> | undefined)?.title as string | undefined;
        return (aTitle || "").localeCompare(bTitle || "");
      });
    } else if (sortBy === "progress") {
      filtered.sort((a: unknown, b: unknown) => {
        const aItem = a as Record<string, unknown>;
        const bItem = b as Record<string, unknown>;
        const aTime = aItem.updatedAt instanceof Date ? aItem.updatedAt.getTime() : 0;
        const bTime = bItem.updatedAt instanceof Date ? bItem.updatedAt.getTime() : 0;
        return bTime - aTime;
      });
    }

    // Get total count
    const countResult = await db
      .select({ count: sql<number>`count(*)` })
      .from(bookmark)
      .where(and(...conditions));

    const total = countResult[0]?.count || 0;

    return { ok: true, data: { bookmarks: filtered, total } };
  } catch (error) {
    console.error("[getBookmarksAction]", error);
    return { ok: false, error: "Failed to fetch bookmarks" };
  }
}

/**
 * Update bookmark status
 */
export async function updateBookmarkStatusAction(
  input: UpdateBookmarkStatusInput
): Promise<ActionResult<typeof bookmark.$inferSelect>> {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Must be signed in" };
    }

    const parsed = updateBookmarkStatusSchema.safeParse(input);
    if (!parsed.success) {
      return { ok: false, error: "Invalid input" };
    }

    const { comicId, status } = parsed.data;

    // Update bookmark
    const [result] = await db
      .update(bookmark)
      .set({ status, updatedAt: new Date() })
      .where(and(eq(bookmark.userId, session.user.id), eq(bookmark.comicId, comicId)))
      .returning();

    if (!result) {
      return { ok: false, error: "Bookmark not found" };
    }

    revalidatePath("/bookmarks");

    return { ok: true, data: result };
  } catch (error) {
    console.error("[updateBookmarkStatusAction]", error);
    return { ok: false, error: "Failed to update bookmark" };
  }
}

/**
 * Remove bookmark
 */
export async function removeBookmarkAction(comicId: number): Promise<ActionResult<boolean>> {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Must be signed in" };
    }

    await db.delete(bookmark).where(and(eq(bookmark.userId, session.user.id), eq(bookmark.comicId, comicId)));

    revalidatePath("/bookmarks");

    return { ok: true, data: true };
  } catch (error) {
    console.error("[removeBookmarkAction]", error);
    return { ok: false, error: "Failed to remove bookmark" };
  }
}

/**
 * Get bookmark reading progress
 */
export async function getBookmarkProgressAction(
  comicId: number
): Promise<ActionResult<{ currentChapter: null | string; progress: number }>> {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Must be signed in" };
    }

    const progress = await db.query.readingProgress.findFirst({
      where: and(eq(readingProgress.userId, session.user.id), eq(readingProgress.comicId, comicId)),
      columns: {
        progressPercent: true,
        chapterId: true,
      },
    });

    return {
      ok: true,
      data: {
        progress: progress?.progressPercent ? parseFloat(progress.progressPercent.toString()) : 0,
        currentChapter: progress?.chapterId ? `Chapter ${progress.chapterId}` : null,
      },
    };
  } catch (error) {
    console.error("[getBookmarkProgressAction]", error);
    return { ok: false, error: "Failed to fetch reading progress" };
  }
}

/**
 * Add a bookmark with a specific status (upsert)
 */
export async function addBookmarkAction(
  comicId: number,
  status: BookmarkStatus = "Reading"
): Promise<ActionResult<{ status: string }>> {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Must be signed in" };
    }

    const parsed = bookmarkStatusEnum.safeParse(status);
    if (!parsed.success) {
      return { ok: false, error: "Invalid bookmark status" };
    }

    const comicExists = await db.query.comic.findFirst({
      where: eq(comic.id, comicId),
    });

    if (!comicExists) {
      return { ok: false, error: "Comic not found" };
    }

    const [result] = await db
      .insert(bookmark)
      .values({
        userId: session.user.id,
        comicId,
        status: parsed.data,
      })
      .onConflictDoUpdate({
        target: [bookmark.userId, bookmark.comicId],
        set: { status: parsed.data, updatedAt: new Date() },
      })
      .returning();

    if (!result) {
      return { ok: false, error: "Failed to add bookmark" };
    }

    revalidatePath("/bookmarks");

    return { ok: true, data: { status: result.status } };
  } catch (error) {
    console.error("[addBookmarkAction]", error);
    return { ok: false, error: "Failed to add bookmark" };
  }
}

/**
 * Get the current bookmark status for a comic (null if not bookmarked)
 */
export async function getBookmarkStatusAction(comicId: number): Promise<ActionResult<BookmarkStatus | null>> {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: true, data: null };
    }

    const result = await db.query.bookmark.findFirst({
      where: and(eq(bookmark.userId, session.user.id), eq(bookmark.comicId, comicId)),
      columns: { status: true },
    });

    if (!result) {
      return { ok: true, data: null };
    }

    const parsed = bookmarkStatusEnum.safeParse(result.status);
    return { ok: true, data: parsed.success ? parsed.data : null };
  } catch (error) {
    console.error("[getBookmarkStatusAction]", error);
    return { ok: false, error: "Failed to get bookmark status" };
  }
}

/**
 * Get all bookmarks by status for quick stats
 */
export async function getBookmarkStatsAction(): Promise<
  ActionResult<{
    completed: number;
    dropped: number;
    onHold: number;
    planToRead: number;
    reading: number;
  }>
> {
  try {
    const session = await auth();
    if (!session?.user?.id) {
      return { ok: false, error: "Must be signed in" };
    }

    const results = await db
      .select({
        status: bookmark.status,
        count: sql<number>`count(*)`,
      })
      .from(bookmark)
      .where(eq(bookmark.userId, session.user.id))
      .groupBy(bookmark.status);

    const stats = {
      reading: 0,
      completed: 0,
      planToRead: 0,
      onHold: 0,
      dropped: 0,
    };

    for (const r of results) {
      if (r.status === "Reading") stats.reading = r.count;
      else if (r.status === "Completed") stats.completed = r.count;
      else if (r.status === "Plan to Read") stats.planToRead = r.count;
      else if (r.status === "On Hold") stats.onHold = r.count;
      else if (r.status === "Dropped") stats.dropped = r.count;
    }

    return { ok: true, data: stats };
  } catch (error) {
    console.error("[getBookmarkStatsAction]", error);
    return { ok: false, error: "Failed to fetch bookmark stats" };
  }
}
