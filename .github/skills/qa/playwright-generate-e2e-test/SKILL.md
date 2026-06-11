---
name: playwright-generate-e2e-test
description: "Generate Playwright E2E tests for new features"
applyTo: "src/tests/**/*.ts,src/tests/**/*.tsx"
---

# Playwright E2E Test Generation

Your goal is to generate a Playwright test based on the provided scenario after completing all prescribed steps.


## When to Use

- Use this skill when working with playwright generate e2e test tasks
- Triggered by: `playwright-generate-e2e-test` related operations

## Specific Instructions

- You are given a scenario, and you need to generate a playwright test for it. If the user does not provide a scenario, you will ask them to provide one.
- DO NOT generate test code prematurely or based solely on the scenario without completing all prescribed steps.
- DO run steps one by one using the tools provided by the Playwright MCP.
- Only after all steps are completed, emit a Playwright TypeScript test that uses `@playwright/test` based on message history
- Save generated test file in the tests directory
- Execute the test file and iterate until the test passes
- Use Playwright for browser automation and E2E tests
- Follow Page Object pattern for maintainability
- Ensure cross-browser compatibility
- Document test steps and expected outcomes
- Integrate with CI workflow for test automation
