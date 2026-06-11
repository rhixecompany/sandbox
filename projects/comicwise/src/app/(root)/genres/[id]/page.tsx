/**
 * Genre Detail Page
 * Route: /genres/[id]
 */

import { notFound } from "next/navigation";

import { getComicsByGenreAction } from "@/actions/genre.actions";
import { GenreDetailWrapper } from "@/components/genres/genre-detail-wrapper";

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const result = await getComicsByGenreAction(id);

  if (!result.ok || !result.data) {
    return {
      title: "Genre Not Found - ComicWise",
      description: "The requested genre could not be found",
    };
  }

  return {
    title: `${result.data.name} Comics - ComicWise`,
    description: result.data.description || `Browse ${result.data.name} comics`,
  };
}

export default async function GenreDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const result = await getComicsByGenreAction(id);

  if (!result.ok || !result.data) {
    notFound();
  }

  return <GenreDetailWrapper comics={result.data.comics} genre={result.data} />;
}
