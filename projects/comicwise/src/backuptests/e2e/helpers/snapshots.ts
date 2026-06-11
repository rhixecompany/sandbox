import type { Locator, Page } from "@playwright/test";
import { expect } from "@playwright/test";

export interface SnapshotConfig {
  name: string;
  threshold?: number;
}

const DEFAULT_THRESHOLD = 0.2;

export async function captureSnapshot(page: Page, config: SnapshotConfig): Promise<void> {
  const { name, threshold = DEFAULT_THRESHOLD } = config;

  await page.waitForLoadState("networkidle");
  await page.waitForTimeout(500);

  await expect(page).toHaveScreenshot(`${name}.png`, { maxDiffPixelRatio: threshold });
}

export async function captureFullPageSnapshot(page: Page, config: SnapshotConfig): Promise<void> {
  const { name, threshold = DEFAULT_THRESHOLD } = config;

  await page.waitForLoadState("networkidle");
  await page.waitForTimeout(500);

  await expect(page).toHaveScreenshot(`${name}-full.png`, {
    fullPage: true,
    maxDiffPixelRatio: threshold,
  });
}

export async function captureElementSnapshot(locator: Locator, config: SnapshotConfig): Promise<void> {
  const { name, threshold = DEFAULT_THRESHOLD } = config;

  await locator.waitFor();
  await expect(locator).toHaveScreenshot(`${name}-element.png`, {
    maxDiffPixelRatio: threshold,
  });
}

export function createSnapshotGroup(name: string) {
  return {
    async capture(page: Page, variant?: string): Promise<void> {
      const snapshotName = variant ? `${name}-${variant}` : name;
      await captureSnapshot(page, { name: snapshotName });
    },
    async captureFullPage(page: Page, variant?: string): Promise<void> {
      const snapshotName = variant ? `${name}-${variant}-full` : `${name}-full`;
      await captureFullPageSnapshot(page, { name: snapshotName });
    },
    async captureElement(locator: Locator, variant?: string): Promise<void> {
      const snapshotName = variant ? `${name}-${variant}-element` : `${name}-element`;
      await captureElementSnapshot(locator, { name: snapshotName });
    },
  };
}
