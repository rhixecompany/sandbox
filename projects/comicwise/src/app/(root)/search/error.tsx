"use client";

export default function SearchError({ reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return (
    <div className="min-h-screen bg-linear-to-br from-gray-50 to-white dark:bg-linear-to-br dark:from-background dark:to-background/95">
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <div className="mb-8">
          <h1 className="mb-2 text-4xl font-bold dark:text-foreground">Advanced Search</h1>
          <p className="text-lg text-red-600 dark:text-red-400">Failed to load search filters. Please try again.</p>
          <button className="mt-4 rounded bg-primary px-4 py-2 text-white hover:bg-primary/90" onClick={reset}>
            Retry
          </button>
        </div>
      </div>
    </div>
  );
}
