/**
 * ComicImageSeeder - seeds comic images from comic.json data
 *
 * Extracts image data from comic entries and inserts into comicImage table.
 * Depends on comics being seeded first (resolves comicId from cache).
 *
 * Features:
 * - Multi-strategy image handling (urls, local, imagekit)
 * - Downloads images to local filesystem with caching
 * - URL format validation with ComicWise branded fallback placeholders
 * - Parallel processing via Promise.allSettled (batches of 5 comics)
 * - Loads from same comic.json source as ComicSeeder
 * - Filters to entries with image data
 * - Skips cover images (already set on comic record)
 * - Uses onConflictDoNothing for unique imageUrl constraint
 * - Can run independently to add images to existing comics
 */

import { and, eq, not } from "drizzle-orm";

import { db } from "@/database/db";
import { comicImage } from "@/database/schema";
import { type ComicSeed, comicSeedItemSchema } from "@/schemas/seed/comic.seed";

import { getEnv } from "appConfig";

import {
  type EntityMeta,
  extractExtension,
  extractOriginalName,
  imageDownloader,
  type ImageDownloadResult,
} from "@/storages/image-downloader";
import { getDeduplicationStats } from "../helpers/image-deduplicator";
import { getCoverFallback } from "../helpers/image-fallback";
import { migrateImages } from "../helpers/image-migrator";
import { isValidImageUrl } from "../helpers/image-url-validator";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

const PARALLEL_BATCH_SIZE = 15;

/**
 * Apply image strategy transformation to a URL
 * For "local" strategy, this downloads the image to the filesystem with deduplication
 */
async function applyImageStrategy(
  url: string,
  strategy: string,
  comicTitle: string,
  comicId: number,
  slug: string,
  imageIndex: number,
  isCover: boolean = false
): Promise<string> {
  if (!url || !isValidImageUrl(url)) {
    return getCoverFallback(comicTitle);
  }

  switch (strategy) {
    case "local": {
      const entityMeta: EntityMeta = {
        slug,
        imageIndex,
        isCover,
        originalExtension: extractExtension(url),
        originalName: extractOriginalName(url),
      };
      const result: ImageDownloadResult = await imageDownloader.download(url, "comics", comicId, { entityMeta });
      if (result.success && result.filePath) {
        return result.filePath;
      }
      logger.debug(`Failed to download comic image: ${url}, using branded placeholder`);
      return getCoverFallback(comicTitle);
    }
    case "imagekit": {
      const imagekitBase = getEnv().IMAGEKIT_URL_ENDPOINT ?? "https://ik.imagekit.io/comicwise";
      try {
        const parsed = new URL(url);
        return `${imagekitBase}${parsed.pathname}`;
      } catch {
        return url;
      }
    }
    case "urls":
    default:
      return url;
  }
}

/**
 * ComicImageSeeder loads images from comic.json and inserts into comicImage table
 *
 * Handles:
 * - Multi-strategy image handling (urls/local/imagekit)
 * - URL format validation with fallback placeholders
 * - Parallel processing in batches of 5 comics
 * - Resolving comicId from LookupCache by slug
 * - Filtering comic entries that have image data
 * - Skipping cover images (already handled by ComicSeeder)
 * - onConflictDoNothing for unique imageUrl constraint
 */
export class ComicImageSeeder extends BaseSeeder<ComicSeed> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("comic-images", comicSeedItemSchema, cache, options);
    this.dependencies = ["comics"];
  }

  protected getDataSources(): string[] {
    return ["comic"];
  }

  protected getUniqueField(): string {
    return "imageUrl";
  }

  protected async transformData(raw: ComicSeed): Promise<unknown> {
    return raw;
  }

  /**
   * Pre-populate comic cache from existing database records
   * Ensures image seeding can find comics even if they weren't just inserted
   */
  private async preloadComicCache(): Promise<void> {
    try {
      const existingComics = await db.query.comic.findMany();
      for (const c of existingComics) {
        this.cache.comics.set(c.slug, c.id);
      }
      if (existingComics.length > 0) {
        logger.debug(`Pre-loaded ${existingComics.length} comics into cache for image seeding`);
      }
    } catch (error) {
      logger.warn(`Failed to pre-load comic cache: ${error}`);
    }
  }

  /**
   * Override seed to pre-load comic cache before processing
   * For local strategy, also run migration on existing images
   */
  async seed(): Promise<EntityResult> {
    await this.preloadComicCache();

    // Run migration for local strategy
    if (this.options.imageStrategy === "local") {
      const migrationResult = await migrateImages();
      if (migrationResult.success) {
        logger.success("Image migration completed successfully");
      } else if (migrationResult.stats.migrated > 0) {
        logger.warn(`Image migration completed with ${migrationResult.stats.errors} errors`);
      }

      // Log deduplication stats
      const dedupStats = await getDeduplicationStats();
      if (dedupStats.totalImages > 0) {
        logger.info(
          `Deduplication: ${dedupStats.totalImages} images, ${dedupStats.uniqueImages} unique, ${dedupStats.duplicates} duplicates, saved ${dedupStats.storageSavedMB}MB`
        );
      }
    }

    return super.seed();
  }

  /**
   * Override loadData to filter to only comics with images
   */
  protected async loadData(): Promise<ComicSeed[]> {
    const allData = await super.loadData();
    const withImages = allData.filter((item) => item.images && item.images.length > 0);
    logger.debug(`Filtered to ${withImages.length} comics with images (from ${allData.length} total)`);
    return withImages;
  }

  /**
   * Process a single comic's images and return counts
   * Smart update: checks if record exists, updates only if different
   * No "skipped" count - all records are processed (updated if exists, inserted if new)
   */
  private async processComicImages(
    item: ComicSeed,
    strategy: string
  ): Promise<{ error?: string; inserted: number; skipped: number; updated: number }> {
    const comicId = this.cache.comics.get(item.slug);
    if (!comicId) {
      if (this.options.verbose) {
        logger.debug(`No comic found in cache for slug "${item.slug}", skipping images`);
      }
      return { inserted: 0, skipped: 1, updated: 0 };
    }

    // Filter out cover image (already set on comic record)
    const images = item.coverImage ? item.images.filter((img) => img.url !== item.coverImage) : item.images;
    if (!images || images.length === 0) {
      return { inserted: 0, skipped: 1, updated: 0 };
    }

    // Apply image strategy + validation (async for local downloads)
    const imageUrls = await Promise.all(
      images.map(async (img, idx) => ({
        comicId,
        imageUrl: await applyImageStrategy(img.url, strategy, item.title, comicId, item.slug, idx + 1),
        imageOrder: idx + 1,
        originalUrl: img.url, // Keep original URL for comparison
      }))
    );

    // Determine if we should update existing records
    const shouldUpdate =
      this.options.forceOverwrite || this.options.updateMode === "full" || this.options.updateMode === "smart";

    if (shouldUpdate) {
      let inserted = 0;
      let skipped = 0;
      let updated = 0;

      for (const img of imageUrls) {
        // Check if image already exists by comicId and imageOrder
        const existing = await db.query.comicImage.findFirst({
          where: and(eq(comicImage.comicId, comicId), eq(comicImage.imageOrder, img.imageOrder)),
        });

        if (existing) {
          // Smart update: only update if URL has changed (for local strategy)
          // or if updateMode is "full" or if forceOverwrite is set
          if (
            this.options.forceOverwrite ||
            this.options.updateMode === "full" ||
            (strategy === "local" && img.imageUrl !== existing.imageUrl)
          ) {
            // Check if the new URL already exists for another comic (unique constraint)
            if (img.imageUrl !== existing.imageUrl) {
              const urlExistsForOther = await db.query.comicImage.findFirst({
                where: and(eq(comicImage.imageUrl, img.imageUrl), not(eq(comicImage.id, existing.id))),
              });

              if (urlExistsForOther) {
                // URL already used by another comic - skip update to avoid constraint violation
                skipped++;
                continue;
              }
            }

            await db.update(comicImage).set({ imageUrl: img.imageUrl }).where(eq(comicImage.id, existing.id));
            updated++;
          } else {
            // Record exists and URL is the same - don't count as skipped
            // This is "no skipped records" behavior
            skipped++;
          }
        } else {
          // Insert new record - use onConflictDoNothing to handle duplicate URLs
          const result = await db
            .insert(comicImage)
            .values({
              comicId: img.comicId,
              imageUrl: img.imageUrl,
              imageOrder: img.imageOrder,
            })
            .onConflictDoNothing();

          // Check if insertion was successful by counting affected rows
          const resultWithCount = result as unknown as { rowCount?: number };
          if (resultWithCount.rowCount && resultWithCount.rowCount > 0) {
            inserted++;
          } else {
            // URL already exists for another comic - count as skipped
            skipped++;
          }
        }
      }

      return { inserted, skipped, updated };
    } else {
      // Original: onConflictDoNothing for non-force mode
      const result = await db.insert(comicImage).values(imageUrls).onConflictDoNothing().returning();

      return {
        inserted: result.length,
        skipped: imageUrls.length - result.length,
        updated: 0,
      };
    }
  }

  async insertBatch(data: ComicSeed[]): Promise<EntityResult> {
    const startTime = Date.now();
    let inserted = 0;
    let skipped = 0;
    let updated = 0;
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];
    const strategy = this.options.imageStrategy ?? "urls";
    const totalComics = data.length;

    // Track progress with ETA
    const chunkTimings: number[] = [];
    const ETA_WINDOW_SIZE = 5;

    const formatDuration = (ms: number): string => {
      if (ms < 1000) return `${ms}ms`;
      const seconds = Math.floor(ms / 1000);
      const minutes = Math.floor(seconds / 60);
      if (minutes > 0) return `${minutes}m ${seconds % 60}s`;
      return `${seconds}s`;
    };

    // Process in parallel batches of PARALLEL_BATCH_SIZE comics
    for (let batchStart = 0; batchStart < data.length; batchStart += PARALLEL_BATCH_SIZE) {
      const batchStartTime = Date.now();
      const batch = data.slice(batchStart, batchStart + PARALLEL_BATCH_SIZE);

      const results = await Promise.allSettled(batch.map((item) => this.processComicImages(item, strategy)));

      for (let j = 0; j < results.length; j++) {
        const result = results[j];
        if (result.status === "fulfilled") {
          inserted += result.value.inserted;
          skipped += result.value.skipped;
          updated += result.value.updated;
        } else {
          const message = result.reason instanceof Error ? result.reason.message : String(result.reason);
          errors.push({
            itemIndex: batchStart + j,
            value: batch[j],
            message,
          });
          if (this.options.verbose) {
            logger.debug(`Error inserting comic images: ${message}`);
          }
        }
      }

      // Calculate progress and ETA
      const chunkElapsed = Date.now() - batchStartTime;
      chunkTimings.push(chunkElapsed);
      if (chunkTimings.length > ETA_WINDOW_SIZE) chunkTimings.shift();

      const processed = Math.min(batchStart + PARALLEL_BATCH_SIZE, totalComics);

      if (this.options.verbose || (batchStart + PARALLEL_BATCH_SIZE) % 50 === 0) {
        const avgChunkTime = chunkTimings.reduce((a, b) => a + b, 0) / chunkTimings.length;
        const remainingComics = totalComics - processed;
        const eta = formatDuration(Math.round(avgChunkTime * (remainingComics / PARALLEL_BATCH_SIZE)));
        const elapsed = formatDuration(Date.now() - startTime);

        logger.info(
          `[comic-images] Progress: ${processed}/${totalComics} | inserted: ${inserted}, updated: ${updated}, skipped: ${skipped} | ETA: ${eta} | elapsed: ${elapsed}`
        );
      }
    }

    const duration = Date.now() - startTime;

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
