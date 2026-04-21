# Parallel Code Generation with Amika

## Background
You need to automate a parallel code generation workflow using the `amika` CLI. You have a git repository at `/home/user/project`.

## Requirements
Write a bash script at `/home/user/project/run_parallel.sh` that does the following:
1. Creates two sandboxes named `feature-a` and `feature-b` from the current git repository.
2. Sends a prompt to the `feature-a` sandbox: `"Generate frontend components"`
3. Sends a prompt to the `feature-b` sandbox: `"Generate backend API"`
4. The two `agent-send` commands must be run in parallel (e.g., in the background).
5. The script must wait for both parallel agent commands to complete before exiting.

## Implementation Guide
- Use `amika sandbox create --name <name> --git` to create the sandboxes.
- Use `amika sandbox agent-send <name> "<prompt>"` to send the prompts.
- Run the `agent-send` commands in the background using `&` and use `wait` to ensure both finish.
- Ensure the script is executable (`chmod +x`).

## Constraints
- Project path: `/home/user/project`
- The script must be named `run_parallel.sh`.
