import os
import shutil
import subprocess

PROJECT_DIR = "/workspace/project"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_npm_binary_available():
    assert shutil.which("npm") is not None, "npm binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_git_repo_initialized():
    git_dir = os.path.join(PROJECT_DIR, ".git")
    assert os.path.isdir(git_dir), f"Git repository not initialized in {PROJECT_DIR}."

def test_package_json_exists():
    package_json_path = os.path.join(PROJECT_DIR, "package.json")
    assert os.path.isfile(package_json_path), f"package.json not found in {PROJECT_DIR}."

def test_amika_config_exists():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    assert os.path.isfile(config_path), f".amika/config.toml not found in {PROJECT_DIR}."

def test_setup_script_fails():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    with open(config_path) as f:
        content = f.read()
    assert "npm isntall" in content, "Expected failing setup_script 'npm isntall' in .amika/config.toml."
