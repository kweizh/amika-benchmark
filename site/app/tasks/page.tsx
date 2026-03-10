import { CheckCircle2, Clock, XCircle, Terminal } from "lucide-react";
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface Task {
  id: string;
  name: string;
  description: string;
  status: "completed" | "in-progress" | "failed";
  duration: string;
}

const mockTasks: Task[] = [
  {
    id: "task-1",
    name: "jj_abandon_wip_revisions_revsets",
    description: "Abandon work-in-progress revisions using revsets",
    status: "completed",
    duration: "45s",
  },
  {
    id: "task-2",
    name: "jj_amend_working_copy",
    description: "Amend the current working copy with new changes",
    status: "completed",
    duration: "12s",
  },
  {
    id: "task-3",
    name: "jj_bookmark_sync_conflict",
    description: "Resolve conflicts when synchronizing bookmarks",
    status: "in-progress",
    duration: "2m 15s",
  },
  {
    id: "task-4",
    name: "jj_conflict_abandon_conflicted",
    description: "Abandon a conflicted commit and restore previous state",
    status: "failed",
    duration: "1m 30s",
  },
  {
    id: "task-5",
    name: "jj_git_remote_migration",
    description: "Migrate a repository to use Git remotes",
    status: "completed",
    duration: "58s",
  },
];

function StatusIcon({ status }: { status: Task["status"] }) {
  switch (status) {
    case "completed":
      return <CheckCircle2 className="w-5 h-5 text-emerald-500" />;
    case "in-progress":
      return <Clock className="w-5 h-5 text-blue-500 animate-pulse" />;
    case "failed":
      return <XCircle className="w-5 h-5 text-red-500" />;
  }
}

function StatusBadge({ status }: { status: Task["status"] }) {
  switch (status) {
    case "completed":
      return (
        <span className="px-2 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-500 border border-emerald-500/20">
          Completed
        </span>
      );
    case "in-progress":
      return (
        <span className="px-2 py-1 rounded-full text-xs font-medium bg-blue-500/10 text-blue-500 border border-blue-500/20">
          In Progress
        </span>
      );
    case "failed":
      return (
        <span className="px-2 py-1 rounded-full text-xs font-medium bg-red-500/10 text-red-500 border border-red-500/20">
          Failed
        </span>
      );
  }
}

export default function TasksPage() {
  return (
    <div className="min-h-screen bg-background text-foreground font-sans selection:bg-primary/20">
      {/* Background Gradient Effect */}
      <div className="fixed inset-0 -z-10 h-full w-full bg-background bg-[radial-gradient(#2a2a2a_1px,transparent_1px)] [background-size:16px_16px] [mask-image:radial-gradient(ellipse_50%_50%_at_50%_50%,#000_70%,transparent_100%)] opacity-20 dark:opacity-40"></div>

      <div className="container mx-auto px-4 py-16 max-w-6xl">
        {/* Header Section */}
        <div className="mb-12 space-y-4">
          <div className="inline-flex items-center justify-center p-1.5 rounded-full bg-secondary/50 backdrop-blur-sm border border-border mb-2">
            <span className="flex h-2 w-2 rounded-full bg-blue-500 mx-2"></span>
            <span className="text-xs font-medium px-2">Task Execution</span>
          </div>

          <h1 className="text-4xl md:text-5xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-b from-foreground to-foreground/50 pb-2">
            Benchmark Tasks
          </h1>

          <p className="text-lg text-muted-foreground max-w-2xl leading-relaxed">
            Detailed view of individual Jujutsu tasks, their descriptions, and execution status.
          </p>
        </div>

        {/* Tasks List */}
        <div className="space-y-4">
          {mockTasks.map((task) => (
            <div
              key={task.id}
              className="p-6 rounded-xl border border-border bg-card/50 backdrop-blur-sm shadow-sm hover:bg-secondary/20 transition-colors duration-200 flex flex-col sm:flex-row sm:items-center justify-between gap-4"
            >
              <div className="flex items-start gap-4">
                <div className="mt-1">
                  <StatusIcon status={task.status} />
                </div>
                <div>
                  <h3 className="text-lg font-semibold text-foreground flex items-center gap-2">
                    {task.name}
                  </h3>
                  <p className="text-sm text-muted-foreground mt-1">
                    {task.description}
                  </p>
                  <div className="flex items-center gap-4 mt-3 sm:hidden">
                    <StatusBadge status={task.status} />
                    <span className="text-xs text-muted-foreground flex items-center gap-1">
                      <Terminal className="w-3 h-3" />
                      {task.duration}
                    </span>
                  </div>
                </div>
              </div>

              <div className="hidden sm:flex items-center gap-6">
                <span className="text-sm text-muted-foreground flex items-center gap-1.5 font-mono">
                  <Terminal className="w-4 h-4" />
                  {task.duration}
                </span>
                <div className="w-24 flex justify-end">
                  <StatusBadge status={task.status} />
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
