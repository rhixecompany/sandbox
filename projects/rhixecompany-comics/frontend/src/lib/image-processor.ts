/**
 * Image Processor - Memory-safe image optimization using sharp
 *
 * Features:
 * - Streaming pipeline for low memory usage
 * - Max dimension resizing while preserving aspect ratio
 * - WebP conversion for ~60-70% size reduction
 * - Progress tracking with bytes saved
 * - Graceful error handling
 */

/* eslint-disable security/detect-non-literal-fs-filename */

import fs from "node:fs/promises";
import path from "node:path";
import sharp from "sharp";

export interface OptimizeOptions {
  format?: "jpeg" | "png" | "webp";
  maxHeight: number;
  maxWidth: number;
  quality: number;
}

export interface OptimizeResult {
  error?: string;
  newSize?: number;
  originalSize?: number;
  savedBytes?: number;
  savedPercent?: number;
  success: boolean;
}

const DEFAULT_OPTIONS: Required<OptimizeOptions> = {
  maxWidth: 1200,
  maxHeight: 2000,
  quality: 75,
  format: "webp",
};

export async function optimizeImage(
  inputPath: string,
  options: Partial<OptimizeOptions> = {}
): Promise<OptimizeResult> {
  const opts: Required<OptimizeOptions> = {
    maxWidth: options.maxWidth ?? DEFAULT_OPTIONS.maxWidth,
    maxHeight: options.maxHeight ?? DEFAULT_OPTIONS.maxHeight,
    quality: options.quality ?? DEFAULT_OPTIONS.quality,
    format: options.format ?? DEFAULT_OPTIONS.format,
  };

  try {
    const inputStats = await fs.stat(inputPath);
    const originalSize = inputStats.size;

    if (originalSize === 0) {
      return { success: false, error: "Empty file" };
    }

    const sharpInstance = sharp(inputPath, {
      limitInputPixels: false,
      sequentialRead: true,
    });

    const metadata = await sharpInstance.metadata();
    const { width = 0, height = 0 } = metadata;

    if (width === 0 || height === 0) {
      return { success: false, error: "Invalid image dimensions" };
    }

    const needsResize = width > opts.maxWidth || height > opts.maxHeight;
    const needsConvert = opts.format !== "png" && metadata.format !== opts.format;

    if (!needsResize && !needsConvert) {
      const newStats = await fs.stat(inputPath);
      if (newStats.size < originalSize * 0.95) {
        return {
          success: true,
          originalSize,
          newSize: newStats.size,
          savedBytes: originalSize - newStats.size,
          savedPercent: ((originalSize - newStats.size) / originalSize) * 100,
        };
      }
      return { success: true, originalSize, newSize: originalSize };
    }

    let pipeline = sharp(inputPath, { limitInputPixels: false, sequentialRead: true });

    if (needsResize) {
      pipeline = pipeline.resize(opts.maxWidth, opts.maxHeight, {
        fit: "inside",
        withoutEnlargement: true,
      });
    }

    switch (opts.format) {
      case "webp":
        pipeline = pipeline.webp({ quality: opts.quality, effort: 4 });
        break;
      case "jpeg":
        pipeline = pipeline.jpeg({ quality: opts.quality, mozjpeg: true });
        break;
      case "png":
        pipeline = pipeline.png({ compressionLevel: 9, quality: opts.quality });
        break;
    }

    const tempPath = `${inputPath}.optimizing`;
    await pipeline.toFile(tempPath);

    const newStats = await fs.stat(tempPath);
    const newSize = newStats.size;

    if (newSize >= originalSize) {
      await fs.unlink(tempPath).catch(() => {});
      return {
        success: true,
        originalSize,
        newSize: originalSize,
        savedBytes: 0,
        savedPercent: 0,
      };
    }

    await fs.rename(tempPath, inputPath);

    const savedBytes = originalSize - newSize;
    const savedPercent = (savedBytes / originalSize) * 100;

    return {
      success: true,
      originalSize,
      newSize,
      savedBytes,
      savedPercent,
    };
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);

    if (message.includes("Input buffer") || message.includes("image expected")) {
      return { success: false, error: "Invalid image format" };
    }

    if (message.includes("EMFILE") || message.includes("ENFILE")) {
      return { success: false, error: "Too many open files" };
    }

    return { success: false, error: message };
  }
}

export async function getImageDimensions(imagePath: string): Promise<{ height: number; width: number } | null> {
  try {
    const metadata = await sharp(imagePath).metadata();
    if (metadata.width && metadata.height) {
      return { height: metadata.height, width: metadata.width };
    }
    return null;
  } catch {
    return null;
  }
}

export async function isImageFile(filePath: string): Promise<boolean> {
  try {
    const ext = path.extname(filePath).toLowerCase();
    const validExts = [".jpg", ".jpeg", ".png", ".webp", ".avif", ".gif"];

    if (!validExts.includes(ext)) {
      return false;
    }

    await sharp(filePath).metadata();
    return true;
  } catch {
    return false;
  }
}

export async function scanDirectoryForImages(dirPath: string, recursive: boolean = true): Promise<string[]> {
  const images: string[] = [];

  async function scan(currentPath: string): Promise<void> {
    try {
      const entries = await fs.readdir(currentPath, { withFileTypes: true });

      for (const entry of entries) {
        const fullPath = path.join(currentPath, entry.name);

        if (entry.isDirectory() && recursive) {
          await scan(fullPath);
        } else if (entry.isFile() && (await isImageFile(fullPath))) {
          images.push(fullPath);
        }
      }
    } catch {
      // Skip directories we can't read
    }
  }

  await scan(dirPath);
  return images;
}

export interface ReprocessStats {
  errors: number;
  processed: number;
  skipped: number;
  totalNewBytes: number;
  totalOriginalBytes: number;
  totalSavedBytes: number;
}

export async function reprocessImagesInDirectory(
  dirPath: string,
  options: Partial<OptimizeOptions>,
  onProgress?: (current: number, total: number, saved: number) => void
): Promise<ReprocessStats> {
  const stats: ReprocessStats = {
    processed: 0,
    skipped: 0,
    errors: 0,
    totalSavedBytes: 0,
    totalOriginalBytes: 0,
    totalNewBytes: 0,
  };

  const images = await scanDirectoryForImages(dirPath);
  const total = images.length;
  let index = 0;

  for (const imagePath of images) {
    index++;
    try {
      const originalStats = await fs.stat(imagePath);
      const originalSize = originalStats.size;

      const result = await optimizeImage(imagePath, options);

      if (result.success && result.savedBytes && result.savedBytes > 0) {
        stats.processed++;
        stats.totalOriginalBytes += originalSize;
        stats.totalNewBytes += result.newSize!;
        stats.totalSavedBytes += result.savedBytes;
      } else if (result.success) {
        stats.skipped++;
      } else {
        stats.errors++;
      }

      if (onProgress) {
        onProgress(index, total, stats.totalSavedBytes);
      }
    } catch {
      stats.errors++;
    }
  }

  return stats;
}
