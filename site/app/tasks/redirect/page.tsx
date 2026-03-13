"use client";

import { useEffect, useState, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import { Loader2 } from "lucide-react";

function getServerBaseUrl() {
  const isDev = process.env.NODE_ENV === "development";
  return isDev ? "http://localhost:4113" : "https://cc.getpochi.com";
}

function RedirectContent() {
  const searchParams = useSearchParams();
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const jobName = searchParams.get("job_name");
    const trialName = searchParams.get("trial_name");

    if (!jobName || !trialName) {
      setError("Missing job_name or trial_name parameters.");
      return;
    }

    const fallbackUrl = `https://github.com/TabbyML/jj-benchmark/blob/main/jobs/${jobName}/${trialName}/result.json`;

    const processRedirect = async () => {
      try {
        const messagesModule = await import("../../../messages.json");
        const messagesData = messagesModule.default || messagesModule;
        const trialMessages = (messagesData as Record<string, any>)[trialName];

        if (trialMessages) {
          const baseUrl = getServerBaseUrl();
          const response = await fetch(`${baseUrl}/api/clips`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ data: { messages: trialMessages } })
          });
          
          if (!response.ok) {
            throw new Error(`Failed to post clip: ${response.statusText}`);
          }

          const { id } = await response.json();
          if (id) {
            window.location.replace(`${baseUrl}/s/${id}?embed=true`);
            return;
          }
        }
        
        // Fallback
        window.location.replace(fallbackUrl);
        
      } catch (err) {
        console.error("Failed to process redirect:", err);
        window.location.replace(fallbackUrl);
      }
    };

    processRedirect();
  }, [searchParams]);

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-[50vh] space-y-4">
        <div className="text-red-500 font-medium">{error}</div>
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center justify-center h-[60vh] space-y-6">
      <div className="relative flex items-center justify-center">
        <div className="absolute inset-0 bg-primary/20 blur-xl rounded-full w-24 h-24 animate-pulse" />
        <Loader2 className="w-12 h-12 text-primary animate-spin relative z-10" />
      </div>
      <div className="space-y-2 text-center">
        <h2 className="text-xl font-semibold tracking-tight text-foreground">Preparing Trial Details</h2>
        <p className="text-sm text-muted-foreground max-w-[250px] mx-auto animate-pulse">
          Loading messages and setting up your environment...
        </p>
      </div>
    </div>
  );
}

export default function RedirectPage() {
  return (
    <div className="min-h-screen bg-background text-foreground font-sans selection:bg-primary/20">
      {/* Background Gradient Effect */}
      <div className="fixed inset-0 -z-10 h-full w-full bg-background bg-[radial-gradient(#2a2a2a_1px,transparent_1px)] [background-size:16px_16px] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_70%,transparent_100%)] opacity-20 dark:opacity-40"></div>
      
      <div className="container mx-auto px-4 py-16">
        <Suspense fallback={
          <div className="flex flex-col items-center justify-center h-[60vh] space-y-6">
            <Loader2 className="w-12 h-12 text-primary animate-spin" />
            <h2 className="text-xl font-semibold text-foreground">Loading...</h2>
          </div>
        }>
          <RedirectContent />
        </Suspense>
      </div>
    </div>
  );
}
