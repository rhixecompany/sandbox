import { getAuthorByIdAction, getAuthorsListAction } from "@/actions/author.actions";
import { describe, expect, it, vi } from "vitest";

vi.mock("@/database/db", () => ({
  db: {
    query: {
      author: {
        findFirst: vi.fn().mockResolvedValue(null),
      },
    },
  },
}));

describe("getAuthorsListAction", () => {
  it("should return authors list", async () => {
    vi.mock("@/dal/author-dal", () => ({
      authorDal: {
        list: vi.fn().mockResolvedValue([]),
      },
    }));
    const result = await getAuthorsListAction();
    expect(result.ok).toBe(true);
  });
});

describe("getAuthorByIdAction", () => {
  it("should return error for invalid ID", async () => {
    const result = await getAuthorByIdAction("invalid");
    expect(result.ok).toBe(false);
  });

  it("should return null for non-existent author", async () => {
    const result = await getAuthorByIdAction("999");
    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.data).toBeNull();
    }
  });
});
