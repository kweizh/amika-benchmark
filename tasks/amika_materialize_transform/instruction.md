# Amika Materialize Data Transformation

## Background
You have the Amika CLI installed and authenticated. You need to use Amika's materialize feature to run a data transformation script in an ephemeral container and copy the results back to the host.

## Requirements
- Create a Python script `transform.py` in `/home/user/project` that reads a JSON file `input.json` containing an array of numbers, squares each number, and writes the result to `output.json`.
- Create `input.json` with the content `[1, 2, 3, 4, 5]` in the same directory.
- Use `amika materialize` to execute `python transform.py` in an ephemeral container.
- Ensure the generated `output.json` is copied back to the host directory `/home/user/project/results`.

## Constraints
- Project path: `/home/user/project`
- The script must run via `amika materialize`.
- The output must be saved to `/home/user/project/results/output.json` on the host.