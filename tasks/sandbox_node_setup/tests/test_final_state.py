import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"

def test_sandbox_is_running():
    result = subprocess.run(
        ["amika", "sandbox", "list"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"'amika sandbox list' failed: {result.stderr}"
    assert "node-sandbox" in result.stdout, f"Expected 'node-sandbox' in sandbox list, got: {result.stdout}"
    
    # Ideally we'd check if it's running, but just existing in the list is a good start
    # We can check if the line contains "Running" or "Started" depending on the CLI output
    # but the exact state string isn't strictly defined in the docs we saw, so we check existence.

def test_service_is_exposed():
    result = subprocess.run(
        ["amika", "service", "list", "--sandbox-name", "node-sandbox"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0, f"'amika service list' failed: {result.stderr}"
    assert "web" in result.stdout, f"Expected 'web' service in output, got: {result.stdout}"
    assert "3000" in result.stdout, f"Expected port '3000' in output, got: {result.stdout}"

def test_config_toml_exists_and_valid():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    assert os.path.isfile(config_path), f"config.toml not found at {config_path}"
    
    with open(config_path) as f:
        content = f.read()
    
    assert "setup_script" in content or "npm install" in content, "Expected setup_script for npm install in config.toml"
    assert "web" in content and "3000" in content, "Expected service 'web' with port 3000 in config.toml"
