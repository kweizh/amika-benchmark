import os
import json
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"
MOCK_MCP_SCRIPT = os.path.join(PROJECT_DIR, "mock_mcp.py")
CONFIG_FILE = os.path.expanduser("~/.claude/.config.json")

def test_mock_mcp_script_exists():
    """Priority 3: Check if the mock MCP script exists."""
    assert os.path.isfile(MOCK_MCP_SCRIPT), f"Mock MCP script not found at {MOCK_MCP_SCRIPT}"

def test_config_file_exists_and_valid():
    """Priority 3: Check if the config file exists and contains the mock-mcp configuration."""
    assert os.path.isfile(CONFIG_FILE), f"Config file not found at {CONFIG_FILE}"
    
    with open(CONFIG_FILE) as f:
        try:
            config = json.load(f)
        except json.JSONDecodeError:
            pytest.fail(f"Config file {CONFIG_FILE} is not valid JSON")
            
    assert "mcpServers" in config, "Config missing 'mcpServers' key"
    assert "mock-mcp" in config["mcpServers"], "Config missing 'mock-mcp' in 'mcpServers'"

def test_mock_mcp_script_executable():
    """Priority 1: Check if the mock MCP script is executable and runs."""
    result = subprocess.run(
        ["python3", MOCK_MCP_SCRIPT],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"Mock MCP script failed to execute: {result.stderr}"
