import { eq } from "drizzle-orm";

import { db } from "@/database/db";
import { userPreference } from "@/database/schema";
import { type UserPreferenceSeedItem, userPreferenceSeedItemSchema } from "@/schemas/seed/user-preference.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class UserPreferenceSeeder extends BaseSeeder<UserPreferenceSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("user-preferences", userPreferenceSeedItemSchema, cache, options);
    this.dependencies = ["users"];
  }

  protected getDataSources(): string[] {
    return ["user-preference"];
  }

  protected async loadData(): Promise<UserPreferenceSeedItem[]> {
    const sources = this.getDataSources();
    const allData: UserPreferenceSeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<UserPreferenceSeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} user preference records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleUserPreferences();
    }

    return allData;
  }

  private async generateSampleUserPreferences(): Promise<UserPreferenceSeedItem[]> {
    const preferences: UserPreferenceSeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 20 });

    for (const user of users) {
      preferences.push({
        userId: user.id,
        theme: "system",
        defaultLayout: "webtoon",
        pageNavigationStyle: "swipe",
        fontSize: 16,
        lineHeight: "normal",
        notifyNewChapters: true,
        notifyComments: true,
        notifyBookmarkUpdates: false,
        profilePublic: false,
        showReadingHistory: false,
      });
    }

    logger.info(`Generated ${preferences.length} sample user preferences`);
    return preferences;
  }

  protected getUniqueField(): string {
    return "userId";
  }

  protected async transformData(raw: UserPreferenceSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: UserPreferenceSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.userPreference.findFirst({
          where: eq(userPreference.userId, item.userId),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges =
              existing.theme !== item.theme ||
              existing.defaultLayout !== item.defaultLayout ||
              existing.pageNavigationStyle !== item.pageNavigationStyle ||
              existing.fontSize !== item.fontSize ||
              existing.lineHeight !== item.lineHeight ||
              existing.notifyNewChapters !== item.notifyNewChapters ||
              existing.notifyComments !== item.notifyComments ||
              existing.notifyBookmarkUpdates !== item.notifyBookmarkUpdates ||
              existing.profilePublic !== item.profilePublic ||
              existing.showReadingHistory !== item.showReadingHistory;

            if (hasChanges) {
              await db
                .update(userPreference)
                .set({
                  theme: item.theme,
                  defaultLayout: item.defaultLayout,
                  pageNavigationStyle: item.pageNavigationStyle,
                  fontSize: item.fontSize,
                  lineHeight: item.lineHeight,
                  notifyNewChapters: item.notifyNewChapters,
                  notifyComments: item.notifyComments,
                  notifyBookmarkUpdates: item.notifyBookmarkUpdates,
                  profilePublic: item.profilePublic,
                  showReadingHistory: item.showReadingHistory,
                  updatedAt: new Date(),
                })
                .where(eq(userPreference.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(userPreference).values({
          userId: item.userId,
          theme: item.theme,
          defaultLayout: item.defaultLayout,
          pageNavigationStyle: item.pageNavigationStyle,
          fontSize: item.fontSize,
          lineHeight: item.lineHeight,
          notifyNewChapters: item.notifyNewChapters,
          notifyComments: item.notifyComments,
          notifyBookmarkUpdates: item.notifyBookmarkUpdates,
          profilePublic: item.profilePublic,
          showReadingHistory: item.showReadingHistory,
          createdAt: item.createdAt ?? new Date(),
          updatedAt: item.updatedAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting user preference: ${message}`);
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
