import { defineConfig } from "vitest/config";

export default defineConfig({
  resolve: {
    tsconfigPaths: true,
  },
  test: {
    environment: "happy-dom",
    setupFiles: ["./src/tests/unit/setup-env.ts"],
    include: ["src/tests/unit/**/*.test.{ts,tsx,js,jsx}"],
    exclude: ["**/.references/**", "**/tests/e2e/**", "**/node_modules/**", "src/backuptests/**"],
    pool: "forks",
    testTimeout: 30000,
    hookTimeout: 15000,
  },
});
