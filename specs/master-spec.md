---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---



## Goal

Master specification that couples all plan files in `./plans/` for cross-validation. Every plan references this spec, and this spec references every plan back.

## Linked Plans


## Acceptance Criteria

- All 51 plans have complete frontmatter (7 fields)
- All plans have >=3 Phase sections with **Gate** markers
- All plans reference this spec via `## Linked Specs`
- This spec references all plans via `## Linked Plan`
- All plans pass plans-judge score >=99
