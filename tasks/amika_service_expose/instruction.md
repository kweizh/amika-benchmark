# Expose a Web Service with Amika

## Background
You have an Amika project at `/home/user/project` with a Node.js web server that listens on port 8080. You need to declare a web service in `.amika/config.toml`, start it in a remote sandbox, and verify the public URL is accessible.

## Requirements
- Initialize an Amika configuration for the project in `/home/user/project/`.
- Declare a web service in `.amika/config.toml` that maps port 8080.
- Start the Amika remote sandbox named `service-sandbox` and ensure the service is exposed.
- Write the public URL of the exposed service to `/home/user/project/output.log`.

## Constraints
- Project path: /home/user/project
- Log file: /home/user/project/output.log
- Use Amika CLI to create and manage the sandbox.
- The sandbox must be named `service-sandbox`.

## Integrations
- Amika Cloud