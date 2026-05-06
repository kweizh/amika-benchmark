# Amika Git Workflow

## Background
Amika can create persistent remote sandboxes from a specific git branch. This is useful for clean-room benchmarking or isolated development.

## Requirements
- Create a remote sandbox named `git-sandbox` from the current git repository, specifically using the `feature` branch.
- Use `amika sandbox ssh` to execute a command inside the sandbox that creates a new file named `hello.txt` containing the text `Hello Amika`, stages it, and commits it with the message `Add hello.txt`.
- Delete the sandbox without deleting its volumes.
- Create a new remote sandbox named `git-sandbox-restore` using the same git repository and branch.
- Verify that the commit persists in the new sandbox by checking the git log.

## Constraints
- Project path: /home/user/test-repo
- The repository is already initialized at `/home/user/test-repo` with a `main` and `feature` branch.
- You must use `amika sandbox create --name <name> --git --branch feature --remote` to create the sandboxes.
- You must use `amika sandbox ssh <name> -- <command>` to interact with the sandbox.
- Do not use `--delete-volumes` when deleting the first sandbox.