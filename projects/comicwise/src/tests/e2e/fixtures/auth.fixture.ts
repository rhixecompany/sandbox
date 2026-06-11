import { test as base } from "@playwright/test";

export interface AuthTestFixtures {
  authenticatedUser: {
    email: string;
    id: string;
    name: string;
  };
}

export const test = base.extend<AuthTestFixtures>({
  authenticatedUser: async ({ page }, withAuth) => {
    await page.goto("/sign-in");
    await page.waitForLoadState("networkidle");
    const testUser = {
      id: "test-user-id",
      email: "test@example.com",
      name: "Test User",
    };
    await withAuth(testUser);
  },
});

export { expect } from "@playwright/test";
