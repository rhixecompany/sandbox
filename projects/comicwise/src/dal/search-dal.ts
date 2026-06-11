/**
 * SearchDAL - Full-Text Search Data Access Layer
 * Pattern: Section 22.4 - ilike() for substring matching with pagination
 *
 * Implements case-insensitive searching across comic title, description, and author names.
 * Single query with proper eager loading to prevent N+1 problems.
 */

import { and, count, eq, ilike, or, type SQL } from "drizzle-orm";

import { db } from "@/database/db";
import { comic } from "@/database/schema";

type ComicType = typeof comic.$inferSelect;

export interface SearchOptions {
  artistId?: number;
  authorId?: number;
  genreId?: number;
  limit?: number;
  offset?: number;
  query: string;
  status?: string;
  typeId?: number;
}

export interface SearchResult {
  items: Array<
    ComicType & {
      artist: { id: number; name: string } | null;
      author: { id: number; name: string } | null;
      genres: Array<{ id: number; name: string }>;
      type: { id: number; name: string } | null;
    }
  >;
  page: number;
  pageSize: number;
  total: number;
}

/**
 * Search DAL for full-text search queries
 * Uses ilike() for case-insensitive substring matching
 * Implements pagination for efficient result loading
 */
export class SearchDAL {
  /**
   * Search comics by query with optional filters
   * Pattern: Section 22.4 - ilike() with WHERE conditions
   *
   * @param options - Search options including query, filters, and pagination
   * @returns SearchResult with items, total count, and pagination info
   */
  async searchComics(options: SearchOptions): Promise<SearchResult> {
    const { query, limit = 20, offset = 0, authorId, artistId, typeId, status } = options;

    // Cap limit to 100 for performance
    const cappedLimit = Math.min(limit, 100);

    try {
      // Build search condition - search in title and description
      const searchCondition = or(ilike(comic.title, `%${query}%`), ilike(comic.description, `%${query}%`));

      // Build filter conditions
      const filterConditions: Array<SQL> = [];
      if (authorId) filterConditions.push(eq(comic.authorId, authorId));
      if (artistId) filterConditions.push(eq(comic.artistId, artistId));
      if (typeId) filterConditions.push(eq(comic.typeId, typeId));
      if (
        status &&
        (["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"] as readonly string[]).includes(
          status
        )
      ) {
        filterConditions.push(
          eq(comic.status, status as "Coming Soon" | "Completed" | "Dropped" | "Hiatus" | "Ongoing" | "Season End")
        );
      }

      // Combine all conditions
      const allConditions = filterConditions.length > 0 ? and(searchCondition, ...filterConditions) : searchCondition;

      // Get total count for pagination
      const countResult = await db.select({ count: count() }).from(comic).where(allConditions);

      const total = countResult[0]?.count || 0;

      // Get paginated results with eager loading
      const items = await db.query.comic.findMany({
        where: allConditions,
        with: {
          author: {
            columns: { id: true, name: true },
          },
          artist: {
            columns: { id: true, name: true },
          },
          genres: {
            with: {
              genre: {
                columns: { id: true, name: true },
              },
            },
          },
          comicType: {
            columns: { id: true, name: true },
          },
        },
        limit: cappedLimit,
        offset,
        orderBy: (comic, { desc }) => [desc(comic.createdAt)],
      });

      // Transform results to match SearchResult interface
      const transformedItems = (items ?? []).map((item) => ({
        ...item,
        genres: ((item.genres ?? []) as Array<{ genre: { id: number; name: string } }>).map((g) => g.genre),
        type: item.comicType,
      }));

      return {
        items: transformedItems,
        total,
        page: Math.floor(offset / cappedLimit),
        pageSize: cappedLimit,
      };
    } catch (error) {
      console.error("Search error:", error);
      throw error;
    }
  }
}

export const searchDal = new SearchDAL();
