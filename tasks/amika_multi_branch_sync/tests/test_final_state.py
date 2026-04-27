import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"
LOG_FILE = os.path.join(PROJECT_DIR, "output.log")

def test_sandbox_created():
    """Priority 1: Use Amika CLI to verify the sandbox exists."""
    result = subprocess.run(
        ["amika", "sandbox", "list", "--local"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"'amika sandbox list --local' failed: {result.stderr}"
    assert "test-sandbox" in result.stdout, f"Expected 'test-sandbox' in local sandboxes, got: {result.stdout}"

def test_output_log_exists_and_content():
    """Priority 3 fallback: basic file existence and content check."""
    assert os.path.isfile(LOG_FILE), f"Log file not found at {LOG_FILE}"
    with open(LOG_FILE, "r") as f:
        content = f.read().strip()
    assert content == "feature-value", f"Expected log file to contain exactly 'feature-value', got: '{content}'"
