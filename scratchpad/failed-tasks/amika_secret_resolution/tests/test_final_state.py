import os
import subprocess
import pytest

def test_api_token_injected_correctly():
    """Priority 1: Use Amika CLI to run a command in the sandbox and verify output."""
    result = subprocess.run(
        ["amika", "sandbox", "agent-send", "my-sandbox", "echo $API_TOKEN"],
        capture_output=True, text=True, cwd="/home/user/myproject"
    )
    assert result.returncode == 0, \
        f"'amika sandbox agent-send' failed: {result.stderr}"
    assert "db_override_token" in result.stdout, \
        f"Expected 'db_override_token' in output, got: {result.stdout}"
