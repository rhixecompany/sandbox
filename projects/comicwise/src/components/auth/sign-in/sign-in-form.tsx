"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { EyeIcon, EyeOffIcon, Loader2 } from "lucide-react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { useForm } from "react-hook-form";
import { toast } from "sonner";
import * as z from "zod";

import { signInWithCredentialsAction } from "@/actions/credentials.actions";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

// Zod validation schema for login form
const loginSchema = z.object({
  username: z
    .string()
    .min(3, "Username must be at least 3 characters")
    .max(50, "Username must not exceed 50 characters"),
  password: z
    .string()
    .min(8, "Password must be at least 8 characters")
    .max(100, "Password must not exceed 100 characters"),
  rememberMe: z.boolean().optional(),
});

type LoginFormData = z.infer<typeof loginSchema>;

const LoginForm = () => {
  const [isPasswordVisible, setIsPasswordVisible] = useState(false);
  const [isPending, startTransition] = useTransition();
  const router = useRouter();

  // Initialize react-hook-form with Zod validation
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      username: "",
      password: "",
      rememberMe: false,
    },
  });

  // Handle form submission
  const onSubmit = async (data: LoginFormData) => {
    startTransition(async () => {
      try {
        const result = await signInWithCredentialsAction(data.username, data.password);

        if (result.ok) {
          toast.success("Sign in successful!", {
            description: "Welcome back! Redirecting...",
          });

          // Redirect to home page after successful sign in
          router.push("/");
          router.refresh();
        } else {
          toast.error("Sign in failed", {
            description: result.error,
          });
        }
      } catch (error) {
        console.error("Login error:", error);
        toast.error("An unexpected error occurred", {
          description: "Please try again later.",
        });
      }
    });
  };

  return (
    <form
      className="space-y-4"
      onSubmit={(e) => {
        void handleSubmit(onSubmit)(e);
      }}
    >
      {/* Username */}
      <div className="space-y-1">
        <Label className="leading-5" htmlFor="username">
          Username*
        </Label>
        <Input
          disabled={isPending}
          id="username"
          placeholder="Enter your username"
          type="text"
          {...register("username")}
          className={errors.username ? "border-red-500" : ""}
        />
        {errors.username && <p className="text-sm text-red-500">{errors.username.message}</p>}
      </div>

      {/* Password */}
      <div className="w-full space-y-1">
        <Label className="leading-5" htmlFor="password">
          Password*
        </Label>
        <div className="relative">
          <Input
            className={`pe-9 ${errors.password ? "border-red-500" : ""}`}
            disabled={isPending}
            id="password"
            placeholder="••••••••••••••••"
            type={isPasswordVisible ? "text" : "password"}
            {...register("password")}
          />
          <Button
            className="absolute inset-y-0 inset-e-0 rounded-s-none text-muted-foreground hover:bg-transparent focus-visible:ring-ring/50"
            disabled={isPending}
            onClick={() => setIsPasswordVisible((prev) => !prev)}
            size="icon"
            type="button"
            variant="ghost"
          >
            {isPasswordVisible ? <EyeOffIcon /> : <EyeIcon />}
            <span className="sr-only">{isPasswordVisible ? "Hide password" : "Show password"}</span>
          </Button>
        </div>
        {errors.password && <p className="text-sm text-red-500">{errors.password.message}</p>}
      </div>

      {/* Remember Me and Forgot Password */}
      <div className="flex items-center justify-between gap-y-2">
        <div className="flex items-center gap-3">
          <Checkbox className="size-6" disabled={isPending} id="rememberMe" {...register("rememberMe")} />
          <Label className="text-muted-foreground" htmlFor="rememberMe">
            Remember Me
          </Label>
        </div>

        <a className="text-sm hover:underline" href="/forgot-password" tabIndex={isPending ? -1 : 0}>
          Forgot Password?
        </a>
      </div>

      <Button className="w-full" disabled={isPending} type="submit">
        {isPending ? (
          <>
            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            Signing in...
          </>
        ) : (
          "Sign in"
        )}
      </Button>

      {/* Link to sign-up page */}
      <div className="text-center text-sm text-muted-foreground">
        Don&apos;t have an account?{" "}
        <Link className="font-medium text-primary hover:underline" href="/sign-up">
          Sign up
        </Link>
      </div>
    </form>
  );
};

export default LoginForm;
