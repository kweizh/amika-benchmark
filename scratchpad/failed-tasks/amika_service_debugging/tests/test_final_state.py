import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"

def test_amika_config_port_conflict_resolved():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    assert os.path.isfile(config_path), f"Config file {config_path} does not exist."
    with open(config_path) as f:
        content = f.read()
    
    # frontend should still be 3000
    assert "3000:3000" in content, "Expected frontend service to remain mapped to port 3000 in config.toml."
    # api should be updated to 3001
    assert "3001:8080" in content, "Expected api service to be mapped to port 3001 in config.toml."
    # old mapping should not exist
    assert "3000:8080" not in content, "Expected old api port mapping (3000:8080) to be removed."

def test_amika_config_db_password_added():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    with open(config_path) as f:
        content = f.read()
    
    assert "DB_PASSWORD" in content and "secret123" in content, "Expected DB_PASSWORD = \"secret123\" to be added to the [env] section of config.toml."

def test_frontend_env_updated():
    env_path = os.path.join(PROJECT_DIR, "frontend", ".env")
    assert os.path.isfile(env_path), f"Frontend .env file {env_path} does not exist."
    with open(env_path) as f:
        content = f.read()
    
    assert "REACT_APP_API_URL=http://localhost:3001" in content, "Expected frontend .env to point to http://localhost:3001."
    assert "http://localhost:3000" not in content, "Expected old API URL (http://localhost:3000) to be removed from frontend .env."