import { ChevronRight } from "lucide-react";
import Link from "next/link";
import { Suspense } from "react";

import { getFeaturedComicsAction, getNewComicsAction } from "@/actions/comic.actions";
import { ComicCard } from "@/components/comics";
import { Button } from "@/components/ui/button";

async function FeaturedSection() {
  const result = await getFeaturedComicsAction(8);
  if (!result.ok) return null;

  return (
    <section className="py-12">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="mb-8 flex items-center justify-between">
          <div>
            <h2 className="text-3xl font-bold">Trending Now</h2>
            <p className="mt-2 text-muted-foreground">Most popular comics this week</p>
          </div>
          <Link href="/comics?sort=popular">
            <Button className="gap-2" variant="outline">
              View All
              <ChevronRight className="h-4 w-4" />
            </Button>
          </Link>
        </div>
        <div className="grid grid-cols-2 gap-4 md:grid-cols-4 lg:grid-cols-5">
          {result.data.map((comic) => (
            <ComicCard
              comic={
                comic as {
                  coverImage?: null | string;
                  description?: string;
                  id: number;
                  rating?: null | number | string;
                  slug: string;
                  status?: string;
                  title: string;
                }
              }
              key={String(comic.id)}
              variant="grid"
            />
          ))}
        </div>
      </div>
    </section>
  );
}

async function NewReleasesSection() {
  const result = await getNewComicsAction(12);
  if (!result.ok) return null;

  return (
    <section className="bg-muted/50 py-12">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="mb-8 flex items-center justify-between">
          <div>
            <h2 className="text-3xl font-bold">New Releases</h2>
            <p className="mt-2 text-muted-foreground">Latest comics added to our library</p>
          </div>
          <Link href="/comics?sort=latest">
            <Button className="gap-2" variant="outline">
              View All
              <ChevronRight className="h-4 w-4" />
            </Button>
          </Link>
        </div>
        <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
          {result.data.map((comic) => (
            <ComicCard
              comic={
                comic as {
                  coverImage?: null | string;
                  description?: string;
                  id: number;
                  rating?: null | number | string;
                  slug: string;
                  status?: string;
                  title: string;
                }
              }
              key={String(comic.id)}
              variant="grid"
            />
          ))}
        </div>
      </div>
    </section>
  );
}

export default function HomeWrapper() {
  return (
    <>
      <section className="relative bg-linear-to-br from-primary/20 via-background to-primary/10 py-16 md:py-24">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="mx-auto max-w-3xl text-center">
            <h1 className="mb-4 text-4xl font-bold md:text-5xl lg:text-6xl">Discover Your Next Favorite Comic</h1>
            <p className="mb-8 text-lg text-muted-foreground">
              Explore thousands of manga and comics. Track your reading progress and build your personal library.
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/comics">
                <Button className="gap-2" size="lg">
                  Browse Comics
                  <ChevronRight className="h-5 w-5" />
                </Button>
              </Link>
              <Link href="/browse">
                <Button size="lg" variant="outline">
                  Explore by Genre
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </section>

      <Suspense fallback={<div className="h-96 animate-pulse bg-muted" />}>
        <FeaturedSection />
      </Suspense>

      <Suspense fallback={<div className="h-96 animate-pulse bg-muted" />}>
        <NewReleasesSection />
      </Suspense>

      <section className="py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <h2 className="mb-12 text-center text-3xl font-bold">Why Choose ComicWise?</h2>
          <div className="grid gap-8 md:grid-cols-3">
            <div className="rounded-lg border border-border p-6 transition hover:border-primary/50">
              <div className="mb-4 text-3xl">📚</div>
              <h3 className="mb-2 text-xl font-semibold">Vast Library</h3>
              <p className="text-muted-foreground">Access thousands of manga and comics from around the world</p>
            </div>
            <div className="rounded-lg border border-border p-6 transition hover:border-primary/50">
              <div className="mb-4 text-3xl">⭐</div>
              <h3 className="mb-2 text-xl font-semibold">Track Progress</h3>
              <p className="text-muted-foreground">Keep track of where you left off and your reading progress</p>
            </div>
            <div className="rounded-lg border border-border p-6 transition hover:border-primary/50">
              <div className="mb-4 text-3xl">❤️</div>
              <h3 className="mb-2 text-xl font-semibold">Personalized</h3>
              <p className="text-muted-foreground">Get recommendations based on your reading history and bookmarks</p>
            </div>
          </div>
        </div>
      </section>

      <section className="border-t border-b border-border bg-primary/5 py-12">
        <div className="mx-auto max-w-7xl px-4 text-center sm:px-6 lg:px-8">
          <h2 className="mb-4 text-3xl font-bold">Ready to Start Reading?</h2>
          <p className="mx-auto mb-8 max-w-2xl text-lg text-muted-foreground">
            Join thousands of manga enthusiasts and find your next favorite series today
          </p>
          <Link href="/comics">
            <Button size="lg">Explore Comics Now</Button>
          </Link>
        </div>
      </section>
    </>
  );
}
