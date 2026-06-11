import { expect, test } from "@playwright/test";

test.describe("Author Page", () => {
  test("should display 404 for non-existent author", async ({ page }) => {
    await page.goto("/authors/99999");
    await expect(page.getByText(/not found/i)).toBeVisible();
  });
});
