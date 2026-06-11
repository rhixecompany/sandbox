import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { share } from "@/database/schema";
import { type ShareSeedItem, shareSeedItemSchema } from "@/schemas/seed/share.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class ShareSeeder extends BaseSeeder<ShareSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("shares", shareSeedItemSchema, cache, options);
    this.dependencies = ["users", "comics"];
  }

  protected getDataSources(): string[] {
    return ["share"];
  }

  protected async loadData(): Promise<ShareSeedItem[]> {
    const sources = this.getDataSources();
    const allData: ShareSeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<ShareSeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} share records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleShares();
    }

    return allData;
  }

  private async generateSampleShares(): Promise<ShareSeedItem[]> {
    const shares: ShareSeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 10 });
    const comics = await db.query.comic.findMany({ limit: 30 });

    if (users.length === 0 || comics.length === 0) {
      return [];
    }

    for (const user of users.slice(0, 5)) {
      const numShares = Math.floor(Math.random() * 3) + 1;
      for (let i = 0; i < numShares; i++) {
        const comic = comics[Math.floor(Math.random() * comics.length)];
        shares.push({
          userId: user.id,
          resourceType: "comic",
          resourceId: comic.id,
          message: `Check out ${comic.title}!`,
        });
      }
    }

    logger.info(`Generated ${shares.length} sample shares`);
    return shares;
  }

  protected getUniqueField(): string {
    return "userId";
  }

  protected async transformData(raw: ShareSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: ShareSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.share.findFirst({
          where: and(eq(share.userId, item.userId), eq(share.resourceId, item.resourceId)),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges = existing.resourceType !== item.resourceType || existing.message !== item.message;

            if (hasChanges) {
              await db
                .update(share)
                .set({
                  resourceType: item.resourceType,
                  message: item.message,
                })
                .where(eq(share.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(share).values({
          userId: item.userId,
          resourceType: item.resourceType,
          resourceId: item.resourceId,
          message: item.message,
          createdAt: item.createdAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting share: ${message}`);
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
