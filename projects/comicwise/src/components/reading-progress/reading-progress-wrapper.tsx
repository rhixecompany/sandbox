"use client";

import { Suspense } from "react";

import { ContinueReadingSection } from "@/components/reading/continue-reading-section";

export function ReadingProgressWrapper() {
  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <div className="border-b bg-white">
        <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
          <h1 className="mb-2 text-4xl font-bold">Continue Reading</h1>
          <p className="text-muted-foreground">Your reading history and bookmarks</p>
        </div>
      </div>

      {/* Content */}
      <div className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        {/* Continue Reading List */}
        <div className="space-y-6">
          <h2 className="text-2xl font-bold">Your Reading History</h2>
          <Suspense
            fallback={
              <div className="space-y-4">
                <div className="h-32 animate-pulse rounded bg-muted" />
              </div>
            }
          >
            <ContinueReadingSection />
          </Suspense>
        </div>
      </div>
    </main>
  );
}
