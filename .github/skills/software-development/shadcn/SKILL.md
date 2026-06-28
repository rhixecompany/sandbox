---
name: shadcn
title: shadcn/ui
description: "Use when working with shadcn/ui components — adding, searching, fixing, debugging, styling, and composing UI with preset configurations."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [ui, shadcn, components, tailwind, react]
metadata:
  hermes:
    tags: [imported]
---
# shadcn/ui

## Overview

Manage shadcn/ui components — add, search, style, compose, and debug. shadcn/ui provides a collection of beautifully designed, accessible components built on Radix UI and Tailwind CSS that can be copied into your project.

## When to Use

- Adding new shadcn/ui components to a project
- Styling or customizing existing shadcn components
- Composing shadcn components into complex UI
- Debugging component issues
- Using --preset codes for quick setup

## When NOT TO USE

- Non-shadcn UI frameworks (Material UI, Ant Design, etc.)
- Simple HTML/CSS projects
- Non-React frameworks (Vue, Angular, Svelte have their own shadcn ports)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `frontend-design` | UI/UX design patterns |
| `bun-nextjs` | Next.js setup with Bun runtime |

## Workflow

### Phase 1: Initialize shadcn

```bash
# Initialize shadcn in a new project
npx shadcn-ui@latest init

# Answer prompts:
# - Style: Default or New York
# - Base color: Slate, Gray, Zinc, Neutral, Stone, etc.
# - CSS variables: Yes (recommended)
# - Tailwind config: tailwind.config.ts
# - Components directory: @/components
# - Utility directory: @/lib/utils
# - RSC: Yes (for Next.js App Router)
# - tsx: Yes
```

### Phase 2: Add Components

```bash
# Add a specific component
npx shadcn-ui@latest add button
npx shadcn-ui@latest add card
npx shadcn-ui@latest add dialog
npx shadcn-ui@latest add form

# Add multiple at once
npx shadcn-ui@latest add button card dialog form input

# Add with --yes to skip prompts
npx shadcn-ui@latest add button --yes
```

### Phase 3: Use Components

```tsx
import { Button } from "@/components/ui/button"
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card"

export default function MyComponent() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>My Card</CardTitle>
      </CardHeader>
      <CardContent>
        <Button variant="default">Click me</Button>
        <Button variant="outline">Outline</Button>
        <Button variant="destructive">Delete</Button>
      </CardContent>
    </Card>
  )
}
```

### Phase 4: Customize

1. Edit component files directly in `components/ui/`
2. Customize the theme in `tailwind.config.ts`
3. Override CSS variables in `globals.css`
4. Use `cn()` utility for conditional classes:

```tsx
import { cn } from "@/lib/utils"

<Button className={cn(
  "w-full",
  isLoading && "opacity-50 cursor-not-allowed"
)}>
  Submit
</Button>
```

## Common Components

| Component | CLI Command | Description |
|-----------|------------|-------------|
| Button | `add button` | Button with variants |
| Card | `add card` | Card container |
| Dialog | `add dialog` | Modal dialog |
| Form | `add form` | Form with validation |
| Input | `add input` | Text input |
| Select | `add select` | Select dropdown |
| Table | `add table` | Data table |
| Tabs | `add tabs` | Tab navigation |
| Toast | `add toast` | Notifications |

## Verification Checklist

- [ ] shadcn initialized with correct style and base color
- [ ] Component added successfully
- [ ] Component imported from correct path (`@/components/ui/`)
- [ ] Tailwind classes applied correctly
- [ ] Custom styling doesn't break component defaults

## Pitfalls

- **Not running init first:** Always run `npx shadcn-ui@latest init` before adding components
- **Wrong import path:** Components import from `@/components/ui/`, not a package
- **Over-customizing base styles:** Edit components in `components/ui/` directly, don't override the theme for minor changes
- **Missing dependencies:** Some components depend on others (e.g., Form needs Label, Select)
- **Forgetting to add the cn() utility:** The `cn()` function from `@/lib/utils` is essential for conditional classes
