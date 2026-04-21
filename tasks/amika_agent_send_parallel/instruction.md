# Parallel Agent Execution with Amika

## Background
You have a git repository initialized at `/home/user/myproject`. You need to create multiple local sandboxes and send agent commands to them concurrently without waiting for the responses.

## Requirements
1. Create a local sandbox named `task-1` from the current git repository.
2. Create a local sandbox named `task-2` from the current git repository.
3. Use `amika sandbox agent-send` with the `--no-wait` flag to send the prompt "Implement feature A" to `task-1`.
4. Use `amika sandbox agent-send` with the `--no-wait` flag to send the prompt "Implement feature B" to `task-2`.

## Implementation Guide
1. Use `amika sandbox create --name <name> --git --local` to create the local sandboxes.
2. Use `amika sandbox agent-send <name> "<prompt>" --local --no-wait` to send the prompts.

## Constraints
- Project path: /home/user/myproject
- You must use the `--local` flag for all Amika commands to avoid requiring remote authentication.
- You must use the `--no-wait` flag for `agent-send`.