# Fix SSH Heredoc Variable Escaping

## Background
You have a script `run_agent.sh` that creates a remote Amika sandbox and executes a multi-line bash script inside it using `amika sandbox ssh` with a heredoc. However, the script is currently failing to output the correct guest-side variable because `$AMIKA_AGENT_CWD` is being expanded on the host instead of inside the sandbox.

## Requirements
- Fix the `/home/user/workspace/run_agent.sh` script so that the `AMIKA_AGENT_CWD` environment variable is correctly evaluated inside the remote sandbox, not on the host.
- Ensure the script still outputs the text `CWD: <value of AMIKA_AGENT_CWD>` to the log file.

## Implementation Guide
1. Inspect `/home/user/workspace/run_agent.sh`.
2. Modify the script to properly escape the guest-side variable or quote the heredoc delimiter so that the host's shell does not expand `$AMIKA_AGENT_CWD` prematurely.
3. Run the script to verify it works and writes the correct guest-side path to `/home/user/workspace/output.log`.

## Constraints
- Project path: /home/user/workspace
- Log file: /home/user/workspace/output.log
- The script must use `amika sandbox ssh` to execute the command.

## Integrations
- Amika