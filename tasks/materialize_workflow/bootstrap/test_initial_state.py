import os
import shutil
import subprocess

WORKSPACE_DIR = "/home/user/workspace"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_workspace_directory_exists():
    assert os.path.isdir(WORKSPACE_DIR), f"Workspace directory {WORKSPACE_DIR} does not exist."
