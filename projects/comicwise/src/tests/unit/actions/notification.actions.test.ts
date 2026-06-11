import { getNotificationsAction } from "@/actions/notification.actions";
import { describe, expect, it, vi } from "vitest";

vi.mock("@/auth", () => ({
  auth: vi.fn().mockResolvedValue({ user: null }),
}));

describe("getNotificationsAction", () => {
  it("should return error when not authenticated", async () => {
    const result = await getNotificationsAction();
    expect(result.ok).toBe(false);
  });
});
