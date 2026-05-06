# Amika Credential Shadowing

## Background
You have a wrapper script `/home/user/project/amika_wrapper.sh` that executes `amika` commands.
Amika's default authentication precedence prioritizes the `AMIKA_API_KEY` environment variable over a stored browser session (`workos-session.json`).
However, in our development environment, developers often have a global `AMIKA_API_KEY` set for read-only access, but we want them to use their personal browser session if they have logged in.

## Requirements
Modify `/home/user/project/amika_wrapper.sh` so that it forces the `amika` CLI to prioritize the browser session over the `AMIKA_API_KEY` environment variable.
Specifically, if a browser session file exists at `${XDG_STATE_HOME:-$HOME/.local/state}/amika/workos-session.json`, the script must ensure that `amika` ignores the `AMIKA_API_KEY` environment variable. If no browser session exists, `amika` should behave normally (using `AMIKA_API_KEY` if present).

The script takes any `amika` command as arguments and executes it. For example:
`./amika_wrapper.sh auth status`

## Constraints
- Project path: `/home/user/project`
- The wrapper script is `/home/user/project/amika_wrapper.sh`
- You must handle the `XDG_STATE_HOME` environment variable if it is set, otherwise default to `$HOME/.local/state`.

## Integrations
None