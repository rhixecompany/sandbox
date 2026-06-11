import profilePicture from '@/assets/profile-picture.webp';

import { auth } from '@/auth';
import { SignOut } from '@/components/sign-out';
import {
  Sheet,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from '@/components/ui/sheet';
import { Bookmark, House, Library, LogIn, Menu, Settings } from 'lucide-react';
import Image from 'next/image';
import Link from 'next/link';
const UserMenuButton = async () => {
  const session = await auth();

  if (!session) {
    return (
      <Sheet>
        <SheetTrigger className='inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:text-accent-foreground h-10 w-10 text-white hover:bg-purple-800/50'>
          <Menu className=' h-5 w-5' />
        </SheetTrigger>
        <SheetContent className='fixed z-50 gap-4 bg-background shadow-lg transition ease-in-out data-open:animate-in data-closed:animate-out data-closed:duration-300 data-open:duration-500 inset-y-0 right-0 h-full data-closed:slide-out-to-right data-open:slide-in-from-right sm:max-w-sm w-full max-w-xs border-l-0 bg-gradient-to-b from-[#1a1a1a] to-purple-900 p-0 pointer-events-auto'>
          <SheetHeader className='flex flex-col h-full'>
            <SheetTitle>
              <span className='sr-only'>Title</span>
            </SheetTitle>
            <SheetDescription className='flex-1 space-y-1 p-4'>
              <Link
                className='flex items-center space-x-2 rounded-lg px-4 py-3 text-white hover:bg-white/10 transition-colors duration-200'
                href='/'
              >
                <House className='h-5 w-5' />
                <span>Home</span>
              </Link>
              <Link
                href='/series'
                className='flex items-center space-x-2 rounded-lg px-4 py-3 text-white hover:bg-white/10 transition-colors duration-200'
              >
                <Library className='h-5 w-5' />
                <span>Series</span>
              </Link>
              <Link
                href='/bookmarks'
                className='flex items-center space-x-2 rounded-lg px-4 py-3 text-white hover:bg-white/10 transition-colors duration-200'
              >
                <Bookmark className='h-5 w-5' />
                <span>Bookmarks</span>
              </Link>
            </SheetDescription>
            <div className='border-t border-white/10 p-4'>
              <button className='inline-flex items-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:text-accent-foreground h-10 px-4 py-2 w-full justify-start space-x-2 text-white hover:bg-white/10 transition-colors duration-200'>
                <Link href='/sign-in' className='flex flex-row gap-2'>
                  <LogIn className='h-5 w-5' />
                  <span>Login</span>
                </Link>
              </button>
            </div>
          </SheetHeader>
        </SheetContent>
      </Sheet>
    );
  }

  return (
    <Sheet>
      <SheetTrigger className='inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:text-accent-foreground h-10 w-10 text-white hover:bg-purple-800/50'>
        <Menu className=' h-5 w-5' />
      </SheetTrigger>
      <SheetContent className='fixed z-50 gap-4 bg-background shadow-lg transition ease-in-out data-open:animate-in data-closed:animate-out data-closed:duration-300 data-open:duration-500 inset-y-0 right-0 h-full data-closed:slide-out-to-right data-open:slide-in-from-right sm:max-w-sm w-full max-w-xs border-l-0 bg-gradient-to-b from-[#1a1a1a] to-purple-900 p-0 pointer-events-auto'>
        <SheetHeader className='flex flex-col h-full'>
          <SheetTitle>
            <div className='flex items-center space-x-4'>
              <Image
                width={100}
                height={100}
                src={profilePicture}
                alt='adminbot'
                className='h-12 w-12 rounded-full border-2 border-white/20'
              />
              <div className='space-y-1'>
                <h2 className='text-base font-medium text-white'>
                  {session.user?.name}
                </h2>
                <p className='text-sm text-white/70'>{session.user?.email}</p>
              </div>
            </div>
          </SheetTitle>
          <SheetDescription className='flex-1 space-y-1 p-4'>
            <Link
              className='flex items-center space-x-2 rounded-lg px-4 py-3 text-white hover:bg-white/10 transition-colors duration-200'
              href='/'
            >
              <House className='h-5 w-5' />
              <span>Home</span>
            </Link>
            <Link
              href='/series'
              className='flex items-center space-x-2 rounded-lg px-4 py-3 text-white hover:bg-white/10 transition-colors duration-200'
            >
              <Library className='h-5 w-5' />
              <span>Series</span>
            </Link>
            <Link
              href='/bookmarks'
              className='flex items-center space-x-2 rounded-lg px-4 py-3 text-white hover:bg-white/10 transition-colors duration-200'
            >
              <Bookmark className='h-5 w-5' />
              <span>Bookmarks</span>
            </Link>
          </SheetDescription>
          <div className='border-t border-white/10 p-4'>
            <button className='inline-flex items-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:text-accent-foreground h-10 px-4 py-2 w-full justify-start space-x-2 text-white hover:bg-white/10 transition-colors duration-200'>
              <Link href='/user/profile' className='flex flex-row gap-2'>
                <Settings className='h-5 w-5' />
                <span>Settings</span>
              </Link>
            </button>
            <SignOut />
          </div>
        </SheetHeader>
      </SheetContent>
    </Sheet>
  );
};

export default UserMenuButton;
