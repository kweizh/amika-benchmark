import os
import pytest

PROJECT_DIR = "/home/user/project"
SCRIPT_PATH = os.path.join(PROJECT_DIR, "run_agent.sh")

def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), f"Script not found at {SCRIPT_PATH}"

def test_script_is_executable():
    assert os.access(SCRIPT_PATH, os.X_OK), f"Script {SCRIPT_PATH} is not executable"

def test_script_contents():
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    
    assert "amika sandbox agent-send" in content, "Script does not contain 'amika sandbox agent-send'"
    assert "dev-sandbox" in content, "Script does not contain the sandbox name 'dev-sandbox'"
    assert "Please update the README.md with deployment instructions" in content, "Script does not contain the expected prompt"
