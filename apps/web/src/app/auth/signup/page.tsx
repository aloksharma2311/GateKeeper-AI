import { SignupForm } from "@/features/auth/components/signup-form";

export default function SignupPage() {
  return (
    <main className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <h1 className="text-3xl font-bold mb-2">
          Create Account
        </h1>

        <p className="text-muted-foreground mb-6">
          Start investigating cyber threats.
        </p>

        <SignupForm />
      </div>
    </main>
  );
}