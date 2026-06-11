"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { EyeIcon, EyeOffIcon, Loader2 } from "lucide-react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState, useTransition } from "react";
import { useForm } from "react-hook-form";
import { toast } from "sonner";
import * as z from "zod";

import { registerAction } from "@/actions/credentials.actions";
import { Button } from "@/components/ui/button";
import { Checkbox } from "@/components/ui/checkbox";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

// Zod validation schema for registration form
const registerSchema = z
  .object({
    username: z
      .string()
      .min(3, "Username must be at least 3 characters")
      .max(50, "Username must not exceed 50 characters")
      .regex(/^[a-zA-Z0-9_-]+$/, "Username can only contain letters, numbers, hyphens, and underscores"),
    email: z.string().min(1, "Email is required").email("Please enter a valid email address"),
    password: z
      .string()
      .min(8, "Password must be at least 8 characters")
      .max(100, "Password must not exceed 100 characters")
      .regex(
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/,
        "Password must contain at least one uppercase letter, one lowercase letter, and one number"
      ),
    confirmPassword: z.string().min(1, "Please confirm your password"),
    agreeToTerms: z.boolean().refine((val) => val === true, {
      message: "You must agree to the privacy policy and terms",
    }),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: "Passwords do not match",
    path: ["confirmPassword"],
  });

type RegisterFormData = z.infer<typeof registerSchema>;

const RegisterForm = () => {
  const [isPasswordVisible, setIsPasswordVisible] = useState(false);
  const [isConfirmPasswordVisible, setIsConfirmPasswordVisible] = useState(false);
  const [isPending, startTransition] = useTransition();
  const router = useRouter();

  // Initialize react-hook-form with Zod validation
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<RegisterFormData>({
    resolver: zodResolver(registerSchema),
    defaultValues: {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
      agreeToTerms: false,
    },
  });

  // Handle form submission
  const onSubmit = async (data: RegisterFormData) => {
    startTransition(async () => {
      try {
        const result = await registerAction(data.username, data.email, data.password);

        if (result.ok) {
          toast.success("Registration successful!", {
            description: "Your account has been created. Please sign in.",
          });

          // Redirect to sign-in page after successful registration
          router.push("/sign-in");
          router.refresh();
        } else {
          toast.error("Registration failed", {
            description: result.error,
          });
        }
      } catch (error) {
        console.error("Registration error:", error);
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

      {/* Email */}
      <div className="space-y-1">
        <Label className="leading-5" htmlFor="userEmail">
          Email address*
        </Label>
        <Input
          disabled={isPending}
          id="userEmail"
          placeholder="Enter your email address"
          type="email"
          {...register("email")}
          className={errors.email ? "border-red-500" : ""}
        />
        {errors.email && <p className="text-sm text-red-500">{errors.email.message}</p>}
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

      {/* Confirm Password */}
      <div className="w-full space-y-1">
        <Label className="leading-5" htmlFor="confirmPassword">
          Confirm Password*
        </Label>
        <div className="relative">
          <Input
            className={`pe-9 ${errors.confirmPassword ? "border-red-500" : ""}`}
            disabled={isPending}
            id="confirmPassword"
            placeholder="••••••••••••••••"
            type={isConfirmPasswordVisible ? "text" : "password"}
            {...register("confirmPassword")}
          />
          <Button
            className="absolute inset-y-0 inset-e-0 rounded-s-none text-muted-foreground hover:bg-transparent focus-visible:ring-ring/50"
            disabled={isPending}
            onClick={() => setIsConfirmPasswordVisible((prev) => !prev)}
            size="icon"
            type="button"
            variant="ghost"
          >
            {isConfirmPasswordVisible ? <EyeOffIcon /> : <EyeIcon />}
            <span className="sr-only">{isConfirmPasswordVisible ? "Hide password" : "Show password"}</span>
          </Button>
        </div>
        {errors.confirmPassword && <p className="text-sm text-red-500">{errors.confirmPassword.message}</p>}
      </div>

      {/* Privacy policy */}
      <div className="space-y-1">
        <div className="flex items-start gap-3">
          <Checkbox className="mt-0.5 size-6" disabled={isPending} id="agreeToTerms" {...register("agreeToTerms")} />
          <Label className="cursor-pointer" htmlFor="agreeToTerms">
            <span className="text-muted-foreground">I agree to</span>{" "}
            <a
              className="text-primary hover:underline"
              href="/privacy-policy"
              rel="noopener noreferrer"
              target="_blank"
            >
              privacy policy & terms
            </a>
          </Label>
        </div>
        {errors.agreeToTerms && <p className="text-sm text-red-500">{errors.agreeToTerms.message}</p>}
      </div>

      <Button className="w-full" disabled={isPending} type="submit">
        {isPending ? (
          <>
            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            Creating account...
          </>
        ) : (
          "Sign Up"
        )}
      </Button>

      {/* Link to sign-in page */}
      <div className="text-center text-sm text-muted-foreground">
        Already have an account?{" "}
        <Link className="font-medium text-primary hover:underline" href="/sign-in">
          Sign in
        </Link>
      </div>
    </form>
  );
};

export default RegisterForm;
