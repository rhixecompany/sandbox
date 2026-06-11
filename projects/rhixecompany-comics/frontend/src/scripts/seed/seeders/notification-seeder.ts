import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { notification } from "@/database/schema";
import { type NotificationSeedItem, notificationSeedItemSchema } from "@/schemas/seed/notification.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class NotificationSeeder extends BaseSeeder<NotificationSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("notifications", notificationSeedItemSchema, cache, options);
    this.dependencies = ["users", "comics"];
  }

  protected getDataSources(): string[] {
    return ["notification"];
  }

  protected async loadData(): Promise<NotificationSeedItem[]> {
    const sources = this.getDataSources();
    const allData: NotificationSeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<NotificationSeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} notification records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleNotifications();
    }

    return allData;
  }

  private async generateSampleNotifications(): Promise<NotificationSeedItem[]> {
    const notifications: NotificationSeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 10 });
    const comics = await db.query.comic.findMany({ limit: 20 });

    if (users.length === 0) {
      return [];
    }

    const notificationTypes = ["new_chapter", "comment_reply", "system"] as const;

    for (const user of users.slice(0, 5)) {
      const numNotifications = Math.floor(Math.random() * 3) + 1;
      for (let i = 0; i < numNotifications; i++) {
        const type = notificationTypes[Math.floor(Math.random() * notificationTypes.length)];
        const comic = comics[Math.floor(Math.random() * comics.length)];

        notifications.push({
          userId: user.id,
          type,
          title:
            type === "new_chapter"
              ? "New chapter available!"
              : type === "system"
                ? "System update"
                : "Reply to your comment",
          message:
            type === "new_chapter" ? `${comic?.title || "A comic"} has a new chapter` : "You have a new notification",
          link: comic ? `/comic/${comic.slug}` : undefined,
          read: Math.random() > 0.7,
          comicId: comic?.id,
          chapterId: undefined,
        });
      }
    }

    logger.info(`Generated ${notifications.length} sample notifications`);
    return notifications;
  }

  protected getUniqueField(): string {
    return "title";
  }

  protected async transformData(raw: NotificationSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: NotificationSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.notification.findFirst({
          where: and(eq(notification.userId, item.userId), eq(notification.title, item.title)),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges =
              existing.type !== item.type ||
              existing.message !== item.message ||
              existing.link !== item.link ||
              existing.read !== item.read ||
              existing.comicId !== item.comicId ||
              existing.chapterId !== item.chapterId;

            if (hasChanges) {
              await db
                .update(notification)
                .set({
                  type: item.type,
                  message: item.message,
                  link: item.link,
                  read: item.read,
                  comicId: item.comicId,
                  chapterId: item.chapterId,
                })
                .where(eq(notification.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(notification).values({
          userId: item.userId,
          type: item.type,
          title: item.title,
          message: item.message,
          link: item.link,
          read: item.read,
          comicId: item.comicId,
          chapterId: item.chapterId,
          createdAt: item.createdAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting notification: ${message}`);
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
