"use client";

import Link from "next/link";

import { Button } from "@/components/ui/button";

interface CommentData {
  chapter: {
    chapterNumber: number | string;
    comic?: {
      slug: string;
      title: string;
    };
  };
  content: string;
  createdAt: Date | string;
  id: number | string;
}

interface CommentsWrapperProps {
  comments: CommentData[];
}

export function CommentsWrapper({ comments }: CommentsWrapperProps) {
  return (
    <main className="min-h-screen py-12">
      <div className="mx-auto max-w-4xl px-4">
        <div className="mb-8">
          <h1 className="mb-2 text-4xl font-bold">My Comments</h1>
          <p className="text-muted-foreground">
            {comments.length === 0
              ? "You haven't made any comments yet"
              : `You have ${comments.length} comment${comments.length === 1 ? "" : "s"}`}
          </p>
        </div>

        {comments.length === 0 ? (
          <div className="rounded-lg border border-border bg-muted/50 p-8 text-center">
            <p className="mb-4 text-muted-foreground">Start commenting on chapters to engage with the community!</p>
            <Link href="/browse">
              <Button>Browse Comics</Button>
            </Link>
          </div>
        ) : (
          <div className="space-y-6">
            {comments.map((c) => (
              <div className="rounded-lg border border-border p-6" key={c.id}>
                <div className="mb-3 flex items-start justify-between">
                  <div>
                    <h3 className="text-lg font-semibold">{c.chapter?.comic?.title || ""}</h3>
                    <p className="text-sm text-muted-foreground">Chapter {c.chapter?.chapterNumber}</p>
                  </div>
                  <span className="text-xs text-muted-foreground">{new Date(c.createdAt).toLocaleDateString()}</span>
                </div>

                <p className="mb-4 text-sm leading-relaxed">
                  {c.content === "[deleted]" ? "[This comment has been deleted]" : c.content}
                </p>

                {c.chapter?.comic?.slug && (
                  <Link className="text-sm text-primary hover:underline" href={`/comics/${c.chapter.comic.slug}`}>
                    View Chapter →
                  </Link>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
