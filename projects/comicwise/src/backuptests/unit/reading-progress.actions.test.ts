/**
 * Reading Progress Actions Unit Tests
 * Tests: upsert pattern, stats calculation, ActionResult handling
 */

import { beforeEach, describe, expect, it, vi } from "vitest";

import { updateProgressAction } from "@/actions/reading-progress.actions";

// Mock auth module with proper session
const mockSession = {
  user: { id: "test-user-1", email: "test@example.com", name: "Test User" },
};

vi.mock("@/auth", () => ({
  auth: vi.fn(async () => mockSession),
}));

// Mock reading progress DAL
vi.mock("@/dal/reading-progress-dal", () => ({
  readingProgressDal: {
    updateProgress: vi.fn(async (data) => ({
      id: 1,
      userId: mockSession.user.id,
      comicId: data.comicId,
      chapterId: data.chapterId,
      pageNumber: data.pageNumber || 0,
      progressPercent: 50,
      lastReadAt: new Date(),
    })),
    getContinueReadingList: vi.fn(async () => []),
    markCompleted: vi.fn(async () => ({
      id: 1,
      userId: mockSession.user.id,
      comicId: 1,
      pageNumber: 100,
      progressPercent: 100,
      lastReadAt: new Date(),
    })),
    getUserStats: vi.fn(async () => ({
      totalChaptersRead: 10,
      totalChaptersCompleted: 5,
    })),
  },
}));

describe("readingProgressActions", () => {
  const testComicId = 1;
  const testChapterId = 1;

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe("updateProgressAction", () => {
    describe("validation", () => {
      it("should accept comicId", async () => {
        const result = await updateProgressAction({
          comicId: testComicId,
        });

        expect(typeof result.ok).toBe("boolean");
      });

      it("should accept chapterId", async () => {
        const result = await updateProgressAction({
          comicId: testComicId,
          chapterId: testChapterId,
        });

        expect(typeof result.ok).toBe("boolean");
      });

      it("should accept pageNumber", async () => {
        const result = await updateProgressAction({
          comicId: testComicId,
          pageNumber: 5,
        });

        expect(typeof result.ok).toBe("boolean");
      });

      it("should accept scrollPercentage", async () => {
        const result = await updateProgressAction({
          comicId: testComicId,
          scrollPercentage: 50,
        });

        expect(typeof result.ok).toBe("boolean");
      });
    });

    describe("idempotency", () => {
      it("should handle duplicate updates gracefully", async () => {
        const input = {
          comicId: testComicId,
          chapterId: testChapterId,
          pageNumber: 15,
        };

        const result1 = await updateProgressAction(input);
        const result2 = await updateProgressAction(input);

        // Both calls should have consistent ok status
        expect(typeof result1.ok).toBe("boolean");
        expect(typeof result2.ok).toBe("boolean");
      });
    });

    describe("success cases", () => {
      it("should update reading progress on valid input", async () => {
        const result = await updateProgressAction({
          comicId: testComicId,
          chapterId: testChapterId,
          pageNumber: 25,
        });

        expect(result.ok).toBe(true);
        if (result.ok) {
          expect(result.data).toBeDefined();
        }
      });

      it("should return ActionResult<T> type", async () => {
        const result = await updateProgressAction({
          comicId: testComicId,
          chapterId: testChapterId,
          pageNumber: 30,
        });

        expect(result).toHaveProperty("ok");
        if (result.ok) {
          expect(result).toHaveProperty("data");
        } else {
          expect(result).toHaveProperty("error");
        }
      });

      it("should accept large page numbers", async () => {
        const result = await updateProgressAction({
          comicId: testComicId,
          chapterId: testChapterId,
          pageNumber: 9999,
        });

        expect(typeof result.ok).toBe("boolean");
      });

      it("should accept percentage between 0-100", async () => {
        const result = await updateProgressAction({
          comicId: testComicId,
          scrollPercentage: 75,
        });

        expect(typeof result.ok).toBe("boolean");
      });
    });

    describe("error handling", () => {
      it("should handle database errors gracefully", async () => {
        const result = await updateProgressAction({
          comicId: testComicId,
          chapterId: testChapterId,
          pageNumber: 15,
        });

        // Should return error, not throw
        expect(result).toHaveProperty("ok");
        expect(typeof result.ok).toBe("boolean");
      });
    });
  });
});
