# Testing Patterns

> Extracted from `comicwise-development.prompt.md`.

## Testing Patterns

### Unit Tests (Vitest)

```typescript
import { describe, it, expect, beforeEach } from "vitest";
import { comicDal } from "@/dal/comic-dal";

describe("ComicDal", () => {
  beforeEach(() => {
    // Setup mocks from src/tests/setup-env.ts
  });

  it("should list comics with eager loading", async () => {
    const comics = await comicDal.list();
    expect(comics).toHaveLength(5);
    expect(comics[0].author).toBeDefined(); // Eager loaded
  });
});
```

### E2E Tests (Playwright)

```typescript
import { test, expect } from "@playwright/test";

test.describe("Comic Reader", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("http://localhost:3000/comics/test-comic");
  });

  test("should load chapter and display reader controls", async ({
    page
  }) => {
    await test.step("Load page", async () => {
      await expect(
        page.getByRole("heading", { name: "Chapter 1" })
      ).toBeVisible();
    });

    await test.step("Change reading mode", async () => {
      await page
        .getByRole("button", { name: /reading mode/i })
        .click();
      await expect(
        page.locator("[data-reading-mode]")
      ).toHaveAttribute("data-reading-mode", "scroll");
    });
  });
});
```
