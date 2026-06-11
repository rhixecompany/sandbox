'use server';
import db from '@/lib/prisma';
import { Prisma } from '@prisma/client';
import { revalidatePath } from 'next/cache';
import { z } from 'zod';
import { LATEST_COMICS_LIMIT, PAGE_SIZE } from '../constants';
import { convertToPlainObject, formatError } from '../utils';
import { insertComicSchema, updateComicSchema } from '../validators';

// Get latest comics
export async function getLatestComics() {
  const data = await db.comic.findMany({
    take: LATEST_COMICS_LIMIT,
    orderBy: { createdAt: 'desc' },
  });

  return convertToPlainObject(data);
}

// Get single comic by it's slug
export async function getComicBySlug(slug: string) {
  return await db.comic.findFirst({
    where: { slug: slug },
  });
}

// Get single comic by it's ID
export async function getComicById(comicId: string) {
  const data = await db.comic.findFirst({
    where: { id: comicId },
  });

  return convertToPlainObject(data);
}

// Get all comics
export async function getAllComics({
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
  const queryFilter: Prisma.ComicWhereInput =
    query && query !== 'all'
      ? {
          title: {
            contains: query,
            mode: 'insensitive',
          } as Prisma.StringFilter,
        }
      : {};

  const data = await db.comic.findMany({
    where: {
      ...queryFilter,
    },
    orderBy:
      sort === 'lowest'
        ? { title: 'asc' }
        : sort === 'highest'
          ? { title: 'desc' }
          : sort === 'rating'
            ? { rating: 'desc' }
            : { createdAt: 'desc' },
    skip: (page - 1) * limit,
    take: limit,
  });

  const dataCount = await db.comic.count();

  return {
    data,
    totalPages: Math.ceil(dataCount / limit),
  };
}

// Delete a comic
export async function deleteComic(id: string) {
  try {
    const comicExists = await db.comic.findFirst({
      where: { id },
    });

    if (!comicExists) throw new Error('Comic not found');

    await db.comic.delete({ where: { id } });

    revalidatePath('/admin/comics');

    return {
      success: true,
      message: 'Comic deleted successfully',
    };
  } catch (error) {
    return { success: false, message: formatError(error) };
  }
}

// Create a comic
export async function createComic(data: z.infer<typeof insertComicSchema>) {
  try {
    const comic = insertComicSchema.parse(data);
    await db.comic.create({ data: comic });

    revalidatePath('/admin/comics');

    return {
      success: true,
      message: 'Comic created successfully',
    };
  } catch (error) {
    return { success: false, message: formatError(error) };
  }
}

// Update a comic
export async function updateComic(data: z.infer<typeof updateComicSchema>) {
  try {
    const comic = updateComicSchema.parse(data);
    const comicExists = await db.comic.findFirst({
      where: { id: comic.id },
    });

    if (!comicExists) throw new Error('Comic not found');

    await db.comic.update({
      where: { id: comic.id },
      data: comic,
    });

    revalidatePath('/admin/comics');

    return {
      success: true,
      message: 'Comic updated successfully',
    };
  } catch (error) {
    return { success: false, message: formatError(error) };
  }
}

// Get all categories
export async function getAllCategories() {
  const data = await db.comic.groupBy({
    by: ['category'],
    _count: true,
  });

  return data;
}

// Get featured comics
export async function getFeaturedComics() {
  const data = await db.comic.findMany({
    where: { has_images: true },
    orderBy: { createdAt: 'desc' },
    take: 4,
  });

  return convertToPlainObject(data);
}
