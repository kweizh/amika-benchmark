import os
import pytest
import tomllib

PROJECT_DIR = "/home/user/myproject"
CONFIG_FILE = os.path.join(PROJECT_DIR, ".amika", "config.toml")

def test_config_file_exists():
    assert os.path.isfile(CONFIG_FILE), f"Amika configuration file {CONFIG_FILE} does not exist."

def test_config_lifecycle_setup_script():
    with open(CONFIG_FILE, "rb") as f:
        try:
            config = tomllib.load(f)
        except Exception as e:
            pytest.fail(f"Failed to parse TOML configuration: {e}")
            
    lifecycle = config.get("lifecycle", {})
    setup_script = lifecycle.get("setup_script")
    assert setup_script == "npm install", \
        f"Expected [lifecycle] setup_script to be 'npm install', got: {setup_script}"

def test_config_services_frontend_port():
    with open(CONFIG_FILE, "rb") as f:
        try:
            config = tomllib.load(f)
        except Exception as e:
            pytest.fail(f"Failed to parse TOML configuration: {e}")
            
    services = config.get("services", {})
    frontend = services.get("frontend", {})
    port = frontend.get("port")
    assert port == 3000, \
        f"Expected [services.frontend] port to be 3000, got: {port}"
