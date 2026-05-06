# Amika Sandbox Volume Cleanup

## Background
Deleting a sandbox in Amika does not delete its `rwcopy` volumes by default, which can lead to orphaned cloud volumes. You need to write a script that deletes a sandbox and explicitly removes its volumes.

## Requirements
- Create a bash script named `cleanup.sh`.
- The script must use the Amika CLI to delete a sandbox named `orphaned-box`.
- The command must explicitly delete the sandbox's volumes.
- Make the script executable.

## Constraints
- Project path: `/home/user/workspace`
- The script must be located at `/home/user/workspace/cleanup.sh`.
- Do not execute the script, as the environment does not have a valid Amika API key. Just create it.