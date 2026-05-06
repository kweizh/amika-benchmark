# Non-Interactive SSH Command Execution

## Background
Amika allows executing commands non-interactively on a remote sandbox using `amika sandbox ssh`. This is useful for programmatic agent driving and automation.

## Requirements
- Create a remote sandbox named `test-box` from the current git repository.
- Execute a non-interactive command on `test-box` using `amika sandbox ssh` to create a file at `/home/user/hello.txt` containing the exact text `Hello from SSH`.
- Save the standard output or log of your ssh command to `/home/user/project/output.log`.

## Constraints
- Project path: /home/user/project
- Log file: /home/user/project/output.log
- You must use `amika sandbox create` and `amika sandbox ssh`.