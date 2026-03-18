import tasksData from "@/tasks.json";
import trajectoryUrls from "@/trajectory.json";
import { TrajectoryPage } from "./components/trajectory-page";
import zealtConfig from "@/../zealt.json";


type RouteParams = {
  name: string;
  jobName: string;
};

type TrialEntry = {
  trial_name: string;
  job_name: string;
};

function buildFallbackUrl(jobName: string, trialName: string) {
  return `${zealtConfig.github_repo}/blob/main/jobs/${jobName}/${trialName}/result.json`
}

function getServerBaseUrl() {
  return process.env.CLIPS_BASE_URL || 'https://cc.getpochi.com';
}

function buildClipUrl(clipId: string, title: string): string {
  const url = new URL(`/e/${clipId}`, getServerBaseUrl());
  url.searchParams.set("title", title);
  url.searchParams.set("theme", "dark");
  return url.toString();
}

function getTrajectoryEntry(jobName: string, trialName: string) {
  const urlsByJob = trajectoryUrls as Record<
    string,
    Record<string, { clip_id?: string; error: string | null }> | undefined
  >;
  return urlsByJob[jobName]?.[trialName] || null;
}

function isTrialEntry(value: unknown): value is TrialEntry {
  if (typeof value !== "object" || value === null) {
    return false;
  }

  const trial = value as Record<string, unknown>;
  return typeof trial.trial_name === "string" && typeof trial.job_name === "string";
}

export const dynamicParams = false;

export function generateStaticParams(): RouteParams[] {
  const params: RouteParams[] = [];

  for (const trials of Object.values(tasksData as Record<string, unknown>)) {
    if (!Array.isArray(trials)) {
      continue;
    }

    for (const trial of trials) {
      if (!isTrialEntry(trial)) {
        continue;
      }

      params.push({
        name: trial.trial_name,
        jobName: trial.job_name,
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
  const fallbackUrl = buildFallbackUrl(resolvedParams.jobName, resolvedParams.name);
  const trajectoryEntry = getTrajectoryEntry(resolvedParams.jobName, resolvedParams.name);
  const clipId = trajectoryEntry?.clip_id || null;
  const trajectoryUrl = clipId ? buildClipUrl(clipId, resolvedParams.name) : null;

  return (
    <div className="w-full h-screen bg-background text-foreground font-sans selection:bg-primary/20 overflow-hidden">
      <div className="fixed inset-0 -z-10 h-full w-full bg-background bg-[radial-gradient(#2a2a2a_1px,transparent_1px)] [background-size:16px_16px] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_70%,transparent_100%)] opacity-20 dark:opacity-40"></div>
      <TrajectoryPage
        title={resolvedParams.name}
        trajectoryUrl={trajectoryUrl}
        fallbackUrl={fallbackUrl}
      />
    </div>
  );
}