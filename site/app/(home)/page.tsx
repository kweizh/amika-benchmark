import { Github, Terminal, ClipboardList, ListTree } from "lucide-react";
import Link from "next/link";
import tasksData from "@/zealt/tasks.json";
import pendingTasksData from "@/zealt/pending-tasks.json";
import zealtConfig from "@/zealt/config.json";
import LeaderboardTable, { type LeaderboardEntry } from "./components/leaderboard-table";

type TaskTrial = {
  agent: string;
  model: string;
  passed: boolean;
  latency_sec: number | null;
};

type TaskValue = {
  trials?: TaskTrial[];
};

type PendingTasksValue = {
  'pending-tasks'?: number;
};

export default function Home() {
  const totalTasks = Object.keys(tasksData as Record<string, unknown>).length;
  const hasTasks = Object.keys(tasksData as Record<string, unknown>).length > 0;
  const pendingSampleCases = Math.max(
    0,
    Number((pendingTasksData as PendingTasksValue)['pending-tasks'] ?? 0),
  );

  // Process tasks.json to compute leaderboard stats directly on the server
  const statsMap = new Map<string, {
    passed: number;
    total: number;
    totalLatency: number;
    latencyCount: number;
    model: string;
    agent: string;
  }>();

  Object.values(tasksData as Record<string, unknown>).forEach((taskValue) => {
    let trials: TaskTrial[] = [];
    if (Array.isArray(taskValue)) {
      trials = taskValue as TaskTrial[];
    } else if (typeof taskValue === "object" && taskValue !== null) {
      const task = taskValue as TaskValue;
      trials = Array.isArray(task.trials) ? task.trials : [];
    }

    trials.forEach((trial) => {
      // Simplify model name
      const modelName = trial.model.split('/').pop() || trial.model;
      const agentName = trial.agent.charAt(0).toUpperCase() + trial.agent.slice(1);

      const key = `${modelName}-${agentName}`;

      if (!statsMap.has(key)) {
        statsMap.set(key, {
          passed: 0,
          total: 0,
          totalLatency: 0,
          latencyCount: 0,
          model: modelName,
          agent: agentName
        });
      }

      const stats = statsMap.get(key);
      if (!stats) {
        return;
      }
      stats.total += 1;
      if (trial.passed) {
        stats.passed += 1;
      }
      if (trial.latency_sec) {
        stats.totalLatency += trial.latency_sec;
        stats.latencyCount += 1;
      }
    });
  });

  const data: LeaderboardEntry[] = Array.from(statsMap.values())
    .map((stats, index) => {
      const successRate = stats.total > 0 ? Math.round((stats.passed / stats.total) * 100) : 0;
      const avgLatency = stats.latencyCount > 0 ? stats.totalLatency / stats.latencyCount : 0;
      return {
        id: String(index + 1),
        model: stats.model,
        agent: stats.agent,
        passedEvals: stats.passed,
        successRate: successRate,
        avgLatency: avgLatency,
      };
    })
    .sort((a, b) => b.successRate - a.successRate);

  // Re-assign IDs based on sorted order and adjust isNew
  data.forEach((item, index) => {
    item.id = String(index + 1);
    item.isNew = index === 0; // Keeping the original visual effect for the top item
  });

  return (
    <div className="min-h-screen bg-background text-foreground font-sans selection:bg-primary/20">
      {/* Background Gradient Effect */}
      <div className="fixed inset-0 -z-10 h-full w-full bg-background bg-[radial-gradient(#2a2a2a_1px,transparent_1px)] [background-size:16px_16px] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_70%,transparent_100%)] opacity-20 dark:opacity-40"></div>

      <div className="container mx-auto px-4 py-16 max-w-6xl">
        {/* Header Section */}
        <div className="text-center mb-16 space-y-6">
          <div className="inline-flex items-center justify-center p-1.5 rounded-full bg-secondary/50 backdrop-blur-sm border border-border mb-4">
            <span className="flex h-2 w-2 rounded-full bg-emerald-500 mx-2 animate-pulse"></span>
            <span className="text-xs font-medium px-2">Live Benchmarks</span>
          </div>

          <h1 className="text-5xl md:text-7xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-b from-foreground to-foreground/50 pb-2">
            {zealtConfig.title}
          </h1>

          <p className="text-lg text-muted-foreground max-w-2xl mx-auto leading-relaxed">
            {zealtConfig.description}
          </p>

          <div className="flex flex-wrap items-center justify-center gap-x-6 gap-y-3 text-sm text-muted-foreground pt-4">
            <a href={zealtConfig.github_repo} target="_blank" rel="noopener noreferrer" className="flex w-full sm:w-auto items-center justify-center gap-2 hover:text-primary transition-colors">
              <Github className="w-4 h-4" />
              <span>View on GitHub</span>
            </a>
            {data.length > 0 && (
              <>
                <div className="hidden h-4 w-px bg-border sm:block"></div>
                <span className="flex w-full sm:w-auto items-center justify-center gap-2">
                  <ClipboardList className="w-4 h-4" />
                  <span>Total tasks: {totalTasks}</span>
                </span>
              </>
            )}
            <div className="hidden h-4 w-px bg-border sm:block"></div>
            <span className="flex w-full sm:w-auto items-center justify-center gap-2">
              <Terminal className="w-4 h-4" />
              <span>Last run: {new Date().toLocaleDateString()}</span>
            </span>
          </div>
        </div>

        {!hasTasks ? (
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
            <div className="relative mt-7 flex items-center justify-center">
              <a
                href="mailto:zealtdev@tabbyml.com"
                className="inline-flex items-center justify-center rounded-lg border border-border bg-card/70 px-4 py-2 text-sm font-medium text-foreground transition-colors hover:bg-secondary/60"
              >
                Contact Support
              </a>
            </div>
          </div>
        ) : data.length === 0 ? (
          <div className="rounded-2xl border border-dashed border-border bg-card/40 backdrop-blur-sm px-8 py-14 text-center">
            <h2 className="text-2xl font-semibold tracking-tight">No evaluation data yet</h2>
            <div className="mt-6 flex justify-center">
              <Link
                href="./tasks"
                className="flex items-center justify-center gap-2 px-4 py-2 border border-border bg-card/50 hover:bg-secondary/50 text-foreground rounded-lg text-sm font-medium transition-colors shadow-sm backdrop-blur-sm whitespace-nowrap"
              >
                <ListTree className="w-4 h-4" />
                View Tasks
              </Link>
            </div>
          </div>
        ) : (
          // Client Component for Interactive Table
          <LeaderboardTable data={data} />
        )}
      </div>
    </div>
  );
}
