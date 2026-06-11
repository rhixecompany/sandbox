"use client";

import { Star } from "lucide-react";
import Image from "next/image";
import Link from "next/link";

import { Button } from "@/components/ui/button";

interface RatingWithComic {
  comic: {
    coverImage: null | string;
    slug: string;
    title: string;
  } | null;
  createdAt: Date | string;
  id: number;
  rating: number;
  review: null | string;
}

interface RatingsWrapperProps {
  ratings: RatingWithComic[];
}

export function RatingsWrapper({ ratings }: RatingsWrapperProps) {
  return (
    <main className="min-h-screen py-12">
      <div className="mx-auto max-w-6xl px-4">
        <div className="mb-8">
          <h1 className="mb-2 text-4xl font-bold">My Ratings</h1>
          <p className="text-muted-foreground">
            {ratings.length === 0
              ? "You haven't rated any comics yet"
              : `You have rated ${ratings.length} comic${ratings.length === 1 ? "" : "s"}`}
          </p>
        </div>

        {ratings.length === 0 ? (
          <div className="rounded-lg border border-border bg-muted/50 p-8 text-center">
            <p className="mb-4 text-muted-foreground">Start rating comics to help others find great reads!</p>
            <Link href="/browse">
              <Button>Browse Comics</Button>
            </Link>
          </div>
        ) : (
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3">
            {ratings.map((r) => {
              const comic = r.comic;
              if (!comic) return null;

              return (
                <div
                  className="overflow-hidden rounded-lg border border-border transition-shadow hover:shadow-lg"
                  key={r.id}
                >
                  <div className="relative h-48 bg-muted">
                    {comic.coverImage && (
                      <Image alt={comic.title} className="object-cover" fill src={comic.coverImage} />
                    )}
                  </div>

                  <div className="p-4">
                    <div className="mb-3 flex items-start justify-between">
                      <Link className="flex-1 font-semibold hover:underline" href={`/comics/${comic.slug}`}>
                        {comic.title}
                      </Link>
                    </div>

                    <div className="mb-3 flex items-center gap-1">
                      {Array.from({ length: 5 }).map((_, i) => (
                        <Star
                          className={`h-4 w-4 ${
                            i < r.rating ? "fill-yellow-400 text-yellow-400" : "text-muted-foreground"
                          }`}
                          key={i}
                        />
                      ))}
                      <span className="ml-1 text-sm font-medium">{r.rating}/5</span>
                    </div>

                    {r.review && <p className="mb-3 line-clamp-2 text-sm text-muted-foreground">{r.review}</p>}

                    <p className="text-xs text-muted-foreground">Rated {new Date(r.createdAt).toLocaleDateString()}</p>

                    <Link href={`/comics/${comic.slug}`}>
                      <Button className="mt-3 w-full" size="sm" variant="secondary">
                        View Comic
                      </Button>
                    </Link>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </main>
  );
}
