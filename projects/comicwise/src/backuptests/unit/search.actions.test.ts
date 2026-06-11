/**
 * Search Server Actions Unit Tests
 * Tests: validation, error handling, ActionResult pattern
 */

import { describe, expect, it, vi } from "vitest";

import { getSearchSuggestionsAction, performSearchAction } from "@/actions/search.actions";

// Mock auth module
vi.mock("@/auth", () => ({
  auth: vi.fn(),
}));

describe("performSearchAction", () => {
  describe("validation", () => {
    it("should reject query under 2 characters", async () => {
      const result = await performSearchAction({
        q: "a",
      });

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.error).toContain("at least 2 characters");
      }
    });

    it("should reject query over 100 characters", async () => {
      const longQuery = "a".repeat(101);
      const result = await performSearchAction({
        q: longQuery,
      });

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.error).toContain("less than 100 characters");
      }
    });

    it("should accept valid query", async () => {
      const result = await performSearchAction({
        q: "test manga",
      });

      expect(result.ok).toBe(true);
      if (result.ok) {
        expect(result.data).toBeDefined();
        expect(result.data.results).toBeDefined();
      }
    });
  });

  describe("filters", () => {
    it("should accept status filter", async () => {
      const result = await performSearchAction({
        q: "action",
        filters: {
          status: "Ongoing",
        },
      });

      expect(result.ok).toBe(true);
    });

    it("should accept rating range filters", async () => {
      const result = await performSearchAction({
        q: "popular",
        filters: {
          minRating: 3,
          maxRating: 5,
        },
      });

      expect(result.ok).toBe(true);
    });

    it("should accept genre and author UUIDs", async () => {
      const testUUID = "550e8400-e29b-41d4-a716-446655440000";
      const result = await performSearchAction({
        q: "manga",
        filters: {
          genres: [testUUID],
          authors: [testUUID],
        },
      });

      expect(result.ok).toBe(true);
    });

    it("should accept sort options", async () => {
      const result = await performSearchAction({
        q: "manga",
        filters: {
          sortBy: "rating",
        },
      });

      expect(result.ok).toBe(true);
    });
  });

  describe("pagination", () => {
    it("should accept valid page and limit", async () => {
      const result = await performSearchAction({
        q: "manga",
        page: 2,
        limit: 50,
      });

      expect(result.ok).toBe(true);
      if (result.ok) {
        expect(result.data.page).toBe(2);
        expect(result.data.limit).toBe(50);
      }
    });

    it("should use default pagination values", async () => {
      const result = await performSearchAction({
        q: "manga",
      });

      expect(result.ok).toBe(true);
      if (result.ok) {
        expect(result.data.page).toBe(1);
        expect(result.data.limit).toBe(20);
      }
    });

    it("should reject page under 1", async () => {
      const result = await performSearchAction({
        q: "manga",
        page: 0,
      });

      expect(result.ok).toBe(false);
    });

    it("should reject limit over 100", async () => {
      const result = await performSearchAction({
        q: "manga",
        limit: 101,
      });

      expect(result.ok).toBe(false);
    });
  });

  describe("error handling", () => {
    it("should return ActionResult with ok false on validation error", async () => {
      const result = await performSearchAction({
        q: "",
      });

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.error).toBeDefined();
      }
    });

    it("should return ActionResult.ok true on success", async () => {
      const result = await performSearchAction({
        q: "test",
      });

      expect(result.ok).toBe(true);
      if (result.ok) {
        expect(result.data).toBeDefined();
      }
    });
  });
});

describe("getSearchSuggestionsAction", () => {
  describe("validation", () => {
    it("should reject query under 2 characters", async () => {
      const result = await getSearchSuggestionsAction({
        q: "a",
      });

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.error).toBeDefined();
      }
    });

    it("should reject query over 50 characters", async () => {
      const longQuery = "a".repeat(51);
      const result = await getSearchSuggestionsAction({
        q: longQuery,
      });

      expect(result.ok).toBe(false);
    });

    it("should accept valid query", async () => {
      const result = await getSearchSuggestionsAction({
        q: "man",
      });

      expect(result.ok).toBe(true);
      if (result.ok) {
        expect(Array.isArray(result.data)).toBe(true);
      }
    });
  });

  describe("pagination", () => {
    it("should accept valid limit", async () => {
      const result = await getSearchSuggestionsAction({
        q: "manga",
        limit: 5,
      });

      expect(result.ok).toBe(true);
    });

    it("should use default limit of 10", async () => {
      const result = await getSearchSuggestionsAction({
        q: "manga",
      });

      expect(result.ok).toBe(true);
    });

    it("should reject limit over 20", async () => {
      const result = await getSearchSuggestionsAction({
        q: "manga",
        limit: 21,
      });

      expect(result.ok).toBe(false);
    });
  });

  describe("error handling", () => {
    it("should return ActionResult with ok false on validation error", async () => {
      const result = await getSearchSuggestionsAction({
        q: "a",
      });

      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.error).toBeDefined();
      }
    });

    it("should return array data on success", async () => {
      const result = await getSearchSuggestionsAction({
        q: "test",
      });

      expect(result.ok).toBe(true);
      if (result.ok) {
        expect(Array.isArray(result.data)).toBe(true);
      }
    });
  });
});
