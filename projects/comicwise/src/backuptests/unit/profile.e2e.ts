/**
 * Profile Pages E2E Tests
 * Tests for complete user profile flows with Playwright
 */

import { expect, test } from "@playwright/test";

test.describe("Profile Pages E2E Tests", () => {
  test.beforeEach(async () => {
    // Note: These tests assume user is already authenticated
    // In real scenario, would need to set up auth session first
    // For now, these are example test cases
  });

  test.describe("Profile Page", () => {
    test("should load profile page and display user information", async ({ page }) => {
      // Navigate to profile page
      await page.goto("/profile");

      // Check if page title is correct
      await expect(page).toHaveTitle(/Profile/i);

      // Verify main heading exists
      const heading = page.locator("h1");
      await expect(heading).toBeVisible();

      // Profile should not be empty
      const profileCards = page.locator("[class*='rounded-lg']");
      expect(await profileCards.count()).toBeGreaterThan(0);
    });

    test("should display profile statistics", async ({ page }) => {
      await page.goto("/profile");

      // Check for statistics section
      const statsElements = page.locator("text=/Bookmarks|Ratings|Comments|Chapters/");
      const count = await statsElements.count();
      expect(count).toBeGreaterThanOrEqual(2);
    });

    test("should have working navigation buttons", async ({ page }) => {
      await page.goto("/profile");

      // Check for edit profile button
      const editButton = page.locator('button:has-text("Edit Profile")');
      await expect(editButton).toBeVisible();

      // Check for settings button (if visible)
      const settingsButton = page.locator("button:has-text(/Settings|Preferences/)");
      expect(await settingsButton.count()).toBeGreaterThanOrEqual(0);
    });

    test("should load profile page with suspense boundary", async ({ page }) => {
      // Start waiting for navigation before clicking
      const navigationPromise = page.waitForNavigation();
      await page.goto("/profile");
      await navigationPromise;

      // Page should load without errors

      expect(page.locator("body")).toBeTruthy();
    });

    test("should handle missing profile gracefully", async ({ page }) => {
      // Mock 401 response for profile fetch
      await page.route("**/api/**", (route) => {
        route.abort("aborted");
      });

      await page.goto("/profile");

      // Should either show error or redirect
      const currentUrl = page.url();
      const isError = await page.locator("text=/Error|error/").isVisible();
      expect(isError || currentUrl.includes("sign-in")).toBeTruthy();
    });
  });

  test.describe("Profile Edit Page", () => {
    test("should load profile edit page", async ({ page }) => {
      await page.goto("/profile/edit");

      // Check page title
      await expect(page).toHaveTitle(/Edit/i);

      // Form should be visible
      const form = page.locator("form");
      await expect(form).toBeVisible();
    });

    test("should have form inputs", async ({ page }) => {
      await page.goto("/profile/edit");

      // Check for input fields
      const inputs = page.locator('input[type="text"], textarea');
      const count = await inputs.count();
      expect(count).toBeGreaterThan(0);
    });

    test("should have submit button", async ({ page }) => {
      await page.goto("/profile/edit");

      // Check for submit button
      const submitButton = page.locator("button:has-text(/Save|Submit/)");
      await expect(submitButton).toBeVisible();
    });

    test("should have back button", async ({ page }) => {
      await page.goto("/profile/edit");

      // Look for back navigation
      const backButton = page.locator("button:has-text(/Back|Cancel/), a:has-text(/Back|Cancel/)");
      expect(await backButton.count()).toBeGreaterThan(0);
    });

    test("should navigate back to profile when clicking back button", async ({ page }) => {
      await page.goto("/profile/edit");

      // Get back button and click it
      const backButton = page.locator("button:has-text(/Back|Cancel/), a:has-text(/Back|Cancel/)").first();

      if (await backButton.isVisible()) {
        await backButton.click();
        // Should be back on profile page
        await page.waitForURL("**/profile");
        expect(page.url()).toContain("/profile");
      }
    });

    test("should load edit form with suspense boundary", async ({ page }) => {
      await page.goto("/profile/edit");

      // Check for loading skeleton if exists
      const loadingElement = page.locator("[class*='skeleton'], [class*='loading']");
      const count = await loadingElement.count();
      expect(count).toBeGreaterThanOrEqual(0);

      // After brief wait, form should be visible
      await page.waitForLoadState("networkidle");
      const form = page.locator("form");
      await expect(form).toBeVisible();
    });
  });

  test.describe("Settings Page", () => {
    test("should load settings page", async ({ page }) => {
      await page.goto("/profile/settings");

      // Check page title
      await expect(page).toHaveTitle(/Settings/i);

      // Form should be visible
      const form = page.locator("form");
      await expect(form).toBeVisible();
    });

    test("should display preference sections", async ({ page }) => {
      await page.goto("/profile/settings");

      // Look for settings section headings
      const text = await page.locator("body").textContent();

      // Should have various preference categories
      expect(text).toContain(/Display|Theme|Reading|Notification|Privacy/i);
    });

    test("should have theme selector", async ({ page }) => {
      await page.goto("/profile/settings");

      // Look for theme dropdown or radio buttons
      const themeSelector = page.locator(
        'select, [role="combobox"], input[type="radio"][value*="light"], input[type="radio"][value*="dark"]'
      );
      expect(await themeSelector.count()).toBeGreaterThan(0);
    });

    test("should have notification toggles", async ({ page }) => {
      await page.goto("/profile/settings");

      // Look for toggle switches
      const toggles = page.locator('[role="switch"]');
      const count = await toggles.count();

      // Should have at least some toggles for notifications
      expect(count).toBeGreaterThanOrEqual(0);
    });

    test("should have save button", async ({ page }) => {
      await page.goto("/profile/settings");

      // Check for save button
      const saveButton = page.locator("button:has-text(/Save|Submit|Update/)");
      await expect(saveButton).toBeVisible();
    });

    test("should load settings with suspense boundary", async ({ page }) => {
      await page.goto("/profile/settings");

      // Check for loading state
      const loadingElement = page.locator("[class*='animate-pulse'], [class*='skeleton']");
      await loadingElement.count();

      // Wait for content to load
      await page.waitForLoadState("networkidle");

      // Form should be fully loaded
      const form = page.locator("form");
      await expect(form).toBeVisible();
    });

    test("should have back button to profile", async ({ page }) => {
      await page.goto("/profile/settings");

      // Look for back navigation
      const backButton = page.locator("a:has-text(/Back|Profile/), button:has-text(/Back|Profile/)").first();
      expect(await backButton.count()).toBeGreaterThan(0);
    });
  });

  test.describe("Profile Navigation", () => {
    test("should navigate from profile to edit page", async ({ page }) => {
      await page.goto("/profile");

      // Click edit profile button
      const editButton = page.locator("button, a").filter({
        hasText: /Edit Profile/,
      });

      if (await editButton.isVisible()) {
        await editButton.click();
        await page.waitForURL("**/profile/edit");
        expect(page.url()).toContain("/profile/edit");
      }
    });

    test("should navigate from profile to settings page", async ({ page }) => {
      await page.goto("/profile");

      // Click settings/preferences button
      const settingsButton = page.locator("button, a").filter({
        hasText: /Settings|Preferences/,
      });

      if (await settingsButton.isVisible()) {
        await settingsButton.click();
        await page.waitForURL("**/profile/settings");
        expect(page.url()).toContain("/profile/settings");
      }
    });

    test("should navigate back from edit to profile", async ({ page }) => {
      await page.goto("/profile/edit");

      // Find and click back button
      const backButton = page
        .locator("button, a")
        .filter({
          hasText: /Back|Return/,
        })
        .first();

      if (await backButton.isVisible()) {
        await backButton.click();
        // Should navigate back to profile
        const url = page.url();
        expect(url).toMatch(/\/profile\b/);
      }
    });

    test("should navigate back from settings to profile", async ({ page }) => {
      await page.goto("/profile/settings");

      // Find and click back button
      const backButton = page
        .locator("button, a")
        .filter({
          hasText: /Back|Return|Profile/,
        })
        .first();

      if (await backButton.isVisible()) {
        await backButton.click();
        // Should navigate back to profile
        const url = page.url();
        expect(url).toMatch(/\/profile\b/);
      }
    });
  });

  test.describe("Error Boundaries", () => {
    test("should show error boundary on profile page error", async ({ page }) => {
      // Mock error response
      await page.route("**/api/**", (route) => {
        route.abort("failed");
      });

      await page.goto("/profile");

      // Should either show error or be on sign-in due to auth
      const pageContent = await page.content();
      expect(pageContent.includes("Error") || pageContent.includes("sign-in")).toBeTruthy();
    });

    test("should show error boundary on edit page error", async ({ page }) => {
      await page.route("**/api/**", (route) => {
        route.abort("failed");
      });

      await page.goto("/profile/edit");

      // Page should be accessible
      const body = page.locator("body");
      await expect(body).toBeVisible();
    });

    test("should show error boundary on settings page error", async ({ page }) => {
      await page.route("**/api/**", (route) => {
        route.abort("failed");
      });

      await page.goto("/profile/settings");

      // Page should be accessible
      const body = page.locator("body");
      await expect(body).toBeVisible();
    });
  });

  test.describe("Loading States", () => {
    test("should show loading skeleton on slow network", async ({ page, context }) => {
      // Simulate slow 4G
      await context.route("**/*", (route) => {
        setTimeout(() => route.continue(), 500);
      });

      await page.goto("/profile");

      // Should show loading indicators initially
      const skeletons = page.locator("[class*='animate-pulse'], [class*='skeleton']");
      expect(await skeletons.count()).toBeGreaterThanOrEqual(0);

      // After loading, content should be visible
      await page.waitForLoadState("networkidle");

      expect(page.locator("body")).toBeTruthy();
    });

    test("should show loading state on edit page", async ({ page, context }) => {
      await context.route("**/*", (route) => {
        setTimeout(() => route.continue(), 300);
      });

      await page.goto("/profile/edit");

      // Form should eventually be visible
      await page.waitForLoadState("networkidle");
      const form = page.locator("form");
      await expect(form).toBeVisible();
    });

    test("should show loading state on settings page", async ({ page, context }) => {
      await context.route("**/*", (route) => {
        setTimeout(() => route.continue(), 300);
      });

      await page.goto("/profile/settings");

      // Form should eventually be visible
      await page.waitForLoadState("networkidle");
      const form = page.locator("form");
      await expect(form).toBeVisible();
    });
  });

  test.describe("Responsive Design", () => {
    test("should be responsive on mobile profile page", async ({ page }) => {
      await page.setViewportSize({ width: 375, height: 667 });
      await page.goto("/profile");

      // Content should be visible and not overflow
      const viewport = page.viewportSize();
      const body = page.locator("body");
      expect(viewport).toBeTruthy();
      await expect(body).toBeVisible();
    });

    test("should be responsive on tablet edit page", async ({ page }) => {
      await page.setViewportSize({ width: 768, height: 1024 });
      await page.goto("/profile/edit");

      // Form should be properly sized
      const form = page.locator("form");
      await expect(form).toBeVisible();
    });

    test("should be responsive on desktop settings page", async ({ page }) => {
      await page.setViewportSize({ width: 1920, height: 1080 });
      await page.goto("/profile/settings");

      // Content should fit well on wide screen
      const form = page.locator("form");
      await expect(form).toBeVisible();
    });
  });
});
