import os
import subprocess
import pytest

LOG_FILE = "/home/user/project/env.txt"
MOCK_KEY = "sk-ant-api03-mock-key"

def test_log_file_exists():
    """Priority 3: Check if the log file was created."""
    assert os.path.isfile(LOG_FILE), f"Log file {LOG_FILE} not found."

def test_secret_injected():
    """Priority 3: Check the contents of the log file for the mock key."""
    with open(LOG_FILE, "r") as f:
        content = f.read()
    assert MOCK_KEY in content, f"Expected mock key {MOCK_KEY} in {LOG_FILE}."
