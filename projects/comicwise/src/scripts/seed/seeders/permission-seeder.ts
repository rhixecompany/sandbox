/**
 * PermissionSeeder - seeds all permission combinations
 * No external JSON - permissions are generated from enums
 */

import { eq } from "drizzle-orm";

import { db } from "@/database/db";
import { permission } from "@/database/schema";
import { type PermissionSeedItem, permissionSeedItemSchema } from "@/schemas/seed/permission.seed";

import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

const RESOURCES = [
  "comic",
  "chapter",
  "user",
  "comment",
  "rating",
  "bookmark",
  "notification",
  "author",
  "artist",
  "genre",
  "type",
  "system",
] as const;

const ACTIONS = ["create", "read", "update", "delete", "manage"] as const;

export class PermissionSeeder extends BaseSeeder<PermissionSeedItem> {
  private predefinedPermissions: PermissionSeedItem[];

  constructor(cache: LookupCache, options: SeedOptions) {
    super("permissions", permissionSeedItemSchema, cache, options);
    this.dependencies = [];
    this.predefinedPermissions = this.generatePermissions();
  }

  private generatePermissions(): PermissionSeedItem[] {
    const permissions: PermissionSeedItem[] = [];

    for (const resource of RESOURCES) {
      for (const action of ACTIONS) {
        permissions.push({
          name: `${action}:${resource}`,
          description: `Permission to ${action} ${resource}`,
          resource,
          action,
        });
      }
    }

    return permissions;
  }

  protected getDataSources(): string[] {
    return [];
  }

  protected async loadData(): Promise<PermissionSeedItem[]> {
    logger.debug(`Loading ${this.predefinedPermissions.length} predefined permissions`);
    return this.predefinedPermissions;
  }

  protected getUniqueField(): string {
    return "name";
  }

  protected async transformData(raw: PermissionSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: PermissionSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];
    let inserted = 0;
    let updated = 0;
    let skipped = 0;

    try {
      if (this.options.forceOverwrite) {
        for (const item of data) {
          const existing = await db.query.permission.findFirst({
            where: eq(permission.name, item.name),
          });

          if (existing) {
            const hasChanges = existing.description !== item.description;

            if (hasChanges) {
              await db
                .update(permission)
                .set({
                  description: item.description,
                })
                .where(eq(permission.id, existing.id));
              updated++;
            } else {
              skipped++;
            }
          } else {
            const result = await db
              .insert(permission)
              .values({
                name: item.name,
                description: item.description,
                resource: item.resource,
                action: item.action,
                createdAt: item.createdAt ?? new Date(),
              })
              .returning();
            if (result.length > 0) {
              inserted++;
            }
          }
        }
      } else {
        const insertedRows = await db
          .insert(permission)
          .values(
            data.map((item) => ({
              name: item.name,
              description: item.description,
              resource: item.resource,
              action: item.action,
              createdAt: item.createdAt ?? new Date(),
            }))
          )
          .onConflictDoNothing()
          .returning();

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
      logger.debug(`Error inserting permissions batch: ${message}`);

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
