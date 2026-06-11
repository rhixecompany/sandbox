/**
 * ChapterImageSeeder - seeds chapter images from chapter.json data
 *
 * Extracts image data from chapter entries and inserts into chapterImage table.
 * Depends on chapters being seeded first (resolves chapterId from DB).
 *
 * Features:
 * - Downloads images to local filesystem with caching (local strategy)
 * - Bulk insert optimization (up to 500 images per batch)
 * - URL format validation with warnings for invalid URLs
 * - ETA tracking with sliding window average
 * - Loads from same chapter.json source as ChapterSeeder
 * - Intelligent comic matching via chapter-matcher helpers
 * - Preloads all chapters for efficient batch lookups
 * - Uses onConflictDoNothing for unique (chapterId, pageNumber) constraint
 * - ComicWise branded fallback placeholders for failed downloads
 * - Can run independently to add images to existing chapters
 */

import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { chapter, chapterImage, comic } from "@/database/schema";
import { type ChapterSeed, chapterSeedItemSchema } from "@/schemas/seed/chapter.seed";

import {
  type EntityMeta,
  extractExtension,
  extractOriginalName,
  getCachedPathForUrl,
  imageDownloader,
  type ImageDownloadResult,
  isUrlCached,
  markUrlAsDownloaded,
} from "@/storages/image-downloader";
import {
  extractChapterNumber,
  extractImageUrls,
  getChapterName,
  matchChapterToComic,
  normalizeSlug,
} from "../helpers/chapter-matcher";
import { getChapterPageFallback } from "../helpers/image-fallback";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

const BULK_INSERT_SIZE = 1000; // Increased from 500 for better performance
const IMAGE_URL_PATTERN = /^https?:\/\/.+/i;
const ETA_WINDOW_SIZE = 5;
const IMAGE_CONCURRENCY = 10; // Parallel image downloads within a chapter

/**
 * ChapterImageSeeder loads images from chapter.json and inserts into chapterImage table
 *
 * Handles:
 * - Bulk insert optimization (up to 500 images per DB call)
 * - URL format validation with warnings
 * - ETA tracking with sliding window
 * - Multi-level comic matching (explicit slug, fuzzy title, normalized)
 * - Chapter lookup by (comicId, chapterNumber) unique constraint
 * - Multiple image formats (images array, image_urls array)
 * - onConflictDoNothing for unique (chapterId, pageNumber) constraint
 */
export class ChapterImageSeeder extends BaseSeeder<ChapterSeed> {
  /** Local cache: "comicId:chapterNumber" → chapterId */
  private chapterCache = new Map<string, number>();

  constructor(cache: LookupCache, options: SeedOptions) {
    super("chapter-images", chapterSeedItemSchema, cache, options);
    this.dependencies = ["chapters"];
  }

  protected getDataSources(): string[] {
    return ["chapter"];
  }

  protected getUniqueField(): string {
    return "chapterId_pageNumber";
  }

  protected async transformData(raw: ChapterSeed): Promise<unknown> {
    return raw;
  }

  /**
   * Pre-populate comic cache from existing database records
   */
  private async preloadComicCache(): Promise<void> {
    try {
      const existingComics = await db.query.comic.findMany();
      for (const c of existingComics) {
        this.cache.comics.set(c.slug, c.id);
      }
      if (existingComics.length > 0) {
        logger.debug(`Pre-loaded ${existingComics.length} comics into cache`);
      }
    } catch (error) {
      logger.warn(`Failed to pre-load comic cache: ${error}`);
    }
  }

  /**
   * Pre-populate chapter cache from existing database records
   * Builds a map of "comicId:chapterNumber" → chapterId for fast lookups
   */
  private async preloadChapterCache(): Promise<void> {
    try {
      const existingChapters = await db.query.chapter.findMany();
      for (const ch of existingChapters) {
        const key = `${ch.comicId}:${ch.chapterNumber}`;
        this.chapterCache.set(key, ch.id);
      }
      if (existingChapters.length > 0) {
        logger.debug(`Pre-loaded ${existingChapters.length} chapters into cache for image seeding`);
      }
    } catch (error) {
      logger.warn(`Failed to pre-load chapter cache: ${error}`);
    }
  }

  /**
   * Override seed to pre-load caches before processing
   */
  async seed(): Promise<EntityResult> {
    await this.preloadComicCache();
    await this.preloadChapterCache();
    return super.seed();
  }

  /**
   * Override loadData to filter to only chapters with images
   */
  protected async loadData(): Promise<ChapterSeed[]> {
    const allData = await super.loadData();
    const withImages = allData.filter((item) => {
      const imageUrls = extractImageUrls(item);
      return imageUrls.length > 0;
    });
    logger.debug(`Filtered to ${withImages.length} chapters with images (from ${allData.length} total)`);
    return withImages;
  }

  /**
   * Resolve a chapter's database ID from comic matching + chapter number
   */
  private async resolveChapterId(item: ChapterSeed): Promise<null | number> {
    // Build normalized slug map for fuzzy matching
    const comicsByNormalizedSlug = new Map<string, number>();
    for (const [slug, comicId] of this.cache.comics.entries()) {
      const normalized = normalizeSlug(slug);
      if (normalized && !comicsByNormalizedSlug.has(normalized)) {
        comicsByNormalizedSlug.set(normalized, comicId);
      }
    }

    // Match chapter to comic
    const comicId = matchChapterToComic(item, this.cache.comics, comicsByNormalizedSlug);
    if (!comicId) return null;

    // Extract chapter number
    const chapterNumber = extractChapterNumber(getChapterName(item)) ?? 0;

    // Look up chapter from preloaded cache
    const cacheKey = `${comicId}:${chapterNumber}`;
    const cachedChapterId = this.chapterCache.get(cacheKey);
    if (cachedChapterId) return cachedChapterId;

    // Fallback: query DB directly
    const chapterRecord = await db.query.chapter.findFirst({
      where: and(eq(chapter.comicId, comicId), eq(chapter.chapterNumber, chapterNumber)),
    });

    if (chapterRecord) {
      // Cache for future lookups
      this.chapterCache.set(cacheKey, chapterRecord.id);
      return chapterRecord.id;
    }

    return null;
  }

  /**
   * Format elapsed time into human-readable string
   */
  private formatDuration(ms: number): string {
    if (ms < 1000) return `${ms}ms`;
    const seconds = Math.floor(ms / 1000);
    const minutes = Math.floor(seconds / 60);
    if (minutes > 0) return `${minutes}m ${seconds % 60}s`;
    return `${seconds}s`;
  }

  /**
   * Get chapter info for dynamic path generation
   */
  private async getChapterInfoForPath(chapterId: number): Promise<{ chapterNumber: number; comicSlug: string } | null> {
    try {
      // Get chapter record
      const chapterRecord = await db.query.chapter.findFirst({
        where: eq(chapter.id, chapterId),
        columns: { comicId: true, chapterNumber: true },
      });
      if (!chapterRecord?.comicId) {
        return null;
      }

      // Get comic slug
      const comicRecord = await db.query.comic.findFirst({
        where: eq(comic.id, chapterRecord.comicId),
        columns: { slug: true },
      });

      if (comicRecord?.slug) {
        return {
          comicSlug: comicRecord.slug,
          chapterNumber: chapterRecord.chapterNumber,
        };
      }
      return null;
    } catch {
      return null;
    }
  }

  async insertBatch(data: ChapterSeed[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let skipped = 0;
    let updated = 0;
    // eslint-disable-next-line prefer-const
    let cacheHits = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];

    const strategy = this.options.imageStrategy ?? "urls";
    const enableDeduplication = this.options.enableDeduplication !== false;

    // Phase 1: Resolve all chapter IDs and collect image rows with parallel downloads
    const allImageRows: Array<{ chapterId: number; imageUrl: string; pageNumber: number }> = [];
    const chunkTimings: number[] = [];
    const totalChapters = data.length;

    // Process chapters in parallel batches
    const chapterBatchSize = 10;
    for (let batchStart = 0; batchStart < data.length; batchStart += chapterBatchSize) {
      const batch = data.slice(batchStart, batchStart + chapterBatchSize);
      const batchStartTime = Date.now();

      // Process each chapter in the batch
      const chapterResults = await Promise.all(
        batch.map(async (item) => {
          try {
            const chapterId = await this.resolveChapterId(item);
            if (!chapterId) {
              return { chapterId: null, images: [], error: null };
            }

            const imageUrls = extractImageUrls(item);
            if (imageUrls.length === 0) {
              return { chapterId, images: [], error: null };
            }

            // Validate URLs and prepare image data
            const seenPages = new Set<number>();
            const imageData: Array<{ pageNumber: number; url: string }> = [];

            for (let idx = 0; idx < imageUrls.length; idx++) {
              const url = imageUrls[idx];
              const pageNumber = idx + 1;

              if (seenPages.has(pageNumber)) {
                continue;
              }
              seenPages.add(pageNumber);

              if (!IMAGE_URL_PATTERN.test(url)) {
                continue;
              }

              imageData.push({ url, pageNumber });
            }

            // Download images in parallel for this chapter
            let finalImages: Array<{ imageUrl: string; pageNumber: number }> = [];

            if (strategy === "local" && imageData.length > 0) {
              const chapterInfo = await this.getChapterInfoForPath(chapterId);

              finalImages = await Promise.all(
                imageData.map(async (img) => {
                  // Check URL cache for deduplication (skip at download time)
                  if (enableDeduplication && isUrlCached(img.url)) {
                    const cachedPath = getCachedPathForUrl(img.url);
                    if (cachedPath) {
                      return { imageUrl: cachedPath, pageNumber: img.pageNumber, cached: true };
                    }
                  }

                  const entityMeta: EntityMeta = {
                    comicSlug: chapterInfo?.comicSlug,
                    chapterNum: chapterInfo?.chapterNumber,
                    pageNum: img.pageNumber,
                    originalExtension: extractExtension(img.url),
                    originalName: extractOriginalName(img.url),
                  };

                  const downloadResult: ImageDownloadResult = await imageDownloader.download(
                    img.url,
                    "chapters",
                    chapterId,
                    {
                      entityMeta,
                      skipIfExists: enableDeduplication,
                    }
                  );

                  if (downloadResult.success && downloadResult.filePath) {
                    // Mark URL as downloaded for future deduplication
                    if (enableDeduplication) {
                      markUrlAsDownloaded(img.url, downloadResult.filePath);
                    }
                    return { imageUrl: downloadResult.filePath, pageNumber: img.pageNumber, cached: false };
                  }

                  // Use branded placeholder on download failure
                  return {
                    imageUrl: getChapterPageFallback(`Ch.${chapterInfo?.chapterNumber ?? "?"}`),
                    pageNumber: img.pageNumber,
                    cached: false,
                  };
                })
              );
            } else {
              finalImages = imageData.map((img) => ({ imageUrl: img.url, pageNumber: img.pageNumber, cached: false }));
            }

            return {
              chapterId,
              images: finalImages.map((img) => ({
                chapterId,
                imageUrl: img.imageUrl,
                pageNumber: img.pageNumber,
              })),
              error: null,
            };
          } catch (error) {
            return {
              chapterId: null,
              images: [],
              error: error instanceof Error ? error.message : String(error),
            };
          }
        })
      );

      // Collect results from this batch
      for (const result of chapterResults) {
        if (result.error) {
          errors.push({ itemIndex: -1, value: null, message: result.error });
          continue;
        }

        if (!result.chapterId) {
          skipped++;
          continue;
        }

        for (const img of result.images) {
          allImageRows.push(img);
        }
      }

      // Progress tracking
      const batchElapsed = Date.now() - batchStartTime;
      chunkTimings.push(batchElapsed);
      if (chunkTimings.length > ETA_WINDOW_SIZE) chunkTimings.shift();

      const processed = Math.min(batchStart + chapterBatchSize, totalChapters);

      if (this.options.verbose || (batchStart + chapterBatchSize) % 50 === 0) {
        const avgBatchTime = chunkTimings.reduce((a, b) => a + b, 0) / chunkTimings.length;
        const remainingChapters = totalChapters - processed;
        const eta = this.formatDuration(Math.round(avgBatchTime * (remainingChapters / chapterBatchSize)));
        const elapsed = this.formatDuration(Date.now() - startTime);

        logger.info(
          `[chapter-images] Progress: ${processed}/${totalChapters} chapters | images: ${allImageRows.length} collected | ETA: ${eta} | elapsed: ${elapsed}`
        );
      }
    }

    // Phase 2: Bulk insert or update in chunks of BULK_INSERT_SIZE
    const totalChunks = Math.ceil(allImageRows.length / BULK_INSERT_SIZE);
    const shouldUpdate =
      this.options.forceOverwrite || this.options.updateMode === "full" || this.options.updateMode === "smart";

    for (let chunkIdx = 0; chunkIdx < totalChunks; chunkIdx++) {
      const chunkStart = Date.now();
      const chunk = allImageRows.slice(chunkIdx * BULK_INSERT_SIZE, (chunkIdx + 1) * BULK_INSERT_SIZE);

      try {
        if (shouldUpdate) {
          // Smart update: check if exists, update only if different
          for (const img of chunk) {
            const existing = await db.query.chapterImage.findFirst({
              where: and(eq(chapterImage.chapterId, img.chapterId), eq(chapterImage.pageNumber, img.pageNumber)),
            });

            if (existing) {
              // Smart update: only update if URL has changed or updateMode is "full"
              if (this.options.updateMode === "full" || (strategy === "local" && img.imageUrl !== existing.imageUrl)) {
                await db.update(chapterImage).set({ imageUrl: img.imageUrl }).where(eq(chapterImage.id, existing.id));
                updated++;
              } else {
                // Record exists and URL is the same - don't count as skipped
              }
            } else {
              await db.insert(chapterImage).values({
                chapterId: img.chapterId,
                imageUrl: img.imageUrl,
                pageNumber: img.pageNumber,
              });
              inserted++;
            }
          }
        } else {
          // Original: onConflictDoNothing for non-update mode
          const result = await db.insert(chapterImage).values(chunk).onConflictDoNothing().returning();
          inserted += result.length;
        }
      } catch (error) {
        const message = error instanceof Error ? error.message : String(error);
        errors.push({
          itemIndex: chunkIdx * BULK_INSERT_SIZE,
          value: `bulk chunk ${chunkIdx + 1}/${totalChunks}`,
          message,
        });
        if (this.options.verbose) {
          logger.debug(`Error in bulk insert chunk ${chunkIdx + 1}: ${message}`);
        }
      }

      // ETA tracking
      const chunkElapsed = Date.now() - chunkStart;
      chunkTimings.push(chunkElapsed);
      if (chunkTimings.length > ETA_WINDOW_SIZE) chunkTimings.shift();

      if (this.options.verbose && (chunkIdx + 1) % 5 === 0) {
        const avgChunkTime = chunkTimings.reduce((a, b) => a + b, 0) / chunkTimings.length;
        const remainingChunks = totalChunks - (chunkIdx + 1);
        const eta = this.formatDuration(Math.round(avgChunkTime * remainingChunks));
        const elapsed = this.formatDuration(Date.now() - startTime);
        logger.info(
          `[chunk ${chunkIdx + 1}/${totalChunks}] ${inserted} inserted, ${updated} updated | elapsed: ${elapsed} | ETA: ${eta}`
        );
      }
    }

    const duration = Date.now() - startTime;

    if (cacheHits > 0 && this.options.verbose) {
      logger.info(`Cache hits (deduplicated): ${cacheHits} images`);
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
