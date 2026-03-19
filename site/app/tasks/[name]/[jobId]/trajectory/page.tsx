import type { CSSProperties } from "react";
import tasksData from "@/tasks.json";
import { TrajectoryPage } from "./components/trajectory-page";
import zealtConfig from "@/../zealt.json";
import { redirect } from "next/navigation";


type RouteParams = {
  name: string;
  jobId: string;
};

type TrialEntry = {
  trial_name: string;
  job_name: string;
  agent: string;
  latency_sec?: number | null;
  trajectory_id?: string;
  stderr_text?: string | null;
  stderr_line_count?: number;
  verifier_text?: string | null;
  verifier_line_count?: number;
};

function formatStartTime(jobName: string): string {
  const match = jobName.match(/^(\d{4})-(\d{2})-(\d{2})__(\d{2})-(\d{2})-(\d{2})$/);
  if (!match) {
    return "Unknown";
  }

  const [, year, month, day, hour, minute, second] = match;
  const localDate = new Date(Number(year), Number(month) - 1, Number(day), Number(hour), Number(minute), Number(second));
  if (Number.isNaN(localDate.getTime())) {
    return "Unknown";
  }

  return localDate.toLocaleString();
}

function formatDuration(durationSec: number | null | undefined): string {
  if (durationSec == null || Number.isNaN(durationSec)) {
    return "Unknown";
  }

  if (durationSec < 60) {
    return `${durationSec.toFixed(1)}s`;
  }

  const minutes = Math.floor(durationSec / 60);
  const seconds = durationSec % 60;
  return `${minutes}m ${seconds.toFixed(1)}s`;
}

function buildFallbackUrl(jobName: string, trialName: string) {
  return `${zealtConfig.github_repo}/blob/main/jobs/${jobName}/${trialName}/result.json`
}

function splitTrialName(trialName: string): { taskName: string; jobId: string } | null {
  const separatorIndex = trialName.lastIndexOf("__");
  if (separatorIndex <= 0 || separatorIndex >= trialName.length - 2) {
    return null;
  }

  return {
    taskName: trialName.slice(0, separatorIndex),
    jobId: trialName.slice(separatorIndex + 2),
  };
}

function getServerBaseUrl() {
  return process.env.CLIPS_BASE_URL || 'https://cc.getpochi.com';
}

function getGithubOwnerRepo(): string {
  const repoUrl = zealtConfig.github_repo;
  const match = repoUrl.match(/github\.com\/(.+?\/[^/]+)/);
  return match ? match[1] : repoUrl;
}

function buildClipUrl(jobName: string, trialName: string, title: string): string {
  const ownerRepo = getGithubOwnerRepo();
  const url = new URL(`/f/raw.githubusercontent.com/${ownerRepo}/refs/heads/main/jobs/${jobName}/${trialName}/agent/pochi/trajectory.jsonl`, getServerBaseUrl());
  url.searchParams.set("title", title);
  url.searchParams.set("theme", "dark");
  return url.toString();
}

function isTrialEntry(value: unknown): value is TrialEntry {
  if (typeof value !== "object" || value === null) {
    return false;
  }

  const trial = value as Record<string, unknown>;
  if (
    typeof trial.trial_name !== "string" ||
    typeof trial.job_name !== "string" ||
    typeof trial.agent !== "string"
  ) {
    return false;
  }

  return true;
}

function findTrialEntry(taskName: string, jobId: string): TrialEntry | null {
  for (const task of Object.values(tasksData as Record<string, unknown>)) {
    if (typeof task !== "object" || task === null) {
      continue;
    }

    const trials = (task as { trials?: unknown }).trials;
    if (!Array.isArray(trials)) {
      continue;
    }

    for (const trial of trials) {
      if (!isTrialEntry(trial)) {
        continue;
      }

      const splitName = splitTrialName(trial.trial_name);
      if (!splitName) {
        continue;
      }

      if (splitName.taskName === taskName && splitName.jobId === jobId) {
        return trial;
      }
    }
  }

  return null;
}

export const dynamicParams = false;

export function generateStaticParams(): RouteParams[] {
  const params: RouteParams[] = [];

  for (const task of Object.values(tasksData as Record<string, unknown>)) {
    if (typeof task !== "object" || task === null) {
      continue;
    }

    const trials = (task as { trials?: unknown }).trials;
    if (!Array.isArray(trials)) {
      continue;
    }

    for (const trial of trials) {
      if (!isTrialEntry(trial)) {
        continue;
      }

      const splitName = splitTrialName(trial.trial_name);
      if (!splitName) {
        continue;
      }

      params.push({
        name: splitName.taskName,
        jobId: splitName.jobId,
      });
    }
  }

  return params;
}

export default async function TrajectoryRoutePage({
  params,
}: {
  params: Promise<RouteParams>;
}) {
  const resolvedParams = await params;

  const trialEntry = findTrialEntry(resolvedParams.name, resolvedParams.jobId);
  const fallbackUrl = trialEntry
    ? buildFallbackUrl(trialEntry.job_name, trialEntry.trial_name)
    : null;
  const clipId = trialEntry?.trajectory_id?.trim() || null;
  const headerTitle = `${resolvedParams.name}__${resolvedParams.jobId}`;
  const startedAt = trialEntry ? formatStartTime(trialEntry.job_name) : "Unknown";
  const durationLabel = formatDuration(trialEntry?.latency_sec ?? null);
  const contentTopOffsetClassName = "top-28";
  
  const trajectoryUrl = clipId && trialEntry
    ? buildClipUrl(trialEntry.job_name, trialEntry.trial_name, resolvedParams.name)
    : null;
  
  // FIXME
  if (!trajectoryUrl) {
    redirect(fallbackUrl ?? '/tasks');
  }
  const stderrText = trialEntry?.stderr_text ?? null;
  const verifierText = trialEntry?.verifier_text ?? null;
  const pageThemeVars = {
    "--background": "oklch(0.268 0.004 106.643)",
    "--border": "oklch(0.362 0.01 106.893)",
  } as CSSProperties;

  return (
    <div style={pageThemeVars} className="w-full h-screen bg-background text-foreground font-sans selection:bg-primary/20 overflow-hidden">
      <div className="fixed inset-0 -z-10 h-full w-full bg-background bg-[radial-gradient(#2a2a2a_1px,transparent_1px)] [background-size:16px_16px] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_70%,transparent_100%)] opacity-20 dark:opacity-40"></div>
      <div className="fixed inset-x-0 top-0 z-40 border-b border-border/50 bg-background/85 backdrop-blur-sm">
        <div className="mx-auto w-full max-w-[1400px] px-4 py-4 sm:px-7 lg:px-10">
          <div className="flex flex-col gap-1">
            <h1 className="truncate whitespace-nowrap font-bold text-2xl">
              {headerTitle}
            </h1>
            <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-xs text-muted-foreground sm:text-sm mt-1.5">
              <span>Started: {startedAt}</span>
              <span>Duration: {durationLabel}</span>
            </div>
          </div>
        </div>
      </div>
      <TrajectoryPage
        trajectoryUrl={trajectoryUrl}
        fallbackUrl={fallbackUrl ?? ''}
        stderrText={stderrText}
        verifierText={verifierText}
        topOffsetClassName={contentTopOffsetClassName}
      />
    </div>
  );
}