---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Migrate To Next16
name: migrate-to-next16
agent: "Next.js Expert"
model: GPT-4.1 (copilot)
tools:
  [
    vscode,
    execute,
    read,
    agent,
    edit,
    search,
    web,
    "github/*",
    browser,
    "io.github.upstash/context7/*",
    "io.github.vercel/next-devtools-mcp/*",
    vscode.mermaid-chat-features/renderMermaidDiagram,
    github.vscode-pull-request-github/issue_fetch,
    github.vscode-pull-request-github/labels_fetch,
    github.vscode-pull-request-github/notification_fetch,
    github.vscode-pull-request-github/doSearch,
    github.vscode-pull-request-github/activePullRequest,
    github.vscode-pull-request-github/pullRequestStatusChecks,
    github.vscode-pull-request-github/openPullRequest,
    todo
  ]
description: "Automate Next.js 16 migration tasks"
---

Your goal is to automate migration to Next.js 16, including codemod, breaking changes, and validation.

Requirements:

- Run codemod for Next.js/React upgrades
- Update config and API usage
- Validate build, lint, and tests
- Document migration steps and issues
