# Amika Agent Send

## Background
Amika is infrastructure for building software factories. It provides managed, multiplayer sandboxes pre-loaded with coding agents. You need to create a sandbox and send a prompt to an agent inside it to generate a file.

## Requirements
- Initialize a Git repository in `/home/user/myproject`.
- Create an empty `.amika/config.toml` file in the repository root.
- Create a sandbox named `test-sandbox` from the repository.
- Send a prompt to the agent in the sandbox to create a file named `hello.txt` containing the exact text `hello world`.

## Implementation Guide
1. Initialize a git repository in `/home/user/myproject`.
2. Create an empty `.amika/config.toml` in `/home/user/myproject`.
3. Run `amika sandbox create --name test-sandbox --git`.
4. Run `amika sandbox agent-send test-sandbox "create a file named hello.txt containing 'hello world'"`.

## Constraints
- Project path: /home/user/myproject
- Use `amika` CLI to create the sandbox and send the prompt.

## Integrations
- Amika