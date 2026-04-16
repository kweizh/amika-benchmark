import os
import subprocess
import json
import shutil
import pytest

SESSION_FILE = "/root/.config/amika/workos-session.json"

def test_amika_installed_and_executable():
    """Priority 1: Verify the CLI is installed and can run."""
    amika_path = shutil.which("amika")
    assert amika_path is not None, "amika binary not found in PATH."
    
    result = subprocess.run([amika_path, "--version"], capture_output=True, text=True)
    assert result.returncode == 0, f"'amika --version' failed: {result.stderr}"
    assert "amika" in result.stdout.lower() or "version" in result.stdout.lower(), \
        f"Expected version output, got: {result.stdout}"

def test_session_file_exists():
    """Priority 3: Verify the session file was created."""
    assert os.path.isfile(SESSION_FILE), f"Session file {SESSION_FILE} does not exist."

def test_session_file_content():
    """Priority 3: Verify the session file contains the correct JSON."""
    with open(SESSION_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            pytest.fail(f"Failed to parse {SESSION_FILE} as JSON: {e}")
    
    assert "access_token" in data, f"Expected 'access_token' key in {SESSION_FILE}."
    assert data["access_token"] == "mock_token_123", \
        f"Expected access_token to be 'mock_token_123', got: {data['access_token']}"
