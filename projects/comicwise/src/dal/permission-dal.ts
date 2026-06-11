/**
 * Permission DAL (Data Access Layer)
 * Manages permission CRUD operations
 */

import { and, desc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { permission } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type PermissionType = typeof permission.$inferSelect;

export interface CreatePermissionInput {
  action: "create" | "delete" | "manage" | "read" | "update";
  description?: string;
  name: string;
  resource:
    | "artist"
    | "author"
    | "bookmark"
    | "chapter"
    | "comic"
    | "comment"
    | "genre"
    | "notification"
    | "rating"
    | "system"
    | "type"
    | "user";
}

export class PermissionDal extends BaseDal<PermissionType> {
  async list(options?: DalOptions): Promise<PermissionType[]> {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.permission.findMany({
      orderBy: desc(permission.createdAt),
      limit,
      offset,
    });
  }

  async getById(id: number): Promise<null | PermissionType> {
    return (
      (await db.query.permission.findFirst({
        where: eq(permission.id, id),
      })) ?? null
    );
  }

  async getByName(name: string): Promise<null | PermissionType> {
    return (
      (await db.query.permission.findFirst({
        where: eq(permission.name, name),
      })) ?? null
    );
  }

  async getByResourceAndAction(resource: string, action: string): Promise<null | PermissionType> {
    return (
      (await db.query.permission.findFirst({
        where: and(
          eq(permission.resource, resource as PermissionType["resource"]),
          eq(permission.action, action as PermissionType["action"])
        ),
      })) ?? null
    );
  }

  async create(data: unknown): Promise<PermissionType> {
    const input = data as CreatePermissionInput;
    const [result] = await db.insert(permission).values(input).returning();

    if (!result) {
      throw new Error("Failed to create permission");
    }

    return result;
  }

  async update(id: number, data: unknown): Promise<null | PermissionType> {
    const input = data as Partial<CreatePermissionInput>;
    const [result] = await db.update(permission).set(input).where(eq(permission.id, id)).returning();

    return result ?? null;
  }

  async delete(id: number): Promise<void> {
    await db.delete(permission).where(eq(permission.id, id));
  }
}

export const permissionDal = new PermissionDal();
