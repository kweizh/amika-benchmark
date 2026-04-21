# Secret Resolution Precedence in Amika

## Background
Amika allows you to define environment variables in your `.amika/config.toml`. However, secrets stored in the Amika database take precedence over values defined in the TOML file. This task tests your ability to correctly override a TOML-defined environment variable using a DB-stored secret before creating a sandbox.

## Requirements
- Push a secret named `API_TOKEN` with the value `db_override_token` to the Amika secret store.
- Create a sandbox named `my-sandbox` from the git repository at `/home/user/myproject`.
- Verify that the sandbox environment correctly resolves `API_TOKEN` to `db_override_token`.

## Implementation Guide
1. Use `amika secret push API_TOKEN=db_override_token` to store the secret.
2. Change directory to `/home/user/myproject`.
3. Create the sandbox using `amika sandbox create --name my-sandbox --git`.
4. You can verify the secret is injected correctly by running `amika sandbox agent-send my-sandbox "echo \$API_TOKEN"`.

## Constraints
- Project path: /home/user/myproject
- The secret MUST be pushed before creating the sandbox.