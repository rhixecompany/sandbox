import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { readingGoal } from "@/database/schema";
import { type ReadingGoalSeedItem, readingGoalSeedItemSchema } from "@/schemas/seed/reading-goal.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class ReadingGoalSeeder extends BaseSeeder<ReadingGoalSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("reading-goals", readingGoalSeedItemSchema, cache, options);
    this.dependencies = ["users"];
  }

  protected getDataSources(): string[] {
    return ["reading-goal"];
  }

  protected async loadData(): Promise<ReadingGoalSeedItem[]> {
    const sources = this.getDataSources();
    const allData: ReadingGoalSeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<ReadingGoalSeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} reading goal records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleReadingGoals();
    }

    return allData;
  }

  private async generateSampleReadingGoals(): Promise<ReadingGoalSeedItem[]> {
    const goals: ReadingGoalSeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 10 });

    const goalTypes = ["daily_chapters", "weekly_comics", "monthly_minutes"] as const;

    for (const user of users.slice(0, 5)) {
      for (const type of goalTypes) {
        const now = new Date();
        const endDate = new Date(now);
        endDate.setDate(endDate.getDate() + (type === "daily_chapters" ? 1 : type === "weekly_comics" ? 7 : 30));

        goals.push({
          userId: user.id,
          type,
          target: type === "daily_chapters" ? 5 : type === "weekly_comics" ? 10 : 300,
          currentCount: 0,
          startDate: now,
          endDate,
          isActive: true,
          completedAt: undefined,
        });
      }
    }

    logger.info(`Generated ${goals.length} sample reading goals`);
    return goals;
  }

  protected getUniqueField(): string {
    return "userId";
  }

  protected async transformData(raw: ReadingGoalSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: ReadingGoalSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.readingGoal.findFirst({
          where: and(eq(readingGoal.userId, item.userId), eq(readingGoal.type, item.type)),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges =
              existing.target !== item.target ||
              existing.currentCount !== item.currentCount ||
              existing.startDate?.getTime() !== item.startDate?.getTime() ||
              existing.endDate?.getTime() !== item.endDate?.getTime() ||
              existing.isActive !== item.isActive ||
              existing.completedAt?.getTime() !== item.completedAt?.getTime();

            if (hasChanges) {
              await db
                .update(readingGoal)
                .set({
                  target: item.target,
                  currentCount: item.currentCount,
                  startDate: item.startDate,
                  endDate: item.endDate,
                  isActive: item.isActive,
                  completedAt: item.completedAt,
                  updatedAt: new Date(),
                })
                .where(eq(readingGoal.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(readingGoal).values({
          userId: item.userId,
          type: item.type,
          target: item.target,
          currentCount: item.currentCount,
          startDate: item.startDate,
          endDate: item.endDate,
          isActive: item.isActive,
          completedAt: item.completedAt,
          createdAt: item.createdAt ?? new Date(),
          updatedAt: item.updatedAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting reading goal: ${message}`);
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
