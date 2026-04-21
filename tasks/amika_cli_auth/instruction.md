# Install and Authenticate Amika CLI

## Background
Amika is an infrastructure tool for building software factories. To use it, developers must first install the CLI and authenticate.

## Requirements
1. Install the Amika CLI using the official installation script.
2. Authenticate the CLI. Since this is a headless environment, you must simulate the WorkOS Device Authorization Flow by manually writing a mock session file.

## Implementation Guide
1. Run the installation script: `curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh`
2. Create the configuration directory: `mkdir -p /root/.config/amika`
3. Create the WorkOS session file at `/root/.config/amika/workos-session.json` with the exact content: `{"access_token": "mock_token_123"}`

## Constraints
- Project path: /home/user/project
- The session file must be valid JSON.