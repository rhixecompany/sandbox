import { expect, test } from "@playwright/test";

test.describe("Genre Page", () => {
  test("should display 404 for non-existent genre", async ({ page }) => {
    await page.goto("/genres/99999");
    await expect(page.getByText(/not found/i)).toBeVisible();
  });
});
