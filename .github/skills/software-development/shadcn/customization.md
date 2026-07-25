---
name: shadcn-customization
description: "Customization & Theming"
version: 1.0.0
author: Alexa
---
     1|# Customization & Theming
     2|
     3|Components reference semantic CSS variable tokens. Change the variables to change every component.
     4|
     5|## Contents
     6|
     7|- How it works (CSS variables → Tailwind utilities → components)
     8|- Color variables and OKLCH format
     9|- Dark mode setup
    10|- Changing the theme (presets, CSS variables)
    11|- Adding custom colors (Tailwind v3 and v4)
    12|- Border radius
    13|- Customizing components (variants, className, wrappers)
    14|- Checking for updates
    15|
    16|---
    17|
    18|## How It Works
    19|
    20|1. CSS variables defined in `:root` (light) and `.dark` (dark mode).
    21|2. Tailwind maps them to utilities: `bg-primary`, `text-muted-foreground`, etc.
    22|3. Components use these utilities — changing a variable changes all components that reference it.
    23|
    24|---
    25|
    26|## Color Variables
    27|
    28|Every color follows the `name` / `name-foreground` convention. The base variable is for backgrounds, `-foreground` is for text/icons on that background.
    29|
    30|| Variable | Purpose |
    31|| --- | --- |
    32|| `--background` / `--foreground` | Page background and default text |
    33|| `--card` / `--card-foreground` | Card surfaces |
    34|| `--primary` / `--primary-foreground` | Primary buttons and actions |
    35|| `--secondary` / `--secondary-foreground` | Secondary actions |
    36|| `--muted` / `--muted-foreground` | Muted/disabled states |
    37|| `--accent` / `--accent-foreground` | Hover and accent states |
    38|| `--destructive` / `--destructive-foreground` | Error and destructive actions |
    39|| `--border` | Default border color |
    40|| `--input` | Form input borders |
    41|| `--ring` | Focus ring color |
    42|| `--chart-1` through `--chart-5` | Chart/data visualization |
    43|| `--sidebar-*` | Sidebar-specific colors |
    44|| `--surface` / `--surface-foreground` | Secondary surface |
    45|
    46|Colors use OKLCH: `--primary: oklch(0.205 0 0)` where values are lightness (0–1), chroma (0 = gray), and hue (0–360).
    47|
    48|---
    49|
    50|## Dark Mode
    51|
    52|Class-based toggle via `.dark` on the root element. In Next.js, use `next-themes`:
    53|
    54|```tsx
    55|import { ThemeProvider } from "next-themes";
    56|
    57|<ThemeProvider attribute="class" defaultTheme="system" enableSystem>
    58|  {children}
    59|</ThemeProvider>;
    60|```
    61|
    62|---
    63|
    64|## Changing the Theme
    65|
    66|```bash
    67|# Apply a preset code from ui.shadcn.com.
    68|npx shadcn@latest init --preset a2r6bw --force
    69|
    70|# Switch to a named preset.
    71|npx shadcn@latest init --preset radix-nova --force
    72|npx shadcn@latest init --reinstall  # update existing components to match
    73|
    74|# Use a custom theme URL.
    75|npx shadcn@latest init --preset "https://ui.shadcn.com/init?base=radix&style=nova&theme=blue&..." --force
    76|```
    77|
    78|Or edit CSS variables directly in `globals.css`.
    79|
    80|---
    81|
    82|## Adding Custom Colors
    83|
    84|Add variables to the file at `tailwindCssFile` from `npx shadcn@latest info` (typically `globals.css`). Never create a new CSS file for this.
    85|
    86|```css
    87|/* 1. Define in the global CSS file. */
    88|:root {
    89|  --warning: oklch(0.84 0.16 84);
    90|  --warning-foreground: oklch(0.28 0.07 46);
    91|}
    92|.dark {
    93|  --warning: oklch(0.41 0.11 46);
    94|  --warning-foreground: oklch(0.99 0.02 95);
    95|}
    96|```
    97|
    98|```css
    99|/* 2a. Register with Tailwind v4 (@theme inline). */
   100|@theme inline {
   101|  --color-warning: var(--warning);
   102|  --color-warning-foreground: var(--warning-foreground);
   103|}
   104|```
   105|
   106|When `tailwindVersion` is `"v3"` (check via `npx shadcn@latest info`), register in `tailwind.config.js` instead:
   107|
   108|```js
   109|// 2b. Register with Tailwind v3 (tailwind.config.js).
   110|module.exports = {
   111|  theme: {
   112|    extend: {
   113|      colors: {
   114|        warning: "oklch(var(--warning) / <alpha-value>)",
   115|        "warning-foreground":
   116|          "oklch(var(--warning-foreground) / <alpha-value>)"
   117|      }
   118|    }
   119|  }
   120|};
   121|```
   122|
   123|```tsx
   124|// 3. Use in components.
   125|<div className="bg-warning text-warning-foreground">Warning</div>
   126|```
   127|
   128|---
   129|
   130|## Border Radius
   131|
   132|`--radius` controls border radius globally. Components derive values from it (`rounded-lg` = `var(--radius)`, `rounded-md` = `calc(var(--radius) - 2px)`).
   133|
   134|---
   135|
   136|## Customizing Components
   137|
   138|See also: [rules/styling.md](./rules/styling.md) for Incorrect/Correct examples.
   139|
   140|Prefer these approaches in order:
   141|
   142|### 1. Built-in variants
   143|
   144|```tsx
   145|<Button variant="outline" size="sm">
   146|  Click
   147|</Button>
   148|```
   149|
   150|### 2. Tailwind classes via `className`
   151|
   152|```tsx
   153|<Card className="max-w-md mx-auto">...</Card>
   154|```
   155|
   156|### 3. Add a new variant
   157|
   158|Edit the component source to add a variant via `cva`:
   159|
   160|```tsx
   161|// components/ui/button.tsx
   162|warning: "bg-warning text-warning-foreground hover:bg-warning/90",
   163|```
   164|
   165|### 4. Wrapper components
   166|
   167|Compose shadcn/ui primitives into higher-level components:
   168|
   169|```tsx
   170|export function ConfirmDialog({
   171|  title,
   172|  description,
   173|  onConfirm,
   174|  children
   175|}) {
   176|  return (
   177|    <AlertDialog>
   178|      <AlertDialogTrigger asChild>{children}</AlertDialogTrigger>
   179|      <AlertDialogContent>
   180|        <AlertDialogHeader>
   181|          <AlertDialogTitle>{title}</AlertDialogTitle>
   182|          <AlertDialogDescription>
   183|            {description}
   184|          </AlertDialogDescription>
   185|        </AlertDialogHeader>
   186|        <AlertDialogFooter>
   187|          <AlertDialogCancel>Cancel</AlertDialogCancel>
   188|          <AlertDialogAction onClick={onConfirm}>
   189|            Confirm
   190|          </AlertDialogAction>
   191|        </AlertDialogFooter>
   192|      </AlertDialogContent>
   193|    </AlertDialog>
   194|  );
   195|}
   196|```
   197|
   198|---
   199|
   200|## Checking for Updates
   201|
   202|```bash
   203|npx shadcn@latest add button --diff
   204|```
   205|
   206|To preview exactly what would change before updating, use `--dry-run` and `--diff`:
   207|
   208|```bash
   209|npx shadcn@latest add button --dry-run        # see all affected files
   210|npx shadcn@latest add button --diff button.tsx # see the diff for a specific file
   211|```
   212|
   213|See [Updating Components in SKILL.md](./SKILL.md#updating-components) for the full smart merge workflow.
   214|