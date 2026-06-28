---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "execute-plan-comicwise-session"
title: "ComicWise Session Prompt"
description: "Execute ComicWise Session Prompt"
trigger: /execute-plan-comicwise-session
tags:
  - hermes
  - plan
  - execute
dependencies:
  - skill:plan:comicwise-session.md
---

## Goal
Execute the plan at `.hermes/plans/comicwise-session.md`.

## Execution
1. Load the plan from `.hermes/plans/comicwise-session.md`
2. Follow the plan's phases and instructions
3. Report progress and completion
