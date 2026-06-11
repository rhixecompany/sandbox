import { eq, ilike } from "drizzle-orm";

import { db } from "@/database/db";
import { artist } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type ArtistType = typeof artist.$inferSelect;

export class ArtistDal extends BaseDal<ArtistType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(artist)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0);
  }

  async getById(id: number): Promise<ArtistType | null> {
    const result = await db.select().from(artist).where(eq(artist.id, id)).limit(1);
    return result[0] ?? null;
  }

  /**
   * Get artist by name
   */
  async getByName(name: string): Promise<ArtistType | null> {
    const result = await db.select().from(artist).where(eq(artist.name, name)).limit(1);
    return result[0] ?? null;
  }

  async search(query: string) {
    return db
      .select()
      .from(artist)
      .where(ilike(artist.name, `%${query}%`));
  }

  async create(data: Omit<ArtistType, "id">) {
    const [result] = await db.insert(artist).values(data).returning();
    return result;
  }

  async update(id: number, data: Partial<Omit<ArtistType, "id">>) {
    const [result] = await db.update(artist).set(data).where(eq(artist.id, id)).returning();
    return result ?? null;
  }

  async delete(id: number) {
    await db.delete(artist).where(eq(artist.id, id));
  }
}

export const artistDal = new ArtistDal();
