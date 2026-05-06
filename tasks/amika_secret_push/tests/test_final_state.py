import os
import subprocess
import pytest

def test_secret_pushed_via_cli():
    """Priority 1: Use Amika CLI to verify the secret is pushed."""
    result = subprocess.run(
        ["amika", "secret", "claude", "list"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"'amika secret claude list' failed: {result.stderr}"
    assert "mock-key" in result.stdout, f"Expected 'mock-key' in secret list, got: {result.stdout}"
    assert "api_key" in result.stdout, f"Expected 'api_key' in secret list, got: {result.stdout}"
