# Fix Amika Port Collision

## Background
You have an Amika project at `/home/user/myproject`. The `.amika/config.toml` defines two services (`frontend` and `api`), but both are mistakenly configured to map to the same host port (3000). This causes a port collision when creating a sandbox.

## Requirements
- Identify the port collision in `/home/user/myproject/.amika/config.toml`.
- Change the `api` service to map to host port 3001 instead of 3000.
- Ensure the `frontend` service remains mapped to host port 3000.

## Implementation Guide
1. Open `/home/user/myproject/.amika/config.toml`.
2. Locate the `[services.api]` section.
3. Change the port mapping so that it maps container port 8080 to host port 3001.
4. Save the file.

## Constraints
- Project path: /home/user/myproject
- The `frontend` service must remain on port 3000.
- The `api` service must be moved to port 3001.

## Integrations
- None