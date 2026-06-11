import { expect, test } from "@playwright/test";

test.describe("Authentication", () => {
  test("sign-in page loads", async ({ page }) => {
    await page.goto("/sign-in");
    // Just verify the page loads without errors
    await expect(page).toHaveURL(/\/sign-in/);
    // Wait for any content to load
    await page.waitForTimeout(1000);
    // Verify page has some content (heading or text)
    const content = page.locator("body");
    await expect(content).toBeVisible();
  });

  test("unauthenticated user redirected from admin", async ({ page }) => {
    // Disable popup dialogs
    page.on("popup", (popup) => popup.close());

    await page.goto("/admin");
    // Should redirect to sign-in
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test("sign-up page loads", async ({ page }) => {
    await page.goto("/sign-up");
    // Just verify the page loads without errors
    await expect(page).toHaveURL(/\/sign-up/);
    // Wait for any content to load
    await page.waitForTimeout(1000);
    // Verify page has some content
    const content = page.locator("body");
    await expect(content).toBeVisible();
  });
});
