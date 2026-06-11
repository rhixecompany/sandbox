/**
 * ArtistSeeder - seeds artists from JSON with deduplication and caching
 */

import { eq, inArray } from "drizzle-orm";

import { db } from "@/database/db";
import { artist } from "@/database/schema";
import { type ArtistSeed, artistSeedSchema } from "@/schemas/seed/artist.seed";

import { dataLoader } from "../data-loader";
import { extractEntitiesFromComics } from "../helpers/comic-data-extractor";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

/**
 * ArtistSeeder loads artists from JSON and caches for relation resolution
 * Mirrors AuthorSeeder pattern
 */
export class ArtistSeeder extends BaseSeeder<ArtistSeed> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("artists", artistSeedSchema.element, cache, options);
    this.dependencies = [];
  }

  protected getDataSources(): string[] {
    return ["artist"];
  }

  protected async loadData(): Promise<ArtistSeed[]> {
    const sources = this.getDataSources();
    const allData: ArtistSeed[] = [];

    // Try loading from dedicated artist.json first
    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<ArtistSeed>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} artist records from ${source}`);
      } catch {
        logger.debug(`No ${source}.json found, will extract from comic.json`);
      }
    }

    // Fallback: extract artists from comic.json
    if (allData.length === 0) {
      const extracted = await extractEntitiesFromComics();
      allData.push(...extracted.artists);
      logger.info(`Extracted ${extracted.artists.length} unique artists from comic.json`);
    }

    return allData;
  }

  protected getUniqueField(): string {
    return "name";
  }

  protected async transformData(raw: ArtistSeed): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: ArtistSeed[]): Promise<EntityResult> {
    const startTime = Date.now();
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];
    let inserted = 0;
    // eslint-disable-next-line prefer-const
    let updated = 0;
    let skipped = 0;

    // Filter out items already in cache
    const uncachedItems = data.filter((item) => !this.cache.artists.has(item.name));
    const cachedSkipped = data.length - uncachedItems.length;

    if (uncachedItems.length === 0) {
      const duration = Date.now() - startTime;
      return {
        entityName: this.entityName,
        inserted: 0,
        updated: 0,
        skipped: data.length,
        errors,
        duration,
        success: true,
      };
    }

    try {
      // Handle force overwrite with smart update
      if (this.options.forceOverwrite) {
        for (const item of uncachedItems) {
          const existing = await db.query.artist.findFirst({
            where: eq(artist.name, item.name),
          });

          if (existing) {
            // No other fields to update for artist, just cache it
            this.cache.artists.set(item.name, {
              id: String(existing.id),
              name: existing.name,
            });
            skipped++;
          } else {
            // Insert new
            const result = await db.insert(artist).values({ name: item.name }).returning();
            if (result.length > 0) {
              inserted++;
              this.cache.artists.set(item.name, {
                id: String(result[0].id),
                name: result[0].name,
              });
            }
          }
        }
      } else {
        // Original: Atomic batch insert
        const insertedRows = await db
          .insert(artist)
          .values(uncachedItems.map((item) => ({ name: item.name })))
          .onConflictDoNothing()
          .returning();

        // Cache inserted rows
        for (const row of insertedRows) {
          this.cache.artists.set(row.name, {
            id: String(row.id),
            name: row.name,
          });
        }

        // Fetch existing rows that were skipped to populate cache
        const insertedNames = new Set(insertedRows.map((r) => r.name));
        const skippedNames = uncachedItems.map((d) => d.name).filter((name) => !insertedNames.has(name));

        if (skippedNames.length > 0) {
          const existingRows = await db.query.artist.findMany({
            where: inArray(artist.name, skippedNames),
          });
          for (const row of existingRows) {
            this.cache.artists.set(row.name, {
              id: String(row.id),
              name: row.name,
            });
          }
        }

        inserted = insertedRows.length;
        skipped = cachedSkipped + (uncachedItems.length - inserted);
      }

      const duration = Date.now() - startTime;

      return {
        entityName: this.entityName,
        inserted,
        skipped,
        updated: 0,
        errors,
        duration,
        success: true,
      };
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      errors.push({ itemIndex: 0, value: data, message });
      logger.debug(`Error inserting artists batch: ${message}`);

      const duration = Date.now() - startTime;
      return {
        entityName: this.entityName,
        inserted: 0,
        updated: 0,
        skipped: 0,
        errors,
        duration,
        success: false,
      };
    }
  }
}
