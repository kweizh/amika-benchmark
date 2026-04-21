import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"
CONFIG_FILE = os.path.join(PROJECT_DIR, ".amika/config.toml")

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_config_file_exists():
    assert os.path.isfile(CONFIG_FILE), f"Config file {CONFIG_FILE} does not exist."

def test_initial_port_collision():
    with open(CONFIG_FILE, "r") as f:
        content = f.read()
    
    assert "[services.frontend]" in content, "Expected [services.frontend] in config.toml"
    assert "[services.api]" in content, "Expected [services.api] in config.toml"
    # We expect both to map to 3000 initially
    assert content.count("host_port = 3000") >= 2 or content.count("3000") >= 2, "Expected port collision on port 3000 in initial state."
