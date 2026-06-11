import { eq } from "drizzle-orm";

import { db } from "@/database/db";
import { readerSettings } from "@/database/schema";
import { type ReaderSettingsSeedItem, readerSettingsSeedItemSchema } from "@/schemas/seed/reader-settings.seed";

import { dataLoader } from "../data-loader";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class ReaderSettingsSeeder extends BaseSeeder<ReaderSettingsSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("reader-settings", readerSettingsSeedItemSchema, cache, options);
    this.dependencies = ["users"];
  }

  protected getDataSources(): string[] {
    return ["reader-settings"];
  }

  protected async loadData(): Promise<ReaderSettingsSeedItem[]> {
    const sources = this.getDataSources();
    const allData: ReaderSettingsSeedItem[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<ReaderSettingsSeedItem>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} reader settings records from ${source}`);
      } catch {
        // No data file - will generate sample data
      }
    }

    if (allData.length === 0) {
      return this.generateSampleReaderSettings();
    }

    return allData;
  }

  private async generateSampleReaderSettings(): Promise<ReaderSettingsSeedItem[]> {
    const settings: ReaderSettingsSeedItem[] = [];
    const users = await db.query.user.findMany({ limit: 20 });

    for (const user of users) {
      settings.push({
        userId: user.id,
        backgroundMode: "white",
        readingMode: "vertical",
        defaultQuality: "medium",
      });
    }

    logger.info(`Generated ${settings.length} sample reader settings`);
    return settings;
  }

  protected getUniqueField(): string {
    return "userId";
  }

  protected async transformData(raw: ReaderSettingsSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: ReaderSettingsSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        const existing = await db.query.readerSettings.findFirst({
          where: eq(readerSettings.userId, item.userId),
        });

        if (existing) {
          if (this.options.forceOverwrite) {
            const hasChanges =
              existing.backgroundMode !== item.backgroundMode ||
              existing.readingMode !== item.readingMode ||
              existing.defaultQuality !== item.defaultQuality;

            if (hasChanges) {
              await db
                .update(readerSettings)
                .set({
                  backgroundMode: item.backgroundMode,
                  readingMode: item.readingMode,
                  defaultQuality: item.defaultQuality,
                  updatedAt: new Date(),
                })
                .where(eq(readerSettings.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        await db.insert(readerSettings).values({
          userId: item.userId,
          backgroundMode: item.backgroundMode,
          readingMode: item.readingMode,
          defaultQuality: item.defaultQuality,
          createdAt: item.createdAt ?? new Date(),
          updatedAt: item.updatedAt ?? new Date(),
        });

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({ itemIndex: i, value: data[i], message });
        logger.debug(`Error inserting reader settings: ${message}`);
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
