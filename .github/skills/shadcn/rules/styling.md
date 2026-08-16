---
name: shadcn-styling
description: "Shadcn Styling"
version: 1.0.0
author: Alexa
---
     1|---
     2|description: Styling & customization rules for shadcn/ui components
     3|applyTo: "**/*"
     4|priority: medium
     5|canonicalSource: AGENTS.md
     6|category: development
     7|tags: [shadcn, ui, styling]
     8|date: 2026-05-17
     9|lastReviewed: 2026-05-17
    10|---
    11|
    12|# Styling & Customization
    13|
    14|See [customization.md](../customization.md) for theming, CSS variables, and adding custom colors.
    15|
    16|## Contents
    17|
    18|- Semantic colors
    19|- Built-in variants first
    20|- className for layout only
    21|- No space-x-_ / space-y-_
    22|- Prefer size-_ over w-_ h-\* when equal
    23|- Prefer truncate shorthand
    24|- No manual dark: color overrides
    25|- Use cn() for conditional classes
    26|- No manual z-index on overlay components
    27|
    28|---
    29|
    30|## Semantic colors
    31|
    32|**Incorrect:**
    33|
    34|```tsx
    35|<div className="bg-blue-500 text-white">
    36|  <p className="text-gray-600">Secondary text</p>
    37|</div>
    38|```
    39|
    40|**Correct:**
    41|
    42|```tsx
    43|<div className="bg-primary text-primary-foreground">
    44|  <p className="text-muted-foreground">Secondary text</p>
    45|</div>
    46|```
    47|
    48|---
    49|
    50|## No raw color values for status/state indicators
    51|
    52|For positive, negative, or status indicators, use Badge variants, semantic tokens like `text-destructive`, or define custom CSS variables — don't reach for raw Tailwind colors.
    53|
    54|**Incorrect:**
    55|
    56|```tsx
    57|<span className="text-emerald-600">+20.1%</span>
    58|<span className="text-green-500">Active</span>
    59|<span className="text-red-600">-3.2%</span>
    60|```
    61|
    62|**Correct:**
    63|
    64|```tsx
    65|<Badge variant="secondary">+20.1%</Badge>
    66|<Badge>Active</Badge>
    67|<span className="text-destructive">-3.2%</span>
    68|```
    69|
    70|If you need a success/positive color that doesn't exist as a semantic token, use a Badge variant or ask the user about adding a custom CSS variable to the theme (see [customization.md](../customization.md)).
    71|
    72|---
    73|
    74|## Built-in variants first
    75|
    76|**Incorrect:**
    77|
    78|```tsx
    79|<Button className="border border-input bg-transparent hover:bg-accent">
    80|  Click me
    81|</Button>
    82|```
    83|
    84|**Correct:**
    85|
    86|```tsx
    87|<Button variant="outline">Click me</Button>
    88|```
    89|
    90|---
    91|
    92|## className for layout only
    93|
    94|Use `className` for layout (e.g. `max-w-md`, `mx-auto`, `mt-4`), **not** for overriding component colors or typography. To change colors, use semantic tokens, built-in variants, or CSS variables.
    95|
    96|**Incorrect:**
    97|
    98|```tsx
    99|<Card className="bg-blue-100 text-blue-900 font-bold">
   100|  <CardContent>Dashboard</CardContent>
   101|</Card>
   102|```
   103|
   104|**Correct:**
   105|
   106|```tsx
   107|<Card className="max-w-md mx-auto">
   108|  <CardContent>Dashboard</CardContent>
   109|</Card>
   110|```
   111|
   112|To customize a component's appearance, prefer these approaches in order:
   113|
   114|1. **Built-in variants** — `variant="outline"`, `variant="destructive"`, etc.
   115|2. **Semantic color tokens** — `bg-primary`, `text-muted-foreground`.
   116|3. **CSS variables** — define custom colors in the global CSS file (see [customization.md](../customization.md)).
   117|
   118|---
   119|
   120|## No space-x-_ / space-y-_
   121|
   122|Use `gap-*` instead. `space-y-4` → `flex flex-col gap-4`. `space-x-2` → `flex gap-2`.
   123|
   124|```tsx
   125|<div className="flex flex-col gap-4">
   126|  <Input />
   127|  <Input />
   128|  <Button>Submit</Button>
   129|</div>
   130|```
   131|
   132|---
   133|
   134|## Prefer size-_ over w-_ h-\* when equal
   135|
   136|`size-10` not `w-10 h-10`. Applies to icons, avatars, skeletons, etc.
   137|
   138|---
   139|
   140|## Prefer truncate shorthand
   141|
   142|`truncate` not `overflow-hidden text-ellipsis whitespace-nowrap`.
   143|
   144|---
   145|
   146|## No manual dark: color overrides
   147|
   148|Use semantic tokens — they handle light/dark via CSS variables. `bg-background text-foreground` not `bg-white dark:bg-gray-950`.
   149|
   150|---
   151|
   152|## Use cn() for conditional classes
   153|
   154|Use the `cn()` utility from the project for conditional or merged class names. Don't write manual ternaries in className strings.
   155|
   156|**Incorrect:**
   157|
   158|```tsx
   159|<div className={`flex items-center ${isActive ? "bg-primary text-primary-foreground" : "bg-muted"}`}>
   160|```
   161|
   162|**Correct:**
   163|
   164|```tsx
   165|import { cn } from "@/lib/utils"
   166|
   167|<div className={cn("flex items-center", isActive ? "bg-primary text-primary-foreground" : "bg-muted")}>
   168|```
   169|
   170|---
   171|
   172|## No manual z-index on overlay components
   173|
   174|`Dialog`, `Sheet`, `Drawer`, `AlertDialog`, `DropdownMenu`, `Popover`, `Tooltip`, `HoverCard` handle their own stacking. Never add `z-50` or `z-[999]`.
   175|