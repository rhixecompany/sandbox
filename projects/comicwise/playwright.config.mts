import { defineConfig, devices } from "@playwright/test";

/**
 * See https://playwright.dev/docs/test-configuration.
 */
export default defineConfig({
  testDir: "./src/tests/e2e",
  /* Run tests in files in parallel */
  fullyParallel: true,
  /* Fail the build on CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env["CI"],
  /* Retry on CI only */
  retries: process.env["CI"] ? 2 : 1,
  /* Opt out of parallel tests on CI. */
  workers: process.env["CI"] ? 1 : 2,

  /* Global setup - seed database before tests */
  // globalSetup: "./src/tests/e2e/global-setup.ts",
  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: "html",
  /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
  use: {
    /* Base URL to use in actions like `await page.goto('')`. */
    baseURL: "http://localhost:3000",

    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    trace: "on-first-retry",

    /* Screenshots only on failure to save disk space */
    screenshot: "only-on-failure",

    /* Video only on failure to save disk space */
    video: "retain-on-failure",

    /* Fail fast on slow actions */
    actionTimeout: 15000,

    /* Fail fast on slow navigation */
    navigationTimeout: 60000,
  },

  /* Configure projects for major browsers */
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
  ],

  /* Run your local dev server before starting the tests */
  webServer: {
    command: "pnpm dev",
    url: "http://localhost:3000",
    reuseExistingServer: false,
    timeout: 120 * 1000,
  },
});
