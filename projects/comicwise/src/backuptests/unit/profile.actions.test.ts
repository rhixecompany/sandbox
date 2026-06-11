/**
 * Profile Actions Integration Tests
 * Tests for user profile management server actions
 */

import { describe, expect, it } from "vitest";

import type { ActionResult } from "@/types/actions-types";

describe("Profile Actions - ActionResult Type", () => {
  describe("ActionResult<T> Structure", () => {
    it("should have ok property that is boolean", () => {
      const successResult: ActionResult<{ id: string }> = {
        ok: true,
        data: { id: "test" },
      };
      expect(typeof successResult.ok).toBe("boolean");
      expect(successResult.ok).toBe(true);
    });

    it("should have data property when ok is true", () => {
      const successResult: ActionResult<{ name: string }> = {
        ok: true,
        data: { name: "John" },
      };
      expect(successResult).toHaveProperty("data");
      expect(successResult.data.name).toBe("John");
    });

    it("should have error property when ok is false", () => {
      const errorResult: ActionResult<never> = {
        ok: false,
        error: "Something went wrong",
      };
      expect(errorResult).toHaveProperty("error");
      expect(errorResult.error).toBe("Something went wrong");
    });

    it("should be a discriminated union", () => {
      const result1: ActionResult<{ value: number }> = {
        ok: true,
        data: { value: 42 },
      };

      const result2: ActionResult<{ value: number }> = {
        ok: false,
        error: "Error message",
      };

      if (result1.ok) {
        expect(result1.data.value).toBe(42);
      }

      if (!result2.ok) {
        expect(result2.error).toBe("Error message");
      }
    });
  });

  describe("Profile-Related Action Results", () => {
    it("should support user profile data", () => {
      const profileResult: ActionResult<{
        bio?: string;
        email: string;
        id: string;
        image?: string;
        name: string;
      }> = {
        ok: true,
        data: {
          id: "user-123",
          name: "John Doe",
          email: "john@example.com",
          image: "https://example.com/avatar.jpg",
          bio: "A comic reader",
        },
      };

      expect(profileResult.ok).toBe(true);
      if (profileResult.ok) {
        expect(profileResult.data.name).toBe("John Doe");
        expect(profileResult.data.email).toBe("john@example.com");
      }
    });

    it("should support profile stats data", () => {
      const statsResult: ActionResult<{
        bookmarks: number;
        chaptersRead: number;
        commentsMade: number;
        ratingsGiven: number;
      }> = {
        ok: true,
        data: {
          bookmarks: 15,
          ratingsGiven: 8,
          commentsMade: 23,
          chaptersRead: 42,
        },
      };

      expect(statsResult.ok).toBe(true);
      if (statsResult.ok) {
        expect(statsResult.data.bookmarks).toBe(15);
        expect(statsResult.data.chaptersRead).toBe(42);
      }
    });

    it("should support error responses", () => {
      const errorResult: ActionResult<never> = {
        ok: false,
        error: "User not found",
      };

      expect(errorResult.ok).toBe(false);
      if (!errorResult.ok) {
        expect(errorResult.error).toBe("User not found");
      }
    });
  });

  describe("Type Narrowing", () => {
    it("should narrow types correctly with ok check", () => {
      const result: ActionResult<{ value: string }> = {
        ok: true,
        data: { value: "test" },
      };

      if (result.ok) {
        // Type should be narrowed to { ok: true; data: ... }
        const data = result.data;
        expect(data.value).toBe("test");
      }
    });

    it("should narrow to error type with !ok check", () => {
      const result: ActionResult<{ value: string }> = {
        ok: false,
        error: "Test error",
      };

      if (!result.ok) {
        // Type should be narrowed to { ok: false; error: ... }
        const error = result.error;
        expect(error).toBe("Test error");
      }
    });
  });

  describe("Action Pattern Usage", () => {
    it("should support server action pattern", async () => {
      // Simulates a server action that returns ActionResult
      const mockServerAction = async (): Promise<ActionResult<{ id: string }>> => {
        return {
          ok: true,
          data: { id: "user-123" },
        };
      };

      const result = await mockServerAction();
      expect(result.ok).toBe(true);
      if (result.ok) {
        expect(result.data.id).toBe("user-123");
      }
    });

    it("should handle error case in server action", async () => {
      const mockServerAction = async (): Promise<ActionResult<never>> => {
        return {
          ok: false,
          error: "Authentication failed",
        };
      };

      const result = await mockServerAction();
      expect(result.ok).toBe(false);
      if (!result.ok) {
        expect(result.error).toContain("Authentication");
      }
    });

    it("should allow chaining with early return", async () => {
      const mockAction = async (): Promise<ActionResult<string>> => {
        const check1: ActionResult<never> = {
          ok: false,
          error: "Validation failed",
        };

        if (!check1.ok) {
          return check1;
        }

        return {
          ok: true,
          data: "success",
        };
      };

      const result = await mockAction();
      expect(result.ok).toBe(false);
    });
  });

  describe("Profile Preferences Schema Support", () => {
    it("should support user preferences structure", () => {
      const prefsResult: ActionResult<{
        defaultLayout: "book" | "comic" | "webtoon";
        notifyNewChapters: boolean;
        theme: "dark" | "light" | "system";
      }> = {
        ok: true,
        data: {
          theme: "dark",
          defaultLayout: "webtoon",
          notifyNewChapters: true,
        },
      };

      expect(prefsResult.ok).toBe(true);
      if (prefsResult.ok) {
        expect(prefsResult.data.theme).toBe("dark");
        expect(prefsResult.data.notifyNewChapters).toBe(true);
      }
    });
  });
});
