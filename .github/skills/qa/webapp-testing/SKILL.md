---
name: webapp-testing
title: "Web Application Testing"
description: "Use when testing local web applications with Playwright — verifying frontend functionality, debugging UI behavior, capturing screenshots, and viewing browser logs."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [testing, playwright, web, e2e, ui-testing]
metadata:
  hermes:
    tags: [imported]
---
# Web Application Testing

## Overview

Test local web applications using Playwright for end-to-end UI testing, debugging, and verification. This skill covers test creation, execution, and analysis for web applications.

## When to Use

- Testing local web applications during development
- Verifying frontend functionality works as expected
- Debugging UI behavior issues
- Capturing screenshots for documentation or bug reports
- Viewing browser console logs for JavaScript errors
- Running automated E2E tests

## When NOT TO USE

- Production testing (use monitoring tools instead)
- Non-web applications (CLI, API-only services)
- Performance testing (use Lighthouse, k6)
- Unit testing (use Jest, pytest, etc.)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Debug test failures |
| `verification-before-completion` | Verify before claiming done |

## Workflow

### Phase 1: Setup Playwright

```bash
# Install Playwright
npm init -y
npm install -D @playwright/test
npx playwright install

# Or with Bun
bun add -d @playwright/test
bunx playwright install
```

### Phase 2: Create Tests

```typescript
// tests/example.spec.ts
import { test, expect } from '@playwright/test';

test('homepage loads correctly', async ({ page }) => {
  await page.goto('http://localhost:3000');

  // Verify title
  await expect(page).toHaveTitle(/My App/);

  // Verify key elements
  await expect(page.locator('h1')).toBeVisible();
  await expect(page.locator('[data-testid="welcome"]')).toContainText('Welcome');

  // Take screenshot
  await page.screenshot({ path: 'screenshots/homepage.png' });
});

test('user can submit a form', async ({ page }) => {
  await page.goto('http://localhost:3000/contact');

  // Fill form
  await page.fill('[name="email"]', 'test@example.com');
  await page.fill('[name="message"]', 'Hello, this is a test');

  // Submit
  await page.click('button[type="submit"]');

  // Verify success
  await expect(page.locator('.success-message')).toBeVisible();
});
```

### Phase 3: Execute Tests

```bash
# Run all tests
npx playwright test

# Run with browser visible (for debugging)
npx playwright test --headed

# Run specific test file
npx playwright test tests/example.spec.ts

# Run in debug mode
npx playwright test --debug

# View test report
npx playwright show-report
```

### Phase 4: Analyze & Debug

1. Check test results in the HTML report
2. For failures, examine:
   - Screenshot of the failure state
   - Video recording (if enabled)
   - Console logs
   - Network requests
3. Fix the issue and re-run

## Verification Checklist

- [ ] Playwright installed and browsers downloaded
- [ ] Tests written for critical user flows
- [ ] Tests pass locally before pushing
- [ ] Screenshots captured for visual verification
- [ ] Console errors checked and resolved
- [ ] Test report reviewed

## Pitfalls

- **Not waiting for elements:** Use `await expect(locator).toBeVisible()` instead of `sleep()`
- **Hardcoded URLs:** Use environment variables for base URLs
- **Missing test IDs:** Add `data-testid` attributes to elements you need to target
- **Not checking console errors:** Always check for JS errors after navigation
- **Flaky tests:** Avoid timing-dependent assertions; use Playwright's built-in waits
- **Forgetting to close browser:** Playwright handles this, but custom browser instances need cleanup
