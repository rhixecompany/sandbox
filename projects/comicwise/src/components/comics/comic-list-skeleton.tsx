/**
 * Comic List Skeleton (Loading State)
 * Suspense boundary fallback for comic grid
 */

export function ComicListSkeleton() {
  return (
    <div className="lg:col-span-3">
      <div className="grid grid-cols-2 gap-6 sm:grid-cols-3">
        {Array.from({ length: 12 }).map((_, i) => (
          <div className="space-y-2" key={i}>
            {/* Image skeleton */}
            <div className="aspect-2/3 w-full animate-pulse rounded-lg bg-muted" />
            {/* Title skeleton */}
            <div className="h-4 animate-pulse rounded bg-muted" />
            {/* Subtitle skeleton */}
            <div className="h-3 w-2/3 animate-pulse rounded bg-muted" />
          </div>
        ))}
      </div>
    </div>
  );
}
