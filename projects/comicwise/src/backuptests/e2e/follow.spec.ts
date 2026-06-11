import { expect, test } from "@playwright/test";

test.describe("Follow System", () => {
  test("should redirect unauthenticated users from followers page", async ({ page }) => {
    await page.goto("/profile/user-123/followers");
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test("should redirect unauthenticated users from following page", async ({ page }) => {
    await page.goto("/profile/user-123/following");
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test.skip("should show empty state when no followers", async ({ page }) => {
    await page.goto("/profile/user-123/followers");
    await expect(page.locator("text=No followers yet")).toBeVisible();
  });
});
