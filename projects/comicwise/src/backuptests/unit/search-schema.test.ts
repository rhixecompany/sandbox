import { describe, expect, it } from "vitest";

import {
  SearchQuerySchema,
  SearchResultItemSchema,
  SearchResultsSchema,
  SearchSuggestionsSchema,
} from "@/schemas/search.schema";

/**
 * SearchQuerySchema Tests
 * Validates full-text search input with filters and pagination
 */
describe("SearchQuerySchema", () => {
  describe("valid inputs", () => {
    it("accepts minimal valid query", () => {
      const result = SearchQuerySchema.safeParse({
        q: "manga",
      });
      expect(result.success).toBe(true);
      if (result.success) {
        expect(result.data.q).toBe("manga");
        expect(result.data.page).toBe(1); // default
        expect(result.data.limit).toBe(20); // default
      }
    });

    it("accepts query with all filters", () => {
      const uuid1 = "550e8400-e29b-41d4-a716-446655440001";
      const uuid2 = "550e8400-e29b-41d4-a716-446655440002";
      const result = SearchQuerySchema.safeParse({
        q: "dragon ball",
        filters: {
          status: "Ongoing",
          minRating: 3,
          maxRating: 5,
          genres: [uuid1, uuid2],
          authors: [uuid1],
          sortBy: "rating",
        },
        page: 2,
        limit: 50,
      });
      expect(result.success).toBe(true);
      if (result.success) {
        expect(result.data.filters?.status).toBe("Ongoing");
        expect(result.data.filters?.sortBy).toBe("rating");
        expect(result.data.page).toBe(2);
        expect(result.data.limit).toBe(50);
      }
    });

    it("accepts query with partial filters", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        filters: {
          status: "Completed",
        },
      });
      expect(result.success).toBe(true);
    });

    it("uses default values for optional fields", () => {
      const result = SearchQuerySchema.safeParse({
        q: "manga",
      });
      expect(result.success).toBe(true);
      if (result.success) {
        expect(result.data.page).toBe(1); // default
        expect(result.data.limit).toBe(20); // default
        expect(result.data.filters).toBeUndefined(); // filters is optional object
      }
    });
  });

  describe("query validation", () => {
    it("rejects query shorter than 2 characters", () => {
      const result = SearchQuerySchema.safeParse({
        q: "a",
      });
      expect(result.success).toBe(false);
      if (!result.success) {
        expect(result.error.issues[0].message).toContain("at least 2");
      }
    });

    it("rejects query longer than 100 characters", () => {
      const result = SearchQuerySchema.safeParse({
        q: "a".repeat(101),
      });
      expect(result.success).toBe(false);
      if (!result.success) {
        expect(result.error.issues[0].message).toContain("less than 100");
      }
    });

    it("accepts query exactly 2 characters", () => {
      const result = SearchQuerySchema.safeParse({
        q: "ab",
      });
      expect(result.success).toBe(true);
    });

    it("accepts query exactly 100 characters", () => {
      const result = SearchQuerySchema.safeParse({
        q: "a".repeat(100),
      });
      expect(result.success).toBe(true);
    });

    it("rejects empty query", () => {
      const result = SearchQuerySchema.safeParse({
        q: "",
      });
      expect(result.success).toBe(false);
    });
  });

  describe("filter validation", () => {
    it("accepts valid status values", () => {
      const statuses = ["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"];
      for (const status of statuses) {
        const result = SearchQuerySchema.safeParse({
          q: "test",
          filters: { status },
        });
        expect(result.success).toBe(true);
      }
    });

    it("rejects invalid status", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        filters: {
          status: "Invalid",
        },
      });
      expect(result.success).toBe(false);
    });

    it("accepts valid rating ranges", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        filters: {
          minRating: 1,
          maxRating: 5,
        },
      });
      expect(result.success).toBe(true);
    });

    it("rejects rating out of bounds", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        filters: {
          minRating: 6,
        },
      });
      expect(result.success).toBe(false);
    });

    it("accepts valid sortBy values", () => {
      const sortValues = ["relevance", "rating", "popularity", "newest"];
      for (const sortBy of sortValues) {
        const result = SearchQuerySchema.safeParse({
          q: "test",
          filters: { sortBy },
        });
        expect(result.success).toBe(true);
      }
    });

    it("rejects invalid sortBy value", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        filters: {
          sortBy: "invalid",
        },
      });
      expect(result.success).toBe(false);
    });

    it("accepts UUID arrays for genres and authors", () => {
      const uuid = "550e8400-e29b-41d4-a716-446655440000";
      const result = SearchQuerySchema.safeParse({
        q: "test",
        filters: {
          genres: [uuid],
          authors: [uuid],
        },
      });
      expect(result.success).toBe(true);
    });

    it("rejects invalid UUIDs in genres array", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        filters: {
          genres: ["not-a-uuid"],
        },
      });
      expect(result.success).toBe(false);
    });
  });

  describe("pagination validation", () => {
    it("accepts valid page numbers", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        page: 1,
      });
      expect(result.success).toBe(true);
    });

    it("rejects page numbers less than 1", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        page: 0,
      });
      expect(result.success).toBe(false);
    });

    it("accepts limit between 5 and 100", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        limit: 50,
      });
      expect(result.success).toBe(true);
    });

    it("rejects limit less than 5", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        limit: 4,
      });
      expect(result.success).toBe(false);
    });

    it("rejects limit greater than 100", () => {
      const result = SearchQuerySchema.safeParse({
        q: "test",
        limit: 101,
      });
      expect(result.success).toBe(false);
    });

    it("accepts limit at boundaries", () => {
      expect(SearchQuerySchema.safeParse({ q: "test", limit: 5 }).success).toBe(true);
      expect(SearchQuerySchema.safeParse({ q: "test", limit: 100 }).success).toBe(true);
    });
  });
});

/**
 * SearchSuggestionsSchema Tests
 * Validates autocomplete/suggestions input
 */
describe("SearchSuggestionsSchema", () => {
  describe("valid inputs", () => {
    it("accepts minimal valid query", () => {
      const result = SearchSuggestionsSchema.safeParse({
        q: "ma",
      });
      expect(result.success).toBe(true);
      if (result.success) {
        expect(result.data.q).toBe("ma");
        expect(result.data.limit).toBe(10); // default
      }
    });

    it("accepts query with limit", () => {
      const result = SearchSuggestionsSchema.safeParse({
        q: "manga",
        limit: 20,
      });
      expect(result.success).toBe(true);
      if (result.success) {
        expect(result.data.limit).toBe(20);
      }
    });
  });

  describe("query validation", () => {
    it("rejects query shorter than 2 characters", () => {
      const result = SearchSuggestionsSchema.safeParse({
        q: "a",
      });
      expect(result.success).toBe(false);
      if (!result.success) {
        expect(result.error.issues[0].message).toContain("at least 2");
      }
    });

    it("rejects query longer than 50 characters", () => {
      const result = SearchSuggestionsSchema.safeParse({
        q: "a".repeat(51),
      });
      expect(result.success).toBe(false);
      if (!result.success) {
        expect(result.error.issues[0].message).toContain("less than 50");
      }
    });

    it("accepts query exactly at boundaries", () => {
      expect(SearchSuggestionsSchema.safeParse({ q: "ab" }).success).toBe(true);
      expect(SearchSuggestionsSchema.safeParse({ q: "a".repeat(50) }).success).toBe(true);
    });
  });

  describe("limit validation", () => {
    it("accepts limit between 1 and 20", () => {
      const result = SearchSuggestionsSchema.safeParse({
        q: "test",
        limit: 15,
      });
      expect(result.success).toBe(true);
    });

    it("rejects limit less than 1", () => {
      const result = SearchSuggestionsSchema.safeParse({
        q: "test",
        limit: 0,
      });
      expect(result.success).toBe(false);
    });

    it("rejects limit greater than 20", () => {
      const result = SearchSuggestionsSchema.safeParse({
        q: "test",
        limit: 21,
      });
      expect(result.success).toBe(false);
    });

    it("accepts limit at boundaries", () => {
      expect(SearchSuggestionsSchema.safeParse({ q: "test", limit: 1 }).success).toBe(true);
      expect(SearchSuggestionsSchema.safeParse({ q: "test", limit: 20 }).success).toBe(true);
    });
  });
});

/**
 * SearchResultItemSchema Tests
 * Validates single search result item structure
 */
describe("SearchResultItemSchema", () => {
  const validItem = {
    id: 1,
    title: "Attack on Titan",
    slug: "attack-on-titan",
    coverImage: "https://example.com/image.jpg",
    synopsis: "A great manga",
    rating: "4.5",
    status: "Ongoing",
    author: {
      id: 1,
      name: "Hajime Isayama",
    },
    chapterCount: 139,
  };

  it("accepts valid result item", () => {
    const result = SearchResultItemSchema.safeParse(validItem);
    expect(result.success).toBe(true);
  });

  it("accepts null coverImage", () => {
    const result = SearchResultItemSchema.safeParse({
      ...validItem,
      coverImage: null,
    });
    expect(result.success).toBe(true);
  });

  it("accepts null synopsis", () => {
    const result = SearchResultItemSchema.safeParse({
      ...validItem,
      synopsis: null,
    });
    expect(result.success).toBe(true);
  });

  it("transforms rating string to number", () => {
    const result = SearchResultItemSchema.safeParse({
      ...validItem,
      rating: "3.8",
    });
    expect(result.success).toBe(true);
    if (result.success) {
      expect(result.data.rating).toBe(3.8);
      expect(typeof result.data.rating).toBe("number");
    }
  });

  it("rejects non-integer for id", () => {
    const result = SearchResultItemSchema.safeParse({
      ...validItem,
      id: "not-a-number",
    });
    expect(result.success).toBe(false);
  });

  it("rejects non-integer for author.id", () => {
    const result = SearchResultItemSchema.safeParse({
      ...validItem,
      author: {
        id: "not-a-number",
        name: "Test",
      },
    });
    expect(result.success).toBe(false);
  });

  it("rejects invalid status", () => {
    const result = SearchResultItemSchema.safeParse({
      ...validItem,
      status: "InvalidStatus",
    });
    expect(result.success).toBe(false);
  });
});

/**
 * SearchResultsSchema Tests
 * Validates paginated search results response
 */
describe("SearchResultsSchema", () => {
  const validResults = {
    results: [
      {
        id: 1,
        title: "Attack on Titan",
        slug: "attack-on-titan",
        coverImage: "https://example.com/image.jpg",
        synopsis: "A great manga",
        rating: "4.5",
        status: "Ongoing",
        author: {
          id: 1,
          name: "Hajime Isayama",
        },
        chapterCount: 139,
      },
    ],
    total: 100,
    page: 1,
    limit: 20,
    pageCount: 5,
  };

  it("accepts valid paginated results", () => {
    const result = SearchResultsSchema.safeParse(validResults);
    expect(result.success).toBe(true);
  });

  it("accepts empty results array", () => {
    const result = SearchResultsSchema.safeParse({
      results: [],
      total: 0,
      page: 1,
      limit: 20,
      pageCount: 0,
    });
    expect(result.success).toBe(true);
  });

  it("accepts multiple results", () => {
    const result = SearchResultsSchema.safeParse({
      ...validResults,
      results: Array(20)
        .fill(null)
        .map((_, i) => ({
          ...validResults.results[0],
          id: i + 1,
        })),
    });
    expect(result.success).toBe(true);
  });

  it("rejects page number less than 1", () => {
    const result = SearchResultsSchema.safeParse({
      ...validResults,
      page: 0,
    });
    expect(result.success).toBe(false);
  });

  it("rejects limit less than 5", () => {
    const result = SearchResultsSchema.safeParse({
      ...validResults,
      limit: 4,
    });
    expect(result.success).toBe(false);
  });

  it("rejects limit greater than 100", () => {
    const result = SearchResultsSchema.safeParse({
      ...validResults,
      limit: 101,
    });
    expect(result.success).toBe(false);
  });

  it("rejects invalid result items", () => {
    const result = SearchResultsSchema.safeParse({
      ...validResults,
      results: [
        {
          id: "not-a-number",
          title: "Test",
          slug: "test",
          coverImage: null,
          synopsis: null,
          rating: "4",
          status: "Ongoing",
          author: {
            id: 1,
            name: "Test",
          },
          chapterCount: 10,
        },
      ],
    });
    expect(result.success).toBe(false);
  });
});
