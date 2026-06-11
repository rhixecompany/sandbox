import { expect, test } from "@playwright/test";

test.describe("Admin Dashboard Page", () => {
  test("should redirect to sign-in when not authenticated", async ({ page }) => {
    await page.goto("/admin");
    await expect(page).toHaveTitle(/Sign In/);
  });
});
