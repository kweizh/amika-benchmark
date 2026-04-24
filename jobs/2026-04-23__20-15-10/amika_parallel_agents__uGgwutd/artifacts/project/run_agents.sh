#!/usr/bin/env bash
# run_agents.sh
# Spins up two Amika sandboxes in parallel, sends a code-gen task to each,
# and waits for both to finish before exiting.

set -euo pipefail

# ---------------------------------------------------------------------------
# 1. Create the two sandboxes from the current git repository
# ---------------------------------------------------------------------------
echo "[*] Creating sandbox: task-1"
amika sandbox create --name task-1 --git

echo "[*] Creating sandbox: task-2"
amika sandbox create --name task-2 --git

# ---------------------------------------------------------------------------
# 2. Send prompts to each sandbox in parallel (background jobs)
# ---------------------------------------------------------------------------
echo "[*] Sending agent task to task-1 (background)..."
amika sandbox agent-send task-1 "Create a file named hello.txt containing exactly 'Hello from task 1'" &
PID_TASK1=$!

echo "[*] Sending agent task to task-2 (background)..."
amika sandbox agent-send task-2 "Create a file named hello.txt containing exactly 'Hello from task 2'" &
PID_TASK2=$!

# ---------------------------------------------------------------------------
# 3. Wait for both background jobs to complete
# ---------------------------------------------------------------------------
echo "[*] Waiting for both agent tasks to complete..."

FAILED=0

wait "$PID_TASK1" || { echo "[!] task-1 agent-send failed"; FAILED=1; }
wait "$PID_TASK2" || { echo "[!] task-2 agent-send failed"; FAILED=1; }

if [ "$FAILED" -eq 1 ]; then
    echo "[✗] One or more agent tasks failed."
    exit 1
fi

echo "[✓] Both agent tasks completed successfully."
exit 0
