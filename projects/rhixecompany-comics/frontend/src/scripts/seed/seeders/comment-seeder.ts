import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { comment } from "@/database/schema";
import { type CommentSeedItem, commentSeedItemSchema } from "@/schemas/seed/comment.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class CommentSeeder extends BaseSeeder<CommentSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("comments", commentSeedItemSchema, cache, options);
    this.dependencies = ["users", "chapters"];
  }

  protected getDataSources(): string[] {
    return ["comment"];
  }

  protected async loadData(): Promise<CommentSeedItem[]> {
    const sources = this.getDataSources();
    const allData: CommentSeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<CommentSeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} comment records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleComments();
    }

    return allData;
  }

  private async generateSampleComments(): Promise<CommentSeedItem[]> {
    const comments: CommentSeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 10 });
    const chapters = await db.query.chapter.findMany({ limit: 100 });

    if (users.length === 0 || chapters.length === 0) {
      return [];
    }

    const sampleComments = [
      "Great chapter!",
      "Can't wait for the next one!",
      "This is amazing!",
      "Love the artwork!",
      "Best series ever!",
    ];

    for (const chapter of chapters.slice(0, 50)) {
      const numComments = Math.floor(Math.random() * 3) + 1;
      for (let i = 0; i < numComments; i++) {
        const user = users[Math.floor(Math.random() * users.length)];
        comments.push({
          userId: user.id,
          chapterId: chapter.id,
          content: sampleComments[Math.floor(Math.random() * sampleComments.length)],
          parentId: undefined,
          deletedAt: undefined,
        });
      }
    }

    logger.info(`Generated ${comments.length} sample comments`);
    return comments;
  }

  protected getUniqueField(): string {
    return "content";
  }

  protected async transformData(raw: CommentSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: CommentSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.comment.findFirst({
          where: and(
            eq(comment.userId, item.userId),
            eq(comment.chapterId, item.chapterId),
            eq(comment.content, item.content)
          ),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges =
              existing.content !== item.content ||
              existing.parentId !== item.parentId ||
              existing.deletedAt?.getTime() !== item.deletedAt?.getTime();

            if (hasChanges) {
              await db
                .update(comment)
                .set({
                  content: item.content,
                  parentId: item.parentId,
                  deletedAt: item.deletedAt,
                  updatedAt: new Date(),
                })
                .where(eq(comment.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(comment).values({
          content: item.content,
          userId: item.userId,
          chapterId: item.chapterId,
          parentId: item.parentId,
          deletedAt: item.deletedAt,
          createdAt: item.createdAt ?? new Date(),
          updatedAt: item.updatedAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting comment: ${message}`);
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
