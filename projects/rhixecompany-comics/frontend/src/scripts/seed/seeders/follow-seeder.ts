import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { follow } from "@/database/schema";
import { type FollowSeedItem, followSeedItemSchema } from "@/schemas/seed/follow.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class FollowSeeder extends BaseSeeder<FollowSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("follows", followSeedItemSchema, cache, options);
    this.dependencies = ["users"];
  }

  protected getDataSources(): string[] {
    return ["follow"];
  }

  protected async loadData(): Promise<FollowSeedItem[]> {
    const sources = this.getDataSources();
    const allData: FollowSeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<FollowSeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} follow records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleFollows();
    }

    return allData;
  }

  private async generateSampleFollows(): Promise<FollowSeedItem[]> {
    const follows: FollowSeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 20 });

    if (users.length < 2) {
      return [];
    }

    for (let i = 0; i < users.length - 1; i++) {
      const follower = users[i];
      const followingCount = Math.min(3, users.length - i - 1);

      for (let j = i + 1; j < i + 1 + followingCount; j++) {
        follows.push({
          followerId: follower.id,
          followingId: users[j].id,
        });
      }
    }

    logger.info(`Generated ${follows.length} sample follows`);
    return follows;
  }

  protected getUniqueField(): string {
    return "followerId";
  }

  protected async transformData(raw: FollowSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: FollowSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.follow.findFirst({
          where: and(eq(follow.followerId, item.followerId), eq(follow.followingId, item.followingId)),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges = existing.followerId !== item.followerId || existing.followingId !== item.followingId;

            if (hasChanges) {
              await db
                .update(follow)
                .set({
                  followerId: item.followerId,
                  followingId: item.followingId,
                })
                .where(and(eq(follow.followerId, item.followerId), eq(follow.followingId, item.followingId)));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(follow).values({
          followerId: item.followerId,
          followingId: item.followingId,
          createdAt: item.createdAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting follow: ${message}`);
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
