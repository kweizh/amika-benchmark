import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_directory_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_git_repo_initialized():
    git_dir = os.path.join(PROJECT_DIR, ".git")
    assert os.path.isdir(git_dir), f"Git repository not initialized in {PROJECT_DIR}."

def test_amika_config_exists():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    assert os.path.isfile(config_path), f"Amika config file {config_path} does not exist."

def test_initial_setup_script_fails():
    setup_script_path = os.path.join(PROJECT_DIR, "setup.sh")
    assert os.path.isfile(setup_script_path), f"Setup script {setup_script_path} does not exist."
    with open(setup_script_path) as f:
        content = f.read()
    assert "exit 1" in content, "Expected initial setup_script to contain a command that fails (e.g., 'exit 1')."
