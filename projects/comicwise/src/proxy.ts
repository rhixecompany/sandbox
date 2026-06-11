/**
 * Next.js Proxy
 * Handles authentication and route protection
 */

import { NextResponse } from "next/server";

import { auth } from "auth";

import type { NextRequest } from "next/server";

// Define protected routes that require authentication
const protectedRoutes = [
  "/feed",
  "/profile",
  "/profile/edit",
  "/profile/change-password",
  "/profile/settings",
  "/bookmarks",
  "/ratings",
  "/admin",
];

// Define auth routes that should redirect if already authenticated
const authRoutes = ["/sign-in", "/sign-up", "/auth/sign-in", "/auth/sign-up"];

export async function proxy(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // Get session
  const session = await auth();
  const isAuthenticated = !!session?.user;

  // Check if route is protected
  const isProtectedRoute = protectedRoutes.some((route) => pathname.startsWith(route));

  // Check if route is an auth route
  const isAuthRoute = authRoutes.some((route) => pathname.startsWith(route));

  // Redirect unauthenticated users from protected routes to sign-in
  if (isProtectedRoute && !isAuthenticated) {
    const signInUrl = new URL("/sign-in", request.url);
    signInUrl.searchParams.set("callbackUrl", pathname);
    return NextResponse.redirect(signInUrl);
  }

  // Redirect authenticated users away from auth pages to home
  if (isAuthRoute && isAuthenticated) {
    return NextResponse.redirect(new URL("/", request.url));
  }

  return NextResponse.next();
}

// Configure which routes to run proxy on
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     * - public files (images, etc.)
     */
    "/((?!api|_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",
  ],
};
