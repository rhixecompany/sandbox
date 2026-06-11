/**
 * Search DAL Unit Tests
 * Tests: ilike search, pagination, eager loading
 */

import { describe, expect, it } from "vitest";

import { searchDal } from "@/dal/search-dal";

describe("SearchDAL", () => {
  describe("searchComics()", () => {
    it("should search comics by title", async () => {
      const result = await searchDal.searchComics({
        query: "test",
        limit: 20,
        offset: 0,
      });

      expect(result).toHaveProperty("items");
      expect(result).toHaveProperty("total");
      expect(result).toHaveProperty("page");
      expect(result).toHaveProperty("pageSize");
      expect(Array.isArray(result.items)).toBe(true);
      expect(typeof result.total).toBe("number");
    });

    it("should return paginated results", async () => {
      const limit = 10;
      const offset = 0;

      const result = await searchDal.searchComics({
        query: "comic",
        limit,
        offset,
      });

      expect(result.pageSize).toBe(limit);
      expect(result.page).toBe(0);
      expect(result.items.length).toBeLessThanOrEqual(limit);
    });

    it("should filter by author", async () => {
      const result = await searchDal.searchComics({
        query: "test",
        authorId: 1,
        limit: 20,
      });

      expect(result).toHaveProperty("items");
      // All results should have authorId matching filter
      for (const comic of result.items) {
        expect(comic.authorId).toBe(1);
      }
    });

    it("should handle empty search results gracefully", async () => {
      const result = await searchDal.searchComics({
        query: "zzznonexistentqueryzzzz",
        limit: 20,
      });

      expect(result.items).toEqual([]);
      expect(result.total).toBe(0);
    });

    it("should include eager-loaded relationships", async () => {
      const result = await searchDal.searchComics({
        query: "test",
        limit: 1,
      });

      if (result.items.length > 0) {
        const comic = result.items[0];
        // Check eager-loaded relationships exist
        expect(comic).toHaveProperty("author");
        expect(comic).toHaveProperty("genres");
      }
    });

    it("should limit max results per page to 100", async () => {
      const result = await searchDal.searchComics({
        query: "a",
        limit: 500, // Try to request more than max
        offset: 0,
      });

      // Should be capped at 100 or less
      expect(result.pageSize).toBeLessThanOrEqual(100);
    });

    it("should handle pagination offset", async () => {
      const result1 = await searchDal.searchComics({
        query: "comic",
        limit: 5,
        offset: 0,
      });

      const result2 = await searchDal.searchComics({
        query: "comic",
        limit: 5,
        offset: 5,
      });

      expect(result1.page).toBe(0);
      expect(result2.page).toBe(1);
    });

    it("should handle special characters in query", async () => {
      const result = await searchDal.searchComics({
        query: "test%like",
        limit: 20,
      });

      expect(result).toHaveProperty("items");
      expect(Array.isArray(result.items)).toBe(true);
    });
  });

  describe("searchComics() with filters", () => {
    it("should filter by status", async () => {
      const result = await searchDal.searchComics({
        query: "test",
        status: "Ongoing",
        limit: 20,
      });

      if (result.items.length > 0) {
        for (const comic of result.items) {
          expect(comic.status).toBe("Ongoing");
        }
      }
    });

    it("should combine multiple filters", async () => {
      const result = await searchDal.searchComics({
        query: "test",
        authorId: 1,
        status: "Completed",
        limit: 20,
      });

      expect(result).toHaveProperty("items");
    });
  });
});
