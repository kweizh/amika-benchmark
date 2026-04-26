# Node.js Sandbox Setup Report

## Project Configuration
- Path: `/home/user/project`
- Config File: `.amika/config.toml`

## Config Content
```toml
setup_script = "npm install"

[services.web]
port = 3000
```

## Sandbox Creation
- Name: `node-sandbox`
- Command: `amika sandbox create --name node-sandbox --git --local --yes`

Note: The creation command was attempted but failed due to the absence of a Docker daemon in the current environment. However, the configuration and the command syntax are correct according to the requirements and CLI help.
