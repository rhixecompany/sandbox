import '@/assets/styles/globals.css';
import Footer from '@/components/footer';
import Header from '@/components/shared/header';

import { Toaster } from '@/components/ui/toaster';
import { APP_DESCRIPTION, APP_NAME, SERVER_URL } from '@/lib/constants';
import type { Metadata } from 'next';
import { ThemeProvider } from 'next-themes';
// import { Fira_Sans } from 'next/font/google';

// const fira_Sans = Fira_Sans({
//   // display: 'swap',
//   subsets: ['latin'],
//   weight: ['100', '200', '300', '400', '500', '600', '700', '800', '900'],
// });

export const metadata: Metadata = {
  title: {
    template: `%s | Rhixe Scans`,
    default: APP_NAME,
  },
  description: APP_DESCRIPTION,
  metadataBase: new URL(SERVER_URL),
};
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang='en' suppressHydrationWarning>
      {/* <html lang="en" className={`${fira_Sans.className}`}> */}
      <body className='antialiased'>
        {/* <body className={` ${fira_Sans.className} antialiased`}> */}
        <ThemeProvider
          attribute='class'
          defaultTheme='dark'
          enableSystem
          disableTransitionOnChange
        >
          <Header />
          {children}
          <Footer />

          <Toaster />
        </ThemeProvider>
      </body>
    </html>
  );
}
