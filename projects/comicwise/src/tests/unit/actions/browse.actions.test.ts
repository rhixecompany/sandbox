import { getBrowseDataAction } from "@/actions/browse.actions";
import { describe, expect, it, vi } from "vitest";

vi.mock("@/database/db", () => ({
  db: {
    select: vi.fn().mockReturnValue({
      from: vi.fn().mockReturnValue({
        where: vi.fn().mockReturnValue({
          limit: vi.fn().mockResolvedValue([]),
          orderBy: vi.fn().mockResolvedValue([]),
        }),
        orderBy: vi.fn().mockReturnValue({
          where: vi.fn().mockReturnValue({
            limit: vi.fn().mockResolvedValue([]),
          }),
          limit: vi.fn().mockResolvedValue([]),
        }),
        limit: vi.fn().mockResolvedValue([]),
      }),
    }),
  },
}));

describe("getBrowseDataAction", () => {
  it("should return genres and authors", async () => {
    const result = await getBrowseDataAction();
    expect(result.ok).toBe(true);
  });

  it("should return data object with genres and authors arrays", async () => {
    const result = await getBrowseDataAction();
    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.data).toHaveProperty("genres");
      expect(result.data).toHaveProperty("authors");
    }
  });
});
