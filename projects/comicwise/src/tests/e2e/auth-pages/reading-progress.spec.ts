import { expect, test } from "@playwright/test";

test.describe("Reading Progress Page", () => {
  test("should redirect to sign-in when not authenticated", async ({ page }) => {
    await page.goto("/reading-progress");
    await expect(page).toHaveTitle(/Sign In/);
  });
});
