import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"
CONFIG_FILE = os.path.join(PROJECT_DIR, ".amika/config.toml")

def test_secret_exists():
    """Priority 1: Use Amika CLI to verify the secret was pushed."""
    result = subprocess.run(
        ["amika", "secret", "list"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika secret list' failed: {result.stderr}"
    assert "OPENAI_API_KEY" in result.stdout, \
        f"Expected 'OPENAI_API_KEY' in secret list, got: {result.stdout}"

def test_sandbox_exists():
    """Priority 1: Use Amika CLI to verify the sandbox was created."""
    result = subprocess.run(
        ["amika", "sandbox", "list"],
        capture_output=True, text=True, cwd=PROJECT_DIR
    )
    assert result.returncode == 0, f"'amika sandbox list' failed: {result.stderr}"
    assert "secret-sandbox" in result.stdout, \
        f"Expected 'secret-sandbox' in sandbox list, got: {result.stdout}"

def test_config_file_contains_env_mapping():
    """Priority 3 fallback: basic file check for config.toml."""
    assert os.path.isfile(CONFIG_FILE), f"config.toml not found at {CONFIG_FILE}"
    
    with open(CONFIG_FILE, "r") as f:
        content = f.read()
    
    # Check for [env] section and the secret mapping
    assert "[env]" in content, "Expected '[env]' section in config.toml"
    assert "OPENAI_API_KEY" in content and "secret" in content, \
        "Expected 'OPENAI_API_KEY' to be mapped to a secret in config.toml"
