---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "Dataverse Python Quickstart Generator"
title: "Dataverse Python Quickstart Generator"
description: "Generate Python SDK setup + CRUD + bulk + paging snippets using official patterns."
trigger: dataverse-python-quickstart-generator
tags:
  - audit
  - data
  - frontend
  - generator
  - prompts
  - python
  - typescript
  - hermes
  - codegen
  - python
  - dataverse
metadata:
  hermes:
    related_skills: []
    tags:
    - dataverse-python-quickstart.prompt

---
metadata:
  hermes:
    related_skills: []
    tags:
    - dataverse-python-quickstart.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - dataverse-python-quickstart.prompt

You are assisting with Microsoft Dataverse SDK for Python (preview). Generate concise Python snippets that:

- Install the SDK (pip install PowerPlatform-Dataverse-Client)
- Create a DataverseClient with InteractiveBrowserCredential
- Show CRUD single-record operations
- Show bulk create and bulk update (broadcast + 1:1)
- Show retrieve-multiple with paging (top, page_size)
- Optionally demonstrate file upload to a File column Keep code aligned with official examples and avoid unannounced preview features.

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
