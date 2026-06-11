/**
 * Comics Page Loading State
 * Displays skeleton loaders while comics are being fetched
 */

import { Skeleton } from "@/components/ui/skeleton";

export default function ComicsLoading() {
  return (
    <main className="min-h-screen bg-background">
      {/* Header Skeleton */}
      <div className="border-b bg-white">
        <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
          <Skeleton className="mb-4 h-10 w-48" />
          <Skeleton className="h-6 w-96" />
        </div>
      </div>

      {/* Main Content */}
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 gap-8 lg:grid-cols-4">
          {/* Sidebar Skeletons */}
          <div className="lg:col-span-1">
            <div className="sticky top-4 space-y-6">
              {/* Search Skeleton */}
              <div>
                <Skeleton className="mb-2 h-5 w-16" />
                <Skeleton className="h-10 w-full" />
              </div>

              {/* Sort Skeleton */}
              <div>
                <Skeleton className="mb-2 h-5 w-12" />
                <div className="space-y-2">
                  {[1, 2, 3].map((i) => (
                    <Skeleton className="h-8 w-full" key={i} />
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Grid Skeletons */}
          <div className="lg:col-span-3">
            <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
              {[1, 2, 3, 4, 5, 6].map((i) => (
                <div className="space-y-3" key={i}>
                  <Skeleton className="aspect-2/3 w-full rounded-lg" />
                  <Skeleton className="h-5 w-full" />
                  <Skeleton className="h-4 w-3/4" />
                  <div className="flex gap-2">
                    <Skeleton className="h-4 w-12" />
                    <Skeleton className="h-4 w-16" />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
