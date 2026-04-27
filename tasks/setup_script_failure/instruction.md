# Fix Amika Sandbox Setup Script

## Background
We have a Node.js project configured to run in an Amika sandbox. However, the sandbox creation fails because the `setup_script` in the repository configuration exits with a non-zero status. This prevents the container command from running.

## Requirements
- Identify the cause of the `setup_script` failure in the `.amika/config.toml` file.
- Fix the `setup_script` so that dependencies are installed correctly.
- Successfully create an Amika sandbox named `test-sandbox` from the current git repository.
- Ensure the sandbox is running and the web service is accessible.

## Constraints
- Project path: `/workspace/project`
- The repository is already initialized as a git repository.
- Do not change the start command or the port (3000) of the application.