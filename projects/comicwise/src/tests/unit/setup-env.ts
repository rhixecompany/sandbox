import { vi } from "vitest";

vi.mock("@/auth", () => ({
  auth: vi.fn().mockResolvedValue({
    user: { id: "test-user-id", email: "test@example.com", role: "user" },
  }),
}));
