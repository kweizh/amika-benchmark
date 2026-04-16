import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_config_toml_exists():
    config_path = os.path.join(PROJECT_DIR, ".amika/config.toml")
    assert os.path.isfile(config_path), f"Config file {config_path} does not exist."

def test_initial_api_token_in_config():
    config_path = os.path.join(PROJECT_DIR, ".amika/config.toml")
    with open(config_path) as f:
        content = f.read()
    assert "API_TOKEN" in content, "Expected API_TOKEN to be defined in .amika/config.toml."
