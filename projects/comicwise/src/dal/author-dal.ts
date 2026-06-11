import { asc, eq, ilike } from "drizzle-orm";

import { db } from "@/database/db";
import { author } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type AuthorType = typeof author.$inferSelect;

export class AuthorDal extends BaseDal<AuthorType> {
  async list(options?: DalOptions): Promise<AuthorType[]> {
    try {
      return await db
        .select()
        .from(author)
        .orderBy(asc(author.name))
        .limit(options?.limit ?? 20)
        .offset(options?.offset ?? 0);
    } catch (error) {
      console.error("Error listing authors:", error);
      return [];
    }
  }

  async getById(id: number): Promise<AuthorType | null> {
    const result = await db.select().from(author).where(eq(author.id, id)).limit(1);
    return result[0] ?? null;
  }

  /**
   * Get author by name
   */
  async getByName(name: string): Promise<AuthorType | null> {
    const result = await db.select().from(author).where(eq(author.name, name)).limit(1);
    return result[0] ?? null;
  }

  async search(query: string) {
    return db
      .select()
      .from(author)
      .where(ilike(author.name, `%${query}%`));
  }

  async create(data: Omit<AuthorType, "id">) {
    const [result] = await db.insert(author).values(data).returning();
    return result;
  }

  async update(id: number, data: Partial<Omit<AuthorType, "id">>) {
    const [result] = await db.update(author).set(data).where(eq(author.id, id)).returning();
    return result ?? null;
  }

  async delete(id: number) {
    await db.delete(author).where(eq(author.id, id));
  }
}

export const authorDal = new AuthorDal();
