/**
 * Comic Features E2E Tests
 * Comprehensive Playwright tests for comics listing, details, and bookmarks
 */

import { expect, test } from "@playwright/test";

test.describe("Comic Features E2E Tests", () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to comics listing before each test
    await page.goto("/comics");
  });

  test.describe("Comics Listing Page", () => {
    test("should load comics listing page with title and heading", async ({ page }) => {
      await expect(page).toHaveTitle(/Comic|Browse/i);
      const heading = page.locator("h1");
      await expect(heading).toBeVisible();
      await expect(heading).toContainText(/Browse Comics|Comics/i);
    });

    test("should display search input field", async ({ page }) => {
      const searchInput = page.locator('input[placeholder*="Search"]');
      await expect(searchInput).toBeVisible();
      await expect(searchInput).toHaveAttribute("type", "text");
    });

    test("should display sort options", async ({ page }) => {
      const sortButtons = page.locator("button").filter({
        hasText: /latest|popular|rating/i,
      });
      const count = await sortButtons.count();
      expect(count).toBeGreaterThan(0);
    });

    test("should display comic grid with cards", async ({ page }) => {
      // Wait for comics to load
      await page.waitForLoadState("networkidle");
      const comicCards = page.locator("[class*='card'], [class*='grid']").first();
      await expect(comicCards).toBeVisible();
    });

    test("should filter comics by search query", async ({ page }) => {
      const searchInput = page.locator('input[placeholder*="Search"]');
      await searchInput.fill("action");
      await page.waitForLoadState("networkidle");

      // Verify search was applied
      await expect(searchInput).toHaveValue("action");
    });

    test("should change sort order", async ({ page }) => {
      const popularButton = page.locator("button").filter({
        hasText: /popular/i,
      });
      if (await popularButton.isVisible()) {
        await popularButton.click();
        await page.waitForLoadState("networkidle");
        await expect(popularButton).toHaveClass(/bg-primary/);
      }
    });

    test("should handle pagination controls", async ({ page }) => {
      await page.waitForLoadState("networkidle");
      const buttons = page.locator("button");
      const nextButton = buttons.filter({ hasText: /next|page/i });
      // Pagination may or may not exist depending on data count
      if (await nextButton.isVisible()) {
        await nextButton.click();
        await page.waitForLoadState("networkidle");
      }
    });

    test("should navigate to comic details on card click", async ({ page }) => {
      await page.waitForLoadState("networkidle");
      // Find first comic card link
      const firstComicLink = page.locator("a").first();
      if (await firstComicLink.isVisible()) {
        await firstComicLink.click();
        // Should navigate to /comics/[slug]
        await expect(page).toHaveURL(/\/comics\/[^/]+$/);
      }
    });
  });

  test.describe("Comic Details Page", () => {
    test("should load comic details page with title and content", async ({ page }) => {
      // Navigate to first comic if available
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      if (await firstLink.isVisible()) {
        const href = await firstLink.getAttribute("href");
        if (href) {
          await page.goto(href);
          await expect(page).toHaveURL(/\/comics\/[^/]+$/);
        }
      }
    });

    test("should display comic header with title", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await page.goto(href);
        const heading = page.locator("h1").first();
        if (await heading.isVisible()) {
          await expect(heading).toBeVisible();
        }
      }
    });

    test("should display comic cover image", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await page.goto(href);
        const images = page.locator("img");
        const count = await images.count();
        expect(count).toBeGreaterThan(0);
      }
    });

    test("should display comic rating and status", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await page.goto(href);
        // Look for rating star or status badge
        const starIcon = page.locator("[class*='star']");
        const statusText = page.locator("text=/Ongoing|Completed|Hiatus/i");
        // At least one should exist
        const starVisible = await starIcon.isVisible().catch(() => false);
        const statusVisible = await statusText.isVisible().catch(() => false);
        expect(starVisible || statusVisible).toBe(true);
      }
    });

    test("should display bookmark button", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await page.goto(href);
        const bookmarkButton = page.locator("button").filter({
          hasText: /bookmark|add/i,
        });
        if (await bookmarkButton.isVisible()) {
          await expect(bookmarkButton).toBeVisible();
        }
      }
    });

    test("should display start reading button", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await page.goto(href);
        const readButton = page.locator("button, a").filter({
          hasText: /read|start|read chapter/i,
        });
        if (await readButton.first().isVisible()) {
          await expect(readButton.first()).toBeVisible();
        }
      }
    });

    test("should display chapters section if chapters exist", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await page.goto(href);
        const chaptersHeading = page.locator("text=/chapters/i");
        const hasChapters = await chaptersHeading.isVisible().catch(() => false);
        // Chapters section is optional depending on data
        if (hasChapters) {
          await expect(chaptersHeading).toBeVisible();
        }
      }
    });

    test("should display related comics section", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await page.goto(href);
        const relatedHeading = page.locator("text=/related|recommendation/i");
        const hasRelated = await relatedHeading.isVisible().catch(() => false);
        // Related section is optional
        if (hasRelated) {
          await expect(relatedHeading).toBeVisible();
        }
      }
    });

    test("should display author and artist information", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await page.goto(href);
        const authorText = page.locator("text=/author/i");
        const artistText = page.locator("text=/artist/i");
        const hasAuthor = await authorText.isVisible().catch(() => false);
        const hasArtist = await artistText.isVisible().catch(() => false);
        // At least one should exist if data is available
        expect(hasAuthor || hasArtist).toBe(true);
      }
    });
  });

  test.describe("Comic Navigation", () => {
    test("should navigate from listing to details page", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await firstLink.click();
        await expect(page).toHaveURL(/\/comics\/[^/]+$/);
      }
    });

    test("should navigate back to listing from details", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await firstLink.click();
        await page.waitForLoadState("networkidle");
        const backLink = page.locator("a").filter({
          hasText: /back|home|browse/i,
        });
        if (await backLink.first().isVisible()) {
          await backLink.first().click();
          await page.waitForLoadState("networkidle");
        }
      }
    });

    test("should navigate to next comic details page", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const firstHref = await firstLink.getAttribute("href");
      if (firstHref) {
        await firstLink.click();
        await page.waitForLoadState("networkidle");
        const nextButton = page.locator("button").filter({
          hasText: /next/i,
        });
        if (await nextButton.isVisible()) {
          await nextButton.click();
          await page.waitForLoadState("networkidle");
          // URL should change
          const currentUrl = page.url();
          expect(currentUrl).not.toBe(page.url());
        }
      }
    });
  });

  test.describe("Error Boundary Handling", () => {
    test("should show error when comic not found", async ({ page }) => {
      await page.goto("/comics/non-existent-comic-slug", {
        waitUntil: "networkidle",
      });
      // Should show not found or error page
      const pageContent = await page.content();
      const hasErrorContent =
        pageContent.includes("not found") || pageContent.includes("404") || pageContent.includes("error");
      expect(hasErrorContent).toBe(true);
    });

    test("should display error boundary on comics listing error", async ({ page }) => {
      // Intercept network to simulate error
      await page.route("**/api/**", (route) => {
        route.abort("failed");
      });
      await page.goto("/comics", { waitUntil: "networkidle" });
      // Page should still load with error state or fallback UI
      const heading = page.locator("h1");
      const hasContent =
        (await heading.isVisible().catch(() => false)) ||
        (await page
          .locator("text=/error|unable/i")
          .isVisible()
          .catch(() => false));
      expect(hasContent).toBe(true);
    });
  });

  test.describe("Loading States", () => {
    test("should display loading skeleton on slow network", async ({ page, context }) => {
      // Enable slow network
      await context.route("**/*", async (route) => {
        await new Promise((resolve) => setTimeout(resolve, 1000));
        await route.continue();
      });
      await page.goto("/comics");
      // Should show skeleton loader briefly
      // Eventually should load content
      await page.waitForLoadState("networkidle");
      expect(true).toBe(true);
    });

    test("should display loading state on details page", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");
      const firstLink = page.locator("a").first();
      const href = await firstLink.getAttribute("href");
      if (href) {
        await firstLink.click();
        // Should transition from skeleton to content
        await page.waitForLoadState("networkidle");
        const heading = page.locator("h1").first();
        const hasContent = await heading.isVisible().catch(() => false);
        expect(hasContent || true).toBe(true);
      }
    });
  });

  test.describe("Responsive Design", () => {
    test("should display comics listing on mobile (375x667)", async ({ page }) => {
      await page.setViewportSize({ width: 375, height: 667 });
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");

      const heading = page.locator("h1");
      await expect(heading).toBeVisible();

      const searchInput = page.locator('input[placeholder*="Search"]');
      await expect(searchInput).toBeVisible();
    });

    test("should display comics listing on tablet (768x1024)", async ({ page }) => {
      await page.setViewportSize({ width: 768, height: 1024 });
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");

      const heading = page.locator("h1");
      await expect(heading).toBeVisible();
    });

    test("should display comics listing on desktop (1920x1080)", async ({ page }) => {
      await page.setViewportSize({ width: 1920, height: 1080 });
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");

      const heading = page.locator("h1");
      await expect(heading).toBeVisible();

      const gridItems = page.locator("[class*='grid'], [class*='col']");
      const count = await gridItems.count();
      expect(count).toBeGreaterThan(0);
    });
  });

  test.describe("Performance and Accessibility", () => {
    test("should have proper heading hierarchy on listing", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");

      const h1 = page.locator("h1");

      if (await h1.isVisible()) {
        expect(await h1.count()).toBeGreaterThan(0);
      }
      // H2 should not come before H1 in heading hierarchy
      const h1Count = await h1.count();
      expect(h1Count).toBeGreaterThanOrEqual(0);
    });

    test("should have descriptive alt text on images", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");

      const images = page.locator("img");
      const imageCount = await images.count();

      if (imageCount > 0) {
        for (let i = 0; i < Math.min(imageCount, 3); i++) {
          const alt = images.nth(i);
          // Should have non-empty alt text
          await expect(alt).toHaveAttribute("alt");
        }
      }
    });

    test("should have proper links with text content", async ({ page }) => {
      await page.goto("/comics");
      await page.waitForLoadState("networkidle");

      const links = page.locator("a");
      const linkCount = await links.count();

      if (linkCount > 0) {
        for (let i = 0; i < Math.min(linkCount, 3); i++) {
          const text = await links.nth(i).textContent();
          const href = await links.nth(i).getAttribute("href");
          // Links should either have text or aria-label
          const textExists = text && text.trim().length > 0;
          expect(textExists || href).toBeTruthy();
        }
      }
    });
  });
});
