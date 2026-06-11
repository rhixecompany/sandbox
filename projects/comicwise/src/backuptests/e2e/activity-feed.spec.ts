import { expect, test } from "@playwright/test";

test.describe("Activity Feed", () => {
  test("should redirect unauthenticated users from feed page", async ({ page }) => {
    await page.goto("/feed");
    await expect(page).toHaveURL(/\/sign-in/);
  });
});
