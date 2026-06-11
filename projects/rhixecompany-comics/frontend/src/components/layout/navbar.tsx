import Link from "next/link";

import { auth } from "@/auth";
import Logo from "@/components/layout/logo";
import NavbarClient from "@/components/layout/navbar-client";

export default async function Navbar() {
  const session = await auth();
  const user = session?.user;

  return (
    <header className="sticky top-0 z-50 bg-background">
      <div className="mx-auto flex max-w-7xl items-center justify-between gap-8 px-4 py-7 sm:px-6">
        <nav className="flex flex-1 items-center gap-8 font-medium text-muted-foreground md:justify-center lg:gap-16">
          <Link className="hover:text-primary max-md:hidden" href="/">
            Home
          </Link>
          <Link className="hover:text-primary max-md:hidden" href="/comics">
            Comics
          </Link>
          <Link className="hover:text-primary max-md:hidden" href="/browse">
            Browse
          </Link>
          <Link className="hover:text-primary max-md:hidden" href="/genres/action">
            Genres
          </Link>
          <Link href="/">
            <Logo className="gap-3 text-foreground" />
          </Link>
        </nav>

        <NavbarClient serverUser={user} />
      </div>
    </header>
  );
}
