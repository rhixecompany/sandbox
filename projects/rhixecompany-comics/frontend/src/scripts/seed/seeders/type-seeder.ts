/**
 * TypeSeeder - seeds predefined comic types
 * Types are hardcoded; no external JSON loading
 * Uses onConflictDoNothing for atomic idempotent inserts
 */

import { eq, inArray } from "drizzle-orm";

import { db } from "@/database/db";
import { type as comicType } from "@/database/schema";
import { type TypeSeed, typeSeedSchema } from "@/schemas/seed/type.seed";

import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

/**
 * TypeSeeder seeds ComicWise type taxonomy
 * Types: Manga, Manhwa, Manhua, Web Comic, Light Novel
 */
export class TypeSeeder extends BaseSeeder<TypeSeed> {
  private predefinedTypes: TypeSeed[] = [
    { name: "Manga" },
    { name: "Manhwa" },
    { name: "Manhua" },
    { name: "Web Comic" },
    { name: "Light Novel" },
  ];

  constructor(cache: LookupCache, options: SeedOptions) {
    super("types", typeSeedSchema.element, cache, options);
    this.dependencies = []; // No dependencies
  }

  protected getDataSources(): string[] {
    // Types are predefined, not loaded from JSON
    return [];
  }

  protected async loadData(): Promise<TypeSeed[]> {
    logger.debug("Loading predefined types");
    return this.predefinedTypes;
  }

  protected getUniqueField(): string {
    return "name";
  }

  protected async transformData(raw: TypeSeed): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: TypeSeed[]): Promise<EntityResult> {
    const startTime = Date.now();
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];
    let inserted = 0;
    const updated = 0;
    let skipped = 0;

    try {
      if (this.options.forceOverwrite) {
        for (const item of data) {
          const existing = await db.query.type.findFirst({
            where: eq(comicType.name, item.name),
          });

          if (existing) {
            this.cache.types.set(existing.name, existing.id);
            skipped++;
          } else {
            const result = await db.insert(comicType).values({ name: item.name }).returning();
            if (result.length > 0) {
              inserted++;
              this.cache.types.set(result[0].name, result[0].id);
            }
          }
        }
      } else {
        // Atomic batch insert — duplicates are silently skipped via unique constraint
        const insertedRows = await db
          .insert(comicType)
          .values(data.map((item) => ({ name: item.name })))
          .onConflictDoNothing()
          .returning();

        // Cache inserted rows
        for (const row of insertedRows) {
          this.cache.types.set(row.name, row.id);
        }

        // Fetch existing rows that were skipped to populate cache
        const insertedNames = new Set(insertedRows.map((r) => r.name));
        const skippedNames = data.map((d) => d.name).filter((name) => !insertedNames.has(name));

        if (skippedNames.length > 0) {
          const existingRows = await db.query.type.findMany({
            where: inArray(comicType.name, skippedNames),
          });
          for (const row of existingRows) {
            this.cache.types.set(row.name, row.id);
          }
        }

        inserted = insertedRows.length;
        skipped = data.length - inserted;
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
      logger.debug(`Error inserting types batch: ${message}`);

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
