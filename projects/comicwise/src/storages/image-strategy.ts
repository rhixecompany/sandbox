/**
 * ImageStrategy - Strategy pattern dispatcher for image handling
 *
 * Supports three modes:
 * 1. "urls" - Use original URLs unchanged (no downloading/uploading)
 * 2. "local" - Download images to local filesystem with caching
 * 3. "imagekit" - Upload to ImageKit CDN and return CDN URLs
 *
 * Features:
 * - Dynamic strategy selection based on configuration
 * - Batch processing with concurrency control
 * - Fallback to original URLs on error
 * - Consistent error handling
 */

import { logger } from "@/scripts/seed/logger";
import { imageDownloader, type ImageDownloadResult } from "@/storages/image-downloader";
import { imageKitUploader, type ImageUploadResult } from "@/storages/image-kit-uploader";

import type { ImageStrategyContext } from "@/scripts/seed/types";

export type ImageResult = ImageDownloadResult | ImageUploadResult;

export class ImageStrategy {
  private mode: "imagekit" | "local" | "urls";
  private context: ImageStrategyContext;

  constructor(context: ImageStrategyContext) {
    this.mode = context.mode || "urls";
    this.context = context;
    logger.debug(`ImageStrategy initialized with mode: ${this.mode}`);
  }

  async processImage(url: string, entityType: string, entityId: number | string): Promise<ImageResult> {
    if (!url) {
      return {
        success: false,
        error: "Empty URL",
      };
    }

    switch (this.mode) {
      case "local":
        return await imageDownloader.download(url, entityType, entityId);

      case "imagekit":
        return await imageKitUploader.upload(url, entityType, entityId);

      case "urls":
      default:
        return {
          success: true,
          url,
        };
    }
  }

  async batchProcess(
    urls: string[],
    entityType: string,
    entityId: number | string,
    concurrency: number = 5
  ): Promise<ImageResult[]> {
    if (!urls || urls.length === 0) {
      return [];
    }

    logger.debug(`Processing ${urls.length} images with concurrency=${concurrency}`);

    const results: ImageResult[] = [];
    const queue = [...urls];
    const active: Promise<void>[] = [];

    const processUrl = async (url: string): Promise<void> => {
      try {
        const result = await this.processImage(url, entityType, entityId);
        results.push(result);
      } catch (error) {
        const errorMessage = error instanceof Error ? error.message : String(error);
        logger.warn(`Image processing error: ${errorMessage}`);
        results.push({
          success: false,
          error: errorMessage,
          url,
        });
      }
    };

    while (queue.length > 0 || active.length > 0) {
      while (active.length < concurrency && queue.length > 0) {
        const url = queue.shift()!;
        const promise = processUrl(url);
        active.push(promise);
        const cleanup = (): void => {
          const idx = active.indexOf(promise);
          if (idx > -1) {
            // eslint-disable-next-line @typescript-eslint/no-floating-promises
            active.splice(idx, 1);
          }
        };
        void promise.then(cleanup);
        void promise.catch(cleanup);
      }

      if (active.length > 0) {
        await Promise.race(active);
      }
    }

    return results;
  }

  getMode(): "imagekit" | "local" | "urls" {
    return this.mode;
  }

  setMode(mode: "imagekit" | "local" | "urls"): void {
    this.mode = mode;
    logger.debug(`ImageStrategy mode changed to: ${this.mode}`);
  }
}

export function createImageStrategy(context: ImageStrategyContext): ImageStrategy {
  return new ImageStrategy(context);
}
