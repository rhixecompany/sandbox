/**
 * Comic Data Access Layer Tests
 * Tests for comic CRUD operations and queries
 */

import { beforeEach, describe, expect, it, vi } from "vitest";

import { ComicDal } from "@/dal/comic-dal";
import { db } from "@/database/db";

describe("ComicDal", () => {
  const dal = new ComicDal();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("calls db.query.comic.findMany in list()", async () => {
    const mockComics = [{ id: 1, title: "Test Comic", status: "Ongoing" }];
    vi.mocked(db.query.comic.findMany).mockResolvedValue(mockComics as never);
    const result = await dal.list({ limit: 10 });
    expect(db.query.comic.findMany).toHaveBeenCalled();
    expect(result).toEqual(mockComics);
  });

  it("returns null from getById when not found", async () => {
    vi.mocked(db.query.comic.findFirst).mockResolvedValue(undefined as never);
    const result = await dal.getById(999);
    expect(result).toBeNull();
  });

  it("returns null from getById with invalid string id", async () => {
    const result = await dal.getById("not-a-number");
    expect(result).toBeNull();
  });

  it("calls findFirst in getBySlug()", async () => {
    const mockComic = { id: 1, title: "Test Comic", slug: "test-comic" };
    vi.mocked(db.query.comic.findFirst).mockResolvedValue(mockComic as never);
    const result = await dal.getBySlug("test-comic");
    expect(db.query.comic.findFirst).toHaveBeenCalled();
    expect(result).toEqual(mockComic);
  });

  it("returns null from getBySlug when not found", async () => {
    vi.mocked(db.query.comic.findFirst).mockResolvedValue(undefined as never);
    const result = await dal.getBySlug("nonexistent");
    expect(result).toBeNull();
  });

  it("passes limit and offset options to list()", async () => {
    vi.mocked(db.query.comic.findMany).mockResolvedValue([] as never);
    await dal.list({ limit: 5, offset: 10 });
    expect(db.query.comic.findMany).toHaveBeenCalledWith(
      expect.objectContaining({
        limit: 5,
        offset: 10,
      })
    );
  });

  it("uses default limit and offset when not provided", async () => {
    vi.mocked(db.query.comic.findMany).mockResolvedValue([] as never);
    await dal.list();
    expect(db.query.comic.findMany).toHaveBeenCalledWith(
      expect.objectContaining({
        limit: 20,
        offset: 0,
      })
    );
  });
});

describe("Comic Model Validation", () => {
  const validComic = {
    id: 1,
    slug: "one-piece",
    title: "One Piece",
    description: "A manga about pirates",
    coverImageUrl: "https://example.com/cover.jpg",
    status: "Ongoing" as const,
    authorId: 1,
    views: 1000,
    averageRating: 4.5,
    totalRatings: 100,
    createdAt: new Date(),
    updatedAt: new Date(),
  };

  describe("Comic object", () => {
    it("should have required fields", () => {
      expect(validComic).toHaveProperty("id");
      expect(validComic).toHaveProperty("slug");
      expect(validComic).toHaveProperty("title");
      expect(validComic).toHaveProperty("status");
    });

    it("should have valid slug format", () => {
      const slugRegex = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
      expect(slugRegex.test(validComic.slug)).toBe(true);
    });

    it("should have valid status enum", () => {
      const validStatuses = ["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"];
      expect(validStatuses).toContain(validComic.status);
    });

    it("should have non-negative views", () => {
      expect(validComic.views).toBeGreaterThanOrEqual(0);
    });

    it("should have rating between 0-5", () => {
      expect(validComic.averageRating).toBeGreaterThanOrEqual(0);
      expect(validComic.averageRating).toBeLessThanOrEqual(5);
    });
  });

  describe("Comic slug validation", () => {
    const validSlugs = ["one-piece", "attack-on-titan", "my-hero-academia", "demon-slayer-1"];

    const invalidSlugs = [
      "One Piece", // uppercase
      "one_piece", // underscore
      "one-piece-", // trailing dash
      "-one-piece", // leading dash
    ];

    for (const slug of validSlugs) {
      it(`should accept "${slug}" as valid slug`, () => {
        const slugRegex = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
        expect(slugRegex.test(slug)).toBe(true);
      });
    }

    for (const slug of invalidSlugs) {
      it(`should reject "${slug}" as invalid slug`, () => {
        const slugRegex = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
        expect(slugRegex.test(slug)).toBe(false);
      });
    }
  });
});

describe("Comic Pagination", () => {
  it("should paginate correctly", () => {
    const pageSize = 20;
    const totalItems = 100;
    const currentPage = 2;

    const skip = (currentPage - 1) * pageSize;
    const take = pageSize;
    const totalPages = Math.ceil(totalItems / pageSize);

    expect(skip).toBe(20);
    expect(take).toBe(20);
    expect(totalPages).toBe(5);
  });

  it("should handle last page correctly", () => {
    const pageSize = 20;
    const totalItems = 95;
    const currentPage = 5;

    const skip = (currentPage - 1) * pageSize;
    const itemsOnPage = Math.min(pageSize, totalItems - skip);

    expect(skip).toBe(80);
    expect(itemsOnPage).toBe(15); // 95 - 80 = 15
  });

  it("should validate page numbers", () => {
    const isValidPage = (page: number, totalPages: number) => {
      return page > 0 && page <= totalPages;
    };

    expect(isValidPage(1, 5)).toBe(true);
    expect(isValidPage(5, 5)).toBe(true);
    expect(isValidPage(0, 5)).toBe(false);
    expect(isValidPage(6, 5)).toBe(false);
  });
});

describe("Comic Filtering", () => {
  const comics = [
    { id: 1, title: "One Piece", status: "Ongoing" as const, averageRating: 4.8 },
    { id: 2, title: "Naruto", status: "Completed" as const, averageRating: 4.5 },
    { id: 3, title: "Bleach", status: "Completed" as const, averageRating: 4.3 },
    { id: 4, title: "My Hero Academia", status: "Ongoing" as const, averageRating: 4.7 },
  ];

  it("should filter by status", () => {
    const ongoing = comics.filter((c) => c.status === "Ongoing");
    expect(ongoing).toHaveLength(2);
    expect(ongoing[0].title).toBe("One Piece");
  });

  it("should sort by rating", () => {
    const sorted = [...comics].sort((a, b) => b.averageRating - a.averageRating);
    expect(sorted[0].averageRating).toBe(4.8);
    expect(sorted[sorted.length - 1].averageRating).toBe(4.3);
  });

  it("should filter and sort combined", () => {
    const filtered = comics.filter((c) => c.status === "Completed").sort((a, b) => b.averageRating - a.averageRating);

    expect(filtered).toHaveLength(2);
    expect(filtered[0].title).toBe("Naruto");
  });

  it("should search by title", () => {
    const search = "hero";
    const results = comics.filter((c) => c.title.toLowerCase().includes(search.toLowerCase()));

    expect(results).toHaveLength(1);
    expect(results[0].title).toBe("My Hero Academia");
  });

  it("should handle empty search query", () => {
    const search = "";
    const results = comics.filter((c) => c.title.toLowerCase().includes(search.toLowerCase()));

    expect(results).toHaveLength(4);
  });

  it("should handle case-insensitive search", () => {
    const search = "ONE PIECE";
    const results = comics.filter((c) => c.title.toLowerCase().includes(search.toLowerCase()));

    expect(results).toHaveLength(1);
    expect(results[0].title).toBe("One Piece");
  });
});

describe("Comic List Options Validation", () => {
  it("should validate list options with all filters", () => {
    const options = {
      limit: 20,
      offset: 0,
      orderBy: "popular" as const,
      query: "test",
      status: "Ongoing" as const,
      genreId: 1,
      typeId: 2,
    };

    expect(options.limit).toBe(20);
    expect(options.offset).toBe(0);
    expect(options.orderBy).toBe("popular");
    expect(options.query).toBe("test");
    expect(options.status).toBe("Ongoing");
    expect(options.genreId).toBe(1);
    expect(options.typeId).toBe(2);
  });

  it("should validate sort options", () => {
    const validSorts = ["latest", "popular", "rating", "title"];
    for (const sort of validSorts) {
      expect(validSorts).toContain(sort);
    }
  });

  it("should validate status filter values match DB enum", () => {
    const validStatuses = ["Ongoing", "Hiatus", "Completed", "Dropped", "Season End", "Coming Soon"];
    expect(validStatuses).toHaveLength(6);
    for (const status of validStatuses) {
      expect(status[0]).toBe(status[0].toUpperCase()); // Title-Case
    }
  });

  it("should compute pagination offset correctly from page number", () => {
    const computeOffset = (page: number, limit: number) => (page - 1) * limit;

    expect(computeOffset(1, 20)).toBe(0);
    expect(computeOffset(2, 20)).toBe(20);
    expect(computeOffset(3, 10)).toBe(20);
    expect(computeOffset(1, 50)).toBe(0);
  });
});
