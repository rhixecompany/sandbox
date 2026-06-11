import Link from "next/link";

import AuthBackgroundShape from "@/assets/svg/auth-background-shape";
import RegisterForm from "@/components/auth/sign-up/sign-up-form";
import Logo from "@/components/layout/logo";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";

const Register = () => {
  return (
    <div className="relative flex h-auto min-h-screen items-center justify-center overflow-x-hidden px-4 py-10 sm:px-6 lg:px-8">
      <div className="absolute">
        <AuthBackgroundShape />
      </div>

      <Card className="z-1 w-full border-none shadow-md sm:max-w-lg">
        <CardHeader className="gap-6">
          <Logo className="gap-3" />

          <div>
            <CardTitle className="mb-1.5 text-2xl">Sign Up to ComicWise</CardTitle>
            <CardDescription className="text-base">Ship Faster and Focus on Growth.</CardDescription>
          </div>
        </CardHeader>

        <CardContent>
          {/* Register Form */}
          <div className="space-y-4">
            <RegisterForm />

            <p className="text-center text-muted-foreground">
              Already have an account?{" "}
              <Link className="text-card-foreground hover:underline" href="/sign-in">
                Sign in instead
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

export default Register;
