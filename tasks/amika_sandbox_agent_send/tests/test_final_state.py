import os
import subprocess
import pytest

def test_sandbox_exists_via_cli():
    """Priority 1: Use Amika CLI to verify the sandbox state."""
    result = subprocess.run(
        ["amika", "sandbox", "list"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"'amika sandbox list' failed: {result.stderr}"
    assert "agent-box" in result.stdout, f"Expected 'agent-box' in 'amika sandbox list' output, got: {result.stdout}"

def test_file_created_in_sandbox_via_cli():
    """Priority 1: Use Amika CLI to run a command in the sandbox and verify output."""
    result = subprocess.run(
        ["amika", "sandbox", "ssh", "agent-box", "--", "cat", "hello.txt"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"'amika sandbox ssh' failed: {result.stderr}"
    assert "Hello, Amika!" in result.stdout, f"Expected 'Hello, Amika!' in output, got: {result.stdout}"
