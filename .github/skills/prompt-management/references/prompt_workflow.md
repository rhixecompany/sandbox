# Prompt Workflow Reference

## Overview
This document describes the three-phase lifecycle of a prompt in the `prompt-management` skill.

---

## Phase 1 – Create Prompt (Interactive)

```mermaid
flowchart TD
    A[Start] --> B[hermes profile use <profile>]
    B --> C[Load prompt_template.md]
    C --> D[Ask user for each component]
    D --> E[Write prompts/<name>.md]
    E --> F[Write scripts/<name>.<ext> if needed]
    F --> G[Write profiles/<name>.yaml if needed]
    G --> H[Add front‑matter references]
    H --> I[Verify with read_file]
    I --> J[git add / commit]
    J --> K[Done]
```

**Interactive questions** (prompted to user):
1. Prompt name & brief description
2. Desired model / provider
3. Required toolsets
4. Personality / tone
5. High‑level success criteria

---

## Phase 2 – Update Prompt

```mermaid
flowchart TD
    A[Start] --> B[read_file prompt markdown]
    B --> C[read_file all linked files]
    C --> D[Extract components]
    D --> E[Ask clarifying questions]
    E --> F[Apply changes with patch / write_file]
    F --> G[Run Verification Checklist]
    G --> H[git commit]
    H --> I[Done]
```

---

## Phase 3 – Execute Prompt

```mermaid
flowchart TD
    A[Start] --> B[Gather full context]
    B --> C[Spawn sub‑agent via delegate_task]
    C --> D[Monitor with process wait]
    D --> E[Collect output]
    E --> F[Store in results/<name>.md]
    F --> G[Report success / errors]
    G --> H[Done]
```

---

## Integration Points
- `templates/prompt_template.md` – main skeleton
- `templates/plans_and_specs_template.md` – for Plans‑and‑Specs section
- `templates/script_template.md` – for Scripts section
- `templates/persona_template.md` – for Personas section
- `templates/profile_template.md` – for Profile section
- `references/prompt_library_integration.md` – library reuse guide