---
description: "Design System patterns, theme management, and component refinement guidelines for Phase 4"
applyTo: "src/components/**/*.{ts,tsx}, src/styles/**/*.css"
---

# Design System & UI Component Guidelines (Phase 4)

Comprehensive guide for building consistent, accessible, and performant UI components across ComicWise using shadcn/ui, Radix UI, and Tailwind CSS v4.

---

## Design System Principles

### 1. Component-First Architecture

- **Atomic Design**: Build from atoms (Button) → molecules (ButtonGroup) → organisms (Header)
- **Single Responsibility**: Each component does one thing well
- **Composition**: Combine simple components to create complex UIs
- **Props API**: Make components flexible through well-designed props

### 2. Theme System

All theming flows through the theme provider:

```tsx
// Root layout
import { ThemeProvider } from "@/components/theme/theme-provider";

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <ThemeProvider defaultTheme="system" storageKey="app-theme">
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
```

**Theme Modes**:

- `light` — Light color scheme
- `dark` — Dark color scheme
- `system` — Follow OS preference

**Color Palette** (Tailwind CSS v4):

```css
/* Light theme */
:root {
  --background: 0 0% 100%;
  --foreground: 0 0% 3.6%;
  --primary: 0 0% 9%;
  --primary-foreground: 0 0% 98%;
  --secondary: 0 0% 96.1%;
  --secondary-foreground: 0 0% 9%;
  --accent: 0 84.2% 60.2%;
  --muted: 0 0% 96.1%;
  --muted-foreground: 0 0% 45.1%;
  --border: 0 0% 89.8%;
}

/* Dark theme */
@media (prefers-color-scheme: dark) {
  :root {
    --background: 0 0% 3.6%;
    --foreground: 0 0% 98%;
    --primary: 0 0% 98%;
    --primary-foreground: 0 0% 9%;
    --secondary: 0 0% 14.9%;
    --secondary-foreground: 0 0% 98%;
    --accent: 0 84.2% 60.2%;
    --muted: 0 0% 14.9%;
    --muted-foreground: 0 0% 63.9%;
    --border: 0 0% 14.9%;
  }
}
```

### 3. Tailwind CSS v4 Conventions

**Color Usage**:

```tsx
// ✅ GOOD: Use CSS variables
<div className="bg-background text-foreground border-border">

// ✅ GOOD: Use semantic Tailwind utilities
<button className="bg-primary text-primary-foreground hover:bg-primary/90">

// ✅ GOOD: Dark mode variants
<div className="bg-white dark:bg-slate-950">

// ❌ BAD: Hardcoded colors (not themeable)
<div className="bg-blue-500 dark:bg-blue-800">
```

**Spacing Scale** (4px base):

```
0: 0px
1: 4px
2: 8px
3: 12px
4: 16px
5: 20px
6: 24px
...
```

**Typography Scale**:

```
text-xs: 12px / 16px
text-sm: 14px / 20px
text-base: 16px / 24px
text-lg: 18px / 28px
text-xl: 20px / 28px
text-2xl: 24px / 32px
```

---

## Component Patterns

### Pattern 1: Server Component with Client Interactivity

```tsx
// src/components/comics/comic-detail.tsx (Server Component)
import { ComicDetailClient } from "./comic-detail-client";
import { comicDal } from "@/dal/comic-dal";

interface ComicDetailProps {
  slug: string;
}

export async function ComicDetail({ slug }: ComicDetailProps) {
  // Fetch data server-side
  const comic = await comicDal.getBySlug(slug);
  if (!comic) return notFound();

  return (
    <ComicDetailClient
      initialComic={comic}
      // Pass serialized data to client component
    />
  );
}
```

```tsx
// src/components/comics/comic-detail-client.tsx (Client Component)
"use client";

import { useState } from "react";
import { BookmarkButton } from "./bookmark-button";

interface ComicDetailClientProps {
  initialComic: Comic;
}

export function ComicDetailClient({
  initialComic
}: ComicDetailClientProps) {
  const [bookmarked, setBookmarked] = useState(false);

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold">{initialComic.title}</h1>
      <BookmarkButton
        comicId={initialComic.id}
        onBookmarkChange={setBookmarked}
      />
    </div>
  );
}
```

**Benefits**:

- Fetch data server-side (faster)
- Reduce JavaScript bundle
- Keep secrets on server
- Use client features only where needed

### Pattern 2: Loading States with Suspense

```tsx
// Show skeleton while component loads
import { Suspense } from "react";

export function ComicList() {
  return (
    <Suspense fallback={<ComicListSkeleton />}>
      <ComicListContent />
    </Suspense>
  );
}

async function ComicListContent() {
  const comics = await comicDal.list();
  return <div>{/* render comics */}</div>;
}

function ComicListSkeleton() {
  return (
    <div className="grid grid-cols-1 gap-4 md:grid-cols-3 lg:grid-cols-6 animate-pulse">
      {[...Array(6)].map((_, i) => (
        <div key={i} className="bg-muted aspect-2/3 rounded-lg" />
      ))}
    </div>
  );
}
```

### Pattern 3: Empty & Error States

```tsx
// src/components/ui/empty-state.tsx
import { LucideIcon } from "lucide-react";
import { Button } from "./button";

interface EmptyStateProps {
  action?: React.ReactNode;
  description?: string;
  icon: LucideIcon;
  title: string;
}

export function EmptyState({
  icon: Icon,
  title,
  description,
  action
}: EmptyStateProps) {
  return (
    <div className="flex flex-col items-center justify-center gap-4 py-12">
      <Icon className="h-12 w-12 text-muted-foreground" />
      <div className="text-center space-y-2">
        <h3 className="text-lg font-semibold">{title}</h3>
        {description && (
          <p className="text-muted-foreground">{description}</p>
        )}
      </div>
      {action && <div>{action}</div>}
    </div>
  );
}
```

**Usage**:

```tsx
// src/app/(root)/bookmarks/page.tsx
if (bookmarks.length === 0) {
  return (
    <EmptyState
      icon={BookmarkIcon}
      title="No bookmarks yet"
      description="Start by saving your favorite comics"
      action={<Button href="/browse">Browse Comics</Button>}
    />
  );
}
```

### Pattern 4: Responsive Layout

```tsx
// Mobile-first approach
<div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
  {/* Mobile: 1 column, Tablet: 2 columns, Desktop: 4 columns */}
</div>

// Hide/show based on screen size
<nav className="hidden lg:block">
  {/* Desktop navigation */}
</nav>
<button className="lg:hidden">
  {/* Mobile menu toggle */}
</button>
```

**Breakpoints** (Tailwind default):

- `sm` — 640px (tablets)
- `md` — 768px (larger tablets)
- `lg` — 1024px (desktops)
- `xl` — 1280px (large desktops)
- `2xl` — 1536px (x-large)

### Pattern 5: Accessible Components

```tsx
// ✅ GOOD: Semantic HTML + ARIA
<button
  aria-label="Add to bookmarks"
  className="rounded-lg p-2 hover:bg-muted"
  onClick={handleBookmark}
  title="Save this comic to your library"
>
  <Heart className="h-5 w-5" />
</button>

// ✅ GOOD: Focus management
<Dialog onOpenChange={setOpen} open={isOpen}>
  <DialogTrigger asChild>
    <Button>Open Settings</Button>
  </DialogTrigger>
  <DialogContent>
    {/* Focus will move here when dialog opens */}
  </DialogContent>
</Dialog>

// ❌ BAD: Non-semantic, no a11y
<div onClick={handleBookmark}>
  <img alt="" src="/heart.svg" />
</div>
```

**Accessibility Checklist**:

- [ ] Semantic HTML (`<button>`, `<nav>`, `<header>`, etc.)
- [ ] ARIA labels for icon-only buttons
- [ ] Color isn't the only indicator (add icons, text)
- [ ] Form labels and error messages associated
- [ ] Keyboard navigation works (Tab, Enter, Escape)
- [ ] Focus states visible and logical
- [ ] Screen reader testing done
- [ ] 4.5:1 contrast ratio on text

---

## Tailwind CSS v4 Syntax

**Key changes from v3**:

```tailwind
/* v3: OLD */
bg-gradient-to-br from-blue-500 to-purple-600
aspect-[16/9]
!h-10

/* v4: NEW */
bg-linear-to-br from-blue-500 to-purple-600
aspect-16/9
h-10!
```

**Common utilities**:

```tsx
// Colors
className = "bg-primary text-foreground border-border";

// Spacing
className = "p-4 m-2 px-6 py-3";

// Layout
className = "flex items-center justify-between gap-4";
className = "grid grid-cols-1 md:grid-cols-3 gap-4";

// Typography
className = "text-lg font-semibold leading-tight";

// Effects
className = "shadow-lg rounded-lg hover:shadow-xl";
className = "transition-all duration-200 ease-out";

// Responsive
className = "hidden md:block lg:flex";
className = "w-full sm:w-1/2 lg:w-1/4";

// Dark mode
className = "bg-white dark:bg-slate-950";
className = "text-black dark:text-white";

// States
className = "hover:bg-primary/90 focus:outline-none";
className = "disabled:opacity-50 disabled:cursor-not-allowed";
className = "group hover:bg-muted group-hover:text-primary";
```

---

## Component Refinement Checklist

For each component, verify:

### Design

- [ ] Consistent with design system
- [ ] Matches color palette
- [ ] Proper spacing and alignment
- [ ] Typography hierarchy correct
- [ ] Dark mode variants implemented
- [ ] Responsive on all breakpoints

### Functionality

- [ ] Props are flexible and composable
- [ ] Default props sensible
- [ ] Handles loading states
- [ ] Handles error states
- [ ] Handles empty states

### Accessibility

- [ ] Semantic HTML used
- [ ] ARIA labels where needed
- [ ] Keyboard navigation works
- [ ] Focus states visible
- [ ] Color contrast 4.5:1+
- [ ] Screen reader tested

### Performance

- [ ] No unnecessary re-renders
- [ ] Images optimized (use `next/image`)
- [ ] No large bundles
- [ ] Lazy load if appropriate
- [ ] Lighthouse score 85+

### Code Quality

- [ ] TypeScript types correct
- [ ] No `any` types
- [ ] ESLint passing
- [ ] Consistent formatting
- [ ] JSDoc comments present

---

## Dark Mode Implementation

**In component**:

```tsx
export function ComicCard({ comic }: ComicCardProps) {
  return (
    <div className="rounded-lg border border-border bg-white dark:bg-slate-900 p-4">
      {/* Card content */}
    </div>
  );
}
```

**In CSS** (if needed):

```css
@media (prefers-color-scheme: dark) {
  .custom-element {
    background-color: var(--background);
    color: var(--foreground);
  }
}
```

**Testing dark mode**:

1. Browser DevTools > Rendering > Emulate CSS media feature prefers-color-scheme
2. Or toggle theme widget in UI
3. Verify all colors readable
4. Check for "dark mode" specific classes

---

## Theme Provider Implementation

**File: `src/components/theme/theme-provider.tsx`**

```tsx
"use client";

import {
  createContext,
  useContext,
  useEffect,
  useState
} from "react";

export type Theme = "dark" | "light" | "system";

interface ThemeContextType {
  theme: Theme;
  setTheme: (theme: Theme) => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(
  undefined
);

interface ThemeProviderProps {
  children: React.ReactNode;
  defaultTheme?: Theme;
  storageKey?: string;
}

export function ThemeProvider({
  children,
  defaultTheme = "system",
  storageKey = "theme"
}: ThemeProviderProps) {
  const [theme, setThemeState] = useState<Theme>(defaultTheme);
  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    setIsMounted(true);
    // Load from localStorage
    const stored = localStorage.getItem(storageKey) as Theme | null;
    if (stored) {
      setThemeState(stored);
    }
  }, [storageKey]);

  useEffect(() => {
    if (!isMounted) return;

    const root = document.documentElement;

    if (theme === "system") {
      const systemTheme = window.matchMedia(
        "(prefers-color-scheme: dark)"
      ).matches
        ? "dark"
        : "light";
      root.classList.toggle("dark", systemTheme === "dark");
    } else {
      root.classList.toggle("dark", theme === "dark");
    }

    localStorage.setItem(storageKey, theme);
  }, [theme, isMounted, storageKey]);

  const setTheme = (newTheme: Theme) => {
    setThemeState(newTheme);
  };

  if (!isMounted) {
    return <>{children}</>;
  }

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error("useTheme must be used within ThemeProvider");
  }
  return context;
}
```

---

## Performance Optimization

### Image Optimization

```tsx
// ✅ GOOD: Use next/image with proper sizes
import Image from 'next/image';

<Image
  alt="Comic cover"
  className="rounded-lg"
  height={300}
  priority // For above-the-fold images
  sizes="(max-width: 640px) 100vw, 50vw"
  src={comic.coverImage}
  width={200}
/>

// ❌ BAD: Native img tag (no optimization)
<img alt="Comic cover" src={comic.coverImage} />
```

### Code Splitting

```tsx
// ✅ GOOD: Lazy load heavy components
import dynamic from "next/dynamic";

const ReaderComponent = dynamic(
  () => import("@/components/reader/reader"),
  { loading: () => <ReaderSkeleton /> }
);

// ❌ BAD: Load everything upfront
import { ReaderComponent } from "@/components/reader/reader";
```

### Memoization

```tsx
// ✅ GOOD: Memoize expensive components (React Compiler handles this)
function ComicCard({ comic }: ComicCardProps) {
  // If using React Compiler, no need for manual memo()
  return <div>{/* ... */}</div>;
}

// ❌ BAD: Manual memoization defeats React Compiler optimization
export const ComicCard = memo(function ComicCard({
  comic
}: ComicCardProps) {
  return <div>{/* ... */}</div>;
});
```

---

## Common Patterns Reference

| Pattern | Location | Use Case |
| --- | --- | --- |
| Card | `src/components/ui/card.tsx` | Content containers |
| Button | `src/components/ui/button.tsx` | Actions |
| Dialog | `src/components/ui/dialog.tsx` | Modals |
| Loading Skeleton | `src/components/states/loading-skeleton.tsx` | Async content |
| Empty State | `src/components/states/empty-state.tsx` | No data scenario |
| Error Boundary | `src/components/errors/error-boundary.tsx` | Error handling |

---

## Design System Validation

Before merging component changes:

```bash
# Type safety
pnpm type-check

# Linting & formatting
pnpm lint:fix

# Accessibility check
# Use axe DevTools browser extension or:
npm install --save-dev @axe-core/cli
npx axe http://localhost:3000/path-to-test

# Lighthouse audit
pnpm build:analyze  # Includes Lighthouse data

# Visual regression
# Use playwright visual comparisons or manual review
```

---

## References

- **Tailwind CSS v4**: https://tailwindcss.com/docs
- **shadcn/ui**: https://ui.shadcn.com
- **Radix UI**: https://www.radix-ui.com
- **WCAG 2.1 AA**: https://www.w3.org/WAI/WCAG21/quickref/
- **Accessible Components**: https://www.a11y-101.com/
