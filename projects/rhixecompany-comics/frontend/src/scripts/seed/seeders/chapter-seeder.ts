/**
 * ChapterSeeder - seeds chapters with intelligent comic matching
 *
 * Features:
 * - Multi-format chapter data support (5+ different JSON structures)
 * - Intelligent comic matching: explicit slug → fuzzy title matching
 * - Handles multiple date formats (ISO, human-readable, timestamps)
 * - Supports multiple image formats (images array OR image_urls array)
 * - Graceful fallback for missing references
 */

import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { chapter } from "@/database/schema";
import { type ChapterSeed, chapterSeedItemSchema } from "@/schemas/seed/chapter.seed";

import { dataLoader } from "../data-loader";
import {
  extractChapterNumber as extractChapterNumberFallback,
  getChapterName,
  getChapterTitle,
  matchChapterToComic,
  normalizeSlug,
  parseDate,
} from "../helpers/chapter-matcher";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedError, SeedOptions } from "../types";

/**
 * ChapterSeeder loads chapters with image array handling
 *
 * Handles:
 * - Multi-level comic matching (explicit slug, fuzzy title, normalized)
 * - Chapter number extraction from chapter names
 * - Comic relation resolution with intelligent fallback
 * - ChapterImage creation for both image formats
 * - Date parsing from multiple field names and formats
 */
export class ChapterSeeder extends BaseSeeder<ChapterSeed> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("chapters", chapterSeedItemSchema, cache, options);
    this.dependencies = ["comics"];
  }

  protected getDataSources(): string[] {
    return ["chapter"];
  }

  protected async loadData(): Promise<ChapterSeed[]> {
    const sources = this.getDataSources();

    if (sources.length === 0) {
      return [];
    }

    const allData: ChapterSeed[] = [];

    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<ChapterSeed>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} chapter records from ${source}`);
      } catch (error) {
        logger.warn(`Failed to load ${source}: ${error}`);
      }
    }

    return allData;
  }

  /**
   * Pre-populate comic cache from existing database records
   * This ensures chapter seeding can find comics even if they weren't just inserted
   */
  private async preloadComicCache(): Promise<void> {
    try {
      const existingComics = await db.query.comic.findMany();
      for (const comic of existingComics) {
        this.cache.comics.set(comic.slug, comic.id);
      }
      if (existingComics.length > 0) {
        logger.success(`Pre-loaded ${existingComics.length} existing comics into cache`);
      }
    } catch (error) {
      logger.warn(`Failed to pre-load comic cache: ${error}`);
    }
  }

  /**
   * Override seed to pre-load comic cache before processing
   */
  async seed(): Promise<EntityResult> {
    // Pre-load existing comics into cache
    await this.preloadComicCache();
    // Call parent seed method
    return super.seed();
  }

  protected getUniqueField(): string {
    return "url";
  }

  protected async transformData(raw: ChapterSeed): Promise<unknown> {
    // Extract chapter number from name using intelligent parser
    const chapterNumber = extractChapterNumberFallback(getChapterName(raw)) ?? 0;

    // Will be used during insertBatch for slug generation (needs comic context)
    return {
      ...raw,
      chapterNumber,
    };
  }

  async insertBatch(data: ChapterSeed[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let updated = 0;
    let skipped = 0;
    const errors: SeedError[] = [];

    // Build extended comic cache with normalized slugs for fuzzy matching
    const comicsByNormalizedSlug = new Map<string, number>();
    for (const [slug, comicId] of this.cache.comics.entries()) {
      const normalized = normalizeSlug(slug);
      if (normalized && !comicsByNormalizedSlug.has(normalized)) {
        comicsByNormalizedSlug.set(normalized, comicId);
      }
    }

    if (this.cache.comics.size === 0) {
      logger.warn("NO COMICS FOUND IN CACHE! All chapters will be skipped.");
    } else {
      logger.progress(`Built comic cache: ${this.cache.comics.size} exact, ${comicsByNormalizedSlug.size} normalized`);
    }

    for (let i = 0; i < data.length; i++) {
      try {
        const item = data[i];

        // Use intelligent matching to find comic
        const comicId = matchChapterToComic(item, this.cache.comics, comicsByNormalizedSlug);

        if (!comicId) {
          skipped++;
          continue;
        }

        // Extract chapter number using intelligent parser
        const chapterNumber = extractChapterNumberFallback(getChapterName(item)) ?? 0;

        // Find comic slug for slug generation
        const comicSlug = Array.from(this.cache.comics.entries()).find(([_, id]) => id === comicId)?.[0] || "unknown";

        // Generate chapter slug if missing
        const slug = item.slug || item.chapterslug || `${comicSlug}-chapter-${chapterNumber}`;

        // Parse release date from multiple possible field names
        const releaseDate =
          parseDate(item.releaseDate) || parseDate(item.updated_at) || parseDate(item.updatedAt) || new Date();

        // Extract chapter title with fallback chain
        const title = getChapterTitle(item);

        // Check if chapter already exists
        const existingChapter = await db.query.chapter.findFirst({
          where: and(eq(chapter.comicId, comicId), eq(chapter.chapterNumber, chapterNumber)),
        });

        if (existingChapter) {
          if (this.options.forceOverwrite) {
            const hasChanges =
              existingChapter.title !== title ||
              existingChapter.slug !== slug ||
              existingChapter.releaseDate?.getTime() !== releaseDate.getTime();

            if (hasChanges) {
              await db
                .update(chapter)
                .set({
                  title,
                  slug,
                  releaseDate,
                })
                .where(eq(chapter.id, existingChapter.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            skipped++;
          }
          continue;
        }

        // Insert new chapter
        const chapterResult = await db
          .insert(chapter)
          .values({
            title,
            slug,
            chapterNumber,
            comicId,
            releaseDate,
          })
          .returning();

        if (chapterResult.length === 0) {
          throw new Error("Failed to insert chapter");
        }

        inserted++;
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({
          itemIndex: i,
          value: data[i],
          message,
        });
        if (this.options.verbose) {
          logger.debug(`Error inserting chapter ${i}: ${message}`);
        }
      }
    }

    const duration = Date.now() - startTime;

    if (skipped > 0) {
      logger.warn(`Skipped ${skipped} chapters (duplicates or no comic match)`);
    }

    return {
      entityName: this.entityName,
      inserted,
      updated,
      skipped,
      errors,
      duration,
      success: errors.length === 0,
    };
  }
}
