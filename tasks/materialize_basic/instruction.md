# Basic Materialization with Amika

## Background
Amika provides ephemeral jobs for data processing or context collection via the `amika materialize` command. It runs a command in a container and saves the output to the host.

## Requirements
- Use `amika materialize` to execute a command that generates a `report.json` file containing exactly `{"status": "success"}`.
- The output must be saved to the host directory `/workspace/output`.

## Implementation Guide
1. Ensure you are in the `/workspace` directory.
2. Run the `amika materialize` command. You can use a simple shell command to generate the JSON file.
3. For example: `amika materialize --cmd "mkdir -p /tmp/out && echo '{\"status\": \"success\"}' > /tmp/out/report.json && cp -r /tmp/out/* /output/" --destdir /workspace/output` (Note: adjust the paths according to how amika materialize handles the destination directory mapping, typically it might map the `--destdir` to a specific path in the container or you just write to the current directory and it syncs it. If the exact container path is unknown, you might need to test or use a command that writes to the working directory).

## Constraints
- Project path: /workspace
- Output file: /workspace/output/report.json
- You must use `amika materialize` to generate the file, not just create it directly on the host.