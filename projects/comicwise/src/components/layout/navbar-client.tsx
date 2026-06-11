"use client";

import { MenuIcon, SearchIcon } from "lucide-react";
import { useSession } from "next-auth/react";
import Link from "next/link";
import { useTransition } from "react";

import { signOutAction } from "@/actions/auth.actions";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

interface User {
  email?: null | string;
  image?: null | string;
  name?: null | string;
}

interface NavbarClientProps {
  serverUser?: null | User;
}

export default function NavbarClient({ serverUser }: NavbarClientProps) {
  const { data: session } = useSession();
  const [isPending, startTransition] = useTransition();
  const user = serverUser ?? session?.user;

  const handleSignOut = () => {
    startTransition(async () => {
      await signOutAction("/sign-in");
    });
  };

  return (
    <div className="flex items-center gap-6">
      <Link href="/search">
        <Button size="icon" variant="ghost">
          <SearchIcon />
          <span className="sr-only">Search</span>
        </Button>
      </Link>

      <DropdownMenu>
        <DropdownMenuTrigger asChild className="md:hidden">
          <Button size="icon" variant="outline">
            <MenuIcon />
            <span className="sr-only">Menu</span>
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent align="end" className="w-56">
          <DropdownMenuItem asChild>
            <Link href="/">Home</Link>
          </DropdownMenuItem>
          <DropdownMenuItem asChild>
            <Link href="/comics">Comics</Link>
          </DropdownMenuItem>
          <DropdownMenuItem asChild>
            <Link href="/browse">Browse</Link>
          </DropdownMenuItem>
          <DropdownMenuItem asChild>
            <Link href="/genres/action">Genres</Link>
          </DropdownMenuItem>
          <DropdownMenuSeparator />
          {user && (
            <>
              <DropdownMenuItem asChild>
                <Link href="/bookmarks">My Bookmarks</Link>
              </DropdownMenuItem>
              <DropdownMenuItem asChild>
                <Link href="/profile">Profile</Link>
              </DropdownMenuItem>
            </>
          )}
        </DropdownMenuContent>
      </DropdownMenu>

      {user ? (
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <Button size="sm" variant="outline">
              {user.name || "User"}
            </Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end" className="w-56">
            <DropdownMenuItem asChild>
              <Link href="/bookmarks">My Bookmarks</Link>
            </DropdownMenuItem>
            <DropdownMenuItem asChild>
              <Link href="/profile">Profile</Link>
            </DropdownMenuItem>
            <DropdownMenuItem asChild>
              <Link href="/profile/settings">Settings</Link>
            </DropdownMenuItem>
            <DropdownMenuSeparator />
            <DropdownMenuItem asChild>
              <button className="w-full cursor-default items-center" disabled={isPending} onClick={handleSignOut}>
                Sign Out
              </button>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      ) : (
        <Link href="/sign-in">
          <Button size="sm">Sign In</Button>
        </Link>
      )}
    </div>
  );
}
