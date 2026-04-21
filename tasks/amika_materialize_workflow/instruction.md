# Materialize Workflow with Amika

## Background
Amika provides a `materialize` command to run ephemeral jobs for data processing or context collection in a container, and save the output back to the host machine.

## Requirements
- Create a Python script named `generate_report.py` in `/home/user/workspace`.
- The script should generate a file named `report.json` containing `{"status": "success", "data": "materialized"}`.
- Use the `amika materialize` command to run this Python script in an ephemeral container.
- The generated `report.json` must be saved to `/home/user/workspace/output` on the host.

## Implementation Guide
1. Create the directory `/home/user/workspace` and `/home/user/workspace/output`.
2. Write the `generate_report.py` script to create `report.json` in its current working directory.
3. Run `amika materialize --cmd "python generate_report.py" --destdir /home/user/workspace/output` to execute the script and extract the output.

## Constraints
- Project path: /home/user/workspace
- Output directory: /home/user/workspace/output
- The file `/home/user/workspace/output/report.json` must exist and contain the exact JSON payload after execution.