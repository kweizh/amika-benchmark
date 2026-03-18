import fs from 'fs/promises';
import path from 'path';

type TrialEntry = {
  jobName: string;
  trialName: string;
  trialDir: string;
  stdoutPath: string;
  resultLinkPath: string;
};

type UrlJsonPayload = {
  clip_id?: string;
  error?: string;
};

type TrajectoryClipEntry = {
  clip_id?: string;
  error: string | null;
};

type TrajectoryUrls = Record<string, Record<string, TrajectoryClipEntry>>;

type CheckIssue = {
  jobName: string;
  trialName: string;
  reason: string;
};

// Set to -1 for no limit; set to a positive number to cap processed trials for testing.
const MAX_TASKS = 3;
const RETRY_ATTEMPTS = 3;
const RETRY_BASE_DELAY_MS = 700;

function getServerBaseUrl() {
  return process.env.CLIPS_BASE_URL || "https://cc.getpochi.com"
}

function parseJsonLines(content: string): { messages: unknown[]; error: string | null } {
  const lines = content.split(/\r?\n/).filter((line) => line.trim().length > 0);
  if (lines.length === 0) {
    const error = 'Empty JSONL payload';
    console.error(error);
    return { messages: [], error };
  }

  const parsed: unknown[] = [];
  for (const line of lines) {
    try {
      parsed.push(JSON.parse(line));
    } catch (_e) {
      const error = 'Error parsing JSONL line';
      console.error(error);
      return { messages: [], error };
    }
  }

  return { messages: parsed, error: null };
}

async function sleep(ms: number) {
  await new Promise((resolve) => setTimeout(resolve, ms));
}

async function postClipWithRetry(
  baseUrl: string,
  messages: unknown[],
  authorizationHeaderValue: string
): Promise<{ clipId: string | null; error: string | null }> {
  const endpoint = `${baseUrl}/api/clips`;
  let lastError: string | null = null;

  for (let attempt = 1; attempt <= RETRY_ATTEMPTS; attempt++) {
    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'authorization': authorizationHeaderValue,
        },
        body: JSON.stringify({ data: { messages } }),
      });
      if (!response.ok) {
        const text = await response.text();
        throw new Error(`HTTP ${response.status}: ${text || response.statusText}`);
      }

      const json = await response.json() as { id?: string };
      if (!json.id) {
        throw new Error('Response missing clip id');
      }

      return { clipId: json.id, error: null };
    } catch (e) {
      const errorText = e instanceof Error ? e.message : String(e);
      lastError = errorText;
      console.error(`POST failed (attempt ${attempt}/${RETRY_ATTEMPTS}): ${errorText}`);
      if (attempt < RETRY_ATTEMPTS) {
        await sleep(RETRY_BASE_DELAY_MS * attempt);
      }
    }
  }

  return { clipId: null, error: lastError || 'Unknown error when posting clip' };
}

async function getTrialEntries(jobsDir: string): Promise<TrialEntry[]> {
  const entries: TrialEntry[] = [];

  const jobs = await fs.readdir(jobsDir, { withFileTypes: true });
  for (const job of jobs) {
    if (!job.isDirectory()) continue;

    const jobName = job.name;
    const jobDir = path.join(jobsDir, jobName);
    const trials = await fs.readdir(jobDir, { withFileTypes: true });

    for (const trial of trials) {
      if (!trial.isDirectory()) continue;

      const trialName = trial.name;
      const trialDir = path.join(jobDir, trialName, 'agent', 'pochi');
      const stdoutPath = path.join(trialDir, 'stdout.txt');
      const resultLinkPath = path.join(trialDir, 'result-link.json');

      try {
        await fs.access(stdoutPath);
      } catch (_e) {
        continue;
      }

      entries.push({
        jobName,
        trialName,
        trialDir,
        stdoutPath,
        resultLinkPath,
      });
    }
  }

  // Keep ordering deterministic for repeatable runs.
  entries.sort((a, b) => a.stdoutPath.localeCompare(b.stdoutPath));
  return entries;
}

function getAuthorizationHeaderValue(): string {
  const internalApiKey = process.env.INTERNAL_API_KEY?.trim();
  if (internalApiKey) {
    return `x-api-key: ${internalApiKey}`;
  }

  throw new Error('Missing environment variable INTERNAL_API_KEY');
}

function normalizePayload(payload: UrlJsonPayload): TrajectoryClipEntry | null {
  const clipId = payload.clip_id?.trim();
  const error = payload.error?.trim();
  if (!clipId && !error) {
    return null;
  }
  return {
    ...(clipId ? { clip_id: clipId } : {}),
    error: error || null,
  };
}

function setTrajectoryEntry(
  trajectoryUrls: TrajectoryUrls,
  jobName: string,
  trialName: string,
  payload: UrlJsonPayload
) {
  const normalized = normalizePayload(payload);
  if (!normalized) {
    return;
  }

  if (!trajectoryUrls[jobName]) {
    trajectoryUrls[jobName] = {};
  }
  trajectoryUrls[jobName][trialName] = normalized;
}

async function readUrlJsonPayload(urlJsonPath: string): Promise<UrlJsonPayload | null> {
  try {
    const content = await fs.readFile(urlJsonPath, 'utf-8');
    const parsed = JSON.parse(content) as UrlJsonPayload;
    if (!parsed.clip_id && !parsed.error) {
      return null;
    }
    return parsed;
  } catch (_e) {
    return null;
  }
}

async function writeUrlJson(urlJsonPath: string, payload: UrlJsonPayload): Promise<void> {
  await fs.writeFile(urlJsonPath, JSON.stringify(payload, null, 2));
}

async function readTrajectoryUrls(aggregateOutputPath: string): Promise<TrajectoryUrls> {
  try {
    const content = await fs.readFile(aggregateOutputPath, 'utf-8');
    const parsed = JSON.parse(content) as unknown;
    if (typeof parsed !== 'object' || parsed === null) {
      return {};
    }
    return parsed as TrajectoryUrls;
  } catch (_e) {
    return {};
  }
}

async function runCheckMode(entries: TrialEntry[], aggregateOutputPath: string): Promise<void> {
  const aggregate = await readTrajectoryUrls(aggregateOutputPath);
  const issues: CheckIssue[] = [];

  for (const entry of entries) {
    const payload = await readUrlJsonPayload(entry.resultLinkPath);
    if (!payload) {
      issues.push({
        jobName: entry.jobName,
        trialName: entry.trialName,
        reason: 'Missing or invalid result-link.json',
      });
      continue;
    }

    const aggregateEntry = aggregate[entry.jobName]?.[entry.trialName];
    if (!aggregateEntry) {
      issues.push({
        jobName: entry.jobName,
        trialName: entry.trialName,
        reason: 'Missing entry in trajectory.json',
      });
      continue;
    }

    const payloadClipId = payload.clip_id?.trim() || null;
    const payloadError = payload.error?.trim() || null;
    const aggregateClipId = aggregateEntry.clip_id?.trim() || null;
    const aggregateError = aggregateEntry.error?.trim() || null;

    if (payloadClipId !== aggregateClipId) {
      issues.push({
        jobName: entry.jobName,
        trialName: entry.trialName,
        reason: 'result-link.json clip_id and trajectory.json value mismatch',
      });
    }

    if (payloadError !== aggregateError) {
      issues.push({
        jobName: entry.jobName,
        trialName: entry.trialName,
        reason: 'result-link.json error and trajectory.json error mismatch',
      });
    }
  }

  if (issues.length > 0) {
    console.error(`Trajectory URL check failed with ${issues.length} issue(s):`);
    for (const issue of issues) {
      console.error(`- ${issue.jobName}/${issue.trialName}: ${issue.reason}`);
    }
    console.error('Run `bun run compute-trajectory` to regenerate trajectory link files.');
    process.exit(1);
  }

  console.log(`Trajectory URL check passed for ${entries.length} trial(s).`);
}

async function main() {
  const isCheckMode = process.argv.includes('--check');
  const isForceMode = process.argv.includes('--force');
  const jobsDir = path.join(process.cwd(), '..', 'jobs');
  const aggregateOutputPath = path.join(process.cwd(), 'trajectory.json');
  const baseUrl = getServerBaseUrl();
  console.log(`Post clips to ${baseUrl}`)
  let authorizationHeaderValue: string | null = null;

  let entries: TrialEntry[] = [];
  try {
    entries = await getTrialEntries(jobsDir);
  } catch (e) {
    console.error(`Error scanning jobs dir ${jobsDir}:`, e);
    process.exit(1);
  }

  if (isCheckMode) {
    await runCheckMode(entries, aggregateOutputPath);
    return;
  }

  let processed = 0;
  const trajectoryUrls: TrajectoryUrls = {};

  for (const entry of entries) {
    const existingPayload = isForceMode ? null : await readUrlJsonPayload(entry.resultLinkPath);
    const existingClipId = existingPayload?.clip_id || null;
    const existingError = existingPayload?.error?.trim();
    const shouldSkip = !isForceMode && !!existingClipId && !existingError;

    if (shouldSkip) {
      console.log(`Skip existing ${path.relative(jobsDir, entry.resultLinkPath)}`);
      setTrajectoryEntry(trajectoryUrls, entry.jobName, entry.trialName, {
        clip_id: existingClipId,
      });
      continue;
    }

    if (!isForceMode && existingClipId && existingError) {
      console.log(`Regenerate due to existing error ${path.relative(jobsDir, entry.resultLinkPath)}`);
    }

    if (isForceMode) {
      console.log(`Force regenerate ${path.relative(jobsDir, entry.resultLinkPath)}`);
    }

    if (MAX_TASKS >= 0 && processed >= MAX_TASKS) {
      continue;
    }

    let content = '';
    try {
      content = await fs.readFile(entry.stdoutPath, 'utf-8');
    } catch (e) {
      const errorText = `Error reading ${entry.stdoutPath}: ${e instanceof Error ? e.message : String(e)}`;
      console.error(errorText);
      await fs.mkdir(entry.trialDir, { recursive: true });
      await writeUrlJson(entry.resultLinkPath, { error: errorText });
      processed++;
      continue;
    }

    const { messages, error: parseError } = parseJsonLines(content);
    let clipIdToWrite: string | undefined;
    let errorMessage: string | undefined;

    if (parseError) {
      errorMessage = parseError;
    }

    if (messages.length > 0) {
      if (!authorizationHeaderValue) {
        authorizationHeaderValue = getAuthorizationHeaderValue();
      }
      const { clipId, error } = await postClipWithRetry(baseUrl, messages, authorizationHeaderValue);
      if (clipId) {
        clipIdToWrite = clipId;
        errorMessage = undefined;
      } else if (error) {
        errorMessage = `Post clip failed: ${error}`;
      }
    }

    await fs.mkdir(entry.trialDir, { recursive: true });
    await writeUrlJson(
      entry.resultLinkPath,
      errorMessage
        ? { clip_id: clipIdToWrite, error: errorMessage }
        : (clipIdToWrite ? { clip_id: clipIdToWrite } : { error: 'No valid messages to post' })
    );

    setTrajectoryEntry(trajectoryUrls, entry.jobName, entry.trialName, {
      clip_id: clipIdToWrite,
      error: errorMessage,
    });

    console.log(`Wrote ${path.relative(jobsDir, entry.resultLinkPath)}`);

    processed++;
  }

  await fs.writeFile(aggregateOutputPath, JSON.stringify(trajectoryUrls, null, 2));

  console.log(`Processed ${processed} trial(s).`);
  console.log(`Wrote aggregated URLs to ${aggregateOutputPath}.`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
