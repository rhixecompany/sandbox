/**
 * Audit Log DAL (Data Access Layer)
 * Manages audit log CRUD operations
 */

import { and, desc, eq, gt, lt } from "drizzle-orm";

import { db } from "@/database/db";
import { auditLog } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type AuditLogType = typeof auditLog.$inferSelect;

export interface CreateAuditLogInput {
  action: string;
  details?: Record<string, unknown>;
  ipAddress?: string;
  resource: string;
  resourceId?: string;
  userAgent?: string;
  userId?: string;
}

export class AuditLogDal extends BaseDal<AuditLogType> {
  async list(options?: DalOptions): Promise<AuditLogType[]> {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.auditLog.findMany({
      orderBy: desc(auditLog.createdAt),
      limit,
      offset,
    });
  }

  async getById(id: string): Promise<AuditLogType | null> {
    return (
      (await db.query.auditLog.findFirst({
        where: eq(auditLog.id, id),
      })) ?? null
    );
  }

  async create(data: unknown): Promise<AuditLogType> {
    const input = data as CreateAuditLogInput;
    const [result] = await db
      .insert(auditLog)
      .values({
        userId: input.userId,
        action: input.action,
        resource: input.resource,
        resourceId: input.resourceId,
        details: input.details ? JSON.stringify(input.details) : null,
        ipAddress: input.ipAddress,
        userAgent: input.userAgent,
      } as typeof auditLog.$inferInsert)
      .returning();

    if (!result) {
      throw new Error("Failed to create audit log");
    }

    return result;
  }

  async update(_id: string, _data: unknown): Promise<AuditLogType | null> {
    throw new Error("Audit logs cannot be updated");
  }

  async delete(_id: string): Promise<void> {
    throw new Error("Audit logs cannot be deleted");
  }

  async getLogsForUser(userId: string, options?: DalOptions): Promise<AuditLogType[]> {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.auditLog.findMany({
      where: eq(auditLog.userId, userId),
      orderBy: desc(auditLog.createdAt),
      limit,
      offset,
    });
  }

  async getLogsForResource(resource: string, resourceId: string, options?: DalOptions): Promise<AuditLogType[]> {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.auditLog.findMany({
      where: and(eq(auditLog.resource, resource as AuditLogType["resource"]), eq(auditLog.resourceId, resourceId)),
      orderBy: desc(auditLog.createdAt),
      limit,
      offset,
    });
  }

  async getLogsByAction(action: string, options?: DalOptions): Promise<AuditLogType[]> {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.auditLog.findMany({
      where: eq(auditLog.action, action),
      orderBy: desc(auditLog.createdAt),
      limit,
      offset,
    });
  }

  async getLogsByDateRange(startDate: Date, endDate: Date, options?: DalOptions): Promise<AuditLogType[]> {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.auditLog.findMany({
      where: and(gt(auditLog.createdAt, startDate), lt(auditLog.createdAt, endDate)),
      orderBy: desc(auditLog.createdAt),
      limit,
      offset,
    });
  }

  async getRecentLogs(options?: DalOptions): Promise<AuditLogType[]> {
    const { limit = 20, offset = 0 } = options ?? {};

    return db.query.auditLog.findMany({
      orderBy: desc(auditLog.createdAt),
      limit,
      offset,
    });
  }
}

export const auditLogDal = new AuditLogDal();
