import { getComicsByGenreAction, getGenresListAction } from "@/actions/genre.actions";
import { describe, expect, it, vi } from "vitest";

vi.mock("@/database/db", () => ({
  db: {
    query: {
      genre: {
        findFirst: vi.fn().mockResolvedValue(null),
      },
    },
  },
}));

describe("getGenresListAction", () => {
  it("should return genres list", async () => {
    vi.mock("@/dal/genre-dal", () => ({
      genreDal: {
        list: vi.fn().mockResolvedValue([]),
      },
    }));
    const result = await getGenresListAction();
    expect(result.ok).toBe(true);
  });
});

describe("getComicsByGenreAction", () => {
  it("should return error for invalid genre ID", async () => {
    const result = await getComicsByGenreAction("invalid");
    expect(result.ok).toBe(false);
  });

  it("should return null for non-existent genre", async () => {
    const result = await getComicsByGenreAction("999");
    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.data).toBeNull();
    }
  });
});
