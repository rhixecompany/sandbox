import { test as base } from "@playwright/test";

export interface AdminTestFixtures {
  adminUser: {
    email: string;
    id: string;
    name: string;
    role: string;
  };
}

export const test = base.extend<AdminTestFixtures>({
  adminUser: async ({ page }, withAdmin) => {
    await page.goto("/sign-in");
    await page.waitForLoadState("networkidle");
    const adminUser = {
      id: "admin-user-id",
      email: "admin@example.com",
      name: "Admin User",
      role: "admin",
    };
    await withAdmin(adminUser);
  },
});

export { expect } from "@playwright/test";
