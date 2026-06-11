/**
 * RoleSeeder - seeds predefined system roles
 * No external JSON - roles are hardcoded system entities
 */

import { eq, inArray } from "drizzle-orm";

import { db } from "@/database/db";
import { role } from "@/database/schema";
import { type RoleSeedItem, roleSeedItemSchema } from "@/schemas/seed/role.seed";

import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

export class RoleSeeder extends BaseSeeder<RoleSeedItem> {
  private predefinedRoles: RoleSeedItem[];

  constructor(cache: LookupCache, options: SeedOptions) {
    super("roles", roleSeedItemSchema, cache, options);
    this.dependencies = [];
    this.predefinedRoles = [
      { name: "user", description: "Standard user with basic access", isSystem: true },
      { name: "admin", description: "Full administrative access", isSystem: true },
      { name: "moderator", description: "Content moderation capabilities", isSystem: true },
    ];
  }

  protected getDataSources(): string[] {
    return [];
  }

  protected async loadData(): Promise<RoleSeedItem[]> {
    logger.debug("Loading predefined system roles");
    return this.predefinedRoles;
  }

  protected getUniqueField(): string {
    return "name";
  }

  protected async transformData(raw: RoleSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: RoleSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];
    let inserted = 0;
    let updated = 0;
    let skipped = 0;

    try {
      if (this.options.forceOverwrite) {
        for (const item of data) {
          const existing = await db.query.role.findFirst({
            where: eq(role.name, item.name),
          });

          if (existing) {
            const hasChanges = existing.description !== item.description || existing.isSystem !== item.isSystem;

            if (hasChanges) {
              await db
                .update(role)
                .set({
                  description: item.description,
                  isSystem: item.isSystem,
                  updatedAt: new Date(),
                })
                .where(eq(role.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
            this.cache.roles.set(existing.name, existing.id);
          } else {
            const result = await db
              .insert(role)
              .values({
                name: item.name,
                description: item.description,
                isSystem: item.isSystem,
                createdAt: item.createdAt ?? new Date(),
                updatedAt: item.updatedAt ?? new Date(),
              })
              .returning();
            if (result.length > 0) {
              inserted++;
              this.cache.roles.set(result[0].name, result[0].id);
            }
          }
        }
      } else {
        const insertedRows = await db
          .insert(role)
          .values(
            data.map((item) => ({
              name: item.name,
              description: item.description,
              isSystem: item.isSystem,
              createdAt: item.createdAt ?? new Date(),
              updatedAt: item.updatedAt ?? new Date(),
            }))
          )
          .onConflictDoNothing()
          .returning();

        for (const row of insertedRows) {
          this.cache.roles.set(row.name, row.id);
        }

        const insertedNames = new Set(insertedRows.map((r) => r.name));
        const skippedNames = data.map((d) => d.name).filter((name) => !insertedNames.has(name));

        if (skippedNames.length > 0) {
          const existingRows = await db.query.role.findMany({
            where: inArray(role.name, skippedNames),
          });
          for (const row of existingRows) {
            this.cache.roles.set(row.name, row.id);
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
      logger.debug(`Error inserting roles batch: ${message}`);

      return {
        entityName: this.entityName,
        inserted: 0,
        updated: 0,
        skipped: 0,
        errors,
        duration: Date.now() - startTime,
        success: false,
      };
    }
  }
}
