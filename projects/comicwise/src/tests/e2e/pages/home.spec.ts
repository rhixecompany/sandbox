import { expect, test } from "@playwright/test";

test.describe("Home Page", () => {
  test("should display page title", async ({ page }) => {
    await page.goto("/");
    await expect(page).toHaveTitle(/ComicWise/);
  });

  test("should display navigation links", async ({ page }) => {
    await page.goto("/");
    await expect(page.getByRole("link", { name: /comics/i })).toBeVisible();
  });
});
