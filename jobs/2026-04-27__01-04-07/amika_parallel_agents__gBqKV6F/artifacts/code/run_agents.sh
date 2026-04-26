#!/bin/bash
set -e

# Create sandboxes
amika sandbox create --name task-1 --git
amika sandbox create --name task-2 --git

# Send tasks in parallel
amika sandbox agent-send task-1 "Create a file named hello.txt containing exactly 'Hello from task 1'" &
PID1=$!

amika sandbox agent-send task-2 "Create a file named hello.txt containing exactly 'Hello from task 2'" &
PID2=$!

# Wait for both tasks to complete
wait $PID1
wait $PID2

echo "Both agents completed successfully."
exit 0
