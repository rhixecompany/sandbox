/**
 * User Role DAL (Data Access Layer)
 * Manages user-role assignment operations
 */

import { and, desc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { userRole2 } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type UserRoleType = typeof userRole2.$inferSelect;

export interface AssignRoleInput {
  assignedBy?: string;
  roleId: number;
  userId: string;
}

export class UserRoleDal extends BaseDal<UserRoleType> {
  async list(options?: DalOptions): Promise<UserRoleType[]> {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.userRole2.findMany({
      orderBy: desc(userRole2.assignedAt),
      limit,
      offset,
    });
  }

  async getById(_id: number | string): Promise<null | UserRoleType> {
    throw new Error("Use getByUserAndRole instead");
  }

  async create(data: unknown): Promise<UserRoleType> {
    const input = data as AssignRoleInput;
    const [result] = await db
      .insert(userRole2)
      .values({
        userId: input.userId,
        roleId: input.roleId,
        assignedBy: input.assignedBy,
      })
      .onConflictDoNothing()
      .returning();

    if (!result) {
      throw new Error("User already has this role");
    }

    return result;
  }

  async update(_id: number | string, _data: unknown): Promise<null | UserRoleType> {
    throw new Error("User roles cannot be updated, use assign/remove");
  }

  async delete(_id: number | string): Promise<void> {
    throw new Error("Use removeRole instead");
  }

  async getUserRoles(userId: string): Promise<UserRoleType[]> {
    return db.query.userRole2.findMany({
      where: eq(userRole2.userId, userId),
      orderBy: desc(userRole2.assignedAt),
    });
  }

  async getRoleUsers(roleId: number): Promise<UserRoleType[]> {
    return db.query.userRole2.findMany({
      where: eq(userRole2.roleId, roleId),
      orderBy: desc(userRole2.assignedAt),
    });
  }

  async hasRole(userId: string, roleId: number): Promise<boolean> {
    const result = await db.query.userRole2.findFirst({
      where: and(eq(userRole2.userId, userId), eq(userRole2.roleId, roleId)),
    });

    return result !== undefined;
  }

  async hasPermission(userId: string, _permission: string): Promise<boolean> {
    const userRoles = await this.getUserRoles(userId);

    for (const ur of userRoles) {
      if (ur.roleId === 1) {
        return true;
      }
    }

    return false;
  }

  async removeRole(userId: string, roleId: number): Promise<void> {
    await db.delete(userRole2).where(and(eq(userRole2.userId, userId), eq(userRole2.roleId, roleId)));
  }

  async removeAllRoles(userId: string): Promise<void> {
    await db.delete(userRole2).where(eq(userRole2.userId, userId));
  }
}

export const userRoleDal = new UserRoleDal();
