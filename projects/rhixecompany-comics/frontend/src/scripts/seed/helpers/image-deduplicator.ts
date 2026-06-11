/**
 * Image Deduplicator - Content-based deduplication using xxhash
 *
 * Features:
 * - Calculate xxhash64 hash of downloaded image files
 * - Detect duplicates by content hash
 * - Skip/delete duplicate files to save storage
 * - Track deduplication statistics
 * - URL-based deduplication for faster lookups
 */

import { existsSync } from "node:fs";
import { readFile, stat, unlink } from "node:fs/promises";
import path from "node:path";

import xxhash from "xxhash-wasm";

import { logger } from "../logger";

const fileHashCache = new Map<string, string>();
const hashToFileMap = new Map<string, string>();
const urlToHashMap = new Map<string, string>(); // URL → hash mapping for fast lookups

let hasherInstance: Awaited<ReturnType<typeof xxhash>> | null = null;

async function getHasher() {
  if (!hasherInstance) {
    hasherInstance = await xxhash();
  }
  return hasherInstance;
}

export interface DeduplicationStats {
  duplicates: number;
  storageSavedBytes: number;
  storageSavedMB: string;
  totalImages: number;
  uniqueImages: number;
}

export interface DeduplicationResult {
  isDuplicate: boolean;
  originalPath?: string;
}

export async function hashImageFile(filePath: string): Promise<null | string> {
  if (!existsSync(filePath)) {
    return null;
  }

  if (fileHashCache.has(filePath)) {
    return fileHashCache.get(filePath)!;
  }

  try {
    const hasher = await getHasher();
    const buffer = await readFile(filePath);
    const hashBigInt = hasher.h64Raw(buffer);
    const hash = hashBigInt.toString(16).padStart(16, "0");

    fileHashCache.set(filePath, hash);
    return hash;
  } catch (error) {
    logger.debug(`Failed to hash file ${filePath}: ${error}`);
    return null;
  }
}

export async function findDuplicateByHash(filePath: string): Promise<null | string> {
  const hash = await hashImageFile(filePath);
  if (!hash) {
    return null;
  }

  if (hashToFileMap.has(hash)) {
    const existingPath = hashToFileMap.get(hash)!;
    if (existsSync(existingPath)) {
      return existingPath;
    }
    hashToFileMap.delete(hash);
  }

  hashToFileMap.set(hash, filePath);
  return null;
}

export async function processDuplicateImage(imagePath: string): Promise<DeduplicationResult> {
  const duplicatePath = await findDuplicateByHash(imagePath);

  if (!duplicatePath) {
    return { isDuplicate: false };
  }

  try {
    await unlink(imagePath);
    logger.debug(
      `Deduplicated: removed duplicate ${path.basename(imagePath)} (matches ${path.basename(duplicatePath)})`
    );
    return {
      isDuplicate: true,
      originalPath: duplicatePath,
    };
  } catch (error) {
    logger.debug(`Failed to remove duplicate ${imagePath}: ${error}`);
    return {
      isDuplicate: true,
      originalPath: duplicatePath,
    };
  }
}

export async function getDeduplicationStats(): Promise<DeduplicationStats> {
  const totalImages = fileHashCache.size;
  const uniqueImages = hashToFileMap.size;
  const duplicates = totalImages - uniqueImages;

  let storageSavedBytes = 0;
  for (const [, filePath] of hashToFileMap) {
    try {
      const stats = await stat(filePath);
      const dupCount =
        Array.from(fileHashCache.entries()).filter(([, h]) => h === hashToFileMap.get(filePath)).length - 1;
      storageSavedBytes += stats.size * Math.max(0, dupCount);
    } catch {
      // Ignore stat errors
    }
  }

  return {
    totalImages,
    uniqueImages,
    duplicates,
    storageSavedBytes,
    storageSavedMB: (storageSavedBytes / 1024 / 1024).toFixed(2),
  };
}

export function clearDeduplicationCache(): void {
  fileHashCache.clear();
  hashToFileMap.clear();
  urlToHashMap.clear();
}

export function deduplicateImages(images: string[]): string[] {
  return Array.from(new Set(images));
}

/**
 * Check if a URL has already been processed (by hash)
 * This enables skipping duplicate URLs before downloading
 */
export function isUrlProcessed(url: string): boolean {
  return urlToHashMap.has(url);
}

/**
 * Get the file path for a processed URL
 */
export function getProcessedUrlPath(url: string): null | string {
  const hash = urlToHashMap.get(url);
  if (!hash) return null;
  return hashToFileMap.get(hash) || null;
}

/**
 * Mark a URL as processed with its file path
 * This enables fast deduplication lookups
 */
export function markUrlAsProcessed(url: string, filePath: string, hash: string): void {
  urlToHashMap.set(url, hash);
  hashToFileMap.set(hash, filePath);
}

/**
 * Get URL processing statistics
 */
export function getUrlProcessingStats(): { totalUrls: number; uniqueHashes: number } {
  return {
    totalUrls: urlToHashMap.size,
    uniqueHashes: hashToFileMap.size,
  };
}
