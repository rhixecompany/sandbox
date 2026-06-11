import { expect, test } from "@playwright/test";

test.describe("Comics Page", () => {
  test("should display comics page", async ({ page }) => {
    await page.goto("/comics");
    await expect(page).toHaveTitle(/ComicWise/);
  });

  test("should display comics list", async ({ page }) => {
    await page.goto("/comics");
    await expect(page.getByRole("heading", { name: /comic/i })).toBeVisible();
  });
});
