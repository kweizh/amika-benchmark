import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"
SANDBOX_NAME = "heredoc-sandbox"
FILE_PATH = "/workspace/test_dir/result.txt"

def test_sandbox_exists_and_file_content_correct():
    """Priority 1: Use Amika CLI to verify the file content inside the sandbox."""
    result = subprocess.run(
        ["amika", "sandbox", "ssh", SANDBOX_NAME, "--", "cat", FILE_PATH],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, \
        f"'amika sandbox ssh' failed to read {FILE_PATH}: {result.stderr}"
    
    stdout = result.stdout
    assert "Heredoc execution successful" in stdout, \
        f"Expected 'Heredoc execution successful' in output, got: {stdout}"
    assert "passed" in stdout, \
        f"Expected 'passed' in output, got: {stdout}"

def test_sandbox_status():
    """Priority 1: Use Amika CLI to verify the sandbox exists."""
    result = subprocess.run(
        ["amika", "sandbox", "status", SANDBOX_NAME],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, \
        f"'amika sandbox status {SANDBOX_NAME}' failed: {result.stderr}"
