import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { readingHistory } from "@/database/schema";
import { type ReadingHistorySeedItem, readingHistorySeedItemSchema } from "@/schemas/seed/reading-history.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class ReadingHistorySeeder extends BaseSeeder<ReadingHistorySeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("reading-history", readingHistorySeedItemSchema, cache, options);
    this.dependencies = ["users", "comics", "chapters"];
  }

  protected getDataSources(): string[] {
    return ["reading-history"];
  }

  protected async loadData(): Promise<ReadingHistorySeedItem[]> {
    const sources = this.getDataSources();
    const allData: ReadingHistorySeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<ReadingHistorySeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} reading history records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleReadingHistory();
    }

    return allData;
  }

  private async generateSampleReadingHistory(): Promise<ReadingHistorySeedItem[]> {
    const history: ReadingHistorySeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 10 });
    const chapters = await db.query.chapter.findMany({ limit: 200 });

    if (users.length === 0 || chapters.length === 0) {
      return [];
    }

    for (const user of users.slice(0, 5)) {
      const numHistory = Math.min(20, chapters.length);
      for (let i = 0; i < numHistory; i++) {
        const chapter = chapters[i];
        history.push({
          userId: user.id,
          comicId: chapter.comicId,
          chapterId: chapter.id,
          startedAt: new Date(Date.now() - Math.random() * 30 * 24 * 60 * 60 * 1000),
          completedAt: Math.random() > 0.5 ? new Date() : undefined,
          timeSpentSeconds: Math.floor(Math.random() * 600) + 60,
          progress: Math.random() * 100,
        });
      }
    }

    logger.info(`Generated ${history.length} sample reading history entries`);
    return history;
  }

  protected getUniqueField(): string {
    return "userId";
  }

  protected async transformData(raw: ReadingHistorySeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: ReadingHistorySeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.readingHistory.findFirst({
          where: and(
            eq(readingHistory.userId, item.userId),
            eq(readingHistory.comicId, item.comicId),
            eq(readingHistory.chapterId, item.chapterId)
          ),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges =
              existing.startedAt?.getTime() !== item.startedAt?.getTime() ||
              existing.completedAt?.getTime() !== item.completedAt?.getTime() ||
              existing.timeSpentSeconds !== item.timeSpentSeconds ||
              existing.progress !== String(item.progress);

            if (hasChanges) {
              await db
                .update(readingHistory)
                .set({
                  startedAt: item.startedAt,
                  completedAt: item.completedAt,
                  timeSpentSeconds: item.timeSpentSeconds,
                  progress: String(item.progress),
                  updatedAt: new Date(),
                })
                .where(eq(readingHistory.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(readingHistory).values({
          userId: item.userId,
          comicId: item.comicId,
          chapterId: item.chapterId,
          startedAt: item.startedAt ?? new Date(),
          completedAt: item.completedAt,
          timeSpentSeconds: item.timeSpentSeconds,
          progress: String(item.progress),
          createdAt: item.createdAt ?? new Date(),
          updatedAt: item.updatedAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting reading history: ${message}`);
      }
    }

    return {
      entityName: this.entityName,
      inserted,
      updated,
      skipped,
      errors,
      duration: Date.now() - startTime,
      success: errors.length === 0,
    };
  }
}
