import { expect, test } from "@playwright/test";

test.describe("Browse Page", () => {
  test("should display browse page", async ({ page }) => {
    await page.goto("/browse");
    await expect(page).toHaveTitle(/Browse/);
  });

  test("should display browse heading", async ({ page }) => {
    await page.goto("/browse");
    await expect(page.getByRole("heading", { name: /browse/i })).toBeVisible();
  });
});
