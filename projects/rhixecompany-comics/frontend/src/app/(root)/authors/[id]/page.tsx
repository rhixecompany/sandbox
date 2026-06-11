/**
 * Author Detail Page
 * Display all comics by a specific author
 * Route: /authors/[id]
 */

import Image from "next/image";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Suspense } from "react";

import { getAuthorByIdAction } from "@/actions/author.actions";
import { ComicCard } from "@/components/comics";
import { Button } from "@/components/ui/button";

interface AuthorComicData {
  coverImage: null | string;
  createdAt?: Date;
  description?: string;
  id: number;
  rating: null | number | string;
  slug: string;
  status: string;
  title: string;
}

async function AuthorComics({ comics }: { comics: AuthorComicData[] }) {
  if (comics.length === 0) {
    return (
      <div className="py-12 text-center">
        <p className="text-muted-foreground">No comics by this author yet</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
      {comics.map((comic) => (
        <ComicCard comic={comic} key={comic.id} variant="grid" />
      ))}
    </div>
  );
}

export async function generateMetadata({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const result = await getAuthorByIdAction(id);

  if (!result.ok || !result.data) {
    return {
      title: "Author Not Found - ComicWise",
      description: "The requested author could not be found",
    };
  }

  return {
    title: `${result.data.name} - ComicWise`,
    description: result.data.bio || `Explore comics by ${result.data.name}`,
  };
}

export default async function AuthorDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const result = await getAuthorByIdAction(id);

  if (!result.ok || !result.data) {
    notFound();
  }

  const author = result.data;

  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <section className="relative border-b border-border bg-linear-to-br from-primary/20 via-background to-primary/10 py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <Link className="mb-4 inline-block text-primary hover:underline" href="/browse">
            ← Back to Browse
          </Link>

          <div className="flex items-start gap-6">
            {author.image && (
              <Image alt={author.name} className="rounded-lg object-cover" height={96} src={author.image} width={96} />
            )}

            <div className="flex-1">
              <h1 className="mb-2 text-4xl font-bold">{author.name}</h1>
              {author.bio && <p className="max-w-3xl text-lg text-muted-foreground">{author.bio}</p>}
            </div>
          </div>
        </div>
      </section>

      {/* Comics Grid */}
      <section className="py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <h2 className="mb-6 text-2xl font-bold">Comics</h2>
          <Suspense fallback={<div className="h-96 animate-pulse bg-muted" />}>
            <AuthorComics comics={author.comics} />
          </Suspense>
        </div>
      </section>

      {/* CTA */}
      <section className="bg-muted/50 py-12">
        <div className="mx-auto max-w-7xl px-4 text-center sm:px-6 lg:px-8">
          <h2 className="mb-4 text-2xl font-bold">Explore More Authors</h2>
          <Link href="/browse">
            <Button variant="outline">Browse All</Button>
          </Link>
        </div>
      </section>
    </main>
  );
}
