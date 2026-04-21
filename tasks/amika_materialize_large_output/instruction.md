# Generate Large Output with Amika Materialize

## Background
Amika allows running ephemeral jobs using `amika materialize` to process data or collect context, saving the output back to the host machine. You need to write a Python script that generates a large JSON file and use `amika materialize` to execute it and save the output.

## Requirements
- Create a Python script `generate.py` that generates a file `report.json` containing a JSON array of 10,000 objects. Each object must have an `id` (integer from 1 to 10000) and a `timestamp` (string, e.g., ISO format).
- The script should save `report.json` in the current working directory (which will be `/home/amika/workspace` inside the container).
- Run `amika materialize` to execute this script and copy the output back to the host.
- Save the stdout of the `amika materialize` command to `output.log`.

## Implementation Guide
1. Change directory to `/home/user/project`.
2. Write the `generate.py` script to create `report.json` with 10,000 records.
3. Ensure `generate.py` is executable (`chmod +x generate.py`) and has `#!/usr/bin/env python3` at the top.
4. Run `amika materialize --script ./generate.py --destdir ./output > output.log 2>&1`.

## Constraints
- Project path: /home/user/project
- Log file: /home/user/project/output.log
- The output must be saved to the `./output` directory on the host, meaning `report.json` will be located at `/home/user/project/output/report.json`.