/**
 * Edit Profile Loading State
 * Suspense fallback UI for edit profile page
 */

import { Skeleton } from "@/components/ui/skeleton";

export default function EditProfileLoading() {
  return (
    <main className="min-h-screen bg-background py-12">
      <div className="mx-auto max-w-2xl space-y-8 px-4 sm:px-6 lg:px-8">
        {/* Header skeleton */}
        <div className="space-y-4">
          <Skeleton className="h-4 w-32" />
          <Skeleton className="h-8 w-48" />
          <Skeleton className="h-4 w-64" />
        </div>

        {/* Form skeleton */}
        <div className="space-y-6 rounded-lg border border-border bg-card p-8">
          {[1, 2, 3].map((i) => (
            <div className="space-y-2" key={i}>
              <Skeleton className="h-4 w-24" />
              <Skeleton className="h-10 w-full" />
            </div>
          ))}
          <div className="flex gap-4 pt-4">
            <Skeleton className="h-10 flex-1" />
            <Skeleton className="h-10 w-24" />
          </div>
        </div>
      </div>
    </main>
  );
}
