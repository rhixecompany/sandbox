import { Button } from '@/components/ui/button';
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet';
import { Bookmark, MenuIcon } from 'lucide-react';
import Link from 'next/link';
import ModeToggle from './mode-toggle';
import UserButton from './user-button';

const Menu = () => {
  return (
    <div className='flex justify-end gap-3'>
      <nav className='hidden md:flex w-full max-w-xs gap-1'>
        <ModeToggle />
        <Button asChild variant='ghost'>
          <Link href='/bookmark'>
            <Bookmark /> Bookmark
          </Link>
        </Button>
        <UserButton />
      </nav>
      <nav className='md:hidden'>
        <Sheet>
          <SheetTrigger className='align-middle'>
            <MenuIcon />
          </SheetTrigger>
          <SheetContent className='flex flex-col items-start'>
            <SheetTitle>Menu</SheetTitle>
            <ModeToggle />
            <Button asChild variant='ghost'>
              <Link href='/bookmark'>
                <Bookmark /> Bookmark
              </Link>
            </Button>
            <UserButton />
            <SheetDescription></SheetDescription>
          </SheetContent>
        </Sheet>
      </nav>
    </div>
  );
};

export default Menu;
