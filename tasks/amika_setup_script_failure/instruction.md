# Fix Amika Setup Script Failure

## Background
Amika uses `.amika/config.toml` to define repository configuration, including a `setup_script` that runs during sandbox creation. If this script fails, the sandbox cannot be created.

## Requirements
- You have a git repository at `/home/user/myproject` with an Amika configuration.
- Creating a sandbox currently fails because the script `./setup.sh` referenced in `.amika/config.toml` exits with a non-zero status.
- Fix `./setup.sh` so that it executes successfully.
- Create an Amika sandbox named `test-sandbox` from the current git repository using the `ubuntu:24.04` image.

## Implementation Guide
1. Navigate to `/home/user/myproject`.
2. Fix the script `./setup.sh` (e.g., change `exit 1` to `exit 0` or remove the failing command).
3. Commit your changes to the git repository.
4. Run `amika sandbox create --name test-sandbox --git --local --image ubuntu:24.04 --yes`.

## Constraints
- Project path: `/home/user/myproject`
- The sandbox name must be exactly `test-sandbox`.
- You must use the `--local` flag when creating the sandbox.
- You must use the `--image ubuntu:24.04` flag to speed up creation.
- You must use the `--yes` flag to skip interactive prompts.