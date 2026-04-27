# Node.js Sandbox Environment Setup

## Background
Amika uses a declarative `.amika/config.toml` file to configure repository-specific sandbox settings, such as setup scripts and exposed services.

## Requirements
You need to configure and launch a sandbox for a Node.js project.
1. There is a Node.js project at `/home/user/project`.
2. Create an `.amika/config.toml` file in the project root.
3. The config must define a `setup_script` that runs `npm install`.
4. The config must declare a service named `web` that exposes container port `3000` to the host.
5. Create the sandbox named `node-sandbox` from the git repository using the Amika CLI.

## Constraints
- Project path: /home/user/project
- Sandbox name: `node-sandbox`
- The sandbox must be created with the `--git` flag.