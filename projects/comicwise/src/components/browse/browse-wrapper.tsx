"use client";

import { ChevronRight } from "lucide-react";
import Link from "next/link";

import { Button } from "@/components/ui/button";

interface Genre {
  description?: null | string;
  id: number;
  name: string;
}

interface Author {
  bio?: null | string;
  id: number;
  name: string;
}

interface BrowseWrapperProps {
  authors: Author[];
  genres: Genre[];
}

function GenresList({ genres }: { genres: Genre[] }) {
  if (genres.length === 0) {
    return (
      <div className="py-12 text-center">
        <p className="text-muted-foreground">No genres available yet</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-4">
      {genres.map((g) => (
        <Link href={`/genres/${g.id}`} key={g.id}>
          <div className="group cursor-pointer rounded-lg border border-border p-6 text-center transition-colors hover:border-primary/50 hover:bg-primary/5">
            <h3 className="text-lg font-semibold transition group-hover:text-primary">{g.name}</h3>
            {g.description && <p className="mt-2 text-sm text-muted-foreground">{g.description}</p>}
          </div>
        </Link>
      ))}
    </div>
  );
}

function AuthorsList({ authors }: { authors: Author[] }) {
  if (authors.length === 0) {
    return (
      <div className="py-12 text-center">
        <p className="text-muted-foreground">No authors available yet</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {authors.map((a) => (
        <div
          className="group rounded-lg border border-border p-4 transition-colors hover:border-primary/50 hover:bg-primary/5"
          key={a.id}
        >
          <p className="font-medium transition group-hover:text-primary">{a.name}</p>
          {a.bio && <p className="mt-1 line-clamp-2 text-sm text-muted-foreground">{a.bio}</p>}
        </div>
      ))}
    </div>
  );
}

export function BrowseWrapper({ genres, authors }: BrowseWrapperProps) {
  return (
    <main className="min-h-screen bg-background">
      {/* Header */}
      <section className="relative border-b border-border bg-linear-to-br from-primary/20 via-background to-primary/10 py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <h1 className="mb-4 text-4xl font-bold">Browse Comics</h1>
          <p className="max-w-2xl text-lg text-muted-foreground">
            Explore by genre, author, or use our advanced filters to find exactly what you&apos;re looking for.
          </p>
        </div>
      </section>

      {/* Main Content */}
      <section className="py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="grid gap-12 lg:grid-cols-3">
            {/* Genres Section */}
            <div className="lg:col-span-2">
              <div className="mb-8 flex items-center justify-between">
                <div>
                  <h2 className="text-3xl font-bold">Genres</h2>
                  <p className="mt-2 text-muted-foreground">Browse comics by category</p>
                </div>
              </div>
              <GenresList genres={genres} />
            </div>

            {/* Sidebar */}
            <div className="space-y-8">
              {/* Quick Filters */}
              <div className="rounded-lg border border-border bg-muted/50 p-6">
                <h3 className="mb-4 text-xl font-bold">Quick Filters</h3>
                <div className="space-y-3">
                  <Link href={"/comics?sort=popular"}>
                    <Button className="w-full justify-start" size="sm" variant="outline">
                      <ChevronRight className="mr-2 h-4 w-4" />
                      Most Popular
                    </Button>
                  </Link>
                  <Link href={"/comics?sort=latest"}>
                    <Button className="w-full justify-start" size="sm" variant="outline">
                      <ChevronRight className="mr-2 h-4 w-4" />
                      Latest Releases
                    </Button>
                  </Link>
                  <Link href={"/comics?sort=rating"}>
                    <Button className="w-full justify-start" size="sm" variant="outline">
                      <ChevronRight className="mr-2 h-4 w-4" />
                      Top Rated
                    </Button>
                  </Link>
                  <Link href={"/bookmarks"}>
                    <Button className="w-full justify-start" size="sm" variant="outline">
                      <ChevronRight className="mr-2 h-4 w-4" />
                      My Bookmarks
                    </Button>
                  </Link>
                </div>
              </div>

              {/* Help Section */}
              <div className="rounded-lg border border-border bg-primary/5 p-6">
                <h3 className="mb-3 text-lg font-bold">Need Help?</h3>
                <p className="mb-4 text-sm text-muted-foreground">
                  Use the search and filter options to find your next favorite comic quickly.
                </p>
                <Link href={"/comics"}>
                  <Button className="w-full" size="sm" variant="outline">
                    Go to Comics
                  </Button>
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Authors Section */}
      <section className="border-t border-border bg-muted/50 py-12">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div className="mb-8 flex items-center justify-between">
            <div>
              <h2 className="text-3xl font-bold">Featured Authors</h2>
              <p className="mt-2 text-muted-foreground">Discover talented creators</p>
            </div>
          </div>
          <div className="grid gap-6 md:grid-cols-2">
            <AuthorsList authors={authors} />
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-12">
        <div className="mx-auto max-w-7xl text-center sm:px-6 lg:px-8">
          <h2 className="mb-4 text-2xl font-bold">Found your next favorite?</h2>
          <p className="mx-auto mb-8 max-w-2xl text-muted-foreground">
            Add comics to your bookmarks to track your reading progress and get personalized recommendations
          </p>
          <Link href={"/comics"}>
            <Button size="lg">Start Exploring</Button>
          </Link>
        </div>
      </section>
    </main>
  );
}
