import os
import pytest

LOG_DIR = "/home/user/app/logs"
LOG_FILE = os.path.join(LOG_DIR, "output.log")

def test_log_dir_exists():
    """Priority 3 fallback: basic directory existence check."""
    assert os.path.isdir(LOG_DIR), f"Log directory {LOG_DIR} does not exist."

def test_log_file_exists():
    """Priority 3 fallback: basic file existence check."""
    assert os.path.isfile(LOG_FILE), f"Log file {LOG_FILE} does not exist."

def test_log_file_content():
    """Priority 3 fallback: file content check."""
    with open(LOG_FILE, "r") as f:
        content = f.read()
    assert "Processing complete" in content, f"Expected 'Processing complete' in {LOG_FILE}, got: {content}"
