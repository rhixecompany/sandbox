import Link from "next/link";

import AuthBackgroundShape from "@/assets/svg/auth-background-shape";
import LoginForm from "@/components/auth/sign-in/sign-in-form";
import Logo from "@/components/layout/logo";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";

const Login = () => {
  return (
    <div className="relative flex h-auto min-h-screen items-center justify-center overflow-x-hidden px-4 py-10 sm:px-6 lg:px-8">
      <div className="absolute">
        <AuthBackgroundShape />
      </div>

      <Card className="z-1 w-full border-none shadow-md sm:max-w-lg">
        <CardHeader className="gap-6">
          <Logo className="gap-3" />

          <div>
            <CardTitle className="mb-1.5 text-2xl">Sign in to Comicwise</CardTitle>
            <CardDescription className="text-base">Ship Faster and Focus on Growth.</CardDescription>
          </div>
        </CardHeader>

        <CardContent>
          <p className="mb-6 text-muted-foreground">
            Login with{" "}
            <Link className="text-card-foreground hover:underline" href="#">
              Magic Link
            </Link>
          </p>

          {/* Quick Login Buttons */}
          <div className="mb-6 flex flex-wrap gap-4 sm:gap-6">
            <Button className="grow" variant="outline">
              Login as User
            </Button>
            <Button className="grow" variant="outline">
              Login as Admin
            </Button>
          </div>

          {/* Login Form */}
          <div className="space-y-4">
            <LoginForm />

            <p className="text-center text-muted-foreground">
              New on our platform?{" "}
              <Link className="text-card-foreground hover:underline" href="/sign-up">
                Create an account
              </Link>
            </p>

            <div className="flex items-center gap-4">
              <Separator className="flex-1" />
              <p>or</p>
              <Separator className="flex-1" />
            </div>

            <Button asChild className="w-full" variant="ghost">
              <Link href="#">Sign in with google</Link>
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default Login;
