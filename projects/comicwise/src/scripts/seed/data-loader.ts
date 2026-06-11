/**
 * Data loader with multi-file fallback support for JSON seed data
 * @module dataLoader
 */

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { Logger } from "./logger";

// Resolve data directory statically from module location for Turbopack compatibility.
// This file: src/scripts/seed/dataLoader.ts → default data dir: src/data/ = ../../data
const STATIC_DATA_DIR = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..", "data");

/**
 * DataLoader handles loading JSON files with automatic fallback to alternative filenames
 * Supports caching to avoid repeated file I/O operations
 */
export class DataLoader {
  private cache = new Map<string, unknown[]>();
  private logger: Logger;
  private dataDir: string;
  private basePath: string;

  /**
   * Create a new DataLoader instance
   * @param logger - Logger instance for output
   * @param dataDir - Base directory for data files (default: src/data)
   */
  constructor(logger: Logger, dataDir: string = "src/data") {
    this.logger = logger;
    this.dataDir = dataDir;
    // Use static path for default data dir; fall back to CWD-based for custom paths
    this.basePath = dataDir === "src/data" ? STATIC_DATA_DIR : path.resolve(dataDir);
  }

  /**
   * Load JSON data with automatic fallback to alternative filenames
   * Tries: filename.json → filename-data1.json → filename-data2.json
   * Results are cached for subsequent calls
   *
   * @param baseFileName - Base filename without extension (e.g., "comic")
   * @returns Array of loaded data items
   * @throws Error if no data file can be found
   */
  async loadWithFallback<T>(baseFileName: string): Promise<T[]> {
    const cacheKey = baseFileName;

    // Return cached data if available
    if (this.cache.has(cacheKey)) {
      this.logger.debug(`Using cached data for ${baseFileName}`);
      return this.cache.get(cacheKey) as T[];
    }

    // Candidates to try in order
    const candidates = [`${baseFileName}.json`, `${baseFileName}-data1.json`, `${baseFileName}-data2.json`];

    // Attempt to load from each candidate file
    for (const candidate of candidates) {
      const filePath = path.join(this.basePath, candidate);
      try {
        const content = await fs.readFile(filePath, "utf-8");
        const data = JSON.parse(content) as T[];

        // Cache the result
        this.cache.set(cacheKey, data);
        this.logger.success(`Loaded ${data.length} records from ${candidate}`);
        return data;
      } catch {
        this.logger.debug(`Failed to load ${candidate}, trying next...`);
        continue;
      }
    }

    // None of the candidates were found
    throw new Error(`No data file found for ${baseFileName}. Tried: ${candidates.join(", ")}`);
  }

  /**
   * Load a single JSON file directly
   *
   * @param fileName - Exact filename including extension
   * @returns Array of loaded data items
   * @throws Error if file cannot be read
   */
  async loadFile<T>(fileName: string): Promise<T[]> {
    const cacheKey = fileName;

    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey) as T[];
    }

    const filePath = path.join(this.basePath, fileName);

    try {
      const content = await fs.readFile(filePath, "utf-8");
      const data = JSON.parse(content) as T[];
      this.cache.set(cacheKey, data);
      this.logger.success(`Loaded ${data.length} records from ${fileName}`);
      return data;
    } catch (error) {
      this.logger.error(`Failed to load ${fileName}: ${error}`);
      throw error;
    }
  }

  /**
   * Clear the cache to force reloading on next call
   */
  clearCache(): void {
    this.cache.clear();
    this.logger.debug("Data loader cache cleared");
  }

  /**
   * Check if data is cached
   */
  isCached(baseFileName: string): boolean {
    return this.cache.has(baseFileName);
  }

  /**
   * Get cache statistics
   */
  getCacheStats(): { keys: string[]; size: number } {
    return {
      size: this.cache.size,
      keys: Array.from(this.cache.keys()),
    };
  }
}

/**
 * Singleton instance of the DataLoader
 */
export const dataLoader = new DataLoader(new Logger());
