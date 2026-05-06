import os
import pytest

SCRIPT_PATH = "/home/user/workspace/cleanup.sh"

def test_script_exists():
    assert os.path.isfile(SCRIPT_PATH), f"Script {SCRIPT_PATH} does not exist."

def test_script_is_executable():
    assert os.access(SCRIPT_PATH, os.X_OK), f"Script {SCRIPT_PATH} is not executable."

def test_script_contains_correct_command():
    with open(SCRIPT_PATH, "r") as f:
        content = f.read()
    
    assert "amika sandbox delete" in content, "The script must contain the 'amika sandbox delete' command."
    assert "--delete-volumes" in content, "The script must explicitly use the '--delete-volumes' flag."
    assert "orphaned-box" in content, "The script must specify 'orphaned-box' as the sandbox to delete."
