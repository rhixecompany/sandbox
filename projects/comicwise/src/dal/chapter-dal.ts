/**
 * Chapter DAL (Data Access Layer)
 * Manages chapter CRUD operations with eager loading
 */

import { and, asc, desc, eq, gt, lt } from "drizzle-orm";

import { db } from "@/database/db";
import { chapter, chapterImage } from "@/database/schema";

import { BaseDal, type DalOptions } from "./base-dal";

export interface ChapterInput {
  chapterNumber: number;
  comicId: number;
  content?: string;
  releaseDate: Date;
  slug: string;
  title: string;
  url?: string;
}

export interface UpdateChapterInput {
  content?: string;
  releaseDate?: Date;
  slug?: string;
  title?: string;
  url?: string;
}

type ChapterType = typeof chapter.$inferSelect;

export class ChapterDal extends BaseDal<ChapterType> {
  /**
   * List chapters
   */
  async list(options?: DalOptions) {
    const { limit = 50, offset = 0 } = options ?? {};

    return db.query.chapter.findMany({
      with: { comic: true },
      orderBy: desc(chapter.releaseDate),
      limit,
      offset,
    });
  }

  /**
   * Get chapter by ID
   */
  async getById(id: number | string): Promise<ChapterType | null> {
    const numId = typeof id === "string" ? parseInt(id, 10) : id;
    if (isNaN(numId)) return null;

    const result = await db.query.chapter.findFirst({
      where: eq(chapter.id, numId),
      with: {
        comic: true,
        images: { orderBy: asc(chapterImage.pageNumber) },
      },
    });

    return result ? (result as unknown as ChapterType) : null;
  }

  /**
   * Get chapter by comic and chapter number
   */
  async getByComicAndNumber(comicId: number, chapterNumber: number) {
    return (
      db.query.chapter.findFirst({
        where: and(eq(chapter.comicId, comicId), eq(chapter.chapterNumber, chapterNumber)),
        with: {
          comic: true,
          images: { orderBy: asc(chapterImage.pageNumber) },
        },
      }) ?? null
    );
  }

  /**
   * Get all chapters for a comic
   */
  async listByComic(comicId: number, options?: DalOptions) {
    const { limit = 200, offset = 0 } = options ?? {};

    return db.query.chapter.findMany({
      where: eq(chapter.comicId, comicId),
      with: { images: { orderBy: asc(chapterImage.pageNumber) } },
      orderBy: desc(chapter.chapterNumber),
      limit,
      offset,
    });
  }

  /**
   * Get next chapter
   */
  async getNext(comicId: number, chapterNumber: number) {
    const next = await db.query.chapter.findFirst({
      where: and(eq(chapter.comicId, comicId), gt(chapter.chapterNumber, chapterNumber)),
      orderBy: chapter.chapterNumber,
      with: { comic: true },
    });

    return next ?? null;
  }

  /**
   * Get previous chapter
   */
  async getPrevious(comicId: number, chapterNumber: number) {
    const prev = await db.query.chapter.findFirst({
      where: and(eq(chapter.comicId, comicId), lt(chapter.chapterNumber, chapterNumber)),
      orderBy: desc(chapter.chapterNumber),
      with: { comic: true },
    });

    return prev ?? null;
  }

  /**
   * Create chapter
   */
  async create(data: unknown): Promise<ChapterType> {
    if (!data || typeof data !== "object" || !("slug" in data) || !("title" in data) || !("chapterNumber" in data)) {
      throw new Error("Invalid chapter data");
    }

    const input = data as ChapterInput;
    const [result] = await db
      .insert(chapter)
      .values({
        slug: input.slug,
        title: input.title,
        chapterNumber: input.chapterNumber,
        releaseDate: input.releaseDate,
        comicId: input.comicId,
        url: input.url,
        content: input.content,
      })
      .returning();

    if (!result) throw new Error("Failed to create chapter");

    return result;
  }

  /**
   * Update chapter
   */
  async update(id: number | string, data: unknown): Promise<ChapterType | null> {
    if (!data || typeof data !== "object") {
      throw new Error("Invalid update data");
    }

    const input = data as UpdateChapterInput;
    const numId = typeof id === "string" ? parseInt(id, 10) : id;
    if (isNaN(numId)) return null;

    const [result] = await db
      .update(chapter)
      .set({
        ...(input.slug && { slug: input.slug }),
        ...(input.title && { title: input.title }),
        ...(input.releaseDate && { releaseDate: input.releaseDate }),
        ...(input.url !== undefined && { url: input.url }),
        ...(input.content !== undefined && { content: input.content }),
        updatedAt: new Date(),
      })
      .where(eq(chapter.id, numId))
      .returning();

    if (!result) return null;

    return this.getById(numId);
  }

  /**
   * Delete chapter
   */
  async delete(id: number | string): Promise<void> {
    const numId = typeof id === "string" ? parseInt(id, 10) : id;
    if (isNaN(numId)) return;
    await db.delete(chapter).where(eq(chapter.id, numId));
  }
}

export const chapterDal = new ChapterDal();
