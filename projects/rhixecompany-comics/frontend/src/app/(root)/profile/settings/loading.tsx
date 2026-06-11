/**
 * Settings Page Loading State
 * Suspense fallback UI for settings page
 */

import { Skeleton } from "@/components/ui/skeleton";

export default function SettingsPageLoading() {
  return (
    <main className="min-h-screen bg-background py-12">
      <div className="mx-auto max-w-4xl space-y-8 px-4 sm:px-6 lg:px-8">
        {/* Header skeleton */}
        <div className="space-y-4">
          <Skeleton className="h-4 w-32" />
          <Skeleton className="h-8 w-48" />
          <Skeleton className="h-4 w-64" />
        </div>

        {/* Settings sections skeleton */}
        <div className="space-y-6">
          {[1, 2, 3].map((i) => (
            <div className="space-y-4 rounded-lg border border-border bg-card p-6" key={i}>
              <div className="space-y-2">
                <Skeleton className="h-6 w-32" />
                <Skeleton className="h-4 w-48" />
              </div>
              <div className="space-y-3">
                {[1, 2].map((j) => (
                  <div className="flex items-center justify-between" key={j}>
                    <div className="flex-1 space-y-2">
                      <Skeleton className="h-4 w-24" />
                      <Skeleton className="h-3 w-40" />
                    </div>
                    <Skeleton className="h-6 w-10" />
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
