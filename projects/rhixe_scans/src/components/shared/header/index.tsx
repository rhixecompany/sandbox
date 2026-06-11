import { APP_NAME } from '@/lib/constants';
import Image from 'next/image';
import Link from 'next/link';

import logo from '@/assets/logo.png';
import HeaderMenu from './header-menu';
import HeaderNav from './header-nav';
import ModeToggle from './mode-toggle';
import Search from './search';
import SearchMobile from './search-mobile';
import UserButton from './user-button';
const Header = () => {
  return (
    <header className='py-1'>
      <div className='max-w-[1220px] flex mx-auto px-2 items-center justify-between gap-5'>
        <div className='flex items-center gap-2'>
          {/* <CategoryDrawer /> */}
          <Link href='/' className='flex h-12 w-12'>
            <Image
              className='object-cover'
              src={logo}
              alt={`${APP_NAME} logo`}
              height={48}
              width={48}
              priority={true}
            />
          </Link>

          <HeaderNav />
        </div>
        <div className='flex w-full'>
          <div className='flex-row w-full gap-3.5 items-center'>
            <div className='hidden md:flex flex-row w-full gap-3.5 items-center'>
              <Search />
              <ModeToggle />
              <UserButton />
            </div>
            <div className='flex md:hidden flex-row w-full gap-3.5 items-center'>
              <div className='flex flex-row flex-grow items-center justify-end space-x-1'>
                <SearchMobile />
                <ModeToggle />
                <UserButton />
                <HeaderMenu />
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
