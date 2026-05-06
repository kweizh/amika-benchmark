# Configure Amika Repository

## Background
You have a Node.js web project at `/home/user/myproject`. You need to create an Amika repository configuration file to define a setup script, environment variables, and a web service.

## Requirements
- Create an `.amika/config.toml` file in the project root.
- Configure a setup script pointing to `scripts/setup.sh`.
- Add an environment variable `NODE_ENV` set to `"development"`.
- Define a service named `web` running on port 3000 with the `http` URL scheme.
- Set the sandbox preset to `"coder"`.

## Constraints
- Project path: /home/user/myproject
