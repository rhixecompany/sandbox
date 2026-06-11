import { expect, test } from "@playwright/test";

test.describe("Search Page", () => {
  test("should display search page", async ({ page }) => {
    await page.goto("/search");
    await expect(page).toHaveTitle(/Search/);
  });

  test("should display search input", async ({ page }) => {
    await page.goto("/search");
    await expect(page.getByPlaceholder(/search/i)).toBeVisible();
  });
});
