import { expect, test } from "@playwright/test";

test.describe("Comic Detail Page", () => {
  test("should display 404 for non-existent comic", async ({ page }) => {
    await page.goto("/comics/non-existent-comic");
    await expect(page.getByText(/not found/i)).toBeVisible();
  });
});
