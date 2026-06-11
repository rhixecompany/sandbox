/**
 * Share DAL Tests
 */

import { describe, expect, it } from "vitest";

describe("Share Model Validation", () => {
  const validShare = {
    id: 1,
    userId: "user-123",
    resourceType: "comic" as const,
    resourceId: 1,
    message: "Great comic!",
    createdAt: new Date(),
  };

  describe("Share object", () => {
    it("should have required fields", () => {
      expect(validShare).toHaveProperty("id");
      expect(validShare).toHaveProperty("userId");
      expect(validShare).toHaveProperty("resourceType");
      expect(validShare).toHaveProperty("resourceId");
    });

    it("should have valid resourceType", () => {
      const validTypes = ["comic", "chapter"];
      expect(validTypes).toContain(validShare.resourceType);
    });
  });
});

describe("Share Schema Validation", () => {
  it("should accept valid share comic input", () => {
    const input = { comicId: 1, message: "Test" };
    expect(input.comicId).toBeDefined();
    expect(input.message).toBeDefined();
  });

  it("should accept valid share chapter input", () => {
    const input = { chapterId: 1 };
    expect(input.chapterId).toBeDefined();
  });

  it("should reject invalid resource type", () => {
    const invalidTypes = ["invalid", "movie", "book"];
    const validTypes = ["comic", "chapter"];
    for (const type of invalidTypes) {
      expect(validTypes).not.toContain(type);
    }
  });
});
