# Materialize ls Output

## Background
Amika provides ephemeral containers for batch tasks via the `materialize` command. You can run a command in an isolated environment and copy the output back to the host.

## Requirements
- Execute the `ls -R` command in an ephemeral container using `amika materialize`.
- Copy the output directory from the container to the host at `/home/user/logs`.

## Constraints
- Project path: /home/user/myproject
- Log directory: /home/user/logs