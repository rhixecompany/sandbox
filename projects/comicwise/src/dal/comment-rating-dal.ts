/**
 * Comment and Rating DAL
 * Data access layer for comments and ratings
 */

import { and, desc, eq, isNull, sql } from "drizzle-orm";

import { db } from "@/database/db";
import { comic, comment, rating, type user } from "@/database/schema";

import { BaseDal } from "./base-dal";

import type { Comment, CreateCommentInput, CreateRatingInput, Rating } from "@/types/comment-rating";

type CommentRecord = typeof comment.$inferSelect;
type RatingRecord = typeof rating.$inferSelect;

/**
 * Comment Data Access Layer
 */
export class CommentDal extends BaseDal<Comment> {
  /**
   * Get comments for a chapter with optional parent filtering
   */
  async getCommentsByChapterId(
    chapterId: number,
    parentId: null | number = null,
    limit = 20,
    offset = 0
  ): Promise<Comment[]> {
    const results = await db.query.comment.findMany({
      where:
        parentId === null
          ? and(eq(comment.chapterId, chapterId), isNull(comment.parentId))
          : and(eq(comment.chapterId, chapterId), eq(comment.parentId, parentId)),
      orderBy: desc(comment.createdAt),
      limit,
      offset,
      with: {
        user: true,
      },
    });

    return results.map((r) => this.mapRecord(r));
  }

  /**
   * Get child comments (replies) for a parent comment
   */
  async getReplies(parentId: number): Promise<Comment[]> {
    const results = await db.query.comment.findMany({
      where: eq(comment.parentId, parentId),
      orderBy: desc(comment.createdAt),
      with: {
        user: true,
      },
    });

    return results.map((r) => this.mapRecord(r));
  }

  /**
   * Create a new comment
   */
  async create(data: unknown): Promise<Comment> {
    const input = data as CreateCommentInput & { userId: string };
    const result = await db
      .insert(comment)
      .values({
        content: input.content,
        chapterId: input.chapterId,
        userId: input.userId,
        parentId: input.parentId || null,
      })
      .returning();

    return this.mapRecord(result[0]);
  }

  /**
   * Update a comment
   */
  async update(id: number | string, data: unknown): Promise<Comment | null> {
    const updateData = data as { content: string };
    const result = await db
      .update(comment)
      .set({
        content: updateData.content,
        updatedAt: new Date(),
      })
      .where(eq(comment.id, Number(id)))
      .returning();

    return result.length > 0 ? this.mapRecord(result[0]) : null;
  }

  /**
   * Soft delete a comment
   */
  async delete(id: number | string): Promise<void> {
    await db
      .update(comment)
      .set({ deletedAt: new Date() })
      .where(eq(comment.id, Number(id)));
  }

  /**
   * Get by ID
   */
  async getById(id: number | string): Promise<Comment | null> {
    const result = await db.query.comment.findFirst({
      where: eq(comment.id, Number(id)),
      with: {
        user: true,
      },
    });

    return result ? this.mapRecord(result) : null;
  }

  /**
   * Get all comments
   */
  async list(): Promise<Comment[]> {
    const results = await db.query.comment.findMany({
      with: {
        user: true,
      },
    });

    return results.map((r) => this.mapRecord(r));
  }

  private mapRecord(record: CommentRecord & { user?: typeof user.$inferSelect }): Comment {
    return {
      id: record.id,
      content: record.content,
      userId: record.userId,
      chapterId: record.chapterId,
      parentId: record.parentId,
      deletedAt: record.deletedAt,
      createdAt: record.createdAt,
      updatedAt: record.updatedAt,
      user: record.user
        ? {
            id: record.user.id,
            name: record.user.name,
            email: record.user.email,
            image: record.user.image,
          }
        : undefined,
    };
  }

  /**
   * Get all comments for a chapter with nested replies
   */
  async getChapterComments(chapterId: number) {
    return db.query.comment.findMany({
      where: and(eq(comment.chapterId, chapterId), isNull(comment.parentId)),
      with: {
        user: true,
        replies: {
          with: {
            user: true,
          },
          orderBy: desc(comment.createdAt),
        },
      },
      orderBy: desc(comment.createdAt),
    });
  }

  /**
   * Get user's comments with chapter/comic relations
   */
  async getUserComments(userId: string) {
    return db.query.comment.findMany({
      where: eq(comment.userId, userId),
      with: {
        chapter: {
          with: {
            comic: true,
          },
        },
      },
      orderBy: desc(comment.createdAt),
      limit: 50,
    });
  }
}

/**
 * Rating Data Access Layer
 */
export class RatingDal extends BaseDal<Rating> {
  /**
   * Get rating for a user and comic
   */
  async getUserComicRating(userId: string, comicId: number): Promise<null | Rating> {
    const result = await db.query.rating.findFirst({
      where: and(eq(rating.userId, userId), eq(rating.comicId, comicId)),
    });

    return result ? this.mapRecord(result) : null;
  }

  /**
   * Get all ratings for a comic
   */
  async getComicRatings(comicId: number, limit = 20, offset = 0): Promise<Rating[]> {
    const results = await db.query.rating.findMany({
      where: eq(rating.comicId, comicId),
      orderBy: desc(rating.createdAt),
      limit,
      offset,
    });

    return results.map((r) => this.mapRecord(r));
  }

  /**
   * Get average rating for a comic
   */
  async getAverageRating(comicId: number): Promise<number> {
    const results = await db.select().from(rating).where(eq(rating.comicId, comicId));

    if (results.length === 0) return 0;

    const sum = results.reduce((acc, r) => acc + parseFloat(r.rating.toString()), 0);
    return sum / results.length;
  }

  /**
   * Create or update rating
   */
  async upsertRating(userId: string, data: CreateRatingInput): Promise<Rating> {
    const result = await db
      .insert(rating)
      .values({
        userId,
        comicId: data.comicId,
        rating: data.rating,
        review: data.review || null,
      })
      .onConflictDoUpdate({
        target: [rating.userId, rating.comicId],
        set: {
          rating: data.rating,
          review: data.review || null,
          updatedAt: new Date(),
        },
      })
      .returning();

    return this.mapRecord(result[0]);
  }

  /**
   * Create a new rating
   */
  async create(data: unknown): Promise<Rating> {
    const input = data as CreateRatingInput & { userId: string };
    const result = await db
      .insert(rating)
      .values({
        userId: input.userId,
        comicId: input.comicId,
        rating: input.rating,
        review: input.review || null,
      })
      .returning();

    return this.mapRecord(result[0]);
  }

  /**
   * Update a rating
   */
  async update(id: number | string, data: unknown): Promise<null | Rating> {
    const updateData = data as CreateRatingInput;
    const result = await db
      .update(rating)
      .set({
        rating: updateData.rating,
        review: updateData.review || null,
        updatedAt: new Date(),
      })
      .where(eq(rating.id, Number(id)))
      .returning();

    return result.length > 0 ? this.mapRecord(result[0]) : null;
  }

  /**
   * Delete a rating
   */
  async delete(id: number | string): Promise<void> {
    await db.delete(rating).where(eq(rating.id, Number(id)));
  }

  /**
   * Get by ID
   */
  async getById(id: number | string): Promise<null | Rating> {
    const result = await db.query.rating.findFirst({
      where: eq(rating.id, Number(id)),
    });

    return result ? this.mapRecord(result) : null;
  }

  /**
   * Get all ratings
   */
  async list(): Promise<Rating[]> {
    const results = await db.query.rating.findMany();
    return results.map((r) => this.mapRecord(r));
  }

  private mapRecord(record: RatingRecord): Rating {
    return {
      id: record.id,
      userId: record.userId,
      comicId: record.comicId,
      rating: record.rating,
      review: record.review,
      createdAt: record.createdAt,
      updatedAt: record.updatedAt,
    };
  }

  /**
   * Get rating statistics for a comic with distribution
   */
  async getComicRatingStats(comicId: number) {
    const statsResult = await db
      .select({
        totalCount: sql<number>`COUNT(*)`,
        averageScore: sql<number>`AVG(rating)`,
        count5: sql<number>`SUM(CASE WHEN rating = 5 THEN 1 ELSE 0 END)`,
        count4: sql<number>`SUM(CASE WHEN rating = 4 THEN 1 ELSE 0 END)`,
        count3: sql<number>`SUM(CASE WHEN rating = 3 THEN 1 ELSE 0 END)`,
        count2: sql<number>`SUM(CASE WHEN rating = 2 THEN 1 ELSE 0 END)`,
        count1: sql<number>`SUM(CASE WHEN rating = 1 THEN 1 ELSE 0 END)`,
      })
      .from(rating)
      .where(eq(rating.comicId, comicId));

    const stats = statsResult[0] || {
      totalCount: 0,
      averageScore: 0,
      count5: 0,
      count4: 0,
      count3: 0,
      count2: 0,
      count1: 0,
    };

    return {
      totalCount: Number(stats.totalCount),
      averageScore: Number((stats.averageScore || 0).toFixed(2)),
      distribution: {
        5: Number(stats.count5),
        4: Number(stats.count4),
        3: Number(stats.count3),
        2: Number(stats.count2),
        1: Number(stats.count1),
      },
    };
  }

  /**
   * Get user's ratings with comic relations
   */
  async getUserRatings(userId: string) {
    return db.query.rating.findMany({
      where: eq(rating.userId, userId),
      with: { comic: true },
      orderBy: desc(rating.createdAt),
      limit: 50,
    });
  }

  /**
   * Get top-rated comics
   */
  async getTopRatedComics(limit = 10) {
    const topComics = await db
      .select({
        comicId: rating.comicId,
        averageScore: sql<number>`AVG(rating)`,
        ratingCount: sql<number>`COUNT(*)`,
      })
      .from(rating)
      .groupBy(rating.comicId)
      .orderBy(sql`AVG(rating) DESC`)
      .limit(limit);

    return await Promise.all(
      topComics.map(async (item) => {
        const comicRecord = await db.query.comic.findFirst({
          where: eq(comic.id, item.comicId),
        });
        return {
          comic: comicRecord,
          averageScore: parseFloat(item.averageScore.toFixed(2)),
          ratingCount: Number(item.ratingCount),
        };
      })
    );
  }
}

// Export singleton instances
export const commentDal = new CommentDal();
export const ratingDal = new RatingDal();
