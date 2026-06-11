/**
 * Profile Loading State
 * Suspense fallback UI for profile pages
 */

import { Skeleton } from "@/components/ui/skeleton";

export default function ProfileLoading() {
  return (
    <main className="min-h-screen bg-background py-12">
      <div className="mx-auto max-w-2xl space-y-8 px-4 sm:px-6 lg:px-8">
        {/* Header skeleton */}
        <div className="space-y-4">
          <Skeleton className="h-4 w-32" />
          <Skeleton className="h-8 w-48" />
          <Skeleton className="h-4 w-64" />
        </div>

        {/* Content skeleton */}
        <div className="space-y-6 rounded-lg border border-border bg-card p-8">
          <div className="space-y-4">
            <Skeleton className="h-4 w-32" />
            <Skeleton className="h-10 w-full" />
          </div>
          <div className="space-y-4">
            <Skeleton className="h-4 w-32" />
            <Skeleton className="h-12 w-full" />
          </div>
          <div className="flex gap-4">
            <Skeleton className="h-10 flex-1" />
            <Skeleton className="h-10 w-32" />
          </div>
        </div>
      </div>
    </main>
  );
}
