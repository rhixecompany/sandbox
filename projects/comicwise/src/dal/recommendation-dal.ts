/**
 * Recommendation DAL (Data Access Layer)
 * Manages comic recommendations based on user's reading history
 * MVP Algorithm: Genre-based recommendations
 */

import { and, desc, eq, inArray, not, sql } from "drizzle-orm";

import { db } from "@/database/db";
import { bookmark, chapter, comic, comicToGenre, type genre } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type ComicType = typeof comic.$inferSelect;

// Type for comics with genres relation loaded
type ComicWithGenres = ComicType & {
  genres?: Array<{
    genre: typeof genre.$inferSelect;
    genreId: number;
  }>;
};

export class RecommendationDal extends BaseDal<ComicType> {
  /**
   * Get recommended comics for a user based on their reading history
   * Algorithm:
   * 1. Find genres from user's "Reading" bookmarks
   * 2. Find comics with those genres
   * 3. Filter out already bookmarked comics
   * 4. Sort by average rating DESC, then newest first
   * 5. Return top N (limit)
   */
  async getForUser(userId: string, limit: number = 10) {
    try {
      // Step 1: Get user's reading bookmarks
      const userBookmarks = await db.query.bookmark.findMany({
        where: and(eq(bookmark.userId, userId), sql`${bookmark.status} IN ('Reading', 'Completed')`),
        with: {
          comic: true,
        },
        limit: 100, // Get enough to find diverse genres
      });

      if (userBookmarks.length === 0) {
        // No reading history - return trending instead
        return this.getTrending(limit);
      }

      // Extract unique genre IDs from user's bookmarks
      const userGenreIds = new Set<number>();
      for (const bm of userBookmarks) {
        // Fetch the genres for this comic separately to avoid type inference issues
        const genres = await db.query.comicToGenre.findMany({
          where: eq(comicToGenre.comicId, bm.comicId),
        });
        for (const g of genres) {
          userGenreIds.add(g.genreId);
        }
      }

      if (userGenreIds.size === 0) {
        // No genres found - return empty array
        return [];
      }

      // Extract already-bookmarked comic IDs (to filter out)
      const bookmarkedComicIds = userBookmarks.map((b) => b.comicId);

      // Step 2-3: Find comics with user's genres, excluding already bookmarked
      const allComics: ComicWithGenres[] = await db.query.comic.findMany({
        where: not(inArray(comic.id, bookmarkedComicIds)),
        with: {
          genres: {
            with: {
              genre: true,
            },
          },
          author: true,
          artist: true,
          chapters: {
            limit: 1,
            orderBy: desc(chapter.chapterNumber),
          },
        },
        // Step 4: Sort by rating DESC, then newest first
        orderBy: [desc(comic.rating), desc(comic.createdAt)],
        // Step 5: Return top N (we'll filter by genre in memory)
        limit: limit * 3, // Get more to filter down
      });

      // Filter to only those with matching genres
      return allComics.filter((c) => c.genres && c.genres.some((cg) => userGenreIds.has(cg.genreId))).slice(0, limit);
    } catch (error) {
      console.error("[RecommendationDal.getForUser]", error);
      // Silently fail and return empty array (don't break page rendering)
      return [];
    }
  }

  /**
   * Get trending comics (highest rated)
   * Useful as fallback when no personalized recommendations available
   */
  async getTrending(limit: number = 10) {
    try {
      return db.query.comic.findMany({
        with: {
          genres: {
            with: {
              genre: true,
            },
          },
          author: true,
          artist: true,
        },
        orderBy: [sql`${comic.rating} DESC`, desc(comic.createdAt)],
        limit,
      });
    } catch (error) {
      console.error("[RecommendationDal.getTrending]", error);
      return [];
    }
  }

  /**
   * Not used for recommendations - use getForUser() instead
   */
  async getById(_id: number | string): Promise<ComicType | null> {
    throw new Error("Use getForUser(userId, limit) instead");
  }

  /**
   * Not used for recommendations
   */
  async list(_options?: DalOptions): Promise<ComicType[]> {
    throw new Error("Use getForUser(userId, limit) instead");
  }

  /**
   * Not used for recommendations
   */
  async create(_data: unknown): Promise<ComicType> {
    throw new Error("Not implemented for recommendations");
  }

  /**
   * Not used for recommendations
   */
  async update(_id: number | string, _data: unknown): Promise<ComicType> {
    throw new Error("Not implemented for recommendations");
  }

  /**
   * Not used for recommendations
   */
  async delete(_id: number | string): Promise<void> {
    throw new Error("Not implemented for recommendations");
  }
}

export const recommendationDal = new RecommendationDal();
