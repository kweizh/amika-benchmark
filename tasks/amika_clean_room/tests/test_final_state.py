import os
import subprocess
import json
import pytest

PROJECT_DIR = "/home/user/repo"

def test_sandbox_exists_and_on_branch():
    """Priority 1: Use Amika CLI to verify the sandbox state."""
    result = subprocess.run(
        ["amika", "sandbox", "ssh", "my-benchmark-box", "--", "git", "branch", "--show-current"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika sandbox ssh' failed: {result.stderr}"
    assert "benchmark-branch" in result.stdout, f"Expected sandbox to be on 'benchmark-branch', got: {result.stdout}"
