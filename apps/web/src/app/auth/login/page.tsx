import { LoginForm } from "@/features/auth/components/login-form";

export default function LoginPage() {
  return (
    <main className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        <h1 className="text-3xl font-bold mb-2">
          Sign In
        </h1>

        <p className="text-muted-foreground mb-6">
          Access your GateKeeper AI dashboard.
        </p>

        <LoginForm />
      </div>
    </main>
  );
}