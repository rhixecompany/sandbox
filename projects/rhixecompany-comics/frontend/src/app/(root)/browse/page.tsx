/**
 * Browse Page
 * Route: /browse
 */

import { getBrowseDataAction } from "@/actions/browse.actions";
import { BrowseWrapper } from "@/components/browse/browse-wrapper";

export const metadata = {
  title: "Browse - ComicWise",
  description: "Browse comics by genre or author. Discover new series and expand your collection.",
};

export default async function BrowsePage() {
  const result = await getBrowseDataAction();

  const genres = result.ok ? result.data.genres : [];
  const authors = result.ok ? result.data.authors : [];

  return <BrowseWrapper authors={authors} genres={genres} />;
}
