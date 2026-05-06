# Execute Multi-line Scripts in Amika Sandbox via SSH Heredoc

## Background
Amika is a high-performance infrastructure for running AI coding agents in secure sandboxes. The `amika sandbox ssh` command allows you to execute non-interactive commands on a remote sandbox. When scripting complex automated pipelines, a bash heredoc is frequently used to send multi-line scripts to the sandbox.

## Requirements
- You have an empty Git project initialized at `/home/user/project`.
- Authenticate with Amika (the `AMIKA_API_KEY` environment variable is already set).
- Create a remote sandbox named `heredoc-sandbox` from the current Git repository using `amika sandbox create --name heredoc-sandbox --git --remote`.
- Use a single `amika sandbox ssh heredoc-sandbox -- bash` command with a heredoc (e.g. `<<EOF`) to execute a multi-line script inside the sandbox.
- The multi-line script must:
  1. Create a directory named `/workspace/test_dir`.
  2. Write the exact string `Heredoc execution successful` into `/workspace/test_dir/result.txt`.
  3. Define a variable inside the script (e.g. `TEST_VAR="passed"`) and append its value to the same file on a new line.

## Constraints
- Project path: /home/user/project
- You MUST properly escape guest-side variables (like `\$TEST_VAR`) so they are evaluated inside the remote sandbox, not on your host machine.

## Integrations
- Amika Cloud (API key provided via AMIKA_API_KEY)