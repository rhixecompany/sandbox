/**
 * ImageDownloader - handles local filesystem image caching with retry logic
 *
 * Features:
 * - Local filesystem caching to avoid re-downloading
 * - In-memory URL cache for current session
 * - Exponential backoff retry logic (3 attempts)
 * - HTTP request with User-Agent header
 * - Safe URL validation (block localhost/private IPs)
 * - Dynamic path generation based on entity metadata
 * - Pre-download validation (HEAD request)
 * - Pre-deduplication check before downloading
 * - Preserve original file extensions
 * - Filesystem-safe slug sanitization
 */

/* eslint-disable security/detect-non-literal-fs-filename */

import { createWriteStream } from "node:fs";
import fs from "node:fs/promises";
import path from "node:path";
import { pipeline } from "node:stream/promises";

import { optimizeImage } from "@/lib/image-processor";
import { type DeduplicationResult, findDuplicateByHash } from "@/scripts/seed/helpers/image-deduplicator";
import { logger } from "@/scripts/seed/logger";

const urlToPathCache = new Map<string, string>();

export interface ImageOptimizationConfig {
  enabled: boolean;
  maxHeight: number;
  maxWidth: number;
  quality: number;
}

let optimizationConfig: ImageOptimizationConfig = {
  maxWidth: 1200,
  maxHeight: 2000,
  quality: 75,
  enabled: false,
};

export function configureImageDownloader(config: Partial<ImageOptimizationConfig>): void {
  optimizationConfig = {
    ...optimizationConfig,
    ...config,
    enabled: config.enabled ?? optimizationConfig.enabled,
  };
  logger.debug(
    `ImageDownloader configured: optimization=${optimizationConfig.enabled}, maxWidth=${optimizationConfig.maxWidth}, quality=${optimizationConfig.quality}`
  );
}

export function getOptimizationConfig(): ImageOptimizationConfig {
  return { ...optimizationConfig };
}

export interface ImageDownloadResult {
  error?: string;
  filePath?: string;
  fromCache?: boolean;
  fromDuplicate?: boolean;
  originalPath?: string;
  success: boolean;
  url?: string;
}

export interface EntityMeta {
  chapterNum?: number;
  comicSlug?: string;
  imageIndex?: number;
  isCover?: boolean;
  originalExtension?: string;
  originalName?: string;
  pageNum?: number;
  slug?: string;
}

export interface DownloadOptions {
  entityMeta?: EntityMeta;
  maxRetries?: number;
  skipIfExists?: boolean;
  timeout?: number;
}

export function extractOriginalName(url: string): string {
  try {
    const urlObj = new URL(url);
    const pathname = urlObj.pathname;
    const filename = pathname.split("/").pop() || "image";
    const nameWithoutExt = filename.replace(/\.[^./?#]+(?:[?#]|$)/, "");
    return nameWithoutExt.replaceAll(/[^a-zA-Z0-9_-]/g, "_").slice(0, 50) || "image";
  } catch {
    return "image";
  }
}

const urlCache = new Map<string, string>();

const MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024;
const DEFAULT_TIMEOUT_MS = 15000;

export function clearUrlCache(): void {
  urlCache.clear();
}

export function getUrlCacheStats(): { size: number; urls: string[] } {
  return {
    size: urlCache.size,
    urls: Array.from(urlCache.keys()),
  };
}

export function sanitizeSlug(slug: string): string {
  return (
    slug
      // eslint-disable-next-line no-control-regex
      .replaceAll(/[<>:"/\\|?*\x00-\x1f]/g, "_")
      .replaceAll(/\.+/g, "_")
      .replaceAll(/-+/g, "-")
      .replaceAll(/^[-.\s]+|[-.\s]+$/g, "")
      .slice(0, 200)
  );
}

export function extractExtension(url: string): string {
  try {
    const urlObj = new URL(url);
    const pathname = urlObj.pathname;
    const match = pathname.match(/\.([^./?#]+)(?:[?#]|$)/);
    if (match) {
      const ext = match[1].toLowerCase();
      const allowedExts = ["jpg", "jpeg", "png", "webp", "avif", "gif", "svg"];
      return allowedExts.includes(ext) ? ext : "jpg";
    }
    return "jpg";
  } catch {
    return "jpg";
  }
}

export class ImageDownloader {
  private cacheDir: string;
  private maxRetries: number;
  private baseDelay: number;
  private timeout: number;

  constructor(
    cacheDir: string = "./public/uploads/comics",
    maxRetries: number = 3,
    timeout: number = DEFAULT_TIMEOUT_MS
  ) {
    this.cacheDir = cacheDir;
    this.maxRetries = maxRetries;
    this.baseDelay = 1000;
    this.timeout = timeout;
  }

  generateDynamicPath(entityType: string, entityMeta: EntityMeta): { dir: string; filename: string } {
    const ext = entityMeta.originalExtension || "jpg";
    const slug = entityMeta.slug || entityMeta.comicSlug || "unknown";
    const sanitizedSlug = sanitizeSlug(slug);

    if (entityType === "comics") {
      if (entityMeta.isCover) {
        return {
          dir: path.join(this.cacheDir, sanitizedSlug),
          filename: `cover.${ext}`,
        };
      }
      const originalName = entityMeta.originalName || "image";
      const safeOriginalName = sanitizeSlug(originalName).slice(0, 50) || "image";
      return {
        dir: path.join(this.cacheDir, sanitizedSlug, "images"),
        filename: `${safeOriginalName}.${ext}`,
      };
    }

    if (entityType === "chapters") {
      const chapterNum = entityMeta.chapterNum ?? 1;
      const originalName = entityMeta.originalName || "page";
      const safeOriginalName = sanitizeSlug(originalName).slice(0, 50) || "page";
      return {
        dir: path.join(this.cacheDir.replace("/comics", "/chapters"), sanitizedSlug, String(chapterNum)),
        filename: `${safeOriginalName}.${ext}`,
      };
    }

    const fallbackSlug = entityMeta.slug || String(entityMeta.comicSlug || "unknown");
    return {
      dir: path.join(this.cacheDir, sanitizedSlug),
      filename: `${sanitizeSlug(fallbackSlug)}.${ext}`,
    };
  }

  private isSafeUrl(urlString: string): boolean {
    try {
      const url = new URL(urlString);
      if (!/^https?:$/.test(url.protocol)) return false;

      const hostname = url.hostname.toLowerCase();
      if (
        hostname === "localhost" ||
        hostname === "127.0.0.1" ||
        hostname === "::1" ||
        hostname === "0.0.0.0" ||
        /^10\./.test(hostname) ||
        /^192\.168\./.test(hostname) ||
        /^172\.(1[6-9]|2[0-9]|3[0-1])\./.test(hostname) ||
        hostname.endsWith(".local")
      ) {
        return false;
      }
      return true;
    } catch {
      return false;
    }
  }

  async validateBeforeDownload(url: string): Promise<{ contentType?: string; error?: string; valid: boolean }> {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 5000);

      const response = await fetch(url, {
        method: "HEAD",
        signal: controller.signal,
      });

      clearTimeout(timeoutId);

      if (!response.ok) {
        return { valid: false, error: `HTTP ${response.status}: ${response.statusText}` };
      }

      const contentType = response.headers.get("content-type");
      if (!contentType || !contentType.startsWith("image/")) {
        return { valid: false, error: `Not an image: ${contentType}` };
      }

      const contentLength = response.headers.get("content-length");
      if (contentLength) {
        const size = parseInt(contentLength, 10);
        if (size > MAX_IMAGE_SIZE_BYTES) {
          return { valid: false, error: `Image too large: ${(size / 1024 / 1024).toFixed(2)}MB (max: 10MB)` };
        }
      }

      return { valid: true, contentType };
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      if (message.includes("aborted")) {
        return { valid: false, error: "Request timeout" };
      }
      return { valid: false, error: `Validation failed: ${message}` };
    }
  }

  async checkDuplicate(filePath: string): Promise<DeduplicationResult | null> {
    try {
      if (await this.fileExists(filePath)) {
        return { isDuplicate: false };
      }

      const duplicatePath = await findDuplicateByHash(filePath);
      if (duplicatePath) {
        return {
          isDuplicate: true,
          originalPath: duplicatePath,
        };
      }

      return null;
    } catch {
      return null;
    }
  }

  private async getUniqueFilename(dir: string, filename: string): Promise<string> {
    const ext = path.extname(filename);
    const base = path.basename(filename, ext);
    let candidate = filename;
    let counter = 1;

    while (await this.fileExists(path.join(dir, candidate))) {
      candidate = `${base}_${counter}${ext}`;
      counter++;
    }

    return candidate;
  }

  async download(
    url: string,
    entityType: string,
    entityId: number | string,
    options: DownloadOptions = {}
  ): Promise<ImageDownloadResult> {
    const { entityMeta, maxRetries = this.maxRetries, timeout = this.timeout, skipIfExists = true } = options;

    if (!url) {
      return { success: false, error: "Empty URL" };
    }

    if (!this.isSafeUrl(url)) {
      logger.debug(`Blocked unsafe URL: ${url}`);
      return { success: false, error: "Unsafe URL (localhost/private IP)" };
    }

    const extension = extractExtension(url);
    const meta: EntityMeta = {
      ...entityMeta,
      originalExtension: entityMeta?.originalExtension || extension,
    };

    const { dir: entityDir, filename } = this.generateDynamicPath(entityType, meta);
    const uniqueFilename = await this.getUniqueFilename(entityDir, filename);
    const filePath = path.join(entityDir, uniqueFilename);

    const cacheKey = `${entityType}:${entityId}:${url}`;

    if (urlCache.has(cacheKey)) {
      logger.debug(`In-memory cache hit: ${cacheKey}`);
      return {
        success: true,
        filePath: urlCache.get(cacheKey),
        url,
        fromCache: true,
      };
    }

    if (skipIfExists && (await this.fileExists(filePath))) {
      logger.debug(`Filesystem cache hit (skipIfExists): ${filePath}`);
      const resultPath = this.pathToPublicUrl(filePath);
      urlCache.set(cacheKey, resultPath);
      urlToPathCache.set(url, resultPath);
      return {
        success: true,
        filePath: resultPath,
        url,
        fromCache: true,
      };
    }

    if (await this.fileExists(filePath)) {
      logger.debug(`Filesystem cache hit: ${filePath}`);
      const resultPath = this.pathToPublicUrl(filePath);
      urlCache.set(cacheKey, resultPath);
      urlToPathCache.set(url, resultPath);
      return {
        success: true,
        filePath: resultPath,
        url,
        fromCache: true,
      };
    }

    const existingPathByUrl = urlToPathCache.get(url);
    if (
      existingPathByUrl &&
      (await this.fileExists(existingPathByUrl.replace("/uploads/comics/", "./public/uploads/comics/")))
    ) {
      logger.debug(`URL already downloaded previously: ${url} → ${existingPathByUrl}`);
      urlCache.set(cacheKey, existingPathByUrl);
      return {
        success: true,
        filePath: existingPathByUrl,
        url,
        fromCache: true,
        fromDuplicate: true,
        originalPath: existingPathByUrl,
      };
    }

    const tempPath = path.join(entityDir, `temp_${Date.now()}_${uniqueFilename}`);
    await this.ensureDir(entityDir);

    let downloaded = false;
    let lastError: Error | undefined;

    const validation = await this.validateBeforeDownload(url);
    if (!validation.valid) {
      logger.debug(`Pre-validation failed for ${url}: ${validation.error}`);
    }

    for (let attempt = 0; attempt < maxRetries; attempt++) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), timeout);

        const response = await fetch(url, {
          headers: {
            "User-Agent":
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            Accept: "image/webp,image/apng,image/*,*/*",
            "Accept-Encoding": "gzip, deflate, br",
          },
          signal: controller.signal,
        });

        clearTimeout(timeoutId);

        if (!response.ok) {
          throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        if (!response.body) {
          throw new Error("No response body");
        }

        const writeStream = createWriteStream(tempPath);
        await pipeline(response.body as unknown as AsyncIterable<Uint8Array>, writeStream);

        downloaded = true;
        break;
      } catch (error) {
        lastError = error instanceof Error ? error : new Error(String(error));
        logger.debug(`Attempt ${attempt + 1}/${maxRetries} failed: ${lastError.message}`);

        if (attempt < maxRetries - 1) {
          const delay = this.baseDelay * Math.pow(2, attempt);
          await this.sleep(delay);
        }
      }
    }

    if (!downloaded) {
      logger.warn(`Failed to download ${url} after ${maxRetries} attempts`);
      return {
        success: false,
        error: lastError?.message || "Download failed after retries",
        url,
      };
    }

    const deduplicationResult = await this.checkDuplicate(tempPath);
    if (deduplicationResult?.isDuplicate && deduplicationResult.originalPath) {
      try {
        await fs.unlink(tempPath);
        const resultPath = this.pathToPublicUrl(deduplicationResult.originalPath);
        urlCache.set(cacheKey, resultPath);
        urlToPathCache.set(url, resultPath);
        logger.debug(`Deduplicated: ${url} → ${deduplicationResult.originalPath}`);
        return {
          success: true,
          filePath: resultPath,
          url,
          fromDuplicate: true,
          originalPath: deduplicationResult.originalPath,
        };
      } catch {
        // Continue with the downloaded file if unlink fails
      }
    }

    if (optimizationConfig.enabled) {
      const isCover = entityMeta?.isCover === true;
      const optimizeResult = await optimizeImage(tempPath, {
        maxWidth: isCover ? 400 : optimizationConfig.maxWidth,
        maxHeight: isCover ? 600 : optimizationConfig.maxHeight,
        quality: isCover ? 80 : optimizationConfig.quality,
        format: "webp",
      });

      if (optimizeResult.success && optimizeResult.savedPercent && optimizeResult.savedPercent > 1) {
        logger.debug(
          `Optimized ${url}: saved ${optimizeResult.savedPercent.toFixed(1)}% (${(optimizeResult.originalSize! / 1024).toFixed(1)}KB → ${(optimizeResult.newSize! / 1024).toFixed(1)}KB)`
        );
      } else if (!optimizeResult.success) {
        logger.debug(`Optimization failed for ${url}: ${optimizeResult.error}`);
      }
    }

    try {
      if (tempPath !== filePath) {
        await fs.rename(tempPath, filePath);
      }
    } catch {
      // File might already be at final path
    }

    const resultPath = this.pathToPublicUrl(filePath);
    urlCache.set(cacheKey, resultPath);
    urlToPathCache.set(url, resultPath);

    logger.debug(`Downloaded: ${url} → ${filePath}`);
    return {
      success: true,
      filePath: resultPath,
      url,
      fromCache: false,
    };
  }

  private pathToPublicUrl(absolutePath: string): string {
    const uploadsDir = path.resolve("./public/uploads");
    const relative = path.relative(uploadsDir, absolutePath);
    const normalized = relative.replaceAll("\\", "/");

    // Check if path already starts with an entity folder
    if (normalized.startsWith("chapters/")) {
      return `/uploads/${normalized}`;
    }

    if (normalized.startsWith("comics/")) {
      return `/uploads/${normalized}`;
    }

    // Fallback for unexpected paths (shouldn't happen with current logic)
    return `/uploads/comics/${normalized}`;
  }

  private async fileExists(filePath: string): Promise<boolean> {
    try {
      await fs.access(filePath);
      return true;
    } catch {
      return false;
    }
  }

  private async ensureDir(dirPath: string): Promise<void> {
    try {
      await fs.mkdir(dirPath, { recursive: true });
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : String(error);
      logger.warn(`Failed to create directory ${dirPath}: ${errorMessage}`);
    }
  }

  private sleep(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}

export const imageDownloader = new ImageDownloader();

export function clearUrlToPathCache(): void {
  urlToPathCache.clear();
}

export function getUrlToPathCacheStats(): { size: number; urls: string[] } {
  return {
    size: urlToPathCache.size,
    urls: Array.from(urlToPathCache.keys()),
  };
}

export function isUrlCached(url: string): boolean {
  return urlToPathCache.has(url);
}

export function getCachedPathForUrl(url: string): null | string {
  return urlToPathCache.get(url) || null;
}

export function markUrlAsDownloaded(url: string, path: string): void {
  urlToPathCache.set(url, path);
}
