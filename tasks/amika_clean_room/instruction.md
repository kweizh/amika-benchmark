# Amika Clean-Room Sandbox

## Background
Amika provides persistent Docker-backed environments called sandboxes. For clean-room benchmarking, you can create a sandbox from a specific git branch to ensure an isolated state.

## Requirements
- You have a git repository initialized at `/home/user/repo` with a branch named `benchmark-branch`.
- Create a new remote Amika sandbox named `my-benchmark-box` from the current git repository.
- The sandbox must be created specifically from the `benchmark-branch` branch.

## Constraints
- Project path: /home/user/repo
- The `AMIKA_API_KEY` environment variable is already set.
- You must use the Amika CLI.