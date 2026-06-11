/**
 * Storage System Exports
 * Central export point for image storage utilities
 */

export {
  clearUrlCache,
  clearUrlToPathCache,
  type DownloadOptions,
  type EntityMeta,
  extractExtension,
  extractOriginalName,
  getCachedPathForUrl,
  getUrlCacheStats,
  getUrlToPathCacheStats,
  imageDownloader,
  type ImageDownloadResult,
  isUrlCached,
  markUrlAsDownloaded,
  sanitizeSlug,
} from "./image-downloader";

export { createImageStrategy, type ImageResult } from "./image-strategy";

export { type ImageUploadResult } from "./image-kit-uploader";
