import { asc, eq } from "drizzle-orm";

import { db } from "@/database/db";
import { chapterImage } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

type ChapterImageType = typeof chapterImage.$inferSelect;

export class ChapterImageDal extends BaseDal<ChapterImageType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(chapterImage)
      .limit(options?.limit ?? 50)
      .offset(options?.offset ?? 0);
  }

  async getById(id: number): Promise<ChapterImageType | null> {
    const result = await db.select().from(chapterImage).where(eq(chapterImage.id, id)).limit(1);
    return result[0] ?? null;
  }

  async getByChapter(chapterId: number) {
    return db
      .select()
      .from(chapterImage)
      .where(eq(chapterImage.chapterId, chapterId))
      .orderBy(asc(chapterImage.pageNumber));
  }

  async create(data: Omit<ChapterImageType, "id">) {
    const [result] = await db.insert(chapterImage).values(data).returning();
    return result;
  }

  async bulkCreate(images: Omit<ChapterImageType, "id">[]) {
    return db.insert(chapterImage).values(images).returning();
  }

  async update(id: number, data: Partial<Omit<ChapterImageType, "id">>) {
    const [result] = await db.update(chapterImage).set(data).where(eq(chapterImage.id, id)).returning();
    return result ?? null;
  }

  async delete(id: number) {
    await db.delete(chapterImage).where(eq(chapterImage.id, id));
  }
}

export const chapterImageDal = new ChapterImageDal();
