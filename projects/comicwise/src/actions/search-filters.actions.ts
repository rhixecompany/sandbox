"use server";

import { authorDal } from "@/dal/author-dal";
import { genreDal } from "@/dal/genre-dal";

import type { ActionResult } from "@/types/actions-types";

interface GenreFilter {
  id: string;
  name: string;
}

interface AuthorFilter {
  id: string;
  name: string;
}

interface SearchFilters {
  authors: AuthorFilter[];
  genres: GenreFilter[];
}

/**
 * Get genres and authors for search filter options
 */
export async function getSearchFiltersAction(): Promise<ActionResult<SearchFilters>> {
  try {
    const [genres, authors] = await Promise.all([genreDal.list(), authorDal.list()]);

    const genreFilters: GenreFilter[] = genres
      .filter((g) => g.name && g.name.trim())
      .map((g) => ({
        id: String(g.id),
        name: g.name,
      }));

    const authorFilters: AuthorFilter[] = authors
      .filter((a) => a.name && a.name.trim())
      .map((a) => ({
        id: String(a.id),
        name: a.name,
      }));

    return {
      ok: true,
      data: {
        genres: genreFilters,
        authors: authorFilters,
      },
    };
  } catch (error) {
    console.error("[getSearchFiltersAction]", error);
    return { ok: false, error: "Failed to fetch search filters" };
  }
}
