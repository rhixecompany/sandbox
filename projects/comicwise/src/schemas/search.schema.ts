import { z } from "zod";

/**
 * Search query validation schema
 * Validates input for full-text search with optional filters and pagination
 */
export const SearchQuerySchema = z.object({
  q: z
    .string()
    .min(2, "Search query must be at least 2 characters")
    .max(100, "Search query must be less than 100 characters")
    .describe("Search query text"),

  filters: z
    .object({
      status: z
        .enum(["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"])
        .optional()
        .describe("Comic publication status"),

      minRating: z.number().min(0).max(5).optional().describe("Minimum rating (0-5 stars)"),

      maxRating: z.number().min(0).max(5).optional().describe("Maximum rating (0-5 stars)"),

      genres: z.array(z.string().uuid()).optional().describe("Genre UUIDs to filter by"),

      authors: z.array(z.string().uuid()).optional().describe("Author UUIDs to filter by"),

      sortBy: z
        .enum(["relevance", "rating", "popularity", "newest"])
        .default("relevance")
        .optional()
        .describe("Sort order for results"),
    })
    .optional()
    .describe("Optional filters and sorting"),

  page: z.number().int().min(1).default(1).optional().describe("Page number (1-indexed)"),

  limit: z.number().int().min(5).max(100).default(20).optional().describe("Results per page (5-100)"),
});

export type SearchQuery = z.infer<typeof SearchQuerySchema>;

/**
 * Search suggestions validation schema
 * Validates input for autocomplete/suggestions endpoint
 */
export const SearchSuggestionsSchema = z.object({
  q: z
    .string()
    .min(2, "Query must be at least 2 characters")
    .max(50, "Query must be less than 50 characters")
    .describe("Partial search query for suggestions"),

  limit: z.number().int().min(1).max(20).default(10).optional().describe("Maximum number of suggestions (1-20)"),
});

export type SearchSuggestionsInput = z.infer<typeof SearchSuggestionsSchema>;

/**
 * Search result item (minimal comic info for display)
 */
export const SearchResultItemSchema = z.object({
  id: z.number().int(),
  title: z.string(),
  slug: z.string(),
  coverImage: z.string().nullable(),
  synopsis: z.string().nullable(),
  rating: z
    .string() // decimal(10,1) from database
    .transform((val) => parseFloat(val)),
  status: z.enum(["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"]),
  author: z.object({
    id: z.number().int(),
    name: z.string(),
  }),
  chapterCount: z.number().int(),
});

export type SearchResultItem = z.infer<typeof SearchResultItemSchema>;

/**
 * Paginated search results response
 */
export const SearchResultsSchema = z.object({
  results: z.array(SearchResultItemSchema),
  total: z.number().int(),
  page: z.number().int().min(1),
  limit: z.number().int().min(5).max(100),
  pageCount: z.number().int(),
});

export type SearchResults = z.infer<typeof SearchResultsSchema>;
