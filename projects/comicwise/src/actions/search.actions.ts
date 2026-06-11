"use server";

import { searchDal } from "@/dal/search-dal";
import {
  type SearchQuery,
  SearchQuerySchema,
  type SearchResults,
  type SearchSuggestionsInput,
  SearchSuggestionsSchema,
} from "@/schemas/search.schema";

import type { ActionResult } from "@/types/actions-types";

/**
 * Perform a full-text search with optional filters
 *
 * Pattern: User Input → Zod Validation → DAL → ActionResult<T>
 *
 * @param input - Raw search query and filters
 * @returns ActionResult with paginated search results or error
 */
export async function performSearchAction(input: unknown): Promise<ActionResult<SearchResults>> {
  // 1. VALIDATE: Zod schema validation
  const parsed = SearchQuerySchema.safeParse(input);

  if (!parsed.success) {
    const errorMessage = parsed.error.issues[0]?.message ?? "Invalid search query";
    return {
      ok: false,
      error: errorMessage,
    };
  }

  try {
    const query: SearchQuery = parsed.data;
    const page = query.page ?? 1;
    const limit = query.limit ?? 20;
    const offset = (page - 1) * limit;

    // 2. CALL DAL: Search comics with query and optional filters
    // Note: Filter arrays (genres, authors) and numeric ID mappings handled in future enhancement
    const dalResults = await searchDal.searchComics({
      query: query.q,
      limit,
      offset,
      status: query.filters?.status,
      // TODO: Day 2.4 - Add genre and author filtering
      // Requires mapping UUID array to numeric IDs via additional queries
    });

    // 3. TRANSFORM: Convert DAL response to SearchResults schema format
    const results: SearchResults = {
      results: dalResults.items.map((item) => ({
        id: item.id,
        title: item.title,
        slug: item.slug,
        coverImage: item.coverImage ?? null,
        synopsis: item.description ?? null,
        rating: item.rating ? parseFloat(String(item.rating)) : 0,
        status: item.status,
        author: {
          id: item.author?.id ?? 0,
          name: item.author?.name ?? "Unknown",
        },
        chapterCount: 0,
      })),
      total: dalResults.total,
      page,
      limit,
      pageCount: Math.ceil(dalResults.total / limit),
    };

    // 4. RETURN: ActionResult<T> pattern
    return {
      ok: true,
      data: results,
    };
  } catch (error) {
    console.error("Search action error:", error);

    // Handle rate-limit errors gracefully
    if (error instanceof Error && error.message.includes("rate")) {
      return {
        ok: false,
        error: "Search service is temporarily unavailable. Please try again in a moment.",
      };
    }

    return {
      ok: false,
      error: "Failed to perform search. Please try again.",
    };
  }
}

/**
 * Get real-time search suggestions (autocomplete)
 *
 * Pattern: User Input → Zod Validation → DAL → ActionResult<T>
 * Implements simple prefix matching on comic titles
 *
 * @param input - Raw suggestion query
 * @returns ActionResult with array of suggestion strings or error
 */
export async function getSearchSuggestionsAction(input: unknown): Promise<ActionResult<string[]>> {
  // 1. VALIDATE: Zod schema validation
  const parsed = SearchSuggestionsSchema.safeParse(input);

  if (!parsed.success) {
    return {
      ok: false,
      error: "Invalid suggestion request",
    };
  }

  try {
    const query: SearchSuggestionsInput = parsed.data;

    // 2. CALL DAL: Search for comics matching the query
    const results = await searchDal.searchComics({
      query: query.q,
      limit: query.limit ?? 10,
      offset: 0,
    });

    // 3. EXTRACT: Get unique comic titles as suggestions
    const suggestions: string[] = results.items
      .slice(0, query.limit ?? 10)
      .map((item: (typeof results.items)[number]) => item.title)
      .filter((title: string, index: number, self: string[]) => self.indexOf(title) === index); // Remove duplicates

    // 4. RETURN: ActionResult<T> pattern
    return {
      ok: true,
      data: suggestions,
    };
  } catch (error) {
    console.error("Suggestions action error:", error);

    // Handle rate-limit errors gracefully
    if (error instanceof Error && error.message.includes("rate")) {
      return {
        ok: false,
        error: "Suggestions service is temporarily unavailable.",
      };
    }

    return {
      ok: false,
      error: "Failed to get suggestions. Please try again.",
    };
  }
}

/**
 * Save search query to user's search history
 * Note: Requires authentication - placeholder for Day 3
 *
 * @param query - Search query to save
 * @returns ActionResult with success status or error
 */
export async function saveSearchHistoryAction(): Promise<ActionResult<boolean>> {
  // TODO: Day 3 implementation
  // - Check authentication: const session = await auth()
  // - Validate query with schema
  // - Call DAL: await searchHistoryDal.save(session.user.id, query)
  // - Revalidate: revalidatePath("/search")
  //
  // For now, return success (no-op)
  return {
    ok: true,
    data: true,
  };
}
