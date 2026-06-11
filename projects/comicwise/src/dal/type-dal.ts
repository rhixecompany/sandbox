import { eq, ilike } from "drizzle-orm";

import { db } from "@/database/db";
import { type as comicType } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type ComicTypeType = typeof comicType.$inferSelect;

export class TypeDal extends BaseDal<ComicTypeType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(comicType)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0);
  }

  async getById(id: number): Promise<ComicTypeType | null> {
    const result = await db.select().from(comicType).where(eq(comicType.id, id)).limit(1);
    return result[0] ?? null;
  }

  async search(query: string) {
    return db
      .select()
      .from(comicType)
      .where(ilike(comicType.name, `%${query}%`));
  }

  async create(data: Omit<ComicTypeType, "id">) {
    const [result] = await db.insert(comicType).values(data).returning();
    return result;
  }

  async update(id: number, data: Partial<Omit<ComicTypeType, "id">>) {
    const [result] = await db.update(comicType).set(data).where(eq(comicType.id, id)).returning();
    return result ?? null;
  }

  async delete(id: number) {
    await db.delete(comicType).where(eq(comicType.id, id));
  }
}

export const typeDal = new TypeDal();
