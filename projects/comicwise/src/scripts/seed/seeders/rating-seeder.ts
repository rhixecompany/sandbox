import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { rating } from "@/database/schema";
import { type RatingSeedItem, ratingSeedItemSchema } from "@/schemas/seed/rating.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class RatingSeeder extends BaseSeeder<RatingSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("ratings", ratingSeedItemSchema, cache, options);
    this.dependencies = ["users", "comics"];
  }

  protected getDataSources(): string[] {
    return ["rating"];
  }

  protected async loadData(): Promise<RatingSeedItem[]> {
    const sources = this.getDataSources();
    const allData: RatingSeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<RatingSeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} rating records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleRatings();
    }

    return allData;
  }

  private async generateSampleRatings(): Promise<RatingSeedItem[]> {
    const ratings: RatingSeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 10 });
    const comics = await db.query.comic.findMany({ limit: 50 });

    if (users.length === 0 || comics.length === 0) {
      return [];
    }

    for (const user of users.slice(0, 5)) {
      const userComics = comics.slice(0, 3);
      for (const comic of userComics) {
        const ratingValue = Math.floor(Math.random() * 3) + 3;
        ratings.push({
          userId: user.id,
          comicId: comic.id,
          rating: ratingValue,
          review: undefined,
        });
      }
    }

    logger.info(`Generated ${ratings.length} sample ratings`);
    return ratings;
  }

  protected getUniqueField(): string {
    return "userId";
  }

  protected async transformData(raw: RatingSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: RatingSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.rating.findFirst({
          where: and(eq(rating.userId, item.userId), eq(rating.comicId, item.comicId)),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges = existing.rating !== item.rating || existing.review !== item.review;

            if (hasChanges) {
              await db
                .update(rating)
                .set({
                  rating: item.rating,
                  review: item.review,
                  updatedAt: new Date(),
                })
                .where(eq(rating.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(rating).values({
          userId: item.userId,
          comicId: item.comicId,
          rating: item.rating,
          review: item.review,
          createdAt: item.createdAt ?? new Date(),
          updatedAt: item.updatedAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting rating: ${message}`);
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
