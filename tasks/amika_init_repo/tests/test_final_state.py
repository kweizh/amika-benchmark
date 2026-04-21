import os
import pytest

PROJECT_DIR = "/home/user/myproject"
CONFIG_FILE = os.path.join(PROJECT_DIR, ".amika", "config.toml")

def test_config_file_exists():
    assert os.path.isfile(CONFIG_FILE), f"config.toml not found at {CONFIG_FILE}"

def test_config_file_content():
    with open(CONFIG_FILE, "r") as f:
        content = f.read()
    
    assert "[lifecycle]" in content, "Expected '[lifecycle]' section in config.toml"
    assert "setup_script" in content and "npm install" in content, "Expected 'setup_script = \"npm install\"' in config.toml"
