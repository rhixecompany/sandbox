"use server";
import { eq } from "drizzle-orm";
import { revalidatePath, revalidateTag } from "next/cache.js";
import { z } from "zod";

import { auth } from "@/auth";
import { genreDal } from "@/dal/genre-dal";
import { db } from "@/database/db";
import { comic, comicToGenre, genre } from "@/database/schema";
import type { ActionResult } from "@/types/actions-types";

const GenreSchema = z.object({
  name: z.string().min(1, "Name required").max(255),
  slug: z.string().min(1, "Slug required").max(255),
  description: z.string().optional(),
});

type GenreType = Awaited<ReturnType<typeof genreDal.getById>>;

export async function createGenreAction(input: unknown): Promise<ActionResult<NonNullable<GenreType>>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") return { ok: false, error: "Forbidden" };
  const parsed = GenreSchema.safeParse(input);
  if (!parsed.success) {
    const error = parsed.error.issues[0];
    return { ok: false, error: error?.message ?? "Invalid" };
  }
  try {
    const { name, slug, description } = parsed.data;
    const genre = await genreDal.create({
      name,
      slug,
      description: description || null,
      createdAt: new Date(),
      isActive: true,
    });
    revalidatePath("/admin/genres");
    revalidateTag("search-results", "max");
    return { ok: true, data: genre };
  } catch (e) {
    console.error("[createGenreAction]", e);
    return { ok: false, error: "Failed to create genre" };
  }
}

export async function updateGenreAction(id: number, input: unknown): Promise<ActionResult<NonNullable<GenreType>>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") return { ok: false, error: "Forbidden" };
  const parsed = GenreSchema.partial().safeParse(input);
  if (!parsed.success) {
    const error = parsed.error.issues[0];
    return { ok: false, error: error?.message ?? "Invalid" };
  }
  try {
    const genre = await genreDal.update(id, parsed.data);
    if (!genre) return { ok: false, error: "Genre not found" };
    revalidatePath("/admin/genres");
    revalidateTag("search-results", "max");
    return { ok: true, data: genre };
  } catch (e) {
    console.error("[updateGenreAction]", e);
    return { ok: false, error: "Failed to update genre" };
  }
}

export async function deleteGenreAction(id: number): Promise<ActionResult<void>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") return { ok: false, error: "Forbidden" };
  try {
    await genreDal.delete(id);
    revalidatePath("/admin/genres");
    revalidateTag("search-results", "max");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[deleteGenreAction]", e);
    return { ok: false, error: "Failed to delete genre" };
  }
}

export async function getGenresListAction(): Promise<ActionResult<NonNullable<GenreType>[]>> {
  try {
    const genres = await genreDal.list({ limit: 100 });
    return { ok: true, data: genres };
  } catch (error) {
    console.error("[getGenresListAction]", error);
    return { ok: false, error: "Failed to fetch genres" };
  }
}

interface GenreComic {
  coverImage: null | string;
  createdAt?: Date;
  description?: string;
  id: number;
  rating: null | number | string;
  slug: string;
  status: string;
  title: string;
}

interface GenreWithComics {
  comics: GenreComic[];
  description?: null | string;
  id: number;
  name: string;
  slug: null | string;
}

export async function getComicsByGenreAction(genreId: string): Promise<ActionResult<GenreWithComics | null>> {
  try {
    const id = Number(genreId);
    if (isNaN(id)) {
      return { ok: false, error: "Invalid genre ID" };
    }

    const genreData = await db.query.genre.findFirst({
      where: eq(genre.id, id),
    });

    if (!genreData) {
      return { ok: true, data: null };
    }

    const comicsInGenre = await db
      .select({
        id: comic.id,
        title: comic.title,
        slug: comic.slug,
        description: comic.description,
        coverImage: comic.coverImage,
        rating: comic.rating,
        status: comic.status,
        createdAt: comic.createdAt,
      })
      .from(comic)
      .innerJoin(comicToGenre, eq(comicToGenre.comicId, comic.id))
      .where(eq(comicToGenre.genreId, id))
      .limit(24);

    return {
      ok: true,
      data: {
        id: genreData.id,
        name: genreData.name,
        slug: genreData.slug,
        description: genreData.description ?? null,
        comics: comicsInGenre,
      },
    };
  } catch (error) {
    console.error("[getComicsByGenreAction]", error);
    return { ok: false, error: "Failed to fetch genre comics" };
  }
}
