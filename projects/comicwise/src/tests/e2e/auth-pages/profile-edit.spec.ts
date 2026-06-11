import { expect, test } from "@playwright/test";

test.describe("Profile Edit Page", () => {
  test("should redirect to sign-in when not authenticated", async ({ page }) => {
    await page.goto("/profile/edit");
    await expect(page).toHaveTitle(/Sign In/);
  });
});
