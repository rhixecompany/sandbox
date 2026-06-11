"use server";

import { asc } from "drizzle-orm";

import { db } from "@/database/db";
import { author, genre } from "@/database/schema";

import type { ActionResult } from "@/types/actions-types";

interface GenreData {
  description: null | string;
  id: number;
  name: string;
  slug: null | string;
}

interface AuthorData {
  bio: null | string;
  id: number;
  image: null | string;
  name: string;
}

interface BrowseData {
  authors: AuthorData[];
  genres: GenreData[];
}

/**
 * Get all genres and authors for the browse page
 */
export async function getBrowseDataAction(): Promise<ActionResult<BrowseData>> {
  try {
    const [genresResult, authorsResult] = await Promise.all([
      db
        .select({
          id: genre.id,
          name: genre.name,
          slug: genre.slug,
          description: genre.description,
        })
        .from(genre)
        .where(asc(genre.name))
        .limit(20),
      db
        .select({
          id: author.id,
          name: author.name,
          bio: author.bio,
          image: author.image,
        })
        .from(author)
        .orderBy(asc(author.name))
        .limit(20),
    ]);

    return {
      ok: true,
      data: {
        genres: genresResult as GenreData[],
        authors: authorsResult as AuthorData[],
      },
    };
  } catch (error) {
    console.error("[getBrowseDataAction]", error);
    return { ok: false, error: "Failed to fetch browse data" };
  }
}
