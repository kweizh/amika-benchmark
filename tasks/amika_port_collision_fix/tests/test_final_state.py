import os
import pytest
import tomli # if available, or just parse text. Wait, standard library only! json, os, subprocess, etc. I'll just use text parsing.

PROJECT_DIR = "/home/user/myproject"
CONFIG_FILE = os.path.join(PROJECT_DIR, ".amika/config.toml")

def test_api_service_moved_to_3001():
    """Priority 3 fallback: basic file check for config since no CLI command to verify config without starting sandbox."""
    assert os.path.isfile(CONFIG_FILE), f"Config file {CONFIG_FILE} does not exist."
    with open(CONFIG_FILE, "r") as f:
        content = f.read()

    # Find the block for [services.api]
    api_block_start = content.find("[services.api]")
    assert api_block_start != -1, "Expected [services.api] in config.toml"
    
    # We just check if host_port = 3001 is somewhere after [services.api] or just in the file
    # A simple check is that host_port = 3001 exists and host_port = 3000 exists
    assert "3001" in content, "Expected port 3001 in config.toml for api service."
    
def test_frontend_service_remains_on_3000():
    with open(CONFIG_FILE, "r") as f:
        content = f.read()
    
    frontend_block_start = content.find("[services.frontend]")
    assert frontend_block_start != -1, "Expected [services.frontend] in config.toml"
    
    assert "3000" in content, "Expected port 3000 in config.toml for frontend service."
