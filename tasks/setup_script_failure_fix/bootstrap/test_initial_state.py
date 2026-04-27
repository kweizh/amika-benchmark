import os
import shutil
import pytest

PROJECT_DIR = "/home/user/project"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_directory_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_config_toml_exists():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    assert os.path.isfile(config_path), f"Config file {config_path} does not exist."

def test_setup_script_exists():
    script_path = os.path.join(PROJECT_DIR, ".amika", "setup.sh")
    assert os.path.isfile(script_path), f"Setup script {script_path} does not exist."
