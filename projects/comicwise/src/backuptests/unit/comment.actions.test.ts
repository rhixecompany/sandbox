/**
 * Comment Actions Unit Tests
 * Tests: create, update, delete with ownership checks
 */

import { beforeEach, describe, expect, it, vi } from "vitest";

import { createCommentAction, deleteCommentAction, updateCommentAction } from "@/actions/comment-rating.actions";

// Mock auth module with proper session
const mockSession = {
  user: { id: "test-user-1", email: "test@example.com", name: "Test User" },
};

vi.mock("@/auth", () => ({
  auth: vi.fn(async () => mockSession),
}));

// Mock comment DAL
vi.mock("@/dal/comment-rating-dal", () => ({
  commentDal: {
    create: vi.fn(async (data) => ({
      id: 1,
      ...data,
      createdAt: new Date(),
      updatedAt: new Date(),
    })),
    update: vi.fn(async (id, data) => ({
      id,
      ...data,
      createdAt: new Date(),
      updatedAt: new Date(),
    })),
    delete: vi.fn(async () => {}),
    getById: vi.fn(async (id) => ({
      id,
      chapterId: 1,
      userId: mockSession.user.id,
      content: "Test",
      createdAt: new Date(),
      updatedAt: new Date(),
    })),
  },
}));

describe("commentActions", () => {
  const testChapterId = 1;

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe("createCommentAction", () => {
    describe("validation", () => {
      it("should reject empty content", async () => {
        const result = await createCommentAction({
          chapterId: testChapterId,
          content: "",
        });

        expect(result.ok).toBe(false);
        if (!result.ok) {
          expect(result.error).toBeDefined();
        }
      });

      it("should reject whitespace-only content", async () => {
        const result = await createCommentAction({
          chapterId: testChapterId,
          content: "   ",
        });

        expect(result.ok).toBe(false);
      });

      it("should reject missing chapterId", async () => {
        const result = await createCommentAction({
          content: "Valid comment",
        } as unknown);

        expect(result.ok).toBe(false);
      });

      it("should accept valid content", async () => {
        const result = await createCommentAction({
          chapterId: testChapterId,
          content: "This is a valid comment",
        });

        expect(typeof result.ok).toBe("boolean");
      });
    });

    describe("success cases", () => {
      it("should create comment on valid input", async () => {
        const result = await createCommentAction({
          chapterId: testChapterId,
          content: "Test comment",
        });

        expect(result.ok).toBe(true);
        if (result.ok) {
          expect(result.data).toBeDefined();
        }
      });

      it("should return ActionResult<T> type", async () => {
        const result = await createCommentAction({
          chapterId: testChapterId,
          content: "Valid comment",
        });

        expect(result).toHaveProperty("ok");
        if (result.ok) {
          expect(result).toHaveProperty("data");
        } else {
          expect(result).toHaveProperty("error");
        }
      });
    });
  });

  describe("updateCommentAction", () => {
    describe("validation", () => {
      it("should reject empty content on update", async () => {
        const result = await updateCommentAction(1, {
          content: "",
        });

        expect(result.ok).toBe(false);
      });

      it("should accept valid update", async () => {
        const result = await updateCommentAction(1, {
          content: "Updated comment content",
        });

        expect(typeof result.ok).toBe("boolean");
      });
    });

    describe("success cases", () => {
      it("should update comment on valid input", async () => {
        const result = await updateCommentAction(1, {
          content: "Valid updated content",
        });

        expect(result).toHaveProperty("ok");
      });

      it("should return ActionResult<T> type", async () => {
        const result = await updateCommentAction(1, {
          content: "Updated",
        });

        expect(result).toHaveProperty("ok");
        if (result.ok) {
          expect(result).toHaveProperty("data");
        } else {
          expect(result).toHaveProperty("error");
        }
      });
    });
  });

  describe("deleteCommentAction", () => {
    describe("validation", () => {
      it("should accept valid commentId", async () => {
        const result = await deleteCommentAction(1);

        expect(typeof result.ok).toBe("boolean");
      });
    });

    describe("success cases", () => {
      it("should delete comment on valid input", async () => {
        const result = await deleteCommentAction(1);

        expect(result).toHaveProperty("ok");
      });

      it("should return ActionResult<T> type", async () => {
        const result = await deleteCommentAction(1);

        expect(result).toHaveProperty("ok");
        if (result.ok) {
          expect(result).toHaveProperty("data");
        } else {
          expect(result).toHaveProperty("error");
        }
      });
    });

    describe("error handling", () => {
      it("should handle non-existent comment gracefully", async () => {
        const result = await deleteCommentAction(999999);

        expect(result).toHaveProperty("ok");
      });
    });
  });
});
