/**
 * Bookmark DAL (Data Access Layer)
 * Manages bookmark CRUD operations with idempotent upsert
 */

import { and, desc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { bookmark } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

export interface BookmarkInput {
  comicId: number;
  lastReadChapterId?: number;
  notes?: string;
  status: string;
  userId: string;
}

export interface UpdateBookmarkInput {
  lastReadChapterId?: number;
  notes?: string;
  status?: string;
}

type BookmarkType = typeof bookmark.$inferSelect;

export class BookmarkDal extends BaseDal<BookmarkType> {
  /**
   * List all bookmarks (not typically used)
   */
  async list(options?: DalOptions) {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.bookmark.findMany({
      with: {
        comic: { with: { author: true, genres: { with: { genre: true } } } },
        lastReadChapter: true,
      },
      orderBy: desc(bookmark.updatedAt),
      limit,
      offset,
    });
  }

  /**
   * Get bookmark by composite key (userId, comicId)
   */
  async getByUserAndComic(userId: string, comicId: number) {
    // Note: bookmark has composite PK, no single ID
    return (
      db.query.bookmark.findFirst({
        where: and(eq(bookmark.userId, userId), eq(bookmark.comicId, comicId)),
        with: {
          comic: { with: { author: true, genres: { with: { genre: true } } } },
          lastReadChapter: true,
        },
      }) ?? null
    );
  }

  /**
   * Not used for bookmark (composite key)
   * Use getByUserAndComic(userId, comicId) instead
   */
  async getById(_id: number | string): Promise<{
    comicId: number;
    createdAt: Date;
    lastReadChapterId: null | number;
    notes: null | string;
    status: string;
    updatedAt: Date;
    userId: string;
  } | null> {
    throw new Error("Use getByUserAndComic(userId, comicId) instead");
  }

  /**
   * Get all bookmarks for a user
   */
  async getByUser(userId: string, options?: DalOptions) {
    const { limit = 100, offset = 0 } = options ?? {};

    return db.query.bookmark.findMany({
      where: eq(bookmark.userId, userId),
      with: {
        comic: { with: { author: true, genres: { with: { genre: true } } } },
        lastReadChapter: true,
      },
      orderBy: desc(bookmark.updatedAt),
      limit,
      offset,
    });
  }

  /**
   * Get bookmarks by user and status
   */
  async getByUserAndStatus(userId: string, status: string, options?: DalOptions) {
    const { limit = 100, offset = 0 } = options ?? {};

    return db.query.bookmark.findMany({
      where: and(eq(bookmark.userId, userId), eq(bookmark.status, status)),
      with: {
        comic: { with: { author: true, genres: { with: { genre: true } } } },
        lastReadChapter: true,
      },
      orderBy: desc(bookmark.updatedAt),
      limit,
      offset,
    });
  }

  /**
   * Create or update bookmark (idempotent upsert)
   */
  async createOrUpdate(data: BookmarkInput) {
    const [result] = await db
      .insert(bookmark)
      .values({
        userId: data.userId,
        comicId: data.comicId,
        status: data.status,
        notes: data.notes,
        lastReadChapterId: data.lastReadChapterId,
      })
      .onConflictDoUpdate({
        target: [bookmark.userId, bookmark.comicId],
        set: {
          status: data.status,
          notes: data.notes,
          lastReadChapterId: data.lastReadChapterId,
          updatedAt: new Date(),
        },
      })
      .returning();

    if (!result) throw new Error("Failed to create/update bookmark");

    return this.getByUserAndComic(result.userId, result.comicId);
  }

  /**
   * Update bookmark with composite key
   * Signature matches base class update(id, data)
   * For bookmark, use updateByUserAndComic() instead
   */
  async update(
    _id: number | string,
    _data: unknown
  ): Promise<{
    comicId: number;
    createdAt: Date;
    lastReadChapterId: null | number;
    notes: null | string;
    status: string;
    updatedAt: Date;
    userId: string;
  } | null> {
    throw new Error("Use updateByUserAndComic(userId, comicId, data) instead");
  }

  /**
   * Update bookmark by user and comic ID
   */
  async updateByUserAndComic(userId: string, comicId: number, data: UpdateBookmarkInput) {
    const existing = await db.query.bookmark.findFirst({
      where: and(eq(bookmark.userId, userId), eq(bookmark.comicId, comicId)),
    });

    if (!existing) return null;

    const updateData: Record<string, unknown> = { updatedAt: new Date() };
    if (data.status !== undefined) updateData.status = data.status;
    if (data.notes !== undefined) updateData.notes = data.notes;
    if (data.lastReadChapterId !== undefined) {
      updateData.lastReadChapterId = data.lastReadChapterId;
    }

    await db
      .update(bookmark)
      .set(updateData)
      .where(and(eq(bookmark.userId, userId), eq(bookmark.comicId, comicId)));

    return this.getByUserAndComic(userId, comicId);
  }

  /**
   * Delete bookmark with composite key
   * Signature matches base class delete(id)
   * For bookmark, use deleteByUserAndComic() instead
   */
  async delete(_id: number | string): Promise<void> {
    throw new Error("Use deleteByUserAndComic(userId, comicId) instead");
  }

  /**
   * Delete bookmark by user and comic ID
   */
  async deleteByUserAndComic(userId: string, comicId: number) {
    await db.delete(bookmark).where(and(eq(bookmark.userId, userId), eq(bookmark.comicId, comicId)));
  }

  /**
   * Check if user has bookmarked comic
   */
  async isBookmarked(userId: string, comicId: number) {
    const result = await db.query.bookmark.findFirst({
      where: and(eq(bookmark.userId, userId), eq(bookmark.comicId, comicId)),
    });

    return result !== undefined;
  }

  /**
   * Get user's current reading list
   */
  async getCurrentlyReading(userId: string) {
    return db.query.bookmark.findMany({
      where: and(eq(bookmark.userId, userId), eq(bookmark.status, "Reading")),
      with: {
        comic: { with: { author: true } },
        lastReadChapter: true,
      },
      orderBy: desc(bookmark.updatedAt),
      limit: 20,
    });
  }

  /**
   * Create bookmark (via upsert)
   */
  async create(data: unknown): Promise<{
    comicId: number;
    createdAt: Date;
    lastReadChapterId: null | number;
    notes: null | string;
    status: string;
    updatedAt: Date;
    userId: string;
  }> {
    if (!data || typeof data !== "object" || !("userId" in data) || !("comicId" in data) || !("status" in data)) {
      throw new Error("Invalid bookmark data");
    }
    const result = await this.createOrUpdate(data as BookmarkInput);
    if (!result) {
      throw new Error("Failed to create bookmark");
    }
    return result;
  }
}

export const bookmarkDal = new BookmarkDal();
