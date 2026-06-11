import { and, desc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { notification } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type NotificationType = typeof notification.$inferSelect;

export class NotificationDal extends BaseDal<NotificationType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(notification)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0)
      .orderBy(desc(notification.createdAt));
  }

  async getById(id: number): Promise<NotificationType | null> {
    const result = await db.select().from(notification).where(eq(notification.id, id)).limit(1);
    return result[0] ?? null;
  }

  async getByUser(userId: string, options?: DalOptions & { unreadOnly?: boolean }) {
    const conditions = [eq(notification.userId, userId)];
    if (options?.unreadOnly) conditions.push(eq(notification.read, false));
    return db
      .select()
      .from(notification)
      .where(and(...conditions))
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0)
      .orderBy(desc(notification.createdAt));
  }

  async markRead(id: number) {
    const [result] = await db.update(notification).set({ read: true }).where(eq(notification.id, id)).returning();
    return result ?? null;
  }

  async markAllRead(userId: string) {
    await db
      .update(notification)
      .set({ read: true })
      .where(and(eq(notification.userId, userId), eq(notification.read, false)));
  }

  async create(data: Omit<NotificationType, "createdAt" | "id">) {
    const [result] = await db.insert(notification).values(data).returning();
    return result;
  }

  async update(id: number, data: Partial<Omit<NotificationType, "createdAt" | "id">>) {
    const [result] = await db.update(notification).set(data).where(eq(notification.id, id)).returning();
    return result ?? null;
  }

  async delete(id: number) {
    await db.delete(notification).where(eq(notification.id, id));
  }
}

export const notificationDal = new NotificationDal();
