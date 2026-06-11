import { expect, test } from "@playwright/test";

test.describe("Admin RBAC Pages", () => {
  test("should redirect unauthenticated users from roles page", async ({ page }) => {
    await page.goto("/admin/roles");
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test("should redirect unauthenticated users from permissions page", async ({ page }) => {
    await page.goto("/admin/permissions");
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test("should redirect unauthenticated users from audit-logs page", async ({ page }) => {
    await page.goto("/admin/audit-logs");
    await expect(page).toHaveURL(/\/sign-in/);
  });

  test.skip("should show roles management page for admin", async ({ page }) => {
    await page.goto("/admin/roles");
    await expect(page.locator("text=Roles Management")).toBeVisible();
  });

  test.skip("should show permissions management page for admin", async ({ page }) => {
    await page.goto("/admin/permissions");
    await expect(page.locator("text=Permissions Management")).toBeVisible();
  });

  test.skip("should show audit logs page for admin", async ({ page }) => {
    await page.goto("/admin/audit-logs");
    await expect(page.locator("text=Audit Logs")).toBeVisible();
  });
});
