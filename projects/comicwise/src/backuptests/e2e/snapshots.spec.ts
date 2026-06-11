import { test } from "@playwright/test";

import { createSnapshotGroup } from "./helpers/snapshots";

test.describe("Visual Regression", () => {
  test.describe.configure({ mode: "parallel" });

  const homeGroup = createSnapshotGroup("home");
  const comicsGroup = createSnapshotGroup("comics");
  const searchGroup = createSnapshotGroup("search");

  test("homepage renders correctly", async ({ page }) => {
    await page.goto("/");
    await homeGroup.captureFullPage(page);
  });

  test("comics listing page renders correctly", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");
    await comicsGroup.captureFullPage(page);
  });

  test("search page renders correctly", async ({ page }) => {
    await page.goto("/search");
    await page.waitForLoadState("networkidle");
    await searchGroup.captureFullPage(page);
  });

  test("search page with results renders correctly", async ({ page }) => {
    await page.goto("/search?q=one");
    await page.waitForLoadState("networkidle");
    await searchGroup.capture(page, "with-results");
  });

  test("comic card renders correctly", async ({ page }) => {
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");

    const firstCard = page.locator("[data-testid='comic-card']").first();
    if (await firstCard.isVisible()) {
      await comicsGroup.captureElement(firstCard, "card");
    }
  });

  test("dark mode renders correctly", async ({ page }) => {
    await page.emulateMedia({ colorScheme: "dark" });
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");
    await comicsGroup.capture(page, "dark");
  });

  test("mobile view renders correctly", async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 });
    await page.goto("/comics");
    await page.waitForLoadState("networkidle");
    await comicsGroup.capture(page, "mobile");
  });
});
