/**
 * Comic Details Page Loading State
 * Displays skeleton loaders while comic details are being fetched
 */

import { Skeleton } from "@/components/ui/skeleton";

export default function ComicDetailsLoading() {
  return (
    <main className="min-h-screen bg-background">
      {/* Hero Section Skeleton */}
      <div className="relative bg-linear-to-r from-muted to-muted-foreground/20 py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 gap-8 md:grid-cols-4">
            {/* Cover Image Skeleton */}
            <div className="md:col-span-1">
              <Skeleton className="aspect-2/3 w-full rounded-lg" />
            </div>

            {/* Comic Info Skeleton */}
            <div className="md:col-span-3">
              <div className="space-y-4">
                <div>
                  <Skeleton className="mb-2 h-10 w-3/4" />
                  <Skeleton className="h-6 w-full" />
                  <Skeleton className="h-6 w-5/6" />
                </div>

                {/* Author/Artist Skeleton */}
                <div className="space-y-2">
                  <Skeleton className="h-5 w-1/2" />
                  <Skeleton className="h-5 w-1/2" />
                </div>

                {/* Stats Skeleton */}
                <div className="flex flex-wrap items-center gap-4">
                  <Skeleton className="h-8 w-24" />
                  <Skeleton className="h-8 w-24" />
                  <Skeleton className="h-8 w-24" />
                </div>

                {/* Genres Skeleton */}
                <div className="flex flex-wrap gap-2">
                  {[1, 2, 3].map((i) => (
                    <Skeleton className="h-6 w-20 rounded" key={i} />
                  ))}
                </div>

                {/* Action Buttons Skeleton */}
                <div className="flex gap-3 pt-4">
                  <Skeleton className="h-11 w-40" />
                  <Skeleton className="h-11 w-40" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Chapters Section Skeleton */}
      <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="space-y-6">
          <Skeleton className="h-8 w-48" />
          <div className="space-y-3">
            {[1, 2, 3, 4, 5].map((i) => (
              <Skeleton className="h-12 w-full" key={i} />
            ))}
          </div>
        </div>
      </div>
    </main>
  );
}
