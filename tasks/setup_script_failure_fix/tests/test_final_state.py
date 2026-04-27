import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_setup_script_is_executable():
    """Priority 3: Check if setup.sh is executable."""
    script_path = os.path.join(PROJECT_DIR, ".amika", "setup.sh")
    assert os.access(script_path, os.X_OK), f"Setup script {script_path} is not executable."

def test_amika_sandbox_create_succeeds():
    """Priority 1: Run amika sandbox create to validate the setup script executes successfully."""
    # Run the sandbox creation locally to test the setup script
    result = subprocess.run(
        ["amika", "sandbox", "create", "--name", "test-sandbox", "--git", "--local"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    
    assert result.returncode == 0, \
        f"'amika sandbox create' failed with exit code {result.returncode}.\nStdout: {result.stdout}\nStderr: {result.stderr}"

def test_amika_sandbox_list_contains_test_sandbox():
    """Priority 1: Verify the sandbox was created by checking the list."""
    result = subprocess.run(
        ["amika", "sandbox", "list", "--local"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    
    assert result.returncode == 0, \
        f"'amika sandbox list' failed: {result.stderr}"
    assert "test-sandbox" in result.stdout, \
        f"Expected 'test-sandbox' in local sandboxes list, got: {result.stdout}"
