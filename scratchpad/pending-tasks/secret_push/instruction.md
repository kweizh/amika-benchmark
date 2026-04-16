# Store a Secret in Amika

## Background
You are using Amika, an infrastructure tool for building software factories. You need to store a secret API key so that it can be used by sandboxes created in your workspace.

## Requirements
- Use the Amika CLI to store a secret named `OPENAI_API_KEY`.
- The value of the secret must be `sk-1234567890abcdef`.

## Implementation Guide
1. Use the `amika secret push` command to store the secret.
2. Ensure the secret is stored successfully.

## Constraints
- Project path: /home/user/workspace
- The secret must be available for use in sandboxes.