import os
import tomllib
import pytest

PROJECT_DIR = "/home/user/project"
CONFIG_FILE = os.path.join(PROJECT_DIR, ".amika/config.toml")

def test_config_file_exists():
    assert os.path.isfile(CONFIG_FILE), f"Config file not found at {CONFIG_FILE}"

def test_config_contents():
    with open(CONFIG_FILE, "rb") as f:
        config = tomllib.load(f)
    
    assert "lifecycle" in config, "Missing [lifecycle] section in config.toml"
    assert config["lifecycle"].get("setup_script") == "npm install", \
        f"Expected setup_script='npm install', got {config['lifecycle'].get('setup_script')}"
    
    assert "services" in config, "Missing [services] section in config.toml"
    
    assert "frontend" in config["services"], "Missing [services.frontend] section in config.toml"
    assert config["services"]["frontend"].get("port") == 3000, \
        f"Expected frontend port 3000, got {config['services']['frontend'].get('port')}"
    
    assert "api" in config["services"], "Missing [services.api] section in config.toml"
    assert config["services"]["api"].get("port") == 8000, \
        f"Expected api port 8000, got {config['services']['api'].get('port')}"
