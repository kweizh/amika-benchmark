import os
import shutil
import pytest

PROJECT_DIR = "/home/user/app"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_process_script_exists():
    script_path = os.path.join(PROJECT_DIR, "process.sh")
    assert os.path.isfile(script_path), f"Script {script_path} does not exist."
