---
name: agent-browser
title: Agent Browser
description: "Browser automation CLI for AI agents. Use when automating web interactions, filling forms, clicking buttons, taking screenshots, scraping data, testing web apps, or automating Electron desktop apps."
---

## Description

Browser automation CLI for AI agents. Automate web interactions including navigating pages, filling forms, clicking buttons, taking screenshots, extracting data, and testing web apps. Also supports automating Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify).

## When to Use

Use this skill when:

- Interacting with websites programmatically
- Filling out forms automatically
- Taking screenshots for verification
- Scraping data from pages
- Testing web applications
- Automating browser actions
- Automating Electron desktop apps
- Checking Slack unreads or sending messages
- Running browser automation in cloud environments

**Triggers**: "Open a website", "Fill out a form", "Click a button", "Take a screenshot", "Scrape data from a page", "Test this web app", "Login to a site", "Automate browser actions"

## When NOT to Use

- For static HTML generation (use web-artifacts-builder instead)
- For API testing (use httpie instead)
- For unit testing (use test-driven-development instead)
- For code review (use requesting-code-review instead)

## Workflow

### Phase 1: Setup

- Initialize browser automation
- Configure browser type (Chrome, Firefox, WebKit)
- Set up authentication if needed

### Phase 2: Navigation & Interaction

- Navigate to target URL
- Locate elements using selectors
- Perform actions (click, type, select)
- Handle dialogs and popups

### Phase 3: Data Extraction

- Extract text content
- Capture screenshots
- Get element properties
- Collect network requests

### Phase 4: Verification

- Verify page state
- Check for errors
- Validate extracted data
- Document results

## Tools & References

**Related Skills**:

- web-artifacts-builder - Build HTML artifacts
- webapp-testing - Test local web applications
- httpie - Test APIs

**Supported Browsers**:

- Chrome/Chromium
- Firefox
- WebKit (Safari)
- Microsoft Edge

## Best Practices

- **Explicit Waits**: Wait for elements to be ready before interacting
- **Error Handling**: Handle network errors and timeouts gracefully
- **Headless Mode**: Use headless for CI/CD, headed for debugging
- **Screenshots**: Capture before/after for debugging
- **Cleanup**: Close browsers and clean up resources

