### 1. Library Overview
*   **Description**: Amika is infrastructure for building "software factories." It provides managed, multiplayer sandboxes pre-loaded with coding agents (like Claude Code, Codex, and OpenCode) and tools for autonomous background code-generation jobs.
*   **Ecosystem Role**: It acts as the execution layer for AI coding agents, providing a consistent, reproducible environment (Docker-based) that bridges local development and cloud-based automation.
*   **Project Setup**:
    1.  Install CLI: `curl -fsSL https://raw.githubusercontent.com/gofixpoint/amika/main/install.sh | sh`
    2.  Authenticate: `amika auth login`
    3.  Initialize Repo: Create a `.amika/config.toml` at the root of a git repository.
    4.  Create Sandbox: `amika sandbox create --git --connect`
### 2. Core Primitives & APIs
*   **Sandboxes**: Persistent, Docker-backed environments for running code and agents.
    *   `amika sandbox create --name <name> --git`: Creates a sandbox from the current git repo.
    *   `amika sandbox agent-send <name> "<prompt>"`: Sends a prompt directly to an agent (e.g., Claude) inside the sandbox.
    *   [CLI Reference](https://docs.amika.dev/reference/cli-reference)
*   **Repository Configuration (`.amika/config.toml`)**: Declarative configuration for sandboxes.
    *   `[lifecycle]`: Defines `setup_script` for environment initialization.
    *   `[env]`: Manages environment variables and secret references (`{ secret = "key" }`).
    *   `[services.<name>]`: Maps container ports to host ports/URLs.
    *   [Config Reference](https://docs.amika.dev/reference/config-toml)
*   **Materialization**: Ephemeral jobs for data processing or context collection.
    *   `amika materialize --cmd "<command>" --destdir <path>`: Runs a command in a container and saves output to the host.
*   **Secrets**: Remote encrypted store for API keys and tokens.
    *   `amika secret push <KEY>=<VALUE>`: Stores a secret for use in sandboxes.
### 3. Real-World Use Cases & Templates
*   **Parallel Code-Gen**: Spinning up multiple sandboxes (e.g., `task-1`, `task-2`) to run agents on different branches or features simultaneously.
*   **Multiplayer "Vibe Coding"**: Sharing a sandbox URL/SSH access with collaborators for real-time human-agent pair programming.
*   **Automated PR Reviews**: Using `amika materialize` with an agent CLI to analyze a diff and output a review report.
*   **Full-Stack Preview**: Declaring `frontend` and `api` services in `config.toml` to automatically expose a web app for testing.
### 4. Developer Friction Points
*   **Setup Script Failures**: If the `setup_script` exits with a non-zero status, the container command fails to run, which can be hard to debug without connecting manually. ([Docs](https://docs.amika.dev/guides/repository-configuration#lifecycle-setup-script))
*   **Secret Resolution Precedence**: Understanding that secrets must be pushed *before* sandbox creation and that DB-stored secrets override TOML-defined ones can be confusing for new users. ([Docs](https://docs.amika.dev/guides/repository-configuration#configuration-resolution))
*   **Mount Modes (`rwcopy` vs `rw`)**: Users may be surprised when changes in a `rwcopy` mount (the default) do not sync back to their host machine. ([Docs](https://docs.amika.dev/reference/cli-reference#mount-modes))
*   **Port Mapping Collisions**: Amika attempts a "direct mirror" of ports; if the host port is taken, it falls back to a random port, which may break hardcoded service URLs if not using the generated `http://localhost:<port>` links. ([Docs](https://docs.amika.dev/guides/services#port-resolution))
### 5. Evaluation Ideas
*   **Environment Setup**: Create a `.amika/config.toml` for a Node.js project that installs dependencies via a setup script and exposes port 3000.
*   **Secret Injection**: Configure a sandbox to use a secret named `OPENAI_API_KEY` and verify it is available in the environment.
*   **Parallel Agents**: Write a script to create two sandboxes, run `amika sandbox agent-send` on both with different tasks, and wait for completion.
*   **Materialize Workflow**: Use `amika materialize` to run a Python script that generates a `report.json` and ensure the file is correctly copied to the host.
*   **Service Debugging**: Identify and fix a port conflict in a multi-service configuration where two services try to bind to the same host port.
*   **Multi-Branch Sync**: Create a sandbox from a specific git branch and verify that the `.amika/config.toml` settings from that branch are applied.
### 6. Sources
1.  [Amika Introduction](https://docs.amika.dev/): Core purpose and high-level features.
2.  [CLI Reference](https://docs.amika.dev/reference/cli-reference): Detailed command list and flags.
3.  [config.toml Reference](https://docs.amika.dev/reference/config-toml): Exhaustive list of configuration fields.
4.  [Repository Configuration Guide](https://docs.amika.dev/guides/repository-configuration): Explanation of how settings are resolved from TOML and DB.
5.  [Sandbox Configuration Guide](https://docs.amika.dev/guides/sandbox-configuration): Details on setup scripts, git cloning, and credential mounting.
6.  [Services Guide](https://docs.amika.dev/guides/services): How to declare and resolve network services.
7.  [Presets Guide](https://docs.amika.dev/guides/presets): Overview of pre-installed tools and agent CLIs in images.
