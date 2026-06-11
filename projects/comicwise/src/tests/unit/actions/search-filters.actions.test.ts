import { getSearchFiltersAction } from "@/actions/search-filters.actions";
import { describe, expect, it, vi } from "vitest";

vi.mock("@/dal/genre-dal", () => ({
  genreDal: {
    list: vi.fn().mockResolvedValue([]),
  },
}));

vi.mock("@/dal/author-dal", () => ({
  authorDal: {
    list: vi.fn().mockResolvedValue([]),
  },
}));

describe("getSearchFiltersAction", () => {
  it("should return search filters with genres and authors", async () => {
    const result = await getSearchFiltersAction();
    expect(result.ok).toBe(true);
  });

  it("should return data object with genres and authors arrays", async () => {
    const result = await getSearchFiltersAction();
    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.data).toHaveProperty("genres");
      expect(result.data).toHaveProperty("authors");
    }
  });
});
