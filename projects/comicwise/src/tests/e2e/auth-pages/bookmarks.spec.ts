import { expect, test } from "@playwright/test";

test.describe("Bookmarks Page", () => {
  test("should redirect to sign-in when not authenticated", async ({ page }) => {
    await page.goto("/bookmarks");
    await expect(page).toHaveTitle(/Sign In/);
  });
});
