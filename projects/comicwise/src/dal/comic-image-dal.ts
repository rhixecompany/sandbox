import { eq } from "drizzle-orm";

import { db } from "@/database/db";
import { comicImage } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type ComicImageType = typeof comicImage.$inferSelect;

export class ComicImageDal extends BaseDal<ComicImageType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(comicImage)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0);
  }

  async getById(id: number): Promise<ComicImageType | null> {
    const result = await db.select().from(comicImage).where(eq(comicImage.id, id)).limit(1);
    return result[0] ?? null;
  }

  async getByComic(comicId: number) {
    return db.select().from(comicImage).where(eq(comicImage.comicId, comicId));
  }

  async create(data: Omit<ComicImageType, "id">) {
    const [result] = await db.insert(comicImage).values(data).returning();
    return result;
  }

  async update(id: number, data: Partial<Omit<ComicImageType, "id">>) {
    const [result] = await db.update(comicImage).set(data).where(eq(comicImage.id, id)).returning();
    return result ?? null;
  }

  async delete(id: number) {
    await db.delete(comicImage).where(eq(comicImage.id, id));
  }
}

export const comicImageDal = new ComicImageDal();
