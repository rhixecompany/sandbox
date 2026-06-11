'use client';
import { cn } from '@/lib/utils';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import React from 'react';

const links = [
  {
    title: 'Home',
    href: '/',
  },
  {
    title: 'Series',
    href: '/series',
  },
  {
    title: 'Bookmarks',
    href: '/bookmarks',
  },
];

const HeaderNav = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLElement>) => {
  const pathname = usePathname();
  return (
    <ul className={cn('hidden md:flex flex-row', className)} {...props}>
      {links.map((item) => (
        <li key={item.href}>
          <Link
            href={item.href}
            className={cn(
              'text-[13px] tracking-wider block pt-0 pr-[10px] pb-0 pl-[8px] leading-[42px] font-medium transition-colors hover:text-primary',
              pathname.includes(item.href) ? '' : 'text-muted-foreground'
            )}
          >
            {item.title}
          </Link>
        </li>
      ))}
    </ul>
  );
};

export default HeaderNav;
