import { expect, test } from "@playwright/test";

test.describe("Notifications Page", () => {
  test("should redirect to sign-in when not authenticated", async ({ page }) => {
    await page.goto("/notifications");
    await expect(page).toHaveTitle(/Sign In/);
  });
});
