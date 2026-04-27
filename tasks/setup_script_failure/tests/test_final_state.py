import os
import subprocess
import json
import urllib.request
import time
import pytest

PROJECT_DIR = "/workspace/project"

def test_setup_script_fixed():
    """Priority 3: Check if the setup_script typo was fixed in the config file."""
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    with open(config_path) as f:
        content = f.read()
    assert "npm install" in content, "Expected 'npm install' in .amika/config.toml setup_script, but it wasn't fixed."
    assert "npm isntall" not in content, "The typo 'npm isntall' is still present in .amika/config.toml."

def test_sandbox_is_running():
    """Priority 1: Use Amika CLI to verify the sandbox state."""
    # Run amika sandbox status to get the status of test-sandbox
    result = subprocess.run(
        ["amika", "sandbox", "status", "test-sandbox", "--json"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    # Note: If --json is not supported, we can fallback to checking stdout text.
    # But assuming it outputs JSON or at least text we can parse.
    # For safety, let's just check the text output if it's not strictly json.
    assert result.returncode == 0, f"'amika sandbox status' failed: {result.stderr}"
    
    # We expect the status to indicate it's running
    assert "running" in result.stdout.lower() or "ready" in result.stdout.lower(), \
        f"Expected sandbox 'test-sandbox' to be running. Output: {result.stdout}"

def test_service_accessible():
    """Priority 3: Verify the service is accessible on the mapped port."""
    # Since amika connects the service to localhost:3000, we can try to fetch it.
    # We will retry a few times to allow the service to start up in the sandbox.
    max_retries = 5
    success = False
    for _ in range(max_retries):
        try:
            response = urllib.request.urlopen("http://localhost:3000", timeout=5)
            if response.getcode() == 200:
                success = True
                break
        except Exception:
            pass
        time.sleep(2)
    
    assert success, "Failed to reach the web service on http://localhost:3000. It may not be running or the port mapping failed."
