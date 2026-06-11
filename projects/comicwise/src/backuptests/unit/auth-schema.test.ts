import { describe, expect, it } from "vitest";

import { signInSchema, signUpSchema } from "@/schemas/auth.schema";

describe("signInSchema", () => {
  it("validates correct credentials", () => {
    expect(signInSchema.safeParse({ email: "user@test.com", password: "password123" }).success).toBe(true);
  });
  it("rejects invalid email", () => {
    expect(signInSchema.safeParse({ email: "notanemail", password: "password123" }).success).toBe(false);
  });
  it("rejects short password", () => {
    expect(signInSchema.safeParse({ email: "user@test.com", password: "short" }).success).toBe(false);
  });
});

describe("signUpSchema", () => {
  it("rejects mismatched passwords", () => {
    const result = signUpSchema.safeParse({
      name: "Test User",
      email: "user@test.com",
      password: "password123",
      confirmPassword: "different",
    });
    expect(result.success).toBe(false);
    expect(result.error?.issues[0]?.message).toBe("Passwords do not match");
  });
});
