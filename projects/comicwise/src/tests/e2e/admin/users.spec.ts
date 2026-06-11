import { expect, test } from "@playwright/test";

test.describe("Admin Users Page", () => {
  test("should redirect to sign-in when not authenticated", async ({ page }) => {
    await page.goto("/admin/users");
    await expect(page).toHaveTitle(/Sign In/);
  });
});
