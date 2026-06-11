import { expect, test } from "@playwright/test";

/**
 * Search E2E Tests
 * Tests the /search page with Advanced Search form and results display.
 * The search form requires clicking "Search" button to submit (not auto-search on type).
 */

test.describe("Search Feature", () => {
  test("should display search page with heading and input", async ({ page }) => {
    await page.goto("/search");
    await page.waitForLoadState("networkidle");

    // Heading is "Advanced Search"
    await expect(page.getByRole("heading", { name: /advanced search/i })).toBeVisible();

    // Search input has placeholder "Search by title, description, author..."
    await expect(page.getByPlaceholder(/search by title/i)).toBeVisible();
  });

  test("should search for comics and display results", async ({ page }) => {
    await page.goto("/search");
    await page.waitForLoadState("networkidle");

    // Type a search query
    await page.getByPlaceholder(/search by title/i).fill("manga");

    // Click the Search button to submit (use form submit button, not header search)
    await page.getByTestId("advanced-search-form").getByRole("button", { name: "Search" }).click();

    // Wait for navigation and results
    await page.waitForLoadState("networkidle");

    // Either results container or "No comics found" message should appear
    const resultsContainer = page.locator("[data-testid='search-results']");
    const noResults = page.getByText(/no comics found/i);

    const hasResults = await resultsContainer.isVisible();
    const hasNoResults = await noResults.isVisible();

    expect(hasResults || hasNoResults).toBe(true);
  });

  test("should show empty state when no results match", async ({ page }) => {
    await page.goto("/search");
    await page.waitForLoadState("networkidle");

    // Search for non-existent comic
    await page.getByPlaceholder(/search by title/i).fill("xyznonexistentcomicxyz");

    // Click Search button (use form submit button, not header search)
    await page.getByTestId("advanced-search-form").getByRole("button", { name: "Search" }).click();
    await page.waitForLoadState("networkidle");

    // Should show "No comics found" message
    await expect(page.getByText(/no comics found/i)).toBeVisible();
  });

  test("should handle search with special characters", async ({ page }) => {
    await page.goto("/search");
    await page.waitForLoadState("networkidle");

    // Search with special characters
    await page.getByPlaceholder(/search by title/i).fill("test@#$%");

    // Click Search button (use form submit button, not header search)
    await page.getByTestId("advanced-search-form").getByRole("button", { name: "Search" }).click();
    await page.waitForLoadState("networkidle");

    // Should not crash
    await expect(page).not.toHaveURL(/error|500/);
  });

  test("should update URL with search parameters after search", async ({ page }) => {
    await page.goto("/search");
    await page.waitForLoadState("networkidle");

    await page.getByPlaceholder(/search by title/i).fill("test");

    // Click Search to submit (URL updates on submit, not on type)
    await page.getByTestId("advanced-search-form").getByRole("button", { name: "Search" }).click();

    // Wait for URL to update with search params
    await page.waitForURL(/\?q=test/);
    await page.waitForLoadState("networkidle");

    // URL should contain the search query parameter
    const url = page.url();
    expect(url).toContain("q=test");
  });

  test("should display status filter dropdown", async ({ page }) => {
    await page.goto("/search");
    await page.waitForLoadState("networkidle");

    // Status filter has a select trigger with placeholder "All statuses"
    const statusTrigger = page.locator("#status-filter");
    await expect(statusTrigger).toBeVisible();
  });

  test("should display sort filter dropdown", async ({ page }) => {
    await page.goto("/search");
    await page.waitForLoadState("networkidle");

    // Sort filter select
    const sortTrigger = page.locator("#sort-filter");
    await expect(sortTrigger).toBeVisible();
  });

  test("should navigate to comic from search results", async ({ page }) => {
    await page.goto("/search");
    await page.waitForLoadState("networkidle");

    // Search for something likely to return results
    await page.getByPlaceholder(/search by title/i).fill("a");
    await page.getByTestId("advanced-search-form").getByRole("button", { name: "Search" }).click();
    await page.waitForLoadState("networkidle");

    // Click first result item if available
    const firstResult = page.locator("[data-testid='search-result-item']").first();
    if (await firstResult.isVisible()) {
      await firstResult.click();

      // Should navigate to comic detail page
      await expect(page).toHaveURL(/\/comics\/[^/]+/);
    }
  });
});
