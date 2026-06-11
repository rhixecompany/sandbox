'use server';
import db from '@/lib/prisma';
import { Prisma } from '@prisma/client';
import { revalidatePath } from 'next/cache';
import { z } from 'zod';
import { LATEST_COMICS_LIMIT, PAGE_SIZE } from '../constants';
import { convertToPlainObject, formatError } from '../utils';
import { insertChapterSchema, updateChapterSchema } from '../validators';

// Get latest chapters
export async function getLatestChapters() {
  const data = await db.chapter.findMany({
    take: LATEST_COMICS_LIMIT,
    orderBy: { createdAt: 'desc' },
  });

  return convertToPlainObject(data);
}

// Get single chapter by it's slug
export async function getChapterBySlug(slug: string) {
  return await db.chapter.findFirst({
    where: { slug: slug },
  });
}

// Get single chapter by it's ID
export async function getChapterById(chapterId: string) {
  const data = await db.chapter.findFirst({
    where: { id: chapterId },
  });

  return convertToPlainObject(data);
}

// Get all chapters
export async function getAllChapters({
  query,
  limit = PAGE_SIZE,
  page,
  sort,
}: {
  query: string;
  limit?: number;
  page: number;
  category?: string;
  numchapters?: string;
  rating?: string;
  sort?: string;
}) {
  // Query filter
  const queryFilter: Prisma.ChapterWhereInput =
    query && query !== 'all'
      ? {
          name: {
            contains: query,
            mode: 'insensitive',
          } as Prisma.StringFilter,
        }
      : {};

  const data = await db.chapter.findMany({
    where: {
      ...queryFilter,
    },
    orderBy:
      sort === 'lowest'
        ? { title: 'asc' }
        : sort === 'highest'
          ? { numimages: 'desc' }
          : { createdAt: 'desc' },
    skip: (page - 1) * limit,
    take: limit,
  });

  const dataCount = await db.chapter.count();

  return {
    data,
    totalPages: Math.ceil(dataCount / limit),
  };
}

// Delete a chapter
export async function deleteChapter(id: string) {
  try {
    const chapterExists = await db.chapter.findFirst({
      where: { id },
    });

    if (!chapterExists) throw new Error('Chapter not found');

    await db.chapter.delete({ where: { id } });

    revalidatePath('/admin/chapters');

    return {
      success: true,
      message: 'Chapter deleted successfully',
    };
  } catch (error) {
    return { success: false, message: formatError(error) };
  }
}

// Create a chapter
export async function createChapter(data: z.infer<typeof insertChapterSchema>) {
  try {
    const chapter = insertChapterSchema.parse(data);
    await db.chapter.create({ data: chapter });

    revalidatePath('/admin/chapters');

    return {
      success: true,
      message: 'Chapter created successfully',
    };
  } catch (error) {
    return { success: false, message: formatError(error) };
  }
}

// Update a chapter
export async function updateChapter(data: z.infer<typeof updateChapterSchema>) {
  try {
    const chapter = updateChapterSchema.parse(data);
    const chapterExists = await db.chapter.findFirst({
      where: { id: chapter.id },
    });

    if (!chapterExists) throw new Error('Chapter not found');

    await db.chapter.update({
      where: { id: chapter.id },
      data: chapter,
    });

    revalidatePath('/admin/chapters');

    return {
      success: true,
      message: 'Chapter updated successfully',
    };
  } catch (error) {
    return { success: false, message: formatError(error) };
  }
}

// Get featured chapters
export async function getFeaturedChapters() {
  const data = await db.chapter.findMany({
    where: { has_images: true },
    orderBy: { createdAt: 'desc' },
    take: 4,
  });

  return convertToPlainObject(data);
}
