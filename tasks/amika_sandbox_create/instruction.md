# Create an Amika Sandbox

## Background
You have a project initialized as a git repository at `/home/user/myproject`. Amika is a tool for building software factories and managed sandboxes. You need to create a local Amika sandbox for this project.

## Requirements
- Use the Amika CLI to create a local sandbox from the current git repository.
- The sandbox must be named `test-sandbox`.
- You must use the `--git` and `--connect` flags as specified in the task concept.

## Implementation Guide
1. Navigate to `/home/user/myproject`.
2. Create a basic `.amika/config.toml` file to initialize the repo if needed.
3. Run the command to create the sandbox: `amika sandbox create --name test-sandbox --git --connect --local`. (Note: use `--local` to run it locally without cloud authentication. Since `--connect` opens an interactive shell, you can pipe a command like `echo 'done'` or `exit` to it, or run it in the background).
4. Ensure the sandbox is successfully created.
5. Save the output or a success message to `/home/user/myproject/output.log`.

## Constraints
- Project path: /home/user/myproject
- Log file: /home/user/myproject/output.log