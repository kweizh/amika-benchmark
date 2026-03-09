import { Github, ChevronDown, Trophy, Search, Filter, ArrowUpRight, Terminal } from "lucide-react";
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface LeaderboardEntry {
  id: string;
  model: string;
  agent: string;
  totalEvals: number;
  successRate: number;
  successRateWithDocs: number;
  isNew?: boolean;
}

const data: LeaderboardEntry[] = [
  { id: "1", model: "GPT 5.3 Codex (xhigh)", agent: "Codex", totalEvals: 20, successRate: 90, successRateWithDocs: 100, isNew: true },
  { id: "2", model: "Claude Opus 4.6", agent: "Claude Code", totalEvals: 20, successRate: 75, successRateWithDocs: 100 },
  { id: "3", model: "Gemini 3.0 Pro Preview", agent: "OpenCode", totalEvals: 20, successRate: 75, successRateWithDocs: 90 },
  { id: "4", model: "Claude Sonnet 4.6", agent: "Claude Code", totalEvals: 20, successRate: 70, successRateWithDocs: 100 },
  { id: "5", model: "Gemini 3.0 Pro Preview", agent: "Gemini CLI", totalEvals: 20, successRate: 70, successRateWithDocs: 90 },
  { id: "6", model: "Cursor Composer 1.5", agent: "Cursor", totalEvals: 20, successRate: 65, successRateWithDocs: 95 },
  { id: "7", model: "Claude Sonnet 4.5", agent: "Claude Code", totalEvals: 20, successRate: 60, successRateWithDocs: 85 },
  { id: "8", model: "GPT 5.2 Codex (xhigh)", agent: "Codex", totalEvals: 20, successRate: 55, successRateWithDocs: 85 },
];

function ProgressBar({ value, colorClass }: { value: number; colorClass: string }) {
  return (
    <div className="h-2 w-24 bg-secondary rounded-full overflow-hidden">
      <div 
        className={cn("h-full transition-all duration-500 ease-out", colorClass)} 
        style={{ width: `${value}%` }} 
      />
    </div>
  );
}

function ScoreCell({ value, highlight = false }: { value: number; highlight?: boolean }) {
  let colorClass = "bg-primary";
  let textClass = "text-muted-foreground";
  
  if (value >= 90) {
    colorClass = "bg-emerald-500";
    textClass = "text-emerald-500 font-bold";
  } else if (value >= 75) {
    colorClass = "bg-blue-500";
    textClass = "text-blue-500 font-medium";
  } else if (value >= 60) {
    colorClass = "bg-amber-500";
    textClass = "text-amber-500";
  } else {
    colorClass = "bg-red-500";
    textClass = "text-red-500";
  }

  if (highlight) {
    // Override for the highlighted column if needed, or keep logic
  }

  return (
    <div className="flex items-center gap-3">
      <span className={cn("w-12 text-right", textClass)}>{value}%</span>
      <ProgressBar value={value} colorClass={colorClass} />
    </div>
  );
}

export default function Home() {
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
            SuperSDK Agent Benchmark
          </h1>
          
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto leading-relaxed">
            Performance results of AI coding agents on SuperSDK integration and usage tasks, 
            measuring success rate and execution time with high precision.
          </p>

          <div className="flex items-center justify-center gap-6 text-sm text-muted-foreground pt-4">
            <a href="#" className="flex items-center gap-2 hover:text-primary transition-colors">
              <Github className="w-4 h-4" />
              <span>View on GitHub</span>
            </a>
            <div className="h-4 w-px bg-border"></div>
            <span className="flex items-center gap-2">
              <Terminal className="w-4 h-4" />
              <span>Last run: February 18, 2026</span>
            </span>
          </div>
        </div>

        {/* Controls & Filters */}
        <div className="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
          <h2 className="text-2xl font-semibold flex items-center gap-2">
            Agent Performance
            <span className="text-xs font-normal text-muted-foreground bg-secondary px-2 py-1 rounded-md border border-border">
              v2.4
            </span>
          </h2>
          
          <div className="flex items-center gap-3">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted-foreground" />
              <input 
                type="text" 
                placeholder="Search agents..." 
                className="pl-9 pr-4 py-2 bg-card border border-border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary/20 w-64"
              />
            </div>
            <button className="flex items-center gap-2 px-4 py-2 bg-card border border-border rounded-lg text-sm hover:bg-secondary transition-colors">
              <Filter className="w-4 h-4" />
              <span>Filters</span>
            </button>
            <button className="flex items-center gap-2 px-4 py-2 bg-primary text-primary-foreground rounded-lg text-sm hover:bg-primary/90 transition-colors shadow-lg shadow-primary/20">
              <span>Show All Agents</span>
              <ChevronDown className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* Leaderboard Table */}
        <div className="rounded-xl border border-border bg-card/50 backdrop-blur-sm shadow-xl overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-sm text-left">
              <thead className="bg-secondary/50 text-muted-foreground font-medium border-b border-border">
                <tr>
                  <th className="px-6 py-4 w-[30%]">Model</th>
                  <th className="px-6 py-4 w-[15%]">Agent</th>
                  <th className="px-6 py-4 w-[10%] text-center">Total Evals</th>
                  <th className="px-6 py-4 w-[20%]">Success Rate</th>
                  <th className="px-6 py-4 w-[25%]">
                    <div className="flex items-center gap-1 cursor-help group relative w-fit">
                      Success with Docs
                      <div className="absolute left-0 bottom-full mb-2 hidden group-hover:block w-48 p-2 bg-popover text-popover-foreground text-xs rounded shadow-lg border border-border z-10">
                        Pass rate when agents had access to bundled SuperSDK documentation.
                      </div>
                    </div>
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border/50">
                {data.map((row, index) => (
                  <tr 
                    key={row.id} 
                    className="group hover:bg-secondary/30 transition-colors duration-200"
                  >
                    <td className="px-6 py-4 font-medium text-foreground flex items-center gap-3">
                      <span className="w-6 text-muted-foreground/50 text-xs">#{index + 1}</span>
                      <div className="flex flex-col">
                        <span className="flex items-center gap-2">
                          {row.model}
                          {index === 0 && <Trophy className="w-3 h-3 text-yellow-500" />}
                          {row.isNew && (
                            <span className="px-1.5 py-0.5 rounded text-[10px] font-bold bg-blue-500/10 text-blue-500 border border-blue-500/20">
                              NEW
                            </span>
                          )}
                        </span>
                      </div>
                    </td>
                    <td className="px-6 py-4 text-muted-foreground">
                      <div className="flex items-center gap-2">
                        <div className="w-6 h-6 rounded-full bg-secondary flex items-center justify-center text-[10px] font-bold border border-border">
                          {row.agent.substring(0, 1)}
                        </div>
                        {row.agent}
                      </div>
                    </td>
                    <td className="px-6 py-4 text-center text-muted-foreground font-mono">
                      {row.totalEvals}
                    </td>
                    <td className="px-6 py-4">
                      <ScoreCell value={row.successRate} />
                    </td>
                    <td className="px-6 py-4">
                      <ScoreCell value={row.successRateWithDocs} highlight />
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          
          {/* Table Footer */}
          <div className="px-6 py-4 border-t border-border bg-secondary/20 text-xs text-muted-foreground flex justify-between items-center">
            <p>* AGENTS.md provides bundled SuperSDK documentation for AI coding agents.</p>
            <button className="flex items-center gap-1 hover:text-foreground transition-colors">
              Full Methodology <ArrowUpRight className="w-3 h-3" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
