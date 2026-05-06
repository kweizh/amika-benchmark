import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/project"
WRAPPER_SCRIPT = os.path.join(PROJECT_DIR, "amika_wrapper.sh")

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_project_dir_exists():
    assert os.path.isdir(PROJECT_DIR), f"Project directory {PROJECT_DIR} does not exist."

def test_wrapper_script_exists():
    assert os.path.isfile(WRAPPER_SCRIPT), f"Wrapper script {WRAPPER_SCRIPT} does not exist."
    assert os.access(WRAPPER_SCRIPT, os.X_OK), f"Wrapper script {WRAPPER_SCRIPT} is not executable."
