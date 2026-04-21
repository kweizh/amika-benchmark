# Parallel Code-Gen with Amika Sandboxes

## Background
Amika allows spinning up multiple sandboxes to run agents on different tasks simultaneously. You need to create a script that automates the creation of two separate sandboxes from the current repository, sends a unique code-generation task to each using `amika sandbox agent-send`, and waits for both tasks to complete.

## Requirements
- Initialize an Amika repository configuration in `/home/user/project`.
- Write a bash script `/home/user/project/run_agents.sh` that:
  1. Creates two sandboxes named `task-1` and `task-2` from the current git repository.
  2. Sends a prompt to `task-1` to create a file `hello.txt` containing "Hello from task 1".
  3. Sends a prompt to `task-2` to create a file `hello.txt` containing "Hello from task 2".
  4. Runs these agent tasks in parallel.
  5. Waits for both agent tasks to complete.

## Implementation Guide
1. Navigate to `/home/user/project` and initialize a git repository if one does not exist.
2. Create a basic `.amika/config.toml` file.
3. Create `run_agents.sh` with the required commands.
   - Use `amika sandbox create --name task-1 --git` and `amika sandbox create --name task-2 --git`.
   - Use `amika sandbox agent-send task-1 "Create a file named hello.txt containing exactly 'Hello from task 1'" &` to run in background.
   - Use `amika sandbox agent-send task-2 "Create a file named hello.txt containing exactly 'Hello from task 2'" &` to run in background.
   - Use `wait` to ensure the script blocks until both background jobs finish.
4. Make the script executable with `chmod +x run_agents.sh`.

## Constraints
- Project path: `/home/user/project`
- The script must use `&` and `wait` to run the `agent-send` commands in parallel.
- The script must exit with a 0 status code upon successful completion of both agents.