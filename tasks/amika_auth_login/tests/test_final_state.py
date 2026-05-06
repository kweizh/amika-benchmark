import subprocess
import pytest

def test_amika_auth_status_via_cli():
    """Priority 1: Use Amika CLI to verify the authentication state."""
    result = subprocess.run(
        ["amika", "auth", "status"],
        capture_output=True, text=True, cwd="/home/user"
    )
    assert result.returncode == 0, \
        f"'amika auth status' failed: {result.stderr}"
    assert "Authenticated via stored API key" in result.stdout or "Authenticated via stored API key" in result.stderr, \
        f"Expected 'Authenticated via stored API key' in output, got stdout: {result.stdout}, stderr: {result.stderr}"
