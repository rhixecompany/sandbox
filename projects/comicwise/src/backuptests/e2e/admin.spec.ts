import { expect, test } from "@playwright/test";

/**
 * Admin Dashboard E2E Tests
 * Tests admin route protection and basic page loading.
 * Note: Admin sidebar navigation links are placeholder (#) and admin pages
 * (comics, users, chapters) are stubs ("Coming soon..."), so we only test
 * redirect behavior and basic page rendering.
 */

test.describe("Admin Dashboard", () => {
  test("should redirect unauthenticated users to sign-in", async ({ page }) => {
    await page.goto("/admin");

    // Admin layout redirects to /sign-in when not authenticated
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test("should redirect unauthenticated users from admin/comics to sign-in", async ({ page }) => {
    await page.goto("/admin/comics");

    // Should redirect to sign-in
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test("should redirect unauthenticated users from admin/users to sign-in", async ({ page }) => {
    await page.goto("/admin/users");

    // Should redirect to sign-in
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test("should redirect unauthenticated users from admin/chapters to sign-in", async ({ page }) => {
    await page.goto("/admin/chapters");

    // Should redirect to sign-in
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test("should not show error page for admin redirect", async ({ page }) => {
    await page.goto("/admin");

    // After redirect, should be on sign-in page, not an error page
    await expect(page).not.toHaveURL(/error|500/);
    const bodyText = page.locator("body");
    await expect(bodyText).toBeVisible();
  });
});
