/**
 * Comic Details Page
 * Route: /comics/[slug]
 */

import { notFound } from "next/navigation";
import { Suspense } from "react";

import { getBookmarkStatusAction } from "@/actions/bookmark.actions";
import { getComicBySlugAction, getRelatedComicsAction } from "@/actions/comic.actions";
import {
  getComicAverageRatingAction,
  getComicRatingsAction,
  getUserComicRatingAction,
} from "@/actions/comment-rating.actions";
import { auth } from "@/auth";
import { ComicDetailWrapper } from "@/components/comics/comic-detail-wrapper";
import type { Rating } from "@/types/comment-rating";

// Type for the comic data structure from getComicBySlugAction
interface ComicData {
  artist?: { name: string } | null;
  author?: { name: string } | null;
  chapters?: Array<{
    chapterNumber: number;
    createdAt: Date | string;
    id: number;
    title: null | string;
  }>;
  comicToGenre?: Array<{ genre?: { id: number; name: string } }>;
  coverImage: null | string;
  description: null | string;
  id: number;
  rating: { average: number } | null;
  slug: string;
  status: string;
  title: string;
  type?: { name: string } | null;
}

// Type for related comic data
interface RelatedComicData {
  coverImage?: null | string;
  description?: string;
  id: number;
  rating?: null | number | string;
  slug: string;
  status?: string;
  title: string;
  type?: { name: string } | null;
}

// Type for ratings data
interface RatingsData {
  allRatings: Rating[];
  averageRating: number;
  userRating: null | Rating;
}

import type { Metadata } from "next";

interface PageProps {
  params: Promise<{
    slug: string;
  }>;
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const { slug } = await params;
  const result = await getComicBySlugAction(slug);

  if (!result.ok || !result.data) {
    return { title: "Comic Not Found | ComicWise" };
  }

  return {
    title: `${result.data.title as string} | ComicWise`,
    description: (result.data.description as string)?.substring(0, 160),
  };
}

export default async function ComicDetailPage({ params }: PageProps) {
  const { slug } = await params;

  const [comicResult, session] = await Promise.all([getComicBySlugAction(slug), auth()]);

  if (!comicResult.ok || !comicResult.data) {
    notFound();
  }

  // Cast to expected types
  const comic = comicResult.data as unknown as ComicData;
  const comicId = comic.id;
  const [relatedResult, bookmarkResult, averageRatingResult, ratingsResult] = await Promise.all([
    getRelatedComicsAction(comicId, 6),
    session?.user ? getBookmarkStatusAction(comicId) : { ok: true as const, data: null },
    getComicAverageRatingAction(comicId),
    getComicRatingsAction(comicId, 1, 100),
  ]);

  // Fetch user rating if authenticated
  const userRatingResult = session?.user ? await getUserComicRatingAction(comicId) : { ok: true as const, data: null };

  const relatedComics = (relatedResult.ok ? relatedResult.data : []) as unknown as RelatedComicData[];

  const ratingsData: RatingsData = {
    averageRating: averageRatingResult.ok ? averageRatingResult.data : 0,
    allRatings: ratingsResult.ok ? (ratingsResult.data as unknown as Rating[]) : [],
    userRating: userRatingResult.ok ? (userRatingResult.data as unknown as null | Rating) : null,
  };

  return (
    <Suspense
      fallback={
        <div className="min-h-screen bg-background">
          <div className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
            <div className="h-96 animate-pulse rounded-lg bg-muted" />
          </div>
        </div>
      }
    >
      <ComicDetailWrapper
        bookmarkStatus={bookmarkResult.ok ? bookmarkResult.data : null}
        comic={comic}
        ratingsData={ratingsData}
        relatedComics={relatedComics}
        sessionUserId={session?.user?.id}
      />
    </Suspense>
  );
}
