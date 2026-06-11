/**
 * Role DAL (Data Access Layer)
 * Manages role CRUD operations
 */

import { desc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { role } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type RoleType = typeof role.$inferSelect;

export interface CreateRoleInput {
  description?: string;
  isSystem?: boolean;
  name: string;
}

export class RoleDal extends BaseDal<RoleType> {
  async list(options?: DalOptions): Promise<RoleType[]> {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.role.findMany({
      orderBy: desc(role.createdAt),
      limit,
      offset,
    });
  }

  async getById(id: number): Promise<null | RoleType> {
    return (
      (await db.query.role.findFirst({
        where: eq(role.id, id),
      })) ?? null
    );
  }

  async getByName(name: string): Promise<null | RoleType> {
    return (
      (await db.query.role.findFirst({
        where: eq(role.name, name),
      })) ?? null
    );
  }

  async create(data: unknown): Promise<RoleType> {
    const input = data as CreateRoleInput;
    const [result] = await db.insert(role).values(input).returning();

    if (!result) {
      throw new Error("Failed to create role");
    }

    return result;
  }

  async update(id: number, data: unknown): Promise<null | RoleType> {
    const input = data as Partial<CreateRoleInput>;
    const [result] = await db
      .update(role)
      .set({ ...input, updatedAt: new Date() })
      .where(eq(role.id, id))
      .returning();

    return result ?? null;
  }

  async delete(id: number): Promise<void> {
    const existing = await this.getById(id);
    if (existing?.isSystem) {
      throw new Error("Cannot delete system role");
    }

    await db.delete(role).where(eq(role.id, id));
  }
}

export const roleDal = new RoleDal();
