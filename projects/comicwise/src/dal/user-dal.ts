import { desc, eq, ilike } from "drizzle-orm";

import { db } from "@/database/db";
import { user } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type UserType = typeof user.$inferSelect;

export class UserDal extends BaseDal<UserType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(user)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0)
      .orderBy(desc(user.createdAt));
  }

  async getById(id: string): Promise<null | UserType> {
    const result = await db.select().from(user).where(eq(user.id, id)).limit(1);
    return result[0] ?? null;
  }

  async getByEmail(email: string): Promise<null | UserType> {
    const result = await db.select().from(user).where(eq(user.email, email)).limit(1);
    return result[0] ?? null;
  }

  async search(query: string) {
    return db
      .select()
      .from(user)
      .where(ilike(user.name, `%${query}%`));
  }

  async create(data: Omit<UserType, "createdAt" | "id" | "updatedAt">) {
    const [result] = await db.insert(user).values(data).returning();
    return result;
  }

  async update(id: string, data: Partial<Omit<UserType, "id">>) {
    const [result] = await db
      .update(user)
      .set({ ...data, updatedAt: new Date() })
      .where(eq(user.id, id))
      .returning();
    return result ?? null;
  }

  async updateByEmail(email: string, data: Partial<Omit<UserType, "id">>) {
    const [result] = await db
      .update(user)
      .set({ ...data, updatedAt: new Date() })
      .where(eq(user.email, email))
      .returning();
    return result ?? null;
  }

  async updatePassword(email: string, password: string) {
    const [result] = await db
      .update(user)
      .set({ password, updatedAt: new Date() })
      .where(eq(user.email, email))
      .returning();
    return result ?? null;
  }

  async updateRole(id: string, role: "admin" | "moderator" | "user") {
    const [result] = await db.update(user).set({ role }).where(eq(user.id, id)).returning();
    return result ?? null;
  }

  async delete(id: string) {
    await db.delete(user).where(eq(user.id, id));
  }
}

export const userDal = new UserDal();
