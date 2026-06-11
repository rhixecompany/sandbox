"use client";

import { useCallback, useEffect, useState } from "react";
import Link from "next/link";
import { useParams, useRouter } from "next/navigation";
import { api } from "@/lib/api";
import type { ChapterDetail, ComicDetail } from "@/lib/types";
import { Button } from "@/components/ui/button";
import { Skeleton } from "@/components/ui/skeleton";
import { ChevronLeft, ChevronRight, Home } from "lucide-react";

export default function ChapterReaderPage() {
  const params = useParams();
  const router = useRouter();
  const slug = params.slug as string;
  const chapterSlug = params.chapterSlug as string;

  const [comic, setComic] = useState<ComicDetail | null>(null);
  const [chapter, setChapter] = useState<ChapterDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Find current chapter index in the comic's chapter list
  const currentChapterIndex =
    comic?.chapters.findIndex((ch) => ch.slug === chapterSlug) ?? -1;
  const prevChapter = currentChapterIndex > 0 ? comic?.chapters[currentChapterIndex - 1] : null;
  const nextChapter =
    currentChapterIndex >= 0 && currentChapterIndex < (comic?.chapters.length ?? 0) - 1
      ? comic?.chapters[currentChapterIndex + 1]
      : null;

  useEffect(() => {
    async function loadData() {
      setLoading(true);
      setError(null);
      try {
        // Fetch comic detail (gives us chapter list)
        const comicData = await api.get<ComicDetail>(`/comics/${slug}/`);
        setComic(comicData);

        // Find the chapter by slug and fetch its detail
        const found = comicData.chapters.find((ch) => ch.slug === chapterSlug);
        if (!found) {
          setError("Chapter not found");
          return;
        }

        // Fetch chapter detail with images
        const chapterData = await api.get<ChapterDetail>(`/chapters/${found.id}/`);
        setChapter(chapterData);
      } catch {
        setError("Failed to load chapter");
      } finally {
        setLoading(false);
      }
    }
    loadData();
  }, [slug, chapterSlug]);

  const navigateChapter = useCallback(
    (newSlug: string) => {
      router.push(`/comics/${slug}/chapter/${newSlug}`);
    },
    [router, slug],
  );

  if (loading) {
    return (
      <div className="mx-auto max-w-3xl px-4 py-8">
        <Skeleton className="mb-4 h-8 w-48" />
        <Skeleton className="mb-2 h-[600px] w-full" />
        <Skeleton className="h-[600px] w-full" />
      </div>
    );
  }

  if (error || !chapter) {
    return (
      <div className="flex flex-col items-center justify-center py-20">
        <p className="text-lg text-muted-foreground">{error || "Chapter not found"}</p>
        <Button variant="outline" className="mt-4" onClick={() => router.push(`/comics/${slug}`)}>
          Back to comic
        </Button>
      </div>
    );
  }

  return (
    <div className="mx-auto max-w-4xl">
      {/* Top Nav */}
      <div className="sticky top-14 z-40 border-b bg-background/95 backdrop-blur">
        <div className="flex items-center justify-between px-4 py-2 sm:px-6">
          <div className="flex items-center gap-2">
            <Link href={`/comics/${slug}`}>
              <Button variant="ghost" size="icon" aria-label="Back to comic">
                <Home className="h-4 w-4" />
              </Button>
            </Link>
            <div className="text-sm">
              <p className="font-medium leading-none">{comic?.title}</p>
              <p className="text-xs text-muted-foreground mt-0.5">
                Ch. {chapter.chapter_number}{chapter.title ? ` - ${chapter.title}` : ""}
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            {prevChapter && (
              <Button
                variant="outline"
                size="sm"
                onClick={() => navigateChapter(prevChapter.slug)}
              >
                <ChevronLeft className="h-4 w-4" />
                Prev
              </Button>
            )}
            {nextChapter && (
              <Button
                variant="outline"
                size="sm"
                onClick={() => navigateChapter(nextChapter.slug)}
              >
                Next
                <ChevronRight className="h-4 w-4" />
              </Button>
            )}
          </div>
        </div>
      </div>

      {/* Chapter Pages */}
      <div className="px-4 py-4 sm:px-6">
        {chapter.images.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-20 text-center">
            <p className="text-muted-foreground">No images available for this chapter.</p>
          </div>
        ) : (
          <div className="flex flex-col items-center gap-4">
            {chapter.images
              .sort((a, b) => a.page_number - b.page_number)
              .map((img) => (
                <div key={img.id} className="w-full max-w-3xl">
                  <img
                    src={img.image}
                    alt={img.alt_text || `Page ${img.page_number}`}
                    className="w-full rounded-lg"
                    loading="lazy"
                  />
                </div>
              ))}
          </div>
        )}
      </div>

      {/* Bottom Nav */}
      <div className="sticky bottom-0 border-t bg-background/95 backdrop-blur">
        <div className="flex items-center justify-center gap-4 px-4 py-3">
          {prevChapter && (
            <Button variant="outline" onClick={() => navigateChapter(prevChapter.slug)}>
              <ChevronLeft className="h-4 w-4 mr-1" />
              Previous Chapter
            </Button>
          )}
          {nextChapter && (
            <Button variant="default" onClick={() => navigateChapter(nextChapter.slug)}>
              Next Chapter
              <ChevronRight className="h-4 w-4 ml-1" />
            </Button>
          )}
        </div>
      </div>
    </div>
  );
}
