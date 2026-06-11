import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { bookmark } from "@/database/schema";
import { type BookmarkSeedItem, bookmarkSeedItemSchema } from "@/schemas/seed/bookmark.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class BookmarkSeeder extends BaseSeeder<BookmarkSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("bookmarks", bookmarkSeedItemSchema, cache, options);
    this.dependencies = ["users", "comics"];
  }

  protected getDataSources(): string[] {
    return ["bookmark"];
  }

  protected async loadData(): Promise<BookmarkSeedItem[]> {
    const sources = this.getDataSources();
    const allData: BookmarkSeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<BookmarkSeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} bookmark records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleBookmarks();
    }

    return allData;
  }

  private async generateSampleBookmarks(): Promise<BookmarkSeedItem[]> {
    const bookmarks: BookmarkSeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 10 });
    const comics = await db.query.comic.findMany({ limit: 50 });

    if (users.length === 0 || comics.length === 0) {
      logger.warn("Cannot generate sample bookmarks: no users or comics");
      return [];
    }

    for (const user of users.slice(0, 5)) {
      const userComics = comics.slice(0, 3);
      for (const comic of userComics) {
        bookmarks.push({
          userId: user.id,
          comicId: comic.id,
          status: "Reading",
          notes: undefined,
          lastReadChapterId: undefined,
        });
      }
    }

    logger.info(`Generated ${bookmarks.length} sample bookmarks`);
    return bookmarks;
  }

  protected getUniqueField(): string {
    return "userId";
  }

  protected async transformData(raw: BookmarkSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: BookmarkSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.bookmark.findFirst({
          where: and(eq(bookmark.userId, item.userId), eq(bookmark.comicId, item.comicId)),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges =
              existing.lastReadChapterId !== item.lastReadChapterId ||
              existing.status !== item.status ||
              existing.notes !== item.notes;

            if (hasChanges) {
              await db
                .update(bookmark)
                .set({
                  lastReadChapterId: item.lastReadChapterId,
                  status: item.status,
                  notes: item.notes,
                  updatedAt: new Date(),
                })
                .where(and(eq(bookmark.userId, item.userId), eq(bookmark.comicId, item.comicId)));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(bookmark).values({
          userId: item.userId,
          comicId: item.comicId,
          lastReadChapterId: item.lastReadChapterId,
          status: item.status,
          notes: item.notes,
          createdAt: item.createdAt ?? new Date(),
          updatedAt: item.updatedAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting bookmark: ${message}`);
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
