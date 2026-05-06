import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"
LOG_FILE = os.path.join(PROJECT_DIR, "output.log")

def test_log_file_exists():
    """Priority 3: Check if the log file was created."""
    assert os.path.isfile(LOG_FILE), f"Log file not found at {LOG_FILE}"

def test_ssh_command_execution():
    """Priority 1: Use amika CLI to verify the file was created on the remote sandbox."""
    result = subprocess.run(
        ["amika", "sandbox", "ssh", "test-box", "--", "cat", "/home/user/hello.txt"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika sandbox ssh' failed: {result.stderr}"
    assert "Hello from SSH" in result.stdout, \
        f"Expected 'Hello from SSH' in output, got: {result.stdout}"
