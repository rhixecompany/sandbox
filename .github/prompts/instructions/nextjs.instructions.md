---
applyTo: "**/app/**/*.tsx,**/app/**/*.ts"
description: "Next.js App Router development guidelines for ComicWise"
---

# Next.js App Router Guidelines

Follow these guidelines when working with Next.js App Router in ComicWise.

## App Router Standards

- **Directory Structure:** Use route groups (auth), (root), admin for logical organization
- **Server Components:** Default to Server Components for better performance
- **Client Components:** Mark with "use client" directive only when interactivity is required
- **Layouts:** Share layouts appropriately using layout.tsx files
- **Loading States:** Implement loading.tsx files for better UX
- **Error Handling:** Use error.tsx files for route-level error boundaries

## Data Fetching Patterns

- **Server Side:** Fetch data directly in Server Components using async/await
- **Client Side:** Use React Query for client-side data fetching and caching
- **Static Generation:** Prefer static generation where possible
- **Dynamic Routes:** Avoid export const dynamic = 'force-dynamic' unless necessary

## Performance Guidelines

- **Runtime APIs:** Never call Date.now(), localStorage, window, document in Server Components
- **Image Optimization:** Use Next.js Image component for all images
- **Bundle Size:** Leverage optimizePackageImports in next.config.ts
- **Caching:** Respect staleTimes configuration for optimal caching strategy

## Build Configuration

- **React Compiler:** Code must be compatible with React Compiler
- **Turbopack:** Follow patterns compatible with Turbopack dev mode
- **TypeScript:** Run type generation before builds (pnpm run type-gen)
- **Static Assets:** Place static assets in /public directory with proper organization
