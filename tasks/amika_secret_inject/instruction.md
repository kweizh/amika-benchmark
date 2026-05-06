# Inject Secrets into Amika Sandbox

## Background
Amika allows you to securely store API keys in the cloud and inject them into persistent sandboxes for agents to use.

## Requirements
- Push a mock Claude API key (`sk-ant-api03-mock-key`) into the Amika secret store as a `claude` secret of type `api_key`.
- Create a new remote sandbox named `secret-sandbox` from the current project directory and inject the `claude` secret into it.
- Use `amika sandbox ssh` to run a command inside the sandbox that outputs its environment variables, and save this output to `/home/user/project/env.txt`.

## Constraints
- Project path: `/home/user/project`
- Log file: `/home/user/project/env.txt`
- Ensure the project is initialized as a git repository before creating the sandbox, as remote sandboxes require it.