/**
 * Reading History DAL
 * Manages reading history tracking and analytics queries
 */

import { and, desc, eq, gte, lte } from "drizzle-orm";

import { db } from "@/database/db";
import { readingHistory } from "@/database/schema";

import { BaseDal } from "./base-dal";

type ReadingHistoryType = typeof readingHistory.$inferSelect;

export class ReadingHistoryDal extends BaseDal<ReadingHistoryType> {
  // Implement abstract methods
  async list(): Promise<ReadingHistoryType[]> {
    return db.query.readingHistory.findMany({ limit: 100 });
  }

  async getById(id: number | string): Promise<null | ReadingHistoryType> {
    const numId = typeof id === "string" ? parseInt(id) : id;
    const [result] = await db.select().from(readingHistory).where(eq(readingHistory.id, numId)).limit(1);
    return result || null;
  }

  async create(): Promise<ReadingHistoryType> {
    throw new Error("Use recordChapterRead() instead");
  }

  async update(): Promise<ReadingHistoryType> {
    throw new Error("Use updateProgress() or completeChapter() instead");
  }

  async delete(id: number | string): Promise<void> {
    const numId = typeof id === "string" ? parseInt(id) : id;
    await db.delete(readingHistory).where(eq(readingHistory.id, numId));
  }

  // Business methods
  async recordChapterRead(userId: string, comicId: number, chapterId: number): Promise<ReadingHistoryType> {
    const [result] = await db
      .insert(readingHistory)
      .values({
        userId,
        comicId,
        chapterId,
        startedAt: new Date(),
      })
      .returning();

    if (!result) {
      throw new Error("Failed to record chapter read");
    }

    return result;
  }

  async updateProgress(historyId: number, timeSpentSeconds: number, progress: number): Promise<ReadingHistoryType> {
    const [result] = await db
      .update(readingHistory)
      .set({
        timeSpentSeconds,
        progress: String(Math.min(progress, 100)),
        completedAt: progress >= 100 ? new Date() : undefined,
        updatedAt: new Date(),
      })
      .where(eq(readingHistory.id, historyId))
      .returning();

    if (!result) {
      throw new Error("Failed to update reading progress");
    }

    return result;
  }

  async completeChapter(historyId: number): Promise<ReadingHistoryType> {
    const [result] = await db
      .update(readingHistory)
      .set({
        progress: "100",
        completedAt: new Date(),
        updatedAt: new Date(),
      })
      .where(eq(readingHistory.id, historyId))
      .returning();

    if (!result) {
      throw new Error("Failed to complete chapter");
    }

    return result;
  }

  async getReadingHistory(
    userId: string,
    limit: number = 50,
    offset: number = 0,
    startDate?: Date,
    endDate?: Date
  ): Promise<ReadingHistoryType[]> {
    const whereConditions = [eq(readingHistory.userId, userId)];

    if (startDate) {
      whereConditions.push(gte(readingHistory.startedAt, startDate));
    }

    if (endDate) {
      whereConditions.push(lte(readingHistory.startedAt, endDate));
    }

    return db.query.readingHistory.findMany({
      where: and(...whereConditions),
      orderBy: [desc(readingHistory.startedAt)],
      limit,
      offset,
    });
  }

  async getComicReadingHistory(userId: string, comicId: number, limit: number = 20): Promise<ReadingHistoryType[]> {
    return db.query.readingHistory.findMany({
      where: and(eq(readingHistory.userId, userId), eq(readingHistory.comicId, comicId)),
      orderBy: [desc(readingHistory.startedAt)],
      limit,
    });
  }

  async getLastReadChapter(userId: string, comicId: number): Promise<null | ReadingHistoryType> {
    const [result] = await db
      .select()
      .from(readingHistory)
      .where(and(eq(readingHistory.userId, userId), eq(readingHistory.comicId, comicId)))
      .orderBy(desc(readingHistory.startedAt))
      .limit(1);

    return result || null;
  }

  async getReadingStats(
    userId: string,
    startDate?: Date,
    endDate?: Date
  ): Promise<{
    averageTimePerChapter: number;
    completionRate: number;
    totalChaptersRead: number;
    totalComicsRead: number;
    totalMinutesSpent: number;
  }> {
    const whereConditions = [eq(readingHistory.userId, userId)];

    if (startDate) {
      whereConditions.push(gte(readingHistory.startedAt, startDate));
    }

    if (endDate) {
      whereConditions.push(lte(readingHistory.startedAt, endDate));
    }

    const stats = await db
      .selectDistinct({
        chaptersRead: readingHistory.id,
        totalTime: readingHistory.timeSpentSeconds,
        comicsRead: readingHistory.comicId,
        completed: readingHistory.completedAt,
      })
      .from(readingHistory)
      .where(and(...whereConditions));

    if (stats.length === 0) {
      return {
        totalChaptersRead: 0,
        totalMinutesSpent: 0,
        totalComicsRead: 0,
        averageTimePerChapter: 0,
        completionRate: 0,
      };
    }

    const totalChapters = stats.length;
    const totalSeconds = stats.reduce((sum, s) => sum + (s.totalTime || 0), 0);
    const totalMinutes = Math.round(totalSeconds / 60);
    const uniqueComics = new Set(stats.map((s) => s.comicsRead)).size;
    const completedChapters = stats.filter((s) => s.completed).length;

    return {
      totalChaptersRead: totalChapters,
      totalMinutesSpent: totalMinutes,
      totalComicsRead: uniqueComics,
      averageTimePerChapter: totalChapters > 0 ? Math.round(totalSeconds / totalChapters / 60) : 0,
      completionRate: totalChapters > 0 ? Math.round((completedChapters / totalChapters) * 100) : 0,
    };
  }

  async getTotalTimeSpent(userId: string): Promise<number> {
    const result = await db
      .selectDistinct({ total: readingHistory.timeSpentSeconds })
      .from(readingHistory)
      .where(eq(readingHistory.userId, userId));

    const totalSeconds = result.reduce((sum, r) => sum + (r.total || 0), 0);
    return Math.round(totalSeconds / 3600);
  }

  async getRecentlyReadComics(userId: string, limit: number = 5): Promise<ReadingHistoryType[]> {
    const results = await db.query.readingHistory.findMany({
      where: eq(readingHistory.userId, userId),
      orderBy: [desc(readingHistory.startedAt)],
      limit: limit * 2,
    });

    const seenComics = new Set<number>();
    return results
      .filter((r) => {
        if (seenComics.has(r.comicId)) {
          return false;
        }
        seenComics.add(r.comicId);
        return true;
      })
      .slice(0, limit);
  }

  async deleteOlderThan(days: number): Promise<void> {
    const cutoffDate = new Date();
    cutoffDate.setDate(cutoffDate.getDate() - days);

    await db.delete(readingHistory).where(lte(readingHistory.createdAt, cutoffDate));
  }
}

export const readingHistoryDal = new ReadingHistoryDal();
