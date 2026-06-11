import { asc, eq, ilike } from "drizzle-orm";

import { db } from "@/database/db";
import { comicToGenre, genre } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type GenreType = typeof genre.$inferSelect;

export class GenreDal extends BaseDal<GenreType> {
  async list(options?: DalOptions): Promise<GenreType[]> {
    try {
      return await db
        .select()
        .from(genre)
        .orderBy(asc(genre.name))
        .limit(options?.limit ?? 50)
        .offset(options?.offset ?? 0);
    } catch (error) {
      console.error("Error listing genres:", error);
      return [];
    }
  }

  async getById(id: number): Promise<GenreType | null> {
    const result = await db.select().from(genre).where(eq(genre.id, id)).limit(1);
    return result[0] ?? null;
  }

  async getBySlug(slug: string): Promise<GenreType | null> {
    const result = await db.select().from(genre).where(eq(genre.slug, slug)).limit(1);
    return result[0] ?? null;
  }

  async search(query: string) {
    return db
      .select()
      .from(genre)
      .where(ilike(genre.name, `%${query}%`));
  }

  async create(data: Omit<GenreType, "id">) {
    const [result] = await db.insert(genre).values(data).returning();
    return result;
  }

  async update(id: number, data: Partial<Omit<GenreType, "id">>) {
    const [result] = await db.update(genre).set(data).where(eq(genre.id, id)).returning();
    return result ?? null;
  }

  async delete(id: number) {
    await db.delete(genre).where(eq(genre.id, id));
  }

  async getComicsForGenre(genreId: number) {
    return db.query.comicToGenre.findMany({
      where: eq(comicToGenre.genreId, genreId),
      with: { comic: true },
    });
  }
}

export const genreDal = new GenreDal();
