/**
 * Reading Progress Data Access Layer (DAL)
 * Handles database operations for user reading progress
 *
 * Schema: Users track reading progress per chapter with page-level details
 */

import { and, desc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { chapter, comic, readingProgress } from "@/database/schema";

import { BaseDal } from "./base-dal";

export interface UpdateProgressInput {
  chapterId?: number;
  comicId: number;
  pageNumber?: number;
  scrollPercentage?: number;
  scrollPosition?: number;
  userId: string;
}

export type ReadingProgressRecord = typeof readingProgress.$inferSelect;

export class ReadingProgressDal extends BaseDal<ReadingProgressRecord> {
  /**
   * Get reading progress for a user on a specific chapter
   */
  async getProgress(userId: string, chapterId: number): Promise<null | ReadingProgressRecord> {
    try {
      const [result] = await db
        .select()
        .from(readingProgress)
        .where(and(eq(readingProgress.userId, userId), eq(readingProgress.chapterId, chapterId)));

      return result ?? null;
    } catch (error) {
      return this.handleError(error, "getProgress");
    }
  }

  /**
   * Get user's "continue reading" list - last read chapters
   * Used for dashboard quick links
   */
  async getContinueReadingList(userId: string, limit: number = 10) {
    try {
      return await db
        .selectDistinct({
          comicId: readingProgress.comicId,
          comicTitle: comic.title,
          comicSlug: comic.slug,
          chapterId: readingProgress.chapterId,
          pageNumber: readingProgress.pageNumber,
          progressPercent: readingProgress.progressPercent,
          lastReadAt: readingProgress.lastReadAt,
          chapterNumber: chapter.chapterNumber,
          chapterTitle: chapter.title,
        })
        .from(readingProgress)
        .innerJoin(comic, eq(readingProgress.comicId, comic.id))
        .leftJoin(chapter, eq(readingProgress.chapterId, chapter.id))
        .where(eq(readingProgress.userId, userId))
        .orderBy(desc(readingProgress.lastReadAt))
        .limit(limit);
    } catch (error) {
      return this.handleError(error, "getContinueReadingList");
    }
  }

  /**
   * Update reading progress - idempotent upsert per chapter per user
   */
  async updateProgress(data: UpdateProgressInput): Promise<ReadingProgressRecord> {
    try {
      if (!data.chapterId) {
        throw new Error("chapterId is required");
      }

      const [result] = await db
        .insert(readingProgress)
        .values({
          userId: data.userId,
          comicId: data.comicId,
          chapterId: data.chapterId,
          pageNumber: data.pageNumber ?? 0,
          scrollPosition: data.scrollPosition ?? 0,
          scrollPercentage: data.scrollPercentage ?? 0,
          lastReadAt: new Date(),
          updatedAt: new Date(),
        })
        .onConflictDoUpdate({
          target: [readingProgress.userId, readingProgress.chapterId],
          set: {
            pageNumber: data.pageNumber ?? undefined,
            scrollPosition: data.scrollPosition ?? undefined,
            scrollPercentage: data.scrollPercentage ?? undefined,
            lastReadAt: new Date(),
            updatedAt: new Date(),
          },
        })
        .returning();

      if (!result) {
        throw new Error("Failed to update reading progress");
      }

      return result;
    } catch (error) {
      return this.handleError(error, "updateProgress");
    }
  }

  /**
   * Mark chapter as completed
   */
  async markCompleted(userId: string, chapterId: number): Promise<null | ReadingProgressRecord> {
    try {
      const [result] = await db
        .update(readingProgress)
        .set({
          completedAt: new Date(),
          progressPercent: 100,
          updatedAt: new Date(),
        })
        .where(and(eq(readingProgress.userId, userId), eq(readingProgress.chapterId, chapterId)))
        .returning();

      return result ?? null;
    } catch (error) {
      return this.handleError(error, "markCompleted");
    }
  }

  /**
   * Get reading statistics for a user
   */
  async getUserStats(userId: string) {
    try {
      const records = await db.selectDistinct().from(readingProgress).where(eq(readingProgress.userId, userId));

      const completed = records.filter((r) => r.completedAt !== null).length;
      const avgProgress =
        records.length > 0 ? Math.round(records.reduce((sum, r) => sum + r.progressPercent, 0) / records.length) : 0;

      return {
        totalChaptersRead: records.length,
        totalChaptersCompleted: completed,
        averageProgressPercent: avgProgress,
      };
    } catch (error) {
      return this.handleError(error, "getUserStats");
    }
  }

  /**
   * Clear progress for a chapter
   */
  async clearForChapter(chapterId: number): Promise<void> {
    try {
      await db.delete(readingProgress).where(eq(readingProgress.chapterId, chapterId));
    } catch (error) {
      return this.handleError(error, "clearForChapter");
    }
  }

  // BaseDal abstract methods (not used)
  async list(): Promise<ReadingProgressRecord[]> {
    throw new Error("Use getContinueReadingList() instead");
  }

  async getById(): Promise<null | ReadingProgressRecord> {
    throw new Error("Use getProgress(userId, chapterId) instead");
  }

  async create(): Promise<ReadingProgressRecord> {
    throw new Error("Use updateProgress() instead");
  }

  async update(): Promise<null | ReadingProgressRecord> {
    throw new Error("Use updateProgress() instead");
  }

  async delete(): Promise<void> {
    throw new Error("Use clearForChapter() instead");
  }
}

// Export singleton instance
export const readingProgressDal = new ReadingProgressDal();
