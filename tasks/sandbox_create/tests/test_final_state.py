import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"
LOG_FILE = os.path.join(PROJECT_DIR, "output.log")

def test_sandbox_created_via_cli():
    """Priority 1: Use Amika CLI to verify the sandbox exists locally."""
    # amika sandbox list --local might output a table or JSON.
    # We check if 'test-sandbox' is in the output.
    result = subprocess.run(
        ["amika", "sandbox", "list", "--local"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika sandbox list --local' failed: {result.stderr}"
    assert "test-sandbox" in result.stdout, f"Expected 'test-sandbox' in local sandboxes, got: {result.stdout}"

def test_log_file_exists():
    """Priority 3: Verify the log file exists."""
    assert os.path.isfile(LOG_FILE), f"Log file not found at {LOG_FILE}"
