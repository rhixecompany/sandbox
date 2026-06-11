import { expect, test } from "@playwright/test";

test.describe("Profile Settings Page", () => {
  test("should redirect to sign-in when not authenticated", async ({ page }) => {
    await page.goto("/profile/settings");
    await expect(page).toHaveTitle(/Sign In/);
  });
});
