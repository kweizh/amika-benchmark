# Amika Materialize Logs

## Background
Amika provides materialization for running ephemeral containers for batch tasks. You can run a command and copy the output back to the host using `amika materialize`.

## Requirements
- You have a data processing script `process.sh` located at `/home/user/app/process.sh`.
- Run this script inside an ephemeral container using the `amika materialize` command.
- The script generates a log file at `/logs/output.log` inside the container.
- You must copy the `/logs` directory from the container back to the host at `/home/user/app/logs`.

## Constraints
- Project path: /home/user/app
- Log file: /home/user/app/logs/output.log