import { expect, test } from "@playwright/test";

test.describe("Asura Scans Navigation", () => {
  test.skip("should display manga series listing", async ({ page }) => {
    test.setTimeout(60000);
    await page.goto("https://asuracomic.net/series");
    await page.waitForLoadState("networkidle");

    const seriesLink = page
      .locator('a[href*="/series/"]', {
        hasText: /MANHWA|Ongoing|Comic/i,
      })
      .first();
    await expect(seriesLink).toBeVisible({ timeout: 15000 });
  });

  test.skip("should navigate to comic detail and read chapter", async ({ page }) => {
    test.setTimeout(60000);
    await page.goto("https://asuracomic.net/series");
    await page.waitForLoadState("networkidle");

    const comicLink = page.locator('a[href*="/series/"]').first();
    await expect(comicLink).toBeVisible({ timeout: 15000 });
    await comicLink.click();
    await page.waitForLoadState("networkidle");
    await expect(page.locator("body")).toBeVisible();

    const chapterLink = page.locator('a[href*="/chapter/"]').first();
    if (await chapterLink.isVisible({ timeout: 5000 }).catch(() => false)) {
      await chapterLink.click();
      await page.waitForLoadState("networkidle");
      await expect(page.locator("body")).toBeVisible();
    }
  });
});
