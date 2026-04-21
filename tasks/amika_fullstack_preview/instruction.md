# Amika Full-Stack Preview Configuration

## Background
Amika allows declaring services in `.amika/config.toml` to map container ports to host ports. You have a full-stack project at `/home/user/project` that needs to expose a frontend and an API.

## Requirements
- Initialize Amika configuration in `/home/user/project`.
- Configure a `frontend` service that maps container port 3000 to host port 3000.
- Configure an `api` service that maps container port 8000 to host port 8000.
- Set the lifecycle setup script to `npm install`.

## Implementation Guide
1. Create the `.amika/config.toml` file in `/home/user/project`.
2. Add a `[lifecycle]` section with `setup_script = "npm install"`.
3. Add a `[services.frontend]` section with `port = 3000`.
4. Add a `[services.api]` section with `port = 8000`.

## Constraints
- Project path: /home/user/project