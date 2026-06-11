"use server";
import { asc, eq } from "drizzle-orm";
import { revalidatePath, revalidateTag } from "next/cache.js";
import { z } from "zod";

import { auth } from "@/auth";
import { authorDal } from "@/dal/author-dal";
import { db } from "@/database/db";
import { author, comic } from "@/database/schema";
import type { ActionResult } from "@/types/actions-types";

const AuthorSchema = z.object({
  name: z.string().min(1, "Name required").max(255),
  bio: z.string().optional(),
  imageUrl: z.string().url().optional().or(z.literal("")),
});

type AuthorType = Awaited<ReturnType<typeof authorDal.getById>>;

export async function createAuthorAction(input: unknown): Promise<ActionResult<NonNullable<AuthorType>>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") return { ok: false, error: "Forbidden" };
  const parsed = AuthorSchema.safeParse(input);
  if (!parsed.success) {
    const error = parsed.error.issues[0];
    return { ok: false, error: error?.message ?? "Invalid" };
  }
  try {
    const { name, bio, imageUrl } = parsed.data;
    const author = await authorDal.create({
      name,
      image: imageUrl || null,
      isActive: true,
      bio: bio || null,
      searchVector: null,
      createdAt: new Date(),
    });
    revalidatePath("/admin/authors");
    revalidateTag("search-results", "max");
    return { ok: true, data: author };
  } catch (e) {
    console.error("[createAuthorAction]", e);
    return { ok: false, error: "Failed to create author" };
  }
}

export async function updateAuthorAction(id: number, input: unknown): Promise<ActionResult<NonNullable<AuthorType>>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") return { ok: false, error: "Forbidden" };
  const parsed = AuthorSchema.partial().safeParse(input);
  if (!parsed.success) {
    const error = parsed.error.issues[0];
    return { ok: false, error: error?.message ?? "Invalid" };
  }
  try {
    const author = await authorDal.update(id, parsed.data);
    if (!author) return { ok: false, error: "Author not found" };
    revalidatePath("/admin/authors");
    revalidateTag("search-results", "max");
    return { ok: true, data: author };
  } catch (e) {
    console.error("[updateAuthorAction]", e);
    return { ok: false, error: "Failed to update author" };
  }
}

export async function deleteAuthorAction(id: number): Promise<ActionResult<void>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") return { ok: false, error: "Forbidden" };
  try {
    await authorDal.delete(id);
    revalidatePath("/admin/authors");
    revalidateTag("search-results", "max");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[deleteAuthorAction]", e);
    return { ok: false, error: "Failed to delete author" };
  }
}

export async function getAuthorsListAction(): Promise<ActionResult<NonNullable<AuthorType>[]>> {
  try {
    const authors = await authorDal.list({ limit: 50 });
    return { ok: true, data: authors };
  } catch (error) {
    console.error("[getAuthorsListAction]", error);
    return { ok: false, error: "Failed to fetch authors" };
  }
}

interface AuthorWithComics {
  bio: null | string;
  comics: Array<{
    coverImage: null | string;
    createdAt?: Date;
    description?: string;
    id: number;
    rating: null | number | string;
    slug: string;
    status: string;
    title: string;
  }>;
  id: number;
  image: null | string;
  name: string;
}

export async function getAuthorByIdAction(id: string): Promise<ActionResult<AuthorWithComics | null>> {
  try {
    const authorId = Number(id);
    if (isNaN(authorId)) {
      return { ok: false, error: "Invalid author ID" };
    }

    const authorData = await db.query.author.findFirst({
      where: eq(author.id, authorId),
    });

    if (!authorData) {
      return { ok: true, data: null };
    }

    const comics = await db
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
      .where(eq(comic.authorId, authorId))
      .orderBy(asc(comic.title));

    return {
      ok: true,
      data: {
        id: authorData.id,
        name: authorData.name,
        bio: authorData.bio,
        image: authorData.image,
        comics,
      },
    };
  } catch (error) {
    console.error("[getAuthorByIdAction]", error);
    return { ok: false, error: "Failed to fetch author" };
  }
}
