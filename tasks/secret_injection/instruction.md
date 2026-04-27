# Amika Secret Injection

## Background
Amika sandboxes can have secrets injected into their environment from a remote encrypted store. This is useful for providing API keys and tokens securely.

## Requirements
- Initialize an amika repository in `/home/user/myproject`.
- Push a secret named `OPENAI_API_KEY` with the value `sk-test-secret-12345` using `amika secret push`.
- Configure the `.amika/config.toml` to map the `OPENAI_API_KEY` secret to the environment variable `OPENAI_API_KEY`.
- Create a sandbox named `secret-sandbox` from the git repository using `amika sandbox create`.

## Constraints
- Project path: `/home/user/myproject`