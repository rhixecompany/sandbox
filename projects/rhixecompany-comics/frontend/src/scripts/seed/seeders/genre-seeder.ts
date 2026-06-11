/**
 * GenreSeeder - seeds genres from JSON with deduplication and caching
 */

import { eq, inArray } from "drizzle-orm";

import { db } from "@/database/db";
import { genre } from "@/database/schema";
import { type GenreSeed, genreSeedSchema } from "@/schemas/seed/genre.seed";

import { dataLoader } from "../data-loader";
import { extractEntitiesFromComics } from "../helpers/comic-data-extractor";
import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

/**
 * GenreSeeder loads genres from JSON and caches for relation resolution
 */
export class GenreSeeder extends BaseSeeder<GenreSeed> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("genres", genreSeedSchema.element, cache, options);
    this.dependencies = [];
  }

  protected getDataSources(): string[] {
    return ["genre"];
  }

  protected async loadData(): Promise<GenreSeed[]> {
    const sources = this.getDataSources();
    const allData: GenreSeed[] = [];

    // Try loading from dedicated genre.json first
    for (const source of sources) {
      try {
        const data = await dataLoader.loadWithFallback<GenreSeed>(source);
        allData.push(...data);
        logger.debug(`Loaded ${data.length} genre records from ${source}`);
      } catch {
        logger.debug(`No ${source}.json found, will extract from comic.json`);
      }
    }

    // Fallback: extract genres from comic.json (includes auto-generated slugs)
    if (allData.length === 0) {
      const extracted = await extractEntitiesFromComics();
      allData.push(...extracted.genres);
      logger.info(`Extracted ${extracted.genres.length} unique genres from comic.json`);
    }

    return allData;
  }

  protected getUniqueField(): string {
    return "name";
  }

  protected async transformData(raw: GenreSeed): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: GenreSeed[]): Promise<EntityResult> {
    const startTime = Date.now();
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];
    let inserted = 0;
    let updated = 0;
    let skipped = 0;

    // Filter out items already in cache
    const uncachedItems = data.filter((item) => !this.cache.genres.has(item.name));
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
          const existing = await db.query.genre.findFirst({
            where: eq(genre.name, item.name),
          });

          if (existing) {
            // Smart update: only if slug changed
            if (existing.slug !== item.slug) {
              await db.update(genre).set({ slug: item.slug }).where(eq(genre.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
            this.cache.genres.set(item.name, existing.id);
          } else {
            // Insert new
            const result = await db.insert(genre).values({ name: item.name, slug: item.slug }).returning();
            if (result.length > 0) {
              inserted++;
              this.cache.genres.set(item.name, result[0].id);
            }
          }
        }
      } else {
        // Original: Atomic batch insert — duplicates silently skipped via unique constraint on name
        const insertedRows = await db
          .insert(genre)
          .values(uncachedItems.map((item) => ({ name: item.name, slug: item.slug })))
          .onConflictDoNothing()
          .returning();

        // Cache inserted rows
        for (const row of insertedRows) {
          this.cache.genres.set(row.name, row.id);
        }

        // Fetch existing rows that were skipped to populate cache
        const insertedNames = new Set(insertedRows.map((r) => r.name));
        const skippedNames = uncachedItems.map((d) => d.name).filter((name) => !insertedNames.has(name));

        if (skippedNames.length > 0) {
          const existingRows = await db.query.genre.findMany({
            where: inArray(genre.name, skippedNames),
          });
          for (const row of existingRows) {
            this.cache.genres.set(row.name, row.id);
          }
        }

        inserted = insertedRows.length;
        skipped = cachedSkipped + (uncachedItems.length - inserted);
      }

      const duration = Date.now() - startTime;

      return {
        entityName: this.entityName,
        inserted,
        updated,
        skipped,
        errors,
        duration,
        success: true,
      };
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      errors.push({ itemIndex: 0, value: data, message });
      logger.debug(`Error inserting genres batch: ${message}`);

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
