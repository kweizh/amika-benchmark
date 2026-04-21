# Amika Agent Send

## Background
Amika is an infrastructure tool for building software factories, providing sandboxes for coding agents. You need to write a shell script that uses the Amika CLI to send a prompt to an agent inside a sandbox.

## Requirements
- Create a bash script named `run_agent.sh`.
- The script must use the `amika sandbox agent-send` command to send a prompt to a sandbox named `dev-sandbox`.
- The prompt to send is `"Please update the README.md with deployment instructions"`.
- The script must be executable.

## Implementation Guide
1. Create the file `/home/user/project/run_agent.sh`.
2. Add the appropriate shebang (`#!/bin/bash`).
3. Add the `amika sandbox agent-send` command with the correct sandbox name and prompt.
4. Make the script executable using `chmod +x`.

## Constraints
- Project path: /home/user/project
- The sandbox name must be exactly `dev-sandbox`.
- The prompt must be exactly `"Please update the README.md with deployment instructions"`.
