# Configure Mock MCP Server for Amika

## Background
Amika sandboxes can inject MCP servers into the agent's environment (e.g., `~/.claude/.config.json`). You need to set up a mock MCP server locally and configure it so an agent inside the sandbox can discover it.

## Requirements
1. Create a mock MCP server script at `/home/user/project/mock_mcp.py` that implements a simple tool (e.g., `get_mock_data` returning `{"status": "ok"}`).
2. Configure the Amika agent environment to use this MCP server by creating/updating the `~/.claude/.config.json` file to include the `mock-mcp` server pointing to the python script.

## Constraints
- Project path: /home/user/project
- The mock MCP server must be executable via `python3 /home/user/project/mock_mcp.py`.
- The configuration must be in `~/.claude/.config.json`.