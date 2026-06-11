/**
 * Comic DAL (Data Access Layer)
 * Manages comic CRUD operations and queries with eager loading
 */

import { and, asc, desc, count as drizzleCount, eq, ilike, inArray, ne, sql } from "drizzle-orm";

import { db } from "@/database/db";
import { chapter, comic, comicToGenre } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

export type ComicType = typeof comic.$inferSelect;

export interface ComicListOptions {
  artistId?: number;
  authorId?: number;
  genreId?: number;
  limit?: number;
  offset?: number;
  orderBy?: "latest" | "popular" | "rating" | "title";
  query?: string;
  status?: string;
  typeId?: number;
}

export interface CreateComicInput {
  artistId?: number;
  authorId?: number;
  coverImage: string;
  description: string;
  publicationDate: Date;
  serialization?: string;
  slug: string;
  status: string;
  title: string;
  typeId?: number;
  url?: string;
}

export interface UpdateComicInput {
  artistId?: number;
  authorId?: number;
  coverImage?: string;
  description?: string;
  publicationDate?: Date;
  rating?: string;
  serialization?: string;
  slug?: string;
  status?: string;
  title?: string;
  typeId?: number;
  url?: string;
  views?: number;
}

export class ComicDal extends BaseDal<ComicType> {
  /**
   * Build SQL filter conditions from options
   */
  private buildFilters(options: ComicListOptions) {
    const filters = [];

    if (options.query) {
      filters.push(ilike(comic.title, `%${options.query}%`));
    }

    if (options.status) {
      const validStatuses = ["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"] as const;
      if (validStatuses.includes(options.status as (typeof validStatuses)[number])) {
        filters.push(
          eq(
            comic.status,
            options.status as "Coming Soon" | "Completed" | "Dropped" | "Hiatus" | "Ongoing" | "Season End"
          )
        );
      }
    }

    if (options.typeId) filters.push(eq(comic.typeId, options.typeId));
    if (options.authorId) filters.push(eq(comic.authorId, options.authorId));
    if (options.artistId) filters.push(eq(comic.artistId, options.artistId));

    // Genre filtering via subquery — find comicIds that belong to the genre
    if (options.genreId) {
      filters.push(
        inArray(
          comic.id,
          db
            .select({ comicId: comicToGenre.comicId })
            .from(comicToGenre)
            .where(eq(comicToGenre.genreId, options.genreId))
        )
      );
    }

    return filters;
  }

  /**
   * Get SQL orderBy clause from sort option
   */
  private getOrderBy(orderBy: string = "latest") {
    switch (orderBy) {
      case "popular":
        return desc(comic.views);
      case "rating":
        return desc(comic.rating);
      case "title":
        return asc(comic.title);
      case "latest":
      default:
        return desc(comic.createdAt);
    }
  }

  /**
   * Count comics matching filter options (for pagination)
   */
  async count(options?: ComicListOptions): Promise<number> {
    const filters = this.buildFilters(options ?? {});
    const whereCondition = filters.length > 0 ? and(...filters) : undefined;

    const result = await db.select({ value: drizzleCount() }).from(comic).where(whereCondition);

    return result[0]?.value ?? 0;
  }

  /**
   * List comics with SQL-level filtering, sorting, and pagination
   */
  async list(options?: ComicListOptions) {
    const { limit = 20, offset = 0, orderBy = "latest" } = options ?? {};

    const filters = this.buildFilters(options ?? {});
    const whereCondition = filters.length > 0 ? and(...filters) : undefined;

    return db.query.comic.findMany({
      where: whereCondition,
      with: {
        author: true,
        artist: true,
        comicType: true,
        genres: { with: { genre: true } },
      },
      orderBy: this.getOrderBy(orderBy),
      limit,
      offset,
    });
  }

  /**
   * Get comic by ID with all relationships
   */
  async getById(id: number | string): Promise<ComicType | null> {
    // Accept both number and string for base class compatibility
    const numId = typeof id === "string" ? parseInt(id, 10) : id;
    if (isNaN(numId)) return null;

    const result = await db.query.comic.findFirst({
      where: eq(comic.id, numId),
      with: {
        author: true,
        artist: true,
        comicType: true,
        genres: { with: { genre: true } },
      },
    });

    // Cast result to ComicType (base class type) - relationships will be present in runtime
    return result ? (result as unknown as ComicType) : null;
  }

  /**
   * Get comic by slug with full details including chapters
   */
  async getBySlug(slug: string) {
    return (
      (await db.query.comic.findFirst({
        where: eq(comic.slug, slug),
        with: {
          author: true,
          artist: true,
          comicType: true,
          genres: { with: { genre: true } },
          chapters: {
            orderBy: desc(chapter.chapterNumber),
            limit: 100,
          },
        },
      })) ?? null
    );
  }

  /**
   * Search comics by title or description
   */
  async search(query: string, options?: DalOptions) {
    const { limit = 20, offset = 0 } = options ?? {};

    return await db.query.comic.findMany({
      where: ilike(comic.title, `%${query}%`),
      with: {
        author: true,
        artist: true,
        comicType: true,
        genres: { with: { genre: true } },
      },
      limit,
      offset,
    });
  }

  /**
   * Get popular comics by views
   */
  async getPopular(options?: DalOptions) {
    const { limit = 20, offset = 0 } = options ?? {};

    return db.query.comic.findMany({
      with: {
        author: true,
        artist: true,
        comicType: true,
        genres: { with: { genre: true } },
      },
      orderBy: desc(comic.views),
      limit,
      offset,
    });
  }

  /**
   * Get top rated comics
   */
  async getTopRated(options?: DalOptions) {
    const { limit = 20, offset = 0 } = options ?? {};

    return db.query.comic.findMany({
      with: {
        author: true,
        artist: true,
        comicType: true,
        genres: { with: { genre: true } },
      },
      orderBy: desc(comic.rating),
      limit,
      offset,
    });
  }

  /**
   * Get comics by status
   */
  async getByStatus(status: string, options?: DalOptions) {
    const { limit = 20, offset = 0 } = options ?? {};

    const validStatuses = ["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"] as const;
    const castStatus = validStatuses.includes(status as unknown as (typeof validStatuses)[number])
      ? (status as "Coming Soon" | "Completed" | "Dropped" | "Hiatus" | "Ongoing" | "Season End")
      : null;

    if (!castStatus) {
      return [];
    }

    return db.query.comic.findMany({
      where: eq(comic.status, castStatus),
      with: {
        author: true,
        artist: true,
        comicType: true,
        genres: { with: { genre: true } },
      },
      orderBy: desc(comic.createdAt),
      limit,
      offset,
    });
  }

  /**
   * Get related comics (same genre) using SQL subquery
   */
  async getRelated(comicId: number, options?: DalOptions) {
    const { limit = 5 } = options ?? {};

    // Get the source comic's genre IDs via subquery
    const genreIds = db
      .select({ genreId: comicToGenre.genreId })
      .from(comicToGenre)
      .where(eq(comicToGenre.comicId, comicId));

    // Find comics sharing those genres, excluding the source comic
    const relatedComicIds = db
      .selectDistinct({ comicId: comicToGenre.comicId })
      .from(comicToGenre)
      .where(and(inArray(comicToGenre.genreId, genreIds), ne(comicToGenre.comicId, comicId)));

    return db.query.comic.findMany({
      where: inArray(comic.id, relatedComicIds),
      with: {
        author: true,
        artist: true,
        comicType: true,
        genres: { with: { genre: true } },
      },
      orderBy: desc(comic.rating),
      limit,
    });
  }

  /**
   * Increment view count atomically
   */
  async incrementViews(id: number) {
    const [result] = await db
      .update(comic)
      .set({ views: sql`COALESCE(${comic.views}, 0) + 1` })
      .where(eq(comic.id, id))
      .returning();

    return result ?? null;
  }

  /**
   * Create new comic
   */
  async create(data: unknown): Promise<ComicType> {
    if (!data || typeof data !== "object" || !("title" in data) || !("slug" in data)) {
      throw new Error("Invalid comic data");
    }

    const input = data as CreateComicInput;

    // Validate and cast status enum
    const validStatuses = ["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"] as const;
    const status = validStatuses.includes(input.status as unknown as (typeof validStatuses)[number])
      ? (input.status as "Coming Soon" | "Completed" | "Dropped" | "Hiatus" | "Ongoing" | "Season End")
      : "Coming Soon"; // Default to Coming Soon

    const [result] = await db
      .insert(comic)
      .values({
        title: input.title,
        slug: input.slug,
        description: input.description,
        coverImage: input.coverImage,
        status,
        publicationDate: input.publicationDate,
        authorId: input.authorId,
        artistId: input.artistId,
        typeId: input.typeId,
        url: input.url,
        serialization: input.serialization,
      })
      .returning();

    if (!result) throw new Error("Failed to create comic");

    return result;
  }

  /**
   * Update comic
   */
  async update(id: number | string, data: unknown): Promise<ComicType | null> {
    if (!data || typeof data !== "object") {
      throw new Error("Invalid update data");
    }

    const input = data as UpdateComicInput;
    const numId = typeof id === "string" ? parseInt(id, 10) : id;
    if (isNaN(numId)) return null;

    // Prepare update object with conditional status casting
    const updateSet: Record<string, unknown> = {
      updatedAt: new Date(),
    };

    if (input.title !== undefined) updateSet.title = input.title;
    if (input.slug !== undefined) updateSet.slug = input.slug;
    if (input.description !== undefined) updateSet.description = input.description;
    if (input.coverImage !== undefined) updateSet.coverImage = input.coverImage;
    if (input.publicationDate !== undefined) updateSet.publicationDate = input.publicationDate;
    if (input.authorId !== undefined) updateSet.authorId = input.authorId;
    if (input.artistId !== undefined) updateSet.artistId = input.artistId;
    if (input.typeId !== undefined) updateSet.typeId = input.typeId;
    if (input.url !== undefined) updateSet.url = input.url;
    if (input.serialization !== undefined) updateSet.serialization = input.serialization;
    if (input.rating !== undefined) updateSet.rating = input.rating;
    if (input.views !== undefined) updateSet.views = input.views;

    // Validate and cast status enum
    if (input.status !== undefined) {
      const validStatuses = ["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"] as const;
      if (validStatuses.includes(input.status as unknown as (typeof validStatuses)[number])) {
        updateSet.status = input.status as
          | "Coming Soon"
          | "Completed"
          | "Dropped"
          | "Hiatus"
          | "Ongoing"
          | "Season End";
      }
    }

    const [result] = await db.update(comic).set(updateSet).where(eq(comic.id, numId)).returning();

    if (!result) return null;

    return this.getById(numId);
  }

  /**
   * Delete comic (will cascade to chapters, bookmarks, etc.)
   */
  async delete(id: number) {
    await db.delete(comic).where(eq(comic.id, id));
  }
}

export const comicDal = new ComicDal();
