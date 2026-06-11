/**
 * UserRoleSeeder - auto-assigns RBAC roles to users
 * No external JSON - assigns based on user email patterns
 */

import { and, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { userRole2 } from "@/database/schema";
import { type UserRoleSeedItem, userRoleSeedItemSchema } from "@/schemas/seed/user-role.seed";

import { logger } from "../logger";

import { BaseSeeder } from "./base-seed";

import type { EntityResult, LookupCache, SeedOptions } from "../types";

interface RoleAssignment {
  assignedAt: Date;
  roleId: number;
  userId: string;
}

export class UserRoleSeeder extends BaseSeeder<UserRoleSeedItem> {
  constructor(cache: LookupCache, options: SeedOptions) {
    super("user-roles", userRoleSeedItemSchema, cache, options);
    this.dependencies = ["users", "roles"];
  }

  protected getDataSources(): string[] {
    return [];
  }

  protected async loadData(): Promise<UserRoleSeedItem[]> {
    const assignments: RoleAssignment[] = [];

    const users = await db.query.user.findMany();

    const roleIds = {
      admin: this.cache.roles.get("admin"),
      moderator: this.cache.roles.get("moderator"),
      user: this.cache.roles.get("user"),
    };

    if (!roleIds.admin || !roleIds.moderator || !roleIds.user) {
      const roles = await db.query.role.findMany();
      for (const r of roles) {
        if (r.name === "admin") roleIds.admin = r.id;
        else if (r.name === "moderator") roleIds.moderator = r.id;
        else if (r.name === "user") roleIds.user = r.id;
      }
    }

    for (const u of users) {
      const email = u.email.toLowerCase();
      let roleId: number | undefined;

      if (email.includes("admin")) {
        roleId = roleIds.admin;
      } else if (email.includes("moderator")) {
        roleId = roleIds.moderator;
      } else {
        roleId = roleIds.user;
      }

      if (roleId) {
        assignments.push({
          userId: u.id,
          roleId,
          assignedAt: new Date(),
        });
      }
    }

    logger.debug(`Generated ${assignments.length} user-role assignments`);
    return assignments as UserRoleSeedItem[];
  }

  protected getUniqueField(): string {
    return "userId";
  }

  protected async transformData(raw: UserRoleSeedItem): Promise<unknown> {
    return raw;
  }

  async insertBatch(data: UserRoleSeedItem[]): Promise<EntityResult> {
    const startTime = Date.now();
    const errors: Array<{ itemIndex: number; message: string; value: unknown }> = [];
    let inserted = 0;
    let updated = 0;
    let skipped = 0;

    try {
      const validItems = data.filter((item) => item.roleId != null && item.userId);

      if (validItems.length === 0) {
        return {
          entityName: this.entityName,
          inserted: 0,
          updated: 0,
          skipped: data.length,
          errors,
          duration: Date.now() - startTime,
          success: true,
        };
      }

      if (this.options.forceOverwrite) {
        for (const item of validItems) {
          const existing = await db.query.userRole2.findFirst({
            where: and(eq(userRole2.userId, item.userId), eq(userRole2.roleId, item.roleId)),
          });

          if (existing) {
            const hasChanges = existing.roleId !== item.roleId || existing.assignedBy !== item.assignedBy;

            if (hasChanges) {
              await db
                .update(userRole2)
                .set({
                  roleId: item.roleId,
                  assignedBy: item.assignedBy,
                })
                .where(and(eq(userRole2.userId, item.userId), eq(userRole2.roleId, item.roleId)));
              updated++;
            } else {
              skipped++;
            }
          } else {
            await db.insert(userRole2).values({
              userId: item.userId,
              roleId: item.roleId,
              assignedAt: item.assignedAt ?? new Date(),
              assignedBy: item.assignedBy,
            });
            inserted++;
          }
        }
      } else {
        const insertedRows = await db
          .insert(userRole2)
          .values(
            validItems.map((item) => ({
              userId: item.userId,
              roleId: item.roleId,
              assignedAt: item.assignedAt ?? new Date(),
              assignedBy: item.assignedBy,
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
      logger.debug(`Error inserting user roles: ${message}`);

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
