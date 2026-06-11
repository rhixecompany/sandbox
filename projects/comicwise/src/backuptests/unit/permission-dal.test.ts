/**
 * Permission DAL Tests
 */

import { describe, expect, it } from "vitest";

describe("Permission Model Validation", () => {
  const validPermission = {
    id: 1,
    name: "create_comic",
    description: "Can create comics",
    resource: "comic" as const,
    action: "create" as const,
    createdAt: new Date(),
  };

  describe("Permission object", () => {
    it("should have required fields", () => {
      expect(validPermission).toHaveProperty("id");
      expect(validPermission).toHaveProperty("name");
      expect(validPermission).toHaveProperty("resource");
      expect(validPermission).toHaveProperty("action");
    });

    it("should have valid resource", () => {
      const validResources = [
        "comic",
        "chapter",
        "user",
        "comment",
        "rating",
        "bookmark",
        "notification",
        "author",
        "artist",
        "genre",
        "type",
        "system",
      ];
      expect(validResources).toContain(validPermission.resource);
    });

    it("should have valid action", () => {
      const validActions = ["create", "read", "update", "delete", "manage"];
      expect(validActions).toContain(validPermission.action);
    });
  });
});
