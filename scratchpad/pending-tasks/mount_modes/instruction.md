# Amika Mount Modes

## Background
You are working on a local project at `/home/user/myproject`. You want to use Amika to run a sandbox environment, but you need files generated inside the sandbox to sync back to your host machine. By default, Amika's `--mount` flag uses a `rwcopy` mode, which copies files into a volume but does not sync changes back.

## Requirements
- Create an Amika sandbox named `dev-sandbox`.
- Mount the host directory `/home/user/myproject` to `/workspace/myproject` inside the container.
- Ensure the mount mode is set to read-write (`rw`) so that changes sync back to the host.
- Inside the sandbox, create a file named `output.txt` in `/workspace/myproject` with the content `hello from sandbox`.

## Implementation Guide
1. Run the `amika sandbox create` command with the appropriate `--name` and `--mount` flags, explicitly specifying the `rw` mode.
2. Run a command inside the sandbox using `amika sandbox ssh dev-sandbox -- "echo 'hello from sandbox' > /workspace/myproject/output.txt"`.

## Constraints
- Project path: `/home/user/myproject`
- The sandbox must be named `dev-sandbox`.
- The host directory must be mounted to `/workspace/myproject`.
- The mount mode must be `rw`.