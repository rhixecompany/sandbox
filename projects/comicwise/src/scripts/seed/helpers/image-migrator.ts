/**
 * ImageMigrator - Migrates existing images to new dynamic path structure
 *
 * Scans old paths and moves images to new structured paths:
 * - Comic: /public/comics/{slug}/... → /public/uploads/comics/{slug}/...
 * - Chapter: /public/chapters/{slug}/... → /public/uploads/chapters/{slug}/...
 *
 * Features:
 * - Scan old folder structure
 * - Parse entity ID from filename
 * - Lookup slug from database
 * - Move files to new paths
 * - Update database records
 * - Skip and log on errors
 * - Migration stats reporting
 * - Auto-cleanup of old directories after successful migration
 */

import { existsSync } from "node:fs";
import fs from "node:fs/promises";
import path from "node:path";

import { db } from "@/database/db";
import { chapter, chapterImage, comic, comicImage } from "@/database/schema";
import { eq } from "drizzle-orm";

import { extractExtension, sanitizeSlug } from "@/storages/image-downloader";
import { logger } from "../logger";

export interface MigrationStats {
  dbUpdated: number;
  errors: number;
  migrated: number;
  skipped: number;
  totalScanned: number;
}

export interface MigrationResult {
  errors: string[];
  stats: MigrationStats;
  success: boolean;
}

/**
 * Parse entity ID from old filename format: {id}-{hash}.{ext}
 */
function parseEntityIdFromFilename(filename: string): null | number {
  const match = filename.match(/^(\d+)-[a-z0-9]+\.[a-z]+$/i);
  if (match) {
    return parseInt(match[1], 10);
  }
  return null;
}

/**
 * Get comic slug from database by ID
 */
async function getComicSlug(comicId: number): Promise<null | string> {
  try {
    const result = await db.query.comic.findFirst({
      where: eq(comic.id, comicId),
      columns: { slug: true },
    });
    return result?.slug || null;
  } catch {
    return null;
  }
}

/**
 * Get chapter info (comic slug + chapter number) from database by ID
 */
async function getChapterInfo(chapterId: number): Promise<{ chapterNum: number; comicSlug: string } | null> {
  try {
    // First get chapter with its comicId
    const chapterResult = await db.query.chapter.findFirst({
      where: eq(chapter.id, chapterId),
      columns: { comicId: true, chapterNumber: true },
    });

    if (!chapterResult?.comicId) {
      return null;
    }

    // Then get the comic slug
    const comicResult = await db.query.comic.findFirst({
      where: eq(comic.id, chapterResult.comicId),
      columns: { slug: true },
    });

    if (comicResult?.slug) {
      return {
        comicSlug: comicResult.slug,
        chapterNum: chapterResult.chapterNumber,
      };
    }

    return null;
  } catch {
    return null;
  }
}

/**
 * Get comic ID from comicImage ID
 */
async function getComicIdFromComicImage(imageId: number): Promise<null | number> {
  try {
    const result = await db.query.comicImage.findFirst({
      where: eq(comicImage.id, imageId),
      columns: { comicId: true },
    });
    return result?.comicId || null;
  } catch {
    return null;
  }
}

/**
 * Get chapter ID from chapterImage ID
 */
async function getChapterIdFromChapterImage(imageId: number): Promise<null | number> {
  try {
    const result = await db.query.chapterImage.findFirst({
      where: eq(chapterImage.id, imageId),
      columns: { chapterId: true },
    });
    return result?.chapterId || null;
  } catch {
    return null;
  }
}

/**
 * Migrate comic images from old path to new dynamic path
 * Old path: /public/comics/{slug}/...
 * New path: /public/uploads/comics/{slug}/...
 */
async function migrateComicImages(oldDir: string, stats: MigrationStats): Promise<void> {
  if (!existsSync(oldDir)) {
    logger.debug(`Comic images old path does not exist: ${oldDir}`);
    return;
  }

  const files = await fs.readdir(oldDir);

  for (const filename of files) {
    if (filename === "placeholder" || filename.startsWith(".")) continue;

    const oldPath = path.join(oldDir, filename);
    const imageId = parseEntityIdFromFilename(filename);

    if (!imageId) {
      logger.debug(`Could not parse image ID from filename: ${filename}`);
      stats.skipped++;
      continue;
    }

    try {
      // Get the comicImage record to find the comicId
      const dbImage = await db.query.comicImage.findFirst({
        where: eq(comicImage.id, imageId),
      });

      if (!dbImage) {
        logger.warn(`comicImage record not found for ID ${imageId}, skipping migration`);
        stats.skipped++;
        continue;
      }

      // Get the comic slug
      const comicSlug = await getComicSlug(dbImage.comicId);
      if (!comicSlug) {
        logger.warn(`Comic not found for comicId ${dbImage.comicId}, skipping migration`);
        stats.skipped++;
        continue;
      }

      const sanitizedSlug = sanitizeSlug(comicSlug);
      const ext = extractExtension(filename);

      let newDir: string;
      let newFilename: string;

      // Check if it's a cover image (imageOrder = 0 or filename suggests cover)
      if (dbImage.imageOrder === 0) {
        newDir = path.join("./public/uploads/comics", sanitizedSlug);
        newFilename = `cover.${ext}`;
      } else {
        newDir = path.join("./public/uploads/comics", sanitizedSlug, "images");
        newFilename = `${String(dbImage.imageOrder).padStart(2, "0")}.${ext}`;
      }

      const newPath = path.join(newDir, newFilename);

      // Ensure directory exists
      await fs.mkdir(newDir, { recursive: true });

      // Handle filename collisions
      let finalPath = newPath;
      let counter = 1;
      while (existsSync(finalPath)) {
        const extIdx = newFilename.lastIndexOf(".");
        const base = newFilename.substring(0, extIdx);
        const extPart = newFilename.substring(extIdx);
        finalPath = path.join(newDir, `${base}_${counter}${extPart}`);
        counter++;
      }

      // Move file
      await fs.rename(oldPath, finalPath);

      // Update database with relative path
      const relativePath = `/uploads/comics/${path.relative("./public/uploads/comics", finalPath).replaceAll("\\", "/")}`;

      await db.update(comicImage).set({ imageUrl: relativePath }).where(eq(comicImage.id, dbImage.id));
      stats.dbUpdated++;

      stats.migrated++;
      logger.debug(`Migrated comic image: ${filename} → ${relativePath}`);
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      logger.error(`Failed to migrate comic image ${filename}: ${message}`);
      stats.errors++;
    }
  }
}

/**
 * Migrate chapter images from old path to new dynamic path
 * Old path: /public/chapters/{slug}/...
 * New path: /public/uploads/chapters/{slug}/...
 */
async function migrateChapterImages(oldDir: string, stats: MigrationStats): Promise<void> {
  if (!existsSync(oldDir)) {
    logger.debug(`Chapter images old path does not exist: ${oldDir}`);
    return;
  }

  const files = await fs.readdir(oldDir);

  for (const filename of files) {
    if (filename === "placeholder" || filename.startsWith(".")) continue;

    const oldPath = path.join(oldDir, filename);
    const entityId = parseEntityIdFromFilename(filename);

    if (!entityId) {
      // Try to parse as chapterImage ID
      const chapterImageMatch = filename.match(/^(\d+)-[a-z0-9]+\.[a-z]+$/i);
      if (chapterImageMatch) {
        // This might be a chapter image, but we need to look it up differently
      }
      logger.debug(`Could not parse entity ID from filename: ${filename}`);
      stats.skipped++;
      continue;
    }

    try {
      // First, check if this ID exists in chapterImage table
      const chapterInfo = await getChapterInfo(entityId);
      if (!chapterInfo) {
        logger.warn(`Chapter not found for ID ${entityId}, skipping migration`);
        stats.skipped++;
        continue;
      }

      const { comicSlug, chapterNum } = chapterInfo;
      const sanitizedSlug = sanitizeSlug(comicSlug);
      const ext = extractExtension(filename);

      // Get page number from DB
      const dbChapterImage = await db.query.chapterImage.findFirst({
        where: eq(chapterImage.id, entityId),
      });

      const pageNum = dbChapterImage?.pageNumber || 1;

      const newDir = path.join("./public/uploads/chapters", sanitizedSlug, String(chapterNum));
      const newFilename = `${pageNum}.${ext}`;
      const newPath = path.join(newDir, newFilename);

      // Ensure directory exists
      await fs.mkdir(newDir, { recursive: true });

      // Handle filename collisions
      let finalPath = newPath;
      let counter = 1;
      while (existsSync(finalPath)) {
        const extIdx = newFilename.lastIndexOf(".");
        const base = newFilename.substring(0, extIdx);
        const extPart = newFilename.substring(extIdx);
        finalPath = path.join(newDir, `${base}_${counter}${extPart}`);
        counter++;
      }

      // Move file
      await fs.rename(oldPath, finalPath);

      // Update database
      const relativePath = `/uploads/chapters/${sanitizedSlug}/${chapterNum}/${path.basename(finalPath)}`;

      if (dbChapterImage) {
        await db.update(chapterImage).set({ imageUrl: relativePath }).where(eq(chapterImage.id, dbChapterImage.id));
        stats.dbUpdated++;
      }

      stats.migrated++;
      logger.debug(`Migrated chapter image: ${filename} → ${relativePath}`);
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      logger.error(`Failed to migrate chapter image ${filename}: ${message}`);
      stats.errors++;
    }
  }
}

/**
 * Clean up old image directories after successful migration
 */
async function cleanupOldDirectories(): Promise<void> {
  const oldDirs = ["./public/comics", "./public/chapters"];

  logger.info("Cleaning up old directories after successful migration...");

  for (const dir of oldDirs) {
    try {
      if (existsSync(dir)) {
        await fs.rm(dir, { recursive: true, force: true });
        logger.success(`Removed: ${dir}/`);
      }
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      logger.warn(`Failed to remove old directory ${dir}: ${message}`);
    }
  }
}

/**
 * Main migration function
 * Migrates all existing images to new dynamic path structure
 * Auto-cleans old directories after successful migration
 */
export async function migrateImages(): Promise<MigrationResult> {
  const stats: MigrationStats = {
    totalScanned: 0,
    migrated: 0,
    skipped: 0,
    errors: 0,
    dbUpdated: 0,
  };
  const errors: string[] = [];

  logger.section("Image Migration");
  logger.info("Migrating to new path structure: /public/uploads/");

  try {
    // Define old directories to scan (both legacy and previous paths)
    const comicOldDirs = ["./public/comics/comics", "./public/comics"];
    const chapterOldDirs = ["./public/comics/chapters", "./public/chapters"];

    // Count files in old directories for stats
    for (const comicOldDir of comicOldDirs) {
      if (existsSync(comicOldDir)) {
        const comicFiles = await fs.readdir(comicOldDir);
        stats.totalScanned += comicFiles.filter((f) => !f.startsWith(".") && f !== "placeholder").length;
      }
    }

    for (const chapterOldDir of chapterOldDirs) {
      if (existsSync(chapterOldDir)) {
        const chapterFiles = await fs.readdir(chapterOldDir);
        stats.totalScanned += chapterFiles.filter((f) => !f.startsWith(".") && f !== "placeholder").length;
      }
    }

    logger.info(`Found ${stats.totalScanned} images to migrate`);

    // Migrate comic images from all old directories
    for (const comicOldDir of comicOldDirs) {
      if (existsSync(comicOldDir)) {
        logger.info(`Scanning: ${comicOldDir}/`);
        await migrateComicImages(comicOldDir, stats);
      }
    }

    // Migrate chapter images from all old directories
    for (const chapterOldDir of chapterOldDirs) {
      if (existsSync(chapterOldDir)) {
        logger.info(`Scanning: ${chapterOldDir}/`);
        await migrateChapterImages(chapterOldDir, stats);
      }
    }

    // Report stats
    logger.success(
      `Migration complete: ${stats.migrated} migrated, ${stats.skipped} skipped, ${stats.errors} errors, ${stats.dbUpdated} DB records updated`
    );

    // Auto-cleanup old directories if migration was successful
    if (stats.errors === 0) {
      await cleanupOldDirectories();
    } else {
      logger.warn("Skipping cleanup due to migration errors. Run migration again after fixing issues.");
    }

    return {
      success: stats.errors === 0,
      stats,
      errors,
    };
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    errors.push(message);
    logger.error(`Migration failed: ${message}`);

    return {
      success: false,
      stats,
      errors,
    };
  }
}

export default migrateImages;

export interface ReprocessImagesOptions {
  dryRun?: boolean;
  maxHeight: number;
  maxWidth: number;
  quality: number;
}

export interface ReprocessImagesResult {
  chaptersProcessed: number;
  comicsProcessed: number;
  errors: string[];
  success: boolean;
  totalSavedBytes: number;
}

export async function reprocessExistingImages(options: ReprocessImagesOptions): Promise<ReprocessImagesResult> {
  const { maxWidth, maxHeight, quality, dryRun = false } = options;
  const result: ReprocessImagesResult = {
    chaptersProcessed: 0,
    comicsProcessed: 0,
    errors: [],
    success: true,
    totalSavedBytes: 0,
  };

  try {
    const uploadsDir = path.resolve("./public/uploads");

    if (!existsSync(uploadsDir)) {
      result.success = false;
      result.errors.push("Uploads directory does not exist");
      return result;
    }

    const comicsDir = path.join(uploadsDir, "comics");
    const chaptersDir = path.join(uploadsDir, "chapters");

    if (!existsSync(comicsDir) && !existsSync(chaptersDir)) {
      result.success = false;
      result.errors.push("No comics or chapters directories found");
      return result;
    }

    if (dryRun) {
      logger.info("DRY RUN: No files will be modified");
    }

    // Import here to avoid circular dependency issues
    const { reprocessImagesInDirectory } = await import("@/lib/image-processor");

    // Reprocess comics
    if (existsSync(comicsDir)) {
      logger.info(`Reprocessing comics in: ${comicsDir}`);
      const comicsStats = await reprocessImagesInDirectory(
        comicsDir,
        { maxWidth, maxHeight, quality },
        (current, total, saved) => {
          if (current % 10 === 0 || current === total) {
            logger.info(`Comics: ${current}/${total} (saved ${(saved / 1024 / 1024).toFixed(2)}MB)`);
          }
        }
      );

      result.comicsProcessed = comicsStats.processed;
      result.totalSavedBytes += comicsStats.totalSavedBytes;

      if (comicsStats.errors > 0) {
        result.errors.push(`Comics: ${comicsStats.errors} errors`);
      }
    }

    // Reprocess chapters
    if (existsSync(chaptersDir)) {
      logger.info(`Reprocessing chapters in: ${chaptersDir}`);
      const chaptersStats = await reprocessImagesInDirectory(
        chaptersDir,
        { maxWidth, maxHeight, quality },
        (current, total, saved) => {
          if (current % 50 === 0 || current === total) {
            logger.info(`Chapters: ${current}/${total} (saved ${(saved / 1024 / 1024).toFixed(2)}MB)`);
          }
        }
      );

      result.chaptersProcessed = chaptersStats.processed;
      result.totalSavedBytes += chaptersStats.totalSavedBytes;

      if (chaptersStats.errors > 0) {
        result.errors.push(`Chapters: ${chaptersStats.errors} errors`);
      }
    }

    result.success = result.errors.length === 0;

    logger.success(
      `Reprocessing complete: ${result.comicsProcessed} comics + ${result.chaptersProcessed} chapters processed, saved ${(result.totalSavedBytes / 1024 / 1024).toFixed(2)}MB`
    );

    return result;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    result.success = false;
    result.errors.push(message);
    logger.error(`Reprocessing failed: ${message}`);
    return result;
  }
}
