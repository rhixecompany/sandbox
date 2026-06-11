"use client";

import { Share2 } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

interface ShareButtonProps {
  description?: string;
  title: string;
  url: string;
}

/**
 * Share button component
 * Provides quick sharing options for comics
 */
export function ShareButton({ title, url, description = "" }: ShareButtonProps) {
  const canShare = typeof navigator !== "undefined" && !!(navigator as unknown as { share?: unknown }).share;

  const handleCopyLink = () => {
    void navigator.clipboard.writeText(url);
    toast.success("Link copied to clipboard!");
  };

  const handleShareTwitter = () => {
    const text = `Check out "${title}" on ComicWise! ${description ? description : ""}`;
    const twitterUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}`;
    window.open(twitterUrl, "_blank", "noopener,noreferrer");
  };

  const handleShareFacebook = () => {
    const facebookUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
    window.open(facebookUrl, "_blank", "noopener,noreferrer");
  };

  const handleShare = async () => {
    const nav = navigator as unknown as { share?: (data: ShareData) => Promise<void> };
    if (canShare && nav.share) {
      try {
        await nav.share({
          title,
          text: description,
          url,
        });
      } catch {
        // User cancelled share
      }
    }
  };

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button className="gap-2" size="sm" variant="outline">
          <Share2 className="h-4 w-4" />
          Share
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end">
        {canShare && <DropdownMenuItem onClick={() => void handleShare()}>Share via App</DropdownMenuItem>}
        <DropdownMenuItem onClick={() => void handleCopyLink()}>Copy Link</DropdownMenuItem>
        <DropdownMenuItem onClick={() => void handleShareTwitter()}>Share on Twitter</DropdownMenuItem>
        <DropdownMenuItem onClick={() => void handleShareFacebook()}>Share on Facebook</DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
