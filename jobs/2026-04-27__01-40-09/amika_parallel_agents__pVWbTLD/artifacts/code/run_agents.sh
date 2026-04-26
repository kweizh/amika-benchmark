#!/bin/bash

# Create sandboxes
amika sandbox create --name task-1 --git
amika sandbox create --name task-2 --git

# Send agent tasks in parallel
amika sandbox agent-send task-1 "Create a file named hello.txt containing exactly 'Hello from task 1'" &
amika sandbox agent-send task-2 "Create a file named hello.txt containing exactly 'Hello from task 2'" &

# Wait for both background jobs to finish
wait
