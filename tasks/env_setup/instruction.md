# Amika Environment Setup for Node.js

## Background
Amika provides managed sandboxes for running coding agents. You need to configure a Node.js project to run as an Amika sandbox.

## Requirements
- Create an Amika configuration file for a Node.js project.
- The configuration must specify a setup script that installs Node.js dependencies.
- The configuration must expose a service named `frontend` on port 3000.

## Implementation Guide
1. Navigate to `/home/user/myproject`.
2. Create the file `.amika/config.toml`.
3. Add a `[lifecycle]` section with `setup_script = "npm install"`.
4. Add a `[services.frontend]` section mapping `port = 3000`.

## Constraints
- Project path: /home/user/myproject
- The project is already a git repository with a `package.json`.