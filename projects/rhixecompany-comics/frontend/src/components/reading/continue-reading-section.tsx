/**
 * Continue Reading Section Component
 * Server component that fetches and displays reading progress
 *
 * Features:
 * - Displays user's continue reading list
 * - Shows reading statistics
 * - Auto-revalidates every hour
 */

import { Suspense } from "react";

import { getContinueReadingAction } from "@/actions/reading-progress.actions";
import { auth } from "@/auth";
import { ContinueReadingCard } from "@/components/reading/continue-reading-card";

interface ContinueReadingSectionProps {
  limit?: number;
}

async function ContinueReadingContent({ limit = 6 }: ContinueReadingSectionProps) {
  const session = await auth();

  if (!session?.user?.id) {
    return (
      <div className="py-8 text-center">
        <p className="mb-4 text-gray-600">Sign in to track your reading progress</p>
        <a
          className="inline-block rounded-lg bg-blue-600 px-6 py-2 text-white transition-colors hover:bg-blue-700"
          href="/auth/signin"
        >
          Sign In
        </a>
      </div>
    );
  }

  const itemsResult = await getContinueReadingAction(limit);

  const items = itemsResult.ok ? itemsResult.data : [];

  return (
    <div className="space-y-6">
      {/* Continue Reading List */}
      <div>
        <h2 className="mb-4 text-lg font-semibold text-gray-900">Continue Reading</h2>

        {items.length === 0 ? (
          <div className="rounded-lg border bg-gray-50 py-8 text-center">
            <p className="text-gray-600">No reading history yet</p>
            <p className="mt-2 text-sm text-gray-500">Start reading a comic to track your progress</p>
          </div>
        ) : (
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            {items.map((item) => (
              <ContinueReadingCard item={item} key={`${item.comicId}-${item.chapterId}`} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export function ContinueReadingSection({ limit = 6 }: ContinueReadingSectionProps) {
  return (
    <Suspense
      fallback={
        <div className="space-y-4">
          <div className="h-40 animate-pulse rounded-lg bg-gray-200" />
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            {Array.from({ length: 4 }).map((_, i) => (
              <div className="h-40 animate-pulse rounded-lg bg-gray-200" key={i} />
            ))}
          </div>
        </div>
      }
    >
      <ContinueReadingContent limit={limit} />
    </Suspense>
  );
}
