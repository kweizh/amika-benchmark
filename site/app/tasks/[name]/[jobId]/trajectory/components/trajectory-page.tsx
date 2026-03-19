"use client";

import { useEffect, useRef, useState } from "react";
import { Check, Copy, Loader2 } from "lucide-react";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Button } from "@/components/ui/button";

type TrajectoryPageProps = {
  trajectoryUrl: string;
  fallbackUrl: string;
  stderrText: string | null;
  verifierText: string | null;
  topOffsetClassName?: string;
};

export function TrajectoryPage({
  trajectoryUrl,
  fallbackUrl,
  stderrText,
  verifierText,
  topOffsetClassName = "top-28",
}: TrajectoryPageProps) {
  const [iframeLoading, setIframeLoading] = useState(false);
  const [activeTab, setActiveTab] = useState("trajectory");
  const [copiedTab, setCopiedTab] = useState<"log" | "test" | null>(null);
  const iframeRef = useRef<HTMLIFrameElement>(null);

  useEffect(() => {
    setIframeLoading(true);
  }, [trajectoryUrl]);

  useEffect(() => {
    if (!copiedTab) {
      return;
    }

    const timer = window.setTimeout(() => {
      setCopiedTab(null);
    }, 1200);

    return () => window.clearTimeout(timer);
  }, [copiedTab]);

  const handleIframeLoad = () => {
    setIframeLoading(false);
    setTimeout(() => {
      if (iframeRef.current) {
        iframeRef.current.style.opacity = "1";
      }
    }, 300);
  };

  const handleIframeError = () => {
    window.location.replace(fallbackUrl);
  };

  const copyActiveLog = async () => {
    const targetText = activeTab === "log" ? stderrText : verifierText;
    if (!targetText) {
      return;
    }

    await navigator.clipboard.writeText(targetText);
    setCopiedTab(activeTab === "log" ? "log" : "test");
  };

  const renderLogContent = (text: string | null, emptyMessage: string) => {
    if (!text) {
      return <p className="text-sm text-muted-foreground">{emptyMessage}</p>;
    }

    return (
      <pre className="whitespace-pre-wrap wrap-break-word font-mono text-xs leading-5 text-foreground/95">
        {text}
      </pre>
    );
  };

  return (
    <div className="fixed inset-0 w-full h-full">
      <div className={`absolute inset-x-0 bottom-0 ${topOffsetClassName} pb-4 sm:pb-6`}>
        <div className="mx-auto h-full w-full max-w-[1400px] px-4 sm:px-7 lg:px-10">
          <Tabs value={activeTab} onValueChange={setActiveTab} className="h-full rounded-xl border border-border/60 bg-background/70 backdrop-blur-sm shadow-sm">
            <div className="border-b border-border/50 bg-background/50 px-3 py-3 sm:px-4">
              <div className="flex flex-col gap-2 md:flex-row md:items-center md:justify-between">
                <TabsList className="grid h-11 w-[300px] max-w-full grid-cols-3 items-stretch border border-border/40 bg-background/60 p-1">
                <TabsTrigger
                  value="trajectory"
                  className="h-full w-full cursor-pointer border border-transparent py-0 leading-none text-muted-foreground transition-colors hover:bg-primary/10 hover:text-foreground data-[state=active]:border-primary/35 data-[state=active]:bg-primary/18 data-[state=active]:text-foreground data-[state=active]:shadow-none"
                >
                  Trajectory
                </TabsTrigger>
                <TabsTrigger
                  value="log"
                  className="h-full w-full cursor-pointer border border-transparent py-0 leading-none text-muted-foreground transition-colors hover:bg-primary/10 hover:text-foreground data-[state=active]:border-primary/35 data-[state=active]:bg-primary/18 data-[state=active]:text-foreground data-[state=active]:shadow-none"
                >
                  Log
                </TabsTrigger>
                <TabsTrigger
                  value="test"
                  className="h-full w-full cursor-pointer border border-transparent py-0 leading-none text-muted-foreground transition-colors hover:bg-primary/10 hover:text-foreground data-[state=active]:border-primary/35 data-[state=active]:bg-primary/18 data-[state=active]:text-foreground data-[state=active]:shadow-none"
                >
                  Test
                </TabsTrigger>
                </TabsList>

                {activeTab !== "trajectory" && (
                  <div className="flex items-center gap-2">
                    <Button
                      type="button"
                      variant="outline"
                      size="sm"
                      className="h-8"
                      onClick={copyActiveLog}
                      disabled={activeTab === "log" ? !stderrText : activeTab === "test" ? !verifierText : true}
                    >
                      {copiedTab === activeTab ? <Check className="h-3.5 w-3.5" /> : <Copy className="h-3.5 w-3.5" />}
                      {copiedTab === activeTab ? "Copied" : "Copy"}
                    </Button>
                  </div>
                )}
              </div>
            </div>

            <TabsContent value="trajectory" className="relative h-[calc(100%-64px)] overflow-hidden" forceMount>
              {iframeLoading && (
                <div className="absolute inset-0 z-10 flex flex-col items-center justify-center space-y-6 bg-background/80 backdrop-blur-sm">
                  <div className="relative flex items-center justify-center">
                    <Loader2 className="w-12 h-12 text-primary animate-spin relative z-10" />
                  </div>
                  <div className="space-y-2 text-center">
                    <h2 className="text-lg font-semibold tracking-tight text-foreground">Loading</h2>
                  </div>
                </div>
              )}
              <iframe
                ref={iframeRef}
                src={trajectoryUrl}
                className="h-full w-full border-0 opacity-0 transition-opacity duration-300"
                title="Trial Details"
                onLoad={handleIframeLoad}
                onError={handleIframeError}
              />
            </TabsContent>

            <TabsContent value="log" className="h-[calc(100%-64px)] overflow-auto px-3 pb-3 sm:px-4 sm:pb-4" forceMount>
              <div className="pt-2 sm:pt-3">
                {renderLogContent(stderrText, "No stderr content available for this trial.")}
              </div>
            </TabsContent>

            <TabsContent value="test" className="h-[calc(100%-64px)] overflow-auto px-3 pb-3 sm:px-4 sm:pb-4" forceMount>
              <div className="pt-2 sm:pt-3">
                {renderLogContent(verifierText, "No verifier test output available for this trial.")}
              </div>
            </TabsContent>
          </Tabs>
        </div>
      </div>
    </div>
  );
}