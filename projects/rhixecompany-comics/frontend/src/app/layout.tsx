import localFont from "next/font/local";
import { type ReactNode, Suspense } from "react";

import { LayoutProvider } from "@/components/layout/layout-provider";
import { Toaster } from "@/components/ui/sonner";

import "@/styles/globals.css";

import appConfig from "appConfig";

import type { Metadata, Viewport } from "next";

// Primary Font: IBM Plex Sans (Variable)
const ibmPlexSans = localFont({
  src: [
    {
      path: "../styles/fonts/IBM_Plex_Sans/IBMPlexSans-VariableFont_wdth,wght.ttf",
      style: "normal",
    },
    {
      path: "../styles/fonts/IBM_Plex_Sans/IBMPlexSans-Italic-VariableFont_wdth,wght.ttf",
      style: "italic",
    },
  ],
  variable: "--font-ibm-plex-sans",
  display: "swap",
  preload: true,
});

// Display Font: Bebas Neue
const bebasNeue = localFont({
  src: [
    {
      path: "../styles/fonts/Bebas_Neue/BebasNeue-Regular.ttf",
      weight: "400",
      style: "normal",
    },
  ],
  variable: "--font-bebas-neue",
  display: "swap",
});

// Alternative Sans: Schibsted Grotesk (Variable)
const schibstedGrotesk = localFont({
  src: [
    {
      path: "../styles/fonts/Schibsted_Grotesk/SchibstedGrotesk-VariableFont_wght.ttf",
      style: "normal",
    },
    {
      path: "../styles/fonts/Schibsted_Grotesk/SchibstedGrotesk-Italic-VariableFont_wght.ttf",
      style: "italic",
    },
  ],
  variable: "--font-schibsted-grotesk",
  display: "swap",
});

// Monospace Font: Martian Mono (Variable)
const martianMono = localFont({
  src: [
    {
      path: "../styles/fonts/Martian_Mono/MartianMono-VariableFont_wdth,wght.ttf",
    },
  ],
  variable: "--font-martian-mono",
  display: "swap",
});

// Additional Fonts: Fira Sans (Full Family)
const firaSans = localFont({
  src: [
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-Light.ttf",
      weight: "300",
      style: "normal",
    },
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-LightItalic.ttf",
      weight: "300",
      style: "italic",
    },
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-Regular.ttf",
      weight: "400",
      style: "normal",
    },
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-Italic.ttf",
      weight: "400",
      style: "italic",
    },
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-Medium.ttf",
      weight: "500",
      style: "normal",
    },
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-MediumItalic.ttf",
      weight: "500",
      style: "italic",
    },
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-SemiBold.ttf",
      weight: "600",
      style: "normal",
    },
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-SemiBoldItalic.ttf",
      weight: "600",
      style: "italic",
    },
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-Bold.ttf",
      weight: "700",
      style: "normal",
    },
    {
      path: "../styles/fonts/Fira_Sans/FiraSans-BoldItalic.ttf",
      weight: "700",
      style: "italic",
    },
  ],
  variable: "--font-fira-sans",
  display: "swap",
});

// Monospace Alternative: Fira Mono
const firaMono = localFont({
  src: [
    {
      path: "../styles/fonts/Fira_Mono/FiraMono-Regular.ttf",
      weight: "400",
      style: "normal",
    },
    {
      path: "../styles/fonts/Fira_Mono/FiraMono-Medium.ttf",
      weight: "500",
      style: "normal",
    },
    {
      path: "../styles/fonts/Fira_Mono/FiraMono-Bold.ttf",
      weight: "700",
      style: "normal",
    },
  ],
  variable: "--font-fira-mono",
  display: "swap",
});

export const metadata: Metadata = {
  title: `${appConfig.app.name} - Modern Comic Reading Platform`,
  description:
    "Read your favorite manga, manhwa, and manhua online. Track your reading progress and discover new comics.",
  keywords: ["comics", "manga", "manhwa", "manhua", "webtoon", "reading"],
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  maximumScale: 5,
  userScalable: true,
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "000000" },
  ],
  viewportFit: "cover",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <head>
        <meta content="IE=edge" httpEquiv="x-ua-compatible" />
        <link href="https://fonts.googleapis.com" rel="preconnect" />
        <link href="https://ik.imagekit.io" rel="preconnect" />
        <link href="https://res.cloudinary.com" rel="dns-prefetch" />
      </head>
      <body
        className={`${ibmPlexSans.variable}
          ${bebasNeue.variable}
          ${schibstedGrotesk.variable}
          ${martianMono.variable}
          ${firaSans.variable}
          ${firaMono.variable}
          font-sans antialiased`}
      >
        <Suspense fallback={null}>
          <LayoutProvider attribute="class" defaultTheme="system" disableTransitionOnChange enableSystem session={null}>
            {children}
          </LayoutProvider>
        </Suspense>
        <Toaster />
      </body>
    </html>
  );
}
