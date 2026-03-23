import tasksDataRaw from "@/zealt/tasks.json";
import pendingTasksData from "@/zealt/pending-tasks.json";
import { TasksPageClient, type CompactTask, type CompactTrial } from "./components/tasks-page-client";

type RawTaskTrial = {
  job_name?: string;
  trial_name?: string;
  trajectory_id?: string;
  agent?: string;
  model?: string;
  passed?: boolean;
  reward?: number | null;
  error?: boolean;
  latency_sec?: number | null;
  latency_breakdown?: {
    env_setup?: number | null;
    agent_setup?: number | null;
    agent_exec?: number | null;
    verifier?: number | null;
  };
};

type RawTaskRecord = {
  instruction?: string;
  trials?: RawTaskTrial[];
};

type PendingTasksValue = {
  'pending-tasks'?: number;
};

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

function toCompactTrial(taskName: string, trial: RawTaskTrial): CompactTrial | null {
  if (!trial.job_name || !trial.trial_name || !trial.model || !trial.agent) {
    return null;
  }

  const splitName = splitTrialName(trial.trial_name);
  const derivedTaskName = splitName?.taskName || taskName;
  const jobId = splitName?.jobId || trial.job_name;
  const model = trial.model.split("/").pop() || trial.model;
  const agent = trial.agent ? trial.agent.charAt(0).toUpperCase() + trial.agent.slice(1) : "Unknown";
  const latencyBreakdown = {
    env_setup: trial.latency_breakdown?.env_setup ?? null,
    agent_setup: trial.latency_breakdown?.agent_setup ?? null,
    agent_exec: trial.latency_breakdown?.agent_exec ?? null,
    verifier: trial.latency_breakdown?.verifier ?? null,
  };

  return {
    job_name: trial.job_name,
    trial_name: trial.trial_name,
    ...(trial.trajectory_id ? { trajectory_id: trial.trajectory_id } : {}),
    model,
    agent,
    passed: Boolean(trial.passed),
    reward: trial.reward ?? null,
    error: Boolean(trial.error),
    latency_sec: trial.latency_sec ?? null,
    latency_breakdown: latencyBreakdown,
    taskName: derivedTaskName,
    jobId,
    exec_duration: latencyBreakdown.agent_exec ?? trial.latency_sec ?? 0,
  };
}

function buildCompactTasksData(): CompactTask[] {
  const rawEntries = Object.entries(tasksDataRaw as Record<string, unknown>);
  const compactTasks: CompactTask[] = [];

  for (const [taskName, value] of rawEntries) {
    if (typeof value !== "object" || value === null) {
      continue;
    }

    const taskRecord = value as RawTaskRecord;
    const rawTrials = Array.isArray(taskRecord.trials) ? taskRecord.trials : [];
    const trials: CompactTrial[] = rawTrials
      .map((trial) => toCompactTrial(taskName, trial))
      .filter((trial): trial is CompactTrial => trial !== null);

    compactTasks.push({
      taskName,
      instruction: taskRecord.instruction || "",
      trials,
    });
  }

  compactTasks.sort((a, b) => a.taskName.localeCompare(b.taskName));
  return compactTasks;
}

export default function TasksPage() {
  const compactTasksData = buildCompactTasksData();
  const pendingSampleCases = Math.max(
    0,
    Number((pendingTasksData as PendingTasksValue)['pending-tasks'] ?? 0),
  );

  return (
    <div className="min-h-screen bg-background text-foreground font-sans selection:bg-primary/20">
      <div className="fixed inset-0 -z-10 h-full w-full bg-background bg-[radial-gradient(#2a2a2a_1px,transparent_1px)] [background-size:16px_16px] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_70%,transparent_100%)] opacity-20 dark:opacity-40"></div>

      {compactTasksData.length === 0 ? (
        <div className="container mx-auto px-4 sm:px-8 lg:px-12 py-8 max-w-screen-2xl h-[100dvh] flex flex-col overflow-hidden">
          <div className="mb-6 space-y-4 shrink-0">
            <div className="flex items-center gap-4">
              <a href="/" className="text-sm text-muted-foreground hover:text-foreground transition-colors">
                &larr; Back to Leaderboard
              </a>
            </div>
            <div>
              <h1 className="text-4xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-b from-foreground to-foreground/50">
                Task
              </h1>
            </div>
          </div>

          <div className="relative overflow-hidden rounded-2xl border border-primary/30 bg-gradient-to-br from-primary/10 via-card/90 to-background/90 px-8 py-14 text-center shadow-[0_0_0_1px_hsl(var(--primary)/0.18),0_28px_72px_-32px_hsl(var(--foreground)/0.45)] backdrop-blur-sm">
            <div className="pointer-events-none absolute -right-14 -top-14 h-40 w-40 rounded-full bg-primary/20 blur-3xl" />
            <div className="pointer-events-none absolute -left-20 bottom-0 h-36 w-36 rounded-full bg-foreground/10 blur-3xl" />
            <div className="relative mx-auto mb-4 inline-flex items-center rounded-full border border-primary/40 bg-primary/15 px-3 py-1 text-xs font-semibold tracking-[0.16em] text-foreground">
              🚀 PIPELINE IN PROGRESS
            </div>
            <h2 className="relative text-2xl md:text-[1.75rem] font-semibold tracking-tight text-foreground">
              Generated {pendingSampleCases} sample cases.
            </h2>
            <p className="relative mx-auto mt-4 max-w-2xl text-sm leading-relaxed text-muted-foreground">
              Great progress. This stage is complete, and you are very close to a full evaluation result. Continue the remaining steps to finish the workflow.
            </p>
            <p className="relative mt-2 text-sm text-muted-foreground">
              Need help with data processing or evaluation execution? Contact {" "}
              <a
                href="mailto:zealtdev@tabbyml.com"
                className="font-medium text-foreground underline decoration-primary/60 underline-offset-4 hover:text-primary transition-colors"
              >
                zealtdev@tabbyml.com
              </a>
              .
            </p>
            <div className="relative mt-7 flex flex-wrap items-center justify-center gap-3">
              <a
                href="mailto:zealtdev@tabbyml.com"
                className="inline-flex items-center justify-center rounded-lg border border-border bg-card/70 px-4 py-2 text-sm font-medium text-foreground transition-colors hover:bg-secondary/60"
              >
                Contact Support
              </a>
            </div>
          </div>
        </div>
      ) : (
        <TasksPageClient tasksData={compactTasksData} />
      )}
    </div>
  );
}
