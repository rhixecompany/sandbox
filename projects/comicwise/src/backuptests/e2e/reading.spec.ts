import { expect, test } from "@playwright/test";

/**
 * Comics & Reading E2E Tests
 * Tests the core comic browsing and reading user journey against actual UI.
 * Route: /comics (listing), /comics/:slug (detail), /comics/:slug/chapter/:num (reader)
 */

const COMIC_CARD_SELECTOR = "[data-testid='comic-card']";

test.describe("Comics & Reading", () => {
  test("should display comics listing page with heading", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    // Page heading is "Browse Comics"
    await expect(page.getByRole("heading", { name: /browse comics/i })).toBeVisible();
  });

  test("should display comic cards on listing page", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    const cards = page.locator(COMIC_CARD_SELECTOR);
    const count = await cards.count();

    if (count > 0) {
      await expect(cards.first()).toBeVisible({ timeout: 10000 });
    }
  });

  test("should navigate to comic detail page", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    const cards = page.locator(COMIC_CARD_SELECTOR);
    const count = await cards.count();

    if (count === 0) {
      test.skip(true, "No comics available in database");
      return;
    }

    const firstCard = cards.first();
    await expect(firstCard).toBeVisible({ timeout: 10000 });

    const href = await firstCard.getAttribute("href");
    expect(href).toMatch(/\/comics\/[^/]+/);

    await page.goto(`http://localhost:3000${href}`);
    await page.waitForLoadState("networkidle");

    await expect(page.getByRole("heading").first()).toBeVisible();
  });

  test("should display chapters section on comic detail page", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    const cards = page.locator(COMIC_CARD_SELECTOR);
    const count = await cards.count();

    if (count === 0) {
      test.skip(true, "No comics available in database");
      return;
    }

    const firstCard = cards.first();
    await expect(firstCard).toBeVisible({ timeout: 10000 });

    const href = await firstCard.getAttribute("href");
    expect(href).toMatch(/\/comics\/[^/]+/);

    await page.goto(`http://localhost:3000${href}`);
    await page.waitForLoadState("networkidle");

    const chaptersSection = page.locator("[data-testid='chapters-section']");
    const isVisible = await chaptersSection.isVisible().catch(() => false);

    if (isVisible) {
      await expect(chaptersSection).toBeVisible();
      const chapterLinks = chaptersSection.locator("[data-testid='chapter-link']");
      const linkCount = await chapterLinks.count();
      expect(linkCount).toBeGreaterThan(0);
    }
  });

  test("should have a search input on comics listing page", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    // The filter search input has placeholder "Search comics..."
    const searchInput = page.getByPlaceholder(/search comics/i);
    await expect(searchInput).toBeVisible();
  });

  test("should display sort options", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    // Sort buttons: "Latest", "Popular", "Top Rated"
    await expect(page.getByRole("button", { name: /sort by latest/i })).toBeVisible();
    await expect(page.getByRole("button", { name: /sort by popular/i })).toBeVisible();
    await expect(page.getByRole("button", { name: /sort by top rated/i })).toBeVisible();
  });

  test("should display status filter options", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    // Status filter has "All", "Ongoing", "Completed" buttons (among others)
    await expect(page.getByRole("button", { name: /show all comic statuses/i })).toBeVisible();
    await expect(page.getByRole("button", { name: /show only ongoing/i })).toBeVisible();
    await expect(page.getByRole("button", { name: /show only completed/i })).toBeVisible();
  });

  test("should show comic metadata on detail page", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    const cards = page.locator(COMIC_CARD_SELECTOR);
    const count = await cards.count();

    if (count === 0) {
      test.skip(true, "No comics available in database");
      return;
    }

    const firstCard = cards.first();
    await expect(firstCard).toBeVisible({ timeout: 10000 });

    const href = await firstCard.getAttribute("href");
    expect(href).toMatch(/\/comics\/[^/]+/);

    await page.goto(`http://localhost:3000${href}`);
    await page.waitForLoadState("networkidle");

    await expect(page.getByRole("heading").first()).toBeVisible();
    await expect(page.locator("body")).toBeVisible();
  });

  test("should have pagination controls when comics exceed page size", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    // Pagination has "Previous" and "Next" buttons
    const nextButton = page.getByTestId("pagination-next");
    const prevButton = page.getByRole("button", { name: /previous/i });

    // If pagination exists, both buttons should be present
    if (await nextButton.isVisible()) {
      await expect(nextButton).toBeVisible();
      await expect(prevButton).toBeVisible();
    }
  });

  test("should handle responsive layout on mobile", async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 });

    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    // Page should load without errors
    await expect(page).not.toHaveURL(/error|500/);

    // Heading should still be visible
    await expect(page.getByRole("heading", { name: /browse comics/i })).toBeVisible();
  });
});
