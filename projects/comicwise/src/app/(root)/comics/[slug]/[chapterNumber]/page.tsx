import { notFound } from "next/navigation";
import { Suspense } from "react";

import { getBookmarkStatusAction } from "@/actions/bookmark.actions";
import { getComicBySlugAction } from "@/actions/comic.actions";
import { auth } from "@/auth";
import { ChapterReaderWrapper } from "@/components/reading/chapter-reader-wrapper";

import type { Metadata } from "next";

interface ChapterPageProps {
  params: Promise<{
    chapterNumber: string;
    slug: string;
  }>;
}

interface ChapterData {
  chapterId: number;
  chapterImages: string[];
  chapterNumber: number;
  chapterTitle: string;
  comicId: number;
  comicSlug: string;
  totalChapters: number;
}

async function getChapterData(slug: string, chapterNumber: number): Promise<ChapterData | null> {
  try {
    const comicResult = await getComicBySlugAction(slug);
    if (!comicResult.ok || !comicResult.data) return null;

    const comic = comicResult.data;

    const chapters =
      (comic.chapters as Array<{
        chapterNumber: number;
        id: number;
        title: null | string;
        url: null | string;
      }>) ?? [];

    const chapter = chapters.find((ch) => ch.chapterNumber === chapterNumber);
    if (!chapter) return null;

    const totalChapters = chapters.length;

    let chapterImages: string[] = [];
    if (chapter.url && typeof chapter.url === "string") {
      try {
        chapterImages = JSON.parse(chapter.url) as string[];
      } catch {
        chapterImages = chapter.url.split(",").map((url: string) => url.trim());
      }
    }

    return {
      chapterId: chapter.id,
      chapterImages,
      chapterNumber,
      chapterTitle: String(chapter.title),
      comicId: comic.id as number,
      comicSlug: slug,
      totalChapters,
    };
  } catch (error) {
    console.error("[getChapterData]", error);
    return null;
  }
}

export async function generateMetadata({ params }: ChapterPageProps): Promise<Metadata> {
  const { slug, chapterNumber } = await params;
  const chapterNum = parseInt(chapterNumber, 10);

  const data = await getChapterData(slug, chapterNum);

  if (!data) {
    return { title: "Chapter Not Found" };
  }

  return {
    title: `${data.chapterTitle} - Chapter ${data.chapterNumber}`,
    description: `Read Chapter ${data.chapterNumber} of comic`,
  };
}

export default async function ChapterPage({ params }: ChapterPageProps) {
  const { slug, chapterNumber } = await params;
  const chapterNum = parseInt(chapterNumber, 10);

  if (isNaN(chapterNum) || chapterNum < 1) {
    notFound();
  }

  const data = await getChapterData(slug, chapterNum);

  if (!data) {
    notFound();
  }

  const { chapterId, chapterImages, chapterTitle, comicId, comicSlug, totalChapters } = data;

  if (!chapterImages || chapterImages.length === 0) {
    return (
      <div className="flex h-screen items-center justify-center bg-gray-900">
        <div className="text-center text-white">
          <h1 className="mb-2 text-2xl font-bold">No images found</h1>
          <p className="text-gray-400">This chapter has no images available.</p>
          <a
            className="mt-4 inline-block rounded bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700"
            href={`/comics/${slug}`}
          >
            Back to Comic
          </a>
        </div>
      </div>
    );
  }

  const session = await auth();
  const userId = session?.user?.id;

  let isBookmarked = false;
  if (userId) {
    try {
      const result = await getBookmarkStatusAction(comicId);
      isBookmarked = result.ok && !!result.data;
    } catch {
      isBookmarked = false;
    }
  }

  return (
    <Suspense
      fallback={
        <div className="flex h-screen items-center justify-center bg-gray-900">
          <div className="text-center text-white">
            <div className="mb-4 inline-block h-12 w-12 animate-spin rounded-full border-4 border-gray-700 border-t-blue-600" />
            <p className="text-gray-400">Loading chapter...</p>
          </div>
        </div>
      }
    >
      <ChapterReaderWrapper
        chapterId={chapterId}
        chapterImages={chapterImages}
        chapterNumber={chapterNum}
        chapterTitle={chapterTitle}
        comicId={comicId}
        comicSlug={comicSlug}
        isBookmarked={isBookmarked}
        onBookmarkToggle={() => {}}
        totalChapters={totalChapters}
      />
    </Suspense>
  );
}
