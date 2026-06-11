"use client";

import Link from "next/link";

import { ComicCard } from "@/components/comics";
import { Button } from "@/components/ui/button";

interface Genre {
  description?: null | string;
  id: number;
  name: string;
}

interface ComicData {
  coverImage: null | string;
  createdAt?: Date;
  description?: string;
  id: number;
  rating: null | number | string;
  slug: string;
  status: string;
  title: string;
}

interface GenreDetailWrapperProps {
  comics: ComicData[];
  genre: Genre;
}

export function GenreDetailWrapper({ genre, comics }: GenreDetailWrapperProps) {
  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <section className="relative border-b border-border bg-primary/5 py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <Link className="mb-4 inline-block text-primary hover:underline" href="/browse">
            ← Back to Browse
          </Link>
          <h1 className="mb-4 text-4xl font-bold">{genre.name}</h1>
          {genre.description && <p className="max-w-3xl text-lg text-muted-foreground">{genre.description}</p>}
        </div>
      </section>

      {/* Comics Grid */}
      <section className="py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          {comics.length === 0 ? (
            <div className="py-12 text-center">
              <p className="text-muted-foreground">No comics in this genre yet</p>
            </div>
          ) : (
            <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
              {comics.map((c) => (
                <ComicCard comic={c} key={c.id} variant="grid" />
              ))}
            </div>
          )}
        </div>
      </section>

      {/* CTA */}
      <section className="bg-muted/50 py-12">
        <div className="mx-auto max-w-7xl px-4 text-center sm:px-6 lg:px-8">
          <h2 className="mb-4 text-2xl font-bold">Want to explore more genres?</h2>
          <Link href="/browse">
            <Button variant="outline">Browse All Genres</Button>
          </Link>
        </div>
      </section>
    </main>
  );
}
