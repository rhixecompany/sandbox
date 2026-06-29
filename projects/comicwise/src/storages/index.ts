/**
 * Storage System Exports
 * Central export point for image storage utilities
 */

export {
  clearUrlCache,
  clearUrlToPathCache,
  extractExtension,
  extractOriginalName,
  getCachedPathForUrl,
  getUrlCacheStats,
  getUrlToPathCacheStats,
  imageDownloader,
  isUrlCached,
  markUrlAsDownloaded,
  sanitizeSlug,
  type DownloadOptions,
  type EntityMeta,
  type ImageDownloadResult,
} from "./image-downloader";

export { createImageStrategy, type ImageResult } from "./image-strategy";

export { type ImageUploadResult } from "./image-kit-uploader";
