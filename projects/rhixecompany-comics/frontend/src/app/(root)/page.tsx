/**
 * Home Page
 * Route: /
 */

import HomeWrapper from "@/components/home/home-wrapper";

export const metadata = {
  title: "Home - ComicWise",
  description: "Discover manga and comics. Track your reading progress and build your personal library.",
};

export default function HomePage() {
  return <HomeWrapper />;
}
