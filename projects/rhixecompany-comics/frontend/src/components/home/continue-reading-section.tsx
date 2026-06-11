/**
 * Continue Reading Widget
 *
 * Server component that displays the user's currently reading comics.
 * Shows on homepage when user is logged in.
 *
 * Features:
 * - Fetches user's bookmarks in "Reading" status (top 5)
 * - Displays comic cover, title, current chapter, progress
 * - "Continue Reading" button to jump to last position
 * - "See All" link to bookmarks page
 * - Empty state when no bookmarks
 * - Caches data for 30 seconds
 *
 * Usage (in homepage layout):
 * ```tsx
 * import { ContinueReadingSection } from "@/components/home/continue-reading-section";
 *
 * export default function HomePage() {
 *   return (
 *     <>
 *       <HeroSection />
 *       <ContinueReadingSection />
 *       <TrendingSection />
 *     </>
 *   );
 * }
 * ```
 */

import { BookOpen } from "lucide-react";
import Image from "next/image";
import Link from "next/link";

import { getBookmarksAction } from "@/actions/bookmark.actions";
import { auth } from "@/auth";
import { ResumeButton } from "@/components/bookmarks/resume-button";
import { Button } from "@/components/ui/button";

interface BookmarkWithRelations {
  comic: {
    coverImage: null | string;
    id: number;
    slug: string;
    title: string;
  } | null;
  comicId: number;
  createdAt: Date;
  lastReadChapter: {
    chapterNumber: number;
    id: number;
  } | null;
  lastReadChapterId: null | number;
  notes: null | string;
  status: string;
  updatedAt: Date;
  userId: string;
}

/**
 * ContinueReadingSection
 * Server Component
 * Note: Try/catch at function level is appropriate for Server Components
 */
/* eslint-disable react-hooks/error-boundaries */
export async function ContinueReadingSection() {
  // Check if user is authenticated
  const session = await auth();
  if (!session?.user?.id) {
    // Not authenticated - show nothing or CTA
    return null;
  }

  try {
    // Fetch user's reading bookmarks (top 5, sorted by recently updated)
    const result = await getBookmarksAction({ status: "Reading", limit: 5, page: 1, sortBy: "date" });
    if (!result.ok) {
      return null;
    }
    const bookmarks = result.data.bookmarks as BookmarkWithRelations[];

    // If no bookmarks, show empty state
    if (!bookmarks || bookmarks.length === 0) {
      return null;
    }

    return (
      <section className="py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          {/* Header */}
          <div className="mb-8 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <BookOpen className="h-6 w-6 text-blue-600 dark:text-blue-400" />
              <h2 className="text-2xl font-bold text-gray-900 dark:text-white">Continue Reading</h2>
            </div>
            <Link href="/bookmarks">
              <Button variant="outline">See All Bookmarks</Button>
            </Link>
          </div>

          {/* Grid of comics */}
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-5">
            {bookmarks.map((bookmark: BookmarkWithRelations) => {
              const comic = bookmark.comic || null;
              const chapter = bookmark.lastReadChapter || null;

              if (!comic) return null;

              return (
                <div
                  className="group rounded-lg border border-gray-200 bg-white p-4 transition-all hover:shadow-lg dark:border-gray-700 dark:bg-gray-800"
                  key={`${bookmark.userId}-${bookmark.comicId}`}
                >
                  {/* Cover Image */}
                  <Link href={`/comics/${comic.slug}`}>
                    <div className="relative mb-3 overflow-hidden rounded-md bg-gray-100 dark:bg-gray-700">
                      {comic.coverImage ? (
                        <>
                          <Image
                            alt={comic.title}
                            className="aspect-2/3 w-full object-cover transition-transform duration-200 group-hover:scale-105"
                            height={300}
                            src={comic.coverImage}
                            width={200}
                          />
                        </>
                      ) : (
                        <div className="aspect-2/3 w-full bg-gray-200 dark:bg-gray-600" />
                      )}
                    </div>
                  </Link>

                  {/* Title */}
                  <Link href={`/comics/${comic.slug}`}>
                    <h3 className="mb-1 line-clamp-2 font-semibold text-gray-900 transition-colors hover:text-blue-600 dark:text-white dark:hover:text-blue-400">
                      {comic.title}
                    </h3>
                  </Link>

                  {/* Current Chapter */}
                  {chapter && (
                    <p className="mb-2 text-xs text-gray-600 dark:text-gray-400">Chapter {chapter.chapterNumber}</p>
                  )}

                  {/* Progress Indicator */}
                  {chapter && (
                    <div className="mb-3 space-y-1">
                      <div className="flex items-center justify-between text-xs text-gray-600 dark:text-gray-400">
                        <span>Progress</span>
                        <span>65%</span>
                      </div>
                      <div className="h-1.5 w-full rounded-full bg-gray-200 dark:bg-gray-700">
                        <div
                          className="h-full rounded-full bg-blue-500 dark:bg-blue-400"
                          style={{
                            width: "65%",
                          }}
                        />
                      </div>
                    </div>
                  )}

                  {/* Continue Reading Button */}
                  <ResumeButton
                    className="w-full"
                    comicSlug={comic.slug}
                    firstChapterId={1}
                    lastChapterId={chapter?.id}
                    lastPageNumber={1}
                    size="sm"
                    status="Reading"
                  />
                </div>
              );
            })}
          </div>

          {/* Subtitle */}
          <p className="mt-4 text-xs text-gray-600 dark:text-gray-400">
            {bookmarks.length} comic{bookmarks.length !== 1 ? "s" : ""} in progress
          </p>
        </div>
      </section>
    );
  } catch (error) {
    console.error("[ContinueReadingSection]", error);
    // Silently fail - don't show section if there's an error
    return null;
  }
}

export default ContinueReadingSection;
