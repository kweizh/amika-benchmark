import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/myproject"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_amika_config_exists():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    assert os.path.isfile(config_path), f"Config file {config_path} does not exist."

def test_frontend_env_exists():
    env_path = os.path.join(PROJECT_DIR, "frontend", ".env")
    assert os.path.isfile(env_path), f"Frontend .env file {env_path} does not exist."

def test_initial_config_has_port_conflict():
    config_path = os.path.join(PROJECT_DIR, ".amika", "config.toml")
    with open(config_path) as f:
        content = f.read()
    assert "3000:3000" in content, "Expected frontend service to map to port 3000 in config.toml."
    assert "3000:8080" in content, "Expected api service to map to port 3000 in config.toml initially."
    assert "DB_PASSWORD" not in content, "Expected DB_PASSWORD to be missing from config.toml initially."

def test_initial_frontend_env_has_conflict_url():
    env_path = os.path.join(PROJECT_DIR, "frontend", ".env")
    with open(env_path) as f:
        content = f.read()
    assert "REACT_APP_API_URL=http://localhost:3000" in content, "Expected frontend .env to initially point to http://localhost:3000."