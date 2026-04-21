import os
import subprocess
import pytest

PROJECT_DIR = "/home/user/vibe_project"

def test_git_repository_initialized():
    assert os.path.isdir(os.path.join(PROJECT_DIR, ".git")), "Git repository not initialized in /home/user/vibe_project"

def test_amika_config_exists():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    assert os.path.isfile(config_path), f"Config file {config_path} does not exist."

def test_sandbox_created():
    result = subprocess.run(["amika", "sandbox", "list"], capture_output=True, text=True)
    assert result.returncode == 0, f"'amika sandbox list' failed: {result.stderr}"
    assert "vibe-session" in result.stdout, "Expected 'vibe-session' in sandbox list."
