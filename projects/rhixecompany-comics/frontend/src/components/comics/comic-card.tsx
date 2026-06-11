/**
 * Comic Card Component
 * Displays a comic in a grid/list view
 */

import { Star } from "lucide-react";
import Image from "next/image";
import Link from "next/link";

interface ComicCardProps {
  comic: {
    coverImage?: null | string;
    description?: string;
    id: number;
    rating?: null | number | string;
    slug: string;
    status?: string;
    title: string;
  };
  type?: { name: string } | null;
  variant?: "grid" | "list";
}

export function ComicCard({ comic, type, variant = "grid" }: ComicCardProps) {
  const rating = comic.rating ? parseFloat(comic.rating.toString()) : 0;
  const statusDisplay = comic.status === "Ongoing" ? "Ongoing" : comic.status === "Completed" ? "Completed" : "Hiatus";
  const typeName = type?.name ?? "Comic";

  if (variant === "list") {
    return (
      <Link
        className="flex gap-4 rounded-lg border p-4 transition hover:bg-muted"
        data-testid="comic-card"
        href={`/comics/${comic.slug}`}
      >
        {/* Cover image */}
        {comic.coverImage && (
          <div className="relative h-32 w-24 shrink-0">
            <Image alt={comic.title} className="rounded object-cover" fill src={comic.coverImage} />
          </div>
        )}

        {/* Comic info */}
        <div className="min-w-0 flex-1">
          <h3 className="truncate text-lg font-semibold">{comic.title}</h3>

          {/* Type and Status */}
          <div className="mt-2 flex flex-wrap gap-2">
            <span className="rounded bg-muted px-2 py-1 text-xs">{typeName}</span>
            <span className="rounded bg-muted px-2 py-1 text-xs">{statusDisplay}</span>
          </div>

          {/* Description */}
          <p className="mt-2 line-clamp-2 text-sm text-muted-foreground">{comic.description}</p>

          {/* Rating */}
          <div className="mt-3 flex items-center gap-1">
            <Star className="h-4 w-4 fill-yellow-500 text-yellow-500 dark:fill-yellow-400 dark:text-yellow-400" />
            <span className="text-sm font-semibold dark:text-foreground">{rating.toFixed(1)}</span>
            <span className="text-xs text-muted-foreground dark:text-muted-foreground">
              {rating > 0 ? "/ 5" : "No ratings"}
            </span>
          </div>
        </div>
      </Link>
    );
  }

  // Grid variant (default)
  return (
    <article className="group overflow-hidden">
      <Link className="flex flex-col" data-testid="comic-card" href={`/comics/${comic.slug}`}>
        <div className="relative aspect-2/3 w-full overflow-hidden rounded-lg bg-muted dark:bg-muted/80">
          {/* Cover image */}
          {comic.coverImage ? (
            <Image
              alt={comic.title}
              className="object-cover transition-transform duration-200 group-hover:scale-105"
              fill
              sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
              src={comic.coverImage}
            />
          ) : (
            <div className="flex h-full w-full items-center justify-center bg-linear-to-br from-muted to-muted-foreground/20">
              <span className="text-xs text-muted-foreground">No Cover</span>
            </div>
          )}

          {/* Overlay on hover */}
          <div className="pointer-events-none absolute inset-0 flex flex-col justify-between bg-black/40 p-3 opacity-0 transition-opacity duration-200 group-hover:opacity-100 dark:bg-black/60">
            {/* Status badges */}
            <div className="flex items-start justify-between">
              <span className="rounded bg-primary px-2 py-1 text-xs text-primary-foreground">{statusDisplay}</span>
              <span className="rounded bg-secondary px-2 py-1 text-xs text-secondary-foreground">{typeName}</span>
            </div>

            {/* Rating */}
            <div className="space-y-2">
              <div className="flex items-center gap-1">
                <Star className="h-3 w-3 fill-yellow-300 text-yellow-300 dark:fill-yellow-400 dark:text-yellow-400" />
                <span className="text-xs font-semibold text-white">{rating.toFixed(1)}</span>
              </div>
            </div>
          </div>
        </div>

        {/* Comic info below */}
        <div className="mt-3">
          <h3 className="line-clamp-2 text-sm font-semibold transition group-hover:text-primary">{comic.title}</h3>
          <p className="mt-1 line-clamp-1 text-xs text-muted-foreground">{typeName}</p>
        </div>
      </Link>
    </article>
  );
}
