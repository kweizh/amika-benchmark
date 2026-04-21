import os
import shutil
import subprocess
import pytest

PROJECT_DIR = "/home/user/workspace"

def test_amika_binary_available():
    assert shutil.which("amika") is not None, "amika binary not found in PATH."

def test_workspace_exists():
    assert os.path.isdir(PROJECT_DIR), f"Workspace directory {PROJECT_DIR} does not exist."