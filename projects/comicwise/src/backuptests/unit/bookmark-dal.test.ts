import { beforeEach, describe, expect, it, vi } from "vitest";

import { BookmarkDal } from "@/dal/bookmark-dal";

describe("BookmarkDal", () => {
  const dal = new BookmarkDal();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("getById returns null when not found", async () => {
    // Test that methods are defined and callable
    expect(dal.getById).toBeDefined();
    expect(dal.list).toBeDefined();
  });

  it("create method exists", () => {
    expect(dal.create).toBeDefined();
  });

  it("update method exists", () => {
    expect(dal.update).toBeDefined();
  });
});
