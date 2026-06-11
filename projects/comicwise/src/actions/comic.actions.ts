/**
 * Comic-related Server Actions
 * Handles fetching, filtering, and managing comic data
 */

"use server";

import { and, desc, eq, ilike, sql, type SQL } from "drizzle-orm";

import { db } from "@/database/db";
import { chapter, comic } from "@/database/schema";

import type { ComicFilter } from "@/schemas/comic.schema";
import type { ActionResult } from "@/types/actions-types";

/**
 * Get paginated list of comics with optional filters
 */
export async function getComicsListAction(
  filter: ComicFilter
): Promise<ActionResult<{ comics: unknown[]; total: number }>> {
  try {
    const offset = ((filter.page ?? 1) - 1) * (filter.limit ?? 20);
    const limit = filter.limit ?? 20;

    // Build where conditions
    const conditions: SQL[] = [];

    if (filter.query) {
      conditions.push(ilike(comic.title, `%${filter.query}%`));
    }

    if (filter.status) {
      // Convert lowercase status to database enum value
      const statusMap: Record<string, string> = {
        ongoing: "Ongoing",
        completed: "Completed",
        hiatus: "Hiatus",
      };
      const dbStatus = statusMap[filter.status] ?? filter.status;
      conditions.push(
        eq(comic.status, dbStatus as "Coming Soon" | "Completed" | "Dropped" | "Hiatus" | "Ongoing" | "Season End")
      );
    }

    const whereCondition = conditions.length > 0 ? and(...conditions) : undefined;

    // Get total count
    const countResult = await db
      .select({ count: sql<number>`COUNT(*)` })
      .from(comic)
      .where(whereCondition);

    const total = countResult[0]?.count ?? 0;

    // Get paginated comics
    const comics = await db
      .select()
      .from(comic)
      .where(whereCondition)
      .orderBy(desc(comic.updatedAt))
      .limit(limit)
      .offset(offset);

    return { ok: true, data: { comics, total } };
  } catch (error) {
    console.error("[getComicsListAction]", error);
    return { ok: false, error: "Failed to fetch comics" };
  }
}

/**
 * Get a single comic by slug with all related information
 */
export async function getComicBySlugAction(slug: string): Promise<ActionResult<null | Record<string, unknown>>> {
  try {
    if (!slug) {
      return { ok: false, error: "Slug is required" };
    }

    const result = await db.query.comic.findFirst({
      where: eq(comic.slug, slug),
      with: {
        author: true,
        artist: true,
        genres: {
          with: {
            genre: true,
          },
        },
        chapters: {
          orderBy: desc(chapter.releaseDate),
          limit: 50,
        },
      },
    });

    if (!result) {
      return { ok: true, data: null };
    }

    return { ok: true, data: result };
  } catch (error) {
    console.error("[getComicBySlugAction]", error);
    return { ok: false, error: "Failed to fetch comic details" };
  }
}

/**
 * Get related comics based on shared genres
 */
export async function getRelatedComicsAction(
  comicId: number,
  limit: number = 6
): Promise<ActionResult<Record<string, unknown>[]>> {
  try {
    if (!comicId) {
      return { ok: false, error: "Comic ID is required" };
    }

    const relatedComics = await db
      .select()
      .from(comic)
      .where(sql`${comic.id} != ${Number(comicId)}`)
      .orderBy(desc(comic.rating))
      .limit(limit);

    return { ok: true, data: relatedComics };
  } catch (error) {
    console.error("[getRelatedComicsAction]", error);
    return { ok: false, error: "Failed to fetch related comics" };
  }
}

/**
 * Get featured/trending comics for homepage
 */
export async function getFeaturedComicsAction(limit: number = 12): Promise<ActionResult<Record<string, unknown>[]>> {
  try {
    const featuredComics = await db.select().from(comic).orderBy(desc(comic.rating)).limit(limit);

    return { ok: true, data: featuredComics };
  } catch (error) {
    console.error("[getFeaturedComicsAction]", error);
    return { ok: false, error: "Failed to fetch featured comics" };
  }
}

/**
 * Get new/recent comics for homepage
 */
export async function getNewComicsAction(limit: number = 12): Promise<ActionResult<Record<string, unknown>[]>> {
  try {
    const newComics = await db.select().from(comic).orderBy(desc(comic.createdAt)).limit(limit);

    return { ok: true, data: newComics };
  } catch (error) {
    console.error("[getNewComicsAction]", error);
    return { ok: false, error: "Failed to fetch new comics" };
  }
}
