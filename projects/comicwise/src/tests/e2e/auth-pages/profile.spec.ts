import { expect, test } from "@playwright/test";

test.describe("Profile Page", () => {
  test("should redirect to sign-in when not authenticated", async ({ page }) => {
    await page.goto("/profile");
    await expect(page).toHaveTitle(/Sign In/);
  });
});
